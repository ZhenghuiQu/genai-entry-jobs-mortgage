---
project: genai-entry-jobs-mortgage
document: recommended_research_plan
model: claude-opus-5-5 (Claude Opus 5.5, Claude Code desktop)
date: 2026-10-08
status: independent_review
research_cutoff: 2026-10-08
---

# 07 — Recommended Research Plan

## Scope

This document is in two parts, following the assignment's suggested two-layer structure.

- **Part I** gives the economic design: the question, the logic, and the identification argument, without implementation detail.
- **Part II** is a numbered implementation specification that a coding agent can follow without inventing central methodological choices.

The document ends with a quality-control self-audit and the section *Critical Weaknesses and Unresolved Questions*.

**Provenance of requirements**
- `[ASSIGNMENT]`: required by `研究任务说明.pdf`. This covers HMDA from ffiec.cfpb.gov, code-only data acquisition, one-command replication, an AER-style LaTeX paper, a research plan citing literature for each setting, a GitHub history and AI logs.
- `[LIT: Pxxx]`: literature-based.
- `[REC]`: our recommendation.

Status labels: `DECIDED`, `PROVISIONAL`, `OPEN`, `REJECTED`.

---

# PART I — ECONOMIC RESEARCH DESIGN

## I.1 Research question

**Narrowed question `[REC]`.** Did local mortgage markets where *young* workers were more exposed to large language models see a relative decline in young households' home-purchase mortgage demand after the release of ChatGPT? And is that pattern consistent with an entry-level labor-market channel, rather than with house-price, interest-rate or tech-cycle channels?

This narrows the assignment's question `[ASSIGNMENT]`, "whether and how shocks to young people's employment and income transmit to the mortgage market", for two reasons.

1. **The labor shock is contested.** It is documented for workers aged 22–25 in exposed occupations in payroll, résumé and administrative data (P004, P005, P006). But its timing and attribution are disputed (P008, P009), and it is small in representative survey data (P004 §5) and null in Danish data (P010).
2. **Public mortgage data cannot link individuals to occupations.** HMDA has no occupation or employment field, so the transmission can only be tested at the level of local markets and age groups.

## I.2 Motivation from the literature

- **Labor.** Adjustment to GenAI has run through reduced *hiring* of young workers in exposed occupations, not through layoffs or base pay (P004 Facts 4 and 6; P005; P006; P007).
- **Housing.** Young households' purchase decisions depend on down-payment accumulation and debt-to-income limits (P017, P023), on earnings risk (P016; Paz-Pardo 2024), and on debt burdens (P019). First-time and lower-income buyers are the most sensitive to financing conditions (P022).
- **AI and housing.** Places more exposed to AI saw *faster* house-price growth after 2022 (P035, P036). This makes the naive expectation, that "hit regions weaken", non-obvious, and it introduces a competing channel.
- **Gap.** No study, as of 2026-10-08, examines whether GenAI exposure changed the age composition of mortgage demand, or separates labor channels from price channels (`06` §6).

## I.3 Transmission channels (summary; details in `06`)

| Channel | Story | Key prediction |
|---|---|---|
| M1 Employment and earnings | Fewer and later entry-level jobs mean lower income and down payments | Young applications fall, mostly at the youngest ages, and the decline grows over time. A labor first stage exists. |
| M2 Expectations and risk | Flatter or riskier career ladders mean delayed irreversible purchases | Fewer young applications with positively selected applicants. Not separately identifiable. |
| M3 Selection | Marginal applicants drop out | Counts fall. Denial and pricing changes are ambiguous in sign. |
| M4 Lender response | Lenders tighten for young applicants in exposed markets | Conditional denial rises within lender, including "employment history" reasons. |
| A1 Price channel (competing) | AI raises local prices and prices out first-time buyers | Prices rise; young applicants' loan sizes and DTI rise. |
| A2/A3 Rates and tech cycle (confounders) | The 2022 tightening and the tech correction | The break starts in 2022, before ChatGPT. |

## I.4 Identification logic

The research design compares three things:
1. young (25–34) with prime-age (35–44) home-purchase applicants;
2. within the same local labor-and-housing market (commuting zone) and year;
3. across markets that differed, *before 2020*, in how exposed their young workers' occupations were to LLM capabilities.

The comparison is made before vs after 2022.

**What the design removes.** Comparing ages within a market-year removes every local shock that shifts all buyers alike: local credit supply, general local demand, and the common component of local price changes.

**What it cannot remove.** Shocks that hit young buyers *differently* in exactly the places that are more exposed, such as rate shocks in expensive markets or AI-driven price growth. The design addresses these with three tools:
- pre-period controls for affordability and FHA reliance, each allowed to affect young buyers differently every year;
- pre-trend and sensitivity analysis over 2018–2021, a window that includes both a rate increase and a rate decrease;
- predictions that distinguish channels: the age gradient, the timing of the break, the movement of house prices, and the direction of young applicants' loan sizes.

A parallel analysis of young-worker employment and hiring (Census QWI) tests whether the presumed labor shock exists in the same places and periods.

**Interpretation.** Estimates are *local-market exposure effects on the age composition of mortgage demand*. They are not effects of AI adoption, effects on individual workers, or credit-supply effects.

## I.5 Hypotheses (pre-specified)

| ID | Hypothesis | Role |
|---|---|---|
| H1 | Young (25–34) relative to prime-age (35–44) purchase applications declined more after 2022 in CZs with higher young-worker exposure | **Primary** |
| H2 | Young-worker employment and hiring (QWI) declined relative to prime-age workers in the same CZs and period | First stage |
| H3 | The decline is proportionally larger for applicants under 25 than for 25–34 | Age gradient (M1) |
| H4 | The effect is absent before 2022 and grows over 2023–2025 | Timing (M1 vs A2/A3) |
| H5 | Applicant composition and unconditional denial change in ways that differ from conditional (within-lender) denial | Selection (M3 vs M4) |
| H6 | High-exposure CZs did not experience relative house-price increases that would explain the young decline. Equivalently, young applicants' loan sizes did not rise. | Price channel (A1) |

