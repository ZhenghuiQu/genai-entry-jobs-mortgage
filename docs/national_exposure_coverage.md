# National Exposure Coverage

Date: 2026-10-09 (Asia/Shanghai). This document is a Phase 2 audit, not an implementation or treatment-effect report. Mapping release: **PROVISIONAL_AUDIT_NOT_FINAL**. Recommendation **C**.

## Observed scope and download dependency

The national [ACS 2015–2019 person archive](https://www2.census.gov/programs-surveys/acs/data/pums/2019/5-Year/csv_pus.zip) could not be downloaded: default and Chrome-compatible TLS clients return HTTP 403. The response identifies Cloudflare; no credentials or challenge circumvention was attempted. Metadata listing remains accessible through the web tool. `phase2_national_acquisition.json` and append-only source logs preserve the attempts. This is an access failure, not evidence about occupational coverage.

Current RAM is 16 GiB. Current free storage is 57.22 GiB at report rendering. Prior ZIP directory metadata records a 2,238,752,642-byte national archive and about 10.38 GB of expanded person CSVs; these are historical metadata, not a successful current HEAD. The downloader caps compressed storage at 3 GB and requires 8 GiB free. Processing reads ZIP entries to EOF in 100,000-row chunks, stores only occupation × PUMA × age segment × survey-year aggregates, and uses a 2 GB DuckDB memory cap. It never expands all CSVs or downloads HMDA snapshots.

The complete DE archive was reprocessed: 45,217 person rows, 4,898 civilian employed residents aged 22–34. Reusable national code exists, but it has only been exercised on DE. The national branch is not represented as validated. National, all-state, all-CZ, major-group, high-exposure and unresolved-weight distribution requests remain OPEN until acquisition succeeds.

## Recomputed Delaware results by survey year

| geography_id | age_group | survey_year | employment_weight | covered_weight | weighted_coverage_percent | exposure_lower | exposure_upper | known_high_exposure_weight | possible_high_exposure_weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | 22-34 | 2015 | 24349.000000 | 20252.000000 | 83.173847 | 0.282129 | 0.450390 | 4740.000000 | 8837.000000 |
| 10 | 22-34 | 2016 | 23979.000000 | 20349.000000 | 84.861754 | 0.280346 | 0.431728 | 4495.000000 | 8125.000000 |
| 10 | 22-34 | 2017 | 24463.000000 | 20494.000000 | 83.775498 | 0.289322 | 0.451567 | 5124.000000 | 9093.000000 |
| 10 | 22-34 | 2018 | 25780.000000 | 20813.000000 | 80.733126 | 0.282073 | 0.474742 | 5606.000000 | 10573.000000 |
| 10 | 22-34 | 2019 | 25085.000000 | 20719.000000 | 82.595176 | 0.265341 | 0.439389 | 4364.000000 | 8730.000000 |
| 10 | 22-34 | pooled | 123656.000000 | 102627.000000 | 82.993951 | 0.279789 | 0.449849 | 24329.000000 | 45358.000000 |
| 10 | 25-34 | 2015 | 19492.000000 | 16244.000000 | 83.336754 | 0.288835 | 0.455467 | 3856.000000 | 7104.000000 |
| 10 | 25-34 | 2016 | 19520.000000 | 16680.000000 | 85.450820 | 0.279899 | 0.425391 | 3590.000000 | 6430.000000 |
| 10 | 25-34 | 2017 | 20007.000000 | 16975.000000 | 84.845304 | 0.289751 | 0.441298 | 4207.000000 | 7239.000000 |
| 10 | 25-34 | 2018 | 20788.000000 | 16562.000000 | 79.670964 | 0.284957 | 0.488247 | 4646.000000 | 8872.000000 |
| 10 | 25-34 | 2019 | 20666.000000 | 16920.000000 | 81.873609 | 0.267569 | 0.448833 | 3655.000000 | 7401.000000 |
| 10 | 25-34 | pooled | 100473.000000 | 83381.000000 | 82.988465 | 0.282105 | 0.452220 | 19954.000000 | 37046.000000 |

These use five-year PWGTP as supplied. Pooled weights are not multiplied by five; individual-year rows describe components of the same five-year file, not separate annual-weight population estimates. ESR 1/2 and exact age bands are used. Unmatched occupations remain in every denominator.

The 12 `National` rows in `exposure_coverage_by_geography.csv` have `observed=False`, OPEN status and blank numerical metrics. State rows contain DE only; CZ rows represent two partially observed zones allocated from DE PUMAs, not whole CZs. No other-state or complete-CZ coverage is imputed.

## Major groups, unresolved employment and sensitivity

`phase2_coverage_by_major_group.csv` reports observed DE major-SOC coverage by age/year. `unmatched_employment_by_group.csv` preserves unresolved group labels, reason, members, weights, denominators and shares. `exposure_sensitivity.csv` reports four methods and intervals, not outcome coefficients. `phase2_exposure_rank_checks.csv` records interval overlap for the two sample-allocated CZs.

High exposure is explicitly diagnostic: primary group beta ≥ 0.5, chosen without mortgage coefficient inspection. The output separately shows fully scored high-exposure weight and potentially high weight (known high plus all unresolved weight). Coverage among potentially high employment is a conservative availability ratio, not an observed classification of unscored workers. High-exposure coverage nationally cannot be reported.

No spatial ranking is defensible solely from the observed coverage percentages: all 12 pairwise DE CZ interval checks overlap. Bounds are conditional on scoring/allocation assumptions and do not include rating error, ACS sampling error or unknown within-PUMA employment patterns. Gate O05 remains OPEN; the 98% project target has not been relaxed.

## Reproduction

Run `.venv/bin/python scripts/phase2/acquire_sources.py --national` with public network access. Then run `.venv/bin/python scripts/phase2/exposure_coverage.py`. The latter verifies a completed national archive against its acquisition hash before processing; if the file is absent it explicitly produces DE-only diagnostics. Use `make phase2-analyze` to reproduce currently observed local evidence. A 403 response cannot be treated as a completed national audit.
