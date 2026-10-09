"""Local schema/code/sentinel audit of the downloaded bounded probes."""
import csv,json
from collections import Counter
from common import DATA,OUT,save
from hmda_probe import inspect_csv,FIELDS
if __name__=='__main__':
 r=json.loads((OUT/'hmda_snapshot_probe.json').read_text())
 reference=None;schema=[];codes=[];funnel=[]
 for name,v in r.items():
  path=DATA/(f'hmda_{name}_sample.csv' if name.isdigit() else f'hmda_{name}.csv')
  if not path.exists():continue
  s=inspect_csv(path.read_bytes());v['sample']=s
  header=s['header']
  if reference is None:reference=header
  schema.append(dict(source=name,rows=s['rows'],n_columns=len(header),required_missing=s['required_missing'],added_vs_2018=sorted(set(header)-set(reference)),removed_vs_2018=sorted(set(reference)-set(header)),column_order_same=header==reference))
  for field,vals in s['fields'].items():
   codes.append(dict(source=name,field=field,csv_column=vals['csv_column'],n_unique=vals['n_unique'],observed_codes=vals['codes'],blank=vals['blank'],NA=vals['NA'],Exempt=vals['Exempt'],code1111=vals['1111']))
  rows=list(csv.DictReader(path.open()))
  stages=[('all',lambda x:True),('home_purchase',lambda x:x['loan_purpose']=='1'),('actions_1_5',lambda x:x['action_taken'] in ['1','2','3','4','5']),('first_lien',lambda x:x['lien_status']=='1'),('principal_residence',lambda x:x['occupancy_type']=='1'),('site_built',lambda x:x['construction_method']=='1'),('one_four_units',lambda x:x['total_units'] in ['1','2','3','4']),('reverse_no_or_exempt',lambda x:x['reverse_mortgage'] in ['2','1111','Exempt']),('closed_end_no_or_exempt',lambda x:x.get('open_end_line_of_credit',x.get('open-end_line_of_credit')) in ['2','1111','Exempt']),('business_no_or_exempt',lambda x:x['business_or_commercial_purpose'] in ['2','1111','Exempt'])]
  for label,rule in stages:
   rows=[x for x in rows if rule(x)];funnel.append(dict(source=name,stage=label,retained=len(rows)))
 save('hmda_snapshot_probe.json',r);save('hmda_schema_comparison.json',schema);save('hmda_field_codes.json',codes);save('hmda_filter_funnel.json',funnel)
 print(schema)
 print({f:r['2025']['sample']['fields'][f] for f in FIELDS if f not in ['county_code','lei']})
