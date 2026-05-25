# Consistency Review — claude-code-oauth-quota

**Auditor:** Independent internal-consistency reviewer (no prior context).
**Date:** 2026-05-24
**Scope:** README.md, analysis.md, citations.md, references/oauth-quota-surface.md.
**Inputs:** `C:/Users/jewza/source/cited-research/research/claude-code-oauth-quota/`.

---

## Summary Table

| Severity | Count | Items |
|----------|-------|-------|
| CRITICAL | 0     | —     |
| MODERATE | 1     | #1 README TL;DR row-1 inline labels appear swapped with citation numbers |
| MINOR    | 2     | #2 citations.md broken anchor to analysis.md §Q4; #3 minor heading-anchor differences across docs |

---

## Issue #1 — README TL;DR row-1 inline labels appear swapped with citation numbers

- **File:** `README.md`, line 14
- **Expected:** Inline bracket labels for docs should match the citation numbers they reference. Citations.md establishes `[1] = Authentication doc`, `[2] = Environment variables doc`.
- **Actual:** The row reads `[env-vars] [1] [auth] [2]`. Read positionally, this implies `env-vars = [1]` and `auth = [2]`. The reverse is true in citations.md (env-vars is [2], auth is [1]).
- **Likely intent:** The labels and numbers are intended as separate parallel references (both labels and both numbers, naming the same two docs in different orders). However, the rendered text is ambiguous and a reader following the brackets will get the mapping inverted.
- **Effect:** A reader using the bracketed labels to navigate to citations.md will hit the wrong entry.
- **Grade:** FAIL (MODERATE).
- **Status: RESOLVED.** Fix applied 2026-05-24: row 1 now reads `**Yes** — [1] (auth doc) + [2] (env-vars doc)`, pairing each citation number with its document name in the correct order.
- **Suggested fix:** Either drop the prose labels and use only the numbers (`[1] [2]`), or reorder to match: `[auth] [1] [env-vars] [2]`.

---

## Issue #2 — citations.md broken anchor link to analysis.md §Q4

- **File:** `citations.md`, line 186
- **Expected:** `[analysis.md §Q4](analysis.md#q4--token-rotation-on-refresh-behavior)` — anchor must match the analysis.md heading `## Q4 — Token rotation-on-refresh behavior`.
- **Actual:** `[analysis.md §Q4](analysis.md#q4--token-rotation-on-refresh)` — missing `-behavior` suffix; will not resolve to the heading.
- **Effect:** Markdown anchor will fail to scroll/jump to Q4 section.
- **Grade:** FAIL (MINOR).
- **Status: RESOLVED.** Fix applied 2026-05-24: anchor now ends `-behavior` and matches the heading slug.
- **Suggested fix:** Append `-behavior` so the anchor becomes `#q4--token-rotation-on-refresh-behavior`.

---

## Issue #3 — Stylistic phrasing variation for Q4 "unverified" caveat

- **Files:** README.md row 4, analysis.md Q4, references/oauth-quota-surface.md Q4.
- **Expected:** Per the audit prompt's contradiction-transparency check, the Q4 caveat should be surfaced clearly in all three files.
- **Actual:**
  - README: "**Rotates on each refresh (unverified by first-party docs).**"
  - analysis.md: "**Refresh token rotates on each refresh — unverified by first-party documentation.**"
  - references/oauth-quota-surface.md: "**Answer (with caveat): the refresh token rotates on each refresh.** **No first-party Anthropic documentation states this.**"
- **Effect:** Wording varies but the caveat is consistently and prominently disclosed in each file. Substance matches.
- **Grade:** PASS (informational; no fix required).
- **Status:** OPEN-INFO

---

## Items Verified Consistent

The following cross-file consistency checks PASSED:

