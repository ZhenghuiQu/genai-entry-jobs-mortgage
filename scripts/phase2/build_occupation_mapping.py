"""Explicit Census composites and BLS SOC hierarchy; no inferred X/Y membership."""
import hashlib,json,re,sys
from pathlib import Path
import numpy as np
import pandas as pd
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'feasibility'))
from common import ROOT,DATA,OUT,save
BLS='https://www.bls.gov/soc/2018/soc_structure_2018.pdf'
PUMS='https://www2.census.gov/programs-surveys/demo/guidance/industry-occupation/2018-ACS-PUMS-and-2018-SIPP-Public-Use-Occupation-Code-List.xlsx'
ONET='https://www.onetcenter.org/taxonomy/2019/soc/2019_to_SOC_Crosswalk.xlsx?fmt=xlsx'
def hierarchy():
 text=(ROOT/'audit/phase2_soc_official_web_extract.txt').read_text()
 lines={int(m[1]):m[2] for m in re.finditer(r'^L(\d+)(?:@P[\d-]+)?: (.*)$',text,re.M)}
 assert set(lines)==set(range(1556)), 'Official web extract incomplete'
 nodes={};parents={};rows=[];major=minor=broad=None
 # Level rules are from the official coding guide; actual parentage from ordered BLS rows.
 special_minor={'15-1200','31-1100','51-5100'}
 for line,title in sorted(lines.items()):
  m=re.match(r'(\d{2}-\d{4})(?: (.*))?$',title)
  if not m:continue
  code=m[1];label=m[2] or ''
  if code.endswith('0000'):level='major';major=code;minor=broad=None;anc=[]
  elif code.endswith('000') or code in special_minor:level='minor';minor=code;broad=None;anc=[major]
  elif code.endswith('0'):level='broad';broad=code;anc=[major,minor]
  else:level='detailed';anc=[major,minor,broad]
  assert None not in anc and code not in nodes
  nodes[code]=dict(level=level,title=label,source_line=line,page=int(re.search(rf'^L{line}@P(\d+)',text,re.M)[1])+1)
  parents[code]=anc
  rows.append(dict(soc=code,level=level,major=major,minor=minor,broad=broad,title=label,source_line=line,source_url=BLS))
 counts=pd.Series([v['level'] for v in nodes.values()]).value_counts().to_dict()
 assert counts=={'detailed':867,'broad':459,'minor':98,'major':23},counts
 members={c:([c] if v['level']=='detailed' else [d for d,a in parents.items() if c in a and nodes[d]['level']=='detailed']) for c,v in nodes.items()}
 pd.DataFrame(rows).to_csv(OUT/'soc2018_official_hierarchy.csv',index=False)
 return nodes,members,counts

