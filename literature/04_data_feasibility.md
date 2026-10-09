---
project: genai-entry-jobs-mortgage
document: data_feasibility
model: claude-opus-5-5 (Claude Opus 5.5, Claude Code desktop)
date: 2026-10-08
status: independent_review
research_cutoff: 2026-10-08
---

# 04 — Data Feasibility Audit

## 0. Scope and method

This document evaluates whether a fully code-acquired, reproducible panel can link (i) GenAI exposure, (ii) young-worker labor outcomes, and (iii) HMDA mortgage outcomes within one week. Every availability claim below rests on one of three kinds of evidence:

- `[HEAD]` — an HTTP HEAD request returned status 200 (sizes as reported by the server, 2026-10-08).
- `[SCHEMA]` — we downloaded a header, a small file, or a single state/county extract and inspected its columns.
- `[DOC]` — official documentation.

Claims marked `[OPEN]` still require a feasibility run. No full-scale data collection was performed. The largest objects actually downloaded were the Delaware QWI county-sector file, about 3,900 HMDA rows for one county, and the CT 2024 purchase originations (about 35k rows), all used as schema probes.

Target machine (checked): macOS, 16 GB RAM, 8 cores, 73 GB free disk. `~/Desktop` is a regular local folder, not an iCloud-synced path. This matters because iCloud "Optimize Storage" can evict large files.

---

## 1. Dataset registry

### D01 — HMDA Snapshot National Loan/Application Register (FFIEC/CFPB)

| # | Item | Content |
|---|---|---|
| 1 | Official source / URL | `https://files.ffiec.cfpb.gov/static-data/snapshot/{YYYY}/{YYYY}_public_lar_csv.zip`; documentation `https://ffiec.cfpb.gov/documentation/publications/loan-level-datasets/lar-data-fields` |
| 2 | Exact files | `2018_public_lar_csv.zip` … `2025_public_lar_csv.zip` (pipe-delimited alternatives `_pipe.zip`) |
| 3 | Coverage | Activity years 2017–2025 (2018+ used); all HMDA reporters; national |
| 4 | Unit | Application or purchased loan (one row per record) |
| 5 | Required variables | See `03_hmda_methods_audit.md` §1.2 |
| 6 | Download method | Plain HTTPS GET (curl/requests); no API needed `[HEAD]` |
| 7 | Authentication | None |
| 8 | Availability 2026-10-08 | Verified for 2018, 2024, 2025 by HEAD (sizes 823.7 MB, 664.2 MB, 737.1 MB zipped). 2019–2023 URLs follow the same pattern and are listed in the site's JS bundle. `[OPEN F1]` HEAD-check all 8. |
| 9 | Cleaning / matching | Unzip → CSV → read only about 25 columns → filter (DEC-H10–H19) → Parquet. County FIPS → CZ (D13). |
| 10 | Usable in one week? | **Yes.** Est. 6–8 GB download in total. Processing is streaming and column-pruned (DuckDB). |
| 11 | Limitations | Binned age; no occupation; no credit score; no applicant ID; reporting-threshold changes 2020–2022; CT geography break 2024 |
| 12 | Fallback | Data Browser CSV by state (`/view/csv?years=Y&states=XX&…`). It returns the full row schema, so age can be tabulated locally. This avoids the national zips but needs 49 calls × 8 years. |

### D02 — HMDA Data Browser API (validation only)

| # | Item | Content |
|---|---|---|
| 1 | URL | `https://ffiec.cfpb.gov/v2/data-browser-api/view/aggregations?years=…&states=…&actions_taken=…&loan_purposes=…` |
| 4 | Unit | Aggregated counts and sums by the requested filter combination |
| 6 | Method | GET; JSON |
| 7 | Auth | None |
| 8 | Availability | Verified for 2018, 2022, 2023, 2024, 2025 `[SCHEMA]` |
| 11 | Limitations | **No age filter** (the `ages` parameter is silently ignored `[SCHEMA]`). Serves the snapshot vintage. |
| — | Role | Independent check of the local loan-level aggregation (REQ-VAL-01) |

### D03 — HMDA Transmittal Sheet (lender list)

