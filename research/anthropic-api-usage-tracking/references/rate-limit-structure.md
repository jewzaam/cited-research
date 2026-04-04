# Rate Limit Structure

This reference covers Dimension 6: the actual rate limits (RPM, ITPM, OTPM), the tier system, how limits scale with plan level, and the token bucket algorithm.

Source details: [citations.md](../citations.md)

---

## Two Types of Limits

The API enforces two distinct limit categories [1]:

1. **Spend limits** — maximum monthly cost an organization can incur (calendar month)
2. **Rate limits** — maximum API requests/tokens over a defined period (per minute)

These are independent controls: rate limits govern throughput; spend limits cap total monthly cost [1].

## Spend Limit Tiers

Tier advancement is automatic and immediate upon reaching the cumulative credit purchase threshold [1] [11].

| Usage Tier | Cumulative Credit Purchase | Max Single Purchase | Monthly Spend Limit |
|------------|---------------------------|---------------------|---------------------|
| Tier 1 | $5 | $100 | $100 |
| Tier 2 | $40 | $500 | $500 |
| Tier 3 | $200 | $1,000 | $1,000 |
| Tier 4 | $400 | $200,000 | $200,000 |
| Monthly Invoicing | N/A | N/A | No limit |

Credit purchase amounts are cumulative and exclude tax [1]. Monthly Invoicing removes the spend cap and uses Net-30 payment terms [1].

Organizations can also set a **customer-set spend limit** lower than their tier ceiling via Console → Settings → Limits [1]. This limit cannot exceed the tier-enforced ceiling.

## Rate Limit Tables

Rate limits are measured per model class in RPM, ITPM, and OTPM [1]. Limits apply at the organization level and are shared across all `inference_geo` values [1].

### Tier 1

| Model | RPM | ITPM | OTPM |
|-------|-----|------|------|
| Claude Opus 4.x (combined) | 50 | 30,000 | 8,000 |
| Claude Sonnet 4.x (combined) | 50 | 30,000 | 8,000 |
| Claude Haiku 4.5 | 50 | 50,000 | 10,000 |
| Claude Haiku 3.5† | 50 | 50,000† | 10,000 |
| Claude Haiku 3† | 50 | 50,000† | 10,000 |

### Tier 2

| Model | RPM | ITPM | OTPM |
|-------|-----|------|------|
| Claude Opus 4.x | 1,000 | 450,000 | 90,000 |
| Claude Sonnet 4.x | 1,000 | 450,000 | 90,000 |
| Claude Haiku 4.5 | 1,000 | 450,000 | 90,000 |
| Claude Haiku 3.5† | 1,000 | 100,000† | 20,000 |
| Claude Haiku 3† | 1,000 | 100,000† | 20,000 |

### Tier 3

| Model | RPM | ITPM | OTPM |
|-------|-----|------|------|
| Claude Opus 4.x | 2,000 | 800,000 | 160,000 |
| Claude Sonnet 4.x | 2,000 | 800,000 | 160,000 |
| Claude Haiku 4.5 | 2,000 | 1,000,000 | 200,000 |
| Claude Haiku 3.5† | 2,000 | 200,000† | 40,000 |
| Claude Haiku 3† | 2,000 | 200,000† | 40,000 |

### Tier 4

| Model | RPM | ITPM | OTPM |
|-------|-----|------|------|
| Claude Opus 4.x | 4,000 | 2,000,000 | 400,000 |
| Claude Sonnet 4.x | 4,000 | 2,000,000 | 400,000 |
| Claude Haiku 4.5 | 4,000 | 4,000,000 | 800,000 |
| Claude Haiku 3.5† | 4,000 | 400,000† | 80,000 |
| Claude Haiku 3† | 4,000 | 400,000† | 80,000 |

**Notes:**
- † Models marked with † also count `cache_read_input_tokens` toward ITPM [1]
- Opus 4.x limit is shared across Opus 4.6, 4.5, 4.1, and 4 [1]
- Sonnet 4.x limit is shared across Sonnet 4.6, 4.5, and 4 [1]
- Claude Sonnet 3.7 (deprecated) has separate, lower limits at each tier [1]

## Token Bucket Algorithm

The API uses the **token bucket algorithm** for rate limiting [1]. Key characteristics:

- Capacity replenishes **continuously**, not at fixed minute boundaries [1]
- Short bursts can exceed the sustained rate if the bucket has accumulated capacity [1]
- Sub-minute enforcement: a 60 RPM limit may be enforced as ~1 request per second; short bursts can trigger 429s even when the average rate is within bounds [1]

## Cache-Aware ITPM

For most Claude models, **only uncached input tokens count toward ITPM** [1]:

- `input_tokens` (after last cache breakpoint) — **counts** toward ITPM
- `cache_creation_input_tokens` — **counts** toward ITPM
- `cache_read_input_tokens` — **does NOT count** toward ITPM (for most models)

Example: with a 2,000,000 ITPM limit and 80% cache hit rate, effective throughput is ~10,000,000 total input tokens per minute [1].

ITPM is estimated at request start and adjusted during the request to reflect actual usage [1].

OTPM is evaluated in real time as output tokens are produced. The `max_tokens` parameter does **not** factor into OTPM calculations [1].

## Acceleration Limits

Organizations may encounter 429 errors due to **acceleration limits** if usage increases sharply. The recommendation is to ramp up traffic gradually and maintain consistent patterns [1].

## Workspace Rate Limits

Organizations can set per-workspace rate and spend limits to protect against overuse by one workspace [1]:

- Cannot be set on the default workspace
- If not set, workspace limits match the organization limit
- Organization-wide limits always apply even if workspace limits sum to more
- Currently limited to total tokens per minute; separate input/output limits for workspaces are planned [1]

## Batch API Rate Limits

The Message Batches API has its own limits, shared across all models [1]:

| Tier | RPM | Max Batch Requests in Queue | Max per Batch |
|------|-----|-----------------------------|---------------|
| Tier 1 | 50 | 100,000 | 100,000 |
| Tier 2 | 1,000 | 200,000 | 100,000 |
| Tier 3 | 2,000 | 300,000 | 100,000 |
| Tier 4 | 4,000 | 500,000 | 100,000 |

## Console Monitoring

The Usage page in the Claude Console provides rate limit charts showing [1]:
- Hourly maximum uncached input tokens per minute vs. current ITPM limit
- Cache hit rate percentage
- Hourly maximum output tokens per minute vs. current OTPM limit

## Gaps and Limitations

- Enterprise/custom tier limits are not published; they require contacting sales [1].
- Fast mode rate limits for Opus 4.6 are described as "dedicated" and separate from standard Opus limits, but specific numbers are not in the rate limits page [1].
- No documentation of daily or weekly aggregate rate limits was found in the fetched sources. Discovery agents mentioned "weekly rate limits for Claude Code" introduced August 2025, but this was not confirmed in the official rate limits page [1].
