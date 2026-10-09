# Day 1–2 Feasibility Gate Report

Date: 2026-10-09 (Asia/Shanghai). Scope: Day 1–2 feasibility only. Retrieval timestamps are UTC in the source manifest.

## Recommendation

**C. A critical data dependency remains unresolved and needs further work.** CZ remains the provisional preferred geography and State the pre-specified feasibility fallback. No treatment coefficient or treatment-effect significance was estimated or inspected. No geography was chosen using outcome regressions.

**Evidence labels.** VERIFIED DATA FACT = directly downloaded/parsed or official metadata; TECHNICAL ASSUMPTION = diagnostic implementation rule; UNRESOLVED CHOICE = design/mapping policy not fixed; RECOMMENDATION = action supported by those facts. PASS is limited to the stated procedure and denominator; FAIL rejects the tested configuration; OPEN has an unresolved dependency.

HMDA access, eight-year schemas, Dorn key integrity, small-state auxiliary access and streaming arithmetic are verified. The strict official-membership occupational mapping covers only 71.178%/71.530% of DE employed residents aged 22–34/25–34, and national weighted coverage is not observed. Numeric SOC hierarchy, unrated occupations, group weights and one published invalid member remain unresolved. Four required research-document sets and the existing repository history are inaccessible. State aggregation cannot repair these exposure/provenance dependencies, so a definitive fallback recommendation would be premature.

## Gate summary

| Gate | Outcome | Interpretation |
| --- | --- | --- |
| A — HMDA | PASS access/schema; OPEN national funnel | All eight capped snapshot samples obtained; names differ across route/year. |
| B — Occupations | FAIL tested coverage; OPEN completed concordance | No prefix fill, final exposure or nationwide coverage claim. |
| C — Geography | PASS base crosswalk; FAIL unbridged CT; OPEN universe | 2019 inventory candidates are not mortgage-coverage evidence. |
| D — Auxiliary | PASS tested sources; OPEN national cells/controls | MI post-2021 missing; official ACS bulk alternative works. |
| E — Compute | PASS bounded correctness; OPEN production budget | Exact sizes observed, national runtime/memory not extrapolated. |
| Research provenance | OPEN | Eight local Claude files only; distinct cross-reviews are not merged. |

## Year-specific HMDA evidence

| Year | Prefix rows | ZIP bytes | CSV bytes | Required concepts |
| --- | --- | --- | --- | --- |
| 2018 | 4377 | 823719647 | 5856369323 | 15/15 |
| 2019 | 5331 | 980129414 | 6816270981 | 15/15 |
| 2020 | 5370 | 1460346740 | 10029803062 | 15/15 |
| 2021 | 5948 | 1517879241 | 10206391218 | 15/15 |
| 2022 | 4269 | 877742261 | 6058473013 | 15/15 |
| 2023 | 4812 | 624535331 | 4339556230 | 15/15 |
| 2024 | 5103 | 664242987 | 4625405352 | 15/15 |
| 2025 | 5030 | 737139477 | 5114449258 | 15/15 |

Each sample is the complete CSV lines decompressed from a fixed 256 KiB archive prefix. The truncated last line is discarded. These are deterministic, nonrandom schema probes. Raw range hashes are not full-archive hashes. 2018 has `loan_to_value_ratio`; 2019–2025 have `combined_loan_to_value_ratio`. Other snapshot field names/order are stable after that change; all eight snapshots have 99 columns. Data Browser has a different naming convention, including hyphens in `open-end_line_of_credit`, co-applicant fields and repeated race/ethnicity/AUS/denial-reason fields.

## Early and late observed codes and types

