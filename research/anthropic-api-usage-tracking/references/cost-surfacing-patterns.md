# Surfacing Cost to End Users

This reference covers Dimension 5: patterns for wrapper applications to display usage, enforce per-user budgets, and implement cost controls.

Source details: [citations.md](../citations.md)

---

## The Challenge

Anthropic's API provides organization-level usage tracking (via the Admin API) and per-request token counts (via the `usage` response object), but **no per-end-user attribution or budget enforcement** [3]. Wrapper applications that serve multiple end users must build this layer themselves.

## Architecture Patterns

### Pattern 1: Gateway/Proxy with Budget Enforcement

Route all LLM requests through a gateway that intercepts responses and enforces budgets before forwarding. This is the dominant pattern in the ecosystem [15].

**Four-component architecture** (described by Portkey) [15]:
1. **Request layer** — intercepts outgoing API calls, attaches user metadata
2. **Usage logging** — records token counts and costs per request
3. **Budget manager** — maintains per-user/team running totals; enforces limits
4. **Alerting** — notifies on threshold crossings via Slack, email, or webhook

**Budget enforcement approaches** [15] [16]:
- **Hard block** — reject the request with an error when budget is exceeded (LiteLLM returns HTTP 400 [13])
- **Progressive throttling** — send alerts at warning thresholds (e.g., 80%), then hard-block at the limit [15]
- **Soft alert only** — notify but allow continued usage [16]

### Pattern 2: Observability Platform Integration

Use the Anthropic Admin API as a data source for existing monitoring infrastructure.

#### Grafana Cloud [18] [19]
- Released August 2025 (v1.0.0, updated to v1.1.1) [18]
- **Agentless/collector-less** — Grafana pulls directly from the Anthropic Admin API [18]
- Prometheus-format metrics [18]
- Three built-in alert rules [18]:
  - `AnthropicDailyCostSpike` — >50% day-over-day cost increase
  - (Two additional alert rules referenced but not named in the snippet)
- Requires Admin API key setup [19]

#### Datadog [20]
- Ingests from Anthropic Admin API
- Normalizes to **FinOps Foundation FOCUS format** [20]
- Grouping by model, workspace, service tier, API key [20]
- Integrates with Cloud Cost Management dashboards [20]

#### Honeycomb [21]
- **OpenTelemetry receiver** for Anthropic Admin API data [21]
- Maps Admin API fields to OTel attributes [21]

#### Vantage [3]
- FinOps platform listed as an official Anthropic partner integration [3]

#### CloudZero [3]
- Cloud intelligence platform for cost tracking and forecasting [3]

### Pattern 3: Self-Hosted Observability

For organizations that need on-premise cost tracking.

#### Langfuse [14]
- MIT-licensed, self-hostable (Docker, Kubernetes) [14]
- Per-generation cost tracking with custom model pricing definitions [14]
- Metrics API with filters: user, session, tag [14]
- Can define custom pricing for models not in the built-in table [14]

#### Helicone [17]
- Open-source with self-host option (Docker Compose) [17]
- **Property-based cost attribution** — attach arbitrary metadata (user_id, feature, team) to requests and query cost by any property [17]
- Pricing data for 300+ models from a community-maintained open-source pricing repo [17]
- Two modes: AI Gateway (proxy) or async logging [17]

#### OpenLLMetry [28]
- Apache 2.0 licensed [28]
- OTel extensions for Anthropic, OpenAI, Cohere [28]
- Span attributes for per-user and per-feature cost attribution [28]
- Integrates with any OTel-compatible backend (Jaeger, Grafana Tempo, Datadog, etc.) [28]

### Pattern 4: Dedicated LLM Proxy

#### LiteLLM [12] [13] [31] [32]
- Open-source Python proxy supporting 100+ LLM providers [31]
- **Automatic cost tracking** — stores in Redis or PostgreSQL [12]
- Per-key, per-user (`user_id`), per-team aggregation [12]
- **`max_budget`** field per user with `budget_duration` [13]
- **Hard enforcement** — returns HTTP 400 when budget exceeded [13]
- Also available as a standalone `BudgetManager` class for client-side use without the proxy [32]
- End-user (`customer_id`) spend tracking with admin UI [13]

#### Portkey [15] [16]
- AI gateway with **virtual key budget limits** [16]
- Hierarchical: Customer → Team → Virtual Key → Provider Configuration [15]
- USD or token-based limits [16]
- Automatic expiry on breach [16]
- Alerts via Slack, email, or webhook [16]
- Note: "Enterprise-feature" appears in the docs URL — budget limits may require a paid plan [16]

## Per-User Attribution: The `user_id` Pattern

Since the Anthropic API does not support per-end-user grouping in its Admin API, the standard approach is [12] [15]:

1. Attach a `user_id` (or `customer_id`) to every request at the proxy layer
2. The proxy logs usage per user alongside the token counts from the response
3. Budget checks happen at the proxy before the request reaches Anthropic
4. Dashboards and alerts are built on the proxy's aggregated data

This pattern is implemented by LiteLLM, Portkey, and Helicone [12] [16] [17].

## Claude Code-Specific Tracking

For organizations using Claude Code, the Claude Code Analytics API provides per-user estimated costs and productivity metrics without needing to map API keys to users [30]:

- Endpoint: `/v1/organizations/usage_report/claude_code` [30]
- Metrics: sessions, lines of code, commits, PRs, tool acceptance rates [30]
- Data delay: up to 1 hour [30]

## Community/Open-Source Tools

Several smaller tools target Claude-specific cost tracking (from discovery agent findings):

| Tool | Type | Description |
|------|------|-------------|
| `ccost` | CLI | Claude-specific tracker with LiteLLM pricing integration, multi-currency |
| `claude-usage-analytics` | Drop-in proxy | Replaces `api.anthropic.com`, FinOps analytics for teams |
| `ClaudeUsageTracker` | macOS menu bar | Project-based cost breakdown, monthly totals |
| `PriceyApp` | macOS status bar | Real-time Claude Code cost vs. human developer cost comparison |
| `llm-performance-tracker` | Web dashboard | Next.js + Tinybird + Clerk multi-tenant template |

Note: These are individual GitHub repos (Tier 4 sources) identified by the discovery agent. Maturity, maintenance status, and production readiness are unknown.

## Gaps and Limitations

- **No native Anthropic budget enforcement** — all per-user budget enforcement requires external infrastructure (proxy, gateway, or custom middleware) [3].
- **Portkey budget limits may be enterprise-only** — the URL path includes "enterprise-feature"; open-source availability is unconfirmed [16].
- **Admin API unavailable for individual accounts** — wrapper apps built by individual developers without an Anthropic organization cannot use the Usage & Cost API [3].
- **LiteLLM `max_budget` blocking behavior details** — whether the request is pre-blocked (before tokens are spent) or post-blocked was not confirmed from available sources [13].
- **Pricing staleness risk** — all proxy tools that compute cost client-side must keep pricing tables current. There is no Anthropic webhook or API to signal pricing changes.
- The community tools listed are from discovery agent findings and were not directly fetched or verified for functionality.
