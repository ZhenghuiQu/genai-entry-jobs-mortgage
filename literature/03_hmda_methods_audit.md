---
project: genai-entry-jobs-mortgage
document: hmda_methods_audit
model: claude-opus-5-5 (Claude Opus 5.5, Claude Code desktop)
date: 2026-10-08
status: independent_review
research_cutoff: 2026-10-08
---

# 03 — HMDA Empirical Practices Audit

## 0. Scope and conventions

This document has three parts.

1. **What HMDA is.** Facts about the public HMDA Loan/Application Register (LAR) that matter for this project, checked against official documentation and against live queries to the official API run on 2026-10-08.
2. **What published papers do with HMDA.** Processing conventions reconstructed from the papers themselves.
3. **What we recommend.** Our processing decisions for this project, each tagged with its provenance.

It does not repeat the economic motivation (see `06_mechanisms_and_contribution.md`) or the full regression specifications (see `05_identification_designs.md` and `07_recommended_research_plan.md`).

**Provenance tags used in this file**

| Tag | Meaning |
|---|---|
| `[DOC]` | Verified against official HMDA documentation: the FFIEC/CFPB Filing Instructions Guide (FIG) 2024, the public LAR data-field page, or the CFPB report P031. |
| `[PROBE]` | Verified by a live query to the official FFIEC HMDA endpoints on 2026-10-08. The exact query is reported. |
| `[Pxxx, loc]` | Practice documented in paper Pxxx at the stated page, table, or section. Page numbers refer to the working-paper version we read (see `02_evidence_matrix.md`). |
| `[INFERENCE]` | Our interpretation. Not stated in a source. |
| `[REC]` | Our recommendation for this project. |
| `[OPEN]` | Not yet verified. Must be checked in a feasibility run. |

Paper IDs (P0xx) are defined in `02_evidence_matrix.md`.

---

## 1. Verified facts about the public HMDA LAR (2018–2025)

### 1.1 Availability, vintages and download routes

| Item | Fact | Provenance |
|---|---|---|
| Years with the post-2018 schema (incl. applicant age) | 2018–2025 (activity years). The 2017 file uses the old schema. | `[DOC]` LAR data-field page lists `activity_year` 2017–2025 |
| Snapshot national files | `https://files.ffiec.cfpb.gov/static-data/snapshot/{YYYY}/{YYYY}_public_lar_csv.zip` exists for 2017–2025. Verified sizes (zipped): 2018 = 823,719,647 B; 2024 = 664,242,987 B; 2025 = 737,139,477 B. | `[PROBE]` HTTP HEAD, 2026-10-08 |
| Snapshot freeze dates | 2025: June 2, 2026. 2024: May 19, 2025. 2023: May 1, 2024. 2022: May 1, 2023. 2021: April 30, 2022. 2020: May 3, 2021. 2019: April 27, 2020. 2018: August 7, 2019. | `[PROBE]` FFIEC site JS bundle (`index-DuXocMOj.js`). The CFPB report P031 (p. 4) confirms that the 2023 snapshot is "as of May 1, 2024". |
| One-year files | `…/static-data/one-year/{YYYY}/{YYYY}_public_lar_one_year_csv.zip` for 2019–2024. The 2024 one-year freeze date is June 2, 2026. | `[PROBE]` |
| Three-year files | `…/static-data/three-year/{YYYY}/{YYYY}_public_lar_three_year_csv.zip` for 2017–2022. The 2022 three-year freeze date is December 31, 2025. | `[PROBE]` |
| Other snapshot files | Transmittal sheet `{YYYY}_public_ts_csv.zip` and MSA/MD file `{YYYY}_public_msamd_csv.zip`. A lender "panel" file was **not** found among the snapshot files. | `[PROBE]` |
| Data Browser API | `https://ffiec.cfpb.gov/v2/data-browser-api/view/{aggregations,csv,filers}`. It serves the **snapshot** vintage: the CSV endpoint 301-redirects to `files.ffiec.cfpb.gov/data-browser/datasets/2025/filtered-queries/snapshot/…`. | `[PROBE]` |
| Data Browser age filter | **Not supported.** The parameter `ages=<25` is ignored. It is not echoed in the `parameters` block, and the cached file name omits it. Age-specific tabulations therefore require loan-level files. | `[PROBE]` aggregations and csv endpoints, Kent County DE, 2025 |
| Authentication | None, for both bulk files and the API. | `[PROBE]` |

