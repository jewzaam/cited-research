# LLMeem: External Epistemic Memory for LLMs

LLMeem ([llmeem.ai](https://llmeem.ai/)) is a framework that gives LLMs justified, persistent, auditable knowledge using Doyle's 1979 Belief Maintenance System architecture. It stores beliefs as nodes in a dependency network with truth values (IN/OUT), automatic retraction cascades, contradiction detection (nogoods), and dependency-directed backtracking — all outside the model's parameters.

Last revised: 2026-06-16

## Key Results

| What | Finding |
|------|---------|
| **Core idea** | Shift from "am I sure?" (unreliable confidence) to "is this justified?" (traceable dependency chains) |
| **Architecture** | Symbolic BMS handles consistency; LLM handles semantics. Dual-path retrieval (beliefs + RAG + merge) |
| **Self-reported benchmarks** | 98.5% A/B grade (3,853 questions), 88% vs 33% A-grade vs baseline (50 questions). Single evaluator, no peer review |
| **Self-critique failure** | Accuracy drops 87% → 60% with LLM self-revision. Corroborated by independent research [ICLR 2024, Snorkel AI] |
| **Confidence unreliable** | Sonnet r=0.135, Opus r=−0.045. Corroborated by JMIR (r=−0.40, P=.001) |
| **Expert prompt paradox** | Expert persona reduces accuracy 5–22 points. Corroborated by independent MMLU studies |
| **Project maturity** | Single developer, 0 GitHub stars, 321 PyPI downloads/month, no academic publications |

## What Makes It Unique

EEM is the only reviewed approach that combines formal truth maintenance (justification chains, retraction cascades, nogoods, dependency-directed backtracking) with LLM-driven semantic operations. No other system — RAG, knowledge graphs, MCP servers, LLM Wiki, or agent memory — provides automatic dependency-directed backtracking for LLM knowledge.

## Quick Decision Framework

1. **Do you need auditability** — "how do you know that?" with traceable justification chains? → EEM adds genuine value over alternatives
2. **Do you need automatic retraction** — when one belief is invalidated, should dependents cascade? → EEM is the only option reviewed that does this
3. **Is your knowledge base bounded** (<12K beliefs) and the domain stable? → EEM is architecturally suited
4. **Can you tolerate single-developer risk** — no community, no peer review, ambiguous license? → Significant adoption risk
5. **Is simpler sufficient** — RAG for large corpora, LLM Wiki for bounded compiled expertise, MCP for real-time data access? → Consider whether formal belief maintenance is worth the complexity

## Supporting Files

- [analysis.md](analysis.md) — Full analysis with methodology across 7 dimensions
- [citations.md](citations.md) — All 54 sources, numbered with quality tiers
- [references/theoretical-foundations.md](references/theoretical-foundations.md) — Doyle TMS, AGM, frame problem, Tulving
- [references/architecture-and-mechanics.md](references/architecture-and-mechanics.md) — SL justifications, cascades, dual-path, model stacking
- [references/measured-performance.md](references/measured-performance.md) — Benchmarks, failure modes, methodological concerns
- [references/comparison-with-alternatives.md](references/comparison-with-alternatives.md) — vs. RAG, KG, MCP, LLM Wiki, agent memory
- [references/practical-usage-and-integration.md](references/practical-usage-and-integration.md) — CLI tools, workflow, agent integration
- [references/limitations-and-failure-modes.md](references/limitations-and-failure-modes.md) — Self-critique, confidence, complexity, hallucination
- [references/open-source-and-community.md](references/open-source-and-community.md) — Repos, author, adoption, license
- [audit/citation-audit.md](audit/citation-audit.md) — Independent verification of cited sources
- [audit/consistency-review.md](audit/consistency-review.md) — Numerical and logical consistency check