The primary test is H1. The ranking of designs and these hypotheses were fixed **before** any estimation. Statistical significance did not and must not determine the design `[REC]`.

**Tension to disclose.** The assignment notes that, like most journals, reviewers prefer results supported by significant estimates `[ASSIGNMENT]`. Pre-specification is the appropriate response: report the pre-specified primary estimate whatever its sign or significance, and label any later specification as exploratory.

## I.6 Expected contribution and limits

- **Primary contribution:** a new empirical fact about age-specific mortgage-demand responses to GenAI exposure, using complete public HMDA data for 2018–2025.
- **Secondary contribution:** a set of tests that separate a labor channel from price and rate channels.
- **Possible contribution, depending on results:** reconciling rising prices in exposed markets with weaker young demand.
- **Limits:**
  - no individual linkage;
  - a contested labor first stage;
  - a 25–34 HMDA bin that is only partly the affected age;
  - expectations that cannot be distinguished from price channels;
  - denial and pricing that cannot be read as credit supply.

---

# PART II — IMPLEMENTATION SPECIFICATION

Requirements are numbered `REQ-<area>-<nn>`. Each has a status. A coding agent must not change a `DECIDED` item without recording a deviation in `docs/deviations.md`.

## A. Repository layout and conventions

**REQ-REPO-01 (DECIDED).** Layout:
```
Makefile                 # `make all` = full replication
env/                     # lockfile(s)
src/00_download/         # one script per source; writes data/raw/ + data/raw/MANIFEST.csv (url, bytes, sha256, utc_time)
src/10_build/            # cleaning → data/intermediate/*.parquet
src/20_analysis/         # estimation → output/tables/*.tex, output/figures/*.pdf, output/estimates/*.csv
src/30_validate/         # validation tests → output/validation/report.md (fails build on error)
paper/                   # LaTeX (AER style) reading output/
docs/                    # research plan (copy of this spec), deviations.md, ai_log/
data/                    # git-ignored
```

**REQ-REPO-02 (DECIDED).**
- All FIPS codes are stored as zero-padded strings: state 2 digits, county 5 digits.
- CZ IDs are integers, as in Dorn's files.
- Years are integers.
- HMDA age bins are kept as the exact public strings.

**REQ-REPO-03 (DECIDED).** The data directory must not sit in an iCloud-synced folder.

## B. Data acquisition (all by code; no manual steps) `[ASSIGNMENT]`

| REQ | Source | Exact URL(s) | Status |
|---|---|---|---|
| REQ-DATA-01 | HMDA snapshot LAR 2018–2025 | `https://files.ffiec.cfpb.gov/static-data/snapshot/{Y}/{Y}_public_lar_csv.zip`, Y = 2018…2025 | DECIDED |
| REQ-DATA-02 | HMDA Data Browser aggregations (validation) | `https://ffiec.cfpb.gov/v2/data-browser-api/view/aggregations?years={Y}&actions_taken={a}&loan_purposes=1` (nationwide; optionally `&states=XX`) | PROVISIONAL (nationwide call not yet tested) |
| REQ-DATA-03 | QWI county × age × sector | `https://lehd.ces.census.gov/data/qwi/latest_release/{st}/qwi_{st}_sa_f_gc_ns_op_u.csv.gz` for 48 contiguous states + DC; record `version_qwi.txt` | DECIDED |
| REQ-DATA-04 | ACS PUMS 2015–2019 5-year persons | `https://www2.census.gov/programs-surveys/acs/data/pums/2019/5-Year/csv_pus.zip` | PROVISIONAL (F5) |
| REQ-DATA-05 | Eloundou et al. exposure | `https://raw.githubusercontent.com/openai/GPTs-are-GPTs/main/data/occ_level.csv`. Pin to a commit hash at download time. | DECIDED |
| REQ-DATA-06 | Dorn crosswalks | `https://www.ddorn.net/data/cw_cty_czone.zip`, `https://www.ddorn.net/data/cw_puma2010_czone.zip` | PROVISIONAL (F3) |
| REQ-DATA-07 | PEP county age | `…/popest/datasets/2020-2025/counties/asrh/cc-est2025-agesex-all.csv`; `…/popest/datasets/2010-2020/intercensal/county/asrh/cc-est2020int-agesex-all.csv` | DECIDED (robustness use) |
| REQ-DATA-08 | FHFA county HPI | `https://www.fhfa.gov/hpi/download/annual/hpi_at_county.csv` | DECIDED (mechanism) |
| REQ-DATA-09 | ACS 2015–2019 county B25077, B19013 | Census API `https://api.census.gov/data/2019/acs/acs5?get=NAME,B25077_001E,B19013_001E&for=county:*` | PROVISIONAL (F7) |
| REQ-DATA-10 | Dingel–Neiman teleworkability | `https://raw.githubusercontent.com/jdingel/DingelNeiman-workathome/master/occ_onet_scores/output/occupations_workathome.csv` | DECIDED (control X5) |
| REQ-DATA-11 | OEWS May 2022 national industry × occupation | `https://www.bls.gov/oes/special-requests/oesm22in4.zip` (send a browser-like `User-Agent`) | DECIDED (D-D only) |
| REQ-DATA-12 | Felten LM-AIOE | `https://github.com/AIOE-Data/AIOE` → `Language Modeling AIOE and AIIE.xlsx` | PROVISIONAL (robustness) |

