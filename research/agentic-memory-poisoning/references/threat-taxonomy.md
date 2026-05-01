# Threat-class taxonomy — memory surfaces and the OWASP framing

This file covers the four memory surfaces enumerated in topics5.md, the OWASP ASI06 framing, the Microsoft AI Red Team taxonomy, and the contested question of whether memory poisoning is a distinct threat class or a flavour of indirect prompt injection.

See [citations.md](../citations.md) for source details.

## OWASP ASI06: Memory and Context Poisoning

The OWASP Top 10 for Agentic Applications was released **2025-12-09** with input from "more than 100 industry experts" [12]. The identifier prefix is **ASI** (Agentic Security Initiative); ASI06 is the sixth entry. The complete list per Auth0 [23]:

| ID    | Risk                                |
|-------|-------------------------------------|
| ASI01 | Agent Goal Hijack                   |
| ASI02 | Tool Misuse and Exploitation        |
| ASI03 | Identity and Privilege Abuse        |
| ASI04 | Agentic Supply Chain Vulnerabilities|
| ASI05 | Unexpected Code Execution           |
| **ASI06** | **Memory and Context Poisoning**|
| ASI07 | Insecure Inter-Agent Communication  |
| ASI08 | Cascading Failures                  |
| ASI09 | Human-Agent Trust Exploitation      |
| ASI10 | Rogue Agents                        |

ASI06 definition (verbatim quote of OWASP via Auth0 [23]): **"Bad data is 'planted' in the agent's memory, causing it to make biased or unsafe decisions later on."**

The OWASP announcement [13] cites the **Gemini Memory Attack** (Rehberger Feb 2025 [21]) as the canonical example: "Memory poisoning reshaped behaviour long after the initial interaction (ASI06 - Memory & Context Poisoning, e.g Gemini Memory Attack)."

OWASP's reference implementation is the **Agent Memory Guard** project [14], currently Incubator status at version 0.0.0 (April 2026). The Q3 2026 v0.4.0 milestone — ML-based anomaly detection, vector store protection, real-time monitoring dashboard — is **not yet released**. Any defense effectiveness claim attributed to Agent Memory Guard's ML detection is premature.

## Memory surfaces

The "four memory surfaces" framing (in-context short-term, episodic experience stores, semantic vector databases, external tool state) appears in topics5.md and BeyondScale's defense guide. The closest peer-reviewed taxonomy is Torra & Bras-Amorós [10], which presents **three** primary memory types: "semantic, episodic, and short-term memory," plus a separate notion of "long-term consolidated memory localized in well established knowledge databases." External tool state is **not** explicitly framed as a fourth memory type in their abstract.

| Surface | Concrete attack example |
|---|---|
| In-context short-term memory | Indirect prompt injection in a tool response that the model treats as trusted (Unit 42 [19]) |
| Episodic experience stores | MemoryGraft's poisoned README files retrieved by MetaGPT DataInterpreter via "semantic imitation heuristic" [7] |
| Semantic vector DB / RAG | AgentPoison [1], PoisonedRAG [5] |
| External tool state | Microsoft AI Recommendation Poisoning [15] (the only "external state" entry with empirical data) |

The four-surface taxonomy is widely repeated but **does not have a single canonical academic source**. Different papers use overlapping but inconsistent categorizations.

## Is memory poisoning a distinct threat class?

This is the question the topics5.md framing presupposes — and the answer is contested.

**Mainstream position (memory poisoning is distinct):**
- OWASP ASI06 [12, 13] treats it as its own Top-10 category.
- Schneider [17] argues three structural distinctions from prompt injection: temporal decoupling, agent self-defense of corrupted context, cross-session persistence.
- Microsoft Security Blog [16] frames it as a "novel failure mode unique to agentic AI."
- Torra & Bras-Amorós [10] treat it as a separate research domain from prompt injection.

**Counter-view (memory poisoning is prompt injection with a persistent carrier):**
- The Snyk Labs "RAGPoison" technique is explicitly titled "Persistent Prompt Injection via Poisoned Vector Databases" — same threat class, different carrier (per counter-threat-taxonomy discovery agent, source unfetched).
- Turing Institute / CETaS and NCSC treat indirect prompt injection as the single root vulnerability subsuming RAG, memory, email, and document ingestion (per discovery agent, unfetched).
- Mandiant VP Jurgen Kutscher (Google Cloud Next 2026) argued enterprises focus on "new AI threats like LLM poisoning" while ignoring basic controls (per discovery agent, unfetched).
- The OWASP LLM Top 10 2025's LLM01 (Prompt Injection) already covers indirect injection via RAG. Creating ASI06 as a separate agentic entry potentially overlaps.

**Contradiction flag (Microsoft):** The counter-threat-taxonomy discovery agent reported that Microsoft's own taxonomy whitepaper [30] groups memory poisoning under "Existing Security Failures." The companion announcement blog [16], by contrast, frames it as a "novel failure mode." The PDF body [30] could not be extracted in this session, leaving the disagreement unresolved. **This contradiction is unresolved pending PDF access.**

## Gaps and limitations

- The four-surface taxonomy is widely cited but lacks a single canonical academic source. Torra & Bras-Amorós [10] use three, not four.
- The OWASP ASI06 full text (definition, attack vectors, mitigations enumerated in the framework PDF) was not extracted in this session. Auth0's quote [23] of the definition is the best available proxy.
- The Mandiant practitioner critique was reported by a discovery agent but the underlying source was not directly fetched.
- The Microsoft whitepaper PDF [30] is the source of a contradicted claim and could not be verified.