### 1.2 Fields used in this project (public LAR CSV column names)

The verified CSV header (2025) includes: `activity_year, lei, derived_msa-md, state_code, county_code, census_tract, conforming_loan_limit, derived_loan_product_type, derived_dwelling_category, action_taken, purchaser_type, preapproval, loan_type, loan_purpose, lien_status, reverse_mortgage, open-end_line_of_credit, business_or_commercial_purpose, loan_amount, loan_to_value_ratio, interest_rate, rate_spread, hoepa_status, total_loan_costs, …, loan_term, …, intro_rate_period, …, property_value, construction_method, occupancy_type, …, total_units, …, income, debt_to_income_ratio, applicant_credit_score_type, …, applicant_age, co-applicant_age, applicant_age_above_62, …, aus-1…aus-5, denial_reason-1…denial_reason-4, tract_population, tract_minority_population_percent, ffiec_msa_md_median_family_income, tract_to_msa_income_percentage, tract_owner_occupied_units, tract_one_to_four_family_homes, tract_median_age_of_housing_units` `[PROBE]`.

| Field | Values / units | Provenance |
|---|---|---|
| `action_taken` | 1 originated; 2 approved, not accepted; 3 denied; 4 withdrawn by applicant; 5 file closed for incompleteness; 6 purchased loan; 7 preapproval request denied; 8 preapproval request approved but not accepted | `[DOC]` FIG 2024, field 11 |
| `loan_purpose` | 1 home purchase; 2 home improvement; 31 refinance; 32 cash-out refinance; 4 other; 5 not applicable | `[DOC]` |
| `lien_status` | 1 first lien; 2 subordinate | `[DOC]` |
| `occupancy_type` | 1 principal residence; 2 second residence; 3 investment | `[DOC]` (code meanings per FIG; data-field page lists 1, 2, 3) |
| `loan_type` | 1 conventional; 2 FHA; 3 VA; 4 USDA RHS/FSA | `[DOC]` (`derived_loan_product_type` lists Conventional, FHA, VA, FSA/RHS) |
| `derived_dwelling_category` | "Single Family (1-4 Units):Site-Built", "Single Family (1-4 Units):Manufactured", "Multifamily:Site-Built (5+ Units)", "Multifamily:Manufactured (5+ Units)" | `[DOC]` |
| `reverse_mortgage`, `open-end_line_of_credit`, `business_or_commercial_purpose` | 1 yes; 2 no; 1111 Exempt | `[DOC]` |
| `applicant_age` | Public file **binned**: `<25`, `25-34`, `35-44`, `45-54`, `55-64`, `65-74`, `>74`, `8888` (not applicable). Filers report exact age in years. 8888 applies e.g. to non-natural persons. | `[DOC]` FIG 2024, field 55 (p. 36); data-field page (privacy binning) |
| `co-applicant_age` | Same bins plus `9999` = no co-applicant | `[DOC]` FIG field 56 |
| `income` | Gross annual income relied on, in **thousands of dollars**, rounded to the nearest thousand. May be negative. `NA` if not applicable. | `[DOC]` FIG field 57; edit V654 |
| `debt_to_income_ratio` | Public bins: `<20%`, `20%-<30%`, `30%-<36%`, then single values `36`…`49`, then `50%-60%`, `>60%`, `NA`, `Exempt` | `[DOC]` data-field page |
| `loan_amount` | Dollars. The public file reports the midpoint of a $10,000 interval (e.g. `105000.0`). | `[PROBE]` values seen; `[INFERENCE]` midpoint convention from the observed values (the data-field page does not state the rounding; see §1.5) |
| `property_value` | Midpoint of the nearest $10,000 interval | `[DOC]` |
| `loan_to_value_ratio` (CSV) | The data-field page names this field `combined_loan_to_value_ratio` (CLTV). The CSV column is `loan_to_value_ratio`. | `[DOC]`/`[PROBE]` — the name mismatch is noted; treat as CLTV `[OPEN: confirm with FIG]` |
| `rate_spread` | APR minus APOR, in percentage points; `NA` or `Exempt` possible | `[DOC]` FIG field 59 |
| `denial_reason-1` | 1 DTI; 2 employment history; 3 credit history; 4 collateral; 5 insufficient cash (down payment/closing costs); 6 unverifiable information; 7 credit application incomplete; 8 mortgage insurance denied; 9 other; 10 not applicable | `[DOC]` |
| `ffiec_msa_md_median_family_income` | Dollars; appended by the Census Bureau | `[DOC]` |
| Credit score, application date, action date, AUS result | **Not in the public file.** Only the credit-score *model type* and AUS *system name* are public. | `[PROBE]` header inspection |

