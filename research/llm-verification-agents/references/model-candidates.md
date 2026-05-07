# Model Candidates

Models evaluated for code verification tasks in Claude Code subagent workflows. Verification involves checking binary claims against a codebase (file existence, function behavior). This is comprehension, not generation.

## Candidate Comparison

| Model | Params (total/active) | Context | Input $/MTok | Output $/MTok | SWE-bench V | Struct. Output | Training Independence |
|---|---|---|---|---|---|---|---|
| DeepSeek V4 Flash | 284B/13B MoE | 1M | $0.14 | $0.28 | 79.0%* | 5-12% miss | Compromised [26] |
| Gemini 2.5 Flash | Undisclosed | 1M | $0.30 | $2.50 | N/A | <0.3% | High |
| Gemini 2.5 Flash-Lite | Undisclosed | 1M | $0.10 | $0.40 | N/A | Unknown | High |
| GLM-4.7 | 358B dense | 200K | $0.38 | $1.74 | 73.8% | Unknown | High |
| Qwen3 Coder Next | 80B/3B MoE | 262K | $0.11 | $0.80 | 70.6% | Unknown | Compromised [28] |
| Codestral 25.08 | 22B | 256K | $0.30 | $0.90 | N/A | Unknown | High |
| GPT-4.1-mini | Undisclosed | 1M | $0.40 | $1.60 | 54.6% | <0.1% | High |
| Claude Haiku 4.5 | Undisclosed | 200K | $1.00 | $5.00 | 73.3% | <0.2% | None (same family) |

*Vendor-reported, not independently reproduced [43]

Pricing sources: [1][4][5][8]. SWE-bench scores: [42][43][44][52]. Structured output: [25].

## Individual Assessments

### DeepSeek V4 Flash

Released April 24, 2026 [4]. MoE architecture with 284B total parameters and only 13B activated per token [43]. 1M context window with 384K max output [4]. Supports JSON output and tool calls [4]. Cache hit pricing at $0.0028/MTok makes repeated verification prompts extremely cheap [4].

**Verification viability**: High on cost/capability, but structured output reliability is a concern — 5-12% schema mismatch rate in JSON mode [25] vs <0.2% for Anthropic. For verification agents outputting structured pass/fail judgments, a 5% failure rate per step compounds across a pipeline [49].

**Training independence**: Compromised. Anthropic documented industrial-scale distillation: 150,000+ Claude exchanges through ~24,000 fraudulent accounts [26][27]. This directly contaminates DeepSeek's training with Claude's error patterns and reasoning approaches. The MoE architecture differs structurally, but training data contamination undermines architectural diversity.

**Benchmark caution**: V4-Flash SWE-bench Verified 79.0% is vendor-reported only [43]. The jump from V3's ~49% to V4's ~80% is extraordinary for a single generation. SWE-bench Verified itself has contamination concerns — Claude Opus 4.5 scores 80.9% Verified but only 45.9% on SWE-bench Pro [41].

### Gemini 2.5 Flash

1M context window [5]. Built-in thinking mode and native tool use. Structured output compliance at 99.7%, degrading to 98-99% at 3-4+ nesting levels [25].

**Verification viability**: Moderate. Good structured output, 1M context, competitive pricing. Not natively OpenAI-compatible — requires Google SDK or translation proxy. No published SWE-bench Verified score for the Flash variant specifically.

**Training independence**: Highest of all candidates. Google-trained with independent research infrastructure. No known distillation of Claude's capabilities. Google disclosed in February 2026 that attackers attempted to clone *Gemini*, positioning Google as victim rather than perpetrator [26].

### GLM-4.7

Released December 22, 2025. Dense Transformer, 358B parameters [52]. 200K context. SWE-bench Verified 73.8%, HumanEval 92%, LiveCodeBench 84.9% (open-source SOTA) [52]. Available via Z.AI platform and OpenRouter at $0.38/$1.74 per MTok [52]. Open weights (MIT license).

**Verification viability**: Moderate-high. Strong independently validated benchmarks. LiveCodeBench scores are contamination-resistant (monthly updates). 200K context adequate for verification payloads. Open weights enable self-hosting if needed.

**Training independence**: High. Zhipu AI (Chinese lab), independent training pipeline. Not implicated in Claude distillation.

### Qwen3 Coder Next

Released February 4, 2026 [42]. 80B total / 3B activated MoE. 262K context. SWE-bench Verified 70.6%, SWE-bench Pro 44.3% [42]. Cheapest input pricing at $0.11/MTok [55].

**Verification viability**: Moderate. Only 3B active parameters may limit depth for nuanced code comprehension. Cheapest option for high-volume verification runs.

**Training independence**: Compromised. Qwen 2.5-72B identifies itself as "Claude, made by Anthropic" when asked about identity [28], indicating training on Claude-generated synthetic data. Community has created intentional distillations of Claude reasoning into Qwen models.

### Codestral 25.08

22B parameters. 256K context (the older 25.01 version has only 32K) [40][41]. FIM (Fill-in-the-Middle) score of 95.3% — the closest standard benchmark to verification tasks, testing comprehension of surrounding code context [40].

**Verification viability**: Moderate-low. Strong FIM performance directly maps to "does this function do X?" verification. However, documented weakness at multi-file coordination [40]. Pricing at $0.30/$0.90 is reasonable.

**Training independence**: High. Mistral (French lab), independent architecture and training.

### GPT-4.1-mini

1M context window [44]. Highest structured output reliability (<0.1%) [25] and tool use F1 (0.974) [31]. However, no longer listed on OpenAI's pricing page as of May 2026 [8] — superseded by gpt-5.4 series.

**Verification viability**: Low-moderate due to deprecation risk. Building verification infrastructure on a model removed from the pricing page is risky. SWE-bench Verified at 54.6% [44] is the lowest of all candidates.

### Claude Haiku 4.5 (Excluded)

**Not recommended for this use case.** Using another Claude model to verify Claude's output creates within-family behavioral entanglement [15]. Intra-family error correlation is highest (BEI=0.0446 for Llama family pairs) [15]. Claude Haiku and Claude Opus/Sonnet share training data, RLHF alignment, and architectural patterns. This would create "a consensus of correlated errors rather than independent verification" [15].

## Benchmark Limitations

HumanEval scores do not predict real-world code comprehension. A model scoring 94% on HumanEval solves only 23% of real engineering tasks [32]. SWE-bench Verified has contamination concerns [41]. FIM is the closest proxy for verification tasks [40]. LiveCodeBench (monthly updates, contamination-free) is the most trustworthy benchmark for code capability assessment.

Semantic-preserving mutations (variable renaming, dead code insertion) cause LLMs to fail at localizing faults they previously found correctly in 78% of cases [19]. This applies directly to verification — surface-level pattern matching produces false positives/negatives.

## Gaps and Limitations

- No benchmark specifically measures binary claim verification against code
- Structured output reliability data for GLM-4.7, Codestral, and Qwen3 Coder Next is missing
- DeepSeek V4 Flash benchmark claims are vendor-reported only, not independently reproduced
- Context window degradation profiles are not available for most candidates at verification-specific tasks
