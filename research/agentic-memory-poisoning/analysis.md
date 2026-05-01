# Memory Poisoning of Agentic AI — A citation-backed analysis

*Last revised 2026-04-30.*

This document analyzes memory poisoning as a threat to agentic AI systems: what it is, what the published attacks actually demonstrate, what the defenses actually achieve, and what an operator should do about it today. Citations [N] refer to entries in [citations.md](citations.md). Detailed per-dimension analysis lives in [references/](references/).

A reflection pass was performed before finalizing — the headline numbers in this document differ in places from the headline numbers in topics5.md and most secondary coverage, because metric definitions and lab-vs-production conditions matter and most secondary sources elide them.

---

## TL;DR

Memory poisoning is a real, demonstrated attack mechanism. It is also a documented attempt vector in the wild (50 examples observed by Microsoft over 60 days [15]). It is **not**, as of April 2026, a documented cause of any disclosed production breach.

The lab ASR figures circulated in vendor and OWASP coverage (>80% AgentPoison; 32.5% eTAMP under stress; 8x amplification under UI friction) are technically correct under their lab conditions and **systematically misleading** as production threat indicators. The metric definitions, the white-box embedder assumptions, and the empty-memory test corpora all inflate what realistic deployments would experience.

Defenses are uniformly self-reported. The peer-reviewed adaptive-attack evaluation [6] broke 12 published defenses to 90%+ ASR. The single defense paper [4] that tested its own approach honestly reports no usable operating point. SecureIQLab independent validation only begins April 2026 with results expected August 2026 — meaning **no independent industry validation exists** for any commercial defense as of this writing.

The operator playbook is constrained more by economics than by detection technology: full corpus re-embedding at security-best-practice cadence costs $340K/year per enterprise [26] and 9.5 GPU-years per 600B-token corpus [27]. The pragmatic answer combines network-layer IoC monitoring on Microsoft's documented URL pattern [15], memory segmentation per session, identity-bound retrieval, and accepting that detection is best-effort.

---

## 1. The framing challenge

Three assumptions in the topics5.md framing are worth surfacing before evaluating the evidence:

1. **"Memory poisoning is a distinct threat class."** OWASP, Lakera, Schneider, Microsoft Security Blog all use this framing [12, 13, 17, 18, 16]. The counter-view is that memory poisoning is *prompt injection where the carrier happens to be persistent storage* — Snyk's "RAGPoison" name explicitly chooses this framing (per discovery), and the OWASP LLM Top 10 2025's LLM01 (Prompt Injection) already covers indirect injection via RAG. There is internal OWASP overlap between LLM01 and ASI06 that has not been publicly addressed. **The deliverable adopts neither framing as default**; it reports the structural distinctions Schneider [17] articulates as real but tractable, and the rebrand objection as legitimate but minoritarian.

2. **The evidence base is attack-favorable.** The named attacks (AgentPoison, Morris-II, Microsoft AI Recommendation Poisoning) are largely lab demonstrations or attempt observations by researchers and vendors who benefit from the threat being real. ASR figures need contextualization — see §3 and §4. **Vendors selling agentic-AI products publish defense effectiveness claims that none of them have submitted to independent validation as of April 2026.** The Register [22] documents the pattern: when researchers find vulnerabilities in agentic AI products, vendors dispute or downplay them while continuing to sell defenses against the same threat class.

3. **The question topics5.md does not ask but should:** *at what deployment scale does this become economic for real attackers?* AgentPoison [1] requires white-box embedder access. PoisonedRAG [5] requires write access to the knowledge base. ConfusedPilot (per discovery, unfetched) requires SharePoint write access. These are not assumed in any of the headline ASR numbers but they are real attacker-cost factors. An honest threat model would estimate them.

---

## 2. Threat-class taxonomy — see [threat-taxonomy.md](references/threat-taxonomy.md)

OWASP ASI06 (Memory and Context Poisoning) is the canonical framing [12, 13]. Released 2025-12-09 with input from "more than 100 industry experts." Definition (verbatim quote of OWASP via Auth0 [23]): **"Bad data is 'planted' in the agent's memory, causing it to make biased or unsafe decisions later on."** The OWASP-cited example is the Gemini Memory Attack [21].

The "four memory surfaces" framing in topics5.md (in-context short-term, episodic, semantic vector DB, external tool state) is widely cited but lacks a single canonical academic source. The closest peer-reviewed taxonomy [10] uses **three** primary memory types — semantic, episodic, and short-term — with long-term consolidated knowledge as a separate category. External tool state is *not* explicitly framed as a fourth memory type in their abstract.