| Required concept | Safe analytic type | 2018 observed | 2025 observed |
| --- | --- | --- | --- |
| activity_year | coded integer stored as CSV text | 2018 | 2025 |
| applicant_age | string bin | 25-34, 35-44, 45-54, 55-64, 65-74, <25 | 25-34, 35-44, 45-54, 55-64, 65-74, 8888, <25, >74 |
| action_taken | coded integer stored as CSV text | 1, 2, 3, 4, 5 | 1, 2, 3, 4, 5, 6 |
| loan_purpose | coded integer stored as CSV text | 1, 2, 31, 32, 4 | 1, 2, 31, 32, 4, 5 |
| lien_status | coded integer stored as CSV text | 1, 2 | 1, 2 |
| occupancy_type | coded integer stored as CSV text | 1, 2, 3 | 1, 2, 3 |
| construction_method | coded integer stored as CSV text | 1 | 1, 2 |
| total_units | string bin | 1, 2, 3, 4 | 1, 100-149, 2, 25-49, 3, 4, 5-24, 50-99, >149 |
| loan_type | coded integer stored as CSV text | 1, 2, 3, 4 | 1, 2, 3, 4 |
| reverse_mortgage | coded integer stored as CSV text | 2 | 1111, 2 |
| open-end_line_of_credit | coded integer stored as CSV text | 1, 2 | 1, 1111, 2 |
| business_or_commercial_purpose | coded integer stored as CSV text | 2 | 1, 1111, 2 |
| county_code | string identifier | 646 distinct identifiers; see full code-count JSON | 548 distinct identifiers; see full code-count JSON |
| state_code | string identifier | 50 distinct identifiers; see full code-count JSON | AL, AR, AZ, CA, CO, CT, FL, GA, IA, ID, IL, IN, KY, LA, MA, MD, ME, MI, MN, MS, MT, NC, ND, NE, NH, NJ, NM, NV, OH, OK, OR, PA, RI, SC, SD, TN, TX, VA, WA, WV |
| lei | string identifier | 2 distinct identifiers; see full code-count JSON | 9 distinct identifiers; see full code-count JSON |

Detailed counts for all eight years and CT extracts are in `results/feasibility/hmda_field_codes.json`. `8888` is non-applicable applicant age; preserve it as a separate category/exclusion flag. `1111` denotes partial exemption in the three product indicators. `NA` county and blank values remain distinct from Exempt/non-applicable values. Retaining exempt product indicators follows the available review only provisionally: exemption does not prove the product is code 2. Numeric parsing is applied only after sentinel separation. `total_units` must retain its multiunit ranges, never integer-cast blindly.

## Tests and acceptance boundary

### R01 — Research-document and repository provenance

