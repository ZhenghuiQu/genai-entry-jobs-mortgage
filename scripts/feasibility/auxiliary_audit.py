"""Coding and missingness only, no labor mechanism estimation."""
import csv,io,json,re,zipfile
import pandas as pd
from common import DATA,OUT,save
if __name__=='__main__':
 lookup=json.loads((OUT/'acs_lookup_selected.json').read_text());geos=list(csv.reader((DATA/'acs_de_geo.csv').open()))
 # Layout: SUMLEVEL index 2, component index 3, LOGRECNO index 4,
 # state index 9, county index 10, GEOID index 48, name index 49.
 county={r[4]:dict(fips=r[9]+r[10],name=r[49]) for r in geos if r[2]=='050' and r[3]=='00'}
 results={k:dict(v) for k,v in county.items()}
 specifications={}
 for r in lookup:
  if not r['Start Position']:continue
  table=r['Table ID'];seq=r['Sequence Number'];start=int(r['Start Position'])-1
  specifications[table]=dict(sequence=seq,column_1_based=start+1,universe=next(x['Table Title'] for x in lookup if x['Table ID']==table and x['Table Title'].startswith('Universe')))
  path=DATA/f'acs_de_20195de{seq}000.zip'
  with zipfile.ZipFile(path) as z:
   estimates=list(csv.reader(io.StringIO(z.read(f'e20195de{seq}000.txt').decode())))
  for x in estimates:
   if x[5] in results:
    results[x[5]][table+'_001E']=x[start]
    if table=='B25003':results[x[5]]['B25003_002E']=x[start+1]
 for r in results.values():
  r['home_value_income_ratio']=float(r['B25077_001E'])/float(r['B19013_001E'])
  r['valid_positive_medians']=float(r['B25077_001E'])>0 and float(r['B19013_001E'])>0
 api=(DATA/'acs_counties.json').read_text();api_status='HTML Missing Key; NOT county data' if '<title>Missing Key</title>' in api else 'unexpected response'
 variables=json.loads((DATA/'acs_variables.json').read_text())['variables']
 labels={k:variables[k] for k in ['B25077_001E','B19013_001E','B25003_002E','B01003_001E']}
 qwi=json.loads((OUT/'qwi_versions.json').read_text());ends={};failures={}
 for st,v in qwi.items():
  if not v['text']:failures[st]=v['retrieval'].get('error');continue
  line=v['text'].splitlines()[0];m=re.search(r'(\d{4}:\d)-(\d{4}:\d)',line)
  ends[st]=m.group(2) if m else None
 with zipfile.ZipFile(DATA/'pums_de.zip') as z:
  d=pd.read_csv(z.open('psam_p10.csv'),dtype=str,keep_default_na=False,usecols=['AGEP','ESR','SCHL','NAICSP','SOCP','PWGTP','ST','PUMA'])
 young=d[d.ESR.isin(['1','2']) & d.AGEP.astype(int).between(22,34)]
 pop=pd.read_csv(DATA/'pop2019.csv',encoding='latin1',dtype=str);pop=pop[pop.SUMLEV=='050']
 fhfa_bytes=(DATA/'fhfa_county.csv').read_bytes()
 fhfa_workbook = pd.ExcelFile(io.BytesIO(fhfa_bytes)) if fhfa_bytes.startswith(b'PK') else None
 hpi=pd.read_excel(fhfa_workbook,header=5,dtype=str) if fhfa_workbook else pd.read_csv(DATA/'fhfa_county.csv',dtype=str)
 tele=pd.read_csv(DATA/'telework.csv',dtype=str)
 save('auxiliary_audit.json',dict(acs_api_status=api_status,acs_variables=labels,acs_bulk_specifications=specifications,
 acs_de_counties=list(results.values()),acs_national_missingness='OPEN: only DE bulk values inspected',
 population=dict(rows=len(pop),key_columns=['STATE','COUNTY'],weight='POPESTIMATE2019',missing_weight=int(pop.POPESTIMATE2019.eq('').sum()),duplicate_keys=int(pop.duplicated(['STATE','COUNTY']).sum()),region_codes=sorted(pop.REGION.unique()),division_codes=sorted(pop.DIVISION.unique())),
 qwi_end_quarters=ends,qwi_version_failures=failures,qwi_states_total=len(ends),qwi_end2025q4_count=sum(x=='2025:4' for x in ends.values()),
 young_regional_characteristics=dict(rows=len(young),SCHL_missing=int(young.SCHL.eq('').sum()),NAICSP_missing=int(young.NAICSP.eq('').sum()),SCHL_codes=sorted(young.SCHL.unique()),NAICSP_codes=sorted(young.NAICSP.unique())),
 fhfa=dict(rows=len(hpi),format='XLSX despite .csv request' if fhfa_workbook else 'CSV',sheets=fhfa_workbook.sheet_names if fhfa_workbook else None,columns=list(hpi.columns),missing_by_column=hpi.isna().sum().to_dict()),telework=dict(rows=len(tele),columns=list(tele.columns),code_examples=tele.iloc[:3,0].tolist()),
 FHA_share='OPEN: sample HMDA loan_type observed, national 2018-2019 age-specific baseline not collected',
 affordability_aggregation='OPEN: weighted county medians are a regional index, not a CZ median; owner units vs population and order of ratio/log need reconciliation'))
 print('ACS county medians/weights validated:',list(results.values()))
 print('QWI endpoints:',len(ends),'to2025Q4',sum(x=='2025:4' for x in ends.values()),'exceptions',{s:q for s,q in ends.items() if q!='2025:4'})