OWASP's reference implementation, **Agent Memory Guard** [14], is currently Incubator status at version 0.0.0. The Q3 2026 v0.4.0 milestone — ML-based anomaly detection, vector store protection, real-time monitoring dashboard — is **not yet released**. Defense effectiveness claims attributed to it are premature.

A Microsoft-internal contradiction exists: the Microsoft Security Blog announcement [16] frames memory poisoning as a "novel failure mode unique to agentic AI"; the counter-threat-taxonomy discovery agent reported the underlying whitepaper [30] groups it under "Existing Security Failures." The whitepaper PDF could not be extracted in this session, leaving the disagreement unresolved.

---

## 3. The attack landscape — see [agentpoison-attacks.md](references/agentpoison-attacks.md)

### AgentPoison — the headline obscures the metric

AgentPoison [1] is the most-cited memory poisoning attack and the one the topics5.md framing leans on most heavily. Its abstract claim (verbatim): "AgentPoison achieves an average attack success rate higher than 80% with minimal impact on benign performance (less than 1%) with a poison rate less than 0.1%."

Two corrections that the secondary coverage almost universally elides:

**The >80% is retrieval, not end-to-end.** AgentPoison defines three metrics. ASR-r (retrieval — how often poisoned items are retrieved) is what the ">80%" refers to. ASR-t (end-to-end — how often the agent achieves the adversarial environmental impact) averages around **58%** across the three tested agents [1]:

| Agent              | ASR-r | ASR-t | Corpus  | Poisoned |
|--------------------|-------|-------|---------|----------|
| Agent-Driver       | 80.0% | 56.8% | 23,000  | 20       |
| ReAct-StrategyQA   | 65.5% | 58.6% | 10,000  |  4       |
| EHRAgent           | 98.9% | 58.3% |    700  |  2       |

**The "<0.1% poison rate" claim is an average that obscures one outlier.** EHRAgent's 2 poisoned instances in a 700-document corpus is **0.286%** — nearly 3x the abstract claim. The abstract figure averages with two larger corpora.

**The threat model requires white-box embedder access.** Verbatim from [1]: "we allow the attacker to have white-box access to the RAG embedder of the victim agent for trigger optimization." Production deployments use closed API embedders (OpenAI, Cohere, Vertex). The transferability claim has not been validated against production OpenAI embedders at scale.

### Realistic memory dilution collapses the attack

The strongest empirical pushback on AgentPoison's headline numbers is **arXiv 2601.05504** [4] (Devarangadi Sunil et al., University of Massachusetts):

| Condition | GPT-4o-mini ASR | Llama-3.1-8B ASR |
|---|---|---|
| Empty memory | 62% | high (99.95% ISR) |
| Pre-existing legitimate memories | **6.67%** | **0%** |

Authors' best-case figures under realistic retrieval parameters: 38% (GPT-4o-mini), 28% (Llama). Compared to the 62%-empty-memory headline, the 6.67%-with-legitimate-memories result is roughly **an order of magnitude lower** (62/6.67 ≈ 9.3x). A populated memory store *is* the realistic production state.

Zhang et al. [32, per discovery] and PoisonArena [31, per discovery] report the same direction at the corpus level: ASR collapses under expanded knowledge bases or multi-attacker competition.

---

## 4. Persistence — see [persistence-cross-session.md](references/persistence-cross-session.md)

The "Poison Once, Exploit Forever" framing comes from eTAMP [3] (April 2026). The full ASR table:

| Model              | Baseline ASRB | Best ASRB | Best Condition          |
|--------------------|---------------|-----------|-------------------------|
| GPT-5-mini         | 4.6%          | 32.5%     | Frustration + Chaos     |
| GPT-5.2            | 1.8%          | 23.4%     | Frustration + Chaos     |
| GPT-OSS-120B       | 19.5%         | 19.5%     | (no improvement)        |
| Qwen3.5-122B-A10B  | 1.8%          | 12.0%     | Frustration + Chaos     |

The "8x amplification under UI friction" claim in topics5.md is approximately right: GPT-5-mini 4.6% → 32.5% is ~7x. The "Frustration" condition is a Chaos Monkey applying Click Drop (p=0.4), Scroll Swap (p=1), and Caesar-cipher Type Transform (p=1). These are simulated lab perturbations, not measurements from real production friction.

The **persistence** finding — Task A injection survives to Task B activation across sessions — is real (premature trigger ASRA = 0% on most models). The **effectiveness** of that persisted attack varies by model and conditions. Under realistic memory and absent simulated UI friction, baseline ASR ranges from 1.8% to 19.5%.

**Decay over time has no direct experimental measurement** in any paper surfaced. MemoryGraft [7] mentions MemoryBank's Ebbinghaus-inspired curve but does not quantify decay. eTAMP [3] tests cross-task but not multi-day decay. arXiv 2601.05504 [4] does not test multi-session decay. **This is a research gap, not evidence either way.**

