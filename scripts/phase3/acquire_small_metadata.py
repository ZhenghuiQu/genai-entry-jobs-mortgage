"""Optional, sequential BLS taxonomy metadata only; never acquire microdata."""
import datetime
import hashlib
import io
import json
from pathlib import Path
import shutil
import ssl
import sys
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[2]
CAP = 262144  # 256 KiB per file, 512 KiB maximum successfully retained metadata payload.
FLOOR = 48 * 1024**3  # Preserve the other project's strictest observed safeguard.
FILES = {
    'phase3_nem_onet.xlsx': 'https://www.bls.gov/emp/classifications-crosswalks/nem-onet-to-soc-crosswalk.xlsx',
    'phase3_nem_acs.xlsx': 'https://www.bls.gov/emp/classifications-crosswalks/nem-occcode-acs-crosswalk.xlsx',
}

if __name__ == '__main__':
    backend = 'curl_cffi_chrome' if '--existing-browser-client' in sys.argv else 'urllib'
    manifest = ROOT / 'results/feasibility/phase3_metadata_acquisition.json'
    records = json.loads(manifest.read_text()) if manifest.exists() else []
    for name, url in FILES.items():
        if (ROOT / 'data/feasibility' / name).exists():
            continue
        record = dict(name=name, url=url, cap_bytes=CAP, backend=backend,
                      retrieved_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
        try:
            assert shutil.disk_usage(ROOT).free > FLOOR + 5 * 1024**2, 'Preserve 48 GiB floor plus audit reserve'
            if backend == 'curl_cffi_chrome':
                from curl_cffi import requests  # Already installed; no environment changes.
                with requests.Session(impersonate='chrome') as session:
                    response = session.get(url, timeout=15, stream=True, verify='/etc/ssl/cert.pem', headers={'Accept-Encoding': 'identity'})
                    try:
                        record.update(status=response.status_code, final_url=response.url)
                        response.raise_for_status()
                        assert int(response.headers.get('Content-Length', 0)) <= CAP
                        body = bytearray()
                        for chunk in response.iter_content(chunk_size=8192):
                            assert len(body) + len(chunk) < CAP, 'Refuse file exceeding cap'
                            body.extend(chunk)
                        body = bytes(body)
                    finally:
                        response.close()
            else:
                request = urllib.request.Request(url, headers={'User-Agent': 'Occupational concordance metadata audit', 'Accept-Encoding': 'identity'})
                with urllib.request.urlopen(request, timeout=15, context=ssl.create_default_context(cafile='/etc/ssl/cert.pem')) as response:
                    record.update(status=response.status, final_url=response.url)
                    assert int(response.headers.get('Content-Length', 0)) <= CAP, 'File exceeds explicit cap'
                    body = response.read(CAP)
                    assert len(body) < CAP, 'At cap: refuse possibly truncated file'
            assert zipfile.is_zipfile(io.BytesIO(body)), 'Not an XLSX ZIP'
            with zipfile.ZipFile(io.BytesIO(body)) as archive:
                assert sum(i.file_size for i in archive.infolist()) < 8 * 1024**2, 'Expanded metadata too large'
                assert 'xl/workbook.xml' in archive.namelist()
            (ROOT / 'data/feasibility' / name).write_bytes(body)
            record.update(bytes=len(body), sha256=hashlib.sha256(body).hexdigest(), outcome='ACQUIRED_METADATA_ONLY')
        except Exception as exc:
            record.update(outcome='NOT_ACQUIRED', error=str(exc))
        records.append(record)
    manifest.write_text(json.dumps(records, indent=2) + '\n')
    print(json.dumps(records, indent=2))