`https://files.ffiec.cfpb.gov/static-data/snapshot/2025/2025_public_ts_csv.zip` `[HEAD]` (194,185 B). It is used to describe lenders. Lender type (bank vs non-bank) would have to come from the agency code. `[OPEN]` The TS schema has not been inspected. Not needed for the main design, which uses LEI × year FE.

### D04 — Census Quarterly Workforce Indicators (QWI), LEHD bulk files

| # | Item | Content |
|---|---|---|
| 1 | URL | `https://lehd.ces.census.gov/data/qwi/latest_release/{st}/` ; schema `https://lehd.ces.census.gov/data/schema/latest/` |
| 2 | Exact files | `qwi_{st}_sa_f_gc_ns_op_u.csv.gz` (sex × **age**, all firms, **county**, NAICS **sector**, private ownership, not seasonally adjusted). Finer industry files at county level: `_gc_n3_` and `_gc_n4_`. 5- and 6-digit NAICS exist **only at state level** (`_gs_n5_`, `_gs_n6_`) `[SCHEMA]` (DE directory listing). |
| 3 | Coverage | Release **R2026Q3** (files dated 2026-07-30 to 2026-08-11). End quarter **2025Q4** for 47 states + DC; **Michigan ends 2021Q4**; **Alaska ends 2016Q2** `[SCHEMA]` (`version_qwi.txt` for all 51 directories). Start quarters vary (e.g. MA 2010Q1, DC 2005Q2, AZ 2004Q1). All states cover 2010Q1+ except AK. |
| 4 | Unit | County × sex × age group × industry × quarter (jobs at private employers located in the county, i.e. **workplace-based**) |
| 5 | Required variables | `geography, industry, sex, agegrp, year, quarter, Emp, EmpS, HirA, Sep, EarnS, EarnHirAS` + status flags `sEmp, sHirA, sEarnS, …` `[SCHEMA]` |
| 6 | Method | HTTPS GET of gz files; or Census API `api.census.gov/data/timeseries/qwi/sa` (returned empty without a key in our test `[OPEN]`) |
| 7 | Auth | None for bulk. The API key is free and optional. |
| 8 | Availability | Verified (above) |
| 9 | Cleaning | Keep `sex == 0`, `industry == "00"` (all industries; present in the sector file `[SCHEMA]`), `agegrp ∈ {A03,A04,A05,A06}`. Status flags: 1 OK; 5 suppressed; 6 calculated (no distortion); 9 fuzzed / significantly distorted; −1/−2 no data `[DOC]` `label_flags.csv`. Aggregate counties → CZ. |
| 10 | Usable in one week? | **Yes** for county × age × quarter totals (sector files: 216 MB for CA, the largest state `[HEAD]`). County × NAICS-4 is heavy (CA alone 1.39 GB). Avoid it unless design D-D is run at 4-digit level. |
| 11 | Limitations | **No occupation.** Workplace-based. Private sector only (`op`). Jobs, not persons. Small-cell suppression (Tucker P005 reports ~1% of early-career employment and hires censored at state × industry level). MI and AK lack recent data. |
| 12 | Fallback | QWI via Census API (needs key; many calls). LEHD **J2J** for job-to-job flows (not evaluated). |

**Verified joint breakdown.** QWI *does* provide county × age group × industry × quarter in a single row (e.g. the DE sector file contains `geography=10003, industry=51, agegrp=A03, year=2024, quarter=4, Emp=86, HirA=22`) `[SCHEMA]`. It does **not** provide occupation at any geography.

**QWI age groups** `[DOC]` (`label_agegrp.csv`): A01 14–18, A02 19–21, A03 22–24, A04 25–34, A05 35–44, A06 45–54, A07 55–64, A08 65–99.

### D05 — American Community Survey PUMS 2015–2019 5-year (Census)

