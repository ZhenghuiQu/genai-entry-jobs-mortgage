"""Phase A only: standard-library audit of cached metadata and DE aggregates.

Never opens PUMS/HMDA microdata, networks, or the primary mapping for writing.
Run: .venv/bin/python scripts/phase3/audit_cached_occupations.py
"""
import ast
import collections
import csv
import hashlib
import json
from pathlib import Path
import re
import resource
import shutil
import time
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'results/feasibility'
DATA = ROOT / 'data/feasibility'
NS = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
BLS = 'https://www.bls.gov/soc/2018/soc_structure_2018.pdf'
ONET = 'https://www.onetcenter.org/taxonomy/2019/soc/2019_to_SOC_Crosswalk.xlsx'
CENSUS = 'https://www2.census.gov/programs-surveys/demo/guidance/industry-occupation/2018-ACS-PUMS-and-2018-SIPP-Public-Use-Occupation-Code-List.xlsx'
RATING = 'https://github.com/openai/GPTs-are-GPTs/blob/0471612fef3cc22b74fb884d27bff9dbd3770582/data/occ_level.csv'


def rows(path):
    assert path.stat().st_size < 2 * 1024**2, f'Only compact inputs allowed: {path.name}'
    with path.open(newline='') as stream:
        return list(csv.DictReader(stream))


def workbook_rows(path, sheet_index=1):
    # XML parsing avoids importing pandas/openpyxl or rebuilding the environment.
    with zipfile.ZipFile(path) as z:
        assert sum(i.file_size for i in z.infolist()) < 8 * 1024**2
        shared = ET.fromstring(z.read('xl/sharedStrings.xml'))
        strings = [''.join(s.itertext()) for s in shared]
        sheet = ET.fromstring(z.read(f'xl/worksheets/sheet{sheet_index}.xml'))
        for row in sheet.findall('.//m:sheetData/m:row', NS):
            values = {}
            for cell in row.findall('m:c', NS):
                value = cell.find('m:v', NS)
                text = value.text if value is not None else ''
                if cell.attrib.get('t') == 's':
                    text = strings[int(text)]
                elif cell.attrib.get('t') == 'inlineStr':
                    text = ''.join(cell.find('m:is', NS).itertext())
                values[re.sub(r'\d', '', cell.attrib['r'])] = text.strip()
            yield int(row.attrib['r']), values


