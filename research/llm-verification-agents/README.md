# Alternative LLM Models for Verification Agents in Claude Code

**Question**: Can non-Anthropic models serve as verification agents in Claude Code subagent workflows, checking binary claims against a codebase with failure mode diversity from the primary Claude session?

**Answer**: The models exist, but Claude Code's integration doesn't support them natively. The subagent system is locked to Anthropic model aliases, and the feature request to extend it was closed as "not planned." Using non-Anthropic verification requires building an external harness.

Last revised: 2026-05-07

## Key Decision Table

| If your priority is... | Use | How | Cost/Run |
|---|---|---|---|
| Zero friction | Claude Haiku 4.5 | Native subagent | $0.135 |
| Maximum diversity | Gemini 2.5 Flash | External harness | $0.056 |
| Lowest cost | DeepSeek V4 Flash | External harness | $0.013 |
| Best benchmarks | GLM-4.7 | External harness | $0.032 |
| Fastest execution | Gemini 2.5 Flash-Lite | External harness | $0.012 |

## Three Things to Know

1. **Claude Code subagents only route to Anthropic models.** The Agent tool accepts `sonnet`, `opus`, `haiku`, or full Anthropic model IDs. No extension mechanism exists. GitHub #34821 was closed as "not planned."

2. **Cross-model verification helps, but less than expected.** Model pairs agree on wrong answers 60% of the time (vs 33% random). More capable models have MORE correlated errors. The cheapest alternatives (DeepSeek, Qwen) have documented Claude contamination in their training data, reducing diversity.

3. **The cost difference is real but small.** At 50 runs/month, switching from Sonnet ($0.405/run) to DeepSeek ($0.013/run) saves ~$230/year. Integration engineering to build an external harness costs more than this in most scenarios.

## Quick Decision Framework

```
Is the verification task mechanical (format, existence, schema)?
  -> Claude Haiku 4.5. Intra-family correlation is low-risk for structural checks.

Is failure mode diversity critical?
  -> Gemini 2.5 Flash via external harness. Most independent from Claude.

Is cost the binding constraint?
  -> DeepSeek V4 Flash via external harness. Accept 5-12% parse failures
     and Claude contamination in exchange for 31x cost reduction.

None of the above?
  -> Deterministic verification (tests, linters, type checkers) provides
     truly independent error detection with zero LLM integration friction.
```

## Files in This Topic

- [analysis.md](analysis.md) — Full analysis with methodology, decision framework, and reflection
- [citations.md](citations.md) — All 55 sources with URLs and data extracted
- [references/model-candidates.md](references/model-candidates.md) — Per-model assessment (7 candidates)
- [references/provider-options.md](references/provider-options.md) — Provider comparison (7 providers)
- [references/claude-code-integration.md](references/claude-code-integration.md) — Integration mechanics and limitations
- [references/failure-mode-diversity.md](references/failure-mode-diversity.md) — Error correlation and training independence
- [references/cost-comparison.md](references/cost-comparison.md) — Cost per run, latency, free tier analysis
- [references/reliability.md](references/reliability.md) — Structured output, tool use, rate limiting
- [audit/citation-audit.md](audit/citation-audit.md) — Independent verification of cited claims
- [audit/consistency-review.md](audit/consistency-review.md) — Cross-file numerical consistency check
