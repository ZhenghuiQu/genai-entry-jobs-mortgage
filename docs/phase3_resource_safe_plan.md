# Resource-safe Phase 3 plan — Phase A handoff

Date: 2026-10-09 (Asia/Shanghai). **Phase A complete; Phase B NOT AUTHORIZED.**

## Repository and authorization

Verified repository: https://github.com/ZhenghuiQu/genai-entry-jobs-mortgage. Starting branch `codex/phase2-exposure-repair`, clean at `6ff6250027b52abd8b4cb0b8d41a810463288723`. Working audit branch: `codex/phase3-matching-audit`. The authenticated GitHub CLI successfully read repository metadata and verified the remote research branch at the same SHA. One Git HTTPS ls-remote request returned an empty reply; this does not override the successful API check or imply broken authentication.

Old Phase 2 access statements are historical. No authentication setup, fetch/reset, history rewrite, force-push or main merge was performed. Documentation, a compact issue registry and reproducibility evidence are to be committed locally after review. Publication/push is not required by Phase A.

## Resource-safety preflight

Lightweight commands: git status/remote/log, df, memory_pressure -Q, vm_stat, uptime, and read-only ps/sysctl after sandbox access was needed. Initial disk availability: 57,344,000,000 bytes (53.406 GiB); later df snapshot: 53,426,696 KiB available (50.952 GiB). Physical RAM: 17,179,869,184 bytes (16 GiB). Initial memory_pressure reported 45% free; subsequent snapshot 43%, with 2.12 MiB swap used. This metric is not a promise of allocatable application RAM. Initial vm_stat reported 4,663 free 16-KiB pages, extensive compression; active load increased from 9.64/9.13/6.57 to 19.93/11.30/7.95. Only process names were read; no signals or priority changes occurred.

The separate Finance project's latest local `runs/full_D_dual/code/run_corrected_replay_v5.py` was inspected read-only, specifically constants lines 62–68 and the pre-batch safeguard:

- launch gate: 40 GiB;
- hard stop: 25 GiB;
- controlled projected-free-space stop: **48 GiB**;
- temporary reserve: 1.641940 GiB; output reserve: 2 GiB.

These are independent guards, not interchangeable. Its pre-batch rule subtracts pending hydration plus those reserves before comparing with 48 GiB. Our current free-space snapshot does not reveal its next batch requirement. No other-project files or thresholds were modified, and its runner was not imported or executed. No custom memory threshold was found in the inspected constants; this is not evidence none exists elsewhere.

## Minimal Phase A budget and actual use

Single local Python audit at a time; no agents, parallel downloads, DuckDB, benchmarks or raw microdata scans. Standard-library CSV/XML parsing with a 128 MiB RSS ceiling checked after execution; the final successful audit used about 32.3 MiB RSS and 0.179 seconds internally. This is an observed audit measurement, not a production benchmark or a hard OS memory cap. Resource snapshots and the exact read-only guard-source hash are retained in `audit/phase3_resource_preflight.json`. The later load snapshot rose to 50.56/27.28/17.66; finish text review and the commit, with no further acquisition or computational pilot.

Budget: each cached CSV <2 MiB; each XLSX expanded metadata <8 MiB; new repository artifacts <2 MiB; optional source responses <=256 KiB per crosswalk, 512 KiB intended total successful payload; optional inline receipt <1 MiB. No package or environment installation. The source client used an already installed curl_cffi fallback after the standard client failed. Four sequential metadata requests (two files, two clients) all returned 403; zero crosswalk files accepted or retained. Error responses were not saved; network overhead is not claimed to be zero. Stop retries here.

Audit writes require free space >48 GiB +5 MiB and recheck immediately before outputs. This small audit safeguard does not replace the other project's stricter projection including its batch reserves. External load is high: keep work to text, code lists and cached aggregates; stop further acquisition or calculation if storage approaches the observed 48 GiB safeguard or memory pressure worsens materially.

## Completed Phase A artifacts

1. `docs/literature_matching_benchmarks.md`
2. `docs/occupation_unmatched_root_causes.md`
3. `docs/occupation_concordance_alternatives.md`
4. `docs/exposure_measurement_risk.md`
5. This plan.
6. `results/feasibility/occupation_resolution_priorities.csv`: all 62 groups, employment-ranked, provenance/uncertainty/approval fields.
7. `scripts/phase3/audit_cached_occupations.py`, `phase3_cached_audit.json`, official non-data-level code transcription, metadata-attempt log, controller/validation receipts.

Skills actually invoked: citation-management (primary-source bibliographic/method verification), data-analytics:analyze-data-quality (join-domain, residual missingness and denominator auditing), validate-data (independent arithmetic, source/aggregation and conclusion checks). Local reproducibility code provides the inspectable companion analysis; no new notebook or environment was needed. Tools: existing Python standard library, web primary sources, Git and authenticated gh. No delegation.

## Next phase, only after explicit approval

1. Freeze a score-domain and residual policy: preserve strict original coverage; optionally implement the disclosed available-specialty diagnostic as a separate sensitivity. Do not label it an exact score repair.
2. Approve the versioned 7640 exception and its unresolved residual treatment.
3. Obtain authentic historical NEM workbooks or a supplied copy under a new small explicit acquisition budget. Inspect row memberships, vintage, donor flags and cardinality. Produce long edge provenance and compare effective leaf weights.
4. Use cached Delaware aggregates to validate chosen variants, missingness, dispersion and rankings. Unit assertions should test domain classification, composite ancestry, conservation, source exception and missing-group bounds.
5. Re-evaluate the other project's current resource guards and projected needs. A national acquisition budget requires current free-storage threshold, memory headroom, explicit storage/retention and a sequential pilot. Do not repurpose the Phase 2 script's 2 GiB/two-thread settings for this concurrent-resource situation.
6. National ACS exposure processing needs a distinct explicit approval even if a small concordance repair is approved. Archived size metadata (2.239 GB compressed /10.384 GB expanded) is historical planning evidence, not a current download or permission.
7. Keep CZ provisional with a State alternative; a resource-constrained fallback must retain valid occupational scoring and documented geography. Mortgage treatment-effect estimation remains separately unauthorized.

## Controller recommendation and decisions

Retain the verified baseline. Twenty groups are score-policy candidates, 41 contain wholly unrepresented SOCs, and one requires both source correction and score policy. No remaining assumption-free score repair was confirmed. NEM promises documentary consistency, but its incremental coverage is unverified and can depend on pooling/imputation.

User decisions required before implementation: explicit Phase B authorization; available-specialty versus stricter residual policy; exception handling; equal-SOC/equal-child/external weighting; treatment age composition; whether an authentic NEM pilot is desired. National downloads, national calculation and mortgage regressions are not included in a small mapping authorization. Stop now at the audit handoff.
