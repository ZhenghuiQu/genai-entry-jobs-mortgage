"""Only small sources and one small-state PUMS/QWI file, never national HMDA."""
from common import fetch, save

sources = {
 'dorn_county.zip': 'https://www.ddorn.net/data/cw_cty_czone.zip',
 'dorn_puma.zip': 'https://www.ddorn.net/data/cw_puma2010_czone.zip',
 'dorn_state.zip': 'https://www.ddorn.net/data/cw_czone_state.zip',
 'county_changes.pdf': 'https://www.ddorn.net/data/FIPS_County_Code_Changes.pdf',
 'dorn_page.html': 'https://www.ddorn.net/data.htm',
 'exposure_commit.json': 'https://api.github.com/repos/openai/GPTs-are-GPTs/commits/main',
 'onet_walk.html': 'https://www.onetcenter.org/taxonomy/2019/walk.html',
 'onet_list.html': 'https://www.onetcenter.org/taxonomy/2019/list.html',
 'onet_2010.html': 'https://www.onetcenter.org/taxonomy/2010/list.html',
 'census_occupation_page.html': 'https://www.census.gov/topics/employment/industry-occupation/guidance/code-lists.html',
 'pums_dictionary.txt': 'https://www2.census.gov/programs-surveys/acs/tech_docs/pums/data_dict/PUMS_Data_Dictionary_2015-2019.txt',
 'pums_de.zip': 'https://www2.census.gov/programs-surveys/acs/data/pums/2019/5-Year/csv_pde.zip',
 'hmda_fields.html': 'https://ffiec.cfpb.gov/documentation/publications/loan-level-datasets/lar-data-fields',
 'hmda_static_faq.html': 'https://ffiec.cfpb.gov/documentation/faq/static-datasets',
 'qwi_de.csv.gz': 'https://lehd.ces.census.gov/data/qwi/latest_release/de/qwi_de_sa_f_gc_ns_op_u.csv.gz',
 'qwi_age.csv': 'https://lehd.ces.census.gov/data/schema/latest/label_agegrp.csv',
 'qwi_flags.csv': 'https://lehd.ces.census.gov/data/schema/latest/label_flags.csv',
 'acs_counties.json': 'https://api.census.gov/data/2019/acs/acs5?get=NAME,B25077_001E,B19013_001E,B25003_002E,B01003_001E&for=county:*',
 'acs_variables.json': 'https://api.census.gov/data/2019/acs/acs5/variables.json',
 'fhfa_county.csv': 'https://www.fhfa.gov/hpi/download/annual/hpi_at_county.csv',
 'telework.csv': 'https://raw.githubusercontent.com/jdingel/DingelNeiman-workathome/master/occ_onet_scores/output/occupations_workathome.csv',
}
if __name__ == '__main__':
    import json
    results = {}
    for name, url in sources.items():
        _, rec = fetch(name, url)
        results[name] = rec
        print(name, rec.get('status'), rec.get('bytes'), rec.get('error', ''), flush=True)
    if results['exposure_commit.json'].get('status') == 200:
        from common import DATA
        sha = json.loads((DATA / 'exposure_commit.json').read_text())['sha']
        for name, path in [('exposure.csv', 'data/occ_level.csv'), ('exposure_readme.md', 'README.md')]:
            _, results[name] = fetch(name, f'https://raw.githubusercontent.com/openai/GPTs-are-GPTs/{sha}/{path}', version=sha)
            print(name, results[name].get('status'), flush=True)
    save('small_source_acquisition.json', results)
