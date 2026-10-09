# Occupation Crosswalk Audit

Date: 2026-10-09 (Asia/Shanghai). Scope: Day 1–2 feasibility only. Retrieval timestamps are UTC in the source manifest.

**Evidence labels.** VERIFIED DATA FACT = directly downloaded/parsed or official metadata; TECHNICAL ASSUMPTION = diagnostic implementation rule; UNRESOLVED CHOICE = design/mapping policy not fixed; RECOMMENDATION = action supported by those facts. PASS is limited to the stated procedure and denominator; FAIL rejects the tested configuration; OPEN has an unresolved dependency.

## Source chain and mapping rule

Original ratings are pinned to Git commit `0471612fef3cc22b74fb884d27bff9dbd3770582` in the Eloundou author repository. Join `O*NET-SOC Code` to the official O*NET-SOC 2019→SOC 2018 workbook using the full code. Then use the ACS worksheet of the official 2018 ACS/SIPP PUMS occupation list. The SIPP worksheet is not substituted. The pooled ACS five-year dictionary and [ReadMe, page 18](https://www2.census.gov/programs-surveys/acs/tech_docs/pums/ACS2015_2019_PUMS_README.pdf) identify X/Y as aggregates.

No wildcard or prefix code inference is performed. Explicit Census `Combines` rows determine component membership. A group is scored only when every explicitly enumerated member is a scored exact detailed SOC. Numeric broad/minor codes are retained as unresolved rather than assumed to be detailed codes. A source-defined membership map and a scoring-weight assumption are separate objects.

### B01 — Original exposure classification and dv_rating_beta

- **Status:** PASS.
- **Source and URL:** [Eloundou source repository](https://github.com/openai/GPTs-are-GPTs) and [official O*NET-to-SOC crosswalk](https://www.onetcenter.org/taxonomy/2019/soc/2019_to_SOC_Crosswalk.xlsx?fmt=xlsx).
- **Procedure:** Pin the source Git commit; join complete occupation identifiers to official O*NET 2019 occupations and the SOC 2018 crosswalk.
- **Observed evidence:** 923 unique ratings; all 923 match O*NET-SOC 2019 and the official SOC crosswalk. 798 scored detailed SOC groups; no missing beta; beta is bounded by 0 and 1. Only 762 codes also occur in the older 2010 list.
- **Limitations:** Code membership and exact official mappings establish usable taxonomy; ratings measure task capability, not adoption.
- **Implication for CZ versus State:** Occupation classification is a common dependency for both CZ and State.
- **Next required action:** Retain the pinned raw-source hash and exact concordance, not occupational prefix truncation.

### B02 — Employment-weighted coverage under a strict documented mapping

- **Status:** FAIL.
- **Source and URL:** [Census occupation concordances](https://www.census.gov/topics/employment/industry-occupation/guidance/code-lists.html).
- **Procedure:** occupation_audit.py reads ACS worksheet identifiers and explicit Combines members, then joins complete official SOC codes. Numeric broad/minor groups and incomplete score groups stay unresolved.
- **Observed evidence:** Delaware 22–34 coverage is 71.178% (88,016/123,656); 25–34 is 71.530% (71,868/100,473). Neither satisfies the available review’s proposed 98% acceptance level. 107 unmatched young-worker groups are exported.
- **Limitations:** FAIL refers to this deliberately conservative mapping in DE, not proof that all lawful concordances or national exposure are impossible. Missing detailed membership and unrated All Other groups both contribute.
- **Implication for CZ versus State:** Moving to State does not fix occupational concordance; exposure must be repaired first.
- **Next required action:** Obtain explicit SOC hierarchy membership, resolve missing-rating policy and validate a complete national crosswalk; never fill by undocumented X/Y or prefix matches.

### B03 — 2015–2019 PUMS coding and age-weight constructibility

- **Status:** PASS.
- **Source and URL:** [Census occupation concordances](https://www.census.gov/topics/employment/industry-occupation/guidance/code-lists.html) and [ACS five-year ReadMe](https://www2.census.gov/programs-surveys/acs/tech_docs/pums/ACS2015_2019_PUMS_README.pdf).
- **Procedure:** Read all 45,217 DE person records; infer survey year from SERIALNO; retain ESR 1/2, exact ages, PWGTP; compare OCCP/SOCP to official 2018 ACS worksheet.
- **Observed evidence:** All five years appear. In both requested young age bands, every observed SOCP agrees with the official 2018 PUMS group and has no blank code; 2015–2017 records already use that scheme in the pooled file.
- **Limitations:** This is empirical confirmation for DE only, not a nationwide harmonization certificate; exact age, residence and civilian employment are observed.
- **Implication for CZ versus State:** Age-weighted arithmetic can run at State or via PUMA allocation; complete-score coverage is still B02/B05.
- **Next required action:** Extend the survey-year consistency/missingness audit to the full approved baseline, retaining weights and unmatched codes.

### B04 — Aggregated X/Y occupations and rating aggregation

- **Status:** OPEN.
- **Source and URL:** [Census occupation concordances](https://www.census.gov/topics/employment/industry-occupation/guidance/code-lists.html).
- **Procedure:** Export official PUMS members, worksheet row numbers, candidate score ranges and component counts; use equal-child/equal-member means solely for the diagnostic.
- **Observed evidence:** X/Y groups are actual Census composites. Examples: 11-10XX combines 11-1011 and 11-1031, not 11-1021. Y groups contain explicitly listed subsets. Group 7640 lists 40-9095, which is not in the official SOC crosswalk; it was not silently corrected.
- **Limitations:** Equal means are technical assumptions, not employment shares. Some component groups are broad SOC codes requiring another explicit hierarchy step; some detailed occupations have no rating.
- **Implication for CZ versus State:** Both geographies share aggregation ambiguity; averaging occupations is separate from geographical employment weighting.
- **Next required action:** Freeze and justify within-group weights, missing-rating treatment and any documented erratum; rerun coverage before calculating a final exposure.

### B05 — National employment-weighted exposure acceptance

- **Status:** OPEN.
- **Source and URL:** [Census occupation concordances](https://www.census.gov/topics/employment/industry-occupation/guidance/code-lists.html).
- **Procedure:** Report coverage separately for 22–34/25–34 and all five sample years; attempt only national PUMS size/tail inspection, never its full records.
- **Observed evidence:** Pooled and year-specific DE coverage is archived; covered-weight allocation to two CZs conserves the included weights.
- **Limitations:** No national PUMS records were collected. Covered-only averages are diagnostics; no final state/CZ exposure is released.
- **Implication for CZ versus State:** The critical missing national exposure validation prevents choosing A or claiming State resolves the dependency.
- **Next required action:** Complete B02/B04, then obtain an approved national/count-by-occupation baseline and report both national and regional weighted coverage.

## Employment-weighted sample coverage

| Ages | Survey year | Persons | PWGTP denominator | Scored weight | Coverage | Missing/inconsistent code weight |
| --- | --- | --- | --- | --- | --- | --- |
| 22-34 | pooled | 4898 | 123656 | 88016 | 71.178% | 0/0 |
| 22-34 | 2015 | 980 | 24349 | 17887 | 73.461% | 0/0 |
| 22-34 | 2016 | 970 | 23979 | 17451 | 72.776% | 0/0 |
| 22-34 | 2017 | 950 | 24463 | 16976 | 69.395% | 0/0 |
| 22-34 | 2018 | 978 | 25780 | 17661 | 68.507% | 0/0 |
| 22-34 | 2019 | 1020 | 25085 | 18041 | 71.919% | 0/0 |
| 25-34 | pooled | 3928 | 100473 | 71868 | 71.530% | 0/0 |
| 25-34 | 2015 | 773 | 19492 | 14452 | 74.143% | 0/0 |
| 25-34 | 2016 | 779 | 19520 | 14333 | 73.427% | 0/0 |
| 25-34 | 2017 | 766 | 20007 | 14135 | 70.650% | 0/0 |
| 25-34 | 2018 | 772 | 20788 | 14250 | 68.549% | 0/0 |
| 25-34 | 2019 | 838 | 20666 | 14698 | 71.122% | 0/0 |

Denominator: all civilian employed residents (ESR 1/2) in the exact requested age band, including unmatched occupational groups. It is not the matched subsample denominator. PWGTP values are five-year weights; their pooled sum is not multiplied by five. No employed unmatched group is silently dropped when computing coverage.

## Ambiguity, exclusions and diagnostic construction

For ages 22–34, 12,406/123,656 employment weight lies in X/Y codes. At least 25,621/123,656 weight lies in explicit multi-member or multi-O*NET-child groups under this conservative diagnostic; unresolved broad groups can add further ambiguity. All 107 unmatched young-worker OCCP/SOCP groups and their weights are exported in `occupation_unmatched_groups.csv`. Group labels, explicit members, Excel row numbers, score range and status for all 529 PUMS groups are in `occupation_mapping_diagnostic.csv`; observed ambiguous groups are in `occupation_ambiguous_groups.csv`.

Examples requiring explicit hierarchy expansion include `25-1000` postsecondary teachers, `25-2020` elementary/middle-school teachers, `15-1230` computer support, and `53-3030` driver/sales workers and truck drivers. A nonzero terminal “All Other” code is never filled from neighboring occupations. The group-7640 component `40-9095` is retained as an invalid official-source member until an authoritative correction is established.

TECHNICAL ASSUMPTION: an equal mean over scored O*NET children within a SOC, then an equal mean over explicitly enumerated detailed SOC members within a PUMS group. This is deliberately transparent and provisional. The official crosswalk supplies memberships, not these weights. Employment weights PWGTP, and PWGTP×afactor for CZ allocation, are applied only after occupation scores are defined. Covered-only arithmetic conserves included weights in two DE CZs but does not constitute a complete exposure. No index is standardized or released for treatment estimation.

## Unresolved boundary

A complete occupation mapping could materially raise these conservative coverage rates; 71% is not an estimate of the maximum achievable coverage. A national pass or final index requires official detailed membership for broad SOC groups, a defensible policy for unrated components, resolved source errors, age-specific employment-weighted coverage by region and survey year, and frozen aggregation weights. State aggregation alone does not meet these requirements.
