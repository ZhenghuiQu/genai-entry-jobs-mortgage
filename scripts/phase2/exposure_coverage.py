"""Stream person ZIP members to aggregates; retain all employed occupation weights."""
import argparse,csv,hashlib,json,sys,time,zipfile
from pathlib import Path
import duckdb,numpy as np,pandas as pd
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'feasibility'))
from common import DATA,OUT,save
from geography_audit import stata
from build_occupation_mapping import build
KEYS=['ST','PUMA','survey_year','age_segment','OCCP','SOCP']
FIELDS=['SERIALNO','ST','PUMA','AGEP','ESR','OCCP','SOCP','PWGTP']
def aggregate(path,chunk_rows=100000):
 start=time.monotonic();pieces=[];rawrows=0;employed=0
 if path.name=='pums_us_phase2.zip':
  rec=json.loads((OUT/'phase2_national_acquisition.json').read_text())
  with path.open('rb') as f: digest=hashlib.file_digest(f,'sha256').hexdigest()
  assert not rec.get('error') and rec.get('status')==200 and digest==rec['sha256'], 'National archive not validated'

 con=duckdb.connect();con.execute("SET memory_limit='2GB'; SET threads=2; SET enable_external_access=false; SET allow_persistent_secrets=false")
 sql='SELECT ST,PUMA,survey_year,age_segment,OCCP,SOCP,count(*) AS "rows",sum(weight) AS weight FROM chunk GROUP BY ALL ORDER BY ALL'
 with zipfile.ZipFile(path) as z:
  for name in sorted(n for n in z.namelist() if n.endswith('.csv')):
   with z.open(name) as stream:
    for d in pd.read_csv(stream,usecols=FIELDS,dtype=str,keep_default_na=False,chunksize=chunk_rows):
     rawrows+=len(d);age=pd.to_numeric(d.AGEP,errors='raise');d=d[d.ESR.isin(['1','2']) & age.between(22,34)].copy()
     if d.empty:continue
     age=pd.to_numeric(d.AGEP);d['age_segment']=np.where(age<25,'22-24','25-34');d['survey_year']=d.SERIALNO.str[:4]
     assert d.survey_year.isin(['2015','2016','2017','2018','2019']).all()
     d['weight']=pd.to_numeric(d.PWGTP,errors='raise');assert d.weight.gt(0).all()
     employed+=len(d);chunk=d[KEYS+['weight']];con.register('chunk',chunk);a=con.execute(sql).df();con.unregister('chunk')
     assert int(a.weight.sum())==int(chunk.weight.sum()) and int(a.rows.sum())==len(chunk)
     pieces.append(a)
   print('Aggregated',name,'person rows so far',rawrows,flush=True)
 con.close();a=pd.concat(pieces).groupby(KEYS,as_index=False).agg(rows=('rows','sum'),weight=('weight','sum'))
 return a,dict(raw_person_rows=rawrows,civilian_employed_22_34_rows=employed,seconds=time.monotonic()-start,duckdb_version=duckdb.__version__,chunk_rows=chunk_rows,duckdb_sql=sql,zip_crc_verified='each CSV read to EOF; Python ZipExtFile CRC check',source_archive=path.name)