### 1.3 Reporting-regime changes inside 2018–2025

| Change | Date / years affected | Consequence for a 2018–2025 panel | Provenance |
|---|---|---|---|
| Expanded HMDA data (age, DTI, CLTV, rate spread for all covered loans, denial reasons mandatory, etc.) | Effective for 2018 data | 2018 is the first usable year for age-based analysis | `[DOC]`; P028 p. 10, 21 ("Lenders are now required … to report a denial reason for every denied application") |
| Partial exemptions under EGRRCPA (2018) | Ongoing since 2018 | Insured depositories and credit unions with fewer than 500 closed-end originations in each of the two preceding years may report `Exempt` for many fields (incl. DTI, rate spread, CLTV) | `[DOC]` (FIG `1111`/`Exempt` codes); P028 Table A.2 drops non-full reporters |
| Closed-end coverage threshold raised from 25 to 100 loans | Effective July 1, 2020 | Lenders with 25–99 closed-end loans stopped reporting | P031 p. 7 fn. 7 |
| Threshold increase vacated (D.D.C.) | Sept 23, 2022. Enforcement relief for 2020–2022 data. | "2023 is the first year since 2019 that institutions originating less than 100 closed-end mortgage loans reported closed-end data." The number of reporters rose 14.6% from 2022 to 2023. | P031 p. 7 and fn. 7 |
| Connecticut county codes → planning regions | HMDA 2024 onward (our tabulation) | CT 2024 home-purchase originations carry `county_code` 09110–09190 and `NA`. Fairfield County `09001` has 23,122 originations in 2022, 14,326 in 2023 and 0 in 2024–2025. | `[PROBE]` CSV `states=CT`, 2024; aggregations `counties=09001` |
| 2026 rulemaking | EO 14393 (March 13, 2026) directs the CFPB to *consider* changes. The asset threshold was adjusted to $59M (January 7, 2026). No change to 2025 data fields was found. | No effect on the 2018–2025 data | Web search, secondary sources (`UNVERIFIED` beyond the Federal Register asset-threshold notice) |

### 1.4 Probe tabulations (real values, usable as pipeline unit tests)

All values below come from the official Data Browser (snapshot vintage), queried 2026-10-08.

**Delaware, home purchase (`loan_purposes=1`), no other filters**

| Year | Originated (`action_taken=1`) | Denied (`action_taken=3`) |
|---|---|---|
| 2018 | 15,503 | 2,592 |
| 2022 | 17,271 | 2,785 |
| 2023 | 13,344 | 2,431 |
| 2024 | 13,681 | 2,216 |
| 2025 | 14,078 | 2,145 |

**Kent County, DE (`counties=10001`), 2025, `loan_purposes=1`, `actions_taken=1,2,3,4,5`, no other filters.** N = 3,862 records.

- `action_taken`: 1 = 2,490; 2 = 98; 3 = 539; 4 = 524; 5 = 211.
- `applicant_age`: `<25` = 263; `25-34` = 941; `35-44` = 861; `45-54` = 582; `55-64` = 632; `65-74` = 406; `>74` = 119; `8888` = 58.
- `income`: positive = 3,742; NA = 90; ≤0 = 30.
- `rate_spread` among originations: numeric = 2,319; NA/Exempt = 171.
- `debt_to_income_ratio` = NA for 837 records (all actions pooled).