The architectural counter-argument (Hindsight [24]): **"Most agents were never designed to remember in the first place. Each session starts over."** Persistence applies only to systems with persistent long-term memory enabled. This is a qualitative claim without quantitative deployment data, but it bounds the affected population — the "memory poisoning will affect every AI deployment" framing in vendor coverage overstates scope.

Willison's lethal trifecta [25] adds another constraint: even where memory exists, exploitation requires private data access + untrusted content + external comms channel **simultaneously**. Removing any one breaks the chain. Most production agents do not have all three simultaneously.

---

## 5. Multi-agent propagation — see [multi-agent-propagation.md](references/multi-agent-propagation.md)

Morris-II [2] (Cohen, Bitton, Nassi; ACM CCS 2025) is the canonical multi-agent worm. The v2 paper:

- Backends: Gemini Flash 1.5 (primary); GPT4oMini, Gemini 1.5 Flash/Pro, Claude 3.5 Sonnet (resilience).
- Payloads: **TEXT only** (correcting widespread secondary coverage that mentions images from v1).
- Propagation: "every five emails a user receives/sends" (with k=20 context). Replication >90% through hop 11, 40-80% by hop 20.
- Defense (DonkeyRail / Virtual Donkey): TPR 1.0, FPR 0.015 in-distribution; AUC 0.96-1.0 OOD.

**The worm has not been seen in the wild.** Per IBM Think (per discovery snippet, source [28] returned 403): "The 'Morris II' AI worm has not been seen in the wild, and the researchers did not test it on a publicly available email assistant." Despite the public code repo, no independent reproduction or in-the-wild incident has been documented.

Per Google Security Blog (April 2026, per discovery, unfetched) and Forcepoint X-Labs (per discovery, unfetched): a 32% increase in malicious indirect prompt injection payloads observed in November 2025 - February 2026. **Critical distinction:** this is IPI-as-exploit (single-agent), not IPI-as-worm (Morris-II self-replicating cascade). Worm propagation in the wild is not documented.

---

## 6. Defenses — see [defenses.md](references/defenses.md)

The single most important defense paper is **"The Attacker Moves Second"** [6] (Nasr, Carlini et al., October 2025). Verbatim: 12 recent defenses, "the majority of defenses originally reported near-zero attack success rates." Under adaptive attacks: "attack success rate above 90% for most." This finding directly applies to memory poisoning defenses, evaluated under the same lab conditions.

The defense-effectiveness self-report pattern, summarized:

| Defense | Reported effectiveness | Independent validation? |
|---|---|---|
| RAGShield [8] | 0.0% ASR (CI 0-1%) on 430 attacks | No — single author |
| RAGDefender [34] | PoisonedRAG ASR 0.84 → 0.03 | No (per discovery) |
| RobustRAG | 0-0.5% in one eval, 54-84% in another | Conflicting evals (per discovery) |
| Lakera Guard | 98% / sub-50ms / <0.5% FP (vendor PR; not in [18]) | No |
| SuperLocalMemory [9] | 72% trust degradation for sleepers | No — single author |
| Production guardrails (Azure, Meta) | broken at up to 100% evasion | YES — broken [36] |

The single defense paper [4] that honestly tested its own approach reports **no usable operating point**: GPT-4o-mini set conservatively rejected all 23 candidate entries (zero utility); Gemini-2.0-Flash accepted 54 confirmed malicious entries with trust score 1.0 (defense bypassed). Authors' own framing: "the defense layer operated essentially as a 'confidence filter' rather than a 'security filter.'"

**SecureIQLab's first independent industry validation begins April 2026** [41] with results targeted for Black Hat USA 2026 (~August 2026). As of this writing, **no independent validation results exist for any commercial defense product** [41]. The defense effectiveness landscape is entirely vendor self-report.

---

## 7. Operator playbook — see [operator-playbook.md](references/operator-playbook.md)

The cost asymmetry between attack and defense is concrete:

- **Attack:** PoisonedRAG [5] achieves 90% ASR with 5 documents in a millions-doc corpus. Marginal cost of attack: cost of generating five documents.
- **Defense:** Richards [26] documents (single-enterprise anecdote, not independently audited) $340K/year for overlapping refresh layers on a moderately-sized RAG system. Crosley [27] (vendor-blog calculation) documents 9.5 years of single-GPU time to re-embed a 600B-token corpus, and estimates a production RAG system processing 10M docs at $1,500-3,000/month in embedding operations alone.

Full corpus re-embedding at the cadence security best-practice recommends (quarterly, or after every confirmed incident) is **financially and temporally infeasible** for many production deployments.

