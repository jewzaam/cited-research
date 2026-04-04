# Citations

All sources visited in-session via WebSearch or WebFetch. Numbered sequentially.

---

**[1]** "Rate limits." *Anthropic Platform Docs*, 2026.
<https://platform.claude.com/docs/en/api/rate-limits>
**Tier:** 2
Data extracted: Complete list of 18 rate limit response headers with exact names and descriptions; rate limit tier tables (RPM, ITPM, OTPM) for Tiers 1-4 across all model classes; token bucket algorithm description; spend limit tier requirements ($5/$40/$200/$400 cumulative); cache-aware ITPM explanation; retry-after header behavior; workspace limit configuration.

**[2]** "Pricing." *Anthropic Platform Docs*, 2026.
<https://platform.claude.com/docs/en/about-claude/pricing>
**Tier:** 2
Data extracted: Complete model pricing table (input/output per MTok for all models); prompt caching multipliers (1.25x 5-min write, 2x 1-hour write, 0.1x read); batch API 50% discount table; fast mode pricing ($30/$150 MTok for Opus 4.6); data residency 1.1x multiplier; web search $10/1,000 searches; code execution $0.05/hr/container beyond 1,550 free hours; tool use system prompt overhead tokens.

**[3]** "Usage and Cost API." *Anthropic Platform Docs*, 2026.
<https://platform.claude.com/docs/en/api/usage-cost-api>
**Tier:** 2
Data extracted: Usage endpoint `/v1/organizations/usage_report/messages`; Cost endpoint `/v1/organizations/cost_report`; Admin API key requirement (`sk-ant-admin...`); time buckets (1m, 1h, 1d) with max bucket counts; filter dimensions (api_key_ids, workspace_ids, models, service_tiers, context_window, inference_geos, speeds); group_by dimensions; pagination (has_more, next_page); data freshness ~5 minutes; partner integrations (CloudZero, Datadog, Grafana, Honeycomb, Vantage); Priority Tier cost caveat.

**[4]** "Admin API overview." *Anthropic Platform Docs*, 2026.
<https://platform.claude.com/docs/en/api/administration-api>
**Tier:** 2
Data extracted: Admin API scope (organization members, invites, workspaces, workspace members, API keys, organization info); authentication model (`sk-ant-admin...` key, admin role required); five organization roles (user, claude_code_user, developer, billing, admin); endpoint paths for CRUD on users, invites, workspaces, workspace members, API keys; `/v1/organizations/me` endpoint; API keys cannot be created via API (Console only); admin members cannot be removed via API.

**[5]** "Anthropic SDK for Python." *GitHub — anthropics/anthropic-sdk-python*, 2026.
<https://github.com/anthropics/anthropic-sdk-python>
**Tier:** 2
Data extracted (from discovery agent search snippets): `message.usage` object structure (input_tokens, output_tokens, cache fields); `with_raw_response` pattern for header access; `DefaultHttpxClient` for custom transport; `client.messages.stream()` returning `MessageStreamManager`; `get_final_message()` method.
Note: Full page not fetched; data from search snippets and secondary analysis sources.

**[6]** "Anthropic SDK for TypeScript." *GitHub — anthropics/anthropic-sdk-typescript*, 2026.
<https://github.com/anthropics/anthropic-sdk-typescript>
**Tier:** 2
Data extracted (from discovery agent search snippets): `.on('message', cb)` and `.on('contentBlock', cb)` event hooks; `.finalMessage()` for accumulated usage; `withResponse()` pattern for header access; custom fetch override.
Note: Full page not fetched; data from search snippets.

**[7]** "Token counting." *Anthropic Platform Docs*, 2026.
<https://platform.claude.com/docs/en/build-with-claude/token-counting>
**Tier:** 2
Data extracted (from discovery agent): `/v1/messages/count_tokens` endpoint; free to use; separate RPM limits (100-8,000 by tier); estimate not exact; supports tools/images/PDFs.
Note: Data from discovery agent's confirmed fetch.

**[8]** "Cost tracking — Agent SDK." *Anthropic Platform Docs*, 2026.
<https://platform.claude.com/docs/en/agent-sdk/cost-tracking>
**Tier:** 2
Data extracted (from discovery agent): `total_cost_usd` field on `ResultMessage`; `model_usage`/`modelUsage` breakdown; parallel tool call deduplication by message ID; session-level accumulation pattern.
Note: Data from discovery agent's confirmed fetch.

