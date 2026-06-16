# LLMeem: External Epistemic Memory for LLMs

A citation-backed analysis of LLMeem (llmeem.ai), a framework that gives LLMs justified, persistent, auditable knowledge using Doyle's 1979 Belief Maintenance System architecture.

## Methodology

This analysis was produced using the cited-research methodology: parallel web research across 7 dimensions with 14 independent discovery/counter-discovery agents, multi-engine search augmentation, deep source reading, and independent verification. Every factual claim traces to a URL visited in-session. See [citations.md](citations.md) for all sources.

---

## What LLMeem Is

LLMeem implements External Epistemic Memory (EEM) — a framework for giving LLMs "justified, persistent, auditable knowledge" stored outside model parameters [1]. It adapts Jon Doyle's 1979 Truth Maintenance System [3] for LLM use, placing the LLM in Doyle's "exogenous problem-solver slot" while a symbolic Belief Maintenance System handles structural consistency [1].

Three mandatory properties define EEM [1]:

1. **External** — Knowledge separable from the model: copyable, shareable, inspectable, editable, auditable. Survives model swaps and session boundaries.
2. **Epistemic** — Justified beliefs with truth values (IN/OUT), retraction cascades, contradiction records (nogoods), and derivation depth tracking. Not just facts — justified beliefs.
3. **Memory** — Persistent semantic memory in Tulving's sense [7]: structured general knowledge, not temporally-dated episodes.

The framework ships as two CLI tools: `beliefs` (simple markdown KB with provenance) and `reasons` (full BMS with automatic propagation, cascades, and LLM-driven operations) [1][2].

## Theoretical Foundations

EEM draws on four foundational works [1]:

| Work | Contribution to EEM |
|------|-------------------|
| Doyle 1979 TMS [3] | SL justifications, IN/OUT propagation, retraction cascades, dependency-directed backtracking |
| de Kleer 1986 ATMS [4] | Nogoods and assumption-based reasoning (EEM chose BMS over ATMS for single-context revision) |
| AGM 1985 [5] | Rational belief revision postulates; EEM's entrenchment scoring approximates AGM |
| McCarthy & Hayes 1969 [6] | Frame problem → EEM's `check-stale` for detecting when ground truth shifts |

Tulving's 1972 memory taxonomy [7] classifies EEM as semantic memory — persistent structured knowledge rather than episodic experience replay.

These foundations predate modern LLM capabilities by decades. AGM assumes logical omniscience [8], the frame problem's epistemological version remains unsolved [6], and 2025–2026 research shows LLMs exhibit a "curse of complexity" in non-monotonic reasoning that persists even with larger models [43]. EEM's architectural response: the symbolic BMS handles structural reasoning (retraction, consistency) while the LLM handles semantic operations (derive, review), avoiding reliance on LLM logical reasoning capabilities [1].

## How It Works

### Core Mechanics

A belief is a node in a dependency network with:
- **SL justification**: node is IN when all antecedents are IN; multiple justifications supported [3]
- **Truth values**: IN (believed) or OUT (retracted) [3]
- **Retraction cascades**: when a node goes OUT, all dependents with now-invalid justifications cascade to OUT transitively [1][2]
- **Nogoods**: sets of nodes that cannot simultaneously be IN; dependency-directed backtracking retracts the premise causing minimal disruption [1][2]
- **Challenge/Defend**: dialectical argumentation preserving argument structure [1][2]
- **Restoration**: when a retracted node returns to IN, dependents automatically recompute [1][2]

### Derive-Then-Review Pipeline

The knowledge generation workflow intentionally over-generates, then prunes [1]:

1. `reasons derive` — LLM discovers implicit connections between beliefs
2. `reasons review-beliefs` — LLM audits, retracting 13–37% per round
3. Retraction cascades propagate corrections through the network

This "productive tension between over-generation and over-pruning" yields connections that sources don't make explicit [1].

### Dual-Path Retrieval

Queries use three passes — BMS path (pre-computed justified beliefs), FTS path (traditional RAG chunk search), and a merge pass [1]. Each operates within a "cognitive budget." Mixing beliefs and chunks in a single prompt degraded Opus 4.6 from 95.5% to 86%; three separated passes achieved 100% [1].

### Model Stacking

Layered pipeline: Model A generates candidates → BMS records with provenance → review critiques (machine + human) → Model B receives only validated beliefs → further derivation [1]. Each layer gets fresh context with the critique pipeline as quality gate.

## Measured Performance

All benchmarks originate from llmeem.ai [1]. No independent peer review or external validation has been published.

### Reported Results

| Benchmark | Result | Conditions |
|-----------|--------|------------|
| Overall quality | 98.5% A/B grade | 3,853 questions, Opus 4.6, May 2026 |
| Expert service vs. baseline | 88% vs. 33% A-grade | 50 Red Hat domain questions |
| Speed | 15x faster | EEM expert-service vs. agent pipeline |
| Model compensation | Haiku 94% A+B | vs. Opus 98% baseline |
| Cognitive budget ablation | 100% vs. 86% | 3-pass vs. single-pass, Opus 4.6 |

### Failure Mode Findings (Self-Reported)

| Finding | Data | Corroboration |
|---------|------|---------------|
| Self-critique failure | 87% → 60% accuracy [1] | GPT-4 on GSM8K: 95.5% → 89.0% [25]; Sonnet 4.5: 98.1% → 56.9% on easy tasks [9] |
| Confidence unreliable | Sonnet r=0.135, Opus r=−0.045 [1] | JMIR: r=−0.40 (P=.001) inverse correlation [51]; 86% predictions >0.8 confidence [30] |
| Expert prompt paradox | 100% → 94.2% with expert prompt [1] | MMLU: 71.6% → 66.3% [26]; Llama-3.1-8B: −22.1 points [26] |