| # | Item | Content |
|---|---|---|
| 1 | URL | `https://www2.census.gov/programs-surveys/acs/data/pums/2019/5-Year/csv_pus.zip` (2,238,752,642 B `[HEAD]`); dictionary `https://www2.census.gov/programs-surveys/acs/tech_docs/pums/data_dict/PUMS_Data_Dictionary_2015-2019.txt` `[SCHEMA]` |
| 3 | Coverage | Persons, 2015–2019 pooled, all states; geography = 2010 PUMA (≥100k population) |
| 4 | Unit | Person record with weight `PWGTP` |
| 5 | Variables | `ST, PUMA, AGEP, ESR, SOCP, OCCP, SCHL, NAICSP, PWGTP` (all present in the 2015–2019 dictionary `[SCHEMA]`). `OCCP` is documented as "Occupation recode for 2018 and later based on 2018 OCC codes" and `SOCP` as "SOC codes for 2018 and later based on 2018 SOC codes". |
| 6 | Method | HTTPS GET |
| 7 | Auth | None |
| 8 | Availability | Verified `[HEAD]` |
| 9 | Cleaning | Keep civilian employed (`ESR ∈ {1,2}`), ages 22–34 (main) and other bands. Map `SOCP` → Eloundou β (D06). PUMA → CZ with D13 allocation factors. |
| 10 | One week? | **Yes** (single 2.2 GB download; read 9 columns). |
| 11 | Limitations | Sample-based; PUMA geography (CZ allocation adds noise); **`[OPEN F5]`** whether 2015–2017 records in this 5-year file carry 2018-scheme `SOCP` codes (the dictionary wording suggests harmonization, but this must be verified empirically: share of employed records with blank/invalid `SOCP` by survey year). |
| 12 | Fallback | ACS PUMS 2018–2022 5-year (uniform 2018 SOC, but mixes PUMA10/PUMA20: `PUMA10` for 2018–2021, `PUMA20` for 2022 `[SCHEMA]`); or industry-based exposure (D04 × D10, design D-D). |

### D06 — Eloundou, Manning, Mishkin & Rock (P001) occupational LLM exposure

| # | Item | Content |
|---|---|---|
| 1 | URL | `https://raw.githubusercontent.com/openai/GPTs-are-GPTs/main/data/occ_level.csv` (126,022 B `[HEAD]`) |
| 2 | Columns | `O*NET-SOC Code, Title, dv_rating_alpha, dv_rating_beta, dv_rating_gamma, human_rating_alpha, human_rating_beta, human_rating_gamma` `[SCHEMA]`; 923 occupations |
| 3 | Coverage | O*NET-SOC (8-digit, e.g. `11-1011.03`) |
| 4 | Unit | Occupation |
| 5 | Variables | `dv_rating_beta` (GPT-4-rated β = E1 + 0.5·E2) main; `human_rating_beta` robustness. Definitions: E1 = direct exposure (LLM cuts task time ≥50%); E2 = exposure with LLM-powered software; α = E1, β = E1 + 0.5·E2, ζ/γ = E1 + E2 `[DOC]` P001 arXiv v. §3. |
| 6–8 | Method / auth / availability | GitHub raw; none; verified |
| 9 | Matching | O*NET-SOC 8-digit → SOC 2018 6-digit: truncate to `XX-XXXX` and take the **simple mean** over 8-digit children. Canaries (P004 §1.2) also converts to 6-digit SOC; its exact averaging rule is not stated, so ours is `PROVISIONAL`. SOC 6-digit → ACS `SOCP`: exact match after removing the hyphen. For `SOCP` codes containing `X` (aggregated groups), use the mean over matching 6-digit SOC codes. Military `55-xxxx` is unmatched (dropped). |
| 10 | One week? | Yes |
| 11 | Limitations | Exposure is a *capability* rating as of 2023, not adoption or displacement. GPT-4 ratings may be unstable across rating models (an NBER WP by Yin, Vu & Persico on multi-model replication was seen only as a title, `UNVERIFIED`). |
| 12 | Fallback | `human_rating_beta`; D07; D08 |

### D07 — Felten, Raj & Seamans AI exposure (P002)

`https://github.com/AIOE-Data/AIOE` (HTTP 200). Repository files `[SCHEMA]` (GitHub API listing): `AIOE_DataAppendix.xlsx` (AIOE / AIIE / AIGE from P002), `Language Modeling AIOE and AIIE.xlsx` (language-modeling exposure), `Image Generation AIOE and AIIE.xlsx`. Unit: SOC occupation (and industry; county for AIGE per the P002 abstract). **Use:** robustness exposure (LM-AIOE). `[OPEN]` Sheet names and SOC vintage are not inspected. Requires `openpyxl`.

### D08 — Anthropic Economic Index (P003)

