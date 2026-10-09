from pathlib import Path
import pandas as pd
from pypdf import PdfReader
p=Path('data/feasibility')
for n in ['census_2018_soc.xlsx','census_2018_pums.xlsx']:
 x=pd.ExcelFile(p/n); print(n,x.sheet_names)
 for s in x.sheet_names:
  d=pd.read_excel(x,s,header=None,dtype=str); print(s,d.shape); print(d.head(12).to_string(index=False,header=False))
for n in ['exposure.csv','onet_walk.csv','onet_2019.csv','onet_2010.csv']:
 d=pd.read_csv(p/n);print(n,d.shape,d.columns.tolist()); print(d.head(4).to_string(index=False))
d=pd.read_csv(p/'exposure.csv'); codes=set(d['O*NET-SOC Code'])
for n in ['onet_2019.csv','onet_2010.csv']:
 o=pd.read_csv(p/n); oc=set(o.iloc[:,0]);print(n,'membership',len(codes&oc),'outside',len(codes-oc));print(sorted(codes-oc)[:20])
for n in ['county_changes.pdf','pums_readme.pdf']:
 reader=PdfReader(p/n); text='\n'.join(x.extract_text() for x in reader.pages)
 (p/(n+'.txt')).write_text(text)
 print(n, text if n.startswith('county') else '\n'.join(x for x in text.splitlines() if any(t in x for t in ['occupation','Occupation','SOCP','2018','2017','2015'])))
