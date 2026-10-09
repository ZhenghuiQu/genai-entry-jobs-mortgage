"""Strict official membership concordance. Numeric broad SOC groups remain OPEN.

No prefix/wildcard substitution: X/Y membership is read from the Census workbook's
explicit 'Combines' component rows. O*NET -> SOC uses the official crosswalk.
The equal-child mean is a transparent test assumption, not employment weights.
"""
import re,zipfile
import pandas as pd
from common import DATA,OUT,save

if __name__=='__main__':
 e=pd.read_csv(DATA/'exposure.csv',dtype={'O*NET-SOC Code':str})
 o=pd.read_excel(DATA/'onet_soc2018.xlsx',header=3,dtype=str)
 o.columns=[x.strip() for x in o.columns]
 o=o[o['O*NET-SOC 2019 Code'].str.fullmatch(r'\d{2}-\d{4}\.\d{2}',na=False)]
 joined=e.merge(o,left_on='O*NET-SOC Code',right_on='O*NET-SOC 2019 Code',how='left',validate='one_to_one')
 assert joined['2018 SOC Code'].notna().all()
 beta=joined.groupby('2018 SOC Code').dv_rating_beta.mean()
 children=joined.groupby('2018 SOC Code').size()
 raw=pd.read_excel(DATA/'census_2018_pums.xlsx',sheet_name='ACS',header=None,dtype=str).fillna('')
 groups={};current=None
 for row_no,row in raw.iterrows():
  code,soc,title=[x.strip() for x in row.tolist()]
  if re.fullmatch(r'\d{4}',code) and re.fullmatch(r'\d{2}-[\dXY]{4}',soc):
   current=code
   groups[code]=dict(occp=code,socp=soc.replace('-',''),label=title,soc_members=[soc] if not any(x in soc for x in 'XY') else [],excel_rows=[int(row_no)+1])
  elif not code and re.fullmatch(r'\d{2}-\d{4}',soc) and current:
   groups[current]['soc_members'].append(soc);groups[current]['excel_rows'].append(int(row_no)+1)
  elif '-' in code or (code and not re.fullmatch(r'\d{4}',code)):
   current=None
 for g in groups.values():
  members=sorted(set(g['soc_members']));g['soc_members']=members
  available=[s for s in members if s in beta]
  g['n_members']=len(members);g['n_scored_members']=len(available)
  g['mapping_status']='covered' if members and len(available)==len(members) else 'unresolved_group_or_unscored_member'
  g['beta_equal_member_mean']=float(beta.loc[available].mean()) if g['mapping_status']=='covered' else None
  g['beta_min']=float(beta.loc[available].min()) if available else None
  g['beta_max']=float(beta.loc[available].max()) if available else None
  g['n_onet_children']=int(children.loc[available].sum()) if available else 0
 pd.DataFrame(groups.values()).to_csv(OUT/'occupation_mapping_diagnostic.csv',index=False)
 with zipfile.ZipFile(DATA/'pums_de.zip') as z:
  d=pd.read_csv(z.open('psam_p10.csv'),dtype=str,keep_default_na=False,usecols=['SERIALNO','ST','PUMA','AGEP','ESR','SOCP','OCCP','PWGTP','SCHL','NAICSP'])
 d['weight']=d.PWGTP.astype(int);d['age']=d.AGEP.astype(int);d['year']=d.SERIALNO.str[:4]
 gdf=pd.DataFrame(groups.values()).set_index('occp')
 d['official_socp']=d.OCCP.map(gdf.socp)
 d['code_consistent']=d.SOCP.eq(d.official_socp)
 d['beta']=d.OCCP.map(gdf.beta_equal_member_mean)
 d.loc[~d.code_consistent,'beta']=float('nan')
 d['covered']=d.beta.notna()
 civilian=d[d.ESR.isin(['1','2'])].copy()
 reports=[]
 for age_lo in [22,25]:
  for year in ['pooled','2015','2016','2017','2018','2019']:
   sub=civilian[civilian.age.between(age_lo,34)]
   if year!='pooled':sub=sub[sub.year==year]
   total=int(sub.weight.sum());matched=int(sub.loc[sub.covered,'weight'].sum())
   wildcard=sub.SOCP.str.contains('[XY]',regex=True)
   ambiguous=sub.OCCP.map(gdf.n_members).fillna(0).gt(1) | sub.OCCP.map(gdf.n_onet_children).fillna(0).gt(1)
   reports.append(dict(age_group=f'{age_lo}-34',survey_year=year,rows=len(sub),weight=total,
      covered_weight=matched,weighted_coverage_percent=100*matched/total,
      missing_socp_weight=int(sub.loc[sub.SOCP.eq(''),'weight'].sum()),
      official_code_inconsistent_weight=int(sub.loc[~sub.code_consistent,'weight'].sum()),
      xy_group_weight=int(sub.loc[wildcard,'weight'].sum()),
      ambiguous_member_weight=int(sub.loc[ambiguous,'weight'].sum()),
      mean_exposure_covered_only=float((sub.loc[sub.covered,'beta']*sub.loc[sub.covered,'weight']).sum()/matched)))
 pd.DataFrame(reports).to_csv(OUT/'occupation_weighted_coverage.csv',index=False)
 young=civilian[civilian.age.between(22,34)].copy()
 unmatched=young[~young.covered].groupby(['OCCP','SOCP'],dropna=False).agg(rows=('weight','size'),weight=('weight','sum')).reset_index()
 unmatched['label']=unmatched.OCCP.map(gdf.label);unmatched['members']=unmatched.OCCP.map(gdf.soc_members)
 unmatched.to_csv(OUT/'occupation_unmatched_groups.csv',index=False)
 ambiguities=young.groupby(['OCCP','SOCP']).weight.sum().reset_index()
 ambiguities=ambiguities.merge(gdf.reset_index(),left_on='OCCP',right_on='occp',how='left')
 ambiguities=ambiguities[(ambiguities.n_members>1)|(ambiguities.n_onet_children>1)|ambiguities.mapping_status.ne('covered')]
 ambiguities.to_csv(OUT/'occupation_ambiguous_groups.csv',index=False)
 # Sample arithmetic smoke test only. The result is not the final exposure index.
 from geography_audit import stata
 p=stata('dorn_puma.zip');young['key']=young.ST.astype(int)*100000+young.PUMA.astype(int)
 a=young[young.covered].merge(p,left_on='key',right_on='puma2010',how='left')
 a['allocated_weight']=a.weight*a.afactor
 allocated=a.groupby('czone').allocated_weight.sum()
 save('occupation_audit.json',dict(exposure_rows=len(e),exposure_codes_unique=e['O*NET-SOC Code'].nunique(),
 beta_missing=int(e.dv_rating_beta.isna().sum()),beta_min=float(e.dv_rating_beta.min()),beta_max=float(e.dv_rating_beta.max()),
 official_onet_soc_join_coverage_percent=100*joined['2018 SOC Code'].notna().mean(),scored_soc_groups=len(beta),
 census_pums_groups=len(groups),sample_state='Delaware only',sample_person_rows=len(d),
 assumption='equal O*NET children within SOC, then equal explicit SOC members within PUMS group; not final methodology',
 unresolved_numeric_soc_groups='No undocumented prefix matching: SOC broad/minor codes without explicit detailed members remain unscored',
 coverage=reports,unmatched_22_34=unmatched.to_dict('records'),cz_sample_covered_weight=allocated.to_dict(),
 national_weighted_coverage='OPEN: no national PUMS downloaded; no national acceptance claim',
 telework_classification='OPEN: separate 2010->2019 concordance needed for older telework scores'))
 print([r for r in reports if r['survey_year']=='pooled'])
 print(unmatched.to_string(index=False))
