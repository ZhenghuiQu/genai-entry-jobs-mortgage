# Geography Audit

Date: 2026-10-09 (Asia/Shanghai). Scope: Day 1–2 feasibility only. Retrieval timestamps are UTC in the source manifest.

**Evidence labels.** VERIFIED DATA FACT = directly downloaded/parsed or official metadata; TECHNICAL ASSUMPTION = diagnostic implementation rule; UNRESOLVED CHOICE = design/mapping policy not fixed; RECOMMENDATION = action supported by those facts. PASS is limited to the stated procedure and denominator; FAIL rejects the tested configuration; OPEN has an unresolved dependency.

## Scope and official inputs

The official files are `cw_cty_czone.zip`, `cw_puma2010_czone.zip`, `cw_czone_state.zip` and Dorn’s county-code-change PDF, last updated September 2021. [Dorn’s page](https://www.ddorn.net/data.htm) explicitly distinguishes 1990 county definitions and the 2010 PUMA mapping used for 2012–2021 ACS. The state crosswalk assigns a dominant state, which must not be confused with restricting a cross-border CZ to that state.

### C01 — County-to-1990-CZ key integrity

- **Status:** PASS.
- **Source and URL:** [Dorn geography files](https://www.ddorn.net/data.htm).
- **Procedure:** Read the official Stata archive, ignore macOS resource-fork entries, preserve FIPS as zero-padded strings and test duplicates/missing.
- **Observed evidence:** 3,141 county rows, 741 CZs, zero duplicate county keys and zero missing cells.
- **Limitations:** The crosswalk uses 1990 county definitions, not all modern equivalents.
- **Implication for CZ versus State:** CZ has a valid base join; State needs only stable state codes.
- **Next required action:** Apply audited vintage handling before joining mortgage records.

### C02 — 2010 PUMA identifiers and allocation mass

- **Status:** PASS.
- **Source and URL:** [Dorn geography files](https://www.ddorn.net/data.htm).
- **Procedure:** Read the included README; form int(ST)*100000+int(PUMA); test pair uniqueness, signs and PUMA weight sums at tolerance 1e-6.
- **Observed evidence:** 4,077 pairs, 2,351 PUMAs, 741 CZs; 553 PUMAs split across CZs. No duplicate pairs/negative weights; maximum sum error is 7.31e-8. All 4,898 DE employed 22–34 records match, with zero allocation mass error.
- **Limitations:** Population-based afactor does not reveal a person’s true CZ; young-worker composition can vary within a PUMA. Float tolerances are technical assumptions.
- **Implication for CZ versus State:** CZ allocation arithmetic is technically valid; State avoids PUMA allocation uncertainty.
- **Next required action:** Retain fractional weights and expose uncertainty; do not randomly assign one CZ or normalize away missing joins.

### C03 — Historical county changes in a baseline inventory

- **Status:** PASS.
- **Source and URL:** [Dorn geography files](https://www.ddorn.net/data.htm) and [2019 county population file](https://www2.census.gov/programs-surveys/popest/datasets/2010-2019/counties/totals/co-est2019-alldata.csv).
- **Procedure:** Audit all 2019 county IDs against Dorn; separately evaluate documented 12086→12025, 46102→46113 and Broomfield→28900 candidates.
- **Observed evidence:** For the provisional contiguous+DC, CT-excluded inventory: 3,097/3,100 IDs and 99.131% population match raw; documented candidates yield 3,100/3,100 and 100% population coverage.
- **Limitations:** This is a population inventory, not HMDA coverage. Broomfield includes a small contribution from a county in another CZ; Dorn’s assignment is an approximation needing explicit design acceptance.
- **Implication for CZ versus State:** Historic changes appear manageable for CZ; State sidesteps them.
- **Next required action:** Approve genuine rename links separately from Broomfield’s approximation; report shares affected and retain unmatched logs.

### C04 — Connecticut planning-region compatibility

- **Status:** FAIL.
- **Source and URL:** [Dorn geography files](https://www.ddorn.net/data.htm) and [Census final CT change](https://www2.census.gov/geo/pdfs/reference/ct_county_equiv_change.pdf).
- **Procedure:** Compare 2018/2023/2024/2025 CT purchase-originations with the unchanged 1990 county lookup.
- **Observed evidence:** Old CT counties appear through 2023. Nine 09110–09190 planning-region codes appear in 2024/2025; zero of 35,150/35,676 rows match old Dorn geography. County NA counts are 359/336.
- **Limitations:** No tract-level reconstruction was attempted. Two 2018 CT-filtered rows have out-of-state county prefixes; one 2019 national-prefix row is also inconsistent.
- **Implication for CZ versus State:** Unharmonized CT fails CZ. State codes avoid the planning-region break, subject to an explicit consistent CT policy.
- **Next required action:** Choose a documented tract/town bridge or a consistent all-year CT exclusion; never assign planning regions arbitrarily to old counties/CZs.

### C05 — Coverage of the complete intended HMDA sample

- **Status:** OPEN.
- **Source and URL:** [FFIEC/CFPB snapshot files](https://files.ffiec.cfpb.gov/static-data/snapshot/2025/2025_public_lar_csv.zip) and [field documentation](https://ffiec.cfpb.gov/documentation/publications/loan-level-datasets/lar-data-fields); [Dorn geography files](https://www.ddorn.net/data.htm).
- **Procedure:** Tabulate every unmatched sample identifier before filtering; report provisional-purchase coverage separately; check county/state agreement.
- **Observed evidence:** All eight prefix coverage rates and all CT-extract unmatched counts are in geography_audit.json and the geography audit document. Known missing, changed and inconsistent codes remain visible.
- **Limitations:** No complete intended national loan universe was retrieved. Prefix coverage is not a national percentage; candidate mappings have not been adopted.
- **Implication for CZ versus State:** CZ acceptance remains conditional; State also needs sample-policy reconciliation.
- **Next required action:** Run a count-only national geography audit after acquisition approval; report missing county, missing state, mismatch and patch/exclusion shares separately.

## Observed HMDA sample coverage before any geographic drops

| Sample | Rows | Matched to raw Dorn | Raw coverage | Unmatched counts |
| --- | --- | --- | --- | --- |
| hmda_2018_sample.csv | 4377 | 4320 | 98.698% | {"08014": 2, "12086": 55} |
| hmda_2019_sample.csv | 5331 | 5150 | 96.605% | {"08014": 1, "12086": 3, "NA": 177} |
| hmda_2020_sample.csv | 5370 | 5339 | 99.423% | {"12086": 31} |
| hmda_2021_sample.csv | 5948 | 5701 | 95.847% | {"NA": 247} |
| hmda_2022_sample.csv | 4269 | 4232 | 99.133% | {"12086": 37} |
| hmda_2023_sample.csv | 4812 | 4797 | 99.688% | {"08014": 1, "12086": 14} |
| hmda_2024_sample.csv | 5103 | 4447 | 87.145% | {"09110": 207, "09120": 120, "09130": 13, "09140": 61, "09150": 7, "09160": 10, "09170": 90, "09180": 38, "09190": 106, "12086": 4} |
| hmda_2025_sample.csv | 5030 | 5012 | 99.642% | {"09110": 6, "09120": 3, "09140": 1, "09150": 1, "09160": 1, "09170": 3, "09180": 2, "12086": 1} |
| hmda_ct_2018.csv | 41156 | 41018 | 99.665% | {"NA": 138} |
| hmda_ct_2023.csv | 35534 | 35290 | 99.313% | {"NA": 244} |
| hmda_ct_2024.csv | 35150 | 0 | 0.000% | {"09110": 10032, "09120": 2655, "09130": 1790, "09140": 4776, "09150": 1125, "09160": 1294, "09170": 4980, "09180": 2871, "09190": 5268, "NA": 359} |
| hmda_ct_2025.csv | 35676 | 0 | 0.000% | {"09110": 9882, "09120": 2574, "09130": 1946, "09140": 4835, "09150": 1196, "09160": 1285, "09170": 5028, "09180": 3069, "09190": 5525, "NA": 336} |

These denominators include missing county codes, every action/product in a national prefix, and only purchase originations in the CT API extracts. They are not the national intended analysis sample. `geography_audit.json` also reports the provisional purchase-filter subset and separate candidate-map coverage. No unmatched loan was removed from the raw data.

## Historical changes and allocation errors

| Code | Official documented treatment | Status |
| --- | --- | --- |
| 12086 | Rename to predecessor 12025; CZ 7000 | Verified link, candidate application |
| 46102 | Rename to predecessor 46113; CZ 27704 | Verified link, candidate application |
| 08014 | Dorn recommends CZ 28900; originated from multiple counties | Approximation requires explicit acceptance |
| 09110–09190 | Nine new CT planning regions, no old-county Dorn key | Unresolved, no arbitrary match |
| NA/blank county | No geographic assignment | Retain missingness counts |
| County/state disagreement | 1 row in 2019 prefix; 2 in 2018 CT extract | Retain/flag; reconciliation OPEN |

In the 2019 inventory after excluding AK/HI/CT, raw matched population is 319,725,237 of 322,526,819 (99.131%). The three documented candidate treatments cover the entire inventory. This does not authorize treating Broomfield’s approximation as an exact historical boundary bridge. No Alaska vintage repair is attempted under that provisional universe.

The PUMA key is the seven-character combined identifier (two-digit state FIPS plus five-digit PUMA) represented numerically as `100000*ST+PUMA`; leading-zero strings should be retained for audit display. Weight sums lie between 0.999999936670 and 1.000000073065. At tolerance 1e-6, 100% of 2,351 PUMAs pass mass conservation. All 553 split PUMAs remain fractional; no random assignment, nearest-neighbor match or arbitrary renormalization is used.

## CZ versus State implication

VERIFIED DATA FACT: the base Dorn join and allocation factors are sound. UNRESOLVED CHOICE: accept the published Broomfield approximation, exclude CT consistently, or construct an official fine-geography bridge. TECHNICAL ASSUMPTION: population allocation represents young employment inside each PUMA. RECOMMENDATION: retain CZ provisionally and keep State available; complete C05 and occupational gates before selecting either. The existing review’s suggested county predecessor patch is not applied generically to arbitrary splits.
