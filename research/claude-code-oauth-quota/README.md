# Anthropic OAuth Mechanics + Subscription Quota API Surface

Last revised: 2026-05-24

Citation-backed answers to four focused questions about Claude Code's OAuth
flow and the programmatic surface for subscription quota. Source-tier
constraint: T1-T2 only (Anthropic first-party docs/support and
`anthropics/*` GitHub).

## TL;DR

| # | Question | Answer | First-party? |
|---|----------|--------|--------------|
| 1 | Is `CLAUDE_CODE_OAUTH_TOKEN` a refresh token or access token? | **Access token.** A long-lived (~1-year) OAuth access token; prefix `sk-ant-oat01-*`. A separate `CLAUDE_CODE_OAUTH_REFRESH_TOKEN` env var handles the refresh-token role | **Yes** — [1] (auth doc) + [2] (env-vars doc) |
| 2 | Token-refresh endpoint URL + auth flow | **`POST https://platform.claude.com/v1/oauth/token`.** Full flow: authorize at `https://claude.ai/oauth/authorize` (PKCE S256, `client_id=9d1c250a-e61b-44d9-88ed-5944d1962f5e`, callback `https://console.anthropic.com/oauth/code/callback`); refresh against the token endpoint | **No first-party doc.** URL is from Claude Code 2.1.121's own debug logs; gap is acknowledged in Anthropic-repo issue #52202 |
| 3 | What endpoint(s) expose subscription quota (interactive + Agent SDK pool)? Auth requirement? | **No first-party REST endpoint exposes subscription counters.** `/status` slash command shows "remaining allocation" in the CLI; `anthropic-ratelimit-*` headers describe API tier limits (not subscription); `GET /v1/organizations/rate_limits` returns *configured* limits and requires an **Admin API key (`sk-ant-admin...`)** — not OAuth, not the subscription window. Agent SDK credit-pool balance has no documented endpoint. Agent SDK programmatic auth = `ANTHROPIC_API_KEY`, not OAuth | **No** — confirmed by absence across [rate-limits], [rate-limits-api], [pro-max], and [agent-sdk-plan] docs |
| 4 | Token rotation-on-refresh behavior | **Rotates on each refresh (unverified by first-party docs).** Strong T2 evidence: anthropics/claude-code issues #24317 and #54443 document single-use refresh behavior via reproducible concurrent-session 400 errors; changelog v2.1.118 confirmed server-authoritative revocation | **No T1 source.** T2 only (Anthropic-org repo) |

## Decision framework

1. **Choosing CI auth?** Use `claude setup-token` → set `CLAUDE_CODE_OAUTH_TOKEN`.
   It is a long-lived access token (~1 year), Pro/Max/Team/Enterprise required.
   It works only via the Claude Code CLI; do not point it at `api.anthropic.com/v1/messages`
   directly (rejected with "OAuth authentication is currently not supported").
2. **Need to provision auth in a Docker image without baking a 1-year token?**
   Use `CLAUDE_CODE_OAUTH_REFRESH_TOKEN` + `CLAUDE_CODE_OAUTH_SCOPES` and run
   `claude auth login` in-container; it exchanges the refresh token directly.
3. **Want programmatic subscription-quota visibility?** Not available via a
   public REST endpoint as of 2026-05-24. Options today: parse `/status`
   output in-process, read `anthropic-ratelimit-*` headers on `/v1/messages`
   responses (API-tier limits only, not 5h/weekly subscription windows).
4. **Want programmatic Agent SDK credit-pool balance?** Not documented.
5. **Running many concurrent Claude Code processes?** Expect refresh-token
   rotation contention. Either fan out from a single auth-managing process or
   accept periodic forced `/login`. See issue #24317.

## Where to look next

- Full analysis with citations: [analysis.md](analysis.md)
- Per-question deep dive: [references/oauth-quota-surface.md](references/oauth-quota-surface.md)
- Sources, tiers, exclusions: [citations.md](citations.md)
- Independent audits: [audit/citation-audit.md](audit/citation-audit.md),
  [audit/consistency-review.md](audit/consistency-review.md)