**REQ-DATA-20 (DECIDED).** Every download is written with a SHA-256 hash to `data/raw/MANIFEST.csv`. Later runs verify the hashes and stop on mismatch, unless `ALLOW_VINTAGE_CHANGE=1` is set, in which case the change is logged.

## C. Geography

- **REQ-GEO-01 (DECIDED).** The analysis unit is the 1990 CZ, from `cw_cty_czone`.
- **REQ-GEO-02 (DECIDED).**
  - Main sample: the 48 contiguous states plus DC, **excluding CT** (all years).
  - AK, HI and PR are excluded.
  - **MI** is excluded from QWI first-stage regressions only (QWI ends 2021Q4). HMDA results are also reported on the sample without MI.
- **REQ-GEO-03 (PROVISIONAL, F3).** County patch table. Map any HMDA, QWI or PEP county code missing from `cw_cty_czone` to its 1990-era predecessor or containing county. Write `config/county_patch.csv` with columns (fips_new, fips_old, note).
  - Acceptance: after patching, 0 retained HMDA records lack a CZ.
- **REQ-GEO-04 (DECIDED).** A multi-state CZ is assigned to the state containing the largest share of its 2019 population (from PEP), for state clustering and state × year FE.
- **REQ-GEO-05 (DECIDED).** County-level robustness uses the same filters, without CZ aggregation.

## D. HMDA build

- **REQ-HMDA-01 (DECIDED).** Read only these columns: `activity_year, lei, state_code, county_code, census_tract, derived_dwelling_category, action_taken, loan_type, loan_purpose, lien_status, reverse_mortgage, open-end_line_of_credit, business_or_commercial_purpose, loan_amount, loan_to_value_ratio, rate_spread, loan_term, intro_rate_period, occupancy_type, income, debt_to_income_ratio, applicant_age, co-applicant_age, denial_reason-1, denial_reason-2, denial_reason-3, denial_reason-4, ffiec_msa_md_median_family_income`. Read all as strings, then cast explicitly.
- **REQ-HMDA-02 (DECIDED).** Main population PURCH = DEC-H10 … DEC-H19 (`03` §4.2).
  - `loan_purpose == "1"`
  - `lien_status == "1"`
  - `occupancy_type == "1"`
  - `derived_dwelling_category == "Single Family (1-4 Units):Site-Built"`
  - `reverse_mortgage == "2"`, `open-end_line_of_credit == "2"`, `business_or_commercial_purpose == "2"`
  - `action_taken ∈ {"1","2","3","4","5"}`
  - `applicant_age ∈ {"<25","25-34","35-44","45-54","55-64","65-74",">74"}`
  - `county_code` matches `^\d{5}$`
  - state not in {AK, HI, CT, PR} and not a territory
- **REQ-HMDA-03 (DECIDED).** Write the filter funnel per year to `output/validation/hmda_funnel.csv`: records remaining after each successive filter.
- **REQ-HMDA-04 (DECIDED).** Cell outcomes per CZ × `applicant_age` × year follow DEC-H20 … DEC-H33 (`03` §4.3). Formulas:
  - $N^{app}=\#\{\text{action}\in1..5\}$; $N^{dec}=\#\{1,2,3\}$; $N^{orig}=\#\{1\}$; $N^{den}=\#\{3\}$; $D=N^{den}/N^{dec}$.
  - `inc_ln_mean` = mean of $\ln(\text{income})$ over $0<\text{income}\le1000$.
  - `lmi_share` = share with $1000\cdot\text{income}<0.8\cdot$`ffiec_msa_md_median_family_income` among non-NA income. Income ≤ 0 counts as LMI.
  - `dti_gt43` = share with DTI string ∈ {"44",…,"49","50%-60%",">60%"} among DTI ∉ {"NA","Exempt",""}.
  - `dti_ge50` = share with DTI ∈ {"50%-60%",">60%"}.
  - `lnloan_mean` = mean of $\ln(\text{loan\_amount})$.
  - `fha_share` = share with `loan_type == "2"`.
  - `cltv_ge95` = share with numeric `loan_to_value_ratio` ≥ 95 among numeric.
  - `rs_mean` = mean `rate_spread` over action 1 with `loan_type == "1"`, `loan_term == "360"`, `intro_rate_period == "NA"`, and numeric rate spread.
  - `den_reason_k` for k ∈ {1,2,3,5} = among action 3, share with any `denial_reason-j == k`.
  - Also store denominators for every share.
- **REQ-HMDA-05 (DECIDED).** Missing-data reporting: NA and Exempt shares by year × age × exposure tercile for income, DTI, CLTV and rate spread → `output/validation/hmda_missing.csv`.
- **REQ-HMDA-06 (PROVISIONAL, F6).** Application-level file for D-F: action ∈ {1,2,3}, PURCH, ages `<25`, `25-34`, `35-44`, `45-54`. Columns: CZ, year, age, LEI, denied, income bin, DTI bin, CLTV bin, ln loan bin, loan type, co-applicant indicator (`co-applicant_age != "9999"`), and the four denial reasons.
  - If memory exceeds 12 GB, use a deterministic sample: keep a record if `hash(lei||county||tract||loan_amount||row_number_within_file) mod 4 == 0`. Record the seed and rule.
- **REQ-HMDA-07 (DECIDED).** Consistent-reporter flag: an LEI is consistent if it appears in the PURCH sample in every year 2018–2025.
- **REQ-HMDA-08 (DECIDED).** Boundary cases:
  - `income` may be negative → included only in LMI counts.
  - `loan_amount` is always numeric in the public file; drop and count if not.
  - Empty strings are treated like NA.
  - Duplicate rows cannot be identified; do not deduplicate.

## E. Exposure

