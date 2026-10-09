# Concordance architecture alternatives — Phase A

Date: 2026-10-09 (Asia/Shanghai). No primary mapping changes.

## Current deterministic membership graph

O*NET-SOC 2019 → published SOC 2018 crosswalk → explicit Census PUMS components and BLS hierarchy → Census 2018 PUMS OCCP.

This graph already resolves all 18 broad/minor and 32 composite memberships among the 62 unresolved Delaware groups, except the invalid component of 7640. X/Y characters are Census aggregation markers, not wildcard operators. A detailed “All Other” code stays terminal. Code ancestry comes from the ordered official BLS hierarchy, not an inferred prefix.

The scoring graph is separate: available child beta mean within SOC, then equal SOC mean within PUMS. The current primary additionally requires every official taxonomy title to be rated. This is a conservative availability policy that includes non-data-level residual titles; it is stricter than merely requiring every intended Eloundou data-level rating.

## NEM alternative

Candidate route: O*NET-SOC 2019 → SOC 2018 → versioned NEM → versioned Census PUMS OCCP. Also inspect the direct O*NET → NEM/OOH workbook used by the literature. Do not assume an OOH profile grouping and a NEM code are interchangeable.

| Dimension | Existing hierarchy route | NEM route |
| --- | --- | --- |
| Membership provenance | Cached official rows reproduced | Official crosswalks identified; row-level comparison OPEN |
| Residual scoring | Missing or explicit approved specialty proxy | May encourage pooling or donor use; provenance must distinguish these |
| One-to-many edges | Explicit Census components | May coarsen distinct ACS occupations into one NEM category |
| Internal weights | Equal SOC / child assumptions documented | Two-stage means can change effective child weights |
| Geographic employment | ACS PWGTP, CZ afactor only after scoring | Same final employment weighting; NEM links do not supply age-specific shares |
| Coverage benefit | Observed DE 82.994% under current policy | Not measured; no numerical gain forecast justified |
| Determinism | Source graph plus explicit scoring rule | Possible only with frozen rows, disjoint memberships and documented weights |

[BLS](https://www.bls.gov/emp/documentation/crosswalks.htm) publishes [NEM/SOC → ACS](https://www.bls.gov/emp/classifications-crosswalks/nem-occcode-acs-crosswalk.xlsx) and [O*NET → OOH](https://www.bls.gov/emp/classifications-crosswalks/nem-onet-to-soc-crosswalk.xlsx). The current occupational structure is based on SOC 2018; the current web page is not proof of the historical workbooks' vintages.

Both files were attempted sequentially with 256 KiB caps per file. Both standard and existing browser HTTP clients received 403; no local XLSX bytes were accepted. `phase3_metadata_acquisition.json` preserves all attempts. Thus no claim here that NEM resolves particular residual codes or produces a 494-category replication is verified. Exact historical NEM vintage remains an implementation dependency.

The Treasury procedure and benchmark are recorded once in [literature_matching_benchmarks.md](literature_matching_benchmarks.md). Its many-to-one links provide a useful scaffold; its coarsening of one-to-many categories changes the analysis taxonomy. Reuse of an architecture does not reproduce its score universe or coverage.

## Why coverage can rise without new information

An ACS composite including rated cooks and unrated cooks-all-other can receive the mean of rated cooks. This makes the whole group “available” but assumes the observed specialties represent its unobserved member and its unknown employment shares. A donor score for a wholly unrated occupation makes an even stronger assumption. NEM can document which categories are pooled; it cannot identify missing task scores or age-specific within-category employment.

[BLS's skills page](https://www.bls.gov/emp/skills/science.htm) flags donor imputation from related O*NET occupations. Its imputation target is skills. Any analogous beta proxy would be our methodological choice, with source and donor flags, rather than an original Eloundou rating.

A two-stage equal mean is path-dependent. If two NEM groups contain one and five scored occupations, averaging group means gives the singleton half the final weight; flattening gives it one-sixth. Compare expanded effective weights, not only final category labels. Deduplicate identical leaf memberships; report overlapping memberships and fractional allocation rather than multiplying employment through a join.

## Recommended next-phase changes

1. Introduce an explicit score-domain field: DATA_LEVEL_RATED, NON_DATA_LEVEL_RESIDUAL, MILITARY_NO_SCORE, or DATA_LEVEL_RATING_MISSING. The last state should have zero count in the current source; fail if it appears unexpectedly.
2. Separate membership validity from score representativeness. Keep strict original coverage as one diagnostic. Add available-specialty policy only as a separately named, explicitly approved measure; never overwrite old status semantics.
3. Store a long edge table: source/destination taxonomy and vintage, code, source URL/hash, sheet/row, edge type, member weight, data-level flag, rating status, correction identifier, uncertainty flag. Validate one-to-many and many-to-many cardinality explicitly.
4. Version the Census 7640 exception, supported by the explicit identifier 7550 and both source rows. Even after correction, maintain residual-policy uncertainty.
5. Once authentic small NEM workbooks are accessible, compare leaf-code sets and effective weights for all 529 PUMS categories, prioritizing the 62 issue rows. Inventory coarsening, duplicate paths, unknown codes, unmatched mass and score/rank changes. Pin historical vintage rather than adopting the latest mutable workbook without review.
6. Implement optional equal-SOC, flattened equal-child and compatible pre-treatment national employment-weight sensitivities, with distinct denominators. [OEWS](https://www.bls.gov/oes/oes_ques.htm) has no demographic estimates and excludes self-employment; it cannot identify young-worker O*NET specialty shares.
7. Keep terminal wholly unrated occupations missing in the primary. Proxy/donor use requires explicit approval, a justified protocol and separate bounded sensitivity; title similarity remains prohibited.

Recommendation: retain the verified Census/BLS graph as the baseline and evaluate NEM as an independently documented alternative. Current evidence supports a policy audit before more hierarchy coding. National aggregation and mortgage models remain gated.
