# Persistence and cross-session contamination

The "Poison Once, Exploit Forever" framing claims that what makes memory poisoning materially different from prompt injection is that the payload **persists** — surviving session resets, cache evictions, and re-embedding. This file evaluates that claim.

See [citations.md](../citations.md) for source details.

## The "Poison Once, Exploit Forever" paper

The phrase originates in **eTAMP** [3] (arXiv 2604.02623, April 2026). The paper proves cross-session persistence with a two-phase design: Task A (poisoning encounter, e.g., browsing a manipulated product page) followed by Task B (activation on a different website, days later). Approximately 280 task pairs were constructed across three cross-site directions.

### Full ASR table from eTAMP [3]

| Model              | Baseline ASRB | Best ASRB | Best Condition          |
|--------------------|---------------|-----------|-------------------------|
| GPT-5-mini         | 4.6%          | 32.5%     | Frustration + Chaos     |
| GPT-5.2            | 1.8%          | 23.4%     | Frustration + Chaos     |
| GPT-OSS-120B       | 19.5%         | 19.5%     | Baseline                |
| Qwen3.5-122B-A10B  | 1.8%          | 12.0%     | Frustration + Chaos     |

The "Frustration Exploitation" finding: environmental stress (the Chaos Monkey applies Click Drop p=0.4, Scroll Swap p=1, Type Transform via Caesar cipher p=1) increased GPT-5-mini ASR by ~7x (4.6% → 32.5%). The "8x" figure cited in topics5.md and most secondary coverage is a rounded approximation; the actual amplification is closer to 7x.

**Stealth validation:** Premature trigger rates (ASRA, attack triggering during Task A before Task B activation) were 0% on most models. The two exceptions were Qwen3.5-122B (0.35%) and Qwen3-VL-32B (0.71%) [3].

The eTAMP results are from controlled (Visual)WebArena lab benchmarks, not production observation.

## What "persistence" actually means under realistic conditions

The arXiv 2601.05504 paper [4] is the strongest published evidence that persistence claims overstate the case under realistic memory conditions:

| Condition | GPT-4o-mini ASR | Llama-3.1-8B ASR |
|---|---|---|
| Empty memory | 62% | high |
| Pre-existing legitimate memories | 6.67% | 0% |

Authors' best-case figures under realistic retrieval parameters: 38% (GPT-4o-mini) and 28% (Llama). These are an order of magnitude lower than the empty-memory headline numbers.

**Interpretation:** "Persistence" is established (the payload remains in store across sessions), but **effectiveness** degrades sharply when the store contains competing legitimate memories — which is the realistic production state.

## Decay over time: an open research gap

No paper in this corpus directly measures temporal decay of a poisoned memory store across N sequential sessions as a function of time elapsed or benign memory accumulation:

- **MemoryGraft** [7] mentions MemoryBank's "Ebbinghaus-inspired forgetting curve" but does not quantify decay metrics for itself. Its evaluation runs 12 queries in a single session.
- **eTAMP** [3] tests cross-task persistence but not multi-day decay.
- **arXiv 2601.05504** [4] does not run multi-session decay experiments.

The closest evidence on re-embedding survival comes from AgentPoison [1]: "high attack transferability across different embedding models" — meaning a poisoned trigger optimized against one embedder still gets retrieved when re-embedded with a different encoder. This tests cross-encoder transfer, not literal store regeneration from source documents.

**Garbage collection / cache eviction:** No paper tests what happens when the vector store is GC'd (e.g., entries older than 30 days deleted) or fully regenerated from source. This is a research gap.

## Practitioner framing

Christian Schneider [17] articulates three distinctions from prompt injection:
1. **Detection evasion through time separation:** "The injection happens in February. The damage happens in April."
2. **Agent self-defense of corrupted context:** Agents rationalize poisoned memories as learned knowledge.
3. **Cross-session persistence:** Memory poisoning survives across multiple users and workflows.

Lakera [18] frames the same distinction more compactly: "memory poisoning rewrites the past, goal hijacks rewrite the future."

Unit 42 [19] provides the strongest mechanism-level demonstration: on Amazon Bedrock Agents (Nova Premier v1, Guardrails disabled), they exploit session summarization to inject malicious instructions that are then "automatically inject[ed] into every new session's context." Cross-session persistence demonstrated in subsequent booking interactions days later. Explicitly framed as PoC, not production incident.

## Architectural counter-argument

The Hindsight blog [24] notes that **persistence applies only to systems with persistent long-term memory enabled** — and asserts (qualitatively) that this is a minority deployment pattern: "Most agents were never designed to remember in the first place. Each session starts over."

Willison's "lethal trifecta" [25] adds another constraint: even where memory exists, exploitation requires (1) private data access, (2) untrusted content exposure, and (3) external comms channel **simultaneously**. Removing any one breaks the chain.

These are conditional counter-arguments, not refutations: where persistent memory IS deployed, the eTAMP and MINJA results stand. But the "memory poisoning will affect every AI deployment" framing in the OWASP/vendor coverage overstates the affected population.

## Gaps and limitations

- Decay-over-time has no direct experimental measurement in any paper surfaced.
- The "garbage collection survives the attack" question is open.
- No paper tests at production-scale memory (millions of records); 2601.05504 [4] flags this but does not test it.
- Microsoft [15] notes some previously demonstrated persistence attacks "could no longer be reproduced" after their mitigations — quantitative attribution of how much of the persistence surface has closed is absent.
- The Hindsight quantitative claim (most agents are stateless) is qualitative only.