def summarize(d,keys,scope):
 rows=[]
 for vals,x in d.groupby(keys,dropna=False):
  vals=vals if isinstance(vals,tuple) else (vals,);rec=dict(zip(keys,vals));w=x.weight;total=float(w.sum());covered=x.covered;cw=float(w[covered].sum());num=float((w*x.beta_primary.fillna(0)).sum())
  alt=float((w*x.beta_equal_onet_children.fillna(0)).sum());unmatched=total-cw
  available=x.beta_available_soc_diagnostic.notna();available_w=float(w[available].sum());available_n=float((w*x.beta_available_soc_diagnostic.fillna(0)).sum())
  high=covered&x.beta_primary.ge(.5);possible=high|~covered
  rec.update(scope=scope,observed=True,employment_weight=total,covered_weight=cw,unresolved_weight=unmatched,weighted_coverage_percent=100*cw/total,
   exposure_lower=num/total,exposure_upper=(num+unmatched)/total,covered_only_mean=num/cw if cw else np.nan,
   alternative_equal_onet_lower=alt/total,alternative_equal_onet_upper=(alt+unmatched)/total,
   heterogeneity_lower=float((w*x.beta_member_min.fillna(0)).sum())/total,heterogeneity_upper=(float((w*x.beta_member_max.fillna(0)).sum())+unmatched)/total,
   high_exposure_threshold=.5,known_high_exposure_weight=float(w[high].sum()),possible_high_exposure_weight=float(w[possible].sum()),
   coverage_among_possible_high_percent=100*float(w[high].sum())/float(w[possible].sum()) if w[possible].sum() else np.nan,
   available_soc_diagnostic_coverage_percent=100*available_w/total,available_soc_diagnostic_lower=available_n/total,available_soc_diagnostic_upper=(available_n+total-available_w)/total,
   target_98_achieved=100*cw/total>=98,mapping_release_status='PROVISIONAL_AUDIT_NOT_FINAL',geographic_join_missing_weight=float(w[x.get('geography_missing',pd.Series(False,index=x.index))].sum()))
  rows.append(rec)
 return pd.DataFrame(rows)

