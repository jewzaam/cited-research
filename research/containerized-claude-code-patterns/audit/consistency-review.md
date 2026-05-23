# Consistency review report

Review date: 2026-05-23. Review agent: independent, no research-conversation context. Files read fresh via Read tool.

## Cross-file consistency checks

| ID | Check | Result |
|---|---|---|
| C1 | Auto-mode classifier performance table consistent across deliverable and reference | **FAIL → Status: RESOLVED** (see Fix C1) |
| C2 | Auto-mode availability constraints (model + provider) consistent | PASS |
| C3 | CVE-2025-66479 version range consistent across files | **FAIL → Status: RESOLVED** (see Fix C3) |
| C4 | SOCKS5 affected/patch version consistent | **FAIL → Status: RESOLVED** (see Fix C4) |
| C5 | GitHub App installation token "1 hour" lifetime consistent | PASS |
| C6 | Fine-grained PAT max lifetime (366 days) consistent | PASS |
| C7 | Anthropic Tier-1 Sonnet rate-limit numbers consistent | PASS |
| C8 | Recommendation hierarchy (auto mode preferred over dangerous flag) consistent | PASS |
| C9 | Bedrock/Vertex loses auto-mode statement consistent | PASS |
| C10 | GitHub App = lowest blast radius verdict consistent | PASS |
| C11 | Path C anti-pattern description consistent (minor: ref file lists 6th element "root user" that deliverable omits) | PASS — non-contradictory; ref file has more detail |
| C12 | Research date 2026-05-23 consistent | PASS |
| C13 | Citation numbers spot-check (10 sampled) | PASS |
| C14 | Inter-file markdown links use relative paths | PASS |
| C15 | NODE_OPTIONS + memory-limit pairing consistent | PASS |
| C16 | s1ngularity attack description (Aug 26 2025; flag-as-payload) consistent | PASS — ref file includes Nx package name + additional flags (`--yolo`, `--trust-all-tools`); deliverable abbreviated. Non-contradictory. |
| C17 | Harness-detection $200 incident details (On Patel, Max 20x, hermes.md/OpenClaw) consistent | PASS |
| C18 | "Two paths" framework consistently presented | PASS |
| C19 | Logical: Path B (Bedrock + dangerous flag) + in-container `init-firewall.sh` compatibility | PASS |
| C20 | Reference Dockerfile snippet matches Anthropic-official description | PASS |

## Recommended fixes (consistency)

- **Fix C1 — Restore Stage-1 FNR column in deliverable's auto-mode table.** Reference file (`anthropic-guidance.md` §1.3) and citations.md [7] include "Stage 1 FNR: 1.8%" for synthetic exfil dataset; deliverable §1 had only 3 columns and silently dropped this metric. **Status: RESOLVED** — deliverable §1 table expanded to 4 columns (Stage 1 FPR, Stage 1 FNR, Full pipeline FPR, Full pipeline FNR) with 1.8% restored to the synthetic-exfil row.

- **Fix C3 — Split conflated CVE ranges in deliverable §0 point 4.** Original text grouped CVE-2025-66479 + SOCKS5 into one v2.0.24–v2.1.89 range. CVE-2025-66479 was patched at v2.0.55 (Nov 2025); the v2.0.24–v2.1.89 range belongs only to the SOCKS5 bug per [24], [25] and `dangerously-skip-permissions.md` §5.2. **Status: RESOLVED** — deliverable §0 point 4 rewritten to separate CVE-2025-66479 (launch through v2.0.54, patched v2.0.55) from SOCKS5 (Oct 20 2025 sandbox GA through v2.1.88 patch).

- **Fix C4 — Remove unsupported SOCKS5 patch version "v2.1.90".** citations.md [25] lists only v2.1.88 patch; deliverable + `dangerously-skip-permissions.md` had "v2.1.88/v2.1.90". The v2.1.90 co-patch is not in the cited SecurityWeek source. **Status: RESOLVED** — deliverable §5 line removed v2.1.90; `dangerously-skip-permissions.md` §5.2.2 Patched row simplified to "v2.1.88 (Mar 31 2026)". The "v2.0.24" specific GA version number was also removed since not in source; replaced with "sandbox GA (Oct 20 2025)".

- **Auxiliary — Harness-detection scope wording in `community-dockerfiles.md` §2.5.8.** The reference file said detection "scans git commit messages, branch names, and staged changes" — broader than what citation [17] supports (citation says "git status content"). **Status: RESOLVED** — rewritten to "git-status content (which includes staged changes, branch state, and recent commit information)" with explicit "per [17]" attribution.

- **Auxiliary — ~130-releases claim qualification.** `dangerously-skip-permissions.md` §5.2.2 stated "affected period ~5.5 months, ~130 Claude Code releases" — the ~130 figure derives from npm release history during the window, not from the SecurityWeek source. **Status: RESOLVED** — qualifier added: "The ~130-release figure comes from npm version history across the affected window and is not in the SecurityWeek source; treat as approximate."

## Other consistency findings (auditor's discretion)

- **Path C anti-pattern element ordering** differs between deliverable §5 (5 elements) and `dangerously-skip-permissions.md` §5.6 (6 elements — includes "root user, which Claude Code refuses anyway"). The reference file's extra element is structurally redundant (the dangerous flag refuses root anyway per [2], [15]). **Status: ACCEPTED** — not a contradiction; reference file is more thorough but both convey "do not do this."

- **s1ngularity flag list** — `dangerously-skip-permissions.md` §5.2.4 enumerates `--dangerously-skip-permissions`, `--yolo`, `--trust-all-tools` from [16]; deliverable §0 mentions only the first. **Status: ACCEPTED** — deliverable abbreviates appropriately for the gating-findings section; reference file carries the full list.

- **Source count claim** (deliverable Appendix: "30 numbered primary sources + 14 advisory-tier sources") — verified against citations.md: [1]–[30] = 30 primary; [31a]–[44a] = 14 advisory. Consistent.

## Summary

20 consistency checks performed; 4 FAIL → all **RESOLVED** via edits applied 2026-05-23. 2 auxiliary clarifications also applied. No remaining internal contradictions detected.
