"""Independent CSV arithmetic, source hashes, hierarchy invariants and output contracts."""
import csv,datetime as dt,hashlib,json,re,subprocess,sys,zipfile
from collections import defaultdict
from pathlib import Path
import pandas as pd
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'feasibility'))
from common import ROOT,DATA,OUT,MANIFEST,save
BASE='3f363bca62b6d8938ee8f95696465361d2092476'
def sha(path):
 with path.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def run():
 checks=[]
 def done(name,evidence):checks.append(dict(test=name,status='PASS',evidence=evidence))
 # Preserve actual original documents and script bytes; no Git write occurs here.
 for entry in json.loads((OUT/'research_document_manifest.json').read_text()):assert sha(ROOT/entry['path'])==entry['sha256']
 for name in ['occupation_audit.py','common.py','geography_audit.py']:
  original=subprocess.check_output(['git','show',f'{BASE}:scripts/feasibility/{name}'],cwd=ROOT)
  assert (ROOT/'scripts/feasibility'/name).read_bytes()==original
 assert subprocess.run(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT).returncode==0
 done('history_and_original_research_preserved',{'original_commit':BASE,'literature_files':8,'original_key_scripts':3})
 records=[json.loads(x) for x in MANIFEST.read_text().splitlines()];hashes=defaultdict(set)
 for r in records:
  assert not {'set-cookie','authorization','proxy-authorization'} & set(r.get('headers',{}))
  if r.get('sha256'):hashes[r['id']].add(r['sha256'])
 names=['exposure.csv','onet_soc2018.xlsx','census_2018_pums.xlsx','census_2018_soc.xlsx','pums_de.zip','dorn_county.zip','dorn_puma.zip','dorn_state.zip','pop2019.csv','county_changes.pdf']
 for name in names:assert sha(DATA/name) in hashes[name],name
 assert json.loads((DATA/'exposure_commit.json').read_text())['sha']=='0471612fef3cc22b74fb884d27bff9dbd3770582'
 for r in json.loads((OUT/'phase2_web_source_manifest.json').read_text()):assert sha(ROOT/r['local_artifact_path'])==r['sha256']
 done('web_extract_representation_hashes',{'representations':3,'original_download_hash_claimed':False})
 done('pinned_official_inputs_and_rating_version',{'verified_inputs':len(names),'ratings_commit':'0471612fef3cc22b74fb884d27bff9dbd3770582'})
 h=pd.read_csv(OUT/'soc2018_official_hierarchy.csv',dtype=str);assert h.soc.is_unique
 assert h.level.value_counts().to_dict()=={'detailed':867,'broad':459,'minor':98,'major':23}
 # Official named examples are adversarial checks for prefix mistakes and exceptional minor groups.
 assert set(h.loc[h.minor.eq('25-1000') & h.level.eq('detailed'),'soc'])==set(['25-1011','25-1021','25-1022','25-1031','25-1032','25-1041','25-1042','25-1043','25-1051','25-1052','25-1053','25-1054','25-1061','25-1062','25-1063','25-1064','25-1065','25-1066','25-1067','25-1069','25-1071','25-1072','25-1081','25-1082','25-1111','25-1112','25-1113','25-1121','25-1122','25-1123','25-1124','25-1125','25-1126','25-1192','25-1193','25-1194','25-1199'])
 assert h.loc[h.soc.eq('15-1231'),'minor'].iloc[0]=='15-1200'
 done('complete_official_hierarchy',h.level.value_counts().to_dict())
 rows=list(csv.DictReader((OUT/'occupation_mapping_final.csv').open()));m={r['occp']:r for r in rows};assert len(rows)==len(m)==529
 assert set(json.loads(m['0010']['documented_detailed_members']))=={'11-1011','11-1031'} and '11-1021' not in json.loads(m['0010']['documented_detailed_members'])
 assert set(json.loads(m['1760']['documented_detailed_members']))=={'19-2099'} # terminal All Other does not expand
 assert json.loads(m['7640']['invalid_source_members'])==['40-9095'] and m['7640']['beta_primary']==''
 assert m['9830']['mapping_status']=='C_census_military_unspecified'
 assert all(r['official_description'] and r['source_documentation'] and r['release_status']=='PROVISIONAL_AUDIT_NOT_FINAL' for r in rows)
 for r in rows:
  if r['mapping_status']=='covered':assert json.loads(r['unscored_onet_members'])==[] and json.loads(r['unrated_soc_members'])==[]
 done('explicit_composites_all_other_anomaly_and_provisional_metadata',{'groups':529,'source_anomaly_preserved':True,'prefix_membership_not_assumed':True})
 # Independent person-by-person standard-library CSV arithmetic; no pandas/DuckDB aggregation reuse.
 expected=defaultdict(lambda:[0,0,0.]);n=0
 with zipfile.ZipFile(DATA/'pums_de.zip') as z:
  with z.open('psam_p10.csv') as f:
   import io
   for r in csv.DictReader(io.TextIOWrapper(f)):
    n+=1
    if r['ESR'] not in ['1','2']:continue
    age=int(r['AGEP']);w=int(r['PWGTP']);occ=m.get(r['OCCP']);covered=occ is not None and occ['socp']==r['SOCP'] and occ['mapping_status']=='covered'
    score=float(occ['beta_primary']) if covered else 0
    for lo in [22,25]:
     if lo<=age<=34:
      for y in ['pooled',r['SERIALNO'][:4]]:
       v=expected[(f'{lo}-34',y)];v[0]+=w;v[1]+=w if covered else 0;v[2]+=w*score
 cov=list(csv.DictReader((OUT/'exposure_coverage_by_geography.csv').open()))
 for r in cov:
  if r['scope']=='State':
   e=expected[(r['age_group'],r['survey_year'])];assert int(float(r['employment_weight']))==e[0] and int(float(r['covered_weight']))==e[1]
   assert abs(float(r['exposure_lower'])-e[2]/e[0])<1e-12
   assert abs(float(r['exposure_upper'])-(e[2]+e[0]-e[1])/e[0])<1e-12
   assert r['target_98_achieved']=='False'
 assert n==45217 and expected[('22-34','pooled')][:2]==[123656,102627] and expected[('25-34','pooled')][:2]==[100473,83381]
 done('independent_complete_DE_denominators_coverage_and_bounds',{'person_rows':n,'age_year_comparisons':len(expected),'primary_covered_weights':[102627,83381]})
 # Original rerun genuinely matches historical bytes.
 for name in ['occupation_audit.json','occupation_mapping_diagnostic.csv','occupation_weighted_coverage.csv','occupation_unmatched_groups.csv','occupation_ambiguous_groups.csv']:
  assert (OUT/name).read_bytes()==subprocess.check_output(['git','show',f'{BASE}:results/feasibility/{name}'],cwd=ROOT)
 from exposure_coverage import aggregate
 import contextlib,io
 with contextlib.redirect_stdout(io.StringIO()):a,_=aggregate(DATA/'pums_de.zip',chunk_rows=1000)
 b=pd.read_csv(DATA/'phase2_pums_occupation_aggregates.csv',dtype={k:str for k in ['ST','PUMA','survey_year','age_segment','OCCP','SOCP']})
 keys=['ST','PUMA','survey_year','age_segment','OCCP','SOCP']
 assert a[keys].astype(str).equals(b[keys].astype(str)) and a['weight'].astype(float).equals(b['weight'].astype(float)) and a['rows'].equals(b['rows'])
 done('streaming_chunk_boundary_invariance',{'chunk_rows_compared':[1000,100000],'aggregate_keys':len(a)})
 done('original_occupation_results_reproduced_byte_for_byte',{'outputs':5})
 import geography_audit
 c=geography_audit.stata('dorn_county.zip');p=geography_audit.stata('dorn_puma.zip');assert c.cty_fips.is_unique and not p.duplicated(['puma2010','czone']).any()
 assert c[c.cty_fips.astype(int).between(9000,9999)].czone.eq(20901).all()
 assert p.groupby('puma2010').afactor.sum().sub(1).abs().max()<1e-6
 ct=pd.read_csv(OUT/'phase2_ct_region_membership.csv',dtype={'new_region':str});tr=pd.read_csv(OUT/'phase2_ct_tract_bridge.csv',dtype=str)
 assert len(ct)==9 and ct.unique_cz.eq(20901).all() and ct.new_region.str.fullmatch('09[0-9]{3}').all()
 assert len(tr)==884 and tr.GEOID_TRACT_22.is_unique and tr.status.eq('EXACT_UNIQUE_CZ_BY_OFFICIAL_TOWN_RELATION').all()
 g=json.loads((OUT/'phase2_geography_summary.json').read_text());assert not g['CT_cross_state_CZs']
 assert [r['option_A_mapped_rows'] for r in g['CT_samples']]==[41016,35290,34791,35340]
 assert [r['missing_county_rows'] for r in g['CT_samples']]==[138,244,359,336]
 done('geography_mass_and_official_CT_sample_coverage',{'CT_regions':9,'tracts':884,'CT_cross_state_CZs':0,'cross_state_CZs_national_inventory':g['cross_state_CZs']})
 nat=[r for r in cov if r['scope']=='National'];assert len(nat)==12 and all(r['observed']=='False' and r['weighted_coverage_percent']=='' for r in nat)
 log=json.loads((OUT/'phase2_processing_log.json').read_text());gate=json.loads((OUT/'phase2_gate_status.json').read_text());assert log['regressions_run']==gate['regressions_run']==0 and not gate['national_validation_complete'] and gate['recommendation']=='C'
 assert all(r['status'] in ['PASS','FAIL','OPEN'] and r['source'] and r['version'] and r['test_procedure'] and r['remaining_uncertainty'] and r['primary_design_implication'] for r in gate['gates'])
 assert all(Path(ROOT/'docs'/f).exists() for f in ['occupation_mapping_resolution.md','national_exposure_coverage.md','geographic_design_resolution.md','research_provenance_integration.md','phase2_decision_register.md'])
 assert len({r['gate_id'] for r in gate['gates']})==len(gate['gates'])
 done('honest_scope_and_all_output_contracts',{'national_unobserved_rows':12,'regressions':0,'recommendation':'C','gates':len(gate['gates'])})
 save('phase2_validation.json',dict(status='PASS',executed_at_utc=dt.datetime.now(dt.timezone.utc).isoformat(),checks=checks,scope='Observed local Phase 2 evidence and reproduction; not national acceptance or remote integration',recommendation='C'))
 artifacts=[]
 for folder in ['docs','audit','scripts/phase2','results/feasibility']:
  for path in sorted((ROOT/folder).rglob('*')):
   if path.is_file() and '__pycache__' not in path.parts and path.name!='phase2_artifact_manifest.json':
    artifacts.append(dict(path=str(path.relative_to(ROOT)),bytes=path.stat().st_size,sha256=sha(path),hash_scope='local artifact bytes'))
 for path in [ROOT/'README.md',ROOT/'Makefile']+[DATA/name for name in names]:artifacts.append(dict(path=str(path.relative_to(ROOT)),bytes=path.stat().st_size,sha256=sha(path),hash_scope='local bytes; original-source hashes validated separately' if DATA in path.parents else 'local artifact bytes'))
 save('phase2_artifact_manifest.json',dict(original_commit=BASE,remote_integrated=False,artifacts=artifacts))
 print('PASS:',len(checks),'independent validation groups; national/remote gates remain OPEN; recommendation C')
if __name__=='__main__':run()