These numbers show the cell-size problem directly. In one mid-sized county, under-25 applicants are about 6.8% of purchase applications (263/3,862). `[INFERENCE]` In small rural counties, `<25` cells will often contain single digits. This is why we recommend CZ aggregation (§4.4).

### 1.5 Known limitations of public HMDA relevant here

1. **No applicant identifier.** Repeat applications by the same household to several lenders cannot be deduplicated in the public file. Counts measure *applications*, not *applicants*. None of the audited papers deduplicates public HMDA. `[INFERENCE]` from the absence of such a step in P022–P031.
2. **No occupation or employment status.** HMDA cannot identify AI-displaced workers or workers in exposed occupations. The only employment signal is denial reason 2, "employment history".
3. **No credit score values.** P028 shows that conditional denial gaps shrink sharply once credit score and AUS results are observed (abstract; Table 2, p. 26). Public-data "conditional" denial regressions therefore omit key risk variables.
4. **Age is binned**, and refers to the primary applicant. A co-applicant's age is binned separately.
5. **Geography is property location**, i.e. the post-purchase residence, not the applicant's workplace or prior residence.
6. **Coverage.** P030 (p. 13) and P027 (p. 33) note that small or rural lenders were under-covered in pre-2018 data. P027 shows robustness to restricting to MSAs. `[OPEN]` Post-2018 rules retain a location/volume test for coverage, so rural coverage remains incomplete. This should be checked against Regulation C §1003.2(g).
7. **Rounding.** Loan amount and property value are reported as interval midpoints. Income is rounded to $1,000.

---

## 2. Paper-level reconstruction of HMDA practices

The rows below report only what we could verify in the source. "n.v." means not verified: the item was not found or not extracted. It does **not** mean "not done".

### 2.1 Summary table

