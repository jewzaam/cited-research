# Anthropic OAuth Mechanics + Subscription Quota API Surface

Citation-backed answers to four focused questions about how Claude Code's OAuth
flow is constructed and what programmatic surface exposes subscription quota.
All numeric and behavioral claims trace to a numbered entry in
[citations.md](citations.md). Source-tier constraint set by the user:
**T1-T2 only** (Anthropic first-party docs/support and the `anthropics/*`
GitHub repo).

---

## Methodology

- Single dimension, all four questions answered against the same source pool.
- Phase 1 dispatched one `research-discovery` sub-agent for the dimension plus
  multi-engine search via the cited-research skill's `multi_search.py`.
- Phase 2 fetched the resulting T1 doc pages directly via WebFetch in the main
  thread; T2 GitHub issues fetched via `gh issue view`.
- No iteration 3 ran: post-iteration-2 confidence reached >0.8 on Q1, Q2, Q3
  and >0.5 on Q4 (gated by absence of T1 source, not by missing search).
- Counter-perspective search: skipped per user choice — the questions are
  technical "how does X work," not preference framing.
- Two independent audit agents (`citation-audit`, `consistency-review`) re-read
  the deliverable against the cited sources after writing; their reports are
  in [audit/](audit/).

---

## Q1 — Is `CLAUDE_CODE_OAUTH_TOKEN` a refresh token or access token?

**Access token.** The Claude Code env-vars documentation [2] names this
variable verbatim as "OAuth **access token** for Claude.ai authentication."
A separate env var `CLAUDE_CODE_OAUTH_REFRESH_TOKEN` exists [2] for the
refresh-token role, with a paired `CLAUDE_CODE_OAUTH_SCOPES` requirement.

Lifetime is unusually long for an access token: the authentication doc [1]
describes `claude setup-token` as generating "a **one-year** OAuth token" for
CI pipelines. The token's prefix is `sk-ant-oat01-*` (OAuth Access Token v01),
captured in issue #28091 [15].

This token is scoped to **inference only** and cannot be used to establish
Remote Control sessions [1]. The Anthropic Messages API at
`api.anthropic.com` currently rejects `sk-ant-oat01-*` tokens when sent as a
bearer token, returning `"OAuth authentication is currently not supported."`
[15] — so the token works inside the Claude Code CLI binary against
Anthropic's interactive backend, but is not interchangeable with a console
API key (`sk-ant-api03-*`) for direct Messages API calls.

`--bare` mode does not read `CLAUDE_CODE_OAUTH_TOKEN`; bare-mode scripts must
use `ANTHROPIC_API_KEY` or `apiKeyHelper` [1].

