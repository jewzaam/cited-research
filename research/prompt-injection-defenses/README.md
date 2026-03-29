# Prompt Injection Defenses for LLM Agents Fetching External Content

## TL;DR

No defense provides deterministic guarantees against prompt injection when LLM agents ingest untrusted external content. The most effective approaches are **architectural** (constraining what a compromised agent can do) rather than **detection-based** (trying to identify injection payloads). Production classifiers are routinely bypassed at 70-88% ASR using character injection and adversarial ML [22], while architectural defenses like CaMeL [4] and type-directed separation [7] achieve 0% ASR — at the cost of agent flexibility.

## Key Defense Comparison

| Defense | ASR | Utility Cost | Approach | Maturity |
|---------|-----|-------------|----------|----------|
| Type-directed separation [7] | 0% | High (−35 pts on bug fixing) | Eliminate freeform text | Research |
| CaMeL [4] | Provable | Moderate (−7 pts) | Capability-based security | Research / OSS |
| OpenClaw [25] | 0%\* | Unknown | Agent isolation + JSON | Research |
| PromptArmor [9] | ~0% | Low (API overhead) | LLM-as-judge preprocessing | Research |
| Multi-layer framework [21] | 8.7% | Low (94.3% retained) | Embedding + prompts + verification | Research |
| Anthropic browser [13] | 1% | Unknown | RL + classifiers + red teaming | Production |
| Spotlighting [2] | 3-8% | None | Datamarking untrusted content | Production |
| Instruction Hierarchy [3] | +63% defense improvement | Low | Trust-level training | Production |
| Production classifiers [14][15] | Bypassed 70-88% [22] | Low | DeBERTa/mDeBERTa | Production |

\* OpenClaw 0% ASR was not tested against adaptive attacks.

## Quick Decision Framework

1. **Start with architecture.** Choose the most restrictive design pattern your use case allows (Action-Selector > Plan-Then-Execute > LLM Map-Reduce > Dual LLM) [1].
2. **Add network controls.** Deny-by-default URL allowlisting at the proxy layer; restrict to GET/HEAD/OPTIONS for non-allowlisted domains [17].
3. **Sanitize fetched content.** Apply Spotlighting (datamarking) and force structured output (JSON) before passing to privileged agents [2] [25].
4. **Layer detection.** Run a classifier (Meta Prompt Guard [15] for injection/jailbreak distinction), deploy canary tokens [19], instrument monitoring [24].
5. **Accept residual risk.** No stack eliminates prompt injection. Design for containment (least privilege, human-in-the-loop for high-impact actions) rather than perfect prevention.

## Files

| File | Contents |
|------|----------|
| [prompt-injection-defenses.md](prompt-injection-defenses.md) | Full analysis with methodology |
| [citations.md](citations.md) | All 34 sources with URLs and extraction notes |
| [references/content-sanitization.md](references/content-sanitization.md) | Spotlighting, DataFilter, pattern matching, JSON formatting |
| [references/architectural-defenses.md](references/architectural-defenses.md) | 6 design patterns, CaMeL, Instruction Hierarchy, privilege separation |
| [references/url-allowlisting.md](references/url-allowlisting.md) | Deny-by-default, OpenAI Codex, MCP security, SSRF prevention |
| [references/detection-monitoring.md](references/detection-monitoring.md) | Classifiers, canary tokens, Cloudflare WAF, Datadog observability |
| [references/oss-tools-frameworks.md](references/oss-tools-frameworks.md) | LLM Guard, NeMo Guardrails, Meta Prompt Guard, CaMeL, Progent |
| [references/limitations-open-problems.md](references/limitations-open-problems.md) | Fundamental barriers, open research problems, consensus position |
| [audit/citation-audit.md](audit/citation-audit.md) | Independent verification of claims against sources |
| [audit/consistency-review.md](audit/consistency-review.md) | Cross-file consistency check |
