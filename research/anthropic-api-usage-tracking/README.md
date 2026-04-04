# Anthropic API Usage Tracking and Limits

What the Anthropic API exposes for monitoring usage, enforcing rate limits, and tracking cost — and what you must build yourself. Every claim in this research traces to a web source visited in-session; two independent review agents audit the output.

## TL;DR

The API provides **18 rate limit headers** on every response, a **`usage` object** with exact token counts per request, and an **Admin API** (`/v1/organizations/usage_report/messages` and `/v1/organizations/cost_report`) for historical data. There is **no real-time budget endpoint, no per-end-user cost attribution, and no webhook for spend alerts**. Wrapper apps must compute cost client-side from the `usage` object or deploy a proxy (LiteLLM, Portkey, Helicone) for per-user budget enforcement.

## Key Tables

### Rate Limit Headers (Returned on Every Response)

| Category | Headers (limit / remaining / reset) |
|----------|-------------------------------------|
| Requests | `anthropic-ratelimit-requests-*` |
| Tokens (aggregate) | `anthropic-ratelimit-tokens-*` |
| Input tokens | `anthropic-ratelimit-input-tokens-*` |
| Output tokens | `anthropic-ratelimit-output-tokens-*` |
| Priority Tier (if active) | `anthropic-priority-{input,output}-tokens-*` |
| Error | `retry-after` (seconds to wait on 429) |

### Spend Tiers

| Tier | Deposit | Monthly Cap | Sonnet 4.x RPM / ITPM / OTPM |
|------|---------|-------------|-------------------------------|
| 1 | $5 | $100 | 50 / 30K / 8K |
| 2 | $40 | $500 | 1K / 450K / 90K |
| 3 | $200 | $1,000 | 2K / 800K / 160K |
| 4 | $400 | $200,000 | 4K / 2M / 400K |
| Invoicing | N/A | No limit | Custom |

### Cost Tracking Options

| Approach | Best For | Key Tool |
|----------|----------|----------|
| `message.usage` + local math | Single-user apps | Built into SDK |
| LiteLLM proxy | Multi-user budget enforcement | `max_budget` per user |
| Grafana/Datadog/Honeycomb | Ops teams with existing monitoring | Admin API integration |
| Langfuse / Helicone | Self-hosted / privacy-sensitive | MIT / open-source |
| Agent SDK `total_cost_usd` | Agent workflows | Built into Agent SDK |

## Quick Decision Framework

1. **Do you need per-user budgets?** → Deploy a proxy (LiteLLM or Portkey)
2. **Do you need org-level dashboards?** → Connect a monitoring platform to the Admin API
3. **Do you just need cost awareness?** → Read `message.usage` and multiply by published rates
4. **Do you need pre-flight cost checks?** → Call `/v1/messages/count_tokens` (free)
5. **Are you building with the Agent SDK?** → Use `total_cost_usd` on `ResultMessage`

## Files

| File | Contents |
|------|----------|
| [analysis.md](analysis.md) | Full analysis with methodology and citations |
| [citations.md](citations.md) | All 32 sources with tier ratings |
| [references/response-headers.md](references/response-headers.md) | Complete header list and behavior |
| [references/rate-limit-structure.md](references/rate-limit-structure.md) | Tiers, token bucket algorithm, cache-aware ITPM |
| [references/billing-usage-endpoints.md](references/billing-usage-endpoints.md) | Admin API endpoints, parameters, limitations |
| [references/client-side-tracking.md](references/client-side-tracking.md) | Usage object, cost formulas, pricing tables |
| [references/sdk-hooks.md](references/sdk-hooks.md) | Python and TypeScript SDK extension points |
| [references/cost-surfacing-patterns.md](references/cost-surfacing-patterns.md) | Gateway, observability, and self-hosted patterns |
| [audit/citation-audit.md](audit/citation-audit.md) | Independent citation verification |
| [audit/consistency-review.md](audit/consistency-review.md) | Cross-file consistency check |
