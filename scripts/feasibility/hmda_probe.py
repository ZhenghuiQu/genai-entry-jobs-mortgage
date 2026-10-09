"""Eight snapshot ZIP directories plus capped deterministic first-record probes."""
import csv
import io
import struct
import zlib
from collections import Counter
from common import fetch, DATA, save

FIELDS = ['activity_year','applicant_age','action_taken','loan_purpose','lien_status',
          'occupancy_type','construction_method','total_units','loan_type',
          'reverse_mortgage','open-end_line_of_credit','business_or_commercial_purpose',
          'county_code','state_code','lei']

def directory(tail):
    """Read ZIP central entries including ZIP64 sizes; no full archive required."""
    entries = []
    i = tail.find(b'PK\x01\x02')
    while i >= 0 and tail[i:i+4] == b'PK\x01\x02':
        h = struct.unpack_from('<4s6H3I5H2I', tail, i)
        nlen, elen, clen = h[10:13]
        name = tail[i+46:i+46+nlen].decode('utf-8')
        extra = tail[i+46+nlen:i+46+nlen+elen]
        usize, csize, offset = h[9], h[8], h[16]
        j = 0
        while j+4 <= len(extra):
            tag, length = struct.unpack_from('<HH', extra, j)
            if tag == 1:
                pos = j+4
                if usize == 0xffffffff:
                    usize = struct.unpack_from('<Q', extra, pos)[0]; pos += 8
                if csize == 0xffffffff:
                    csize = struct.unpack_from('<Q', extra, pos)[0]; pos += 8
                if offset == 0xffffffff:
                    offset = struct.unpack_from('<Q', extra, pos)[0]
            j += 4+length
        entries.append(dict(name=name, compressed_bytes=csize, uncompressed_bytes=usize,
                            local_offset=offset, method=h[4], crc32=h[7]))
        i += 46+nlen+elen+clen
    return entries

def partial_csv(raw):
    assert raw[:4] == b'PK\x03\x04'
    h = struct.unpack_from('<4s5H3I2H', raw)
    start = 30 + h[-2] + h[-1]
    assert h[3] == 8, 'Only deflate supported'
    dec = zlib.decompressobj(-15)
    output = dec.decompress(raw[start:], 20_000_000)
    # A partial last CSV record is intentionally discarded. HMDA has one line/row.
    output = output[:output.rfind(b'\n')+1]
    return output

def inspect_csv(body):
    rows = list(csv.DictReader(io.StringIO(body.decode('utf-8-sig'))))
    header = next(csv.reader(io.StringIO(body.decode('utf-8-sig'))))
    fields = {}
    for name in FIELDS:
        physical = 'open_end_line_of_credit' if name == 'open-end_line_of_credit' and 'open_end_line_of_credit' in header else name
        counts = Counter(row.get(physical, '<absent>') for row in rows)
        # Avoid committing individual lender identifiers; retain cardinality only.
        fields[name] = {'csv_column':physical, 'csv_storage_type':'text', 'n_unique':len(counts),
                        'codes':dict(sorted(counts.items())) if name != 'lei' else None,
                        'blank':counts.get('',0), 'NA':counts.get('NA',0),
                        'Exempt':counts.get('Exempt',0), '1111':counts.get('1111',0)}
    physical_fields = ['open_end_line_of_credit' if x=='open-end_line_of_credit' and 'open_end_line_of_credit' in header else x for x in FIELDS]
    return dict(rows=len(rows), header=header, required_missing=sorted(set(physical_fields)-set(header)), fields=fields,
                explicit_aliases={'open-end_line_of_credit':'open_end_line_of_credit'})

if __name__ == '__main__':
    result = {}
    for year in range(2018,2026):
        url = f'https://files.ffiec.cfpb.gov/static-data/snapshot/{year}/{year}_public_lar_csv.zip'
        _, head = fetch(f'hmda_{year}_head', url, method='HEAD', version=f'{year} static snapshot')
        tail, trec = fetch(f'hmda_{year}_tail.bin', url, byte_range='-65536', cap=65536, version=f'{year} snapshot ZIP directory')
        raw, prec = fetch(f'hmda_{year}_prefix.bin', url, byte_range='0-262143', cap=262144, version=f'{year} snapshot prefix')
        item = dict(head=head, tail=trec, prefix=prec)
        try:
            if tail:
                item['zip_entries'] = directory(tail)
            if raw:
                body = partial_csv(raw)
                (DATA / f'hmda_{year}_sample.csv').write_bytes(body)
                item['sample'] = inspect_csv(body)
        except Exception as exc:
            item['parse_error'] = str(exc)
        result[str(year)] = item
        save('hmda_snapshot_probe.json', result)
        print(year, head.get('status'), item.get('sample',{}).get('rows'), item.get('parse_error',''), flush=True)
    for year in [2018,2023,2024,2025]:
        url = f'https://ffiec.cfpb.gov/v2/data-browser-api/view/csv?years={year}&states=CT&actions_taken=1&loan_purposes=1'
        body, rec = fetch(f'hmda_ct_{year}.csv',url,cap=35_000_000,version=f'{year} Data Browser snapshot; CT purchase originations')
        item = dict(retrieval=rec)
        if body:
            try: item['sample'] = inspect_csv(body)
            except Exception as exc: item['parse_error'] = str(exc)
        result[f'ct_{year}'] = item
        save('hmda_snapshot_probe.json', result)
        print('ct',year,item.get('sample',{}).get('rows'),rec.get('error',''),flush=True)
