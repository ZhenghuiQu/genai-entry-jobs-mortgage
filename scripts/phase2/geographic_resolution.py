"""Official town relationship bridge, exact only where old-county CZ is unique."""
import io,json,re,sys
from pathlib import Path
import pandas as pd
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'feasibility'))
from common import ROOT,DATA,OUT,save
from geography_audit import stata

def records(name,expected):
 text=(ROOT/'audit'/name).read_text();lines={int(m[1]):m[2] for m in re.finditer(r'^L(\d+): (.*)$',text,re.M)}
 assert set(lines)==set(range(expected)), f'Incomplete official relationship extract: {name}'
 return pd.read_csv(io.StringIO('\n'.join(lines[i] for i in range(expected))),sep='|',dtype=str)
def run():
 bg=records('phase2_ct_relationship_web_records.txt',2751);tr=records('phase2_ct_tract_web_records.txt',907)
 county=stata('dorn_county.zip');county['fips']=county.cty_fips.astype(int).astype(str).str.zfill(5);cz=dict(zip(county.fips,county.czone.astype(int)))
 # Keep all positive area intersections; no largest-area or population assignment.
 bg=bg[(pd.to_numeric(bg.AREALAND_PART)+pd.to_numeric(bg.AREAWATER_PART))>0].copy();bg['old_county']=bg.GEOID_BLKGRP_20.str[:5];bg['new_region']=bg.GEOID_COUSUB_22.str[:5];bg['cz']=bg.old_county.map(cz)
 town=bg.groupby('GEOID_COUSUB_22').agg(old_counties=('old_county',lambda x:sorted(set(x))),cz_members=('cz',lambda x:sorted(set(x))),town_name=('NAMELSAD_COUSUB_22','first')).reset_index()
 assert town.GEOID_COUSUB_22.is_unique and bg.cz.notna().all()
 bridge=tr[(pd.to_numeric(tr.AREALAND_PART)+pd.to_numeric(tr.AREAWATER_PART))>0].merge(town,on='GEOID_COUSUB_22',how='left',validate='many_to_one')
 assert bridge.cz_members.notna().all()
 tract=bridge.groupby('GEOID_TRACT_22').agg(cz_members=('cz_members',lambda x:sorted({v for vals in x for v in vals})),old_counties=('old_counties',lambda x:sorted({v for vals in x for v in vals}))).reset_index()
 tract['unique_cz']=tract.cz_members.map(lambda x:x[0] if len(x)==1 else None);tract['status']=tract.unique_cz.notna().map({True:'EXACT_UNIQUE_CZ_BY_OFFICIAL_TOWN_RELATION',False:'AMBIGUOUS_NO_ALLOCATION'})
 tract['source']='Census ACS22 COUSUB22-BLKGRP20 and COUSUB22-TRACT22; Dorn county-to-1990-CZ';tract.to_csv(OUT/'phase2_ct_tract_bridge.csv',index=False)
 regions=bg.groupby('new_region').agg(old_counties=('old_county',lambda x:sorted(set(x))),cz_members=('cz',lambda x:sorted(set(x)))).reset_index();regions['unique_cz']=regions.cz_members.map(lambda x:x[0] if len(x)==1 else None);regions.to_csv(OUT/'phase2_ct_region_membership.csv',index=False)
 tract_map=dict(zip(tract.GEOID_TRACT_22,tract.unique_cz));region_map=dict(zip(regions.new_region,regions.unique_cz));report=[]
 for year in [2018,2023,2024,2025]:
  d=pd.read_csv(DATA/f'hmda_ct_{year}.csv',dtype=str,keep_default_na=False);n=len(d)
  state_ok=d.state_code.eq('CT');known=d.county_code.str.fullmatch(r'\d{5}');mismatch=known & ~d.county_code.str.startswith('09');missing=~known
  # Missing county can be recovered only from an official known tract and consistent state.
  old=d.county_code.map(cz);trcz=d.census_tract.map(tract_map);rcz=d.county_code.map(region_map)
  tractknown=d.census_tract.str.fullmatch(r'\d{11}');tract_mismatch=tractknown & known & d.census_tract.str[:5].ne(d.county_code)
  mapped=(old.notna() | trcz.notna() | rcz.notna()) & state_ok & ~mismatch & ~tract_mismatch
  badtract=tractknown & ~d.census_tract.str.startswith('09');mapped &= ~badtract
  reason=pd.Series('unresolved_no_official_bridge',index=d.index);reason[missing]='missing_county_without_recovery';reason[d.census_tract.isin(tract.loc[tract.unique_cz.isna(),'GEOID_TRACT_22'])]='ambiguous_official_tract';reason[mismatch|tract_mismatch|badtract|~state_ok]='inconsistent_identifiers';reason[mapped]='mapped'
  report.append(dict(year=year,sample_scope='CT recorded purchase originations, all ages; not national application universe',rows=n,option_A_mapped_rows=int(mapped.sum()),option_A_coverage_percent=100*float(mapped.mean()),option_A_unmapped_reasons=reason[~mapped].value_counts().to_dict(),missing_county_rows=int(missing.sum()),county_state_inconsistent_rows=int(mismatch.sum()),tract_county_inconsistent_rows=int(tract_mismatch.sum()),option_B_consistent_CT_exclusion_rows=n,option_B_CT_retention_percent=0))
 # Cross-border zones are identified from all component county states, never dominant-state label.
 county['state']=county.fips.str[:2];states=county.groupby('czone').state.agg(lambda x:sorted(set(x)));ctcz=set(county.loc[county.state.eq('09'),'czone']);mi=set(county.loc[county.state.eq('26'),'czone'])
 pop=pd.read_csv(DATA/'pop2019.csv',dtype=str,encoding='latin1');pop=pop[pop.SUMLEV.eq('050')].copy();pop['fips']=pop.STATE.str.zfill(2)+pop.COUNTY.str.zfill(3);pop['pop']=pd.to_numeric(pop.POPESTIMATE2019)
 candidate=cz.copy();candidate['12086']=cz['12025'];candidate['46102']=cz['46113'];candidate['08014']=28900
 pop['cz']=pop.fips.map(candidate);partials=[]
 for excluded in [{'09'},{'09','26'}]:
  for c,x in pop[pop.cz.notna()].groupby('cz'):
   lost=x.loc[x.STATE.isin(excluded),'pop'].sum();kept=x.loc[~x.STATE.isin(excluded),'pop'].sum()
   if lost:partials.append(dict(excluded_states=','.join(sorted(excluded)),cz=int(c),population_total=int(x['pop'].sum()),population_excluded=int(lost),population_retained=int(kept),retained_population_share=float(kept/x['pop'].sum()),policy='Drop whole affected CZ recommended to avoid exposure/outcome geography mismatch; requires approval'))
 pd.DataFrame(partials).to_csv(OUT/'phase2_partial_cz_population.csv',index=False)
 inventory=[]
 for policy in ['retain_CT','exclude_CT','drop_CT_affected_CZs']:
  x=pop[~pop.STATE.isin(['02','15'])].copy()
  if policy=='exclude_CT':x=x[~x.STATE.eq('09')]
  if policy=='drop_CT_affected_CZs':x=x[~x.cz.isin(ctcz)]
  good=x.cz.notna();inventory.append(dict(policy=policy,county_rows=len(x),mapped_rows=int(good.sum()),population=int(x['pop'].sum()),mapped_population=int(x.loc[good,'pop'].sum()),coverage_percent=100*float(x.loc[good,'pop'].sum()/x['pop'].sum()),basis='2019 county population inventory, not HMDA coverage; candidate Broomfield approximation included'))
 save('phase2_geography_summary.json',dict(official_bg_relationship_rows=len(bg),towns=len(town),official_tracts=len(tract),unique_CZ_tracts=int(tract.unique_cz.notna().sum()),ambiguous_CZ_tracts=int(tract.unique_cz.isna().sum()),region_membership=regions.to_dict('records'),CT_samples=report,cross_state_CZs=int(states.map(len).gt(1).sum()),CT_affected_CZs=sorted(map(int,ctcz)),CT_cross_state_CZs=[int(c) for c in ctcz if len(states[c])>1],population_inventory=inventory,complete_national_HMDA_linkage='OPEN; bounded existing samples only',national_employment_loss_by_exclusion='OPEN; national ACS download 403',recommended_policy='Official tract/region bridge where unique; retain CT provisionally; no primary commitment until missing/ambiguous counts and national validation accepted'))
 print(report);print('official tracts',len(tract),'ambiguous',tract.unique_cz.isna().sum(),'cross-state CZs',states.map(len).gt(1).sum())
if __name__=='__main__':run()
