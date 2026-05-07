# Provider Options

Providers evaluated for hosting verification agents. Workload: 4-6 parallel agents, 3-5 claims each, ~60k input + ~15k output tokens per run.

## Provider Comparison

| Provider | Cost/Run (cheapest model) | Free Tier | Parallel Support | Uptime | SLA |
|---|---|---|---|---|---|
| Google AI Studio | $0.012 (Flash-Lite) | 1,500 RPD [7] | 15-30 RPM [7] | Google infra | No (preview) |
| DeepInfra | $0.006 (Qwen3-235B) | Unverified | 200 concurrent [38] | Growing | No |
| DeepSeek Direct | $0.013 (V4 Flash) | No | Dynamic [6] | 99.51% claimed | No |
| Mistral Direct | $0.008 (Ministral 8B) | 1B tokens/mo | Unknown RPS | Unknown | No |
| OpenRouter | Varies + 5.5% [34] | 50 RPD [35] | $1=1 RPS [35] | ~99.3% | No |
| Together AI | $0.014 (Llama 8B) | $25 credit [37] | Dynamic [36] | Problematic | No |
| Alibaba Cloud | ~$0.006 (est.) | 1M tokens/90d [39] | Unknown | Unknown | Unknown |

## Detailed Assessments

### Google AI Studio (Recommended)

**Pricing**: Gemini 2.5 Flash $0.30/$2.50 per MTok; Flash-Lite $0.10/$0.40 [5]. Batch 50% discount [5]. Context caching $0.03/MTok + $1.00/MTok/hour [5].

**Rate limits**: Free tier Flash at 15 RPM, 1,500 RPD; Flash-Lite at 30 RPM, 1,500 RPD [7]. This is the only provider with confirmed adequate free tier rate limits for 4-6 parallel verification agents. A burst of 6 simultaneous requests fits within 15 RPM. 1,500 RPD supports 50-125 verification runs/day. Paid Tier 1 gives 150-300 RPM [7].

**Risk**: Google slashed free tier quotas 50-80% in December 2025 [53]. Quotas have since been adjusted upward for some models. The disclaimer "specified limits are not guaranteed" [7] means capacity can be reduced without notice.

**Recommendation**: Best overall choice for verification workload at the free tier. The combination of adequate rate limits, reasonable pricing, and Google infrastructure stability outweighs the quota instability risk.

### DeepSeek Direct

**Pricing**: V4 Flash $0.14/$0.28 per MTok, cache hit $0.0028 [4]. V4 Pro $0.435/$0.87 (75% discount through May 31, 2026; regular $1.74/$3.48) [4]. 1M context, 384K max output [4].

**Rate limits**: Dynamic concurrency-based, no fixed RPM/TPM [6]. HTTP 429 on overload [6]. Earlier announcement claimed "no limits on concurrency" but that was August 2024 for a prior API version. Current docs confirm dynamic limiting [6]. Recommended starting concurrency: 8-16 parallel requests per discovery agent findings (unverified against primary source).

**Reliability**: Multiple sources track significant outage history. January 2025 saw consecutive outages during viral adoption surge. March 30, 2026 outage lasting 7h13m. No SLA.

**Risk**: V4 Pro discount expires May 31, 2026 (4x price increase) [4]. Dynamic rate limiting means capacity not guaranteed during peak demand. Chinese provider with potential regulatory considerations.

### OpenRouter (Aggregator)

**Pricing**: 5.5% fee on credit purchases [34]. Passes through underlying provider rates. BYOK option eliminates fees for first 1M requests/month [34].

**Rate limits**: Free tier 20 RPM, 50 RPD — insufficient (18-30 requests per verification run burns 36-60% of daily quota) [35]. Paid tier: $1 balance = 1 concurrent RPS, max 500 [35]. A $10 balance gives 10 RPS, more than sufficient.

**Reliability**: 46+ outages tracked by StatusGator over past year. February 2026 outages with 80-90% failure rates at peak, 38-minute durations [45]. No SLA. Adds 25-40ms latency per request.

### Together AI

**Pricing**: Model-dependent serverless pricing [37]. $25 free credit for new users [37]. Batch inference with 50% discount.

**Rate limits**: Dynamic per-model, not published [36]. Together AI explicitly does not publish fixed tier thresholds. Limits visible only in API response headers.

**Reliability**: 764 incidents tracked by IsDown since March 2025, average resolution 66 minutes [46]. 4,889 outages tracked by StatusGator across 30 components. Gap between official status page and third-party monitors is notable.

### DeepInfra

**Pricing**: Per-token, varies by model [38]. Generally competitive. 200 concurrent requests per model per account [38].

**Rate limits**: 200 concurrent per model [38]. 4-6 parallel agents trivially within limits. Higher limits available on request.

**Reliability**: Raised $107M Series B in May 2026. Processes ~5 trillion tokens/week. No published SLA. Free trial exists but exact credit amount unverified.

### Alibaba Cloud (Qwen)

**Pricing**: Tiered billing based on input size per request [39]. 1M input + 1M output tokens free for 90 days, Singapore region only [39]. Batch 50% discount [39].

**Rate limits**: Not publicly documented. RPM and TPM limits apply per model but exact thresholds not published [39].

**Free tier viability**: 1M tokens covers only ~16 verification runs. Not viable for sustained use.

## Gaps and Limitations

- Mistral API rate limits (RPS) not publicly documented — exact parallel agent viability unknown
- DeepInfra free tier credit amount unverified
- None of these providers offer SLAs for LLM API access
- LLM API uptime industry average is ~99.3% (5+ hours downtime/month), 7x worse than traditional cloud [47]
- Provider pricing is volatile — 30-50% annual drops historically, but Google demonstrated willingness to slash quotas [53]