**[9]** "Messages streaming." *Anthropic Platform Docs*, 2026.
<https://platform.claude.com/docs/en/api/messages-streaming>
**Tier:** 2
Data extracted (from discovery agent search snippets): SSE event sequence; `message_delta` event containing usage delta with final output_tokens; `message_start` contains initial usage with input_tokens.
Note: Full page not fetched; data from search snippets.

**[10]** "Our approach to API rate limits." *Anthropic Help Center*, 2026.
<https://support.anthropic.com/en/articles/8243635-our-approach-to-api-rate-limits>
**Tier:** 2
Data extracted (from discovery agent): Philosophy behind rate limits; automatic tier advancement.
Note: Not directly fetched.

**[11]** "How can I advance my API usage to Tier 2?" *Anthropic Help Center*, 2026.
<https://support.anthropic.com/en/articles/10366389-how-can-i-advance-my-api-usage-to-tier-2>
**Tier:** 2
Data extracted (from discovery agent): $40 cumulative purchase requirement for Tier 2; immediate advancement.

**[12]** "Cost tracking." *LiteLLM Docs*, 2026.
<https://docs.litellm.ai/docs/proxy/cost_tracking>
**Tier:** 2
Data extracted (from discovery agent): Automatic spend tracking for 100+ models; database backend (Redis/PostgreSQL); per-key/user/team aggregation.
Note: Not directly fetched.

**[13]** "Users — Budget management." *LiteLLM Docs*, 2026.
<https://docs.litellm.ai/docs/proxy/users>
**Tier:** 2
Data extracted (from discovery agent): `max_budget` field; `budget_duration`; hard 400-error block when exceeded; `user_id` parameter.
Note: Not directly fetched.

**[14]** "Token and cost tracking." *Langfuse Docs*, 2026.
<https://langfuse.com/docs/observability/features/token-and-cost-tracking>
**Tier:** 2
Data extracted (from discovery agent): Per-generation cost tracking; custom model pricing definitions; Metrics API filters (user, session, tag).
Note: Not directly fetched.

**[15]** "Budget limits and alerts in LLM apps." *Portkey Blog*, 2026.
<https://portkey.ai/blog/budget-limits-and-alerts-in-llm-apps/>
**Tier:** 3
Data extracted (from discovery agent): Four-component architecture pattern (request layer, usage logging, budget manager, alerting); progressive throttling vs. hard block.
Note: Not directly fetched.

**[16]** "Virtual key budget limits." *Portkey Docs*, 2026.
<https://portkey.ai/docs/product/ai-gateway-streamline-llm-integrations/virtual-keys/budget-limits-enterprise-feature>
**Tier:** 2
Data extracted (from discovery agent): USD or token-based hard limits; expiry on breach; Slack/email/webhook alerts.
Note: Not directly fetched. "Enterprise-feature" in URL suggests possible paid-only feature.

**[17]** "Cost tracking." *Helicone Docs*, 2026.
<https://docs.helicone.ai/guides/cookbooks/cost-tracking>
**Tier:** 2
Data extracted (from discovery agent): Property-based cost attribution; per-user breakdown; AI Gateway vs. async logging modes; open-source pricing repo for 300+ models.
Note: Not directly fetched.

**[18]** "Anthropic integration for Grafana Cloud." *Grafana Labs Blog*, August 2025.
<https://grafana.com/blog/how-to-monitor-claude-usage-and-costs-introducing-the-anthropic-integration-for-grafana-cloud/>
**Tier:** 3
Data extracted (from discovery agent): Integration released August 2025; collector-less design using Admin API; Prometheus-format metrics; three built-in alert rules including `AnthropicDailyCostSpike`.
Note: Not directly fetched.

**[19]** "Anthropic integration." *Grafana Cloud Docs*, 2025.
<https://grafana.com/docs/grafana-cloud/monitor-infrastructure/integrations/integration-reference/integration-anthropic/>
**Tier:** 2
Data extracted (from discovery agent): Integration version history; Admin API key setup; dashboard panels; alert rule definitions.
Note: Not directly fetched.

**[20]** "Anthropic usage and costs." *Datadog Docs*, 2026.
<https://docs.datadoghq.com/integrations/anthropic-usage-and-costs/>
**Tier:** 2
Data extracted (from discovery agent): Metrics emitted; grouping by model/workspace/service tier; FinOps Foundation FOCUS format normalization; Cloud Cost Management integration.
Note: Not directly fetched.

