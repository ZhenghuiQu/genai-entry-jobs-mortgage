"""Phase 2 official inputs; stream national ZIP without expanding person CSVs."""
import argparse, datetime as dt, hashlib, json, shutil, sys, time, urllib.request, ssl, zipfile
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'feasibility'))
from common import DATA, OUT, fetch, save, MANIFEST
SOURCES={
 'soc_structure_2018.xlsx':'https://www.bls.gov/soc/2018/soc_structure_2018.xlsx',
 'soc_coding_2018.pdf':'https://www.bls.gov/soc/2018/soc_2018_class_and_coding_structure.pdf',
 'ct_cousub22_blkgrp20.txt':'https://www2.census.gov/geo/docs/maps-data/data/rel2022/acs22_cousub22_blkgrp20_st09.txt',
 'ct_cousub22_tract22.txt':'https://www2.census.gov/geo/docs/maps-data/data/rel2022/acs22_cousub22_tract22_st09.txt',
 'census_2018_pums_phase2.xlsx':'https://www2.census.gov/programs-surveys/demo/guidance/industry-occupation/2018-ACS-PUMS-and-2018-SIPP-Public-Use-Occupation-Code-List.xlsx',
 'census_2018_soc_phase2.xlsx':'https://www2.census.gov/programs-surveys/demo/guidance/industry-occupation/2018-occupation-code-list-and-crosswalk.xlsx',
}
def national():
 path=DATA/'pums_us_phase2.zip';partial=path.with_suffix('.partial')
 rec=dict(id=path.name,url='https://www2.census.gov/programs-surveys/acs/data/pums/2019/5-Year/csv_pus.zip',version='ACS 2015-2019 5-Year person PUMS',retrieved_at_utc=dt.datetime.now(dt.timezone.utc).isoformat())
 free=shutil.disk_usage(DATA).free
 rec['free_bytes_before']=free
 if free<8*1024**3:raise RuntimeError('Less than 8 GiB free; refusing download')
 if path.exists():
  print('National ZIP already present; validate against acquisition manifest in audit step.',flush=True);return
 response=session=None
 try:
  from curl_cffi import requests
  session=requests.Session(impersonate='chrome')
  digest=hashlib.sha256();n=0;start=time.monotonic();last=start
  response=session.get(rec['url'],headers={'Accept-Encoding':'identity'},timeout=180,stream=True,verify='/etc/ssl/cert.pem')
  rec['status']=response.status_code
  response.raise_for_status()
  with partial.open('wb') as out:
   length=int(response.headers.get('Content-Length',0));rec.update(status=response.status_code,content_length=length,last_modified=response.headers.get('Last-Modified'))
   if not 0<length<3_000_000_000:raise RuntimeError('Unexpected national ZIP size')
   for chunk in response.iter_content(chunk_size=1024*1024):
    n+=len(chunk)
    if n>3_000_000_000:raise RuntimeError('Download cap exceeded')
    digest.update(chunk);out.write(chunk)
    if time.monotonic()-last>15:print(f'ACS compressed download {n/1e6:.0f}/{length/1e6:.0f} MB',flush=True);last=time.monotonic()
  if n!=length:raise RuntimeError('Length mismatch')
  with zipfile.ZipFile(partial) as z:
   rec['entries']=[dict(name=i.filename,bytes=i.file_size,compressed_bytes=i.compress_size,crc32=i.CRC) for i in z.infolist()]
   assert len([i for i in z.namelist() if i.endswith('.csv')])==4
  partial.rename(path);rec.update(bytes=n,sha256=digest.hexdigest(),seconds=time.monotonic()-start,hash_scope='complete compressed archive')
 except Exception as exc:
  rec['error']=str(exc);raise
 finally:
  if response is not None:response.close()
  if session is not None:session.close()
  with MANIFEST.open('a') as f:f.write(json.dumps(rec)+'\n')
  save('phase2_national_acquisition.json',rec)
 print('National ZIP download complete',flush=True)
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--national',action='store_true');args=a.parse_args()
 records=[]
 for name,url in SOURCES.items():
  if (DATA/name).exists():continue
  b,r=fetch(name,url,version='Official 2018 taxonomy or 2022 CT relationship; Phase 2 retrieved vintage',cap=5_000_000)
  records.append(r);print(name,r.get('status'),r.get('error'),flush=True)
 log=OUT/'phase2_small_acquisition.json'
 old=json.loads(log.read_text()) if log.exists() else []
 save('phase2_small_acquisition.json',old+records)
 if args.national:national()