def build():
 nodes,hm,counts=hierarchy()
 o=pd.read_excel(DATA/'onet_soc2018.xlsx',header=3,dtype=str);o.columns=o.columns.str.strip()
 o=o[o['O*NET-SOC 2019 Code'].str.fullmatch(r'\d{2}-\d{4}\.\d{2}',na=False)]
 e=pd.read_csv(DATA/'exposure.csv',dtype={'O*NET-SOC Code':str})
 assert e['O*NET-SOC Code'].is_unique and e.dv_rating_beta.between(0,1).all()
 j=o.merge(e,left_on='O*NET-SOC 2019 Code',right_on='O*NET-SOC Code',how='left',validate='one_to_one')
 assert set(e['O*NET-SOC Code'])<=set(o['O*NET-SOC 2019 Code'])
 beta=j.groupby('2018 SOC Code').dv_rating_beta.mean();beta=beta.dropna()
 child_total=j.groupby('2018 SOC Code').size();child_rated=j.groupby('2018 SOC Code').dv_rating_beta.count()
 # A detailed SOC is fully scored only when all official O*NET children are rated.
 complete_soc=set(child_total.index[child_total.eq(child_rated)])
 raw=pd.read_excel(DATA/'census_2018_pums.xlsx',sheet_name='ACS',header=None,dtype=str).fillna('')
 groups={};current=None
 for row_no,row in raw.iterrows():
  code,soc,title=[x.strip() for x in row.tolist()]
  if re.fullmatch(r'\d{4}',code) and re.fullmatch(r'\d{2}-[\dXY]{4}',soc):
   current=code;groups[code]=dict(occp=code,socp=soc.replace('-',''),official_description=title,original_soc=soc,raw_components=[],component_rows=[],nested_composites=[])
   if not re.search('[XY]',soc):groups[code]['raw_components']=[soc];groups[code]['component_rows']=[int(row_no)+1]
   groups[code]['root_excel_row']=int(row_no)+1
  elif not code and re.fullmatch(r'\d{2}-\d{4}',soc) and current:
   groups[current]['raw_components'].append(soc);groups[current]['component_rows'].append(int(row_no)+1)
  elif not code and re.fullmatch(r'\d{2}-[\dXY]{4}',soc) and current:
   groups[current]['nested_composites'].append(soc)
  elif code and not re.fullmatch(r'\d{4}',code):current=None
 assert len(groups)==529
 for g in groups.values():
  valid=[s for s in g['raw_components'] if s in hm];invalid=[s for s in g['raw_components'] if s not in hm]
  members=sorted({d for s in valid for d in hm[s]});rated=[s for s in members if s in complete_soc];unrated=sorted(set(members)-set(rated))
  g.update(documented_detailed_members=members,rated_soc_members=[s for s in members if s in beta],fully_rated_soc_members=rated,unrated_soc_members=[s for s in members if s not in beta],partially_rated_soc_members=[s for s in members if s in beta and s not in complete_soc],score_incomplete_soc_members=unrated,invalid_source_members=invalid,
   n_detailed_members=len(members),n_rated_members=sum(s in beta for s in members),n_fully_rated_members=len(rated),membership_status='OPEN_SOURCE_INCONSISTENCY' if invalid else ('COMPLETE_DOCUMENTED' if members else 'OPEN_COMPOSITE'),
   source_level='Census composite X/Y' if re.search('[XY]',g['original_soc']) else nodes.get(g['original_soc'],{}).get('level','unknown'),
   mapping_status='C_census_military_unspecified' if g['occp']=='9830' else ('E_source_inconsistency' if invalid else ('C_ambiguous_composite' if not members else ('B_unrated_detailed_or_child' if unrated else 'covered'))),
   aggregation_rule='Equal rated O*NET children within detailed SOC, then equal detailed SOC members; fully rated groups only',
   ambiguity_status='UNKNOWN_INTERNAL_EMPLOYMENT_SHARES' if len(members)>1 or any(child_total.get(s,0)>1 for s in members) else 'SINGLE_RATED_MEMBER',
   major_group=nodes[valid[0]].get('title','') if valid and nodes[valid[0]]['level']=='major' else (members[0][:2] if members else g['original_soc'][:2]),
   terminal_all_other_members=[s for s in members if s.endswith('9')],
   unscored_onet_members=j.loc[j['2018 SOC Code'].isin(members)&j.dv_rating_beta.isna(),'O*NET-SOC 2019 Code'].tolist(),
   source_documentation=dict(pums_url=PUMS,pums_sheet='ACS',bls_url=BLS,onet_url=ONET),release_status='PROVISIONAL_AUDIT_NOT_FINAL')
  g['beta_available_soc_diagnostic']=float(beta.loc[members].mean()) if members and not invalid and all(v in beta for v in members) else None
  g['beta_primary']=float(beta.loc[members].mean()) if g['mapping_status']=='covered' else None
  allchildren=j[j['2018 SOC Code'].isin(members)]
  g['beta_equal_onet_children']=float(allchildren.dv_rating_beta.mean()) if g['mapping_status']=='covered' else None
  g['beta_member_min']=float(allchildren.dv_rating_beta.min()) if g['mapping_status']=='covered' else None
  g['beta_member_max']=float(allchildren.dv_rating_beta.max()) if g['mapping_status']=='covered' else None
  g['beta_lower']=g['beta_primary'] if g['beta_primary'] is not None else 0.
  g['beta_upper']=g['beta_primary'] if g['beta_primary'] is not None else 1.
  g['correction_candidate']=dict(original='40-9095',candidate='49-9095',basis='Explicit component Census 7550; separate official Census occupation list row 547 and O*NET crosswalk both map 7550 title to 49-9095',status='DOCUMENTED_CANDIDATE_NO_PUMS_ERRATUM; not applied to primary') if g['occp']=='7640' else None
 rows=[]
 for g in groups.values():rows.append({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in g.items()})
 pd.DataFrame(rows).to_csv(OUT/'occupation_mapping_final.csv',index=False)
 missing=j[j.dv_rating_beta.isna()][['O*NET-SOC 2019 Code','2018 SOC Code','O*NET-SOC 2019 Title']]
 missing.to_csv(OUT/'phase2_unrated_onet_members.csv',index=False)
 summary=dict(bls_counts=counts,ratings=len(e),official_onet_children=len(o),rated_soc_groups=len(beta),complete_soc_groups=len(complete_soc),unrated_onet_children=len(missing),pums_groups=len(groups),mapping_status_counts=pd.Series([g['mapping_status'] for g in groups.values()]).value_counts().to_dict(),release_status='PROVISIONAL_AUDIT_NOT_FINAL',original_feasibility_commit='3f363bca62b6d8938ee8f95696465361d2092476')
 save('phase2_occupation_summary.json',summary);print(summary)
 return pd.DataFrame(groups.values())
if __name__=='__main__':build()
