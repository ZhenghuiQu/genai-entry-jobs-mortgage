# Data Source Registry

<!-- PHASE2 BEGIN -->
## Current Phase 2 update — 2026-10-09 (Asia/Shanghai)

Phase 2 adds the complete BLS SOC hierarchy and complete official CT town/block-group and town/tract relationship web extracts. Original downloaded sources and hashes remain preserved. New byte-download attempts and national ACS access fail 403. Resources are remeasured at 16 GiB RAM and roughly 75 GiB free; see [provenance integration](research_provenance_integration.md) and `phase2_resource_audit.json`.

The Day 1–2 evidence below is preserved historically; current Phase 2 findings supersede its occupation/CT/provenance conclusions where explicitly stated. No outcome estimation was authorized.

<!-- PHASE2 END -->
Date: 2026-10-09 (Asia/Shanghai). Scope: Day 1–2 feasibility only. Retrieval timestamps are UTC in the source manifest.

**Evidence labels.** VERIFIED DATA FACT = directly downloaded/parsed or official metadata; TECHNICAL ASSUMPTION = diagnostic implementation rule; UNRESOLVED CHOICE = design/mapping policy not fixed; RECOMMENDATION = action supported by those facts. PASS is limited to the stated procedure and denominator; FAIL rejects the tested configuration; OPEN has an unresolved dependency.

## Retrieval manifest and version policy

The authoritative append-only machine manifest is `results/feasibility/source_manifest.jsonl`. Every attempted acquisition records URL/final redirect, UTC timestamp, method, requested range, HTTP backend/status, version label, response headers, bytes, SHA256 when a body was actually retrieved, and error if any. HEAD requests hash no body; national range hashes cover only those bytes. Successful small complete archives have full downloaded-object hashes. Downloaded microdata, workbooks, source pages, credentials and virtual environments are excluded from Git. Derived aggregate audit results are committed.

The Eloundou source is pinned by Git SHA; the ACS baseline is the official 2015–2019 five-year release; population weights are Vintage 2019, July 1; QWI manifest labels identify V4.14.0/R2026Q3 and per-state build identifiers. Mutable `latest_release` files are identified by the retrieval/hash, not assumed timeless. Raw FHFA URL redirects/content signature are audited separately. For unpinned author-source controls, their content hash is the retrieved version; pinning an upstream commit remains required before implementation.

## Test-linked source decisions

### A01 — Official 2018–2025 snapshot access

