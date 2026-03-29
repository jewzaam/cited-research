# Limitations and Open Problems

Dimension covering what the research says about the fundamental difficulty of prompt injection defense and where current approaches fall short. Sources referenced via `[N]` — see [citations.md](../citations.md) for full entries.

## The Fundamental Problem

Prompt injection is architecturally distinct from traditional injection attacks (SQL injection, XSS) in one critical way: **there is no instruction-data boundary to enforce.** Transformer self-attention processes all tokens uniformly — system instructions, user queries, and untrusted fetched content all occupy the same token stream with no hardware-enforced separation [23] [5].

NVIDIA's AI Red Team states plainly: prompt injection attacks are "common, cannot be effectively mitigated" at the LLM level, requiring defensive architecture at the application layer instead [23].

## Why Complete Prevention Is Likely Impossible

### The Instruction-Data Conflation Problem

Unlike SQL where parameterized queries create a deterministic boundary between code and data, LLMs have no equivalent mechanism. The OWASP cheat sheet [5] notes that attacks are "expressed in natural language with no finite set of dangerous characters." Any string that is valid data could also be a valid instruction.

### The Capability Paradox

More capable models may be more vulnerable because:
- Better reasoning → better understanding of injected instructions
- Longer context windows → more space for hidden injection payloads
- Tool use capability → greater impact from successful injections

This creates a paradox where the properties that make models useful (instruction following, reasoning, tool use) are the same properties that make them exploitable.

### Adaptive Attack Advantage

The critical evaluation by Jia et al. [10] demonstrates that "existing defenses are not as successful as previously reported" when evaluated with a principled approach that includes adaptive attacks (where attackers modify their approach after learning about defense mechanisms).

The guardrail bypass research [22] quantifies this gap across production systems:

| Guardrail | Bypass ASR (Prompt Injection) | Bypass ASR (Jailbreak) |
|-----------|------------------------------|----------------------|
| Vijil | 87.95% | 91.67% |
| ProtectAI v1 | 77.32% | 51.39% |
| Azure Prompt Shield | 71.98% | 60.15% |
| Meta Prompt Guard | 70.44% | 73.08% |
| NeMo Guard | — | 72.54% |
| ProtectAI v2 | 20.26% | — |

Emoji smuggling alone achieved 100% evasion across all tested systems [22].

### Power-Law Scaling of Attacks

OWASP notes a fundamental asymmetry: "power-law scaling behavior means attackers with sufficient computational resources can eventually bypass most current safety measures" [5]. Rate limiting, content filters, and safety training only increase attacker cost — they don't create an absolute barrier.

## What Defenses Actually Achieve

### The Best Published Numbers

| Defense | ASR After | Utility Retained | Benchmark | Caveat |
|---------|-----------|-----------------|-----------|--------|
| Type-directed separation [7] | 0% | Variable (−35 pts on complex tasks) | 3 case studies | Eliminates freeform text entirely |
| OpenClaw full pipeline [25] | 0% | Not reported | 649 attacks | Normalized subset, no adaptive attacks |
| CaMeL [4] | Provable (by design) | 77% task completion | AgentDojo | Research prototype, user policy burden |
| Progent (manual policies) [8] | 0% (EHRAgent) | — | EHRAgent | Manual policy creation required |
| PromptArmor [9] | ~0% | High | AgentDojo | LLM-based, adds API call overhead |
| Anthropic (Opus 4.5) [13] | 1% | — | Adaptive Best-of-N | Browser agent specific |
| Multi-layer framework [21] | 8.7% | 94.3% | 847 adversarial cases | English only, static attacks |
| Progent (auto) [8] | 2.2% | — | AgentDojo | Cannot defend within-privilege attacks |
| Instruction Hierarchy [3] | ~37% unseen | — | Multiple | Treats all tool output as misaligned |
| Spotlighting (datamarking) [2] | <3% | Minimal impact | GPT-3.5 tasks | Bypass possible with system prompt knowledge |

### Pattern: Security vs. Utility Trade-Off