**[21]** "Anthropic usage monitoring." *Honeycomb Docs*, 2026.
<https://docs.honeycomb.io/integrations/anthropic-usage-monitoring>
**Tier:** 2
Data extracted (from discovery agent): OpenTelemetry receiver for Anthropic Admin API; telemetry structure.
Note: Not directly fetched.

**[22]** "Claude rate limits." *Morphllm.com*, 2026.
<https://www.morphllm.com/claude-rate-limits>
**Tier:** 3
Data extracted (from discovery agent): Structured summary of all tiers with specific RPM/ITPM/OTPM numbers.
Note: Not directly fetched. Used for cross-reference only; official docs [1] are authoritative.

**[23]** "Quota tiers and limits." *Aifreeapi.com*, 2026.
<https://www.aifreeapi.com/en/posts/claude-api-quota-tiers-limits>
**Tier:** 3
Data extracted (from discovery agent): Tier deposit thresholds; monthly spend caps; model-specific limits.
Note: Not directly fetched. Used for cross-reference only.

**[24]** "Service tiers." *Anthropic Platform Docs*, 2026.
<https://platform.claude.com/docs/en/api/service-tiers>
**Tier:** 2
Data extracted (from discovery agent search snippets): Priority Tier description; `service_tier` request parameter; priority-specific response headers; committed spend model; 99.5% uptime target; automatic overflow to standard tier.
Note: Not directly fetched.

**[25]** "Revenium middleware for Anthropic Python." *GitHub — revenium/revenium-middleware-anthropic-python*, 2026.
<https://github.com/revenium/revenium-middleware-anthropic-python>
**Tier:** 3
Data extracted (from discovery agent): Third-party middleware wrapping Anthropic SDK; intercepts `messages.create`/`messages.stream`; metadata dict pattern.
Note: Not directly fetched.

**[26]** "AgentOps Anthropic integration." *AgentOps Docs*, 2026.
<https://docs.agentops.ai/v2/integrations/anthropic>
**Tier:** 2
Data extracted (from discovery agent): Auto-instrumentation pattern for Anthropic SDK; usage field capture.
Note: Not directly fetched.

**[27]** Simon Willison (@simonw). Post on X, 2025.
<https://x.com/simonw/status/1948480585308975493>
**Tier:** 4 (social media, but well-known practitioner)
Data extracted (from discovery agent): Confirmation that Tier 2 requires $40 cumulative; Tier 2 Sonnet ITPM raised from 40k to 450k; RPM stayed at 1,000.
Note: Not directly fetched. Used for historical context only; official docs [1] are authoritative for current values.

**[28]** "OpenLLMetry." *GitHub — traceloop/openllmetry*, 2026.
<https://github.com/traceloop/openllmetry>
**Tier:** 3
Data extracted (from discovery agent): Apache 2.0; OTel extensions for Anthropic/OpenAI/Cohere; cost span attributes for per-user/feature attribution.
Note: Not directly fetched.

**[29]** "Cost and usage reporting in Console." *Anthropic Help Center*, 2026.
<https://support.anthropic.com/en/articles/9534590-cost-and-usage-reporting-in-console>
**Tier:** 2
Data extracted (from discovery agent): Console UI cost/usage views; workspace breakdown availability.
Note: Not directly fetched.

**[30]** "Claude Code Analytics API." *Anthropic Platform Docs*, 2026.
<https://platform.claude.com/docs/en/build-with-claude/claude-code-analytics-api>
**Tier:** 2
Data extracted (from discovery agent): `/v1/organizations/usage_report/claude_code` endpoint; per-user estimated costs; productivity metrics (sessions, LOC, commits, PRs, tool acceptance rates); up to 1-hour data delay.
Note: Not directly fetched.

**[31]** "LiteLLM." *GitHub — BerriAI/litellm*, 2026.
<https://github.com/BerriAI/litellm>
**Tier:** 3
Data extracted (from discovery agent): Open-source proxy with cost tracking; Python SDK and proxy server modes.
Note: Not directly fetched.

**[32]** "BudgetManager." *LiteLLM Docs*, 2026.
<https://docs.litellm.ai/docs/budget_manager>
**Tier:** 2
Data extracted (from discovery agent): Standalone `BudgetManager` class for client-side use without proxy.
Note: Not directly fetched.
