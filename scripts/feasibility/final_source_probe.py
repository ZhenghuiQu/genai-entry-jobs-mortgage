from common import fetch,save
sources={
'onet_soc2018.xlsx':'https://www.onetcenter.org/taxonomy/2019/soc/2019_to_SOC_Crosswalk.xlsx?fmt=xlsx',
'soc2018_structure.pdf':'https://www.bls.gov/soc/2018/soc_structure_2018.pdf',
'soc2018_guidelines.pdf':'https://www.bls.gov/soc/2018/soc_2018_class_prin_cod_guide.pdf',
}
if __name__=='__main__':
 for n,u in sources.items():
  _,r=fetch(n,u);print(n,r.get('status'),r.get('error',''),flush=True)
 for n,u in [('hmda2018','https://files.ffiec.cfpb.gov/static-data/snapshot/2018/2018_public_lar_csv.zip'),('hmda2025','https://files.ffiec.cfpb.gov/static-data/snapshot/2025/2025_public_lar_csv.zip'),('pums_us','https://www2.census.gov/programs-surveys/acs/data/pums/2019/5-Year/csv_pus.zip')]:
  _,r=fetch(n+'_resource_head',u,method='HEAD');print(n,r.get('status'),r.get('headers',{}).get('content-length'),flush=True)