| ID | Years / vintage | Population restrictions (verified) | Action codes | Outcomes built from HMDA | Unit & linkage | Model, FE, SE | Location |
|---|---|---|---|---|---|---|---|
| P025 Mian & Sufi (2009) | Public HMDA 1996–2006 (pre-2018 schema) | Home-purchase vs refinance distinguished | All applications for denial rate; originations for credit growth | ZIP-level 1996 denial rate (latent-demand / subprime proxy); home-purchase origination growth; originated mortgage debt / income | ZIP; linked to Equifax and IRS income; within-county design | Within-county (county FE) regressions; SE n.v. | NBER w13936: pp. 10, 13–14, 20, 23; Table p. 47 |
| P027 Fuster et al. (2019) | HMDA 2010–2016, incl. restricted version with application and action dates | Separate samples: originated purchase loans; originated refinances; all applications incl. denied and withdrawn | 1 (originations); all (applications); processing time from restricted dates | Processing time (days); FinTech share; LPM outcomes | Loan level; tract- and county-level covariates; robustness to MSA-only sample | LPM with lender FE, census-tract FE, calendar-month FE; SE clustered by tract (loan level), county (county regressions), White–Huber (lender-month) | w24500: pp. 12 fn. 15, 33, 45, 53, 56–61 |
| P028 Bhutta, Hizmo & Ringo (2025) | **Confidential** HMDA 2018–2019 | First-lien; purchase + refinance; owner-occupied; site-built single-unit; lenders subject to *full* reporting (drops partially exempt); 30-year FRM; FICO 300–850; AUS subsample | **1, 2, 3 only** (withdrawn and incomplete excluded) | Denial indicator; denial reasons; FICO/LTV/DTI bins | Loan level; Ginnie Mae performance linkage for a subsample | LPM; SE clustered by lender and county | FEDS 2022-067: pp. 10, 21, 25–27, 35; Table A.2 p. 37 |
| P022 Ringo (2026) | HMDA (confidential, with application/origination dates) merged to Optimal Blue rate locks; through 2019 | "First-lien, home-purchase loans for owner-occupied properties with a reported borrower income between zero and $1 million" | Originations | LMI share of home buyers; first-time-buyer heterogeneity | Loan level; 212 monetary-policy shocks; >90M purchase loans | High-frequency event design; SE n.v. | FEDS 2023-006: p. 13; Table notes p. 31 |
| P023 Bhutta & Ringo (2021) | Confidential HMDA (application dates) merged to Optimal Blue and McDash; 2014–2015 | Owner-occupied home-purchase loans; FHA vs non-FHA | Originations (counts by week); denials (application level) | Weekly counts of purchase originations; denial indicator; DTI denial reason share (31% of denied FHA purchase applications with a reason in 2014) | Application level; area FHA share (2014) × Post for house prices | RD in application week; application-level denial regression with Black × Post | FEDS 2017-086: pp. 13–14, 22–24, 28 |
| P024 Barrot et al. (2022) | HMDA 2000–2007 (pre-2018) | Home purchase vs refinancing | Applications; originations; denials | Δ log applications, Δ log originations, denial rate (count- and value-weighted) | **Commuting zone** (733 CZs); 1998 controls; Census controls | Cross-sectional long-difference OLS; population weights; SE n.v. | FRBNY SR 821: Table A.4 p. 54; tables pp. 46, 53 |
| P029 Buchak et al. (2018) | HMDA 2010–2015 | Robustness: top-50 lenders | Originations | Lender-type market shares | Loan / county-time | County × time FE; SE clustered at county-year | NBER w23288: pp. 16, 38, 46 |
| P030 Gilje et al. (2016) | HMDA (shale-boom era) | n.v. | Originations; application volume growth | % change in originations by bank-county-year; approval rate | Bank-county-year; Call Reports | County × year FE; SE clustered by bank | NBER w19403: pp. 13–14, 27, 36–41 |
| P031 CFPB (2024) | 2023 snapshot (as of May 1, 2024) plus 2018–2022 | Closed-end excl. reverse; site-built 1–4 family; first lien; principal residence; purchase or refinance | All records (tables 1A–1E); applications and originations | Shares by income and race; denial rates; medians of characteristics; LMI = income < 80% AMFI, zero/negative income counted as LMI | National | Descriptive | pp. 4, 7–8, 18–20 |
| P033 Ouazad & Kahn (2022) — **RETRACTED** | HMDA (pre-2018) | Conventional; 1–4 family excl. manufactured; owner-occupied; home purchase | Originations and purchases | Securitization | ZIP / tract | SE double-clustered by ZIP and year | NBER w26322: pp. 11–12, 23. **Do not use as evidence**; Crossref metadata flags the RFS article as retracted. |
| P034 Chu et al. (2026) | HMDA 2022–2024 (abstract) | n.v. | n.v. | Denial-rate and interest-rate gaps by race | Lender AI adoption from job postings; IV using AI-graduate supply | n.v. | SSRN 6342658 (abstract only) |
| P026 Avery, Brevoort & Canner (2007) | Methodological review of HMDA issues | — | — | — | — | — | JRER 29(4): 351–380 (abstract only) |

### 2.2 Cross-paper regularities (established practice)

The following conventions recur across the verified papers.

1. **Population = first-lien, owner-occupied (principal-residence), home-purchase loans** whenever the question concerns housing demand or credit access: P022 (Table notes p. 31), P023 (p. 13), P028 (p. 10), P031 (pp. 7–8), and P033 (p. 12; retracted, practice only). Refinances are analysed separately or excluded.
2. **Site-built 1–4 family.** P031 and P028 exclude manufactured housing and multifamily. P033 excludes manufactured housing.
3. **Denial analyses use completed decisions only.** P028 keeps actions 1, 2, 3 and drops withdrawn and incomplete files. P027 uses "all applications (including denied and withdrawn)" for application-volume outcomes. So the *denominator differs by outcome*, and good practice states it explicitly.
4. **Income trimming.** P022 restricts to 0 < income ≤ $1M. P031 keeps zero/negative income inside the LMI group for descriptive shares.
5. **Partial-exemption handling.** P028 drops lenders not subject to full reporting when analysing fields that can be `Exempt`.
6. **Area-level outcomes.** P024 builds CZ-level changes in log applications, log originations, and denial rates from HMDA. P025 builds ZIP-level denial rates and origination growth. Both treat HMDA area aggregates as measures of local mortgage *demand and credit flows*.
7. **Fixed effects.** Within-market designs use location × time FE: county × time in P029 and P030, tract and month FE in P027. Lender FE appear when lender behaviour is the object (P027). P028 clusters standard errors by lender and county (two-way).
8. **Interpreting denial rates.** P024 interprets *higher* denial rates in import-exposed CZs as "consistent with the idea that demand for such loans increases more in these areas" (p. 19). So a denial-rate change is **not** read mechanically as a credit-supply change. P023 compares denial rates across groups and notes that "HMDA is our only source for data on denied loan applications", which lacks FICO/LTV (p. 23).

