# Additive original-repository integration plan

The local review branch descends from feasibility commit `3f363bca62b6d8938ee8f95696465361d2092476`. The named original remote is inaccessible in this run. Local commits do not establish remote integration.

1. In an authenticated checkout of `ZhenghuiQu/genai-entry-jobs-mortgage`, inspect its status, remotes, default branch, history and AGENTS.md. Preserve all preexisting research/review files. Do not put credentials in commands or files.
2. Add this local checkout as a filesystem remote and fetch its review branch. Compare trees and histories; the local feasibility commit is a root commit and remote ancestry is currently unknown.
3. Create an original-repository review branch from its verified default branch, using the `codex/` prefix.
4. If shared ancestry and nonconflicting changes are established, review the two patches and cherry-pick the required feasibility and Phase 2 changes without rewriting remote commits.
5. If histories are unrelated or files conflict, use additive integration: import missing feasibility scripts, five Markdown reports, test records and manifests under inspected paths; integrate updated sections into existing reports; preserve original literature files under their existing identities. Do not copy this checkout's `.git`, `data`, `.venv`, unrelated files or credential stores. Do not replace remote reviews with the local literature package.
6. Record the original local hash above and new local Phase 2 commit in the remote provenance manifest. Compare copied file hashes to `phase2_artifact_manifest.json`. Review the resulting diff, run offline validation, and commit only inspected code/documents/aggregate evidence.
7. An ordinary reviewed branch push is possible only after authentication and successful comparison. Never force-push, overwrite the remote default branch, merge automatically, or claim missing research documents were inspected.

Remote integration status: **OPEN**. No remote files or history were modified by this run.
