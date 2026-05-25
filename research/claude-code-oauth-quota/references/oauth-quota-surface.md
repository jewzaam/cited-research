# Reference — OAuth + Quota API Surface

Single dimension covering all four user questions. See
[citations.md](../citations.md) for source details; bracketed numbers
reference entries there. T1-T2 sources only.

---

## Q1 — Is `CLAUDE_CODE_OAUTH_TOKEN` a refresh token or access token?

**Answer: access token.** First-party documentation [2] explicitly classifies it
that way.

### Evidence

From `https://code.claude.com/docs/en/env-vars` [2], verbatim entry:

> `CLAUDE_CODE_OAUTH_TOKEN` — OAuth **access token** for Claude.ai
> authentication. Alternative to `/login` for SDK and automated environments.
> Takes precedence over keychain-stored credentials. Generate one with
> `claude setup-token`

The same page documents a **separate** env variable for the refresh-token role:

> `CLAUDE_CODE_OAUTH_REFRESH_TOKEN` — OAuth refresh token for Claude.ai
> authentication. When set, `claude auth login` exchanges this token directly
> instead of opening a browser. Requires `CLAUDE_CODE_OAUTH_SCOPES`. Useful for
> provisioning authentication in automated environments

And a scopes pairing:

> `CLAUDE_CODE_OAUTH_SCOPES` — Space-separated OAuth scopes the refresh token
> was issued with, such as `"user:profile user:inference user:sessions:claude_code"`.
> Required when `CLAUDE_CODE_OAUTH_REFRESH_TOKEN` is set

### Caveats

- `CLAUDE_CODE_OAUTH_TOKEN` is a **long-lived** access token. The authentication
  doc [1] describes `claude setup-token` as generating "a one-year OAuth token"
  for CI use. So this is an access token with an unusually long lifetime by
  OAuth-2.0 norms, not a refresh token (refresh tokens are exchanged for new
  access tokens; they are not themselves sent as the authorization credential
  for inference).
