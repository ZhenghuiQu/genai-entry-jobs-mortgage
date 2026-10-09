"""Official ACS bulk-summary route when the no-key API returns HTML."""
from common import fetch,DATA,save
import csv,io,zipfile
base='https://www2.census.gov/programs-surveys/acs/summary_file/2019/'
if __name__=='__main__':
 body,rec=fetch('acs_lookup.txt',base+'documentation/user_tools/ACS_5yr_Seq_Table_Number_Lookup.txt',cap=3_000_000)
 if body:
  rows=list(csv.DictReader(io.StringIO(body.decode('latin1'))));print(rows[:2],flush=True)
  wanted=[r for r in rows if r.get('Table ID') in ['B25077','B19013','B25003','B01003']]
  save('acs_lookup_selected.json',wanted);print(wanted,flush=True)
  for seq in sorted({r['Sequence Number'] for r in wanted}):
   name=f'20195de{int(seq):04d}000.zip'
   _,r=fetch('acs_de_'+name,base+'data/5_year_seq_by_state/Delaware/All_Geographies_Not_Tracts_Block_Groups/'+name)
   print(name,r.get('status'),flush=True)
 fetch('acs_de_geo.csv',base+'data/5_year_seq_by_state/Delaware/All_Geographies_Not_Tracts_Block_Groups/g20195de.csv')
 fetch('ct_final_changes.pdf','https://www2.census.gov/geo/pdfs/reference/ct_county_equiv_change.pdf')
