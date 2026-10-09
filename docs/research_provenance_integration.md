# Research Provenance Integration

Date: 2026-10-09 (Asia/Shanghai). This document is a Phase 2 audit, not an implementation or treatment-effect report. Mapping release: **PROVISIONAL_AUDIT_NOT_FINAL**. Recommendation **C**.

## Repository reconciliation

The initial local Git tree was clean at `3f363bca62b6d8938ee8f95696465361d2092476` on `feasibility-handoff`, with origin pointing to the requested [existing repository](https://github.com/ZhenghuiQu/genai-entry-jobs-mortgage). It contains 61 tracked files and a root handoff commit; there is no observed original remote history locally. The new review branch is `codex/phase2-exposure-repair`, descended from the handoff commit. Original feasibility scripts, five reports, 23 structured test records and all manifests are preserved; reports receive explicit current Phase 2 updates and their Day 1–2 contents remain labeled as archived evidence.

GitHub connector authentication succeeds for account EHeroLibertyMan. The requested repository metadata request returns 404; the connector lists no accessible repositories for owner ZhenghuiQu. `gh` is not installed. Sandboxed Git initially fails DNS; network-enabled `git ls-remote` reaches GitHub but cannot read an HTTPS username in noninteractive mode. These tests establish current inaccessibility, not repository nonexistence. Remote branches, AGENTS.md, documents and commit history cannot be compared. No clone, remote integration, cherry-pick, force push, history rewrite or deletion of unrelated files is claimed.

Local implementation can be committed after diff/credential review to preserve work, but that is not a commit on the inaccessible existing remote. R01 remains OPEN. `audit/phase2_integration_plan.md` gives a concrete additive integration sequence for an authenticated checkout; if remote histories are unrelated, copy only inspected changes and record this original base hash rather than replacing the remote tree.

## Document availability

| document | availability |
| --- | --- |
| Research assignment PDF | MISSING in scoped local search; remote inaccessible |
| Independent GPT review | MISSING |
| Independent Claude review | AVAILABLE: eight literature/*.md files, original hashes revalidated |
| Complete GPT–Claude cross-review | MISSING; treatment-window recommendation known only from current user instruction |
| Separate Claude-only State audit | MISSING; distinct from available independent Claude review |

The scoped search examined the workspace, Desktop filenames and attachments; it did not inspect unrelated research contents. No missing document is fabricated. All eight available literature files must match their original stored hashes. The available Claude literature package recommends CZ and an industry-exposure fallback; this does not establish the contents of the missing separate State audit or full cross-review. The current user request controls the continuation.

## Source/version and interaction record

`audit/phase2_request.txt` preserves the supplied Phase 2 instruction. Current source attempts append to `source_manifest.jsonl`; historical entries are not edited. New BLS/CT evidence is explicitly labeled complete web-text extraction, with URL, line coverage and representation hashes. Existing official Census/O*NET/DE/Dorn data retain the original manifests and SHA-256 checks. Phase 2 source hashes and derived-file hashes live in `phase2_artifact_manifest.json`; this supplements, not replaces, Day 1–2 manifests. Test records and gate outputs preserve failures and unresolved choices as well as passes.

Skills actually used: `data-analytics:analyze-data-quality` for hierarchy/completeness/join/missingness checks; `validate-data` for denominators, independent arithmetic and limits on conclusions; `query` for bounded ad-hoc DuckDB aggregations, using the installed Python DuckDB API because the CLI is absent. `panel-data-rules` was inspected but its CRSP/Compustat rules were not applicable or invoked. No occupation-taxonomy-specific, Git-history-specific, or research-provenance-specific skill was available in the inspected catalog; those tasks use official sources, normal Git tools and explicit audit manifests. No subagents were requested or used.

## Overall judgment

Methodological validity: official membership and CT bridging improve, but scores still require unknown internal-share and missing-rating assumptions; source documents cannot authenticate the primary treatment window. Technical feasibility: local streaming/DuckDB and exact CT CZ linkage work; national acquisition and original-repository access remain unavailable. Research-time constraints: no current author deadline is supplied, so C is not justified by an invented one-week limit. These unresolved exposure/provenance dependencies require recommendation C even though CT linkage now passes its bounded validation.
