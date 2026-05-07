# Alternative LLM Models for Verification Agents in Claude Code Subagent Workflows

## Research Question

Can non-Anthropic models serve as verification agents in Claude Code subagent workflows, providing failure mode diversity at equal or lower cost than Claude Sonnet?

## Methodology

Six dimensions were researched across two iterations. Iteration 1 dispatched 12 parallel agents (6 discovery + 6 counter-discovery, Sonnet) for WebSearch-based URL discovery with multi-engine augmentation via DuckDuckGo. Iteration 2 dispatched 6 analysis agents (Opus) that deep-read fetched content from official documentation, academic papers, and GitHub issues.

55 sources were cited, spanning official API documentation (Tier 2), peer-reviewed papers (Tier 1), and industry analyses (Tier 3). Key claims were verified by fetching primary sources: pricing from official API docs, integration mechanics from Anthropic's documentation, and error correlation data from academic papers.

Counter-perspectives were searched for each dimension and included without distinction in the citation pool.

## Key Findings

### 1. Claude Code Does Not Support Non-Anthropic Subagents

The most consequential finding: Claude Code's subagent system is locked to Anthropic models. The Agent tool's model parameter accepts only `sonnet`, `opus`, `haiku`, or full Anthropic model IDs [2][3][10]. GitHub issue #34821 requesting custom model aliases was closed as "not planned" [10]. Two active bugs (#43869, #47488) affect even the supported model routing [11][12].

Claude Code requires Anthropic Messages API format — not OpenAI chat completions [2]. Using non-Anthropic models requires either:

1. **External verification harness** (recommended) — run verification outside Claude Code via hooks, using non-Anthropic models' native APIs directly [3]
2. **Alias hijacking via proxy** (fragile) — hijack the 3 built-in aliases via `ANTHROPIC_DEFAULT_*_MODEL` env vars pointing to a LiteLLM proxy that translates between API formats [10]

See [claude-code-integration.md](references/claude-code-integration.md) for full analysis.

### 2. Failure Mode Diversity Is Real but Limited

Cross-model verification provides measurable but bounded benefit:

- **Cross-model disagreement detects confident errors** with 0.75 AUROC vs 0.59 for self-evaluation — a 27% relative improvement [17]
- **Best 2-agent pair reaches 79.3% accuracy** vs 32.8% for single agents in code verification [16]
- **Error correlation is above random**: model pairs agree on wrong answers 60% of the time (Helm) vs 33% random baseline [14]
- **More capable models have MORE correlated errors** (p<0.001), not fewer [14]
- **Consensus at 25x cost yields no accuracy gain** on truthfulness benchmarks [18]
- **Cross-family correlation (rho=0.4-0.5) is lower than within-family (rho=0.7-0.8)** [24], confirming that different families provide partial — not independent — verification

The cheapest diversity candidates are compromised:
- **DeepSeek**: 150,000+ Claude exchanges distilled via ~24,000 fraudulent accounts [26][27]
- **Qwen**: 2.5-72B identifies itself as "Claude, made by Anthropic" [28]
- **Gemini**: Most independent training lineage — no known Claude distillation [26]

See [failure-mode-diversity.md](references/failure-mode-diversity.md) for full analysis.

### 3. Cost Savings Are Real but Small in Absolute Terms

| Model | Cost/Run | vs Sonnet | Source |
|---|---|---|---|
| Claude Sonnet 4.6 | $0.405 | baseline | [1] |
| Claude Haiku 4.5 | $0.135 | 33% | [1] |
| Gemini 2.5 Flash | $0.056 | 14% | [5] |
| DeepSeek V4 Flash | $0.013 | 3.1% | [4] |
| Gemini 2.5 Flash-Lite | $0.012 | 3.0% | [5] |

At 50 runs/month, annual Sonnet cost is ~$243. Maximum annual savings from the cheapest alternative is ~$230. **Integration engineering cost dominates token savings at low-to-moderate volume.** The cost argument is valid only at high volume or when per-run cost must approach zero.

Latency may matter more than cost: Gemini Flash-Lite completes verification ~5-6x faster than Sonnet [33].

See [cost-comparison.md](references/cost-comparison.md) for full analysis.

### 4. Structured Output Reliability Varies Dramatically

| Provider | Parse Failure Rate | Source |
|---|---|---|
| OpenAI Structured Outputs | <0.1% | [25] |
| Anthropic Claude Tool Use | <0.2% | [25] |
| Google Gemini | <0.3% | [25] |
| DeepSeek JSON mode | 5-12% | [25] |

DeepSeek's 5-12% failure rate compounds across a pipeline: 4 agents at 95% reliability = 81.5% pipeline reliability [25][49]. This effectively disqualifies DeepSeek for structured verification without robust retry logic, despite its pricing advantage.

50-69% of correct answers from small LMs contain flawed reasoning — the "Right-for-Wrong-Reasons" phenomenon [20]. Verification agents that reach right conclusions via wrong reasoning create false confidence.

See [reliability.md](references/reliability.md) for full analysis.

### 5. Recommended Candidates