1. **Token endpoint URL** — All three files: `POST https://platform.claude.com/v1/oauth/token`. Matches citation [10] (#54443).
2. **Authorization endpoint** — All three files: `https://claude.ai/oauth/authorize`. Matches citation [14] (#10715).
3. **CLI `client_id`** — All three files: `9d1c250a-e61b-44d9-88ed-5944d1962f5e`. Matches citation [14].
4. **Redirect URI** — All three files: `https://console.anthropic.com/oauth/code/callback`. Matches citation [14].
5. **PKCE method** — All three files: `code_challenge_method=S256`. Matches citation [14].
6. **Interactive scopes** — analysis.md and references: `user:file_upload user:inference user:mcp_servers user:profile user:sessions:claude_code`. Matches citation [12] (#42904 credentials.json shape).
7. **CI scopes (one observed flow)** — analysis.md and references: `org:create_api_key user:profile user:inference`. Matches citation [14] (#10715 log capture).
8. **OAuth access-token prefix** — analysis.md and references: `sk-ant-oat01-*`. Matches citation [15] (#28091).
9. **Console API-key prefix contrast** — analysis.md: `sk-ant-api03-*`. Matches citation [15].
10. **Admin API key prefix** — all three files: `sk-ant-admin...`. Matches citation [9] verbatim.
11. **Access-token lifetime** — README "~1-year"; analysis.md "one-year OAuth token" / "long-lived (~1-year)"; references "one-year OAuth token" quoted from [1]. Consistent.
12. **Agent SDK credit pool amounts** — analysis.md table and references both list: Pro $20, Max 5x $100, Max 20x $200, Team Standard $20 / Premium $100, Enterprise usage-based $20 / seat-based Premium $200. Matches citation [5] verbatim.
13. **Agent SDK credit-pool launch date** — analysis.md and references: June 15 2026. Matches citation [5].
14. **Agent SDK drain order** — analysis.md and references both quote "Agent SDK usage draws from your monthly credit before any other source." Matches citation [5].
15. **Agent SDK programmatic auth** — All three files agree: `ANTHROPIC_API_KEY`, not OAuth. Matches citations [4] and [15].
16. **Messages API rejects OAuth tokens** — analysis.md and references: verbatim `"OAuth authentication is currently not supported."` Matches citation [15].
17. **`anthropic-ratelimit-*` header family** — analysis.md table lists requests, tokens, input-tokens, output-tokens, priority, retry-after. Matches citation [8].
18. **Rate Limits API endpoint** — analysis.md and references: `GET https://api.anthropic.com/v1/organizations/rate_limits`. Matches citation [9].
19. **`/status` slash command** — All three files describe as "Monitor your remaining allocation." Matches citation [6].
20. **`apiKeyHelper` refresh semantics** — references quotes "called after 5 minutes or on HTTP 401 response." Matches citation [1].
21. **Changelog v2.1.118 quote** — README, analysis.md, and references all reference the changelog text "Fixed OAuth token refresh failing when the server revokes a token before its local expiry time." Matches citation [13] (#52202).
22. **Issue references** — #54443 [10], #24317 [11], #42904 [12], #52202 [13], #10715 [14], #28091 [15], #33820 [16]. All number-to-issue mappings consistent across files.
23. **Citation spot-check (12 of 16 numbered citations verified, ≥75%):** [1], [2], [4], [5], [6], [8], [9], [10], [11], [12], [13], [14], [15], [16] all point to the correct entry in citations.md when used in analysis.md and references. (Citations [3] and [7] are not cited inline anywhere — they are background sources only; this is acceptable and noted, not a defect.)
24. **Q4 T1-gap transparency** — All three files surface "no first-party doc" / "unverified" for Q4. README row 4, analysis.md Limitations section, references Q4 + Gaps section. Pass.
25. **Q3 T1-gap transparency** — All three files surface "no first-party endpoint" for subscription quota. README row 3, analysis.md Q3, references Q3 + Gaps section. Pass.
26. **Q2 doc-gap transparency** — All three files note the refresh endpoint URL is observed in CLI logs, not documented. Anthropic issue #52202 cited as acknowledgment. Pass.
27. **Cross-file markdown links** —
    - README → analysis.md, citations.md, references/oauth-quota-surface.md, audit/citation-audit.md, audit/consistency-review.md: paths valid for topic-root layout.
    - analysis.md → citations.md, references/oauth-quota-surface.md (with anchors), audit/: paths valid.
    - references/oauth-quota-surface.md → ../citations.md: correct relative path from references/ subdir.
    - All anchors verified except the one flagged in Issue #2.
28. **`--bare` mode exclusion** — analysis.md Q1 and references Q1 both state `--bare` mode does not read `CLAUDE_CODE_OAUTH_TOKEN`. Matches citation [1].
29. **Three-environment-variable triad** — `CLAUDE_CODE_OAUTH_TOKEN` / `CLAUDE_CODE_OAUTH_REFRESH_TOKEN` / `CLAUDE_CODE_OAUTH_SCOPES` named consistently across README, analysis, references, and citations.

---

## Methodology

1. Read all four markdown files in full.
2. Built mapping of citation numbers [1]-[16] from citations.md (16 total: 9 T1, 7 T2).
3. Spot-checked 14 of 16 numbered citations for accurate file ↔ citation pairing in analysis.md and references (87.5% — exceeds 50% requirement).
4. Compared numerical claims (credit pool $, lifetimes, scope lists, client_id, URLs) across all three claim-bearing files.
5. Verified caveat / "unverified" / "no first-party" markers appear consistently for Q3 and Q4.
6. Validated relative markdown link targets and anchors against directory structure.

---

## Disposition

- **CRITICAL issues blocking publication:** 0
- **MODERATE issues to fix:** 1 (README label/citation-number ordering) — **RESOLVED**
- **MINOR issues to fix:** 1 (citations.md broken anchor) — **RESOLVED**
- **Phrasing variation noted but acceptable:** 1

Both flagged issues resolved 2026-05-24. No remaining blockers.