- The token has the prefix `sk-ant-oat01-*` (per issue #28091 [15] — "OAuth
  Access Token v01").
- Scope is restricted: "scoped to inference only and cannot establish Remote
  Control sessions" [1]. The Anthropic Messages API at `api.anthropic.com`
  also currently rejects these tokens with `"OAuth authentication is currently
  not supported."` [15].
- `--bare` mode does not read `CLAUDE_CODE_OAUTH_TOKEN`; bare-mode scripts
  must use `ANTHROPIC_API_KEY` or `apiKeyHelper` [1].

---

## Q2 — Token-refresh endpoint URL + auth flow

**Answer (refresh endpoint):** `POST https://platform.claude.com/v1/oauth/token`.

This URL is **not** documented in any first-party Anthropic doc page found in
this search [13]; it is captured from the official Claude Code CLI's own debug
logs (v2.1.121, Linux x86_64) in issue #54443 [10]. Because the captured logs
are emitted by the first-party binary, the URL is established evidence even
though Anthropic has not added it to the docs.

### Full OAuth flow (pieced together from T1 docs + first-party CLI log captures)

| Step | URL / value | Source |
|------|-------------|--------|
| Authorization endpoint | `https://claude.ai/oauth/authorize` | Captured by Claude Code log [14] |
| `client_id` (Claude Code CLI) | `9d1c250a-e61b-44d9-88ed-5944d1962f5e` | Same [14] |
| `redirect_uri` | `https://console.anthropic.com/oauth/code/callback` | Same [14] |
| PKCE | `code_challenge_method=S256` | Same [14] |
| Scopes (interactive `/login`) | `user:file_upload user:inference user:mcp_servers user:profile user:sessions:claude_code` | `~/.claude/.credentials.json` shape in #42904 [12] |
| Scopes (one of the bug-captured flows) | `org:create_api_key user:profile user:inference` | #10715 log [14] |
| Token endpoint | `POST https://platform.claude.com/v1/oauth/token` | #54443 log capture, Claude Code v2.1.121 [10] |

### Interactive vs. automated entry points

| Entry point | What it does | Source |
|-------------|--------------|--------|
| `claude` (first launch) / `/login` | Opens browser, runs full authorization-code+PKCE flow against `claude.ai`, writes credentials to `~/.claude/.credentials.json` (Linux/Windows) or macOS Keychain | [1] |
| `claude setup-token` | Walks through OAuth authorization and prints a long-lived access token to stdout. **Does not save it.** Caller copies the value into `CLAUDE_CODE_OAUTH_TOKEN` | [1] |
| `CLAUDE_CODE_OAUTH_REFRESH_TOKEN` env var | When set, `claude auth login` exchanges this refresh token directly for an access token, bypassing the browser. Requires `CLAUDE_CODE_OAUTH_SCOPES`. | [2] |

### Auth requirement to call the refresh endpoint

Not documented. From log evidence [10] the CLI POSTs to the token endpoint
without an interactive browser; the request body is not enumerated in the
captured logs. This deliverable does not assert a request schema (no T1 source
defines one).

---

## Q3 — Subscription quota API surface

**Answer:** No first-party endpoint exposes subscription (5-hour / weekly)
counters. Visibility is documented at three layers:

| Layer | Surface | Auth | Notes | Source |
|-------|---------|------|-------|--------|
| In-CLI status | `/status` slash command in Claude Code | Implicit (whatever auth the running session uses) | Documented as "Monitor your remaining allocation" | [6] |
| HTTP response headers (per-request) | `anthropic-ratelimit-*` on Messages API responses | Whatever auth the request used | These describe **API rate limits** (RPM/ITPM/OTPM, token-bucket), not subscription windows. Returned on `/v1/messages` calls. Not exposed to Claude Code hooks/statusline | [8], [16] |
| Admin Rate Limits API | `GET https://api.anthropic.com/v1/organizations/rate_limits` (and per-workspace variant) | **Admin API key** (`sk-ant-admin...`); not standard API keys; not OAuth | Returns the **configured** rate limits for an org/workspace, not current consumption. Does not report subscription quota at all | [9] |

### What `/status` shows

The Anthropic Help Center article [6] only states `/status` lets users "Monitor
your remaining allocation"; it does not detail the fields. No first-party API
surface returns the same data.

### Agent SDK pool (subscription-backed SDK use)

Per the Agent SDK plan page [5], from June 15 2026 Agent SDK + `claude -p`
usage on subscription plans draws from a **separate** monthly credit pool
(Pro $20, Max 5x $100, Max 20x $200, Team Standard $20 / Premium $100,
Enterprise usage-based $20 / seat-based Premium $200). Drains before any
other source; resets at billing cycle; does not roll over. **No API endpoint
for reading the remaining credit balance is documented** [5]. The article
also notes interactive Claude Code continues to consume the 5-hour / weekly
subscription limits as before [5].

### Auth requirement to call Agent SDK programmatically

The Agent SDK overview [4] documents `ANTHROPIC_API_KEY` (or cloud-provider
env vars) as the supported auth. The page contains a verbatim restriction:

> Unless previously approved, Anthropic does not allow third party developers
> to offer claude.ai login or rate limits for their products, including agents
> built on the Claude Agent SDK. Please use the API key authentication methods
> described in this document instead.

Combined with issue #28091 [15] showing `sk-ant-oat01-*` tokens are rejected
by the Messages API, the practical position is: **Agent SDK auth = API key,
not OAuth**, and the subscription-credit-pool consumption path is the
`claude -p` / SDK execution against a CLI binary that holds OAuth credentials
locally — not a header-driven OAuth call to `api.anthropic.com`.

---

## Q4 — Token rotation-on-refresh behavior

**Answer (with caveat): the refresh token rotates on each refresh.**
**No first-party Anthropic documentation states this.** The
strongest available evidence is from anthropics-org-repo issues #24317 [11]
and #54443 [10], both of which describe behavior consistent with single-use
refresh tokens.

### Evidence (Tier 2, no T1 confirmation)

- Issue #24317 [11], reporter's reproducible analysis: "OAuth refresh tokens
  are typically single-use: when one process uses the refresh token to get a
  new access/refresh token pair, the old refresh token is invalidated
  server-side." Repro: with N concurrent Claude Code processes sharing
  `~/.claude/.credentials.json`, one process refreshes, others retain the
  stale refresh token, server rejects → forced `/login`.
- Issue #54443 [10], log capture from Claude Code 2.1.121: concurrent sessions
  receive HTTP 400 from `POST .../v1/oauth/token` shortly after one session
  refreshes successfully. Behavior matches single-use rotation.
- Issue #52202 [13] quotes Anthropic changelog v2.1.118: "Fixed OAuth token
  refresh failing when the server revokes a token before its local expiry
  time." This confirms the server is authoritative for revocation; it does
  not, by itself, prove that refresh tokens rotate.

### What the docs do *not* say

The Authentication doc [1] explains `apiKeyHelper` refresh semantics
("called after 5 minutes or on HTTP 401 response") but does not document the
OAuth token refresh lifecycle. Issue #52202 [13] is an Anthropic-acknowledged
documentation gap for exactly this topic.

### Practical implication

Concurrent agents sharing one OAuth credential store will fight each other
on refresh. Each rotation invalidates the prior refresh token, so any process
that started with a now-rotated refresh token gets 400 and must re-login.
This is fragile for headless / SSH / Docker fleet deployments.

---

## Cross-cutting summary

| Topic | First-party answer? | Source(s) |
|-------|---------------------|-----------|
| `CLAUDE_CODE_OAUTH_TOKEN` is an access token | Yes — env-vars doc | [2] |
| Refresh endpoint URL | No (CLI log capture only) | [10] |
| Subscription quota REST API | No first-party endpoint exists | [6], [8], [9] |
| Token rotation on refresh | No first-party doc; T2 only | [10], [11], [13] |

## Gaps and Limitations

1. **Q4 rests on T2.** First-party Anthropic docs do not state refresh-token
   rotation. The behavior is inferred from official-CLI log captures and
   reproducible repo issues, but Anthropic has not published the design.
   Treated as "unverified by first-party documentation."
2. **Q2 endpoint URL is observed, not documented.** `platform.claude.com/v1/oauth/token`
   appears in Claude Code's own debug logs [10] but does not appear in any
   first-party doc page surveyed.
3. **Q3 lacks any first-party REST endpoint** for the subscription window or
   Agent SDK credit balance. Confidence here is high *that no documented
   endpoint exists*; that is not the same as proving none exists internally.
4. The captured `client_id`, `redirect_uri`, and PKCE scheme [14] are
   point-in-time values; they may change with future Claude Code releases
   and should not be relied on as stable API.
