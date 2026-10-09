"""Bounded public-source retrieval; every attempt is logged, data remain ignored."""
import datetime as dt
import hashlib
import json
from pathlib import Path
import urllib.request
import urllib.error
import os
import ssl

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / 'data' / 'feasibility'
OUT = ROOT / 'results' / 'feasibility'
DATA.mkdir(parents=True, exist_ok=True)
OUT.mkdir(parents=True, exist_ok=True)
MANIFEST = OUT / 'source_manifest.jsonl'

def save(name, obj):
    (OUT / name).write_text(json.dumps(obj, indent=2, ensure_ascii=False, allow_nan=False) + '\n')

def fetch(name, url, *, method='GET', byte_range=None, cap=35_000_000, version='retrieved vintage'):
    record = dict(id=name, url=url, method=method, requested_range=byte_range,
                  version=version, retrieved_at_utc=dt.datetime.now(dt.timezone.utc).isoformat())
    headers = {'User-Agent': 'Research feasibility audit (bounded public data)', 'Accept-Encoding': 'identity'}
    backend = os.environ.get('FEASIBILITY_HTTP_BACKEND', 'urllib')
    record['http_backend'] = backend
    if byte_range:
        headers['Range'] = 'bytes=' + byte_range
    try:
        if backend == 'curl_cffi_chrome':
            from curl_cffi import requests
            # Bounded streaming, certificate validation retained; no proxy credential.
            with requests.Session(impersonate='chrome') as session:
                response = session.request(method, url, headers={k:v for k,v in headers.items() if k!='User-Agent'},
                                           timeout=45, stream=True, verify='/etc/ssl/cert.pem')
                try:
                    record.update(status=response.status_code, final_url=response.url,
                                  headers={k.lower():v for k,v in response.headers.items()})
                    response.raise_for_status()
                    if byte_range and response.status_code != 206:
                        raise ValueError('Range not honored; refusing full-object GET')
                    if method != 'HEAD' and int(response.headers.get('Content-Length','0')) > cap:
                        raise ValueError('Content-Length exceeds cap')
                    body = bytearray()
                    if method != 'HEAD':
                        for chunk in response.iter_content(chunk_size=65536):
                            body.extend(chunk)
                            if len(body)>cap:raise ValueError('Response exceeded cap')
                    body=bytes(body)
                    record.update(bytes=len(body),sha256=hashlib.sha256(body).hexdigest() if method!='HEAD' else None,
                                  hash_scope='response body only' if method!='HEAD' else 'metadata only; no object hash')
                    if method!='HEAD':(DATA/name).write_bytes(body)
                    return body,record
                finally:
                    response.close()
        ca = '/etc/ssl/cert.pem'
        context = ssl.create_default_context(cafile=ca) if Path(ca).exists() else ssl.create_default_context()
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers, method=method), timeout=45, context=context) as response:
            record.update(status=response.status, final_url=response.url,
                          headers={k.lower(): v for k, v in response.headers.items()})
            if byte_range and response.status != 206:
                raise ValueError('Range not honored; refusing national/full-object GET')
            if method != 'HEAD' and int(response.headers.get('Content-Length', '0')) > cap:
                raise ValueError('Content-Length exceeds bounded-download cap')
            body = response.read(cap + 1) if method != 'HEAD' else b''
            if len(body) > cap:
                raise ValueError('Response exceeded bounded-download cap')
            record.update(bytes=len(body), sha256=hashlib.sha256(body).hexdigest() if method != 'HEAD' else None,
                          hash_scope='response body only' if method != 'HEAD' else 'metadata only; no object hash')
            if method != 'HEAD':
                (DATA / name).write_bytes(body)
            return body, record
    except Exception as exc:
        record['error'] = str(exc)
        if isinstance(exc, urllib.error.HTTPError):
            record['status'] = exc.code
        return None, record
    finally:
        # Public sites can return anti-bot session cookies. Do not commit cookies.
        response_headers = record.get('headers', {})
        removed = [k for k in response_headers if k in {'set-cookie','authorization','proxy-authorization'}]
        for k in removed:response_headers.pop(k)
        if removed:record['redacted_header_names'] = removed
        with MANIFEST.open('a') as stream:
            stream.write(json.dumps(record, ensure_ascii=False) + '\n')

def require(name, url, **kwargs):
    body, record = fetch(name, url, **kwargs)
    if body is None:
        raise RuntimeError(record)
    return body
