# Design Decisions Pending

<!-- PHASE2 BEGIN -->
## Current Phase 2 update — 2026-10-09 (Asia/Shanghai)

The proposed cross-review primary 2018–2019 versus 2023–2025 window is not silently adopted. The full source document is missing; available Claude PPML uses 2018–2022 pre/reference2022 and has a separate 2018–2019 companion. See [Phase 2 decisions](phase2_decision_register.md) for source-specific competing specifications and author approvals.

The Day 1–2 evidence below is preserved historically; current Phase 2 findings supersede its occupation/CT/provenance conclusions where explicitly stated. No outcome estimation was authorized.

<!-- PHASE2 END -->
Date: 2026-10-09 (Asia/Shanghai). Scope: Day 1–2 feasibility only. Retrieval timestamps are UTC in the source manifest.

**Evidence labels.** VERIFIED DATA FACT = directly downloaded/parsed or official metadata; TECHNICAL ASSUMPTION = diagnostic implementation rule; UNRESOLVED CHOICE = design/mapping policy not fixed; RECOMMENDATION = action supported by those facts. PASS is limited to the stated procedure and denominator; FAIL rejects the tested configuration; OPEN has an unresolved dependency.

## Research versions must remain separate

| Document set | Observed availability | Geography/authority |
| --- | --- | --- |
| Original research assignment PDF | Missing locally; cited filename 研究任务说明.pdf in Claude review | Contents not independently inspected |
| Independent GPT literature-review package | Missing locally; remote inaccessible | No inferred specification |
| Independent Claude literature-review package | Eight original files in literature/ | Proposes CZ; industry-based exposure fallback |
| Complete GPT–Claude cross-review | Missing locally; user describes it | CZ provisionally preferred per current request |
| Distinct Claude-only cross-review/audit | Missing locally; user describes it | State alternative per current request; do not equate with Claude literature package |

The inaccessible remote cannot be searched for missing documents. “Missing locally” is not a claim about its repository contents. The current user instruction controls: CZ is provisional and State is the pre-specified feasibility fallback; neither review can silently finalize the geography. R01 records the provenance test.

## Preserved provisional specification from the available package

- Mortgage panel window 2018–2025; young applicants 25–34 versus 35–44; auxiliary `<25` and placebo 45–54 contrasts. HMDA `<25` cannot identify ages 22–24 exactly.
- Occupational exposure baseline ACS 2015–2019, civilian employed residents aged 22–34; separately check 25–34. Keep both definitions visible.
- Treatment timing remains pre-2023 versus 2023–2025, with 2022 reference; no outcome-driven retiming.
- Mortgage purchase applications: actions 1–5, first lien, principal residence, site-built 1–4 units, closed-end/nonreverse/nonbusiness restrictions. The available review retains partial-exempt product indicators provisionally.
- QWI age groups A03/A04/A05/A06, unadjusted private workplace jobs; reference-quarter conventions and suppression policies are retained as proposals, not evaluated labor effects.
- Denial/pricing remain selection-sensitive secondary outcomes; no primary coefficient or significance inspection occurred. Estimator, fixed effects, inference and normalization are not reoptimized in this feasibility audit.

## Inconsistencies and unresolved choices

| ID | Observed tension or pending decision | Evidence / next action |
| --- | --- | --- |
| P01 — Review provenance | User describes a Claude-only state audit; local Claude literature package itself proposes CZ | Obtain the distinct audit and both other versions; do not infer a contradiction from missing text |
| P02 — Fallback meaning | Local DEC-D02 is industry-exposure/share-form fallback; current instruction specifies State feasibility fallback | Keep these as two distinct choices; State does not license changing occupation exposure |
| P03 — Physical schema | Review asserts Data Browser-style columns for snapshots and loan_to_value_ratio in 2025 | Observed underscore snapshot fields and 2019 CLTV rename require parser adapters |
| P04 — Occupational membership | Review proposes simple 8→6 truncation and X means | Official exact concordances/explicit composites required; B02 fails conservative sample coverage |
| P05 — Geographic commitment | Local DEC-G01/DEC-G02 mark CZ/CT exclusions decided | Current instruction makes geography provisional; CT bridge/exclusion and Broomfield approximation need reconciliation |
| P06 — QWI sample size | Local plan says 47 states+DC after excluding CT/MI from contiguous states | 48 contiguous minus CT/MI = 46 states+DC = 47 jurisdictions; fix implementation acceptance counts |
| P07 — No-key API | Local REQ-REPRO-04 asserts no key is needed | Observed 200 HTML Missing Key; DE bulk-summary route succeeds |
| P08 — Storage | Local HMDA expanded estimate around 40–50 GB and 6–8 GB zipped | Observed 53.047 GB CSV +7.686 GB ZIP; available disk cannot safely retain all plus auxiliary/output |
| P09 — Rate/value controls | Local affordability index allows owner-unit or population weighting; FHFA assumed CSV | Freeze weight/order of logs and ratios; actual FHFA response XLSX, with missing/base-vintage issues |
| P10 — Cross-border CZs | MI missingness and CT exclusion can leave partial CZs; dominant state is only a clustering label | Define complete-versus-partial CZ handling and calculate affected county/employment shares |
| P11 — Exposure aggregation | Equal O*NET/SOC member means are not employment-weighted internal group scores | Freeze component weights/missing-rating policy before final baseline; do not select by mortgage effects |
| P12 — Geographic mismatches | Three sample rows show county/state inconsistency | Flag and investigate; preserve counts rather than assign from one field silently |
| P13 — Deadline | No current implementation deadline appears in the request; local plan uses one week | A deadline-based recommendation B needs a specified deadline and measured remaining burden |
| P14 — Audit trail integration | Native app history available, complete transcript export unavailable; existing remote logs inaccessible | Preserve originals, request/native-export complete history, integrate additive files without replacing remote tree |

## Facts, assumptions and recommendation

VERIFIED DATA FACTS: eight snapshot files are accessible through the demonstrated client; required concepts exist; CT planning-region codes fail unchanged county mapping; Michigan has no post-2021 QWI; DE occupation coverage under the strict exact-member mapping is below the proposed threshold. TECHNICAL ASSUMPTIONS: equal score means, float tolerance 1e-6, sequential disk layout and diagnostic filters. UNRESOLVED METHODOLOGICAL CHOICES: full SOC memberships/unrated scores, CT/MI/cross-border policy, exposure ages/weights, controls and authentic cross-review specifications. RECOMMENDATION: C, complete those dependencies; retain CZ provisional and State fallback. Do not use regression results to resolve any item.

## Next authorized feasibility actions

1. Restore document/repository access and compare the actual two cross-reviews line-by-line.
2. Complete the explicit occupational hierarchy and missing-score policy, then evaluate weighted coverage nationally for both age bands without inspecting mortgage effects.
3. Resolve CT/Broomfield/cross-border rules and audit the full intended geography using counts only after acquisition procedure approval.
4. Quantify nationwide QWI/control missingness, update a sequential storage budget and bounded pilot, and state the deadline.
5. Decide A/B/C on those facts, freeze design decisions, and obtain a subsequent implementation instruction before national regressions.
