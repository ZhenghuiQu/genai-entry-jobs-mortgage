# Occupational Mapping Resolution

Date: 2026-10-09 (Asia/Shanghai). This document is a Phase 2 audit, not an implementation or treatment-effect report. Mapping release: **PROVISIONAL_AUDIT_NOT_FINAL**. Recommendation **C**.

## Official membership and schemas

The complete [BLS 2018 hierarchy](https://www.bls.gov/soc/2018/soc_structure_2018.pdf) has 23 major, 98 minor, 459 broad and 867 detailed occupations. The parser reads ordered published parent/child rows, with level rules and three exceptional minor codes from the [official coding guide](https://www.bls.gov/soc/2018/soc_2018_class_and_coding_structure.pdf). It does not expand Census composites by a shared prefix. All 1,556 extracted BLS source lines are retained; this is a web text representation, not a byte-identical PDF.

The Census ACS worksheet supplies 529 PUMS groups. Explicit `Combines` rows, including nested composite leaf rows, supply component membership; numeric broad/minor members are then expanded through the BLS tree. Original OCCP, SOCP, description, source components, detailed/rated/unrated members, Excel rows, source links, status, ambiguity, terminal All Other members and the aggregation rule appear in `occupation_mapping_final.csv`. The filename is contractual; its metadata explicitly says the mapping is provisional. `soc2018_official_hierarchy.csv` preserves hierarchy levels and source line numbers.

Revalidated ratings: 923 unique O*NET-SOC ratings, linked exactly to the official 2019 crosswalk. There are 1,016 official children, 798 detailed SOCs with at least one rating, 774 with every official child rated, 69 entirely unrated SOCs and 24 partly rated SOCs. The 93 unrated children are exported separately. Source commit: `0471612fef3cc22b74fb884d27bff9dbd3770582`; original local source hashes are rechecked.

## Aggregation and employment weights

Primary audit rule: mean over official O*NET children within detailed SOC, then equal mean over detailed members within PUMS group, only when every child/member is rated and memberships are valid. An equal member mean is not employment-weighted. The geographic index applies ACS PWGTP afterward; CZ allocation uses PWGTP × published afactor.

The inspected ACS/O*NET inputs cannot identify internal detailed-SOC employment shares inside a Census composite or O*NET-child shares inside SOC. [OEWS](https://www.bls.gov/oes/oes_ques.htm) has no age demographics and excludes self-employed workers; its May 2019/2020 categories combine 2010/2018 SOC definitions. National OEWS employment could supply an all-age external sensitivity weighting after explicit concordance, not observed age-specific internal shares. It cannot resolve O*NET-child weights. No employment-weighted internal score is claimed or implemented.

Prespecified alternatives: (1) equal mean across all rated O*NET children of a fully rated PUMS group; (2) an envelope from minimum to maximum child rating for fully rated groups; (3) an explicitly diagnostic equal-SOC mean allowing a SOC with some unrated children. Alternative 3 assumes observed children represent missing children and has a different coverage definition; it is not an accepted primary repair. National OEWS weights remain an unimplemented optional sensitivity because compatible shares have not been validated.

## Unmatched categories and source anomaly

A — official broad/minor expansion: resolved through the BLS tree; original-to-repaired coverage is recomputed, not presumed.

B — 74 PUMS groups contain an unrated detailed SOC or an unrated O*NET child. Terminal All Other occupations remain real detailed occupations and are never expanded to neighbors.

C — Census military rank-not-specified `55-9830` is a special aggregate outside the regular BLS hierarchy; membership stays unresolved. Military groups are preserved even though ESR 1/2 defines the civilian coverage universe.

D — blank/unknown OCCP or OCCP/SOCP inconsistency is flagged at the person-aggregate join. Observed DE young-worker missing/inconsistent weight is zero; national values are unknown.

E — group 7640 contains original `40-9095` at ACS worksheet Excel row 707. The text explicitly calls it Census 7550, manufactured building/mobile home installers. The separate official Census list, Excel row 547, maps that exact Census identifier and title to `49-9095`; the O*NET crosswalk corroborates that SOC. This is authoritative support for a correction candidate, not an observed PUMS erratum. Both codes and the basis are preserved; the primary audit leaves group 7640 unscored. Even correcting this typo does not rate its `49-9099` All Other component.

## Weighted coverage and bounded uncertainty

| age_group | employment_weight | covered_weight | weighted_coverage_percent_after | available_soc_diagnostic_coverage_percent | exposure_lower | exposure_upper | weighted_coverage_percent_before |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 22-34 | 123656.000000 | 102627.000000 | 82.993951 | 88.435660 | 0.279789 | 0.449849 | 71.178107 |
| 25-34 | 100473.000000 | 83381.000000 | 82.988465 | 88.842774 | 0.282105 | 0.452220 | 71.529665 |

The before column independently reproduces Day 1–2. The after column applies the stronger every-child rule, so the change reflects both official hierarchy repair and tighter missing-child accounting. Available-SOC diagnostic coverage is 88.436% / 88.843%; those higher values assume missing children can be represented by rated ones. Neither rule meets the original 98% target.

For total employment W, known-score numerator S and unresolved employment U, the conservative conditional bounds are [S/W, (S+U)/W]. Unmatched employment is retained in W; the lower bound is not zero imputation. These bounds condition on the equal-share primary scores of covered groups. The separate child-min/max envelope permits unknown internal composition among rated children as well. They do not bound uncertainty in the original AI ratings themselves.

There are 62 unresolved DE occupation groups among ages 22–34 (versus 107 in the original audit). Both DE-allocated CZ intervals overlap in every observed age/year comparison; their exposure ranking is not robust to unscored employment. No national ranking claim is made. Coverage describes availability, not identification, AI adoption, or precision; replicate-weight uncertainty has not been estimated.

Gate details: O01–O05 in `phase2_gate_status.json`. The hierarchy procedure passes; rating/aggregation/source policy remains OPEN, and the observed 98% coverage test FAILS.
