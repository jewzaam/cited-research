# Reliability

Tool use support, structured output reliability, rate limiting under parallel load, and effective context window quality for verification agents.

## Structured Output Parse Failure Rates

Data from TokenMix benchmarking (300K-500K test calls per provider) [25]:

| Provider/Model | Parse Failure Rate | Schema Compliance | Test Volume |
|---|---|---|---|
| OpenAI Structured Outputs | <0.1% | 99.9%+ | 500K calls |
| Anthropic Claude Tool Use | <0.2% | 99.8% | 300K calls |
| Google Gemini | <0.3% | 99.7% | Not specified |
| DeepSeek JSON mode | 5-12% | 88-95% | Not specified |
| Llama 4 (open-source) | 10-15% | 85-90% | Not specified |
| Small models (8B) | 15-25% | 75-85% | Not specified |

Gemini compliance degrades to 98-99% at 3-4+ nesting levels [25]. DeepSeek's 5-12% schema mismatch is disqualifying for structured verification — a 5% failure rate per step in a 10-step pipeline compounds to ~40% overall failure [49].

**Token overhead per approach** [25]:

| Approach | Overhead |
|---|---|
| OpenAI Structured Outputs | 80-120 tokens |
| Anthropic Tool Use | 150-300 tokens |
| Gemini Response Schema | 60-100 tokens |
| OpenAI JSON Mode | ~50 tokens |
| DeepSeek JSON | ~30 tokens |

## Tool Use / Function Calling

From Docker-based evaluation [31]:

| Model | F1 Score | Latency | Notes |
|---|---|---|---|
| GPT-4 | 0.974 | ~5s | Highest accuracy |
| Qwen 3 14B | 0.971 | ~142s | Good accuracy but impractically slow |
| Claude 3 Haiku | 0.933 | 3.56s | Best latency-to-accuracy ratio |

Claude Sonnet 4.5 leads multi-turn tool use with 0.862 tau-bench retail score (3.8 points ahead of next competitor) per discovery agent findings (unverified against primary source).

## Rate Limiting Under Parallel Load (4-6 Agents)

| Provider | Mechanism | Limits for Verification Workload | Source |
|---|---|---|---|
| Anthropic | Token bucket, continuous replenishment | Adequate at Tier 2+; burst issues at lower tiers | [1] |
| Google | RPM/TPM/RPD, project-level | Free: 15 RPM adequate; Paid: 150+ RPM | [7] |
| DeepSeek | Dynamic concurrency, no fixed limits | Unpredictable; HTTP 429 under load | [6] |
| OpenAI | RPM/TPM/RPD/TPD rolling windows | Adequate at Tier 2+ | [8] |
| OpenRouter | $1 = 1 concurrent RPS | $10 balance = 10 RPS, sufficient | [35] |
| Together AI | Dynamic, not published | Unpredictable | [36] |

**Industry error rates** from Datadog [30]: February 2026 saw 5% of LLM API call spans with errors, 60% from rate limits. By March 2026, 2% errors with 33% from rate limits (8.4M total). Rate limiting is the dominant source of API errors industry-wide.

## Context Window: Advertised vs Effective

All models exceed the 32K minimum requirement for verification payloads. Typical verification tasks use 3.5-26K tokens (instructions + content + schema), with complex cases reaching ~50K.

From discovery agents (not directly verified via WebFetch):
- Effective context typically 60-70% of advertised maximum [29]
- 18 frontier models tested by Chroma — all showed degradation with no exceptions [29]
- RULER benchmark: 50-65% reliability across current models
- Gemini 1.5 Pro: exceptional — holds at 94.4% accuracy at 128K (only 2.3-point drop)
- GPT-4-1106: drops from 96.6% (4K) to 81.2% (128K)
- DeepSeek R1: speed degradation to 1-2 t/s at max context

**Assessment**: Context window is not a binding constraint for this use case. Even at 60% effective capacity, the smallest candidate (GLM-4.7 at 200K) has 120K effective — 2-5x the largest realistic verification payload.

## Right-for-Wrong-Reasons Risk

50-69% of correct answers from small language models contain flawed reasoning [20]. Standard accuracy metrics miss this entirely — a verification agent that produces the right conclusion via wrong reasoning creates false confidence.

This is most dangerous for reasoning-heavy verification ("is this code correct?") and less concerning for mechanical verification ("does this file exist?", "does this JSON match this schema?"). For the binary claim checking use case, structuring verification as mechanical checks rather than reasoning tasks partially mitigates this risk.

## Reliability Compounding

99% per-step reliability over 10 steps = 90.4% overall. 95% per-step = 59.9% over 10 steps [49]. Each verification agent is a step. With 4-6 parallel agents, overall pipeline reliability is:

| Per-Agent Reliability | 4 Agents | 6 Agents |
|---|---|---|
| 99% | 96.1% | 94.1% |
| 95% | 81.5% | 73.5% |
| 90% | 65.6% | 53.1% |

DeepSeek's 5-12% structured output failure rate implies ~88-95% per-step reliability, leading to 65-81% pipeline reliability with 4 agents [25][49].

## Reliability Ranking for Verification

1. **Claude Haiku 4.5** — <0.2% parse failure, 3.56s latency, native integration. Intra-family correlation risk is real but mitigated for mechanical/structural checks.
2. **Gemini 2.5 Flash** — <0.3% parse failure, native tool use, 1M context. Requires translation proxy.
3. **GPT-4.1-mini** — <0.1% parse failure (best), 0.974 F1 tool use (best). Deprecation risk.
4. **DeepSeek V4 Flash** — 5-12% parse failure disqualifies for structured verification without robust retry logic.
5. **Qwen/Llama/small models** — 10-25% failure rates, impractical latency for some models.

## API Uptime

LLM API uptime industry average: ~99.3% (5+ hours downtime/month), 7x worse than traditional cloud infrastructure [47]. No provider in this evaluation offers an SLA for LLM API access. Enterprise options (Azure OpenAI, Amazon Bedrock) offer 99.9% uptime SLAs but add infrastructure complexity.

## Gaps and Limitations

- Structured output data from a single commercial source (TokenMix) [25]; not independently replicated
- Tool use F1/latency from a single Docker evaluation [31]; model versions and prompts may not match verification use case
- Context window degradation data [29] not verified against primary source (Chroma research)
- Production error rates [30] are aggregate across unspecified model mix
- Right-for-Wrong-Reasons finding [20] applies most directly to small models; frontier model rates unknown
- No structured output reliability data for GLM-4.7, Codestral, or Qwen3 Coder Next
