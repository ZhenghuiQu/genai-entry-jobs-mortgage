from common import fetch,save
from hmda_probe import directory
if __name__=='__main__':
 u='https://www2.census.gov/programs-surveys/acs/data/pums/2019/5-Year/csv_pus.zip'
 _,h=fetch('pums_us_size_head',u,method='HEAD')
 b,r=fetch('pums_us_directory.bin',u,byte_range='-65536',cap=65536)
 save('pums_resource_audit.json',dict(head=h,tail=r,zip_entries=directory(b) if b else None))
 print(h.get('status'),h.get('headers',{}).get('content-length'),r.get('status'))
