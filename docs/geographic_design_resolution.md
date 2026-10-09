# Geographic Design Resolution

Date: 2026-10-09 (Asia/Shanghai). This document is a Phase 2 audit, not an implementation or treatment-effect report. Mapping release: **PROVISIONAL_AUDIT_NOT_FINAL**. Recommendation **C**.

## Option A: official Connecticut bridge

Use the [official Census 2022 relationship files](https://www.census.gov/geographies/reference-files/2022/geo/relationship-files.html), linking new-region county subdivisions to legacy 2020 block groups (which preserve old county FIPS) and to 2022 tracts. Keep every positive land/water area relationship. Map a region or tract only if all documented old-county members have a single Dorn CZ. Do not choose a largest-area county or assign population proportions absent from the source.

Observed: 169 towns; 884 unique tracts, none ambiguous at CZ level; nine planning regions. All eight legacy Connecticut counties map to Dorn CZ 20901, and that CZ contains only Connecticut counties. Every documented new-region component therefore has the same CZ. This exact CZ result does not imply an exact new-region-to-old-county assignment: several regions span multiple old counties. Machine memberships and source records are archived in `phase2_ct_region_membership.csv`, `phase2_ct_tract_bridge.csv`, and complete web-text extracts. Byte download attempts failed 403; extract hashes identify the text representation only.

## Empirical comparison of A and B

| year | rows | option_A_mapped_rows | option_A_coverage_percent | missing_county_rows | county_state_inconsistent_rows | option_B_consistent_CT_exclusion_rows | option_B_CT_retention_percent |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2018 | 41156 | 41016 | 99.659831 | 138 | 2 | 41156 | 0 |
| 2023 | 35534 | 35290 | 99.313334 | 244 | 0 | 35534 | 0 |
| 2024 | 35150 | 34791 | 98.978663 | 359 | 0 | 35150 | 0 |
| 2025 | 35676 | 35340 | 99.058190 | 336 | 0 | 35676 | 0 |

These are existing CT-filtered recorded home-purchase **originations**, all ages, for four years. They are not the primary national home-purchase application sample or all 2018–2025 years. The denominator includes missing/inconsistent records. Option A recovers every consistent nonmissing CT county in 2024/2025. It flags two out-of-state county rows in the 2018 CT extract; no tract/county inconsistencies occur in these four extracts. Remaining counts are 138, 244, 359 and 336 missing-county rows; no supported geographic information recovers them.

Option B consistently excludes CT across every HMDA/ACS/control/labor year: 100% loss of these CT-originations and 0% CT retention. In the 2019 population inventory that removes 3,565,287 residents and eight counties. Because the observed Dorn CT CZ is entirely within CT, exclusion removes one whole CZ and creates no partial CZ. The earlier concern that CT exclusion necessarily fragments a cross-border CZ is not supported by this crosswalk.

## Remaining geography policies

- Genuine renames 12086→12025 and 46102→46113 are supported by Dorn’s September 2021 county-change notes; audit original/repaired keys separately.
- Broomfield 08014→28900 is Dorn’s approximation. Its four source counties include Weld in another CZ. Do not call it an exact bridge. Report its affected HMDA weight before author acceptance; a sensitivity may exclude Broomfield consistently. No such complete national application count is currently observed.
- Missing counties, missing states and state/county/tract disagreements remain separate flagged categories. Do not pick a preferred identifier silently. An officially validated known tract can only recover a missing county when its state and mapping are consistent; no such recovery is observed here.
- There are 137 cross-state CZs in the complete Dorn county inventory. The dominant-state map is a label, not a membership restriction. `phase2_partial_cz_population.csv` measures population consequences of CT and CT+MI exclusions. A MI exclusion can fragment other CZs; preserve all components consistently across exposure and outcomes or drop the whole affected CZ with explicit approval. National young-worker losses are not yet measured.
- Dorn PUMA2010 allocations retain fractional afactor, including 553 split PUMAs. All 2,351 PUMA sums pass tolerance 1e-6; DE allocation mass error is zero. Young-worker spatial composition inside a PUMA remains an assumption.

| policy | county_rows | mapped_rows | population | coverage_percent |
| --- | --- | --- | --- | --- |
| retain_CT | 3108 | 3108 | 326092106 | 100.000000 |
| exclude_CT | 3100 | 3100 | 322526819 | 100.000000 |
| drop_CT_affected_CZs | 3100 | 3100 | 322526819 | 100.000000 |

Inventory rates above are 2019 population/county coverage for contiguous states plus DC, with documented rename candidates and the Broomfield approximation. They do not establish national HMDA coverage. Alaska/Hawaii remain visible in the original inventory, and any primary contiguous-sample restriction still requires author confirmation.

## Recommendation and gate implications

Prefer Option A and retain Connecticut provisionally: it has a documented exact CZ bridge and avoids needless sample loss. Option B is technically coherent but sacrifices an entire CZ. No outcome estimates were used to choose. G02 passes the bridge and bounded-sample test; G03 remains OPEN for the full national application universe, Broomfield policy and state-exclusion employment losses. CZ remains provisional; State remains the geographic fallback and does not resolve missing occupation ratings.