| Rank | Model | Rationale | Best For |
|---|---|---|---|
| 1 | **Gemini 2.5 Flash** | Most independent from Claude, <0.3% parse failure, free tier viable | Maximum diversity |
| 2 | **GLM-4.7** | Independently validated benchmarks, open weights, high independence | Validated capability |
| 3 | **Claude Haiku 4.5** | Native integration, <0.2% parse failure, lowest friction | Pragmatic choice (same family) |
| 4 | **DeepSeek V4 Flash** | Cheapest, 1M context — but compromised independence, 5-12% parse failure | Cost-only optimization |
| 5 | **Qwen3 Coder Next** | Cheapest input — but compromised independence | Budget experiments |

**Claude Haiku 4.5 remains the pragmatic default** despite same-family entanglement [15]. For mechanical/structural verification (schema matching, file existence, format compliance), intra-family correlation matters less than for reasoning-heavy tasks. The zero integration friction outweighs theoretical diversity benefits when:
- The verification task is mechanical, not reasoning-heavy
- Integration engineering budget is limited
- Volume is low enough that per-token cost is negligible

**Gemini 2.5 Flash is the diversity choice** when cross-family independence is the priority. It requires an external harness (not native Claude Code subagent), but provides the highest training independence and adequate structured output reliability.

### 6. Model Candidates Summary

See [model-candidates.md](references/model-candidates.md) for detailed per-model assessments including context windows, benchmark scores, and API compatibility.

### 7. Provider Assessment

Google AI Studio is the only provider with confirmed adequate free tier rate limits (15 RPM, 1,500 RPD for Flash) [7]. LLM API uptime industry average is ~99.3% (5+ hours downtime/month), 7x worse than traditional cloud [47]. No evaluated provider offers an SLA for LLM API access.

See [provider-options.md](references/provider-options.md) for full provider analysis.

## Framing Challenge Outcomes

Three assumptions were challenged at the start of this research:

1. **"Cross-model = diverse failure modes"** — Partially true. Cross-family correlation (rho=0.4-0.5) IS lower than within-family (rho=0.7-0.8) [24], but errors are still correlated well above random [14]. DeepSeek and Qwen's Claude contamination further reduces diversity for the cheapest options [26][28].

2. **"API-hosted scope is sufficient"** — True with caveats. All viable candidates are API-available. The scope exclusion of self-hosted models means we miss models with the most independent training pipelines (e.g., locally fine-tuned models), but the cost/convenience tradeoff is appropriate for verification agents.

3. **"Subagent model override works as documented"** — False. The override is restricted to Anthropic models [2][3][10], and active bugs affect even that (#43869, #47488) [11][12]. This is the single most impactful finding.

## Decision Framework

```
Is verification reasoning-heavy or mechanical?
├─ Mechanical (schema, format, existence checks)
│  └─ Claude Haiku 4.5 via native subagent
│     Cost: $0.135/run, Friction: zero
│
├─ Reasoning-heavy (code correctness, logic verification)
│  ├─ Is failure mode diversity critical?
│  │  ├─ Yes → Gemini 2.5 Flash via external harness
│  │  │  Cost: $0.056/run + engineering, Friction: high
│  │  └─ No → Claude Haiku 4.5 via native subagent
│  │     (accept intra-family correlation risk)
│  │
│  └─ Is cost the binding constraint?
│     ├─ Yes → DeepSeek V4 Flash via external harness
│     │  Cost: $0.013/run + engineering
│     │  Caveat: 5-12% parse failure, Claude contamination
│     └─ No → Claude Sonnet 4.6 via native subagent
│        Cost: $0.405/run, highest quality
│
└─ Consider: deterministic verification (tests, linters, type checkers)
   provides truly independent error detection with no LLM integration friction
```

## Reflection

After assembling this analysis, I reconsidered three areas:

1. **DeepSeek's diversity value is overstated by its pricing**. The $0.013/run cost draws attention, but the documented Claude distillation [26][27] means DeepSeek's errors are partially Claude's errors by construction. The diversity benefit is lower than the architectural difference (MoE vs Transformer) would suggest.

2. **The integration barrier is underappreciated**. Every non-Anthropic option requires building infrastructure outside Claude Code's subagent system. This is not a temporary limitation — the feature request was explicitly closed as "not planned" [10]. The research question may need to be reframed: not "which model?" but "is an external verification harness worth building?"

3. **Mechanical vs reasoning verification is the key distinction**. For mechanical checks, Claude Haiku's intra-family entanglement is less concerning because the errors being checked are structural, not interpretive. The diversity argument is strongest for reasoning-heavy verification, which is also where implementation complexity is highest.

## Limitations

- No benchmark specifically measures binary claim verification against code
- Structured output reliability data for GLM-4.7, Codestral, and Qwen3 Coder Next is missing [25]
- Error correlation data is from MCQ benchmarks, not code comprehension specifically [14]
- Within-Claude-family entanglement has not been directly measured (extrapolated from Llama data) [15]
- DeepSeek V4 Flash benchmark claims are vendor-reported only [43]
- GPT-4.1-mini pricing/availability unverifiable — removed from OpenAI pricing page [8]
- Latency data from aggregator benchmarks, not controlled experiments [33]
- The "Right-for-Wrong-Reasons" finding applies most directly to small models; frontier rates unknown [20]
