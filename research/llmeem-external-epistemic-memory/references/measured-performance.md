# Measured Performance

All performance claims originate from llmeem.ai [1]. No independent peer review or external validation has been published. All evaluation was conducted by the project creator (Ben Thomasson).

## Primary Benchmarks

### Overall Quality: 98.5% A/B Grade

| Metric | Value | Conditions |
|--------|-------|------------|
| Grade | 98.5% A/B | Claude Opus 4.6, May 2026 |
| Questions | 3,853 | Automated rubric-based scoring |
| D/F grades | Zero | "Eliminated the failure tail entirely" |

Architecture: dual-path retrieval (BMS + FTS + merge) [1].

### Expert Service vs. Baseline: 88% vs. 33%

| System | A-grade | Model | Questions |
|--------|---------|-------|-----------|
| EEM expert-service | 88% | Claude Opus 4.6 | 50 Red Hat domain |
| Agent pipeline baseline | 33% | Claude Opus 4.6 | 50 Red Hat domain |

15x speed improvement claimed [1]. Baseline specification not fully documented.

### Model Compensation

Smaller models with EEM approximate larger models without it [1]:

| Configuration | A+B Grade |
|--------------|-----------|
| Opus 4.6 (baseline) | 98% |
| Haiku 4.5 + dual-path | 94% |
| Sonnet + beliefs | ≈ Opus without beliefs |

Grade scale (A/B/C/D/F) not defined numerically [1].

### Cognitive Budget Ablation

| Architecture | Accuracy | Model |
|-------------|----------|-------|
| Single prompt (beliefs + chunks mixed) | 86% | Opus 4.6 |
| Three focused passes (BMS, RAG, merge) | 100% | Opus 4.6 |

95.5% baseline drops to 86% when paths are mixed [1].

## Failure Mode Findings

### Self-Critique Failure: 87% → 60%

| Metric | Value |
|--------|-------|
| Initial accuracy | 87% |
| After self-critique revision | 60% |
| Model | Sonnet 4.6 |
| Invocations | 1,650 (55 questions × 3 conditions × 2 models × 5 runs) |
| Date | March 2026 |

Root cause: "same model that produced error evaluates the error" [1].

This finding is corroborated by independent research:
- GPT-4 on GSM8K drops 95.5% → 89.0% through self-correction rounds [25]
- Snorkel AI: Claude Sonnet 4.5 drops 98.1% → 56.9% on easy tasks with 5 critique iterations [9]
- Self-correction without external feedback "reliably degrades reasoning accuracy" [25]

### Confidence Unreliability

| Model | Correlation (r) | Significance |
|-------|-----------------|-------------|
| Sonnet 4.6 | 0.135 | Not significant at p<0.05 |
| Opus 4.6 | −0.045 | Worse than random |

Tested across 1,650 invocations (55 questions × 3 conditions × 2 models × 5 runs), March 2026 [1].

Independent corroboration:
- JMIR study: inverse correlation between model accuracy and confidence (r=−0.40, P=.001) [51]
- 86% of LLM predictions exceed 0.8 confidence regardless of correctness [30]
- Mean confidence difference between correct and incorrect responses: 0.6–5.4% [28]

### Expert Prompt Paradox

| Configuration | Accuracy | Model |
|--------------|----------|-------|
| Beliefs only | 100% | Opus 4.6 |
| Beliefs + expert prompt | 94.2% | Opus 4.6 |
| Beliefs only | 94.2% | Sonnet 4.6 |
| Beliefs + expert prompt | 91.8% | Sonnet 4.6 |

"Humble generic prompt produces better results because agent consults knowledge base instead of trusting expertise" [1].

Independent corroboration:
- MMLU: expert persona drops accuracy 71.6% → 66.3% [26]
- Llama-3.1-8B with expert persona: 68.4% → 46.3% (−22.1 points) [26]

### Derive-Then-Review Retraction Rate

13–37% of derived beliefs retracted per review round [1]. Range not explained — likely varies by domain and knowledge base maturity.

## Methodological Concerns

1. **No independent validation**: All benchmarks self-reported by project creator [1]
2. **Automated rubric scoring**: Methodology not detailed; LLM-as-judge biases documented (48.4% of verdicts reversed under mirrored order [27])
3. **Small comparison sample**: 50-question expert service evaluation may have wide confidence intervals
4. **Grade scale undefined**: A/B/C/D/F thresholds not specified numerically [1]
5. **Baseline underspecified**: "Agent pipeline baseline" composition not fully documented [1]
6. **Evaluation datasets not public**: Red Hat domain questions not available for independent reproduction

## Gaps and Limitations

1. **Statistical power**: 90% accuracy on 50 examples represents 75–98% true performance at 95% confidence
2. **LLM-as-judge bias**: Positional, verbosity, self-enhancement, and style biases documented across multiple studies [27]
3. **Benchmark contamination risk**: Public benchmarks may leak into training sets [counter-discovery findings]
4. **No ablation on scale**: Performance not tested across knowledge base sizes (237 vs. 12,731 beliefs)