`https://huggingface.co/datasets/Anthropic/EconomicIndex` (HTTP 200). Usage-based task shares with automation vs augmentation labels (P003; used by P004 Fact 5). **Caveat:** measured from **post-2024 usage**, so it is a post-treatment object. Use **only** as a heterogeneity/robustness exposure. Exact files and release `[OPEN]`.

### D09 — O*NET database

`https://www.onetcenter.org/dl_files/database/db_29_0_text.zip` (13.2 MB `[HEAD]`). **Not required** in the main pipeline, because D06 is already at O*NET-SOC level. Keep as fallback for occupation titles and SOC concordance.

### D10 — BLS Occupational Employment and Wage Statistics (OEWS), May 2022

| # | Item | Content |
|---|---|---|
| 1 | URL | National industry-specific (4-digit NAICS × SOC): `https://www.bls.gov/oes/special-requests/oesm22in4.zip` (31.4 MB `[HEAD]`); MSA × SOC: `…/oesm22ma.zip` (39.0 MB); national: `…/oesm22nat.zip` |
| 6 | Method | HTTPS GET **with a browser-like User-Agent header** (BLS blocks default clients; returned 200 with a UA string) |
| 7 | Auth | None |
| 9 | Use | Industry exposure $X_i=\sum_o e_{io}\beta_o$ for design D-D (staffing patterns), and an MSA-level exposure robustness check (workplace-based, not age-specific) |
| 11 | Limitations | Excel files (`openpyxl`); suppressed cells (`**`, `#`); SOC 2018 |
| 12 | Fallback | ACS PUMS industry × occupation shares (D05), as in Tucker (P005) |

### D11 — Census Population Estimates (PEP), county by age

| # | Item | Content |
|---|---|---|
| 1 | URL | 2020–2025: `https://www2.census.gov/programs-surveys/popest/datasets/2020-2025/counties/asrh/cc-est2025-agesex-all.csv` (10.2 MB `[HEAD]`). 2010–2020 intercensal: `https://www2.census.gov/programs-surveys/popest/datasets/2010-2020/intercensal/county/asrh/cc-est2020int-agesex-all.csv` (17.3 MB `[HEAD]`) |
| 5 | Variables | `STATE, COUNTY, YEAR, AGE1824_TOT, AGE2024_TOT, AGE2529_TOT, AGE3034_TOT, AGE3539_TOT, AGE4044_TOT, AGE4549_TOT, AGE5054_TOT, …` `[SCHEMA]` (V2025 header) |
| 9 | Mapping to HMDA bins | `<25` ↔ `AGE1824`; `25-34` ↔ `AGE2529+AGE3034`; `35-44` ↔ `AGE3539+AGE4044`; `45-54` ↔ `AGE4549+AGE5054`. `YEAR` codes must be mapped (V2025: 1 = April 1 2020 base, 2…7 = July 1 2020…2025 `[OPEN]` confirm from file layout doc). |
| 11 | Limitations | Vintage seam between intercensal (≤2019) and V2025 (≥2020). The 2024 revision of net international migration altered population controls (noted by P004 §5 for ACS weights). Use only as an exposure offset or for robustness rates. |

### D12 — FHFA House Price Index, county annual

`https://www.fhfa.gov/hpi/download/annual/hpi_at_county.csv` (5.3 MB `[HEAD]`). Use: pre-period price growth control and the mechanism event study (the price channel found by P035/P036). `[OPEN]` columns not inspected.

### D13 — Geographic crosswalks (David Dorn)

- County → 1990 CZ: `https://www.ddorn.net/data/cw_cty_czone.zip` (13 KB `[HEAD]`)
- 2010 PUMA → 1990 CZ with allocation factors: `https://www.ddorn.net/data/cw_puma2010_czone.zip` (27 KB `[HEAD]`)
- Established in the local-labor-market literature (M19, M20).
- `[OPEN F3]` Variable names inside the Stata files (expected `cty_fips`, `czone`, `puma2010`, `afactor`) are **not yet inspected**. Coverage of post-1990 county codes is also unverified.

### D14 — Teleworkability (Dingel & Neiman, M21)

`https://raw.githubusercontent.com/jdingel/DingelNeiman-workathome/master/occ_onet_scores/output/occupations_workathome.csv` (45 KB `[HEAD]`). O*NET-SOC teleworkability; used as a control (P004 uses it too).

