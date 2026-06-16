# Limitations and Failure Modes

EEM inherits limitations from both its symbolic BMS architecture and its reliance on LLMs for semantic operations.

## Self-Critique Failure

LLMeem's own testing found accuracy dropped from 87% to 60% when Sonnet 4.6 revised based on self-assessed confidence across 1,650 invocations [1].

This is well-corroborated by independent research:

| Study | Finding |
|-------|---------|
| ICLR 2024 (Google DeepMind) | GPT-4 on GSM8K: 95.5% → 89.0% through intrinsic self-correction [25] |
| Snorkel AI (Dec 2025) | Claude Sonnet 4.5: 98.1% → 56.9% on easy tasks with 5 critique iterations [9] |
| Yang et al. (Dec 2024) | Self-correction decomposes into confidence vs. critique; improving one declines the other [10] |

The mechanism: on tasks where initial accuracy is high (≥75%), critics hallucinate flaws in correct answers. "Confidence became a liability" [9]. Self-critique only helps on hard tasks (<35% initial accuracy) where real errors exist to catch [9].

**Implication for EEM**: The `review-beliefs` operation uses LLM-driven critique. If the belief is already correct, review may retract it incorrectly. The 13–37% retraction rate [1] likely includes both genuine errors and false retractions.

## Confidence Unreliability

| Model | Correlation (r) | Interpretation |
|-------|-----------------|---------------|
| Sonnet 4.6 | 0.135 | Not significant at p<0.05 [1] |
| Opus 4.6 | −0.045 | Worse than random [1] |

Independent findings:
- JMIR: inverse correlation between model performance and confidence (r=−0.40, P=.001) [51]
- 86% of LLM predictions exceed 0.8 confidence [30]
- SFT produces calibrated confidence, but RL/DPO induces overconfidence [30]
- "Asking your LLM 'Are you sure?' is a terrible idea" [28]

**Implication**: EEM's shift from "am I sure?" to "is this justified?" [1] directly addresses this — beliefs are IN/OUT based on justification chains rather than confidence scores. This is architecturally sound.

## Expert Prompt Paradox

Telling an LLM it is an expert reduces belief utilization and performance [1]:

| Study | Baseline → Expert Persona |
|-------|--------------------------|
| LLMeem (Opus 4.6) | 100% → 94.2% [1] |
| MMLU benchmark | 71.6% → 66.3% [26] |
| Llama-3.1-8B | 68.4% → 46.3% (−22.1 points) [26] |

Mechanism: "Persona prefixes activate the model's instruction-following mode that would otherwise be devoted to factual recall" [26]. The model focuses on acting like an expert rather than consulting the knowledge base [1].

**Implication**: Agent integration should use generic prompts, not expert personas — EEM's own finding and recommendation [1].

## Context Compaction Destroying Justification Networks

LLMeem measured context compaction destroying justification networks across 33 compaction events [1].

Independent evidence:
- Compaction: 12,847 → 1,526 tokens (88% reduction); LLM recall drops to 0–7% in compacted zones [42]
- After 2–3 compactions, agents "behave as if the session just started" [42]
- "Minor inaccuracies in compaction contaminate the entire remainder of the session" [42]

**Implication**: This is why EEM stores beliefs externally in SQLite rather than in conversation context. The external store survives compaction, model swaps, and session boundaries [1].

## Computational Complexity

TMS computation faces inherent complexity challenges [24]:

| Challenge | Evidence |
|-----------|---------|
| Clause Maintenance System | Σ₂ᵖ-complete — first AI problem proven at this complexity level [24] |
| Monotonic cache growth | Cost of maintaining belief/inference cache grows with knowledge base [24] |
| Scalability | "TMS may not scale well to very large or complex knowledge bases" [counter-discovery] |
| Belief rule base | Rules increase exponentially with attributes and reference levels [31] |

LLMeem's construction cost is O(chunks) + O(beliefs × rounds), amortized to O(queries) at runtime [1]. Knowledge bases range from 237 to 12,731 beliefs [1] — well within practical limits, but scaling behavior beyond this is untested.

## LLM Hallucination in Belief Generation

LLMs hallucinate even when provided with complete, accurate structured knowledge [22]:

| Dataset | Hallucination Rate |
|---------|-------------------|
| MetaQA-1hop (best quadrant) | 5.0% [22] |
| MetaQA-2hop (worst quadrant) | 54.4% [22] |
| WikiTableQuestions | 80–88% [22] |

GPTKB (105M triples from GPT-4o-mini): 19% false, 26% false for person-class [23].

**Implication**: LLM-generated beliefs will contain errors. The derive-then-review pipeline with 13–37% retraction [1] is designed to catch these, but some false beliefs will survive review. External verification (human review, `check-stale`) provides additional safety nets.

## Domain-Specific Hallucination Variance

Hallucination rates vary dramatically by domain [29]:

| Domain | Rate |
|--------|------|
| Legal | 58–88% |
| Medical | 43–64% |
| Code (fake library prompts) | up to 99% |
| Closed-domain QA | 10–20% |
| Grounded summarization | 0.7–1.5% |

EEM's Red Hat domain evaluation (88% A-grade [1]) falls in a moderate-complexity technical domain where grounded retrieval helps, but complex reasoning queries may still produce significant error rates.

## Non-Monotonic Reasoning Limitations in LLMs

LLMs themselves struggle with the kind of reasoning EEM's BMS depends on:

- "Curse of complexity" persists even with larger models and increased inference-time computation [43]
- LLMs fail to maintain stable beliefs when adding supporting or unrelated information [44]
- State-of-the-art models (GPT-4o, Claude-3.5-Sonnet, o1-mini) encounter "significant challenges" with non-monotonic reasoning benchmarks [counter-discovery]

**Implication**: The BMS handles structural non-monotonic reasoning (retraction, restoration, nogoods) symbolically, not via LLM reasoning. The LLM occupies the problem-solver slot for semantic operations while the symbolic system handles consistency — this is the architectural mitigation [1].

## Gaps and Limitations

1. **False retraction rate**: Unknown what fraction of the 13–37% retraction rate represents correct beliefs incorrectly retracted
2. **Scaling cliff**: No data on behavior when KBs grow beyond 12,731 beliefs
3. **Concurrent access**: No documented handling for multiple agents writing to the same reasons.db simultaneously
4. **Error compounding**: Derive operations on incorrect beliefs can produce plausible but wrong derived beliefs that survive review
