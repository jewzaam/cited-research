# Citation Audit — claude-code-oauth-quota

Audit date: 2026-05-24
Auditor: independent (no context from research conversation)
Method: each numbered citation re-read against the matching pre-fetched source file.

## Summary

| Grade | Count |
|-------|-------|
| VERIFIED | 14 |
| PARTIAL | 2 |
| INACCURATE | 0 |
| INACCESSIBLE | 0 |
| DRIFT | 0 |
| NOT FOUND | 0 |
| **Total** | **16** |

Two PARTIAL grades:
- [3] — cited for "pointer to /en/authentication for auth setup; `claude --version` and `claude doctor` for verification"; the fetched excerpt confirms the auth-page pointer but does not include `claude --version` or `claude doctor` text. Low impact: [3] is only used as a minor pointer and the missing detail is not load-bearing for any Q1-Q4 claim.
- [7] — used only to support the "shared usage limit across surfaces" statement; verified. But the deliverable does not actually depend on [7] for any Q1-Q4 specific claim; it is cited mainly in citations.md itself. The single sentence carried over is supported. (Marked PARTIAL only because the deliverable's use of [7] is decorative rather than load-bearing; the support quotation itself is correct.)

All four high-stakes claims flagged for special attention verified directly:
- "OAuth access token" wording for `CLAUDE_CODE_OAUTH_TOKEN` and "OAuth refresh token" wording for `CLAUDE_CODE_OAUTH_REFRESH_TOKEN` — both verbatim in [2].
- Refresh endpoint `POST https://platform.claude.com/v1/oauth/token` — verbatim in [10].
- "Admin API key required" on Rate Limits API — verbatim in [9].
- No first-party REST endpoint exposes subscription quota — confirmed by absence across [5], [6], [7], [8], [9].
- 1-year token lifetime from [1] — verbatim "one-year OAuth token".
- Token prefix `sk-ant-oat01-*` from [15] — verbatim.
- Rotation evidence in [11] and [10] — both quoted accurately.

---

## [1] Authentication doc

**URL:** https://code.claude.com/docs/en/authentication
**Grade:** VERIFIED

**Claims in deliverable:**
- `claude setup-token` generates "a one-year OAuth token" for CI use
- Credential storage paths (macOS Keychain / `~/.claude/.credentials.json` / `%USERPROFILE%\.claude\.credentials.json`)
- `apiKeyHelper` refresh "called after 5 minutes or on HTTP 401 response", `CLAUDE_CODE_API_KEY_HELPER_TTL_MS`
- Full credential-precedence list (6 entries)
- Token "scoped to inference only and cannot establish Remote Control sessions"
- `--bare` mode does not read `CLAUDE_CODE_OAUTH_TOKEN`
- Agent SDK credit-pool transition note for June 15 2026

**Evidence in source:**
- "generate a one-year OAuth token with `claude setup-token`" — present verbatim
- "On macOS, credentials are stored in the encrypted macOS Keychain... On Linux, credentials are stored in `~/.claude/.credentials.json` with file mode `0600`... On Windows, credentials are stored in `%USERPROFILE%\.claude\.credentials.json`" — present verbatim
- "by default, `apiKeyHelper` is called after 5 minutes or on HTTP 401 response. Set `CLAUDE_CODE_API_KEY_HELPER_TTL_MS` environment variable for custom refresh intervals" — present verbatim
- Precedence list 1-6 — present verbatim
- "It is scoped to inference only and cannot establish Remote Control sessions" — present verbatim
- "Bare mode does not read `CLAUDE_CODE_OAUTH_TOKEN`" — present verbatim
- "Starting June 15, 2026, Agent SDK and `claude -p` usage on subscription plans will draw from a new monthly Agent SDK credit" — present verbatim

All claims from [1] are exact-text matches. No drift.

---

## [2] Environment variables doc

**URL:** https://code.claude.com/docs/en/env-vars
**Grade:** VERIFIED

**Claims in deliverable (the decisive Q1/Q4 source):**
- `CLAUDE_CODE_OAUTH_TOKEN` is "OAuth **access token** for Claude.ai authentication"
- `CLAUDE_CODE_OAUTH_REFRESH_TOKEN` is "OAuth refresh token for Claude.ai authentication"
- `CLAUDE_CODE_OAUTH_SCOPES` "Required when `CLAUDE_CODE_OAUTH_REFRESH_TOKEN` is set"

**Evidence in source (verbatim):**
- `CLAUDE_CODE_OAUTH_TOKEN`: "OAuth access token for Claude.ai authentication. Alternative to /login for SDK and automated environments. Takes precedence over keychain-stored credentials. Generate one with claude setup-token"
- `CLAUDE_CODE_OAUTH_REFRESH_TOKEN`: "OAuth refresh token for Claude.ai authentication. When set, claude auth login exchanges this token directly instead of opening a browser. Requires CLAUDE_CODE_OAUTH_SCOPES."
- `CLAUDE_CODE_OAUTH_SCOPES`: "Space-separated OAuth scopes the refresh token was issued with... Required when CLAUDE_CODE_OAUTH_REFRESH_TOKEN is set"

The high-stakes verbatim wording for "access token" vs "refresh token" is exact. Q1 classification is entailed by the source.

---

## [3] Advanced setup doc

**URL:** https://code.claude.com/docs/en/setup
**Grade:** PARTIAL

**Claim in deliverable:**
- "pointer to `/en/authentication` for auth setup; `claude --version` and `claude doctor` for verification; no additional OAuth detail"

**Evidence in source:**
- "After installing, log in by running `claude` and following the browser prompts. See Authentication for all account types and team setup options." — confirms the auth-page pointer.
- The fetched excerpt does NOT contain text about `claude --version` or `claude doctor` for verification — the fetched file says only that the "Page primarily covers installation, OS support, version pinning, signing keys."

**Notes:** The deliverable's description of [3] (citations.md line 41) mentions `claude --version` and `claude doctor`; those phrases do not appear in the fetched excerpt. The fetched excerpt is itself a curated subset, not a full mirror, so the original page may contain them. The deliverable does not lean on [3] for any Q1-Q4 substantive claim — [3] is only used as an auth-page pointer. PARTIAL because the auxiliary detail in citations.md is not directly entailed by the fetched evidence.

---

## [4] Agent SDK overview

**URL:** https://code.claude.com/docs/en/agent-sdk/overview
**Grade:** VERIFIED

**Claims in deliverable:**
- Agent SDK auth = `ANTHROPIC_API_KEY` (or cloud-provider env var)
- Verbatim restriction quoted: "Unless previously approved, Anthropic does not allow third party developers to offer claude.ai login or rate limits for their products, including agents built on the Claude Agent SDK. Please use the API key authentication methods described in this document instead."
- No quota API endpoint mentioned

**Evidence in source:**
- "Set your API key — Get an API key from the Console, then set it as an environment variable: export ANTHROPIC_API_KEY=your-api-key" — present
- Restriction quoted verbatim — present exact word-for-word
- "No CLAUDE_CODE_OAUTH_TOKEN reference / No token refresh endpoint / No quota API endpoint / No subscription credit-balance API" — confirmed by fetched note that these are explicitly absent

The verbatim quote is exact match. VERIFIED.

---

## [5] Agent SDK plan article

**URL:** https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan
**Grade:** VERIFIED

**Claims in deliverable:**
- Monthly credit pool: Pro $20, Max 5x $100, Max 20x $200, Team Standard $20, Team Premium $100, Enterprise usage-based $20, Enterprise seat-based Premium $200
- Drain order: "Agent SDK usage draws from your monthly credit before any other source"
- Zero credit behavior: flows to usage credits at standard API rates if enabled; otherwise stops
- Monthly reset at billing cycle, no rollover
- Interactive Claude Code continues to use existing 5-hour/weekly limits
- No API endpoint documented for credit balance

**Evidence in source (verbatim):**
- All seven plan/credit values match exactly
- "Agent SDK usage draws from your monthly credit before any other source." — exact
- "When your monthly credit runs out, additional Agent SDK usage flows to usage credits at standard API rates—but only if you've enabled usage credits. If usage credits aren't enabled, Agent SDK requests stop until your credit refreshes." — exact
- "Your credit resets at the start of each billing cycle. Unused credits don't roll over to the next billing cycle." — exact
- "Agent SDK and `claude -p` usage no longer counts toward your Claude plan's usage limits" / "Interactive Claude Code in the terminal or IDE" continues — exact
- "API endpoint for credit balance: Not mentioned" — confirmed absence

All numbers and quotes match. VERIFIED.

---

## [6] Pro/Max Claude Code article

**URL:** https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan
**Grade:** VERIFIED

**Claims in deliverable:**
- `/status` is "the surface for 'Monitor your remaining allocation'"
- "usage limits are shared across Claude and Claude Code"
- `ANTHROPIC_API_KEY` precedence warning
- No quota REST endpoint mentioned

**Evidence in source:**
- "`/status` — described as 'Monitor your remaining allocation'" — present verbatim
- "usage limits are shared across Claude and Claude Code, meaning all activity in both tools counts against the same usage limits" — present verbatim
- "If you have an ANTHROPIC_API_KEY environment variable set on your system, Claude Code will use this API key for authentication instead of your Claude subscription..." — present verbatim
- "What is NOT specified: ... Specific API endpoints for quota exposure" — confirms the absence claim

VERIFIED.

---

## [7] Usage and length limits article

**URL:** https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work
**Grade:** PARTIAL

**Claims in deliverable (citations.md only):**
- "your usage of all different Claude product surfaces (claude.ai, Claude Code, Claude Desktop) counts towards the same usage limit"
- Page does not enumerate 5-hour window mechanics or quota visibility surfaces

**Evidence in source:**
- "your usage of all different Claude product surfaces (claude.ai, Claude Code, Claude Desktop) counts towards the same usage limit" — exact verbatim match
- "What is NOT in this article: 5-hour window details / Weekly reset details / Specific UI surfaces for remaining quota / API endpoints for quota checking" — confirms the absence claim

**Notes:** The single quote and the absence claim are both verified. PARTIAL is assigned only because [7] is cited in citations.md but is not actually load-bearing for any Q1-Q4 conclusion in analysis.md or README.md — it functions as supporting absence-of-evidence material. The quotation itself is correctly attributed.

(Could equally be graded VERIFIED — the attributed text is exact. PARTIAL reflects auxiliary use only; no misrepresentation.)

---

## [8] Rate limits doc

**URL:** https://platform.claude.com/docs/en/api/rate-limits
**Grade:** VERIFIED

**Claims in deliverable:**
- Full `anthropic-ratelimit-*` response-header table (requests/tokens/input-tokens/output-tokens, each with limit/remaining/reset)
- `anthropic-priority-*` headers for Priority Tier
- Token-bucket algorithm
- 429 + `retry-after` behavior
- Headers describe API-tier rate limits (not subscription quota)
- Tokens-remaining "rounded to nearest 1000"

**Evidence in source:**
- "The API uses the token bucket algorithm to do rate limiting" — verbatim
- All header families enumerated in fetched excerpt (anthropic-ratelimit-requests-*, -tokens-*, -input-tokens-*, -output-tokens-*, plus anthropic-priority-*)
- "anthropic-ratelimit-tokens-remaining (rounded to nearest thousand)" — confirms the rounding claim
- "If you exceed any of the rate limits you will get a 429 error... along with a retry-after header" — verbatim
- "Scope of page: API-level rate limits, organization-level, by usage tier (Tier 1-4). NOT subscription quota." — confirms the boundary claim

All claims match exactly. VERIFIED.

---

## [9] Rate Limits API

**URL:** https://platform.claude.com/docs/en/build-with-claude/rate-limits-api
**Grade:** VERIFIED

**Claims in deliverable (high-stakes auth claim):**
- Endpoint paths: `GET https://api.anthropic.com/v1/organizations/rate_limits` and per-workspace variant
- "Admin API key required" verbatim
- Admin keys start with `sk-ant-admin...`
- Returns configured rate limits per model group / batch / files
- Does NOT return current consumption or subscription counters

**Evidence in source (verbatim):**
- "Admin API key required. This API is part of the Admin API. These endpoints require an Admin API key (starting with sk-ant-admin...) that differs from standard API keys. Only organization members with the admin role can provision Admin API keys through the Claude Console." — exact match for the high-stakes auth claim
- Both endpoint paths present
- "Returns: Configured rate limit values per group (requests_per_minute, input_tokens_per_minute, output_tokens_per_minute). Does NOT return current consumption."
- "NOT covered: Subscription quota (5-hour / weekly counters) / Agent SDK credit pool balance / Current consumption against the configured limits"

The "Admin API key required" wording is exact verbatim. VERIFIED.

---

## [10] Issue #54443

**URL:** https://github.com/anthropics/claude-code/issues/54443
**Grade:** VERIFIED

**Claims in deliverable (highest-stakes URL):**
- Refresh endpoint URL `POST https://platform.claude.com/v1/oauth/token` captured from Claude Code 2.1.121 debug logs
- HTTP 400 response on refresh after early 401
- Linux x86_64, Max subscription
- References #52202 and #24317

**Evidence in source (verbatim):**
- "POST https://platform.claude.com/v1/oauth/token returns HTTP 400" — verbatim in log lines
- Multiple log timestamps captured: "2026-04-28T19:58:53.736Z OAuth refresh attempt: POST https://platform.claude.com/v1/oauth/token -> 400" — exact
- "Claude Code version: 2.1.121" / "OS: Ubuntu 25.10, Linux x86_64" / "Auth mode: Claude.ai OAuth / Max subscription, not API-key billing" — verbatim
- "This appears related to the early-revocation refresh path discussed in #52202 and potentially to the concurrent-session refresh-token race described in #24317" — verbatim

The most critical claim of the entire deliverable (the refresh endpoint URL) is directly entailed by verbatim log text in the source. VERIFIED.

---

## [11] Issue #24317

**URL:** https://github.com/anthropics/claude-code/issues/24317
**Grade:** VERIFIED

**Claims in deliverable (Q4 T2 evidence):**
- `~/.claude/.credentials.json` shape includes `accessToken`, `refreshToken`, `expiresAt`
- Access token ~15h per reporter
- Reporter analysis: "OAuth refresh tokens are typically single-use: when one process uses the refresh token to get a new access/refresh token pair, the old refresh token is invalidated server-side."
- Reproducible race when N concurrent processes share credential file

**Evidence in source (verbatim):**
- Reporter analysis quote — verbatim exact: "OAuth refresh tokens are typically single-use: when one process uses the refresh token to get a new access/refresh token pair, the old refresh token is invalidated server-side. With N concurrent Claude Code processes: 1. Process A's access token expires..."
- Credentials shape: "accessToken — short-lived (~15 hour expiry), refreshToken — used to obtain new access tokens"
- "Subscription: Team (Max 5x tier)" / "Concurrent sessions: 7-12 active Claude Code processes" — confirms the multi-process repro context

The deliverable correctly characterizes this as community analysis on a first-party repo (not Anthropic's own statement). VERIFIED.

---

## [12] Issue #42904

**URL:** https://github.com/anthropics/claude-code/issues/42904
**Grade:** VERIFIED

**Claims in deliverable:**
- Sanitized credentials shape including `claudeAiOauth.accessToken`, `refreshToken`, `expiresAt`, scopes array, `subscriptionType`, `rateLimitTier`
- Scopes list: `user:file_upload`, `user:inference`, `user:mcp_servers`, `user:profile`, `user:sessions:claude_code`
- Interactive `/login`-issued access tokens observed at ~24-hour TTL

**Evidence in source (verbatim):**
- Exact JSON structure present with scopes list matching exactly
- "the access token has a TTL of approximately 24 hours (confirmed via the expiresAt field)"

All claims match. VERIFIED.

---

## [13] Issue #52202

**URL:** https://github.com/anthropics/claude-code/issues/52202
**Grade:** VERIFIED

**Claims in deliverable:**
- Verbatim Anthropic changelog v2.1.118: "Fixed OAuth token refresh failing when the server revokes a token before its local expiry time."
- Issue body confirms env-vars page documents the three OAuth env vars
- Open documentation gap

**Evidence in source (verbatim):**
- "Fixed OAuth token refresh failing when the server revokes a token before its local expiry time" — exact verbatim
- "https://code.claude.com/docs/en/env-vars Documents CLAUDE_CODE_OAUTH_REFRESH_TOKEN, CLAUDE_CODE_OAUTH_SCOPES, and CLAUDE_CODE_OAUTH_TOKEN without explaining the refresh lifecycle" — confirms env-vars list
- "[DOCS]" prefix and OPEN state, area:auth+documentation+enhancement labels — confirms open doc gap framing

VERIFIED.

---

## [14] Issue #10715

**URL:** https://github.com/anthropics/claude-code/issues/10715
**Grade:** VERIFIED

**Claims in deliverable:**
- OAuth authorize URL: `https://claude.ai/oauth/authorize`
- `client_id=9d1c250a-e61b-44d9-88ed-5944d1962f5e`
- `redirect_uri=https://console.anthropic.com/oauth/code/callback`
- `code_challenge_method=S256`
- Scopes observed in this flow: `org:create_api_key user:profile user:inference`

**Evidence in source:**
- The full authorize URL captured verbatim with all parameters matching exactly
- Decoded values listed: "Authorize endpoint: https://claude.ai/oauth/authorize / client_id: 9d1c250a-e61b-44d9-88ed-5944d1962f5e / redirect_uri: https://console.anthropic.com/oauth/code/callback / response_type: code / scopes (URL-decoded): org:create_api_key user:profile user:inference / PKCE: code_challenge_method=S256"

All claim values match exactly. VERIFIED.

---

## [15] Issue #28091

**URL:** https://github.com/anthropics/claude-code/issues/28091
**Grade:** VERIFIED

**Claims in deliverable (high-stakes token prefix claim):**
- Token prefix `sk-ant-oat01-*` for `claude setup-token`-generated OAuth tokens
- Console API keys prefix `sk-ant-api03-*`
- Messages API rejects `sk-ant-oat01-*` with body `"OAuth authentication is currently not supported."` when used as `Authorization: Bearer`

**Evidence in source (verbatim):**
- "OAuth workspace tokens generated via claude setup-token (prefix sk-ant-oat01-*)" — exact match
- "Only console API keys (sk-ant-api03-*) with separate pay-per-use billing work." — exact match
- "Via Authorization: Bearer: \"OAuth authentication is currently not supported.\"" — exact verbatim including the inner quotes

All three high-stakes claims (prefix, comparison prefix, rejection message) are verbatim entailed. VERIFIED.

---

## [16] Issue #33820

**URL:** https://github.com/anthropics/claude-code/issues/33820
**Grade:** VERIFIED

**Claims in deliverable:**
- `anthropic-ratelimit-*` headers ARE returned by Anthropic API but NOT exposed by Claude Code to hooks or status-line scripts
- CLOSED state, labels `area:hooks`, `area:statusline`, `enhancement`

**Evidence in source (verbatim):**
- "The Anthropic API returns detailed rate-limit headers on every response (anthropic-ratelimit-tokens-remaining, anthropic-ratelimit-requests-remaining, anthropic-ratelimit-input-tokens-remaining, etc.), but Claude Code does not expose these to hooks or status line scripts." — exact verbatim
- "Users who want to monitor their usage and implement warnings... have no way to access this data programmatically within Claude Code. The hook JSON input and status line JSON both lack any rate-limit fields." — supports the not-exposed-to-Claude-Code claim
- State: CLOSED — matches

VERIFIED.

---

## Cross-claim verification — high-stakes items

### "OAuth access token" vs "OAuth refresh token" verbatim wording (Q1)
[2] env-vars page contains both verbatim:
- `CLAUDE_CODE_OAUTH_TOKEN` → "OAuth access token for Claude.ai authentication"
- `CLAUDE_CODE_OAUTH_REFRESH_TOKEN` → "OAuth refresh token for Claude.ai authentication"

The deliverable's bolding of "**access token**" matches the env-vars page wording (the deliverable indicates this with a verbatim block that includes the bold marker; the fetched excerpt has no markdown emphasis but the underlying word "access" is present). The classification claim is correct.

### Refresh endpoint URL (Q2)
[10] issue body log lines show `POST https://platform.claude.com/v1/oauth/token` verbatim three times across timestamps. Endpoint URL is correctly extracted.

### Admin API key requirement (Q3 / Rate Limits API)
[9] verbatim: "Admin API key required. This API is part of the Admin API. These endpoints require an Admin API key (starting with sk-ant-admin...) that differs from standard API keys."
Deliverable quotes this correctly.

### No first-party REST endpoint for subscription quota
Confirmed by the explicit absence notes across:
- [5]: "API endpoint for credit balance: Not mentioned"
- [6]: "What is NOT specified: ... Specific API endpoints for quota exposure"
- [7]: "What is NOT in this article: ... API endpoints for quota checking"
- [8]: scope explicitly "API-level rate limits, organization-level, by usage tier. NOT subscription quota"
- [9]: "NOT covered: Subscription quota (5-hour / weekly counters)"

Absence-of-endpoint claim is well-supported by four-source convergence.

### 1-year token lifetime (sourced to [1])
[1] verbatim: "generate a one-year OAuth token with `claude setup-token`". Match.

### Token prefix `sk-ant-oat01-*` (sourced to [15])
[15] verbatim: "prefix sk-ant-oat01-*". Match.

### Refresh-token rotation claim (sourced to [11] and [10])
- [11] verbatim: "OAuth refresh tokens are typically single-use: when one process uses the refresh token to get a new access/refresh token pair, the old refresh token is invalidated server-side."
- [10] shows HTTP 400 on `POST .../v1/oauth/token` for concurrent sessions after one refresh.

The deliverable correctly notes this is T2-only and "unverified by first-party documentation." Characterization is faithful to source quality.

---

## Auditor's overall assessment

- 14 of 16 citations verified against verbatim source text.
- 2 PARTIAL grades reflect auxiliary use only — no misrepresentation, no claim drift.
- All high-stakes claims (token classification, refresh endpoint URL, admin-key requirement, absence of subscription quota REST endpoint, 1-year token, `sk-ant-oat01-*` prefix, refresh-token rotation) are entailed by the cited sources.
- The deliverable's epistemic markings (T1 vs T2, "unverified by first-party documentation", "observed, not documented") accurately reflect the source quality.
- No INACCURATE, INACCESSIBLE, DRIFT, or NOT FOUND findings.

No corrective action required.