The 0% ASR defenses (type-directed separation, OpenClaw, CaMeL) achieve their guarantees by restricting what the agent can do — eliminating freeform text, forcing structured outputs, requiring policy specification. This creates a fundamental trade-off: the most secure systems are the least flexible.

Jacob et al. [7] illustrate this clearly: their defense achieves 0% ASR on all three case studies, but bug-fixing utility drops from 49.7% to 14.6% (−35 points) because the task inherently requires natural language context.

## Open Research Problems

### 1. Text-to-Text Attacks

When the agent's purpose is to produce text from text (summarization, translation, content analysis), there is no structural boundary between instructions and data. CaMeL and type-directed separation cannot help here because the output must be freeform text [4] [12]. This is the hardest open problem.

### 2. Adaptive Attack Evaluation

Most defenses are evaluated against fixed attack datasets. Jia et al. [10] argue this systematically overestimates effectiveness. A standardized adaptive attack evaluation framework does not yet exist.

### 3. Benchmark Fragmentation

No universally adopted benchmark exists. AgentDojo, Open Prompt Injection, TensorTrust, CyberSecEval, and ASB are used inconsistently across papers, making cross-defense comparison unreliable.

### 4. Multilingual Robustness

Detection performance degrades on non-English content. Meta Prompt Guard TPR drops ~6 percentage points on multilingual jailbreaks (97.5% → 91.5%) compared to English out-of-distribution inputs [15]. Pattern-matching approaches designed for English fail entirely against other languages. Multilingual injection payloads are an active attack vector.

### 5. Composition Effects

How do multiple defenses interact when layered? The design patterns paper [1] recommends combining patterns but does not evaluate combinations. The multi-layer framework [21] shows promising results (73.2%→8.7%) but uses a specific combination — generalizable composition principles are missing.

### 6. User Policy Burden

CaMeL [4] and Progent [8] require security policy specification. Willison notes this is "difficult even for security professionals" [12], creating a deployment barrier. Default configurations that provide reasonable security without user expertise are needed.

### 7. Production Deployment Data

Most effectiveness numbers come from benchmarks, not production deployments. Anthropic's browser agent data [13] and Microsoft's Adaptive Prompt Injection Challenge [6] are the closest to real-world evaluation. Production false positive/negative rates, latency impacts, and operational costs remain largely unpublished.

### 8. Cost and Latency

LLM-as-judge defenses (PromptArmor [9]) add API call overhead per request. Classifier models add inference latency. Multi-layer frameworks add ~2.1% latency [21]. Systematic cost analysis across defense approaches for agentic workflows is absent.

## The Consensus Position

No single vendor or research group claims to have solved prompt injection:

- **NVIDIA:** "cannot be effectively mitigated" at the LLM level [23]
- **Anthropic:** "No browser agent is immune to prompt injection" [13]
- **Microsoft:** Indirect prompt injection is "an inherent risk" from LLMs' probabilistic nature [6]
- **OWASP:** Power-law scaling means "attackers with sufficient computational resources can eventually bypass most current safety measures" [5]
- **Design Patterns Paper:** "General-purpose agents can provide meaningful and reliable safety guarantees" remains unlikely [1]

The practical implication: **defense is about raising the cost and reducing the blast radius of successful attacks, not preventing them entirely.** Architectural controls (what a compromised agent can do) matter more than detection (whether you can identify the attack).

## Gaps and Limitations

- **The "Attacker Moves Second" paper** (referenced in [30] and multiple search results as systematically breaking 12 defenses at >90% ASR) was not fully located for citation. This is a significant source gap — it reportedly provides the strongest evidence against defense durability.
- **StruQ (Structured Queries)** — a fine-tuning approach for separating instructions from data — was referenced but not fully investigated.
- **Taint tracking** is proposed theoretically [30] but no production implementation has been identified.
- **Formal impossibility proofs** — while the practical impossibility is widely argued, rigorous formal proofs (analogous to computational complexity results) are absent from the literature.
