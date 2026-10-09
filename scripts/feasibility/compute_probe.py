"""Measured bounded HMDA aggregation, no model, coefficient, or significance."""
import csv,gzip,json,os,platform,resource,shutil,subprocess,time
from collections import Counter
import duckdb
from common import DATA,OUT,save

def rss_bytes():
 r=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
 return int(r if platform.system()=='Darwin' else r*1024)

def reference(path):
 with path.open() as f:
  return Counter((r['county_code'],r['applicant_age'],r['action_taken']) for r in csv.DictReader(f))

if __name__=='__main__':
 baseline=rss_bytes();tests=[]
 for name in ['hmda_2018_sample.csv','hmda_2025_sample.csv','hmda_ct_2025.csv']:
  path=DATA/name
  if not path.exists():continue
  before=time.perf_counter();ref=reference(path);reference_time=time.perf_counter()-before
  con=duckdb.connect();con.execute("SET memory_limit='256MB'");con.execute('SET threads=2')
  con.execute("SET preserve_insertion_order=false")
  sql='SELECT county_code,applicant_age,action_taken,count(*) FROM read_csv(?,all_varchar=true,header=true,nullstr=\'\',strict_mode=true) GROUP BY ALL'
  before=time.perf_counter();rows=con.execute(sql,[str(path)]).fetchall();elapsed=time.perf_counter()-before
  got={tuple('' if v is None else v for v in r[:3]):r[3] for r in rows}
  assert got==dict(ref),'DuckDB disagrees with independent csv.Counter'
  # A genuinely compressed read exercises decompression and streaming projection.
  gz=DATA/(name+'.gz')
  with path.open('rb') as src,gzip.open(gz,'wb') as dst:shutil.copyfileobj(src,dst)
  before=time.perf_counter();zrows=con.execute(sql,[str(gz)]).fetchall();zelapsed=time.perf_counter()-before
  assert set(zrows)==set(rows)
  tests.append(dict(file=name,bytes=path.stat().st_size,rows=sum(ref.values()),cells=len(ref),duckdb_seconds=elapsed,
    python_counter_seconds=reference_time,rows_per_second=sum(ref.values())/elapsed,
    gzip_bytes=gz.stat().st_size,gzip_duckdb_seconds=zelapsed,
    peak_process_rss_bytes=rss_bytes(),memory_limit='256MB',threads=2,reference_agreement=True,
    scalar_probe='county x age x action counts only; no treatment model'))
  con.close()
 disk=shutil.disk_usage(DATA)
 machine=dict(platform=platform.platform(),cpu_count=os.cpu_count(),python=platform.python_version(),duckdb=duckdb.__version__,disk_total_bytes=disk.total,disk_free_bytes=disk.free,rss_before_bytes=baseline,peak_rss_bytes=rss_bytes())
 if platform.system()=='Darwin':
  try:machine['physical_memory_bytes']=int(subprocess.check_output(['sysctl','-n','hw.memsize'],stderr=subprocess.PIPE))
  except subprocess.CalledProcessError:machine['physical_memory_bytes']=None;machine['physical_memory_status']='sandbox blocks sysctl; retry outside sandbox'
 r=json.loads((OUT/'hmda_snapshot_probe.json').read_text())
 archives={y:dict(zip_bytes=int(v['head']['headers']['content-length']),csv_bytes=sum(x['uncompressed_bytes'] for x in v['zip_entries'])) for y,v in r.items() if y.isdigit() and v.get('zip_entries')}
 result=dict(machine=machine,tests=tests,hmda_archive_sizes=archives,
 zipped_total_bytes=sum(x['zip_bytes'] for x in archives.values()),expanded_total_bytes=sum(x['csv_bytes'] for x in archives.values()),
 sequential_largest_csv_bytes=max(x['csv_bytes'] for x in archives.values()),
 national_projection_status='OPEN: prefix/one-state benchmarks validate parser and arithmetic only; no national timing or peak memory guarantee',
 peak_memory_notes='DuckDB memory_limit does not bound whole-process RSS; observed RSS includes Python and reference Counter')
 save('compute_audit.json',result);print(result)