The only IoC pattern with documented in-the-wild observations is Microsoft's [15] URL parameter pattern (`?q=`, `?prompt=` with keywords `remember`, `memory`, `trusted`, `authoritative`, `future`, `citation`, `cite`). This is detectable at network-layer (email gateway, proxy logs).

The pragmatic operator answer combines:
1. Network-layer IoC monitoring for the Microsoft URL pattern [15].
2. Memory segmentation per session/per domain [23].
3. Disable persistent memory features for users who do not need them — per Hindsight [24], most agents do not actually need persistent memory.
4. Identity-bound retrieval (RBAC+ABAC) [23].
5. Accept a longer-than-textbook re-embedding cadence given cost data [26, 27].
6. Treat detection as best-effort given the calibration failure documented in [4].

There is no operator playbook today that combines acceptable utility, acceptable false-negative rate, and economically sustainable cost.

---

## 8. Bias intersection — see [intersection-with-bias.md](references/intersection-with-bias.md)

Korycki and Krawczyk [11] establish the technical answer to topics5.md's bias-vs-poisoning question: **standard drift detectors structurally cannot distinguish adversarial concept drift from natural distribution shift.** Their best detector (RRBM-DD) achieves RLR 0.85/0.78 vs competitors 0.55-0.62 — improvement, not solution.

This makes the suggestion "use bias-mitigation tooling for poisoning detection (or vice versa)" wrong as a design pattern. Fair-ML and adversarial robustness are in active tension, not alignment (per discovery, unfetched). **Provenance is the only signal that distinguishes them at the symptom level.** Documents from controlled sources get treated as drift candidates; documents from open ingest get treated as poisoning candidates.

Microsoft's "AI Recommendation Poisoning" [15] sits exactly on this boundary. The behavior — promotional injection into AI assistant memory — is structurally identical to shilling attacks against recommender systems documented since 2004 [40, per discovery]. The framing choice (AI security vs recommender manipulation) determines the response toolchain (SOC vs trust&safety) but not the underlying mechanism.

---

## 9. Real-world incidence — see [real-world-incidence.md](references/real-world-incidence.md)

**There are no publicly confirmed cases of successful memory poisoning via prompt injection in a production enterprise agent system causing measurable harm.** What exists:

1. **Real-world deployment of attempts** (Microsoft 50 examples, 31 companies, 60 days [15]) — but Microsoft observed ATTEMPTS, not confirmed memory writes against real users. Attack class is promotional spam.
2. **Authorized researcher PoCs against live consumer products** (SpAIware [20], Gemini Memory [21], Unit 42 Bedrock [19]).
3. **Lab demonstrations against benchmark agents** (AgentPoison [1], MemoryGraft [7], MINJA [38], eTAMP [3]).
4. **Confirmed production memory-poisoning incident with disclosed harm:** **0** publicly disclosed.

The McKinsey Lilli RAG breach (March 2026, per discovery) is a real production breach but the primary attack vector was SQL injection on unauthenticated API endpoints — different attack class. Conflating it with memory poisoning is a category error.

Several "incident" claims circulating in secondary sources are **fabricated**: a "$45M crypto Step Finance breach" attributed to a memory-poisoned trading agent, "CVE-2025-64439 LangGraph RCE memory poisoning" (no NVD entry), "88% of organizations faced an incident" (no traceable primary source), "380 memory poisoning incidents" (no traceable primary source). These should not be cited.

The honest threat statement is: **"demonstrated mechanism, attempts observed in the wild, no confirmed successful production exploitation with disclosed harm to date."**

---

## 10. Conclusion

Memory poisoning is real but the gap between "demonstrated in research" and "observed exploited in production" is the entire dimension that most coverage elides. The pragmatic posture for an operator in mid-2026:

- **Take the threat seriously enough** to deploy network-layer IoC monitoring for the Microsoft URL pattern [15], to enable memory segmentation, and to scope which users actually need persistent memory.
- **Discount the lab ASR figures.** They describe a different threat model than the one your production deployment faces.
- **Discount the vendor defense effectiveness claims** until SecureIQLab's August 2026 results land. Plan as if no commercial defense provides reliable protection against an adaptive attacker.
- **Accept that detection is best-effort.** No published defense produces both acceptable utility and acceptable false-negative rate.
- **Limit blast radius via privilege scope** (Willison's lethal trifecta [25]). Most production agents do not need all three of: private data access, untrusted content exposure, external comms channel.
- **Treat OWASP ASI06 [12, 13] and the Agent Memory Guard roadmap [14] as prospective risk-management tools**, not as evidence of widespread current harm.

The methodology behind this document — including which discovery agent claims were corrected against primary sources, which sources were inaccessible, and what is yet unverified — is logged in [audit/](audit/).