- **REQ-EXP-01 (PROVISIONAL).** Occupation scores. From `occ_level.csv` take `dv_rating_beta`. Set `soc6 = O*NET-SOC code[:7]` (e.g. `"15-1252"`). $\beta_{soc6}$ is the simple mean over 8-digit rows with the same `soc6`. Store the count of children.
- **REQ-EXP-02 (PROVISIONAL, F5).** PUMS mapping:
  - `socp6 = SOCP` (6 characters).
  - If `SOCP` has no `X`: match to `soc6` with the hyphen removed.
  - If it contains `X`: $\beta$ = mean of $\beta_{soc6}$ over `soc6` whose first characters match the non-X prefix.
  - Unmatched records (e.g. military `55xxxx`) are excluded from numerator and denominator.
- **REQ-EXP-03 (DECIDED).** Population: PUMS persons with `ESR ∈ {1,2}` (civilian employed), `AGEP ∈ [22,34]`, non-missing `SOCP`.
- **REQ-EXP-04 (DECIDED).** CZ exposure:
$$
E_c=\frac{\sum_i \text{PWGTP}_i\,\text{afactor}_{p(i),c}\,\beta_{o(i)}}{\sum_i \text{PWGTP}_i\,\text{afactor}_{p(i),c}},
$$
  where the PUMA key is built exactly as in Dorn's `cw_puma2010_czone` (F3). Then $z_c=(E_c-\text{mean}_c E_c)/\text{sd}_c(E_c)$ over CZs in the main sample (unweighted).
- **REQ-EXP-05 (DECIDED).** Also compute, for robustness and description:
  - $E^{16+}_c$ (all employed ages ≥ 16);
  - $E^{22\text{–}24}_c$;
  - $E^{35\text{–}44}_c$;
  - human-rated β;
  - exposure excluding SOC major group 15 (computer and mathematical);
  - LM-AIOE (REQ-DATA-12).
- **REQ-EXP-06 (DECIDED).** Industry exposure for D-D (`05` §2):
  - $X_i$ = OEWS May 2022 national 4-digit-NAICS employment-weighted mean of $\beta_{soc6}$ (`OCC_GROUP == "detailed"` rows only, numeric `TOT_EMP`), aggregated to NAICS sector with OEWS employment weights.
  - Shares $s_{ci}$ from QWI 2019Q1–Q4 average `Emp` for A03 + A04 by sector.
- **REQ-EXP-07 (DECIDED).** Exposure is time-invariant and fixed before any outcome is examined. Write it to `data/intermediate/exposure_cz.parquet` and hash it.

## F. QWI first stage

- **REQ-QWI-01 (DECIDED).** Keep rows with `geo_level == "C"`, `sex == "0"`, `industry == "00"`, `ownercode == "A05"`, `agegrp ∈ {A03, A04, A05, A06}`, `year ≥ 2016`.
- **REQ-QWI-02 (DECIDED).** Status flags (LEHD `label_flags.csv`):
  - set a value to missing if its flag ∈ {−2, −1, 5, 11} (no data, or suppressed);
  - keep all other released values {1, 6, 7, 9, 10, 12} in the main spec;
  - in robustness (REQ-ROB-16), also set the "significantly distorted" flags {7, 9, 12} to missing.
- **REQ-QWI-03 (DECIDED).** Aggregate to CZ × age × quarter:
  - Sum `Emp`, `HirA` and `EmpS` over counties.
  - Earnings: $\text{EarnS}_{c}=\sum_{k}\text{EarnS}_{k}\text{EmpS}_{k}/\sum_k \text{EmpS}_{k}$ over counties $k$ with both values non-missing.
  - Record `share_missing` = 1 − (Emp of non-missing counties / Emp of all counties, where available).
- **REQ-QWI-04 (DECIDED).** Event-time reference: 2022Q4 for `Emp` (beginning of quarter); 2022Q3 for `HirA` `[LIT: P005]`.
- **REQ-QWI-05 (DECIDED).** Sample: 47 states + DC (contiguous, excluding CT and MI), 2016Q1–2025Q4. Drop CZ × age series with more than 20% missing quarters.

## G. Controls and population

- **REQ-CTRL-01 (PROVISIONAL, F7).** X1 = ln(B25077 / B19013), ACS 2015–2019, county → CZ, weighted by owner-occupied units (or county population if unavailable).
- **REQ-CTRL-02 (DECIDED).** X2 = FHA share of PURCH applications aged 25–34 in 2018–2019, by CZ.
- **REQ-CTRL-03 (DECIDED).** X3, X4, X5 from PUMS (22–34 employed):
  - bachelor's or higher: `SCHL ≥ 21`;
  - tech industry: `NAICSP` codes for 5112, 518, 519, 5415 (exact PUMS strings to be confirmed in F5);
  - teleworkable share using Dingel–Neiman scores mapped like REQ-EXP-01/02.
- **REQ-POP-01 (DECIDED).** PEP mapping: `<25` → AGE1824; `25-34` → AGE2529 + AGE3034; `35-44` → AGE3539 + AGE4044; `45-54` → AGE4549 + AGE5054.
  - 2018–2019 come from the intercensal file; 2020–2025 from V2025, July estimates.
  - Used only as a PPML offset in REQ-ROB-11.

## H. Estimation

- **REQ-EST-01 (DECIDED) — Primary (D-B pooled).** Sample: CZ × a × t with a ∈ {`25-34`, `35-44`}, t ∈ 2018…2025. PPML:
$$
\mathbb{E}[N^{app}_{cat}]=\exp\big(\beta\,z_cY_a\text{Post}_t+\alpha_{ct}+\gamma_{at}+\delta_{ca}+\textstyle\sum_{k\ne2022}(X1_c,X2_c)\,Y_a\mathbb{1}[t=k]\,\theta_k\big).
$$
  - Report $\hat\beta$, its SE clustered by state, and $100(e^{\hat\beta}-1)$.
