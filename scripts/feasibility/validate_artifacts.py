"""Hash verification and cross-output acceptance checks; no estimates."""
import hashlib,json,csv
from common import ROOT,DATA,OUT,save

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
if __name__=='__main__':
 records=[json.loads(x) for x in (OUT/'source_manifest.jsonl').read_text().splitlines()]
 valid={};verified=0
 for r in records:
  if r.get('sha256'):valid.setdefault(r['id'],set()).add(r['sha256'])
  assert not {'set-cookie','authorization','proxy-authorization'} & set(r.get('headers',{}))
 for name,hashes in valid.items():
  path=DATA/name
  if path.exists():
   assert digest(path) in hashes, f'Changed downloaded object: {name}'
   verified+=1
 read=lambda x:json.loads((OUT/x).read_text())
 h=read('hmda_snapshot_probe.json')
 for year in map(str,range(2018,2026)):
  v=h[year];assert v['head']['status']==200
  assert v['tail']['status']==v['prefix']['status']==206
  assert len(v['sample']['header'])==99 and not v['sample']['required_missing']
  assert v['zip_entries'][0]['uncompressed_bytes']>4_000_000_000
  assert v['sample']['rows']>0
 g=read('geography_audit.json');assert g['county']['duplicate_fips']==g['puma']['duplicate_pairs']==0
 assert g['puma']['sums_outside_tolerance']==0
 assert g['hmda_samples']['hmda_ct_2024.csv']['matched_rows']==0
 q=read('qwi_sample_audit.json');assert q['rows']==480 and q['absent_cells']==q['duplicates']==0
 a=read('auxiliary_audit.json');assert a['qwi_states_total']==51 and a['qwi_end2025q4_count']==49
 assert a['qwi_end_quarters']['mi']=='2021:4'
 assert len(a['acs_de_counties'])==3 and all(r['valid_positive_medians'] for r in a['acs_de_counties'])
 e=read('compute_audit.json');assert len(e['tests'])==3 and all(t['reference_agreement'] for t in e['tests'])
 o=read('occupation_audit.json')
 for r in o['coverage']:
  assert abs(r['weighted_coverage_percent']-100*r['covered_weight']/r['weight'])<1e-9
  assert r['official_code_inconsistent_weight']==r['missing_socp_weight']==0
 tests=read('test_register.json');ids=[t['test_id'] for t in tests];assert len(ids)==len(set(ids))==23
 fields=['purpose','source','procedure','evidence','limitations','geography_implication','next_action']
 assert all(t['status'] in ['PASS','FAIL','OPEN'] and all(t[f] for f in fields) for t in tests)
 for p in (ROOT/'docs').glob('*.md'):assert p.stat().st_size>1000
 artifacts=[]
 for name in ['README.md','Makefile','.gitignore']:
  p=ROOT/name;artifacts.append(dict(path=name,bytes=p.stat().st_size,sha256=digest(p),scope='local handoff/reproduction artifact'))
 for folder in ['docs','scripts/feasibility','audit','results/feasibility']:
  for p in (ROOT/folder).rglob('*'):
   if p.is_file() and '__pycache__' not in p.parts and p.name not in ['local_artifact_manifest.json','validation.json']:
    artifacts.append(dict(path=str(p.relative_to(ROOT)),bytes=p.stat().st_size,sha256=digest(p),scope='local derived/document/code artifact'))
 for p in DATA.glob('hmda_*_sample.csv'):
  artifacts.append(dict(path=str(p.relative_to(ROOT)),bytes=p.stat().st_size,sha256=digest(p),scope='derived bounded prefix CSV; ignored raw sample'))
 save('local_artifact_manifest.json',artifacts)
 save('research_document_manifest.json',[dict(path=str(p.relative_to(ROOT)),bytes=p.stat().st_size,sha256=digest(p),scope='unchanged local independent Claude review') for p in sorted((ROOT/'literature').glob('*.md'))])
 save('validation.json',dict(status='PASS',downloaded_object_hashes_verified=verified,structured_tests_verified=len(tests),hmda_years_verified=8,duckdb_count_checks=3,regressions_run=0,national_full_data_downloads=0,remaining_dependency_recommendation='C'))
 print('PASS:',verified,'download hashes, 23 test records, 8 HMDA years, 3 exact DuckDB/Python count checks; recommendation C.')
