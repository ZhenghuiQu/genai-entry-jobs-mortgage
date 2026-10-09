"""Small fixtures test >4 GiB ZIP64 directory sizes and a truncated CSV tail."""
import io,struct,unittest,zipfile
from hmda_probe import directory,partial_csv

class ZipHelpers(unittest.TestCase):
 def test_zip64_sizes_without_allocating_gigabytes(self):
  name=b'example.csv';usize=5_000_000_001;csize=900_000_001
  extra=struct.pack('<HHQQ',1,16,usize,csize)
  head=struct.pack('<4s6H3I5H2I',b'PK\x01\x02',45,45,0,8,0,0,123,0xffffffff,0xffffffff,len(name),len(extra),0,0,0,0,0)
  item=directory(head+name+extra)[0]
  self.assertEqual(item['uncompressed_bytes'],usize)
  self.assertEqual(item['compressed_bytes'],csize)
 def test_partial_last_record_is_discarded(self):
  buffer=io.BytesIO()
  with zipfile.ZipFile(buffer,'w',compression=zipfile.ZIP_DEFLATED) as z:z.writestr('s.csv',b'a,b\n1,2\nunfinished')
  data=buffer.getvalue();offset=data.find(b'PK\x01\x02')
  self.assertEqual(partial_csv(data[:offset]),b'a,b\n1,2\n')
 def test_real_standard_directory(self):
  buffer=io.BytesIO()
  with zipfile.ZipFile(buffer,'w',compression=zipfile.ZIP_DEFLATED) as z:z.writestr('s.csv',b'a,b\n1,2\n')
  entries=directory(buffer.getvalue())
  self.assertEqual(len(entries),1);self.assertEqual(entries[0]['uncompressed_bytes'],8)
if __name__=='__main__':unittest.main()