- **REQ-EST-02 (DECIDED) — Event study (D-C).** Replace $\text{Post}_t$ with year indicators for k ≠ 2022.
  - Report the joint pre-trend Wald test (2018–2021).
  - Report HonestDiD relative-magnitude bounds for the 2025 coefficient with $\bar M \in \{0.5, 1, 2\}$ `[LIT: M03]`.
- **REQ-EST-03 (DECIDED) — Auxiliary and placebo ages.** Same as REQ-EST-01/02 with:
  - (`<25` vs `35-44`) — tests H3;
  - (`45-54` vs `35-44`) — placebo.
- **REQ-EST-04 (DECIDED) — Composition and rates (F-COMP).** OLS of each cell outcome from REQ-HMDA-04 on $z_cY_a\text{Post}_t$ with the same FE and controls, weighted by the outcome's denominator. Exclude cells with denominator < 20.
- **REQ-EST-05 (DECIDED) — First stage (D-C, QWI).**
  - PPML for `Emp` and `HirA`, with FE CZ × quarter, age × quarter and CZ × age.
  - Ages (A04 vs A05) main; (A03 vs A05) auxiliary.
  - Pooled post = quarters ≥ 2023Q1; plus a quarterly event study.
  - OLS for ln `EarnS`, weighted by `EmpS`.
- **REQ-EST-06 (PROVISIONAL, F6) — Conditional module (D-F).** LPM `denied ~ z·Y·Post | CZ^year + age^year + CZ^age + LEI^year` with risk bins (F2), then add `LEI^CZ^year` (F3).
  - Same structure for `rs` (rate spread) among originations, and for denial-reason indicators among denials.
- **REQ-EST-07 (DECIDED) — Price channel.** FHFA county HPI aggregated to CZ (weights per F7), then a CZ × year OLS event study:
$$
\ln \text{HPI}_{ct}=\sum_{k\ne2022}\rho_k z_c\mathbb{1}[t=k]+\mu_c+\lambda_{s(c)t}+\varepsilon_{ct}.
$$
- **REQ-EST-08 (DECIDED) — Levels (D-A).** For each age bin separately: PPML with CZ FE, state × year FE, and $z_c\times$year terms.
- **REQ-EST-09 (DECIDED) — Long difference (D-G).** As in `05` §2, weighted OLS with state FE. Pre period = 2018–2019; post = 2023–2025.
- **REQ-EST-10 (REJECTED) — IV.** No 2SLS. The ratio $\hat\beta/\hat\pi$ may be printed only in a "descriptive scaling" table footnote.

### Inference and multiple testing

- **REQ-INF-01 (DECIDED).** Main SEs are clustered by state. Robustness: CZ clusters.
- **REQ-INF-02 (PROVISIONAL).** AKM shift-share SEs for REQ-EST-01 (occupation-level shocks; R package `ShiftShareSE` or an equivalent implementation).
- **REQ-INF-03 (DECIDED).** Anderson (2008) sharpened q-values within families F-LAB, F-COMP and F-COND (`05` §8). The primary H1 test is unadjusted.

### Robustness (pre-specified; all reported regardless of results)

| REQ | Variation |
|---|---|
| REQ-ROB-01 | Comparison group `45-54` |
| REQ-ROB-02 | Outcome $N^{dec}$ (actions 1–3) |
| REQ-ROB-03 | Outcome $N^{orig}$ |
| REQ-ROB-04 | County as unit |
| REQ-ROB-05 | Drop the 10 CZs with the highest $z_c$ |
| REQ-ROB-06 | Consistent-reporter LEIs only (REQ-HMDA-07) |
| REQ-ROB-07 | Alternative exposures (REQ-EXP-05, REQ-EXP-06) |
| REQ-ROB-08 | Baselines: 2018–2019 only; 2022 only |
| REQ-ROB-09 | Horse-race controls X1–X5 |
| REQ-ROB-10 | D-G long difference |
| REQ-ROB-11 | PPML with ln PEP population offset |
| REQ-ROB-12 | Share-form linear DDD |
| REQ-ROB-13 | Three-year (2018–2022) and one-year (2023–2024) vintages |
| REQ-ROB-14 | Refinance applications (`loan_purpose ∈ {31,32}`) with the same structure. This is rate-sensitive, so it is a diagnostic of the rate channel, not a placebo for it. |
| REQ-ROB-15 | HMDA sample excluding MI (first-stage-consistent) |
| REQ-ROB-16 | QWI cells with distorted flags (7, 9, 12) set to missing |
| REQ-ROB-17 | Conventional-only and FHA-only application counts |

## I. Validation tests (the build fails on any FAIL)