### D15 — Census Gazetteer tracts (only if CT is harmonized)

`https://www2.census.gov/geo/docs/maps-data/data/gazetteer/Gaz_tracts_national.zip` (2.5 MB `[HEAD]`). Not needed under DEC-H18 (CT excluded).

### D16 — ACS 5-year county tables via Census API (pre-period affordability)

`api.census.gov/data/2019/acs/acs5?get=B25077_001E,B19013_001E&for=county:*` (median home value; median household income). `[OPEN]` Not tested in this session. Fallback: compute from PUMS household file (heavier) or use FHFA HPI levels.

### Datasets considered and not selected

| Dataset | Reason not selected |
|---|---|
| ADP payroll (used by P004) | Proprietary; not code-downloadable |
| Revelio / LinkedIn (P006, P008) | Proprietary |
| Lightcast postings (P009) | Proprietary |
| CPS monthly microdata | Public, but too thin for local × age × occupation cells (P004 §5 "high levels of noise"; P007 uses 12-month moving averages nationally) |
| BLS QCEW | County × industry, but **no age**. Redundant with QWI for our purposes. |
| BLS LAUS | County unemployment, **no age** |
| NY Fed CCP / Equifax (P024) | Restricted |
| Confidential HMDA (P022, P023, P028) | Restricted |
| PSEO (LEHD graduate outcomes) | Graduation cohorts are too old for a post-2022 window `[INFERENCE, not verified]` |
| ACS 1-year PUMS 2023–2025 (residence-based first stage) | Viable *secondary* source for residence-based labor outcomes and homeownership by exact HMDA age bins. 2025 1-year PUMS release status as of 2026-10-08 is `[OPEN]`. Deferred to robustness to protect the one-week budget. |

---

## 2. Can the required joint breakdowns be obtained?

| Needed object | Source | Joint breakdown actually published? | Verdict |
|---|---|---|---|
| Local × age × **occupation** employment, pre-period | ACS PUMS (D05) | Yes, by construction from person records, at PUMA level; not published as tables | **Feasible** with PUMA→CZ allocation |
| Local × age × **occupation** employment, post-2022, quarterly | None public | QWI has no occupation; OEWS has no age; CPS is too thin | **Not feasible.** This is the key structural limitation. |
| Local × age × industry × quarter employment / hires / earnings | QWI (D04) | Yes, county × age × NAICS (sector/3/4-digit) × quarter in one row `[SCHEMA]` | **Feasible** |
| Local × age mortgage applications × year | HMDA (D01) | Yes, after loan-level aggregation | **Feasible** |
| Local × age population | PEP (D11) | Yes (5-year bands) | **Feasible** |
| County × occupation (all ages) | OEWS MSA (D10) or ACS tables | MSA × occupation yes; county × occupation by **age** no | Use only for robustness |

**Implication.** Exposure can be measured age-specifically and occupation-based in the *pre-period* (PUMS). The *post-period* labor first stage can only be measured by age × industry × place (QWI), not by age × occupation × place. The first stage therefore tests whether places with high young-worker occupational exposure show relative declines in young-worker employment and hiring. It does not observe occupation-level displacement locally. This is a reduced-form, place-based first stage.

---

## 3. Occupational concordances

| Step | From | To | Method | Status |
|---|---|---|---|---|
| C1 | O*NET-SOC 2019 8-digit (D06) | SOC 2018 6-digit | Truncate `XX-XXXX.YY` → `XX-XXXX`; simple mean of β over children | PROVISIONAL |
| C2 | SOC 2018 6-digit | ACS `SOCP` (6 characters, no hyphen; some codes aggregated with `X`) | Exact match; for `X` codes, mean over matching detailed codes | PROVISIONAL (match rate must be ≥ 98% of weighted employment, REQ-VAL-05) |
| C3 | SOC 2018 6-digit | OEWS `OCC_CODE` (SOC 2018) | Exact match (D-D only) | PROVISIONAL |
| C4 | O*NET-SOC | Dingel–Neiman teleworkability | Same as C1 | PROVISIONAL |
| C5 | OEWS 4-digit NAICS | QWI NAICS sector (`ns`) or 3-digit (`n3`) | Aggregate employment-weighted β up the NAICS tree | PROVISIONAL (D-D only) |