See [references/oauth-quota-surface.md §Q1](references/oauth-quota-surface.md#q1-is-claudecodeoauthtoken-a-refresh-token-or-access-token).

---

## Q2 — Token-refresh endpoint URL + auth flow

**`POST https://platform.claude.com/v1/oauth/token`.**

This URL does not appear in any first-party Anthropic documentation page
surveyed (the documentation gap is itself logged as Anthropic-org issue
#52202 [13]). The URL is captured **verbatim** from the official Claude
Code 2.1.121 native binary's debug logs in issue #54443 [10] — a Linux
reproduction filed against the `anthropics/claude-code` repo. Because the
captured logs are emitted by the first-party CLI binary, the URL is
established evidence of CLI behavior, even though the docs do not name it.

The full OAuth flow pieced together from T1 docs and first-party log captures:

| Step | Value | Source |
|------|-------|--------|
| Authorization endpoint | `https://claude.ai/oauth/authorize` | [14] |
| `client_id` (Claude Code CLI) | `9d1c250a-e61b-44d9-88ed-5944d1962f5e` | [14] |
| Redirect URI | `https://console.anthropic.com/oauth/code/callback` | [14] |
| PKCE | `code_challenge_method=S256` | [14] |
| Token endpoint (refresh + initial exchange) | `POST https://platform.claude.com/v1/oauth/token` | [10] |
| Interactive scopes (`/login`) | `user:file_upload user:inference user:mcp_servers user:profile user:sessions:claude_code` | [12] |
| CI scopes (`setup-token`) — at least one observed flow | `org:create_api_key user:profile user:inference` | [14] |

Three entry points exist for getting a token without an interactive browser
each session:

1. **Interactive `/login`** writes credentials (access + refresh tokens,
   `expiresAt`) to `~/.claude/.credentials.json` on Linux/Windows or the
   macOS Keychain [1] [11] [12].
2. **`claude setup-token`** walks through OAuth authorization and prints a
   long-lived (~1-year) access token to stdout. The CLI does not save it;
   the caller copies it into `CLAUDE_CODE_OAUTH_TOKEN` [1].
3. **`CLAUDE_CODE_OAUTH_REFRESH_TOKEN` + `CLAUDE_CODE_OAUTH_SCOPES`**
   environment variables: when both are set, `claude auth login` exchanges
   the refresh token for a fresh access token without opening a browser [2].

The exact HTTP request body to the token endpoint and the auth used for the
refresh call itself are **not documented** in any first-party source and are
not enumerated in the captured logs. This deliverable does not assert that
schema.

See [references/oauth-quota-surface.md §Q2](references/oauth-quota-surface.md#q2-token-refresh-endpoint-url-auth-flow).

---

## Q3 — Subscription quota API surface (interactive + Agent SDK pool)

**No first-party REST endpoint exposes the subscription 5-hour / weekly
counters or the Agent SDK credit-pool balance.** Visibility is documented in
three places, none of which is a callable, OAuth-authenticated quota API:

### (a) In-CLI `/status` slash command [6]

The Anthropic Help Center documents `/status` only as "Monitor your remaining
allocation." Field-level shape is not enumerated. Implicit auth: whatever the
running Claude Code session is already authenticated as.

### (b) `anthropic-ratelimit-*` HTTP response headers on Messages API responses [8]

Returned on every `/v1/messages` response. Documented header set:

| Header family | Limit / remaining / reset |
|---------------|---------------------------|
| `anthropic-ratelimit-requests-*` | per-minute request count |
| `anthropic-ratelimit-tokens-*` | combined token count (rounded to nearest 1000) |
| `anthropic-ratelimit-input-tokens-*` | input tokens |
| `anthropic-ratelimit-output-tokens-*` | output tokens |
| `anthropic-priority-*-tokens-*` | Priority Tier only |
| `retry-after` | seconds-to-retry on 429 |

These headers describe **API-tier rate limits** (RPM/ITPM/OTPM, token-bucket
[8]), **not** the subscription's 5-hour/weekly windows. They are also not
currently exposed to Claude Code hooks or status-line scripts [16].

### (c) Admin Rate Limits API [9]

`GET https://api.anthropic.com/v1/organizations/rate_limits` (and the
per-workspace variant) returns the *configured* rate limits for an
organization. Auth requirement, verbatim: "Admin API key required... an
Admin API key (starting with `sk-ant-admin...`) that differs from standard
API keys" [9]. The endpoint returns model-group RPM/ITPM/OTPM ceilings —
not current consumption, not subscription windows, not Agent SDK credit
balance.

### Agent SDK credit pool (subscription-backed) [5]

From June 15 2026, Agent SDK and `claude -p` usage on subscription plans
draws from a separate monthly credit pool:

| Plan | Monthly Agent SDK credit |
|------|--------------------------|
| Pro | $20 |
| Max 5x | $100 |
| Max 20x | $200 |
| Team — Standard seats | $20 |
| Team — Premium seats | $100 |
| Enterprise — usage-based | $20 |
| Enterprise — seat-based Premium | $200 |

Drain order: "Agent SDK usage draws from your monthly credit before any other
source" [5]. At zero: "additional Agent SDK usage flows to usage credits at
standard API rates—but only if you've enabled usage credits. If usage credits
aren't enabled, Agent SDK requests stop until your credit refreshes" [5].
Reset at start of billing cycle; no rollover [5]. Interactive Claude Code in
terminal or IDE continues to use the existing 5-hour/weekly limits [5]. **No
API endpoint is documented for reading the remaining credit balance** [5].

### Agent SDK auth requirement [4] [15]

The Agent SDK overview documents `ANTHROPIC_API_KEY` (or cloud-provider env
vars) as the supported authentication. Verbatim restriction [4]:

> Unless previously approved, Anthropic does not allow third party developers
> to offer claude.ai login or rate limits for their products, including
> agents built on the Claude Agent SDK. Please use the API key authentication
> methods described in this document instead.

Combined with the Messages API rejecting `sk-ant-oat01-*` tokens [15], the
practical takeaway is: **Agent SDK use against `api.anthropic.com` =
`ANTHROPIC_API_KEY` (`sk-ant-api03-*`).** The Agent SDK credit-pool
consumption path is `claude -p` / SDK execution that spawns or links the
Claude Code CLI binary holding OAuth credentials locally — not a direct
header-driven OAuth call to the Messages API.

See [references/oauth-quota-surface.md §Q3](references/oauth-quota-surface.md#q3-subscription-quota-api-surface).

---

## Q4 — Token rotation-on-refresh behavior

**Refresh token rotates on each refresh — unverified by first-party
documentation.** No T1 Anthropic page describes the OAuth refresh lifecycle.
Issue #52202 [13] is an open documentation request that explicitly flags
this gap.

The strongest available evidence comes from two reproducible-bug reports
filed against the `anthropics/claude-code` repo:

- Issue #24317 [11]: reporter's analysis under reproducible repro,
  "OAuth refresh tokens are typically single-use: when one process uses the
  refresh token to get a new access/refresh token pair, the old refresh
  token is invalidated server-side."
- Issue #54443 [10]: Claude Code 2.1.121 debug logs show two concurrent
  sessions failing on `POST .../v1/oauth/token` with HTTP 400 minutes after
  one session's successful refresh — the symptom pattern of rotation +
  server-side single-use enforcement.

Issue #52202 [13] also quotes Anthropic changelog v2.1.118 verbatim: "Fixed
OAuth token refresh failing when the server revokes a token before its local
expiry time." This confirms server-authoritative revocation, but does not by
itself confirm rotation.

### Practical implication

Concurrent Claude Code sessions sharing one credential file (e.g., headless
fleet, multiple terminal tabs, SSH-multiplexed agents) will fight on
refresh. Each successful rotation invalidates the prior refresh token, so
any process that started with a now-rotated copy gets 400 from the token
endpoint and must re-login interactively. This is the failure pattern in
both #24317 [11] and #54443 [10].

See [references/oauth-quota-surface.md §Q4](references/oauth-quota-surface.md#q4-token-rotation-on-refresh-behavior).

---

## Reflection

A single reflection pass on this draft surfaced two corrections folded back
into the text above:

1. The original draft characterized `CLAUDE_CODE_OAUTH_TOKEN` as
   "functionally a refresh-token-class credential" because of the 1-year
   lifetime. That was an overreach — the env-vars doc [2] is explicit that
   it is an *access* token, and a *separate* refresh-token env var exists.
   The corrected text leads with the access-token classification.
2. The original draft treated #24317 [11] as confirmation of rotation. It is
   community analysis on a first-party repo, not Anthropic-documented
   behavior. Recharacterized as "unverified by first-party documentation,
   strong T2 evidence consistent with rotation."

---

## Limitations

- **T1 evidence is missing for Q4.** Anthropic has not documented OAuth token
  refresh lifecycle; Anthropic itself flagged this gap [13]. Q4's answer
  rests on T2 evidence and is explicitly marked unverified.
- **The refresh endpoint URL [10] is observed, not documented.** Future
  Claude Code releases could route refresh elsewhere without changing any
  doc page.
- **No assertion is made about the request body** to the token endpoint —
  the captured log fragments [10] [14] show the URL, method, and (for the
  authorize call) the URL query parameters, but do not enumerate the
  `application/x-www-form-urlencoded` body of the token POST.
- **`client_id`, scopes, and PKCE specifics [14] are point-in-time** and
  may rotate with new CLI releases.
- The `auth.anthropic.com` hostname referenced in other issues (e.g., #33238)
  was excluded as a separate fact; the only first-party-CLI-logged token
  endpoint surfaced in this research is on `platform.claude.com` [10].