- **Status:** PASS.
- **Source and URL:** [FFIEC/CFPB snapshot files](https://files.ffiec.cfpb.gov/static-data/snapshot/2025/2025_public_lar_csv.zip) and [field documentation](https://ffiec.cfpb.gov/documentation/publications/loan-level-datasets/lar-data-fields).
- **Procedure:** hmda_probe.py: HEAD, final 65,536 archive bytes, first 262,144 bytes; require HTTP 206 for ranges and reject full-object responses.
- **Observed evidence:** All eight HEADs returned 200 with Chrome-compatible TLS; ZIP directories and bounded CSV records were parsed for every year.
- **Limitations:** Standard urllib/curl returned 403. No full ZIP CRC or complete-file SHA256 was computed.
- **Implication for CZ versus State:** The same mortgage source supports either geography.
- **Next required action:** Use the demonstrated client, retain snapshot/ETag metadata, and verify full-file hashes only at authorized acquisition.

### B01 — Original exposure classification and dv_rating_beta

- **Status:** PASS.
- **Source and URL:** [Eloundou source repository](https://github.com/openai/GPTs-are-GPTs) and [official O*NET-to-SOC crosswalk](https://www.onetcenter.org/taxonomy/2019/soc/2019_to_SOC_Crosswalk.xlsx?fmt=xlsx).
- **Procedure:** Pin the source Git commit; join complete occupation identifiers to official O*NET 2019 occupations and the SOC 2018 crosswalk.
- **Observed evidence:** 923 unique ratings; all 923 match O*NET-SOC 2019 and the official SOC crosswalk. 798 scored detailed SOC groups; no missing beta; beta is bounded by 0 and 1. Only 762 codes also occur in the older 2010 list.
- **Limitations:** Code membership and exact official mappings establish usable taxonomy; ratings measure task capability, not adoption.
- **Implication for CZ versus State:** Occupation classification is a common dependency for both CZ and State.
- **Next required action:** Retain the pinned raw-source hash and exact concordance, not occupational prefix truncation.

### C01 — County-to-1990-CZ key integrity

- **Status:** PASS.
- **Source and URL:** [Dorn geography files](https://www.ddorn.net/data.htm).
- **Procedure:** Read the official Stata archive, ignore macOS resource-fork entries, preserve FIPS as zero-padded strings and test duplicates/missing.
- **Observed evidence:** 3,141 county rows, 741 CZs, zero duplicate county keys and zero missing cells.
- **Limitations:** The crosswalk uses 1990 county definitions, not all modern equivalents.
- **Implication for CZ versus State:** CZ has a valid base join; State needs only stable state codes.
- **Next required action:** Apply audited vintage handling before joining mortgage records.

### D01 — QWI age coverage and Michigan limitation

- **Status:** PASS.
- **Source and URL:** [LEHD QWI releases](https://lehd.ces.census.gov/data/qwi/latest_release/).
- **Procedure:** Fetch version_qwi.txt for all 50 states+DC, parse the unadjusted QWI_F interval, and retain all release strings.
- **Observed evidence:** All 51 retrieved manifests identify R2026Q3/V4.14.0. 49 end at 2025Q4; Michigan ends 2021Q4 and Alaska 2016Q2. A03=22–24, A04=25–34, A05=35–44, A06=45–54.
- **Limitations:** Publication endpoint is not proof of nonmissing county cells; adjusted/seasonal variants end one quarter earlier and are not the tested unadjusted series.
- **Implication for CZ versus State:** MI’s post-period mechanism data are unavailable at either geography; cross-border CZ membership needs handling.
- **Next required action:** Pre-specify a harmonized mechanism sample; do not treat unreleased MI values as zero or carry them forward.

### D03 — ACS baseline affordability and no-key alternative

- **Status:** PASS.
- **Source and URL:** [ACS sequence documentation](https://www.census.gov/programs-surveys/acs/data/summary-file/sequence-based/2019.html) and [2019 variable metadata](https://api.census.gov/data/2019/acs/acs5/variables.json).
- **Procedure:** Reject HTML from the no-key API; read official sequence lookup and four DE bulk files, join LOGRECNO to summary-level 050/component 00.
- **Observed evidence:** All three counties have positive B25077 home-value and B19013 household-income medians, B25003 owner units and B01003 population. Ratios are 3.622, 3.529 and 4.094. Metadata/sequence positions agree.
- **Limitations:** The API body says Missing Key despite HTTP 200. National county missingness and aggregating county medians into a CZ affordability index remain unresolved.
- **Implication for CZ versus State:** Bulk collection can support CZ or State without pretending no-key API access works.
- **Next required action:** Use the demonstrated bulk path or a user-supplied environment key; settle aggregation weights and ratio/log order before implementation.

### D04 — 2019 population weights and region/division coding

- **Status:** PASS.
- **Source and URL:** [Census 2019 population file](https://www2.census.gov/programs-surveys/popest/datasets/2010-2019/counties/totals/co-est2019-alldata.csv) and [layout](https://www2.census.gov/programs-surveys/popest/datasets/2010-2019/counties/totals/co-est2019-alldata.pdf).
- **Procedure:** Keep SUMLEV 050 and validate STATE+COUNTY and POPESTIMATE2019; inspect REGION/DIVISION codes.
- **Observed evidence:** 3,142 counties, no duplicate county keys or blank population weight; July 1, 2019 weights and four regions/nine divisions are explicitly coded.
- **Limitations:** These weights differ from pooled ACS 2015–2019 population; changing the intended weight is a methodological choice, not an automatic substitution.
- **Implication for CZ versus State:** Either geography can receive documented 2019 weights once vintage/sample policy is fixed.
- **Next required action:** Freeze population-weight vintage and relevant aggregation universe; retain C03 change accounting.

### D05 — Required regional characteristics and price-control inputs

- **Status:** OPEN.
- **Source and URL:** [PUMS dictionary](https://www2.census.gov/programs-surveys/acs/tech_docs/pums/data_dict/PUMS_Data_Dictionary_2015-2019.txt), [telework source](https://github.com/jdingel/DingelNeiman-workathome), [FHFA file route](https://www.fhfa.gov/hpi/download/annual/hpi_at_county.csv).
- **Procedure:** Inspect SCHL/NAICSP/SOCP/PWGTP in young DE records; detect FHFA format by signature rather than extension; inspect telework identifiers.
- **Observed evidence:** SCHL and NAICSP have no blanks among 4,898 young employed DE persons. Telework has 968 occupational rows. FHFA request returns an XLSX workbook with 106,252 rows, not CSV; it includes missing HPI and multiple index bases.
- **Limitations:** Exact tech-industry membership, telework taxonomy mapping, national FHA baseline shares and national control missingness are not certified.
- **Implication for CZ versus State:** State avoids geographical allocation but shares occupation/industry coding concerns.
- **Next required action:** Create explicit Census industry and 2010→2019 telework concordances; choose FHFA series/base and quantify control availability before using them.

### E01 — Observed download and disk budget

- **Status:** PASS.
- **Source and URL:** [FFIEC/CFPB snapshot files](https://files.ffiec.cfpb.gov/static-data/snapshot/2025/2025_public_lar_csv.zip) and [field documentation](https://ffiec.cfpb.gov/documentation/publications/loan-level-datasets/lar-data-fields).
- **Procedure:** Read all eight ZIP central directories, including ZIP64 sizes, and measure current disk/RAM.
- **Observed evidence:** HMDA ZIP total is 7,685,735,098 bytes; expanded CSV total 53,046,718,437 bytes; largest CSV 10,206,391,218 bytes. Machine has 8 logical CPUs, 16 GiB physical RAM and about 65.4 GB free during the test.
- **Limitations:** Complete PUMS/QWI/conversion/spill space is not included in the mortgage sum; available disk changes over time.
- **Implication for CZ versus State:** Streaming/year-at-a-time aggregation is applicable to both geographies; State has fewer grouping cells.
- **Next required action:** Reserve headroom and process one year at a time; do not retain all expanded CSVs beside ZIPs/Parquet on this disk.

## Individual source objects and attempts

| ID | Version | UTC retrieval | HTTP / bytes | SHA256 or scope | Source URL |
| --- | --- | --- | --- | --- | --- |
| dorn_county.zip | retrieved vintage | 2026-10-09T01:18:54.170321+00:00 | 200 / 13000 | 0843c69c6598ec01311d131e08996a9805e17e2cc7cedbd2d72d617193ed6b9a | [source](https://www.ddorn.net/data/cw_cty_czone.zip) |
| dorn_puma.zip | retrieved vintage | 2026-10-09T01:18:55.618465+00:00 | 200 / 27418 | 295429e9221b5428eac3377d39fc3abd0c574917d07626aafd66a556061f23a7 | [source](https://www.ddorn.net/data/cw_puma2010_czone.zip) |
| dorn_state.zip | retrieved vintage | 2026-10-09T01:18:56.622803+00:00 | 200 / 4114 | 9a1d9f8bcbde2565afd78f0ccc40c1d226c9f5f29bb0c0b331abb71e5ef27304 | [source](https://www.ddorn.net/data/cw_czone_state.zip) |
| county_changes.pdf | retrieved vintage | 2026-10-09T01:18:57.389437+00:00 | 200 / 63680 | 80289731be1777d1999bc203e1ff80c0ecffb244f9e5709454ce39d2873c5703 | [source](https://www.ddorn.net/data/FIPS_County_Code_Changes.pdf) |
| dorn_page.html | retrieved vintage | 2026-10-09T01:18:58.470093+00:00 | 200 / 26516 | 963c6200c0326918689722503ae49ee3aed592e792f9a59a2096338bd7dec68e | [source](https://www.ddorn.net/data.htm) |
| exposure_commit.json | retrieved vintage | 2026-10-09T01:18:59.373051+00:00 | 200 / 5170 | 4cfbad329a0c5c9781d3a227d7e2d7bab3228c6e265df0232d15bd1547653f39 | [source](https://api.github.com/repos/openai/GPTs-are-GPTs/commits/main) |
| onet_walk.html | retrieved vintage | 2026-10-09T01:18:59.999720+00:00 | 200 / 456628 | dbc75e3d9aece607264edc782a3cbb784c62f76e09daf96af1e79ba5d64dfd64 | [source](https://www.onetcenter.org/taxonomy/2019/walk.html) |
| onet_list.html | retrieved vintage | 2026-10-09T01:19:05.825787+00:00 | 200 / 477170 | db389042c2da2c40e19b786cf5654ab1598834af36211676b1e78f06e0e5f429 | [source](https://www.onetcenter.org/taxonomy/2019/list.html) |
| onet_2010.html | retrieved vintage | 2026-10-09T01:19:08.973682+00:00 | 200 / 504822 | 41f903eb35e1fbc9cb3cc724da9cb75d0d10c9549fbf31a3b5a3043a170170a5 | [source](https://www.onetcenter.org/taxonomy/2010/list.html) |
| census_occupation_page.html | retrieved vintage | 2026-10-09T01:19:11.735313+00:00 | 200 / 376623 | e350dcdb356cf2ec0c6f3291228d69e6fe2e245d6f60b4ffc371fee9282f6636 | [source](https://www.census.gov/topics/employment/industry-occupation/guidance/code-lists.html) |
| pums_dictionary.txt | retrieved vintage | 2026-10-09T01:19:13.158644+00:00 | 200 / 299302 | 0065dc022bd473cbcabb70192ac00c6b3bc53c83a32686df91360ce6d07c75fd | [source](https://www2.census.gov/programs-surveys/acs/tech_docs/pums/data_dict/PUMS_Data_Dictionary_2015-2019.txt) |
| pums_de.zip | retrieved vintage | 2026-10-09T01:19:14.484613+00:00 | 200 / 6595972 | 4115c1f8b1c8cce404caabf545c35e370a6268844012340b5dd59f3ad9346afc | [source](https://www2.census.gov/programs-surveys/acs/data/pums/2019/5-Year/csv_pde.zip) |
| hmda_fields.html | retrieved vintage | 2026-10-09T01:19:16.171905+00:00 | 403 / — | HTTP Error 403: Forbidden | [source](https://ffiec.cfpb.gov/documentation/publications/loan-level-datasets/lar-data-fields) |
| hmda_static_faq.html | retrieved vintage | 2026-10-09T01:19:16.546044+00:00 | 403 / — | HTTP Error 403: Forbidden | [source](https://ffiec.cfpb.gov/documentation/faq/static-datasets) |
| hmda_2018_head | 2018 static snapshot | 2026-10-09T01:24:07.509081+00:00 | 200 / 0 | HEAD metadata only | [source](https://files.ffiec.cfpb.gov/static-data/snapshot/2018/2018_public_lar_csv.zip) |
| hmda_2018_tail.bin | 2018 snapshot ZIP directory | 2026-10-09T01:24:13.099336+00:00 | 206 / 65536 | 5977f1fa6ba46160b2a2ba441a7130d9847b6ef9618146c1081251cfd6d83197 | [source](https://files.ffiec.cfpb.gov/static-data/snapshot/2018/2018_public_lar_csv.zip) |
| hmda_2018_prefix.bin | 2018 snapshot prefix | 2026-10-09T01:24:15.308166+00:00 | 206 / 262144 | a1efd2ede30acbe0f3d9ae4abccf2b70fc30b194a75353db49e2a4aad6769835 | [source](https://files.ffiec.cfpb.gov/static-data/snapshot/2018/2018_public_lar_csv.zip) |
| hmda_2019_head | 2019 static snapshot | 2026-10-09T01:24:18.486455+00:00 | 200 / 0 | HEAD metadata only | [source](https://files.ffiec.cfpb.gov/static-data/snapshot/2019/2019_public_lar_csv.zip) |
| hmda_2019_tail.bin | 2019 snapshot ZIP directory | 2026-10-09T01:24:20.257226+00:00 | 206 / 65536 | 10c703667f06d1bacd925c940488265d3c4bb5220c764ea3bacd907a47944162 | [source](https://files.ffiec.cfpb.gov/static-data/snapshot/2019/2019_public_lar_csv.zip) |
| hmda_2019_prefix.bin | 2019 snapshot prefix | 2026-10-09T01:24:22.503387+00:00 | 206 / 262144 | ae7c98f466130e5e8e972c9352cb3921312e308e152a19ae58f1d50f310d7bf4 | [source](https://files.ffiec.cfpb.gov/static-data/snapshot/2019/2019_public_lar_csv.zip) |
| hmda_2020_head | 2020 static snapshot | 2026-10-09T01:24:25.314031+00:00 | 200 / 0 | HEAD metadata only | [source](https://files.ffiec.cfpb.gov/static-data/snapshot/2020/2020_public_lar_csv.zip) |
| hmda_2020_tail.bin | 2020 snapshot ZIP directory | 2026-10-09T01:24:26.956178+00:00 | 206 / 65536 | 1cbbd4c17f040f111179221d1043edaeb92786a7c7895459d4f3222db90252d2 | [source](https://files.ffiec.cfpb.gov/static-data/snapshot/2020/2020_public_lar_csv.zip) |
| hmda_2020_prefix.bin | 2020 snapshot prefix | 2026-10-09T01:24:29.389498+00:00 | 206 / 262144 | 7fcc8adfcbd66e4ac4e168967881a08a237b176e1fbe2e23fb0eac1aea675f71 | [source](https://files.ffiec.cfpb.gov/static-data/snapshot/2020/2020_public_lar_csv.zip) |
| hmda_2021_head | 2021 static snapshot | 2026-10-09T01:24:32.348719+00:00 | 200 / 0 | HEAD metadata only | [source](https://files.ffiec.cfpb.gov/static-data/snapshot/2021/2021_public_lar_csv.zip) |
| hmda_2021_tail.bin | 2021 snapshot ZIP directory | 2026-10-09T01:24:33.841817+00:00 | 206 / 65536 | a9ba9809ab7b8dbdd19477415fd121895fc665067cafac038d9173dec9a012e4 | [source](https://files.ffiec.cfpb.gov/static-data/snapshot/2021/2021_public_lar_csv.zip) |
| hmda_2021_prefix.bin | 2021 snapshot prefix | 2026-10-09T01:24:36.274374+00:00 | 206 / 262144 | 03cc673102d08cd716b6f2f8b0bb2b3ec098115e389601c693507c332ce4665f | [source](https://files.ffiec.cfpb.gov/static-data/snapshot/2021/2021_public_lar_csv.zip) |
| hmda_2022_head | 2022 static snapshot | 2026-10-09T01:24:39.185565+00:00 | 200 / 0 | HEAD metadata only | [source](https://files.ffiec.cfpb.gov/static-data/snapshot/2022/2022_public_lar_csv.zip) |
| qwi_de.csv.gz | retrieved vintage | 2026-10-09T01:19:16.889828+00:00 | 200 / 13069404 | 54dea48dffe17b0daa2179627ffb5e069663b9b718f6fb71c93fe079f6a09fa8 | [source](https://lehd.ces.census.gov/data/qwi/latest_release/de/qwi_de_sa_f_gc_ns_op_u.csv.gz) |
| hmda_2022_tail.bin | 2022 snapshot ZIP directory | 2026-10-09T01:24:40.837031+00:00 | 206 / 65536 | 7d69466d7ad4221025a8c2e63a399401042fccb4b6a9c48235303e1803320597 | [source](https://files.ffiec.cfpb.gov/static-data/snapshot/2022/2022_public_lar_csv.zip) |
| hmda_2022_prefix.bin | 2022 snapshot prefix | 2026-10-09T01:24:42.989329+00:00 | 206 / 262144 | eda10ca397fb473a6670ba14194df2b09b5bf0e24742a60e180e5ec3f535618f | [source](https://files.ffiec.cfpb.gov/static-data/snapshot/2022/2022_public_lar_csv.zip) |
| hmda_2023_head | 2023 static snapshot | 2026-10-09T01:24:45.746698+00:00 | 200 / 0 | HEAD metadata only | [source](https://files.ffiec.cfpb.gov/static-data/snapshot/2023/2023_public_lar_csv.zip) |
| hmda_2023_tail.bin | 2023 snapshot ZIP directory | 2026-10-09T01:24:47.446695+00:00 | 206 / 65536 | c0d780fc4e3df93912ae1cfec7675d53977bbe826c9dcb47ec5fd69b099d165b | [source](https://files.ffiec.cfpb.gov/static-data/snapshot/2023/2023_public_lar_csv.zip) |
| qwi_age.csv | retrieved vintage | 2026-10-09T01:20:05.365726+00:00 | 200 / 132 | eb478c6eda6c12a57609afaf89bbb42dd4d9fb2ee883f6dd0399fb717b27889b | [source](https://lehd.ces.census.gov/data/schema/latest/label_agegrp.csv) |
| hmda_2023_prefix.bin | 2023 snapshot prefix | 2026-10-09T01:24:49.856995+00:00 | 206 / 262144 | cc2a6a8fe3e4f349b4b737844652b025d772b63d37b3f0e39939f7b916f993ca | [source](https://files.ffiec.cfpb.gov/static-data/snapshot/2023/2023_public_lar_csv.zip) |
| hmda_2024_head | 2024 static snapshot | 2026-10-09T01:24:52.549101+00:00 | 200 / 0 | HEAD metadata only | [source](https://files.ffiec.cfpb.gov/static-data/snapshot/2024/2024_public_lar_csv.zip) |
| hmda_2024_tail.bin | 2024 snapshot ZIP directory | 2026-10-09T01:24:54.264381+00:00 | 206 / 65536 | b0fcf46d63d3ac12024bccfff09e10e76add482b88bc50fe4bafdfcb584972f6 | [source](https://files.ffiec.cfpb.gov/static-data/snapshot/2024/2024_public_lar_csv.zip) |
| qwi_flags.csv | retrieved vintage | 2026-10-09T01:20:06.770634+00:00 | 200 / 673 | 2b64bfed86efaa1c0ebd50d3dc94885a769dbcd11790ca9647d0a45e68959edc | [source](https://lehd.ces.census.gov/data/schema/latest/label_flags.csv) |
| hmda_2024_prefix.bin | 2024 snapshot prefix | 2026-10-09T01:24:58.759105+00:00 | 206 / 262144 | 75ce730147157e8dda6775b12113dd2b3c1d7007b33a353c06c7c592fbc5e005 | [source](https://files.ffiec.cfpb.gov/static-data/snapshot/2024/2024_public_lar_csv.zip) |
| hmda_2025_head | 2025 static snapshot | 2026-10-09T01:25:01.535407+00:00 | 200 / 0 | HEAD metadata only | [source](https://files.ffiec.cfpb.gov/static-data/snapshot/2025/2025_public_lar_csv.zip) |
| hmda_2025_tail.bin | 2025 snapshot ZIP directory | 2026-10-09T01:25:02.933420+00:00 | 206 / 65536 | 4d97f1996589dd52b429397c67e115ab2c7e6ab0e680862f951f918d719a9ea7 | [source](https://files.ffiec.cfpb.gov/static-data/snapshot/2025/2025_public_lar_csv.zip) |
| hmda_2025_prefix.bin | 2025 snapshot prefix | 2026-10-09T01:25:04.971293+00:00 | 206 / 262144 | 58e45ee40f33d8b133abf64d5689344e0ddebc2ad2521c2a613814a092a5ae77 | [source](https://files.ffiec.cfpb.gov/static-data/snapshot/2025/2025_public_lar_csv.zip) |
| hmda_ct_2018.csv | 2018 Data Browser snapshot; CT purchase originations | 2026-10-09T01:25:07.401791+00:00 | 200 / 16258764 | f7a696bde3e0f007cf647e87b6427885e37f6bcd468d1d44a0bb0de5e96fc9c6 | [source](https://ffiec.cfpb.gov/v2/data-browser-api/view/csv?years=2018&states=CT&actions_taken=1&loan_purposes=1) |
| hmda_ct_2023.csv | 2023 Data Browser snapshot; CT purchase originations | 2026-10-09T01:25:14.869052+00:00 | 200 / 13785944 | 436064a804aa11b725474560dfe2da9398fdab76bf6d1c374b401071e511fc52 | [source](https://ffiec.cfpb.gov/v2/data-browser-api/view/csv?years=2023&states=CT&actions_taken=1&loan_purposes=1) |
| hmda_ct_2024.csv | 2024 Data Browser snapshot; CT purchase originations | 2026-10-09T01:25:21.586771+00:00 | 200 / 13559246 | 627e59bba36fa0f902b147a189df82857bcb7c39c5d59ff40b5eb9aed161c6fb | [source](https://ffiec.cfpb.gov/v2/data-browser-api/view/csv?years=2024&states=CT&actions_taken=1&loan_purposes=1) |
| acs_counties.json | retrieved vintage | 2026-10-09T01:20:08.141076+00:00 | 200 / 8531 | c2f4687e09b80676de7f68dec92ebea395209616dbc6f895520e547c5f68c0f5 | [source](https://api.census.gov/data/2019/acs/acs5?get=NAME,B25077_001E,B19013_001E,B25003_002E,B01003_001E&for=county:*) |
| hmda_ct_2025.csv | 2025 Data Browser snapshot; CT purchase originations | 2026-10-09T01:25:28.383064+00:00 | 200 / 13690851 | 057d7fc835c7641fe3c9ec2f1c978a012af38341df1369370f4de681096d67b7 | [source](https://ffiec.cfpb.gov/v2/data-browser-api/view/csv?years=2025&states=CT&actions_taken=1&loan_purposes=1) |
| acs_variables.json | retrieved vintage | 2026-10-09T01:20:11.071197+00:00 | 200 / 10036017 | 824bb0c3f1b9ab2d4e7323a5fb184b8a4d15de1b7068e08bef01c6599c8bc574 | [source](https://api.census.gov/data/2019/acs/acs5/variables.json) |
| fhfa_county.csv | retrieved vintage | 2026-10-09T01:20:49.979494+00:00 | 200 / 5334194 | 534e9fd3224c4d9365300cc1be471bcfe4455b72311263a35e9cb50adf79afd1 | [source](https://www.fhfa.gov/hpi/download/annual/hpi_at_county.csv) |
| telework.csv | retrieved vintage | 2026-10-09T01:20:53.393683+00:00 | 200 / 45011 | 42ff3ae084478b554526671710b53a16d39f88c3eebb24f56f46372d7243bd40 | [source](https://raw.githubusercontent.com/jdingel/DingelNeiman-workathome/master/occ_onet_scores/output/occupations_workathome.csv) |
| exposure.csv | 0471612fef3cc22b74fb884d27bff9dbd3770582 | 2026-10-09T01:20:54.070656+00:00 | 200 / 126022 | 40c74f53de40aec91c0017d80690cbba915f83a8bb414bcf2f884692f1749acb | [source](https://raw.githubusercontent.com/openai/GPTs-are-GPTs/0471612fef3cc22b74fb884d27bff9dbd3770582/data/occ_level.csv) |
| exposure_readme.md | 0471612fef3cc22b74fb884d27bff9dbd3770582 | 2026-10-09T01:20:54.758925+00:00 | 200 / 172 | fb8ae66d02142a9b7178d8cbd59b90a6c5bd80bf088107cae126f4276c8d68c6 | [source](https://raw.githubusercontent.com/openai/GPTs-are-GPTs/0471612fef3cc22b74fb884d27bff9dbd3770582/README.md) |
| census_2018_soc.xlsx | retrieved vintage | 2026-10-09T01:21:22.671543+00:00 | 200 / 160312 | fca2818d691c32777a4cd733a9ab77c8c5bd47adcacd7ac3aa149bebd45b5f7f | [source](https://www2.census.gov/programs-surveys/demo/guidance/industry-occupation/2018-occupation-code-list-and-crosswalk.xlsx) |
| census_2018_pums.xlsx | retrieved vintage | 2026-10-09T01:21:23.826058+00:00 | 200 / 73419 | 20cc7112cf96c7a3648b579cc0b2af239bea1c9094885a0d986959888695fe0a | [source](https://www2.census.gov/programs-surveys/demo/guidance/industry-occupation/2018-ACS-PUMS-and-2018-SIPP-Public-Use-Occupation-Code-List.xlsx) |
| onet_walk.csv | retrieved vintage | 2026-10-09T01:21:24.861927+00:00 | 200 / 108052 | 8f026a33134bfde5770308d1c6117cf70d9dd41c2b3467e6dd271d65bdeecc5a | [source](https://www.onetcenter.org/taxonomy/2019/walk/2010_to_2019_Crosswalk.csv?fmt=csv) |
| onet_2019.csv | retrieved vintage | 2026-10-09T01:21:26.802082+00:00 | 200 / 267048 | 8b02868be11d5b55c60b0ab42ac14eb1c0b241dbdff523627c6f10a8ebe184ba | [source](https://www.onetcenter.org/taxonomy/2019/list/2019_Occupations.csv?fmt=csv) |
| onet_2010.csv | retrieved vintage | 2026-10-09T01:21:28.738199+00:00 | 200 / 278382 | e484a6c7d5eb781019d8a16e5f8070eed300bb2874f6a127e3f37d6d2dcea71a | [source](https://www.onetcenter.org/taxonomy/2010/list/2010_Occupations.csv?fmt=csv) |
| pop2019.csv | retrieved vintage | 2026-10-09T01:21:30.767345+00:00 | 200 / 3644730 | 654032fbb805bc9a7c124ba04ad47e170f5d9dc9d4974a73edfc20598fde77d8 | [source](https://www2.census.gov/programs-surveys/popest/datasets/2010-2019/counties/totals/co-est2019-alldata.csv) |
| pop2019_layout.pdf | retrieved vintage | 2026-10-09T01:21:32.444265+00:00 | 200 / 213575 | 42670240dfd594dece0bd256f2deffbc8a7b20c2a2dd652493e73a880876ad9f | [source](https://www2.census.gov/programs-surveys/popest/datasets/2010-2019/counties/totals/co-est2019-alldata.pdf) |
| acs_affordability_de.zip | retrieved vintage | 2026-10-09T01:21:33.674521+00:00 | 404 / — | HTTP Error 404: Not Found | [source](https://www2.census.gov/programs-surveys/acs/summary_file/2019/data/5_year_seq_by_state/Delaware/All_Geographies_Not_Tracts_Block_Groups/20195de0115.zip) |
| pums_readme.pdf | retrieved vintage | 2026-10-09T01:21:34.989337+00:00 | 200 / 467585 | 42d7b44abe25d16f0f3a4dc5d89b25fbb2f6ca4829e51785bbb78a1cb2d7d667 | [source](https://www2.census.gov/programs-surveys/acs/tech_docs/pums/ACS2015_2019_PUMS_README.pdf) |
| pums_code_lists.xlsx | retrieved vintage | 2026-10-09T01:21:36.335540+00:00 | 404 / — | HTTP Error 404: Not Found | [source](https://www2.census.gov/programs-surveys/acs/tech_docs/pums/code_lists/ACS2015_2019_PUMS_Code_Lists.xlsx) |
| soc2018_structure.xlsx | retrieved vintage | 2026-10-09T01:21:37.760124+00:00 | 403 / — | HTTP Error 403: Forbidden | [source](https://www.bls.gov/soc/2018/soc_2018_structure.xlsx) |
| ct_changes.html | retrieved vintage | 2026-10-09T01:21:38.219688+00:00 | 200 / 328850 | 08a9a5a63337c6f0e90fa3901061281e0a3cacc9f711548979411b70aa78775b | [source](https://www.census.gov/programs-surveys/geography/technical-documentation/county-changes/2020.html) |
| qwi_version_ar.txt | retrieved vintage | 2026-10-09T01:22:51.965105+00:00 | 200 / 197 | f5d091c5d48d205483cb106e00152c9346559e07990d5bd8c555f8d3e5af12bc | [source](https://lehd.ces.census.gov/data/qwi/latest_release/ar/version_qwi.txt) |
| qwi_version_ak.txt | retrieved vintage | 2026-10-09T01:22:51.964821+00:00 | 200 / 197 | c3a8caaae50819e21eefaa722d557b61a07895a97a6e3610cc63125b57ed98d5 | [source](https://lehd.ces.census.gov/data/qwi/latest_release/ak/version_qwi.txt) |
| qwi_version_co.txt | retrieved vintage | 2026-10-09T01:22:51.965258+00:00 | 200 / 197 | 044184b2755778cc583109056b8ce7cda781dbf6618d23f7767b29034fbdc15a | [source](https://lehd.ces.census.gov/data/qwi/latest_release/co/version_qwi.txt) |
| qwi_version_ca.txt | retrieved vintage | 2026-10-09T01:22:51.965195+00:00 | 200 / 197 | 3ad6c292a946ed58b5f66b22abf96afc4b34f84144d94632ca2e755f9aae0b93 | [source](https://lehd.ces.census.gov/data/qwi/latest_release/ca/version_qwi.txt) |
| qwi_version_al.txt | retrieved vintage | 2026-10-09T01:22:51.964439+00:00 | 200 / 197 | 0bbf97f7a70414843530508fdaabb64cb7ca49d70771164dd23c64496a6bc30a | [source](https://lehd.ces.census.gov/data/qwi/latest_release/al/version_qwi.txt) |
| qwi_version_az.txt | retrieved vintage | 2026-10-09T01:22:51.964941+00:00 | 200 / 197 | ebe279e91e50d66c01bb16b991ae4b6714d8f2448054c96342f33a934cfafe1f | [source](https://lehd.ces.census.gov/data/qwi/latest_release/az/version_qwi.txt) |
| qwi_version_ct.txt | retrieved vintage | 2026-10-09T01:22:53.485824+00:00 | 200 / 197 | 48567ffc2163f23266bc6aaeb02ea3c6b31dcc07fff02563dd73d1dfdcd2d828 | [source](https://lehd.ces.census.gov/data/qwi/latest_release/ct/version_qwi.txt) |
| qwi_version_de.txt | retrieved vintage | 2026-10-09T01:22:53.496372+00:00 | 200 / 197 | 61535931afd776898a8dae94ab8a305e1b94ef0aad2ea10e48c081f0901169af | [source](https://lehd.ces.census.gov/data/qwi/latest_release/de/version_qwi.txt) |
| qwi_version_ga.txt | retrieved vintage | 2026-10-09T01:22:53.498131+00:00 | 200 / 197 | b2aa6418643853557a40b616cc092025876b9cd3166a7e7a7b6ac5fbb62f2e1c | [source](https://lehd.ces.census.gov/data/qwi/latest_release/ga/version_qwi.txt) |
| qwi_version_fl.txt | retrieved vintage | 2026-10-09T01:22:53.497243+00:00 | 200 / 197 | 70398868c3f98dd94bb8af758151d0d0e494321a34a8de9478f6564080c49d89 | [source](https://lehd.ces.census.gov/data/qwi/latest_release/fl/version_qwi.txt) |
| qwi_version_hi.txt | retrieved vintage | 2026-10-09T01:22:53.498892+00:00 | 200 / 197 | c7112ae9b576370f9850848540eefac41ced818373bd9ab4b0916fe103cb7dac | [source](https://lehd.ces.census.gov/data/qwi/latest_release/hi/version_qwi.txt) |
| qwi_version_dc.txt | retrieved vintage | 2026-10-09T01:22:53.496571+00:00 | 200 / 197 | 697b3d839060c559c4867b6020ab2fce224fe950d35a0cb1570c30722fdedb0e | [source](https://lehd.ces.census.gov/data/qwi/latest_release/dc/version_qwi.txt) |
| qwi_version_id.txt | retrieved vintage | 2026-10-09T01:22:55.021915+00:00 | 200 / 197 | ad2dbfd84dfd04fd95c039cd37d711484a9399f4029270cf7ba82d23f29ca1d3 | [source](https://lehd.ces.census.gov/data/qwi/latest_release/id/version_qwi.txt) |
| qwi_version_ky.txt | retrieved vintage | 2026-10-09T01:22:55.058196+00:00 | 200 / 197 | cabb9e6ca895dbded9fcf8e83ef71b1073ae370296781a6c7d6672aa0dbe78bf | [source](https://lehd.ces.census.gov/data/qwi/latest_release/ky/version_qwi.txt) |
| qwi_version_ia.txt | retrieved vintage | 2026-10-09T01:22:55.042403+00:00 | 200 / 197 | b0847af8cbbbf0b28aad474102202e2d628ddbdc7ed6a16762e3e5ff7d49e25c | [source](https://lehd.ces.census.gov/data/qwi/latest_release/ia/version_qwi.txt) |
| qwi_version_in.txt | retrieved vintage | 2026-10-09T01:22:55.041613+00:00 | 200 / 197 | 48f63badce6b03a8de36f971dafce4c3c94d5ce71f5ffd9c5a2c02e8251788b2 | [source](https://lehd.ces.census.gov/data/qwi/latest_release/in/version_qwi.txt) |
| qwi_version_ks.txt | retrieved vintage | 2026-10-09T01:22:55.057177+00:00 | 200 / 197 | c7dc76d34fde4ecc3acd688d082035ae65ce0176124ea2fe81ffe6cc6b3bcd52 | [source](https://lehd.ces.census.gov/data/qwi/latest_release/ks/version_qwi.txt) |
| qwi_version_il.txt | retrieved vintage | 2026-10-09T01:22:55.041388+00:00 | 200 / 197 | 51873fa1464a496bedb3c908cfa65969b99e216ba51bc8d42790d2c62327b8ed | [source](https://lehd.ces.census.gov/data/qwi/latest_release/il/version_qwi.txt) |
| qwi_version_me.txt | retrieved vintage | 2026-10-09T01:22:57.012025+00:00 | 200 / 197 | f50cc4520381f8c9163473ad1c2151c6b394c982382dbf825651f0f87ed51f38 | [source](https://lehd.ces.census.gov/data/qwi/latest_release/me/version_qwi.txt) |
| qwi_version_md.txt | retrieved vintage | 2026-10-09T01:22:57.016149+00:00 | 200 / 197 | a812c9f974207379d40752bf5e1d78edfb2ce69d9cfb21bdfe6626d9d20b1336 | [source](https://lehd.ces.census.gov/data/qwi/latest_release/md/version_qwi.txt) |
| qwi_version_ma.txt | retrieved vintage | 2026-10-09T01:22:57.020002+00:00 | 200 / 197 | 70f2f190774d06191eae69b0b32ccf5dd433cf4a2b490bc4ca7b1eb3a5793950 | [source](https://lehd.ces.census.gov/data/qwi/latest_release/ma/version_qwi.txt) |
| qwi_version_la.txt | retrieved vintage | 2026-10-09T01:22:57.011732+00:00 | 200 / 197 | 632e0bd83fa441759b0ea40c6053b91cabbef80750381f762388164e57b71e4b | [source](https://lehd.ces.census.gov/data/qwi/latest_release/la/version_qwi.txt) |
| qwi_version_mi.txt | retrieved vintage | 2026-10-09T01:22:57.045223+00:00 | 200 / 197 | 4101f4f05a2fd421cfd4a6bd55a5b7572c8536311a25f5d4d1a8f4c5926b6325 | [source](https://lehd.ces.census.gov/data/qwi/latest_release/mi/version_qwi.txt) |
| qwi_version_mn.txt | retrieved vintage | 2026-10-09T01:22:57.299250+00:00 | 200 / 197 | 2b01cfbcad64c6ca45dacb898dae6a73eb475a4dd6a033be382afb7f5c98fca7 | [source](https://lehd.ces.census.gov/data/qwi/latest_release/mn/version_qwi.txt) |
| qwi_version_ms.txt | retrieved vintage | 2026-10-09T01:22:58.477747+00:00 | 200 / 197 | 3946be60d4ea82c6cd73af2c67ed12888d9fa928751e77a0d3e2c6784b0b6702 | [source](https://lehd.ces.census.gov/data/qwi/latest_release/ms/version_qwi.txt) |
| qwi_version_mo.txt | retrieved vintage | 2026-10-09T01:22:58.493746+00:00 | 200 / 197 | 46031969db06a28618c459eccb6004f6df2548ab4154164c7da86f06a6fe8133 | [source](https://lehd.ces.census.gov/data/qwi/latest_release/mo/version_qwi.txt) |
| qwi_version_mt.txt | retrieved vintage | 2026-10-09T01:22:58.494461+00:00 | 200 / 197 | 245f4ae86f258b1b0a18b2a9c0da0bca7a2be4088ca19a4c1f4c320625e79aa6 | [source](https://lehd.ces.census.gov/data/qwi/latest_release/mt/version_qwi.txt) |
| qwi_version_ne.txt | retrieved vintage | 2026-10-09T01:22:58.498475+00:00 | 200 / 197 | d29cf5d597d30a7c643fcddb335518d988070524f871160fb67769ca106d990b | [source](https://lehd.ces.census.gov/data/qwi/latest_release/ne/version_qwi.txt) |
| qwi_version_nv.txt | retrieved vintage | 2026-10-09T01:22:58.503206+00:00 | 200 / 197 | 170e823b0a3302f0462a1ea302414122fe7cb6d80e853180d72d9ba12e5b72fb | [source](https://lehd.ces.census.gov/data/qwi/latest_release/nv/version_qwi.txt) |
| qwi_version_nh.txt | retrieved vintage | 2026-10-09T01:22:58.722449+00:00 | 200 / 197 | ad72ec2eca3223cba2eff49915cc9b024deefb1e9c72642575b6da16b9c9785c | [source](https://lehd.ces.census.gov/data/qwi/latest_release/nh/version_qwi.txt) |
| qwi_version_ny.txt | retrieved vintage | 2026-10-09T01:22:59.929120+00:00 | 200 / 197 | d22701fdf52ae09bb72033f6fba6ec67e4c6ba7ae5327bb3771be1cfcad3e433 | [source](https://lehd.ces.census.gov/data/qwi/latest_release/ny/version_qwi.txt) |
| qwi_version_nc.txt | retrieved vintage | 2026-10-09T01:22:59.950476+00:00 | 200 / 197 | cb230a3a5d939d34b6b1967d6ce89be0f8af66842b6b48cc78f18206e73f23ec | [source](https://lehd.ces.census.gov/data/qwi/latest_release/nc/version_qwi.txt) |
| qwi_version_nm.txt | retrieved vintage | 2026-10-09T01:22:59.921148+00:00 | 200 / 197 | 38b1950d7f14e3202377bfbe16ebdd35fde4a955d64f5d7bfb83ce78bb71d11a | [source](https://lehd.ces.census.gov/data/qwi/latest_release/nm/version_qwi.txt) |
| qwi_version_nd.txt | retrieved vintage | 2026-10-09T01:22:59.959267+00:00 | 200 / 197 | 004ccdcf7f87fa08f538c3789686abdcf838220d2d82092ddb815d33b6783bad | [source](https://lehd.ces.census.gov/data/qwi/latest_release/nd/version_qwi.txt) |
| qwi_version_nj.txt | retrieved vintage | 2026-10-09T01:22:59.914911+00:00 | 200 / 197 | b4587408303b5a46e76eaf9caa5e55f08ea8ef28bcd6e00b08b86ff647c65ad6 | [source](https://lehd.ces.census.gov/data/qwi/latest_release/nj/version_qwi.txt) |
| qwi_version_oh.txt | retrieved vintage | 2026-10-09T01:23:00.244567+00:00 | 200 / 197 | 678ee7a53aeab39a83fe134521a37514e1acd203b9088f97dd0e0202226bbdf8 | [source](https://lehd.ces.census.gov/data/qwi/latest_release/oh/version_qwi.txt) |
| qwi_version_pa.txt | retrieved vintage | 2026-10-09T01:23:01.382487+00:00 | 200 / 197 | f184c0ce4f7e0333696ee267a79b3603c056dd704572fa5b4c9158d843d9b9a6 | [source](https://lehd.ces.census.gov/data/qwi/latest_release/pa/version_qwi.txt) |
| qwi_version_ri.txt | retrieved vintage | 2026-10-09T01:23:01.386391+00:00 | 200 / 197 | 474c0aeb23fb66097ed9970a0f9b5a95609a289bbe6dc9ad5b4d25883f266c7e | [source](https://lehd.ces.census.gov/data/qwi/latest_release/ri/version_qwi.txt) |
| qwi_version_sc.txt | retrieved vintage | 2026-10-09T01:23:01.387425+00:00 | 200 / 197 | 4496dca22ccbb7d9462b5491a089ec378e58216f8723b421ddb706321ca4117d | [source](https://lehd.ces.census.gov/data/qwi/latest_release/sc/version_qwi.txt) |
| qwi_version_ok.txt | retrieved vintage | 2026-10-09T01:23:01.348547+00:00 | 200 / 197 | f13b4fe9f0d197a0412e6d66b4cd72af5efaa5049f2575d4470570c8193362c5 | [source](https://lehd.ces.census.gov/data/qwi/latest_release/ok/version_qwi.txt) |
| qwi_version_or.txt | retrieved vintage | 2026-10-09T01:23:01.374315+00:00 | 200 / 197 | 90b8f71a07e553ddd60ef5d549730f5e511a64fb7ae0b1f8eac6ddc6d8bd24cd | [source](https://lehd.ces.census.gov/data/qwi/latest_release/or/version_qwi.txt) |
| qwi_version_sd.txt | retrieved vintage | 2026-10-09T01:23:01.860551+00:00 | 200 / 197 | e0157a944198db66bfbe1836a3fee67b77b9c63eb65062e18fbd652dfe629a5a | [source](https://lehd.ces.census.gov/data/qwi/latest_release/sd/version_qwi.txt) |
| qwi_version_tn.txt | retrieved vintage | 2026-10-09T01:23:02.925098+00:00 | 200 / 197 | 13e2a1b27f97763ba7620d7e9f7afdb409af4d1aa29d584499482cc01f3ea91c | [source](https://lehd.ces.census.gov/data/qwi/latest_release/tn/version_qwi.txt) |
| qwi_version_wa.txt | retrieved vintage | 2026-10-09T01:23:03.442161+00:00 | 200 / 197 | e0925291569e98bb0ed345411e1e1a510e1de9975f5d837d7c6f14c613d21479 | [source](https://lehd.ces.census.gov/data/qwi/latest_release/wa/version_qwi.txt) |
| qwi_version_ut.txt | retrieved vintage | 2026-10-09T01:23:02.943017+00:00 | 200 / 197 | 6769cef606f1c852bee1126429ee10c93a8bcc129c44868b96d93b375be898cb | [source](https://lehd.ces.census.gov/data/qwi/latest_release/ut/version_qwi.txt) |
| qwi_version_tx.txt | retrieved vintage | 2026-10-09T01:23:02.933665+00:00 | 200 / 197 | 04719d772ea4d5006ba73eb4a67a00d0a677ccbdf287658a2d761c9603e09305 | [source](https://lehd.ces.census.gov/data/qwi/latest_release/tx/version_qwi.txt) |
| qwi_version_vt.txt | retrieved vintage | 2026-10-09T01:23:02.948463+00:00 | 200 / 197 | 8505453559ea5ad9a0575683238fd4afa876b1f74352b2f98c81dd166f26335a | [source](https://lehd.ces.census.gov/data/qwi/latest_release/vt/version_qwi.txt) |
| qwi_version_va.txt | retrieved vintage | 2026-10-09T01:23:03.381900+00:00 | 200 / 197 | 93736bbef63e6e4bf23954389bdfa84a3f6d67aadf9ab3d110ecce1be4d33b6d | [source](https://lehd.ces.census.gov/data/qwi/latest_release/va/version_qwi.txt) |
| qwi_version_wi.txt | retrieved vintage | 2026-10-09T01:23:05.016768+00:00 | 200 / 197 | f21c8a5803416626460069dabd9b091a5d6d75a15aae9c8ac18de22a626ec743 | [source](https://lehd.ces.census.gov/data/qwi/latest_release/wi/version_qwi.txt) |
| qwi_version_wv.txt | retrieved vintage | 2026-10-09T01:23:05.015128+00:00 | 200 / 197 | bf91ae413f42d25003c971a13fef3935394d1bc19dd470b266f76fe6f3f1a58a | [source](https://lehd.ces.census.gov/data/qwi/latest_release/wv/version_qwi.txt) |
| qwi_version_wy.txt | retrieved vintage | 2026-10-09T01:23:05.020179+00:00 | 200 / 197 | 95eaf165ebf5e972c058828325469e3ce89e3dfcc2f93bfe91574e62ab66e66a | [source](https://lehd.ces.census.gov/data/qwi/latest_release/wy/version_qwi.txt) |
| qwi_size_ca | retrieved vintage | 2026-10-09T01:23:06.573507+00:00 | 200 / 0 | HEAD metadata only | [source](https://lehd.ces.census.gov/data/qwi/latest_release/ca/qwi_ca_sa_f_gc_ns_op_u.csv.gz) |
| qwi_size_de | retrieved vintage | 2026-10-09T01:23:08.346565+00:00 | 200 / 0 | HEAD metadata only | [source](https://lehd.ces.census.gov/data/qwi/latest_release/de/qwi_de_sa_f_gc_ns_op_u.csv.gz) |
| qwi_size_mi | retrieved vintage | 2026-10-09T01:23:09.908448+00:00 | 200 / 0 | HEAD metadata only | [source](https://lehd.ces.census.gov/data/qwi/latest_release/mi/qwi_mi_sa_f_gc_ns_op_u.csv.gz) |
| acs_lookup.txt | retrieved vintage | 2026-10-09T01:23:14.217012+00:00 | 200 / 1621211 | 19687946ed8c7bf8405d613b746de8c9da2ff1909a3b8a730a19d241d1b3ff2b | [source](https://www2.census.gov/programs-surveys/acs/summary_file/2019/documentation/user_tools/ACS_5yr_Seq_Table_Number_Lookup.txt) |
| acs_de_20195de0002000.zip | retrieved vintage | 2026-10-09T01:23:16.038027+00:00 | 200 / 91570 | 3d86220f6070c65cdefd9e525d654bd5c7b294e9b7a17b8792437272877831ae | [source](https://www2.census.gov/programs-surveys/acs/summary_file/2019/data/5_year_seq_by_state/Delaware/All_Geographies_Not_Tracts_Block_Groups/20195de0002000.zip) |
| acs_de_20195de0058000.zip | retrieved vintage | 2026-10-09T01:23:17.533003+00:00 | 200 / 141553 | 1f2410b55329d3764e9cb79db8d119495e0ae60e4795bf1e3d8755899a12ad1a | [source](https://www2.census.gov/programs-surveys/acs/summary_file/2019/data/5_year_seq_by_state/Delaware/All_Geographies_Not_Tracts_Block_Groups/20195de0058000.zip) |
| acs_de_20195de0111000.zip | retrieved vintage | 2026-10-09T01:23:19.168354+00:00 | 200 / 231508 | 04854fe9402e588ef9df33d0362fc40047daf9b4c42cca9106f0bb358c6b4610 | [source](https://www2.census.gov/programs-surveys/acs/summary_file/2019/data/5_year_seq_by_state/Delaware/All_Geographies_Not_Tracts_Block_Groups/20195de0111000.zip) |
| acs_de_20195de0114000.zip | retrieved vintage | 2026-10-09T01:23:20.938042+00:00 | 200 / 181030 | 09a02ee31cb968bdf0d9707ac94eb676ce2a504acc5c55e1548b0d713d97913e | [source](https://www2.census.gov/programs-surveys/acs/summary_file/2019/data/5_year_seq_by_state/Delaware/All_Geographies_Not_Tracts_Block_Groups/20195de0114000.zip) |
| acs_de_geo.csv | retrieved vintage | 2026-10-09T01:23:22.738226+00:00 | 200 / 208010 | 068411246b38aa283b0aaf40be0df5876b5f44837edeb87ceb24bcc8b70e2911 | [source](https://www2.census.gov/programs-surveys/acs/summary_file/2019/data/5_year_seq_by_state/Delaware/All_Geographies_Not_Tracts_Block_Groups/g20195de.csv) |
| ct_final_changes.pdf | retrieved vintage | 2026-10-09T01:23:24.053459+00:00 | 200 / 76103 | 84607142334d7d29aa86f2cd55a65eb80d2817f810cb10adb1839b7c96d6b2b6 | [source](https://www2.census.gov/geo/pdfs/reference/ct_county_equiv_change.pdf) |
| onet_soc2018.xlsx | retrieved vintage | 2026-10-09T01:24:38.200927+00:00 | 200 / 44847 | bfc6722a92c2d607e5a99dee88b7826cf5aa91f7c0453182e0c8268e32a20a19 | [source](https://www.onetcenter.org/taxonomy/2019/soc/2019_to_SOC_Crosswalk.xlsx?fmt=xlsx) |
| soc2018_structure.pdf | retrieved vintage | 2026-10-09T01:24:41.174468+00:00 | 403 / — | HTTP Error 403:  | [source](https://www.bls.gov/soc/2018/soc_structure_2018.pdf) |
| soc2018_guidelines.pdf | retrieved vintage | 2026-10-09T01:24:42.518577+00:00 | 403 / — | HTTP Error 403:  | [source](https://www.bls.gov/soc/2018/soc_2018_class_prin_cod_guide.pdf) |
| hmda2018_resource_head | retrieved vintage | 2026-10-09T01:24:43.625023+00:00 | 200 / 0 | HEAD metadata only | [source](https://files.ffiec.cfpb.gov/static-data/snapshot/2018/2018_public_lar_csv.zip) |
| hmda2025_resource_head | retrieved vintage | 2026-10-09T01:24:45.137631+00:00 | 200 / 0 | HEAD metadata only | [source](https://files.ffiec.cfpb.gov/static-data/snapshot/2025/2025_public_lar_csv.zip) |
| pums_us_resource_head | retrieved vintage | 2026-10-09T01:24:46.460800+00:00 | 403 / — | HTTP Error 403:  | [source](https://www2.census.gov/programs-surveys/acs/data/pums/2019/5-Year/csv_pus.zip) |
| pums_us_size_head | retrieved vintage | 2026-10-09T01:32:24.072871+00:00 | 200 / 0 | HEAD metadata only | [source](https://www2.census.gov/programs-surveys/acs/data/pums/2019/5-Year/csv_pus.zip) |
| pums_us_directory.bin | retrieved vintage | 2026-10-09T01:32:25.240491+00:00 | 206 / 65536 | 305f946686690ad85b2fcb8bc7baa94176b6f02555ba0542cfb36edf7c87f903 | [source](https://www2.census.gov/programs-surveys/acs/data/pums/2019/5-Year/csv_pus.zip) |

The table shows the last attempt per logical object; earlier 403/SSL/404 attempts remain in the append-only manifest. For repeated retrieval the last attempt can fail even when an earlier valid file exists; offline validation uses the matching successful hash. The guessed ACS filename/PUMS code-list URL and the BLS workbook route returned 404/403; only the subsequently observed official successful sources are used. API HTTP 200 is insufficient: `acs_counties.json` is HTML Missing Key, explicitly excluded from data-value use.

## Unavailable research sources

Original assignment, GPT review, full GPT–Claude cross-review and the distinct Claude-only state audit have no retrieved bytes or content hashes. They are not fabricated manifest entries. The local Claude package has an independent file-hash manifest; repository access evidence and the preserved request live under `audit/`. Web-tool verification of the HMDA public field documentation and BLS SOC hierarchy establishes source context, but does not supply a locally hashed original document or complete machine-readable hierarchy. BLS hierarchy remains unused for filling occupational matches.

## Derived artifacts

`local_artifact_manifest.json` hashes ignored derived CSV prefixes and local audit outputs separately from source downloads. `research_document_manifest.json` hashes every preserved local review. The audit validator confirms every available downloaded body against a successful acquisition hash. Full raw source responses are intentionally not committed.
