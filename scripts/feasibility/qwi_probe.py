"""Inspect release manifests for 50 states + DC; one complete county-age sample."""
from concurrent.futures import ThreadPoolExecutor
from common import fetch, DATA, save
import csv,gzip,json
states='al ak az ar ca co ct de dc fl ga hi id il in ia ks ky la me md ma mi mn ms mo mt ne nv nh nj nm ny nc nd oh ok or pa ri sc sd tn tx ut vt va wa wv wi wy'.split()
def version(st):
 body,r=fetch('qwi_version_'+st+'.txt',f'https://lehd.ces.census.gov/data/qwi/latest_release/{st}/version_qwi.txt',cap=10000)
 return st,dict(retrieval=r,text=body.decode() if body else None)
if __name__=='__main__':
 import sys
 versions = json.loads((__import__('common').OUT/'qwi_versions.json').read_text()) if '--analyze-only' in sys.argv else dict(ThreadPoolExecutor(max_workers=6).map(version,states))
 save('qwi_versions.json',versions)
 print({st: v['text'] for st,v in versions.items() if st in ['mi','ak','de','ct']},flush=True)
 # Head metadata on resource bottlenecks only.
 heads={}
 if '--analyze-only' not in sys.argv:
  for st in ['ca','de','mi']:
   _,heads[st]=fetch('qwi_size_'+st,f'https://lehd.ces.census.gov/data/qwi/latest_release/{st}/qwi_{st}_sa_f_gc_ns_op_u.csv.gz',method='HEAD')
  save('qwi_download_sizes.json',heads)
 rows=[]
 with gzip.open(DATA/'qwi_de.csv.gz','rt') as f:
  for r in csv.DictReader(f):
   if r['geo_level']=='C' and r['ind_level']=='A' and r['sex']=='0' and r['industry']=='00' and r['agegrp'] in ['A03','A04','A05','A06'] and 2016<=int(r['year'])<=2025:rows.append(r)
 from collections import Counter
 res=dict(rows=len(rows),counties=sorted({r['geography'] for r in rows}),last_quarter=max((r['year'],r['quarter']) for r in rows),age_codes=sorted({r['agegrp'] for r in rows}),duplicates=len(rows)-len({tuple(r[k] for k in ['geography','year','quarter','agegrp']) for r in rows}),fields=list(rows[0]) if rows else [])
 res['flags']={field:dict(Counter(r[field] for r in rows)) for field in ['sEmp','sHirA']}
 res['missing']={field:sum(r[field] in ['','NA','NaN'] for r in rows) for field in ['Emp','HirA']}
 expected={(c,str(y),str(q),a) for c in res['counties'] for y in range(2016,2026) for q in range(1,5) for a in res['age_codes']}
 res['expected_rows']=len(expected);res['absent_cells']=len(expected-{tuple(r[k] for k in ['geography','year','quarter','agegrp']) for r in rows})
 save('qwi_sample_audit.json',res);print(res,flush=True)