| REQ | Test | Acceptance criterion | Status |
|---|---|---|---|
| REQ-VAL-01 | Loan-level vs API totals | For each year 2018–2025: count of records with `loan_purpose=1` by `action_taken ∈ {1,3}` (no other filters) in the local snapshot file **equals** the Data Browser aggregation for the same filters. State-level probe values for Delaware (`03` §1.4) must match exactly: 2025 originated 14,078 / denied 2,145; 2024 13,681 / 2,216; 2023 13,344 / 2,431; 2022 17,271 / 2,785; 2018 15,503 / 2,592. | PROVISIONAL (exact equality assumed because both are the snapshot) |
| REQ-VAL-02 | County probe | Kent County DE (`10001`), 2025, `loan_purpose=1`, actions 1–5, no other filters: total = 3,862; age counts `<25` 263, `25-34` 941, `35-44` 861, `45-54` 582, `55-64` 632, `65-74` 406, `>74` 119, `8888` 58; actions 1:2,490, 2:98, 3:539, 4:524, 5:211 | DECIDED (values observed 2026-10-08) |
| REQ-VAL-03 | CZ coverage | 0 PURCH records without a CZ after the patch; share of records dropped for county `NA` reported | PROVISIONAL |
| REQ-VAL-04 | PUMA allocation | For every PUMA, Σ afactor = 1 ± 1e-6 | PROVISIONAL |
| REQ-VAL-05 | Exposure match | Weighted share of PUMS 22–34 employed with matched β ≥ 0.98 | PROVISIONAL (threshold) |
| REQ-VAL-06 | QWI completeness | National share of A04 `Emp` in missing cells ≤ 0.02 per quarter | PROVISIONAL (threshold) |
| REQ-VAL-07 | Exposure face validity | Report the top 15 and bottom 15 CZs by $z_c$, and the correlations of $z_c$ with X1–X5. No pass/fail; a human reviews. | DECIDED |
| REQ-VAL-08 | Estimator sanity | PPML converged; number of observations dropped for separation reported; coefficient identical (≤1e-6) across two runs | DECIDED |
| REQ-VAL-09 | Snapshot integrity | SHA-256 in MANIFEST matches the re-download | DECIDED |
| REQ-VAL-10 | Plan–code–paper consistency | Every number in `paper/` is read from `output/estimates/*.csv` via macros; no hand-typed results | DECIDED `[ASSIGNMENT: consistency]` |

**Acceptance counts that cannot be known yet** must be generated in the feasibility run, frozen to `config/acceptance_counts.yaml`, and checked on every run. They must **not** be guessed. They are:
- PURCH records per year;
- number of CZs in the main sample;
- number of CZ × age × year cells with $N^{app}=0$;
- QWI CZ count;
- exposure mean and SD.

## J. Feasibility checks to run before freezing (priority order)

| ID | Check | Resolves |
|---|---|---|
| F1 | HEAD all 8 HMDA snapshot URLs. Download one year (2025). Confirm all 8 headers are identical, or record differences. Confirm column names from REQ-HMDA-01 exist. | REQ-DATA-01, REQ-HMDA-01 |
| F2 | On 2025: the filter funnel and the share of `1111`/Exempt in the reverse, open-end and business fields; `loan_to_value_ratio` = CLTV semantics (compare with FIG field "Combined Loan-to-Value Ratio") | DEC-H14, DEC-H31 |
| F3 | Open the Dorn `.dta` files: variable names, PUMA key format, list of HMDA 2018–2025 county codes not matched | REQ-GEO-03, REQ-EXP-04 |
| F4 | Distribution of $N^{app}$ per CZ × age × year (2025), especially `<25`; share of zeros | `05` §6 |
| F5 | PUMS 2015–2019: `SOCP` non-missing rates by survey year (`SERIALNO` prefix) for 2015–2017 vs 2018–2019; `SOCP` codes containing `X`; `NAICSP` strings for tech industries | REQ-EXP-02, REQ-CTRL-03 |
| F6 | Memory/time of the application-level LPM with LEI × year FE on 2025 alone; extrapolate | REQ-HMDA-06, REQ-EST-06 |
| F7 | Census API call for B25077/B19013 at county level without a key; FHFA HPI column layout | REQ-CTRL-01, REQ-EST-07 |
| F8 | Nationwide Data Browser aggregation call (no `states` parameter) returns totals | REQ-VAL-01 |

## K. Outputs

| REQ | Artifact |
|---|---|
| REQ-OUT-01 | Table 1: summary statistics by age bin and exposure tercile (2018–2019 vs 2023–2025) |
| REQ-OUT-02 | Table 2: QWI first stage (pooled; Emp, HirA, EarnS; A04 and A03) |
| REQ-OUT-03 | Table 3: main D-B estimates (no controls; X1–X2 main; X1–X5 horse race); `<25` and placebo ages |
| REQ-OUT-04 | Table 4: composition (F-COMP) with q-values |
| REQ-OUT-05 | Table 5: conditional outcomes (F-COND: F1/F2/F3 denial, reasons, rate spread) with q-values |
| REQ-OUT-06 | Table 6: robustness (REQ-ROB-01…17) |
| REQ-OUT-07 | Figure 1: map of $z_c$ |
| REQ-OUT-08 | Figure 2: QWI quarterly event studies |
| REQ-OUT-09 | Figure 3: HMDA event studies (25–34 and <25 vs 35–44), with HonestDiD bands |
| REQ-OUT-10 | Figure 4: level effects by age (D-A) |
| REQ-OUT-11 | Figure 5: HPI event study (price channel) |
| REQ-OUT-12 | `output/validation/report.md` (all REQ-VAL results) |

## L. Reproducibility

- **REQ-REPRO-01 (DECIDED).** `make all` runs, in order: download → build → validate → analysis → paper (`latexmk -pdf`). Each stage is idempotent and skips completed steps when the inputs' hashes are unchanged.
- **REQ-REPRO-02 (PROVISIONAL).** Language: Python 3.11 with `duckdb`, `pyarrow`, `polars` or `pandas`, `pyfixest`, `openpyxl`, `pyreadstat` (for Dorn `.dta`), `matplotlib`; all pinned in `env/requirements.lock`. If `pyfixest` lacks a needed feature (e.g. HonestDiD), R ≥ 4.3 with `fixest` and `HonestDiD` may be invoked from `make`, with an `renv.lock`.
- **REQ-REPRO-03 (DECIDED).** Cold-start test: on a fresh clone with an empty `data/`, `make all` must finish without manual steps and reproduce `output/estimates/*.csv` byte-identically, apart from timestamps.
- **REQ-REPRO-04 (DECIDED).** No Census API key is required. If F7 shows a key is needed, read it from the environment variable `CENSUS_API_KEY` and fall back to PUMS-based X1.
- **REQ-REPRO-05 (DECIDED).** Disk peak ≤ 40 GB: delete unzipped CSVs after Parquet conversion. RAM ≤ 14 GB.

