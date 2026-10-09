# Literature matching benchmarks — Phase A

Date: 2026-10-09 (Asia/Shanghai). Base: `6ff6250`. No national calculation or mortgage regression.

## Evidence table

| Source | Reported statistic | Comparability |
| --- | --- | --- |
| Treasury (2024), Appendix A, printed pp. 28–29 | Approximately 95% of ACS persons with occupational codes matched | Best person-coverage benchmark; weighting unspecified |
| Tucker (2026), Section 2, footnote 1, Table 1 | No occupational match percentage found; variance 0.0447 → 0.0148 | Aggregation loss, not matching coverage |
| Felten, Raj, Seamans (2021), Section 2.2.3 | 832 O*NET occupations → 774 SOC scores | Counts, not ACS employment coverage |
| Current cached Delaware audit | 82.993951% / 82.988465%, ages 22–34 / 25–34 | PWGTP-weighted civilian employment; different population and score |

## Treasury

[Schendstok and Schreiner Wertz (2024)](https://home.treasury.gov/system/files/136/AI-Combined-PDF.pdf), Appendix A: O*NET 28.0 work-activity importance → NEM (750 occupations) → ACS (494 analysis categories). Means at each aggregation stage give equal occupational weights. NEM codes 31-1120, 21-1018, and 13-1020 correspond to multiple ACS categories; these ACS categories are coarsened. The appendix uses employed workers and the 2022 five-year ACS; Figure 1 instead labels 2021. Original NEM workbook vintage is not identified.

The approximately 95% denominator is persons with ACS occupational codes. Exact numerator, person-weight use, and a reproducible coverage formula are absent. Missing activity data affect 50 of 923 O*NET occupations, largely residual categories, also software developers. No beta-score imputation or zero-fill rule is documented.

Inference: the route is adaptable as a classification scaffold, but neither its 494 categories nor its coverage can be transferred unchanged to our pre-treatment beta index. Different scoring universes, coarsening, sample years and missingness rules matter. Approximately 95% is a quality target, not an acceptance theorem.

## Tucker

[Lee C. Tucker (2026), CES 26-27](https://www2.census.gov/library/working-papers/2026/adrm/ces/CES-WP-26-27.pdf): GPT-4 beta, SOC 2018 → ACS 2018 via the published Census crosswalk; employed persons' 2015–2019 PUMS weights form occupation–industry employment counts. Detailed industry/state exposure is an employment-weighted mean. ACS 2017 industries → ACS 2022 industries uses many-to-many weights inferred from 2019–2023 five-year PUMS, subtracting part of 2023 and comparing 2019/2021/2022 annual counts. ACS 2022 → QWI NAICS 2022 gives detailed industries their linked ACS exposure.

The paper does not identify the occupational workbook filename or its internal SOC aggregation rule sufficiently for exact replication. No employment-weighted occupational match rate is found. Table 1 reports mean-preserving aggregation and within-industry information loss; its ICC is not coverage. Its construction supports pre-treatment employment weighting, not substituting industry exposure for a regional occupational index.

No replication link was found in the [official landing page](https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-27.html) or [author homepage](https://leetucker.net/), inspected 2026-10-09. This bounded search does not establish that code does not exist.

## Alternative literature and taxonomy methodology

[Felten, Raj, and Seamans (2021), DOI 10.1002/smj.3286](https://sms.onlinelibrary.wiley.com/doi/full/10.1002/smj.3286), Sections 2.2.3–2.2.4, use O*NET 24.3, equally average specialties into six-digit SOC, standardize AIOE, and aggregate using 2019 industry employment, then county industry composition. Their score measures abilities, rather than Eloundou task-time savings. Their [author repository](https://github.com/AIOE-Data/AIOE) supplies scores, inputs and code. The inspected sections do not establish an ACS match denominator, unmatched ACS list, or a comparable coverage percentage. Application-set sensitivity assesses score construction, not concordance coverage. Do not combine their score counts with Treasury's person percentage into a literature average.

[O*NET 2019 taxonomy](https://www.onetcenter.org/taxonomy.html) distinguishes 923 data-level occupations from 93 titles without data; [the complete non-data-level list](https://www.onetcenter.org/taxonomy/2019/no_data_coll.html) was transcribed and checked against our cached ratings. All 923 data-level occupations are rated. Thus “93 missing ratings” does not mean 93 failed rating records. Non-data-level titles still represent employment that needs a disclosed residual scoring policy.

[Census 2019 PUMS documentation](https://www.census.gov/programs-surveys/acs/microdata/documentation.2019.html), its cached ReadMe §X.G–H, and the [five-year dictionary](https://www2.census.gov/programs-surveys/acs/tech_docs/pums/data_dict/PUMS_Data_Dictionary_2015-2019.pdf) distinguish PUMS composites/pseudo-codes from SOC. The five-year product reports the harmonized occupation recode; do not attach an annual-file vintage solely from SERIALNO.

[BLS crosswalk documentation](https://www.bls.gov/emp/documentation/crosswalks.htm) publishes NEM/SOC–ACS and O*NET–OOH links. [BLS skills documentation](https://www.bls.gov/emp/skills/science.htm) explicitly flags imputed skills from similar O*NET occupations. An official donor link for skills would not itself validate imputing Eloundou beta.

## Verification scope

Primary sources only; official PDFs, taxonomy pages and author materials inspected remotely. Two optional XLSX acquisitions failed with HTTP 403; no workbook rows from those NEM files were verified. No national microdata acquired. Detailed local calculation provenance: `results/feasibility/phase3_cached_audit.json`. Literature summaries are bounded; negative findings mean “not found in inspected material,” not universal absence.
