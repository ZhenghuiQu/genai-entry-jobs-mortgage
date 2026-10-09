"""Inspect Dorn keys/allocations and observed county vintages without silent drops."""
import zipfile
import pandas as pd
from common import DATA,OUT,save

def stata(name):
 with zipfile.ZipFile(DATA/name) as z:
  names=[n for n in z.namelist() if n.endswith('.dta') and not n.startswith('__MACOSX')]
  assert len(names)==1
  return pd.read_stata(z.open(names[0]))

def coverage(frame,key,weights,lookup):
 ok=frame[key].isin(lookup)
 return dict(rows=len(frame),matched_rows=int(ok.sum()),row_coverage_percent=float(100*ok.mean()),
             weight_total=float(frame[weights].sum()),matched_weight=float(frame.loc[ok,weights].sum()),
             weighted_coverage_percent=float(100*frame.loc[ok,weights].sum()/frame[weights].sum()),
             unmatched=frame.loc[~ok,[key,weights]].to_dict('records'))

if __name__=='__main__':
 c=stata('dorn_county.zip');p=stata('dorn_puma.zip');s=stata('dorn_state.zip')
 c['fips']=c.cty_fips.astype(int).astype(str).str.zfill(5)
 county=dict(zip(c.fips,c.czone.astype(int)))
 sums=p.groupby('puma2010').afactor.sum();tol=1e-6
 result=dict(county=dict(rows=len(c),czs=c.czone.nunique(),duplicate_fips=int(c.fips.duplicated().sum()),missing=int(c.isna().sum().sum())),
 puma=dict(rows=len(p),pumas=p.puma2010.nunique(),czs=p.czone.nunique(),duplicate_pairs=int(p.duplicated(['puma2010','czone']).sum()),
 afactor_min=float(p.afactor.min()),afactor_max=float(p.afactor.max()),sum_min=float(sums.min()),sum_max=float(sums.max()),
 max_absolute_sum_error=float((sums-1).abs().max()),sums_outside_tolerance=int(((sums-1).abs()>tol).sum()),tolerance=tol,
 negative_weights=int((p.afactor<0).sum()),weights_above_one_tolerance=int((p.afactor>1+tol).sum()),split_pumas=int((p.groupby('puma2010').size()>1).sum()),
 weighted_allocation='PWGTP * afactor; unnormalized published weights'),
 dominant_state=dict(rows=len(s),duplicate_cz=int(s.czone.duplicated().sum())))
 pop=pd.read_csv(DATA/'pop2019.csv',dtype=str,encoding='latin1');pop=pop[pop.SUMLEV=='050'].copy()
 pop['fips']=pop.STATE.str.zfill(2)+pop.COUNTY.str.zfill(3);pop['pop']=pop.POPESTIMATE2019.astype(int)
 target=pop[~pop.STATE.isin(['02','15','09'])].copy()
 result['population2019_nation_raw']=coverage(pop,'fips','pop',county)
 result['population2019_provisional_target_raw']=coverage(target,'fips','pop',county)
 # Documented Dorn strategies, evaluated as candidates only, not adopted HMDA matches.
 candidate=county.copy();candidate['12086']=county['12025'];candidate['46102']=county['46113'];candidate['08014']=28900
 result['population2019_provisional_target_documented_candidates']=coverage(target,'fips','pop',candidate)
 result['candidate_changes']=[dict(fips='12086',old='12025',cz=county['12025'],kind='renaming'),dict(fips='46102',old='46113',cz=county['46113'],kind='renaming'),dict(fips='08014',old=None,cz=28900,kind='Dorn recommended approximation across source counties')]
 result['ct_planning_region_lookup']={f'09{x}':county.get(f'09{x}') for x in range(110,191,10)}
 result['hmda_samples']={}
 for path in sorted(DATA.glob('hmda_*_sample.csv'))+sorted(DATA.glob('hmda_ct_*.csv')):
  try:d=pd.read_csv(path,dtype=str,keep_default_na=False)
  except Exception:continue
  if 'county_code' not in d:continue
  if 'open-end_line_of_credit' in d.columns:d=d.rename(columns={'open-end_line_of_credit':'open_end_line_of_credit'})
  d['n']=1
  state_fips=dict(zip('AL AK AZ AR CA CO CT DE DC FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY PR'.split(),'01 02 04 05 06 08 09 10 11 12 13 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 44 45 46 47 48 49 50 51 53 54 55 56 72'.split()))
  geographic_known=d.county_code.str.fullmatch(r'\d{5}')
  geographic_inconsistent=geographic_known & d.county_code.str[:2].ne(d.state_code.map(state_fips))
  # The entire sample denominator includes NA/blank/non-applicable geographic records.
  result['hmda_samples'][path.name]=coverage(d,'county_code','n',county)
  result['hmda_samples'][path.name]['state_county_inconsistent_rows']=int(geographic_inconsistent.sum())
  # Compact counts, never loan rows, go to results.
  result['hmda_samples'][path.name]['unmatched']=d.loc[~d.county_code.isin(county)].county_code.value_counts().to_dict()
  filt=(d.loan_purpose=='1') & d.action_taken.isin(['1','2','3','4','5']) & (d.lien_status=='1') & (d.occupancy_type=='1') & (d.construction_method=='1') & d.total_units.isin(['1','2','3','4'])
  for field in ['reverse_mortgage','open_end_line_of_credit','business_or_commercial_purpose']:filt &= d[field].isin(['2','1111','Exempt'])
  sub=d[filt & ~d.state_code.isin(['AK','HI','CT','PR'])].copy()
  if len(sub):
   rr=coverage(sub,'county_code','n',candidate);rr['unmatched']=sub.loc[~sub.county_code.isin(candidate)].county_code.value_counts().to_dict()
   result['hmda_samples'][path.name]['provisional_purchase_documented_candidates']=rr
 with zipfile.ZipFile(DATA/'pums_de.zip') as z:
  d=pd.read_csv(z.open('psam_p10.csv'),dtype=str,keep_default_na=False,usecols=['ST','PUMA','PWGTP','AGEP','ESR'])
 d['key']=d.ST.astype(int)*100000+d.PUMA.astype(int);d['PWGTP']=d.PWGTP.astype(int)
 d=d[d.ESR.isin(['1','2']) & d.AGEP.astype(int).between(22,34)]
 result['pums_de_young_geography']=coverage(d,'key','PWGTP',set(p.puma2010))
 joined=d.merge(p,left_on='key',right_on='puma2010',how='left',validate='many_to_many')
 result['pums_de_allocation_weight_error']=float((joined.PWGTP*joined.afactor).sum()-d.PWGTP.sum())
 result['national_hmda_geography_coverage']='OPEN: limited prefixes and CT extracts are not the complete intended HMDA universe'
 save('geography_audit.json',result)
 print({k:v for k,v in result.items() if k not in ['hmda_samples','population2019_nation_raw','population2019_provisional_target_raw']})
