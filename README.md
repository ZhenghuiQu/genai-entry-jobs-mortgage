# Generative AI, Entry-Level Employment, and US Mortgage Markets: feasibility handoff

## Current Phase 2 audit

Recommendation **C**. Start with [the controller report](audit/phase2_controller_report.md) and [Phase 2 decisions](docs/phase2_decision_register.md). Official SOC hierarchy repair improves strict DE coverage to 82.994% (22–34) / 82.988% (25–34). An official CT bridge recovers 98.979% / 99.058% of the existing 2024/2025 CT purchase-originations samples. National ACS downloads currently return 403; original-repository access and four research documents remain unavailable. State fallback does not fix the shared exposure dependency.

The contractual `occupation_mapping_final.csv` is marked **PROVISIONAL_AUDIT_NOT_FINAL**. National CSV entries are unobserved with blank numeric metrics. `make phase2-analyze` regenerates currently available offline Phase 2 diagnostics; `make phase2-validate` checks arithmetic, schemas, original source/literature hashes and scope. `make phase2-acquire` attempts only official Phase 2 inputs and the compressed national ACS baseline; it expands no person CSVs or HMDA snapshots. The national processing branch has not been exercised while download access remains unavailable.

Five new Phase 2 documents accompany labeled updates in the original five reports. Existing literature and historical test/manifests remain preserved. Original feasibility commit `3f363bc` is an ancestor of local branch `codex/phase2-exposure-repair`; local commits do not imply integration into the inaccessible original remote. See [additive integration plan](audit/phase2_integration_plan.md).

## Archived Day 1–2 handoff

The following records describe the earlier audit. Current Phase 2 findings above and the labeled report updates supersede historical occupation, CT and resource conclusions.


This workspace contains Day 1–2 feasibility validation only. Start with [the feasibility report](docs/feasibility_gate_report.md). Recommendation **C**: exposure concordance/national weighted coverage and research-document provenance remain unresolved. CZ is still provisional; State remains the user's pre-specified fallback. No treatment coefficients, significance tests, national full-download pipeline, mechanism estimates, robustness analysis, or paper were produced.

## Required documents

- [Feasibility gate report](docs/feasibility_gate_report.md)
- [Source registry](docs/data_source_registry.md)
- [Geography audit](docs/geography_audit.md)
- [Occupation crosswalk audit](docs/occupation_crosswalk_audit.md)
- [Pending design decisions](docs/design_decisions_pending.md)

The original eight independent Claude review files are preserved in `literature/`. The original assignment PDF, GPT review and two distinct cross-review documents were not available locally. The requested remote repository is inaccessible to the attempted clone/connector; this workspace did not initially have Git history. See [repository access evidence](audit/repository_access.md). A local handoff commit does not replace or join the existing remote history. Do not force-push it as a replacement repository.

## Reproduce

Use Python 3.13 on this machine. Public network access is required for acquisition; no API credentials are required for the demonstrated bulk routes. Census's no-key value API returned an HTML Missing Key page, and the scripts use the verified bulk-summary alternative.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install --cert /etc/ssl/cert.pem -r scripts/feasibility/requirements.lock.txt
make feasibility
```

On a system without `/etc/ssl/cert.pem`, use its trusted CA configuration instead of that pip flag. Certificate verification must remain enabled. The tested successful HMDA client is curl-cffi 0.13.0 with Chrome-compatible TLS; default urllib/curl were denied HTTP 403. The project-local virtual environment is ignored.

To regenerate audits from already downloaded, ignored samples without network acquisition:

```sh
make feasibility-analyze
```

The scripts explicitly cap every response, require HTTP 206 for national ZIP ranges, and never download a national HMDA or PUMS dataset. The HMDA prefix is 262,144 bytes and ZIP tail 65,536 bytes per year. Four CT purchase-origination extracts are capped at 35 MB each; the DE PUMS and QWI files are small complete state files. National PUMS retrieval is metadata and ZIP directory only. Some noncritical attempted documentation URLs fail; those failures are preserved rather than treated as evidence. A failed required source leaves the gate unresolved and may prevent offline regeneration.

## Evidence and retention

`results/feasibility/` contains version/header/code/count summaries, explicit occupation mapping diagnostics, unmatched/ambiguous groups, resource measurements, 23 structured test records, a sanitized append-only source manifest and hash validation results. Downloaded bodies live only under ignored `data/`. Derived audit CSVs are aggregate/mapping outputs, not individual loan/person records. Response cookies and authorization headers are removed from committed metadata. No credentials are read or committed.

`audit/day_1_2_request.txt` preserves the exact supplied request; `audit/interaction_audit.md` records decisions, corrections and the limit of the exported interaction record. The app's native conversation remains the complete available interaction trail; this summary is not represented as a full transcript export.

The sample benchmark aggregates only county × age × action counts and checks every count against independent Python CSV arithmetic. It does not estimate any treatment effect. Strict occupational mapping covers 71.178% and 71.530% of young DE employment, not the national population. Numeric SOC groups, unrated members and the Census group-7640 invalid source member remain unresolved. Those groups are not assigned by prefix or wildcard.

Stop after these gates. Do not extend this Makefile into a national regression/robustness/paper pipeline without a subsequent implementation instruction.
