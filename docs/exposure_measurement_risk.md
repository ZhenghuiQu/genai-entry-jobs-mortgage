# Exposure measurement validity and risk — Phase A

Date: 2026-10-09 (Asia/Shanghai). Diagnostics designed for later approval; no national execution.

## Index and denominator contract

Let W_ga be total pre-treatment ACS civilian employment weight in geography g and age band a. Let w_gao be occupation weight, M_o be a valid score indicator, and b_o the chosen occupational beta. For CZ allocation, w incorporates published PUMA–CZ fractions; retain and report any unallocated mass. State exposure uses PWGTP directly. Fix whether all-age or age-specific composition defines treatment before viewing mortgage outcomes; age-specific treatment can change the interpretation of an age-based DDD.

Coverage C_ga = sum(w_gao M_o)/W_ga. Known numerator S_ga = sum(w_gao M_o b_o). The covered-only mean S_ga/(W_ga C_ga) is a selected-population statistic. Do not call it the full employment index without an assumption about missing exposure. Null groups never receive zero as an imputed score.

Conditional conservative bounds: [S_ga/W_ga, (S_ga + W_ga(1-C_ga))/W_ga], using beta in [0,1]. These condition on the selected aggregation rule in rated groups, not on the validity of task scores. Without defensible internal shares, allow each fully rated composite to span its child minimum/maximum; unscored groups span [0,1]. Missing residual shares cannot be assumed small from their code count.

## Designed diagnostics

| Diagnostic | Planned calculation/output | Interpretation and guardrail |
| --- | --- | --- |
| 1. Employment-weighted coverage | Total/scored/unresolved PWGTP by policy; counts separately | Keep denominator identical across policies and retain every employed record |
| 2. Major-group coverage | Derive official major parent; scored and unresolved weight by major | Concentration in a major group is potentially systematic measurement error |
| 3. Geography and age | State/CZ × age × year/pooled, missing geography shown separately | CZ figures require national component coverage; DE-allocated slices are not complete CZ estimates |
| 4. Missingness vs observed exposure | Missing mass vs covered-only mean; bins and descriptive correlations | Observed mean is selected; unknown beta cannot be regressed as if observed; no mortgage outcomes |
| 5. Composite dispersion | Leaf count, data-level/residual count, min/max, SD, effective weights | Compute only observed-rating dispersion; missing ratings are not zero-valued observations |
| 6. Rank sensitivity | Equal-SOC vs equal-child vs approved pre-treatment external employment weights; Spearman/Kendall, rank shifts, top-quartile membership | Preserve common denominator; identify geography-specific imputed mass; weights are not chosen using regression results |
| 7. Conservative bounds | Missing-group bounds plus internal-composition envelopes; pairwise rank separation | Robust order only when intervals separate; overlap means unidentified order, not equality |
| 8. Unrated-group sensitivity | Strict, available-specialty, donor only if approved, leave-one-major-group-out, worst-case missing exposure | Report coverage gain together with score/rank changes and proxy share, so high availability cannot hide stronger assumptions |

Use existing DE aggregates for arithmetic validation. For a future national run, stream each approved source sequentially into occupation/geography sums with conservation assertions; never create a person-level many-to-many join. Census replicate-weight uncertainty should be evaluated in a separately budgeted run once suitable cached aggregates exist; current aggregates do not retain replicate weights. Do not manufacture standard errors.

## Current observed risk

The independently reproduced coverage is 82.993951% (22–34) and 82.988465% (25–34). Existing conditional DE bounds are approximately [0.279789, 0.449849] and [0.282105, 0.452220]; widths are about 0.170060 and 0.170115. These wide bounds are not confidence intervals. Existing DE-allocated CZ pairs have overlapping missing-score intervals; no national rank conclusion follows.

Available-specialty policy reaches 88.435660% / 88.842774%. This gain chiefly reclassifies 20 group scores by a representativeness assumption; it does not add task ratings. Source correction plus that rule could add 72 further weight to ages 22–34, leaving coverage around 88.494%. Reaching 95% would require about 8,045.2 more weight beyond that scenario. Because occupations are indivisible groups, this arithmetic is not a feasible mapping solution or a target-driven rule.

The largest missing group, cooks, accounts for 2,186 weight, but the wholly unscored 35-2019 component's actual share inside that group is unknown. Assigning the rated cooks' average to all cooks changes the score-assignment estimand. Standalone residuals cannot be repaired by a many-to-one crosswalk alone.

## Severity and uncertainty

High, verified: missing exposure is concentrated in documented residual members; primary scores cover only about 83% of young-worker weight. High, verified: a 923-rating universe and a 1,016-title taxonomy have different domains. Calling non-data-level titles missing data-level observations misstates source completeness.

High, conditional: residual proxy averaging can raise coverage while altering regional ranks; quantify its influence rather than accept a coverage target alone. Medium, verified: 7640 source inconsistency affects 72 weight; its correction does not solve its scoring assumption. Medium, open: NEM may introduce coarsening/overlap and donor assumptions; workbook edges are not yet inspected.

Approximately 95% is literature-informed quality guidance; any 95% or historical 98% rule must be prespecified together with population, score domain, aggregation assumptions and uncertainty diagnostics. Neither is a universal standard. Do not alter prior acceptance rules silently or relabel a proxy as an exact match.

High coverage does not validate AI adoption, treatment intensity, causal identification, the mortgage age comparison or a DDD parallel-trends assumption. Exposure beta remains a potential task-time-saving measure. Do not use mortgage coefficients, signs or significance to select mappings or internal weights.

## Decisions still open

Approve or reject an available-specialty representation rule; determine residual/donor sensitivity scope; approve the documented source exception; choose the treatment composition age universe and aggregation weights; select acceptable missingness/rank robustness criteria independently of outcomes. These are Phase B decisions. The resource and implementation gate is [phase3_resource_safe_plan.md](phase3_resource_safe_plan.md).