The self-reported failure findings are the most credible part of LLMeem's evaluation — they align strongly with independent published research and demonstrate intellectual honesty about the framework's limitations.

### Methodological Concerns

1. **Single evaluator**: All benchmarks conducted by the project creator [1]
2. **LLM-as-judge bias**: 48.4% of LLM judge verdicts reverse under mirrored response order [27]
3. **Small sample**: 50-question expert comparison; 90% accuracy on 50 examples = 75–98% true performance at 95% confidence
4. **Grade scale undefined**: A/B/C/D/F thresholds not specified numerically [1]
5. **Baseline underspecified**: "Agent pipeline baseline" not fully documented [1]
6. **Datasets not public**: Cannot reproduce results independently

## Comparison with Alternatives

### Where EEM Adds Value Over Alternatives

| Capability | EEM | RAG | KG/GraphRAG | MCP | LLM Wiki |
|-----------|-----|-----|-------------|-----|----------|
| Justification chains | Yes | No | Partial | No | No |
| Automatic retraction | Yes | No | No | No | No |
| Contradiction detection | Yes (nogoods) | No | No | No | Partial (lint) |
| Audit trail | Dependency graph | Chunk sources | Graph paths | Tool-dependent | Markdown history |
| Persistence | SQLite, survives model swaps | Stateless | Persistent | External system | Persistent files |

EEM is the only approach that combines formal truth maintenance — justification chains, retraction cascades, nogoods — with LLM-driven semantic operations [1]. No other reviewed system provides automatic dependency-directed backtracking for LLM knowledge.

### Where Simpler Approaches May Suffice

- **RAG** is sufficient for single-hop queries over large corpora where justification chains are not needed. Modern hybrid RAG (BM25 + vector) adds 11–15% accuracy improvement.
- **LLM Wiki** (Karpathy pattern) handles compiled expertise in bounded domains (<50K tokens) with simpler infrastructure and git-native version control.
- **MCP servers** provide real-time connectivity to structured data systems. MCP and EEM are complementary — MCP is the connectivity layer, EEM is the epistemic layer.
- **Fine-tuning** embeds domain knowledge directly in model weights, eliminating external infrastructure at the cost of audit trail and update flexibility.

### The MCP-as-Knowledge-Store Question

MCP is a connectivity protocol ("USB-C port for AI"), not a knowledge representation layer [11][38]. Encoding domain knowledge as MCP tool definitions provides data access but lacks justification chains, truth values, retraction cascades, and contradiction tracking [1][12]. An MCP server could wrap an EEM knowledge base — exposing `reasons search`, `reasons show`, and `reasons explain` as MCP tools — combining both paradigms.

## Limitations

### Architectural

1. **TMS computational complexity**: Clause Maintenance System computation is Σ₂ᵖ-complete [24]. Retraction cascades in large networks may be expensive.
2. **Scale untested**: Knowledge bases range 237–12,731 beliefs [1]. Performance beyond this is undocumented.
3. **Hybrid integration challenges**: Neuro-symbolic systems face scalability, integration complexity, and lack of consensus architecture [52].
4. **No concurrency model**: Concurrent multi-agent access to reasons.db not documented.

### LLM-Dependent

1. **Self-critique degrades correct beliefs**: The derive-then-review pipeline uses LLM critique. If a belief is already correct, review may incorrectly retract it [9][25].
2. **Hallucination in belief generation**: LLMs hallucinate even with complete structured knowledge (5–88% depending on task [22]). LLM-generated KBs contain ~19% false triples [23].
3. **False retraction rate unknown**: The 13–37% retraction rate [1] likely includes both genuine errors and false retractions. The decomposition is not reported.
4. **Error compounding**: Derive operations on incorrect beliefs can produce plausible but wrong derived beliefs that survive review.

### Community

1. **Single-developer project**: 0 stars, 1 fork, no external contributors [2]
2. **No peer review**: No academic publications or independent evaluations
3. **License ambiguity**: ftl-reasons has no explicit license on GitHub [2]
4. **Minimal adoption**: 321 PyPI downloads/month [18], bursty download pattern

## Reflection

Before finalizing, one reflection pass per the cited-research methodology:

- The self-reported benchmarks (98.5% A/B, 88% vs 33%) should be read as suggestive rather than definitive given the single-evaluator, small-sample, undefined-grade-scale methodology.
- The failure mode findings (self-critique, confidence, expert prompt) are more credible because they align with independently published research across multiple labs.
- The theoretical foundations are genuinely deep (Doyle, AGM, Tulving) but the mapping from 1979 TMS to 2026 LLM usage is novel and unvalidated by the research community.
- The comparison with alternatives is fair in identifying what EEM uniquely provides (formal belief maintenance) but lacks head-to-head benchmarks against modern alternatives.
- Cross-source synthesis concern: this analysis draws conclusions across papers that did not reference each other. Claims linking independent findings (e.g., connecting Snorkel's self-critique data to LLMeem's review pipeline) are editorial inference, not source-supported conclusions.

## Key Takeaway

LLMeem/EEM introduces formal belief maintenance to LLM knowledge management — a genuinely novel combination. The core insight is architectural: shifting from "am I sure?" (unreliable confidence) to "is this justified?" (traceable dependency chains) [1]. Whether the complexity of a full BMS is warranted versus simpler alternatives depends on whether the use case demands auditability and formal consistency guarantees.

The project is early-stage (single developer, no peer review, minimal adoption), but the underlying problems it addresses — LLM hallucination, confidence unreliability, context loss, audit trail absence — are well-documented and real.