The Census OCCP ↔ SOC crosswalk is **not** needed if `SOCP` is used directly.

---

## 4. Geographic and temporal alignment

| Source | Native geography | Time | Alignment to CZ × year |
|---|---|---|---|
| HMDA | County (property location) | Calendar year of action | County → CZ (D13) |
| QWI | County (workplace) | Quarter | County → CZ; quarterly kept for the first stage; annual average for scaling |
| ACS PUMS | 2010 PUMA (residence) | 2015–2019 pooled | PUMA → CZ allocation factors (D13) |
| PEP | County (residence) | July 1 | County → CZ |
| FHFA HPI | County | Year | County → CZ (housing-unit or population weights `[OPEN]`) |
| OEWS | National industry; MSA | May 2022 | Industry-level (D-D) |

**Workplace vs residence.** QWI (workplace) and HMDA (residence) are aligned through CZs, which are built from commuting flows (M19). County-level analysis would mis-assign commuters. This is why CZ is the primary unit (DEC-H40).

**Boundary cases**
1. **Connecticut.** Excluded (HMDA 2024+ planning regions; QWI/PEP may also use planning regions in recent vintages `[OPEN]`).
2. **Michigan.** No QWI after 2021Q4. It is excluded from the first stage and kept in HMDA analyses; HMDA results are also reported on the QWI-consistent sample.
3. **Alaska, Hawaii.** Excluded (QWI AK ends 2016Q2; contiguous-US CZ convention).
4. **Post-1990 county codes.** Patch table (DEC-H41).
5. **County `NA` in HMDA.** Dropped; share reported (CT 2024 probe: 359 of about 34,850 originations).

---

## 5. Reproducibility and computational budget

| Step | Data volume | Approach | Est. time on target machine `[INFERENCE]` |
|---|---|---|---|
| HMDA download | about 6–8 GB zipped | Sequential download with SHA-256 manifest; resume on failure | 30–90 min, network-bound |
| HMDA processing | about 15–30M rows/year | `unzip -p` streamed into DuckDB `read_csv` with explicit column types and selected columns only; filter; write Parquet partitioned by year | 1–2 h total |
| QWI download | about 2–3 GB gz (sector files, 49 states + DC) | gz read directly by DuckDB/pandas; keep `sex=0`, `industry=00` | 30–60 min |
| PUMS | 2.2 GB zip | Read 9 columns | 10–20 min |
| Estimation (cell level) | about 600–720 CZs × 2–4 ages × 8 years | PPML with 3 FE sets: seconds | — |
| Estimation (application level, D-F) | up to about 3–5M purchase decisions/year | **Memory risk** with 16 GB RAM and lender × year FE. Use years 2021–2025 or a deterministic 25% hash sample, or estimate at lender × CZ × age × year cell level. | `[OPEN F6]` |

**Dependency management (recommended).**
- Either Python 3.11 with `duckdb`, `polars`/`pandas`, `pyarrow`, `pyfixest` (PPML, OLS with HD FE, clustered SE), `openpyxl` and `matplotlib`;
- or R ≥ 4.3 with `fixest` (more mature `fepois`).
- One language for estimation is preferable, to keep a single-command build simple. See `07` REQ-REPRO.

**Cold-start risks**
- BLS requires a User-Agent header.
- The Census API may need a key for repeated calls. Avoid it by using bulk files.
- FFIEC file names could change. Pin the URLs and record SHA-256 hashes at first download.
- Large downloads should be resumable (`curl -C -`).

---

## 6. Feasibility verdict

| Component | Verdict |
|---|---|
| HMDA 2018–2025 by age × CZ × year | **Feasible** (verified URLs, schema, probe counts) |
| Pre-period, age-specific, occupation-based exposure | **Feasible, pending F5** (PUMS SOCP harmonization) and **F3** (crosswalk inspection) |
| Post-period local young-worker labor outcomes | **Feasible via QWI** (industry, not occupation; MI/AK excluded) |
| Population denominators | Feasible (vintage seam caveat) |
| Within one week, single command | **Feasible if** the application-level module is capped (F6) and robustness is limited to the pre-specified list |

The highest-priority feasibility checks (F1–F8) are listed in `07_recommended_research_plan.md` Part II §J.
