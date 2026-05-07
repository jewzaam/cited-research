# Cost Comparison

Per-token pricing and total cost analysis for verification workload. Includes latency data where available.

## Workload Parameters

- 5 agents average per run
- 4 claims per agent = 20 total verifications
- ~3k input tokens per verification
- ~750 output tokens per verification
- **Total per run: 60k input tokens, 15k output tokens**

## Cost Per Run (Verified Pricing)

| Model | Input Cost | Output Cost | Total/Run | vs Sonnet | Source |
|---|---|---|---|---|---|
| Claude Sonnet 4.6 | $0.180 | $0.225 | **$0.405** | baseline | [1] |
| Claude Haiku 4.5 | $0.060 | $0.075 | **$0.135** | 33% | [1] |
| Gemini 2.5 Flash | $0.018 | $0.038 | **$0.056** | 14% | [5] |
| GPT-4.1-mini | $0.024 | $0.024 | **$0.048** | 12% | Unverified [8] |
| DeepSeek V4 Flash | $0.0084 | $0.0042 | **$0.013** | 3.1% | [4] |
| Gemini 2.5 Flash-Lite | $0.006 | $0.006 | **$0.012** | 3.0% | [5] |
| Qwen3 Coder Next | $0.007 | $0.012 | **$0.018** | 4.5% | Unverified [42] |

Calculations: Input cost = 60k tokens x (price/MTok / 1M). Output cost = 15k tokens x (price/MTok / 1M).

## The Dollar Amounts Are Tiny

At $0.405/run with Sonnet and 50 runs/month, annual cost is ~$243. Maximum annual savings from switching to DeepSeek V4 Flash is ~$230/year. **Integration engineering cost dominates token savings at low-to-moderate volume.**

The cost argument for non-Anthropic models is valid only at high volume (100+ runs/day) or when the per-run cost needs to approach zero for experimentation.

## Cache Pricing

| Model | Cache Hit Rate | Effective Input $/MTok |
|---|---|---|
| Claude Sonnet 4.6 | 0.1x base ($0.30) | $0.30 with caching [1] |
| DeepSeek V4 Flash | ~0.02x base ($0.0028) | $0.0028 with caching [4] |
| Gemini 2.5 Flash | $0.03/MTok + $1/MTok/hr storage | Variable [5] |

DeepSeek's cache hit pricing ($0.0028/MTok) is 107x cheaper than Claude Sonnet's cache hit ($0.30/MTok). Calculated: $0.30 / $0.0028 = 107x [4][1]. For verification agents with repeated system prompts, this dramatically reduces effective cost.

## Latency Data

All latency figures from discovery agents (not directly verified via WebFetch) [33]:

| Model | TTFT | Throughput | Est. Time for 750 tokens |
|---|---|---|---|
| Gemini 2.5 Flash-Lite | 0.29-0.38s | 392.8 t/s | ~2.3s total |
| Gemini 2.5 Flash | 0.56-0.73s | 186-194 t/s | ~4.6s total |
| GPT-4.1-mini | 0.74-0.86s | Unknown | Unknown |
| DeepSeek V4 Flash | 1.06-1.14s | 74-150 t/s | ~6.1-11.2s total |
| Claude Sonnet 4.6 | 1.03-1.36s | 63 t/s | ~13.2s total |

Est. time = TTFT + (750 tokens / throughput). Parallel agents run concurrently.

**Latency may matter more than cost.** Gemini Flash-Lite at ~2.3s/request vs Sonnet at ~13.2s means verification runs complete 5-6x faster. For interactive workflows where a human waits, this speedup has real value independent of dollar savings.

## Free Tier Coverage

| Provider | Free Tier | Runs Covered | Viable | Source |
|---|---|---|---|---|
| Google AI Studio (Flash) | 15 RPM, 1,500 RPD | 50-125/day indefinitely | Yes | [7] |
| Mistral (API) | 1B tokens/month | ~13,000+/month | Likely (RPS unknown) | Unverified |
| Together AI | $25 credit | ~800 runs | Evaluation only | [37] |
| DeepSeek | No free tier | 0 | No | [4] |
| OpenRouter | 50 RPD | 1-2 runs/day | No | [35] |

Google AI Studio is the only provider with a viable free tier for sustained verification workload [7].

## Counter-Perspective: True Cost Beyond Per-Token Pricing

**Price reversal**: In 1 in 5 model comparisons, the cheaper-listed model costs more in practice due to thinking token consumption [48]. A model generating 25x more thinking tokens reverses a 78% per-token price advantage [48].

**Retry costs**: DeepSeek's 5-12% structured output failure rate [25] means ~1 in 10-20 verification outputs needs retry. At 5% failure, expected retries add ~5.3% to effective cost. Calculated: 0.05 / (1 - 0.05) = 0.053, i.e. 5.3% expected retry overhead [25].

**Reliability compounding**: 99% per-step reliability over 10 steps = 90.4% overall [49]. Lower per-step reliability compounds faster: 95% over 10 steps = 59.9%.

## Gaps and Limitations

- GPT-4.1-mini pricing unverified — model no longer on OpenAI pricing page [8]
- Mistral API per-token pricing not verified from primary source
- Qwen3 Coder Next pricing from OpenRouter [42], not confirmed against Alibaba Cloud direct
- Latency data from aggregator benchmarks [33], not controlled experiments
- No data on thinking token overhead for different models on verification prompts
- The "20-40% operational overhead" figure from counter-discovery could not be verified