## M. Decision register

| ID | Decision | Status | Basis | Source |
|---|---|---|---|---|
| DEC-Q01 | Narrowed research question (I.1) | DECIDED | Adapted | `06` §6.4 |
| DEC-D01 | Primary design = age DDD (D-B) with event study (D-C) | DECIDED | Adapted | `05` §10; P024, P005, M04 |
| DEC-D02 | Fallback design = D-D (industry exposure) with share-form linear DDD | DECIDED | Adapted | P005; M05–M07 |
| DEC-D03 | IV design | REJECTED | Exclusion contradicted | P035, P036, P038 |
| DEC-D04 | RD / sharp-date designs; individual-level designs | REJECTED | No cutoff; no occupation in HMDA | `05` §10 |
| DEC-G01 | 1990 CZ via Dorn crosswalks | DECIDED | Established | P024; M19, M20 |
| DEC-G02 | Exclude CT, AK, HI, PR; MI excluded from QWI only | DECIDED | New (data breaks) | `03` §1.3; `04` D04 |
| DEC-A01 | Young = 25–34; comparison = 35–44 | DECIDED | Adapted | P004 Table 1; `05` §3 |
| DEC-A02 | Auxiliary young = <25; placebo = 45–54 vs 35–44 | DECIDED | New | `05` §3 |
| DEC-X01 | Exposure = Eloundou GPT-4 β, 22–34 employed residents, ACS 2015–2019, CZ | DECIDED (measure); PROVISIONAL (F5) | Adapted | P001, P004, P005 |
| DEC-X02 | 8→6-digit SOC by simple mean | PROVISIONAL | Adapted | P004 §1.2 (rule unstated) |
| DEC-X03 | Anthropic usage index only as post-treatment heterogeneity | DECIDED | New | P003, P004 |
| DEC-H01…H53 | HMDA processing | See `03` §4 | — | `03` |
| DEC-E01 | PPML for counts | DECIDED | Established | M08–M12 |
| DEC-E02 | Main controls {X1, X2} × Y × year; X3–X5 in horse race only | DECIDED | New | `05` §4.3 |
| DEC-E03 | State-clustered SEs | DECIDED | Adapted | M14, M15 |
| DEC-E04 | Anderson q-values within families | DECIDED | Established | M17 |
| DEC-E05 | Post = 2023–2025; reference year 2022 | DECIDED | Adapted | P004, P005 |
| DEC-E06 | QWI reference quarters 2022Q4 (stocks) / 2022Q3 (flows) | DECIDED | Established | P005 |
| DEC-E07 | Snapshot vintage for all HMDA years | DECIDED | Adapted | P031 |
| DEC-E08 | Application-level module capped or sampled | PROVISIONAL | New | F6 |

## N. Unresolved matters (OPEN)

1. **O-01.** Dorn crosswalk key formats and post-1990 county coverage (F3).
2. **O-02.** Whether PUMS 2015–2017 records carry 2018-scheme `SOCP` (F5). If not, switch to PUMS 2018–2022 using `PUMA10`-only years (2018–2021), or to D-D.
3. **O-03.** `loan_to_value_ratio` = CLTV confirmation (F2).
4. **O-04.** Lender-type classification (bank vs non-bank) from TS agency code: schema not inspected.
5. **O-05.** AKM implementation effort; Conley SEs need CZ centroids.
6. **O-06.** Regulation C post-2018 coverage rules for rural lenders (location test): affects only levels, but should be stated precisely in the paper.
7. **O-07.** Whether QWI or PEP recent vintages also switched CT to planning regions (irrelevant if CT is excluded).
8. **O-08.** ACS 1-year 2025 PUMS release status (only matters for the optional residence-based first stage).

## O. Fallback design and triggers

**Fallback (DEC-D02):**
- Exposure = $z^{IND}_c$ (REQ-EXP-06).
- Estimator = share-form linear DDD: $s_{ct}=N_{c,25\text{–}34,t}/(N_{c,25\text{–}34,t}+N_{c,35\text{–}44,t})$ regressed on $z^{IND}_c\times$year indicators, X1–X2 × year, CZ FE and year FE, weighted by $N_{c,25\text{–}34,t}+N_{c,35\text{–}44,t}$.
- SEs clustered by state, plus AKM over industries.
- QWI first stage as in REQ-EST-05, with $z^{IND}_c$.

**Triggers.** Switch to the fallback only if:
- (T1) REQ-VAL-04 or REQ-VAL-05 fails and cannot be fixed within 1 day; or
- (T2) the PPML in REQ-EST-01 fails to converge with the documented settings.

Results-based switching (for example, because the main estimate is insignificant) is **prohibited**. If the D-C pre-trends fail, the design is *not* switched. Instead, HonestDiD bounds are reported and the paper's claims are downgraded to descriptive.

## P. One-week schedule (indicative)

| Day | Work |
|---|---|
| 1 | F1–F8; all downloads with manifest |
| 2 | HMDA build + REQ-VAL-01…03; filter funnel |
| 3 | Exposure (PUMS) + QWI build + REQ-VAL-04…07 |
| 4 | REQ-EST-01…05, 07, 08; figures 1–4 |
| 5 | REQ-EST-06 (capped), REQ-EST-09, robustness REQ-ROB |
| 6 | Paper drafting (AER LaTeX), with every number via macros |
| 7 | Cold-start replication (REQ-REPRO-03); plan–code–paper consistency check; AI log export |

---

## Q. Quality-control self-audit (performed 2026-10-08)