- **Status:** OPEN.
- **Source and URL:** [Requested GitHub repository](https://github.com/ZhenghuiQu/genai-entry-jobs-mortgage).
- **Procedure:** Inspect local files, their provenance headers and Git state; attempt clone and authenticated connector read.
- **Observed evidence:** Eight unchanged independent Claude review files exist. Original assignment PDF, GPT package, full GPT–Claude cross-review and distinct Claude-only state audit are unavailable. Clone required authentication; connector returned 404.
- **Limitations:** Cannot assert these documents are absent from the remote repository; its tree and AGENTS.md are inaccessible.
- **Implication for CZ versus State:** Only the current request establishes CZ preference and State fallback; missing versions cannot be merged.
- **Next required action:** Provide a verified checkout/connection and all four missing document sets; integrate additive files without overwriting remote history.

### A01 — Official 2018–2025 snapshot access

- **Status:** PASS.
- **Source and URL:** [FFIEC/CFPB snapshot files](https://files.ffiec.cfpb.gov/static-data/snapshot/2025/2025_public_lar_csv.zip) and [field documentation](https://ffiec.cfpb.gov/documentation/publications/loan-level-datasets/lar-data-fields).
- **Procedure:** hmda_probe.py: HEAD, final 65,536 archive bytes, first 262,144 bytes; require HTTP 206 for ranges and reject full-object responses.
- **Observed evidence:** All eight HEADs returned 200 with Chrome-compatible TLS; ZIP directories and bounded CSV records were parsed for every year.
- **Limitations:** Standard urllib/curl returned 403. No full ZIP CRC or complete-file SHA256 was computed.
- **Implication for CZ versus State:** The same mortgage source supports either geography.
- **Next required action:** Use the demonstrated client, retain snapshot/ETag metadata, and verify full-file hashes only at authorized acquisition.

### A02 — Required-field schema and year differences

- **Status:** PASS.
- **Source and URL:** [FFIEC/CFPB snapshot files](https://files.ffiec.cfpb.gov/static-data/snapshot/2025/2025_public_lar_csv.zip) and [field documentation](https://ffiec.cfpb.gov/documentation/publications/loan-level-datasets/lar-data-fields).
- **Procedure:** hmda_analyze.py compares all headers and audits 15 required concepts as text.
- **Observed evidence:** All required concepts exist in all eight 99-column snapshot headers. Snapshot open_end_line_of_credit differs from Data Browser open-end_line_of_credit. The 2018 loan_to_value_ratio becomes combined_loan_to_value_ratio in 2019–2025.
- **Limitations:** The official public field page is not a literal snapshot header. Other naming differences between delivery routes are enumerated in hmda_schema_comparison.json.
- **Implication for CZ versus State:** Both geographies require explicit delivery-route and year adapters.
- **Next required action:** Freeze the observed adapters before writing the national parser; do not reuse the prior asserted CSV names.

### A03 — Observed codes and sentinel preservation

- **Status:** PASS.
- **Source and URL:** [FFIEC/CFPB snapshot files](https://files.ffiec.cfpb.gov/static-data/snapshot/2025/2025_public_lar_csv.zip) and [field documentation](https://ffiec.cfpb.gov/documentation/publications/loan-level-datasets/lar-data-fields).
- **Procedure:** Count raw string values, blank, NA, Exempt and 1111 before any filtering; preserve age/unit bins and identifiers.
- **Observed evidence:** 2025 prefix has all eight age categories including 8888; reverse/open-end/business each have 392 code-1111 records out of 5,030. 2019 and 2021 prefixes contain county NA; CT extracts quantify county NA.
- **Limitations:** Prefix order is highly selective (2018 age 25–34 is 4,362/4,377); absence of a code in a sample is not absence nationally. Text Exempt is not observed in these three indicators.
- **Implication for CZ versus State:** Sentinel handling is identical across geographies; State can retain records with known state but unavailable county.
- **Next required action:** Keep separate missing/non-applicable/exempt flags; do not coerce 8888 or 1111 into ages/units or code 2.

### A04 — National sample-funnel and representativeness

- **Status:** OPEN.
- **Source and URL:** [FFIEC/CFPB snapshot files](https://files.ffiec.cfpb.gov/static-data/snapshot/2025/2025_public_lar_csv.zip) and [field documentation](https://ffiec.cfpb.gov/documentation/publications/loan-level-datasets/lar-data-fields).
- **Procedure:** Apply the existing provisional purchase filters to each downloaded sample and save stage counts.
- **Observed evidence:** hmda_filter_funnel.json records observed sample retention under actions 1–5, first lien, principal residence, site-built 1–4 units, and indicator no-or-exempt rules.
- **Limitations:** Only CT extracts are complete for their queried purchase-origination subset; national prefixes are not random and do not supply national application counts or rare-cell distributions.
- **Implication for CZ versus State:** Neither geography receives national acceptance counts from this test.
- **Next required action:** After parser/exposure approval, perform a count-only streaming census of the intended universe; keep all exclusions and reporting-threshold diagnostics.

### D01 — QWI age coverage and Michigan limitation

- **Status:** PASS.
- **Source and URL:** [LEHD QWI releases](https://lehd.ces.census.gov/data/qwi/latest_release/).
- **Procedure:** Fetch version_qwi.txt for all 50 states+DC, parse the unadjusted QWI_F interval, and retain all release strings.
- **Observed evidence:** All 51 retrieved manifests identify R2026Q3/V4.14.0. 49 end at 2025Q4; Michigan ends 2021Q4 and Alaska 2016Q2. A03=22–24, A04=25–34, A05=35–44, A06=45–54.
- **Limitations:** Publication endpoint is not proof of nonmissing county cells; adjusted/seasonal variants end one quarter earlier and are not the tested unadjusted series.
- **Implication for CZ versus State:** MI’s post-period mechanism data are unavailable at either geography; cross-border CZ membership needs handling.
- **Next required action:** Pre-specify a harmonized mechanism sample; do not treat unreleased MI values as zero or carry them forward.

### D02 — Observed QWI employment/hiring missingness

- **Status:** PASS.
- **Source and URL:** [DE QWI county-sector file](https://lehd.ces.census.gov/data/qwi/latest_release/de/qwi_de_sa_f_gc_ns_op_u.csv.gz) and [status labels](https://lehd.ces.census.gov/data/schema/latest/label_flags.csv).
- **Procedure:** Select geo_level C, ind_level A, sex 0, industry 00, A03–A06, 2016Q1–2025Q4; compare against a complete 3×4×40 grid.
- **Observed evidence:** 480 expected and observed county-age-quarter cells; no duplicates, missing Emp/HirA or absent cells; every sEmp/sHirA is 1.
- **Limitations:** Only DE totals were examined. The file also contains state aggregates, which must be excluded; national/small-industry suppression is unresolved. QWI jobs are workplace-based, not persons/resident occupations.
- **Implication for CZ versus State:** Small-state mechanism-source arithmetic is available; State does not remove national missingness.
- **Next required action:** Audit missingness nationally by geography/age/quarter with flags -2,-1,5,11 distinct from distorted-but-released 7,9,12.

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

### E02 — Bounded DuckDB streaming aggregation correctness

- **Status:** PASS.
- **Source and URL:** [FFIEC/CFPB snapshot files](https://files.ffiec.cfpb.gov/static-data/snapshot/2025/2025_public_lar_csv.zip) and [field documentation](https://ffiec.cfpb.gov/documentation/publications/loan-level-datasets/lar-data-fields).
- **Procedure:** compute_probe.py: 256 MB engine limit, two threads; group county×age×action; compare every count with an independent Python csv.Counter; repeat on gzip.
- **Observed evidence:** All three samples pass exact count equality: 4,377 early rows, 5,030 late rows and 35,676 CT late rows. The largest plain/gzip scans take 0.266/0.327 seconds in the recorded run; peak process RSS is 137.4 MB.
- **Limitations:** Tiny/warm-cache samples are not national throughput measurements; ZIP is not read directly by DuckDB, and engine memory limits do not cap whole-process RSS.
- **Implication for CZ versus State:** Both aggregation geographies have a demonstrated parser/arithmetic path.
- **Next required action:** Spool one validated CSV or feed a tested bounded decompression stream; measure a larger approved count-only pilot before a national timing commitment.

### E03 — National resource and deadline guarantee

- **Status:** OPEN.
- **Source and URL:** [FFIEC/CFPB snapshot files](https://files.ffiec.cfpb.gov/static-data/snapshot/2025/2025_public_lar_csv.zip) and [field documentation](https://ffiec.cfpb.gov/documentation/publications/loan-level-datasets/lar-data-fields).
- **Procedure:** Separate exact archive sizes/measured samples from hypothetical production budgets.
- **Observed evidence:** All-years ZIP+CSV retention would use 60.73 GB before auxiliary files/output/spill. The tested machine’s free space leaves little room for that layout.
- **Limitations:** No complete national scan, CZ hash-join, Parquet size, spill peak, network-throughput or implementation deadline was measured; no full regression performance test is allowed in this stage.
- **Implication for CZ versus State:** Neither A nor B follows from the microbenchmark; missing exposure/document dependencies independently require C.
- **Next required action:** After the critical concordance is resolved, approve a sequential storage plan and bounded representative pilot; record a concrete deadline before any deadline-based fallback.

## Detailed occupation and geography gates

Tests B01–B05 are recorded in [occupation_crosswalk_audit.md](occupation_crosswalk_audit.md); C01–C05 in [geography_audit.md](geography_audit.md). Every test is also available as a structured record in `results/feasibility/test_register.json`. Sources, versions, hashes and failures are indexed in [data_source_registry.md](data_source_registry.md). Unresolved design choices are in [design_decisions_pending.md](design_decisions_pending.md).

## Computational recommendation

Exact HMDA totals imply 7.686 GB compressed and 53.047 GB expanded (decimal GB). Retaining both consumes 60.732 GB, versus the free disk recorded in `compute_audit.json` (about 65.4 GB), leaving only about 4.7 GB before PUMS, QWI, output or spill. The largest one-year CSV is 10.206 GB. Recommend a single-year ZIP/CSV spool followed by column-pruned aggregation and deletion under a documented retention policy; do not start that download now. A hypothetical 7.686 GB ZIP archive plus one largest CSV is 17.892 GB, before auxiliary/output/spill; this is arithmetic, not a measured production peak. National PUMS metadata-only HEAD/ZIP-tail reads establish 2.239 GB compressed and 10.384 GB expanded person CSVs. No national PUMS records were downloaded. QWI CA/DE/MI HEAD sizes are in `qwi_download_sizes.json`. Small samples do not justify a national runtime estimate or application-level regression RAM claim.

## Reproduction and stopping rule

See the root README and Makefile. `make feasibility-analyze` rebuilds local audits/reports from the capped ignored downloads; `make feasibility` also repeats bounded acquisition. The append-only manifest records unsuccessful attempts as well as successful bodies. Raw data and the local virtual environment are Git-ignored. Original review files and this request are preserved with hashes. Repository-access limitations are recorded in `audit/repository_access.md`; the available AI audit summary is explicitly not a complete native transcript export.

Stop at this evidence report. The next instruction may resolve exposure/geography/document dependencies; national regressions, robustness and paper drafting require a subsequent implementation instruction.