def run():
 m=build();national=DATA/'pums_us_phase2.zip';path=national if national.exists() else DATA/'pums_de.zip';a,log=aggregate(path)
 a.to_csv(DATA/'phase2_pums_occupation_aggregates.csv',index=False)
 d=a.merge(m,left_on='OCCP',right_on='occp',how='left',validate='many_to_one')
 d['reason']=d.mapping_status.fillna('D_missing_or_invalid_identifier');consistent=d.SOCP.eq(d.socp)
 d.loc[~consistent,'reason']='D_missing_or_inconsistent_identifier';d['covered']=d.reason.eq('covered')
 for c in ['beta_primary','beta_equal_onet_children','beta_member_min','beta_member_max','beta_available_soc_diagnostic']:d.loc[~consistent if c=='beta_available_soc_diagnostic' else ~d.covered,c]=np.nan
 d['major_group']=d.major_group.fillna('UNKNOWN');bands=[]
 for lo in [22,25]:
  x=d.copy() if lo==22 else d[d.age_segment=='25-34'].copy();x['age_group']=f'{lo}-34';pooled=x.copy();pooled.survey_year='pooled';bands.extend([x,pooled])
 d=pd.concat(bands,ignore_index=True);d['geography_id']=d.ST.str.zfill(2)
 coverage=[summarize(d,['geography_id','age_group','survey_year'],'State')]
 if national.exists():
  x=d.copy();x.geography_id='US';coverage.append(summarize(x,['geography_id','age_group','survey_year'],'National'))
 else:
  coverage.append(pd.DataFrame([dict(scope='National',geography_id='US',age_group=f'{lo}-34',survey_year=y,observed=False,status='OPEN_DOWNLOAD_HTTP_403') for lo in [22,25] for y in ['pooled','2015','2016','2017','2018','2019']]))
 p=stata('dorn_puma.zip');d['puma_key']=d.ST.astype(int)*100000+d.PUMA.astype(int)
 assert not p.duplicated(['puma2010','czone']).any();sums=p.groupby('puma2010').afactor.sum();assert (sums-1).abs().max()<1e-6
 x=d.merge(p,left_on='puma_key',right_on='puma2010',how='left',validate='many_to_many');x['geography_missing']=x.afactor.isna();x['weight']=x.weight*x.afactor.fillna(1);x['geography_id']=x.czone.map(lambda v:str(int(v)) if pd.notna(v) else 'UNALLOCATED')
 assert abs(float(x.weight.sum()-d.weight.sum()))<1e-6*float(d.weight.sum())
 coverage.append(summarize(x,['geography_id','age_group','survey_year'],'CZ_allocated_sample' if not national.exists() else 'CZ'))
 major=summarize(d,['geography_id','age_group','survey_year','major_group'],'State_major_occupation');major.to_csv(OUT/'phase2_coverage_by_major_group.csv',index=False)
 cov=pd.concat(coverage,ignore_index=True);cov.to_csv(OUT/'exposure_coverage_by_geography.csv',index=False)
 u=d[~d.covered].groupby(['ST','age_group','survey_year','OCCP','SOCP','reason','major_group'],dropna=False).agg(person_rows=('rows','sum'),employment_weight=('weight','sum')).reset_index()
 u=u.merge(m[['occp','official_description','documented_detailed_members','unrated_soc_members','partially_rated_soc_members','unscored_onet_members','invalid_source_members']],left_on='OCCP',right_on='occp',how='left',validate='many_to_one')
 denom=d.groupby(['ST','age_group','survey_year']).weight.sum().rename('denominator');u=u.merge(denom,on=['ST','age_group','survey_year'],how='left',validate='many_to_one');u['unresolved_share_percent']=100*u.employment_weight/u.denominator
 for c in ['documented_detailed_members','unrated_soc_members','partially_rated_soc_members','unscored_onet_members','invalid_source_members']:u[c]=u[c].map(lambda v:json.dumps(v) if isinstance(v,list) else '')
 u.to_csv(OUT/'unmatched_employment_by_group.csv',index=False)
 # Alternative score methods and pairwise conservative ranking checks on observed geographies.
 obs=cov[cov.observed.eq(True)].copy();sens=[]
 for _,r in obs.iterrows():
  for method,l,h in [('equal_soc_primary','exposure_lower','exposure_upper'),('equal_onet_children','alternative_equal_onet_lower','alternative_equal_onet_upper'),('member_heterogeneity_envelope','heterogeneity_lower','heterogeneity_upper'),('available_child_SOC_diagnostic','available_soc_diagnostic_lower','available_soc_diagnostic_upper')]:
   sens.append(dict(scope=r.scope,geography_id=r.geography_id,age_group=r.age_group,survey_year=r.survey_year,method=method,lower=r[l],upper=r[h],status='PROVISIONAL',note='All unresolved group employment allowed exposure [0,1]; envelope spans all rated O*NET children; primary assumes equal internal shares'))
 pd.DataFrame(sens).to_csv(OUT/'exposure_sensitivity.csv',index=False)
 with (OUT/'phase2_exposure_rank_checks.csv').open('w',newline='') as f:
  writer=csv.DictWriter(f,lineterminator='\n',fieldnames=['scope','age_group','survey_year','geo1','geo2','ranking_robust_to_unscored','intervals_overlap']);writer.writeheader()
  for vals,z in obs.groupby(['scope','age_group','survey_year']):
   for i,r in z.iterrows():
    for k,t in z.loc[z.index>i].iterrows():
     robust=(r.exposure_lower>t.exposure_upper)or(t.exposure_lower>r.exposure_upper)
     writer.writerow(dict(scope=vals[0],age_group=vals[1],survey_year=vals[2],geo1=r.geography_id,geo2=t.geography_id,ranking_robust_to_unscored=robust,intervals_overlap=not robust))
 log.update(national_observed=national.exists(),aggregate_rows=len(a),coverage_rows=len(cov),unmatched_output_rows=len(u),all_employed_denominators_retained=True,regressions_run=0,high_exposure_rule='beta_primary >= 0.5 chosen before mortgage outcomes; unscored potentially high',geographic_allocation_error=float(x.weight.sum()-d.weight.sum()),national_dependency='resolved' if national.exists() else 'HTTP 403; complete national validation remains OPEN')
 save('phase2_processing_log.json',log);print(obs[(obs.scope=='State')&obs.survey_year.eq('pooled')][['geography_id','age_group','employment_weight','covered_weight','weighted_coverage_percent','exposure_lower','exposure_upper']].to_string(index=False));print(log)
if __name__=='__main__':run()