| # | Check | Result |
|---|---|---|
| 1 | Does every cited paper exist? | **Yes, for all P/M IDs.** Each was resolved via Crossref DOI or arXiv/official URL, except P005 (slide deck at the author's site) and P007 (Dallas Fed web article); both were fetched directly. One cited article, **P033 Ouazad & Kahn (2022)**, is **flagged RETRACTED** in Crossref metadata and is excluded from evidence. |
| 2 | Are titles, authors, years, DOIs and status accurate? | Checked against Crossref/OpenAlex. Corrections made during the audit: many DOIs initially recalled from memory were wrong and were replaced. Ringo (P022) is now published (REStat 2026). Bhutta–Hizmo–Ringo (P028) is published (JF 2025). NBER WP 33777 (P010) appears in Crossref under the title "Still Waters, Rapid Currents"; the circulated title is "Large Language Models, Small Labor Market Effects". |
| 3 | Are findings supported by the cited sources? | Quantitative claims come from full text (P004, P005, P007, P009, P022–P025, P027–P031) or verbatim abstracts. Abstract-only claims are labelled. P013–P015, P040 and P041 are cited only by title-level topic (no abstract available). |
| 4 | Are HMDA practices traced to papers or documentation? | Yes (`03` §2 with page and table locations; FIG and probes for data facts). |
| 5 | Are recommendations separated from published methods? | Yes: `[REC]`, `[ADAPTED]`, `[NEW]` and `[ESTABLISHED]` tags; decision register "Basis" column. |
| 6 | Is the identification strategy defensible? | Partially. The DDD is defensible against age-invariant local shocks, but **not** against age-specific incidence of rate and price shocks correlated with exposure (`05` §4). The plan states this and relies on controls, timing and gradient tests, and bounds. |
| 7 | Is the labor mechanism measurable? | Only at place × age × industry level (QWI). There is no local occupation × age data post-2022, and no individual linkage. |
| 8 | Are loan demand and conditional credit supply distinguished? | Yes (`06` §3). Counts are primary; conditional denial is labelled "conditional on public observables"; credit supply is not claimed. |
| 9 | Are pre-trends, selection and age measurement addressed? | Yes (`05` §2 D-C, §3; `06` §3). |
| 10 | Are all datasets obtainable by code? | Yes. All URLs returned HTTP 200 (`04`). BLS needs a User-Agent header. The Census API was not tested (F7; a PUMS fallback exists). |
| 11 | Is the project feasible in one week? | Yes for the primary design and first stage. The application-level module is at risk (F6) and capped. |
| 12 | Are outputs understandable without this conversation? | Designed so: stable IDs, explicit URLs, formulas, statuses. |
| 13 | Are unresolved assumptions documented? | Yes (§N, §J, `PROVISIONAL` tags). |
| 14 | Was any result fabricated? | No estimates were run. All numeric values in this package are either quoted from sources (with location) or observed in official-API probes (with the query). |

---

## Critical Weaknesses and Unresolved Questions

These are the five most serious issues a skeptical referee would raise, in order of severity.

**1. The labor "first stage" may be weak, contested, or absent at the local level.**
- The entry-level employment decline is large in ADP data: −0.179 for ages 22–25, Q5 vs Q1 (P004 Table 1).
- But it attenuates to −0.080 (SE 0.057) with education, rate and WFH controls (Panel F).
- It is small and insignificant in the ACS (−0.022 [−0.055, 0.011]; P004 §5), began before ChatGPT (P008), and coincides with monetary tightening (P009).
- At the CZ level and for HMDA's 25–34 bin, where P004 finds only −0.048 (26–30) and −0.014 (31–34), the shock may be too diluted to transmit detectably.

A null mortgage result would then be uninformative about transmission. A non-null result without a first stage could not be attributed to labor.

**2. The DDD does not remove the most plausible confounders.**
CZ × year FE absorb only age-invariant local shocks. The 2022–23 rate shock (P022, P023), AI-linked house-price growth (P035, P036), the student-loan restart and the FHA premium cut all have *age-specific* incidence. Their local intensity is plausibly correlated with exposure. Controls and timing tests mitigate this but cannot exclude it (`05` §4).

**3. Labor channels cannot be separated from price and wealth channels, and expectations cannot be measured.**
GenAI exposure raised local prices in two independent studies. That alone could reduce young first-time-buyer demand, so an exclusion restriction tying mortgage effects to labor outcomes is not credible (D-E rejected). M2 (expectations/risk) is observationally equivalent to A1/A2 in HMDA.

**4. HMDA measurement limits.**
- No occupation, employment status or credit score.
- Binned age referring to the primary applicant only.
- Applications rather than applicants (no deduplication).
- Property-location geography (migration).
- Partial exemptions; the 2020–2022 coverage-threshold episode.
- A 2024 geography break (CT).

Denial and pricing outcomes conflate selection with lender behaviour (P028).

**5. Exposure measurement and inference.**
- Eloundou β measures task *capability*, not adoption, and depends on GPT-4 ratings.
- PUMS-based, PUMA-allocated CZ exposure is a noisy generated regressor, so attenuation is likely.
- Exposure correlates with education, income, teleworkability and rate-sensitive industries, so it is a bundle of place characteristics.
- With continuous treatment, TWFE coefficients require *strong* parallel trends for causal-response interpretation (M01).
- Inference must account for spatial and shift-share correlation (M07).

The coefficient is therefore an exposure association whose causal interpretation rests on assumptions that cannot be fully tested.

**Unresolved questions that would most change the design**
- (i) Does the QWI first stage exist at CZ level for A04 (25–34), or only for A03 (22–24)?
- (ii) Do pre-trends hold through 2021, including the 2020–21 rate decline?
- (iii) Is the PUMS 2015–2019 occupation coding harmonized (F5)?
- (iv) Do high-exposure CZs show the price increases reported by P035/P036 in FHFA data?