### 2.3 What the audited literature does **not** provide

- No audited paper uses **public HMDA applicant age** as a main dimension of analysis. Age-based HMDA work found in the search is limited to policy briefs (e.g. a Boston College CRR brief on older refinance applicants; a Richmond Fed regional analysis). Those were not audited in detail and are marked `UNVERIFIED` in `02_evidence_matrix.md`. `[INFERENCE]` There is no established academic template for an age × geography × year HMDA panel. Our design adapts the area-level conventions of P024 and P025 and the population conventions of P022, P028 and P031.
- No audited paper links HMDA to **QWI**. P024 links HMDA to CZ-level labor-market exposure (trade), which is the closest analogue.
- No paper handles the **2024 Connecticut geography break**. It post-dates most papers.

---

## 3. Suitability of econometric practices for this question

| Practice | Used in | Why authors used it | Suitability here `[REC]` |
|---|---|---|---|
| Application-level LPM for denial | P027, P028, P023 | Large N, many FE, easy interpretation; logit has incidental-parameter issues with many FE | **Suitable** for mechanism module D-F (conditional denial), with explicit caveats: public data lack credit scores (P028), and selection into application is endogenous. |
| Area-level long differences | P024 (CZ), P025 (ZIP) | Exposure is cross-sectional; simple, transparent | **Suitable as fallback / robustness** (design D-G). |
| Location × time FE | P029, P030 | Absorb local demand shocks when the treatment varies within location (bank, lender type) | Our treatment varies across locations, so location × time FE can enter **only** via the age dimension (DDD). See `05_identification_designs.md` §4 for what this does and does not absorb. |
| Lender FE / lender × time FE | P027 | Absorb lender pricing and underwriting policies | **Suitable** in D-F to separate lender composition from within-lender behaviour. |
| Two-way clustering (lender, county) | P028 | Correlated decisions within lender and within county | Adapt: our exposure is at CZ level, so cluster at state level (main) with CZ-level and shift-share (AKM) robustness; see `05` §6. |
| Poisson / PPML for counts | not found in audited HMDA papers | — | **New to this HMDA setting** but established for counts with FE (M08, M09, M10; Canaries P004 App. C.6 uses Poisson for employment because of zero counts, citing M09). |
| Regression discontinuity in time | P023 | Sharp policy date | Not applicable. GenAI diffusion has no sharp, exogenous, borrower-specific cutoff. |

---

## 4. Recommended HMDA processing decisions for this project