def main():
    started = time.monotonic()
    assert shutil.disk_usage(ROOT).free > 48 * 1024**3 + 5 * 1024**2, 'Preserve existing storage safeguard'
    inputs = [DATA / n for n in ['exposure.csv', 'onet_soc2018.xlsx', 'census_2018_pums.xlsx', 'census_2018_soc.xlsx', 'phase2_pums_occupation_aggregates.csv']]
    inputs += [OUT / n for n in ['occupation_mapping_final.csv', 'soc2018_official_hierarchy.csv', 'occupation_mapping_diagnostic.csv', 'occupation_unmatched_groups.csv', 'occupation_ambiguous_groups.csv', 'occupation_weighted_coverage.csv', 'unmatched_employment_by_group.csv', 'exposure_coverage_by_geography.csv', 'phase2_unrated_onet_members.csv']]
    inputs += [ROOT / 'audit/phase3_onet_non_data_codes.json']
    hashes = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
    original_receipts = {}
    with (OUT / 'source_manifest.jsonl').open() as stream:
        for line in stream:
            record = json.loads(line)
            if record.get('id') in {p.name for p in inputs[:4]} and record.get('sha256'):
                original_receipts[record['id']] = record['sha256']
    for path in inputs[:4]:
        assert hashes[str(path.relative_to(ROOT))] == original_receipts[path.name], 'Original acquisition hash changed'
    ratings = rows(DATA / 'exposure.csv')
    score = {r['O*NET-SOC Code']: float(r['dv_rating_beta']) for r in ratings}
    assert len(score) == len(ratings) == 923 and all(0 <= v <= 1 for v in score.values())
    children = collections.defaultdict(list)
    for _, r in workbook_rows(DATA / 'onet_soc2018.xlsx'):
        if re.fullmatch(r'\d{2}-\d{4}\.\d{2}', r.get('A', '')):
            children[r['C']].append(r['A'])
    all_codes = {c for values in children.values() for c in values}
    assert len(all_codes) == sum(map(len, children.values())) == 1016
    nondata = set(json.loads(inputs[-1].read_text())['codes'])
    assert len(nondata) == 93 and all_codes - set(score) == nondata
    cached_missing = {r['O*NET-SOC 2019 Code'] for r in rows(OUT / 'phase2_unrated_onet_members.csv')}
    assert cached_missing == nondata
    beta = {soc: sum(score[c] for c in codes if c in score) / sum(c in score for c in codes)
            for soc, codes in children.items() if any(c in score for c in codes)}
    complete = {soc for soc, codes in children.items() if all(c in score for c in codes)}
    hierarchy = rows(OUT / 'soc2018_official_hierarchy.csv')
    assert collections.Counter(r['level'] for r in hierarchy) == {'detailed': 867, 'broad': 459, 'minor': 98, 'major': 23}
    members = {}
    for row in hierarchy:
        soc = row['soc']
        members[soc] = ({soc} if row['level'] == 'detailed' else
                        {r['soc'] for r in hierarchy if r['level'] == 'detailed' and soc in (r['major'], r['minor'], r['broad'])})
    raw_groups = {}
    current = None
    for number, r in workbook_rows(DATA / 'census_2018_pums.xlsx'):
        code, soc, title = (r.get(c, '') for c in ('A', 'B', 'C'))
        if re.fullmatch(r'\d{4}', code) and re.fullmatch(r'\d{2}-[\dXY]{4}', soc):
            current = code
            raw_groups[code] = {'soc': soc, 'parts': [] if re.search('[XY]', soc) else [soc], 'row': number}
        elif not code and re.fullmatch(r'\d{2}-\d{4}', soc) and current:
            raw_groups[current]['parts'].append(soc)
        elif code and not re.fullmatch(r'\d{4}', code):
            current = None
    mapping = {r['occp']: r for r in rows(OUT / 'occupation_mapping_final.csv')}
    assert len(mapping) == len(raw_groups) == 529
    for code, g in raw_groups.items():
        detailed = set().union(*(members[s] for s in g['parts'] if s in members))
        m = mapping[code]
        assert detailed == set(json.loads(m['documented_detailed_members']))
        assert sorted(s for s in g['parts'] if s not in members) == json.loads(m['invalid_source_members'])
        assert set(json.loads(m['score_incomplete_soc_members'])) == detailed - complete
        if m['mapping_status'] == 'covered':
            value = sum(beta[s] for s in detailed) / len(detailed)
            assert abs(value - float(m['beta_primary'])) < 1e-12
    assert raw_groups['7640']['row'] == 703
    # Verify the inconsistency and correction by explicit Census identifier, never title similarity.
    source_error = [(n, r) for n, r in workbook_rows(DATA / 'census_2018_pums.xlsx') if r.get('B') == '40-9095']
    assert len(source_error) == 1 and source_error[0][0] == 707
    correction = [(n, r) for n, r in workbook_rows(DATA / 'census_2018_soc.xlsx', 2) if '7550' in r.values()]
    assert any('49-9095' in r.values() for n, r in correction), 'Separate Census source must corroborate explicit code'
    aggregates = rows(DATA / 'phase2_pums_occupation_aggregates.csv')
    assert all(r['ST'] == '10' and r['age_segment'] in ['22-24', '25-34'] for r in aggregates)
    assert len({tuple(r[k] for k in ['ST', 'PUMA', 'survey_year', 'age_segment', 'OCCP', 'SOCP']) for r in aggregates}) == len(aggregates)
    old = {r['occp']: r for r in rows(OUT / 'occupation_mapping_diagnostic.csv')}
    existing = rows(OUT / 'exposure_coverage_by_geography.csv')
    before = rows(OUT / 'occupation_weighted_coverage.csv')
    coverage = []
    pooled_weights = {}
    for age in ['22-34', '25-34']:
        band = [r for r in aggregates if age == '22-34' or r['age_segment'] == '25-34']
        w = collections.Counter()
        for r in band:
            assert r['SOCP'] == mapping[r['OCCP']]['socp']
            w[r['OCCP']] += float(r['weight'])
        pooled_weights[age] = w
        total = sum(w.values())
        covered = sum(v for c, v in w.items() if mapping[c]['mapping_status'] == 'covered')
        original = sum(v for c, v in w.items() if old[c]['mapping_status'] == 'covered')
        available = sum(v for c, v in w.items() if mapping[c]['beta_available_soc_diagnostic'])
        target = next(r for r in existing if r['scope'] == 'State' and r['geography_id'] == '10' and r['age_group'] == age and r['survey_year'] == 'pooled')
        initial = next(r for r in before if r['age_group'] == age and r['survey_year'] == 'pooled')
        assert total == float(target['employment_weight']) == float(initial['weight'])
        assert covered == float(target['covered_weight']) and original == float(initial['covered_weight'])
        assert abs(100 * available / total - float(target['available_soc_diagnostic_coverage_percent'])) < 1e-10
        coverage.append(dict(age=age, employment_weight=total, original_covered_weight=original, covered_weight=covered,
                             original_coverage_percent=100*original/total, coverage_percent=100*covered/total,
                             available_soc_diagnostic_percent=100*available/total, unmatched_weight=total-covered))
    w22, w25 = (pooled_weights[k] for k in ['22-34', '25-34'])
    unresolved = {c for c in w22 if mapping[c]['mapping_status'] != 'covered'}
    old_unresolved = {c for c in w22 if old[c]['mapping_status'] != 'covered'}
    assert len(old_unresolved) == len(rows(OUT / 'occupation_unmatched_groups.csv')) == 107
    assert len(unresolved) == 62
    cached_u = [r for r in rows(OUT / 'unmatched_employment_by_group.csv') if r['age_group'] == '22-34' and r['survey_year'] == 'pooled']
    assert {r['OCCP'] for r in cached_u} == unresolved
    assert all(w22[r['OCCP']] == float(r['employment_weight']) for r in cached_u)
    registry = []
    for rank, code in enumerate(sorted(unresolved, key=lambda c: (-w22[c], c)), 1):
        m = mapping[code]
        missing = json.loads(m['unrated_soc_members'])
        partial = json.loads(m['partially_rated_soc_members'])
        invalid = json.loads(m['invalid_source_members'])
        tags = ['D_unrepresented_rating']
        if m['source_level'] in ['broad', 'minor']: tags.append('A_official_hierarchy_already_resolved')
        if m['source_level'] == 'Census composite X/Y': tags.append('B_composite_membership_already_resolved')
        tags.append('C_terminal_all_other')
        if partial: tags.append('G_strict_policy_sensitive_not_confirmed_bug')
        if invalid: tags.append('F_official_source_inconsistency')
        rule = 'Retain missing primary score and [0,1] group bounds; optional rated-member mean only as explicitly approved sensitivity'
        status = 'WHOLLY_UNRATED_SOC_REMAINS'
        uncertainty = 'High: an entire detailed SOC lacks beta; internal employment shares unknown'
        if partial and not missing:
            status = 'AVAILABLE_SPECIALTY_POLICY_CANDIDATE'
            rule = 'If approved: equal rated data-level O*NET specialties within each SOC, then equal documented SOC members; exclude non-data-level titles from score-availability denominator, disclose residual representativeness'
            uncertainty = 'Material: rated specialties do not establish exposure of unspecified residual jobs; no age-specific shares'
        if invalid:
            status = 'SOURCE_CORRECTION_AND_SPECIALTY_POLICY_REQUIRED'
            rule = 'Versioned 40-9095 to 49-9095 exception supported by explicit Census 7550; then approved specialty policy for 49-9099; never apply silently'
        failure = ('Wholly unrated SOC: ' + ';'.join(missing) if missing else 'Rated specialties present, but non-data-level residual title is unscored: ' + ';'.join(partial))
        if invalid: failure += '; invalid published component ' + ';'.join(invalid)
        registry.append(dict(priority_rank=rank, occp=code, socp=m['socp'], description=m['official_description'],
            employment_weight_22_34=w22[code], employment_weight_25_34=w25.get(code, 0),
            share_all_employment_percent=100*w22[code]/sum(w22.values()), share_unmatched_percent=100*w22[code]/21029,
            primary_root_cause='F' if invalid else 'D', root_cause_tags=';'.join(tags), source_level=m['source_level'],
            failure_reason=failure, wholly_unrated_socs=';'.join(missing), partially_rated_socs=';'.join(partial),
            unscored_onet_titles=';'.join(json.loads(m['unscored_onet_members'])),
            documented_soc_members=';'.join(json.loads(m['documented_detailed_members'])),
            invalid_source_members=';'.join(invalid), census_root_excel_row=m['root_excel_row'],
            official_membership_source=CENSUS+' | '+BLS, official_rating_domain_source='https://www.onetcenter.org/taxonomy/2019/no_data_coll.html',
            rating_source=RATING, proposed_resolution_source=(ONET + (' | https://www2.census.gov/programs-surveys/demo/guidance/industry-occupation/2018-occupation-code-list-and-crosswalk.xlsx ; Census identifier 7550, sheet 2018 Census Occ Code List, row 547' if invalid else '')
                if partial and not missing else 'https://www.onetcenter.org/taxonomy/2019/no_data_coll.html ; confirms no rating; no published beta source found for residual; NEM row verification OPEN'),
            resolution_type='Exact membership already documented; scoring requires aggregation/representativeness' if not invalid else 'Documented identifier correction candidate plus aggregation assumption',
            proposed_scoring_rule=rule, measurement_uncertainty=uncertainty,
            available_soc_diagnostic_beta=m['beta_available_soc_diagnostic'], resolution_status=status,
            nem_row_verification='OPEN_HTTP_403', uncertainty_status='NOT_FINAL_NO_PRIMARY_CHANGE', approval_required='Phase B explicit approval before score-policy implementation'))
    assert shutil.disk_usage(ROOT).free > 48 * 1024**3 + 5 * 1024**2
    with (OUT/'occupation_resolution_priorities.csv').open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(registry[0]), lineterminator='\n')
        writer.writeheader(); writer.writerows(registry)
    assert sum(r['employment_weight_22_34'] for r in registry) == 21029
    summary = dict(base_commit='6ff6250027b52abd8b4cb0b8d41a810463288723', scope='Phase A cached Delaware aggregates only',
        input_sha256=hashes, coverage=coverage, unresolved_groups=62, original_unresolved_groups=107,
        issue_status_counts=dict(collections.Counter(r['resolution_status'] for r in registry)),
        issue_status_weights={s: sum(r['employment_weight_22_34'] for r in registry if r['resolution_status']==s) for s in {r['resolution_status'] for r in registry}},
        complete_rating_domain=True, data_level_ratings=923, official_non_data_level_titles=93,
        non_data_civilian=74, non_data_military=19, primary_dataset_changed=False,
        exact_score_repairs_confirmed=0, regressions_run=0, person_microdata_reads=0,
        source_correction_excel_rows=[707, next(n for n,r in correction if '49-9095' in r.values())],
        aggregate_rows=len(aggregates), elapsed_seconds=time.monotonic()-started,
        peak_process_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        disk_free_bytes_end=shutil.disk_usage(ROOT).free)
    assert summary['peak_process_rss_bytes'] < 128 * 1024**2
    (OUT/'phase3_cached_audit.json').write_text(json.dumps(summary, indent=2, sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in summary.items() if k!='input_sha256'}, indent=2))


if __name__ == '__main__':
    main()
