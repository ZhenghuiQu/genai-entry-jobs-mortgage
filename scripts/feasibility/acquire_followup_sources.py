"""Official concordances discovered from downloaded source pages."""
from common import fetch,save
sources={
'census_2018_soc.xlsx':'https://www2.census.gov/programs-surveys/demo/guidance/industry-occupation/2018-occupation-code-list-and-crosswalk.xlsx',
'census_2018_pums.xlsx':'https://www2.census.gov/programs-surveys/demo/guidance/industry-occupation/2018-ACS-PUMS-and-2018-SIPP-Public-Use-Occupation-Code-List.xlsx',
'onet_walk.csv':'https://www.onetcenter.org/taxonomy/2019/walk/2010_to_2019_Crosswalk.csv?fmt=csv',
'onet_2019.csv':'https://www.onetcenter.org/taxonomy/2019/list/2019_Occupations.csv?fmt=csv',
'onet_2010.csv':'https://www.onetcenter.org/taxonomy/2010/list/2010_Occupations.csv?fmt=csv',
'pop2019.csv':'https://www2.census.gov/programs-surveys/popest/datasets/2010-2019/counties/totals/co-est2019-alldata.csv',
'pop2019_layout.pdf':'https://www2.census.gov/programs-surveys/popest/datasets/2010-2019/counties/totals/co-est2019-alldata.pdf',
'acs_affordability_de.zip':'https://www2.census.gov/programs-surveys/acs/summary_file/2019/data/5_year_seq_by_state/Delaware/All_Geographies_Not_Tracts_Block_Groups/20195de0115.zip',
'pums_readme.pdf':'https://www2.census.gov/programs-surveys/acs/tech_docs/pums/ACS2015_2019_PUMS_README.pdf',
'pums_code_lists.xlsx':'https://www2.census.gov/programs-surveys/acs/tech_docs/pums/code_lists/ACS2015_2019_PUMS_Code_Lists.xlsx',
'soc2018_structure.xlsx':'https://www.bls.gov/soc/2018/soc_2018_structure.xlsx',
'ct_changes.html':'https://www.census.gov/programs-surveys/geography/technical-documentation/county-changes/2020.html',
}
if __name__=='__main__':
 r={}
 for n,u in sources.items():
  _,r[n]=fetch(n,u)
  print(n,r[n].get('status'),r[n].get('bytes'),r[n].get('error',''),flush=True)
 save('followup_source_acquisition.json',r)