Decision IDs (DEC-H##) are re-used in `07_recommended_research_plan.md`. Status labels: `DECIDED`, `PROVISIONAL` (needs a feasibility check), `OPEN`, `REJECTED`. "Basis" says whether the choice is **Established** (directly follows a cited practice), **Adapted**, or **New**.

### 4.1 Vintage and years

| ID | Decision | Status | Basis |
|---|---|---|---|
| DEC-H01 | Use activity years **2018–2025**. | DECIDED | Established: the age field exists only from 2018 `[DOC]`; 2025 is the latest available `[PROBE]`. |
| DEC-H02 | Use the **snapshot** national LAR CSV for every year. It has a uniform "about one year after the activity year" freeze rule and is the vintage behind the Data Browser, which enables exact validation (REQ-VAL-01). | DECIDED | Adapted: P031 uses the snapshot. One-year and three-year files are more complete but not available for all years (three-year: 2017–2022 only; one-year: 2019–2024 only). Mixing vintages would create artificial year-to-year completeness differences. |
| DEC-H03 | Robustness: re-run the main count outcome using three-year files for 2018–2022 and one-year files for 2023–2024. | PROVISIONAL | New |

### 4.2 Sample definition (main population "PURCH")

Keep a record if **all** of the following hold.

| ID | Field rule | Status | Basis |
|---|---|---|---|
| DEC-H10 | `loan_purpose == 1` (home purchase) | DECIDED | Established (P022, P023, P031) |
| DEC-H11 | `lien_status == 1` (first lien) | DECIDED | Established (P022, P028, P031) |
| DEC-H12 | `occupancy_type == 1` (principal residence) | DECIDED | Established (P022, P028, P031) |
| DEC-H13 | `derived_dwelling_category == "Single Family (1-4 Units):Site-Built"` | DECIDED | Established (P028, P031) |
| DEC-H14 | `reverse_mortgage == 2` **and** `open-end_line_of_credit == 2` **and** `business_or_commercial_purpose == 2`. Records with `1111` (Exempt) in any of the three are dropped in the main sample and kept in robustness. | PROVISIONAL (share of 1111 to be reported, F2) | Adapted (P031 "closed-end excluding reverse") |
| DEC-H15 | `action_taken ∈ {1,2,3,4,5}` = **applications**. Exclude 6 (purchased loans; these are secondary-market acquisitions, and including them would double count) and 7–8 (preapproval requests not converted into applications). | DECIDED | Adapted (P027 "all applications"; P028 excludes 4, 5 for denial) |
| DEC-H16 | `applicant_age ∈ {<25, 25-34, 35-44, 45-54, 55-64, 65-74, >74}`; drop `8888` | DECIDED | New (age dimension) |
| DEC-H17 | `county_code` non-missing and a valid 5-digit FIPS; drop `NA` (share reported) | DECIDED | Adapted |
| DEC-H18 | Geography: 48 contiguous states + DC, **excluding Connecticut** (2024 code break; ≈1% of US records `[INFERENCE]`) and excluding AK, HI, PR | DECIDED (CT exclusion), PROVISIONAL (alternative tract-based CT harmonization) | New |
| DEC-H19 | No deduplication (impossible in the public file); interpret counts as applications | DECIDED | Established by necessity |

### 4.3 Outcome construction (cell level: CZ × age group × year)

Notation: $\mathcal{A}_{cat}$ = PURCH records in CZ $c$, age bin $a$, year $t$.

| ID | Outcome | Exact definition | Status |
|---|---|---|---|
| DEC-H20 | Applications | $N^{app}_{cat} = \lvert\{i\in\mathcal{A}_{cat}: \text{action}_i\in\{1,\dots,5\}\}\rvert$ | DECIDED (primary outcome) |
| DEC-H21 | Completed decisions | $N^{dec}_{cat}$: action ∈ {1,2,3} | DECIDED |
| DEC-H22 | Originations | $N^{orig}_{cat}$: action = 1 | DECIDED |
| DEC-H23 | Denial rate | $D_{cat} = N^{den}_{cat}/N^{dec}_{cat}$ with $N^{den}$: action = 3 (P028 denominator) | DECIDED |
| DEC-H24 | Withdrawal/incomplete share | $(N_{4}+N_{5})/N^{app}$ | DECIDED (secondary) |
| DEC-H25 | Applicant income | mean of $\ln(\text{income}_i)$ over records with $0<\text{income}_i\le 1000$ (i.e. ≤ $1M; P022 rule); records outside the range are excluded from this mean only | DECIDED |
| DEC-H26 | LMI share | share with $\text{income}_i\times 1000 < 0.8\times$`ffiec_msa_md_median_family_income`. Income ≤ 0 is counted as LMI (P031 convention); NA is excluded. | DECIDED |
| DEC-H27 | High-DTI share | among records with DTI not in {NA, Exempt}: share with DTI ∈ {`44`,…,`49`, `50%-60%`, `>60%`} (i.e. > 43%) | DECIDED |
| DEC-H28 | Very-high-DTI share | share with DTI ∈ {`50%-60%`, `>60%`} | DECIDED |
| DEC-H29 | Loan size | mean $\ln(\text{loan\_amount}_i)$; loan-to-income $= \text{loan\_amount}_i/(1000\cdot \text{income}_i)$ for income > 0, winsorized at the 1st/99th percentile of the pooled 2018–2025 distribution | PROVISIONAL (winsorization cut) |
| DEC-H30 | Product mix | FHA share (`loan_type == 2`); VA share (`== 3`) | DECIDED |
| DEC-H31 | High-CLTV share | share with numeric `loan_to_value_ratio` ≥ 95 among non-NA/non-Exempt | PROVISIONAL (field-name check) |
| DEC-H32 | Pricing | mean `rate_spread` among originations (action 1) that are conventional (`loan_type == 1`), 30-year (`loan_term == 360`), fixed-rate (`intro_rate_period == NA`), with numeric rate spread | PROVISIONAL (fixed-rate proxy) — Adapted from P028 "30-year FRM" |
| DEC-H33 | Denial reasons | among denied records: share with any of `denial_reason-1…4` = 1 (DTI), = 2 (employment history), = 3 (credit history), = 5 (insufficient cash) | DECIDED |

### 4.4 Geography and linkage

| ID | Decision | Status | Basis |
|---|---|---|---|
| DEC-H40 | Primary unit: **1990 commuting zones**, assigned through David Dorn's county→CZ crosswalk (`https://www.ddorn.net/data/cw_cty_czone.zip`, HTTP 200 verified). CZs align workplace-based labor data (QWI) with residence-based mortgage data, as is standard in local-labor-market research (M19, M20). P024 aggregates HMDA to CZs. | DECIDED | Established (P024; M19) |
| DEC-H41 | County FIPS harmonization patch for codes created or changed after 1990 (e.g. 12086 Miami-Dade, 46102 Oglala Lakota, 08014 Broomfield, Virginia independent-city mergers). Exact patch list to be generated by F3: every HMDA county code 2018–2025 must map to a CZ. | PROVISIONAL | New |
| DEC-H42 | Robustness unit: county. | DECIDED | — |
| DEC-H43 | Linking HMDA to other data at CZ × year. HMDA `activity_year` = calendar year of final action, mapped to calendar-year QWI averages and to July-1 PEP population. | DECIDED | Adapted |

### 4.5 Missing values and exempt values

| ID | Rule | Status |
|---|---|---|
| DEC-H50 | `Exempt` and `NA` are **missing** for DTI, CLTV, rate spread and income. They are never coded as 0. Missingness shares are reported by year × age × exposure tercile so that differential missingness is visible. | DECIDED |
| DEC-H51 | For outcomes subject to partial exemption (DTI, CLTV, rate spread), re-estimate on records from lenders (LEI) with no `Exempt` values in that field in that year (adapted from P028's full-reporter restriction). | DECIDED |
| DEC-H52 | **Consistent-reporter robustness.** Restrict to LEIs present in every year 2018–2025, which neutralizes the 2020–2022 threshold change (P031 fn. 7). | DECIDED |
| DEC-H53 | Applicant age `8888` is dropped. Its share is reported (Kent County probe: 58/3,862 = 1.5%). | DECIDED |

### 4.6 Econometric practice recommendations (pointer)

- Count outcomes: PPML with high-dimensional FE (DEC-E01 in `05`). This is new in the HMDA context but established for counts.
- Application-level conditional outcomes: LPM with lender × year FE and borrower-risk controls (Adapted from P027, P028).
- Reported side by side: *unconditional* cell means vs *conditional-on-observables* estimates. The gap between them measures the composition (selection) contribution (see `06` §3).

---

## 5. Implications for this project

1. **Counts are the cleanest HMDA outcome for a demand-side labor shock.** Denial and pricing outcomes combine applicant selection with lender behaviour. This follows from P024's reading of denial rates and from P028's evidence on unobserved risk factors.
2. **Age requires loan-level processing.** The Data Browser cannot filter by age `[PROBE]`, so the pipeline must download about 6–7 GB of zipped snapshot files and aggregate locally. This is feasible on the target machine (16 GB RAM, 73 GB free disk) if columns are pruned at read time.
3. **Panel integrity requires three safeguards:** (i) a uniform vintage (snapshot), (ii) consistent-reporter robustness for the 2020–2022 threshold episode, and (iii) the CT exclusion or harmonization.
4. **The public data cannot separate credit supply from applicant risk.** Credit scores are missing. Any "conditional denial" result must be labelled as conditional on *observables available in public HMDA* only.
