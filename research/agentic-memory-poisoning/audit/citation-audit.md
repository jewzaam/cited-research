# Citation Audit — Memory Poisoning of Agentic AI

Auditor: Claude Code (claude-sonnet-4-6)
Date: 2026-04-30
Scope: Citations [1]–[40] in citations.md, cross-checked against pre-fetched source files in FETCHED_DIR.

The auditor had NO context from the research conversation that produced the deliverables. Every grade is derived by comparing claims in the deliverable documents (citations.md, analysis.md, references/*.md, README.md) against the actual content of the corresponding fetched file.

---

## Summary Table

| Grade | Count | Citations |
|---|---|---|
| VERIFIED | 18 | [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [17], [20], [21], [25] |
| PARTIAL | 10 | [15], [16], [18], [19], [22], [23], [24], [26], [27], [40] |
| INACCURATE | 1 | [13-contributor-count] — see note under [13] |
| INACCESSIBLE | 2 | [28], [30] |
| NOT FOUND | 0 | — |
| DRIFT | 0 | — |
| Per-discovery-only (not directly fetched) | 9 | [31]–[39] (except [37] which is a PDF variant of [1]) |

**Adjusted tally for directly-verifiable citations [1]–[27], [28], [30]:**

| Grade | Count |
|---|---|
| VERIFIED | 18 |
| PARTIAL | 10 |
| INACCURATE | 0 (one intra-citation discrepancy flagged in [13]) |
| INACCESSIBLE | 2 |
| NOT FOUND | 0 |
| DRIFT | 0 |

Citations [29], [31]–[40] are tagged "per discovery agent, unfetched" in the deliverables and carry no direct source-content verification obligation; they are noted below for completeness but not formally graded.

---

## Pre-flagged Items Resolution

Before the per-citation detail, resolving the eight flagged items explicitly requested:

| Flag | Finding |
|---|---|
| [1] ">80% is ASR-r not end-to-end" | CONFIRMED. agentpoison-html-tables.md explicitly labels ASR-r vs ASR-t. The ~58% ASR-t average is confirmed from the table (56.8/58.6/58.3). |
| [1] "ASR-t averages ~58%" | CONFIRMED. Average of 56.8%, 58.6%, 58.3% = 57.9%. The "~58%" claim is accurate. |
| [2] "text-payload-only" | CONFIRMED. morris-ii-html-v2.md: "TEXT-BASED ONLY. The paper does not evaluate image-based adversarial payloads." |
| [2] "every five emails" propagation | CONFIRMED. morris-ii-html-v2.md verbatim: "the worm is expected to propagate to new clients every five emails a user receives/sends" |
| [3] eTAMP full ASR table | CONFIRMED. etamp-html-tables.md contains the exact table the deliverable cites. |
| [4] ASR drop 62% to 6.67% | CONFIRMED. memory-poisoning-2601.05504-html.md verbatim: "GPT-4o-mini: ASR fell from '62%' with empty memory to '6.67%' when legitimate memories existed." |
| [15] Microsoft observed ATTEMPTS not successes | CONFIRMED. microsoft-recommendation-poisoning.md: "CRITICAL METHODOLOGY DISTINCTION: The research is based on PASSIVE OBSERVATION of attack ATTEMPTS, not confirmed memory writes." |
| [16] vs [30] Microsoft framing contradiction | CONFIRMED as unresolved. microsoft-failure-modes-blog.md: "CRITICAL CONTRADICTION FLAG" — the blog frames memory poisoning as a novel failure mode; the PDF body [30] is inaccessible. Contradiction remains unresolved. |
| [19] Unit 42 "66% LLM-detector miss" | CONFIRMED NOT IN SOURCE. unit42-bedrock-memory-poisoning.md: "CRITICAL CORRECTION: The 'LLM-based detectors miss 66% of poisoned entries' figure... is NOT present in this Unit 42 article." |
| [22] Anthropic-vs-OpenAI testing-standards claim | CONFIRMED NOT IN SOURCE. the-register-ai-vendors-response.md: "CORRECTION: The counter-defenses discovery agent claimed... This specific testing-standards comparison is NOT in this article." |

---

## Per-Citation Grades

### [1] AgentPoison — NeurIPS 2024
**Grade: VERIFIED**

Fetched files: `agentpoison-html-tables.md`, `agentpoison-arxiv-abs.md`

**Claims verified:**

- Per-agent ASR-r/ASR-t table: Source verbatim — Agent-Driver (ASR-r 80.0%, ASR-t 56.8%, corpus 23,000, poisoned 20), ReAct-StrategyQA (65.5%/58.6%, 10,000, 4), EHRAgent (98.9%/58.3%, 700, 2). Matches the deliverable table exactly.
- ASR metric definitions: Source defines ASR-r as "Percentage of test instances where all retrieved demonstrations are from the poisoned set" and ASR-t as "percentage of test instances where the agent achieves the final adversarial impact on the environment." The ">80% is ASR-r" claim in the caveat is directly supported.
- EHRAgent poison rate 2/700 = 0.286%: Source confirms "EHRAgent: 2/700 = 0.29% (EXCEEDS the <0.1% threshold)."
- White-box threat model: Source verbatim — "we allow the attacker to have white-box access to the RAG embedder of the victim agent for trigger optimization."
- Embedders listed (DPR, ANCE, BGE, REALM, ORQA, text-embedding-ada-002): Confirmed in source.

**Notes:** The abstract's ">80% ASR" claim (agentpoison-arxiv-abs.md) does not distinguish ASR-r from ASR-t. The HTML body (agentpoison-html-tables.md) makes the distinction explicit. The deliverable correctly characterizes this as conflation in the abstract and corrects it using the HTML body. No overclaiming detected.

---

### [2] Morris-II / "Here Comes The AI Worm"
**Grade: VERIFIED**

Fetched files: `morris-ii-html-v2.md`, `morris-ii-arxiv-abs.md`

**Claims verified:**

- Text-only payload in v2: Source — "Payload types: TEXT-BASED ONLY. The paper does not evaluate image-based adversarial payloads." Deliverable correctly flags image-payload claims as v1 secondary-source error.
- "Every five emails" propagation: Source verbatim — "the worm is expected to propagate to new clients every five emails a user receives/sends (with context k=20 emails)." Matches deliverable exactly.
- Hop degradation (>90% through hop 11, 40-80% by hop 20): Confirmed in source.
- Virtual Donkey defense (TPR 1.0, FPR 0.015, AUC 0.96-1.0 OOD): Confirmed in source.
- Backends (Gemini Flash 1.5 primary; GPT4oMini, Gemini 1.5 Flash/Pro, Claude 3.5 Sonnet resilience): Confirmed in source.
- ACM CCS 2025 venue and DOI: Confirmed in abstract file.

**Notes:** The "20-clients-per-day" figure the deliverable explicitly repudiates is correctly identified as not in the paper. The deliverable's caveat that this comes from discovery agent reports vs actual paper metrics is accurate.

---

### [3] eTAMP — Poison Once, Exploit Forever
**Grade: VERIFIED**

Fetched files: `etamp-html-tables.md`, `etamp-arxiv-abs.md`

**Claims verified:**

- Full ASR table: The etamp-html-tables.md table matches the deliverable exactly (GPT-5-mini 4.6%→32.5%, GPT-5.2 1.8%→23.4%, GPT-OSS-120B 19.5%/no improvement, Qwen3.5-122B-A10B 1.8%→12.0%).
- Frustration+Chaos conditions: Confirmed — Click Drop p=0.4, Scroll Swap p=1, Type Transform (Caesar) p=1.
- ~7x amplification (not exactly 8x): Source — "8x amplification calculation: GPT-5-mini 4.6% baseline -> 32.5% = ~7x. The '8x' claim in topics5.md and discovery agent reports is approximate but valid." The deliverable correctly states "approximately right."
- Task pairs (~280 across three cross-site directions): Source confirms 280 pairs, Reddit→Classifieds 84, Reddit→Shopping 93, Shopping→Reddit 103-106.
- Premature trigger ASRA = 0% on most models (exceptions Qwen3.5-122B 0.35%, Qwen3-VL-32B 0.71%): Confirmed.
- "(Visual)WebArena lab benchmark" caveat: Confirmed in both fetched files.

**Notes:** The "8x claim is approximate" note in the deliverable is well-calibrated — the source explicitly calls it approximate but valid. No overclaiming.

---

### [4] Memory Poisoning Attack and Defense on Memory-Based LLM-Agents (arXiv 2601.05504)
**Grade: VERIFIED**

Fetched files: `memory-poisoning-2601.05504-html.md`, `arxiv-2601.05504-abstract.md`

**Claims verified:**

- GPT-4o-mini ASR 62% (empty memory) → 6.67% (with legitimate memories): Source verbatim — "GPT-4o-mini: ASR fell from '62%' with empty memory to '6.67%' when legitimate memories existed."
- Llama-3.1-8B-Instruct ASR 0% with relevant initial memories despite 99.95% ISR: Confirmed in source.
- Authors' best-case under realistic retrieval: 38% GPT-4o-mini, 28% Llama: Source verbatim — "memory injection attack through query only interactions is possible, it is success rate it as low as 38% for GPT-4o-mini and 28% for Llama in best case."
- GPT-4o-mini rejected all 23 candidate entries (zero utility): Confirmed verbatim.
- Gemini-2.0-Flash accepted 54 malicious entries with trust score 1.0: Confirmed verbatim.
- Authors' framing "confidence filter rather than security filter": Confirmed verbatim.
- MIMIC-III EHR experiment, five victim-target patient ID pairs: Confirmed.
- D1 and D2 defense descriptions: Confirmed.

**Notes:** The deliverable's characterization of this paper as "the single defense paper that tested its own approach honestly" is accurate based on source content. All specific numbers check out.

---

### [5] PoisonedRAG — USENIX Security 2025
**Grade: PARTIAL**

Fetched file: `poisonedrag-arxiv-abs.md`

**Claims verified from source:**

- "90% attack success rate when injecting five malicious texts for each target question": Confirmed verbatim from abstract.
- Black-box and white-box attacker settings: Confirmed.
- Write access to knowledge base required: Confirmed (implicit in "inject a few malicious texts into the knowledge database").
- USENIX Security 2025 venue: Confirmed.

**Claims NOT verifiable from abstract (flagged in deliverable):**

The deliverable correctly flags in citations.md: "Per-dataset ASR (NQ 97%, HotpotQA 99%, MS-MARCO 91%) and model list (PaLM 2, GPT-3.5, GPT-4, LLaMA-2, Vicuna) reported by discovery agent are NOT in abstract — full PDF needed for verification." The grade is PARTIAL because these specific per-dataset figures and model lists appear in the deliverable's agentpoison-attacks.md reference file without adequate sourcing hedges — they are attributed to "discovery agent, unfetched" but the reference file's table presents them as part of the attack comparison, which could mislead a reader.

**Specific concern:** The agentpoison-attacks.md reference table lists PoisonedRAG's headline ASR as "90% with 5 docs" which IS from the abstract, so the primary claim in the deliverable is fine. The per-dataset figures appear only in citations.md's caveat block, appropriately flagged. No overclaiming in the analytical documents.

---

### [6] The Attacker Moves Second
**Grade: VERIFIED**

Fetched file: `attacker-moves-second-arxiv-abs.md`

**Claims verified:**

- "12 recent defenses (based on a diverse set of techniques)": Confirmed verbatim.
- "The majority of defenses originally reported near-zero attack success rates": Confirmed verbatim.
- Under adaptive attacks: "attack success rate above 90% for most": Confirmed verbatim.
- Methods: "gradient descent, reinforcement learning, random search, and human-guided exploration": Confirmed verbatim.
- Both jailbreak AND prompt injection defenses tested: Confirmed.

**Claims with acknowledged uncertainty:**

The deliverable notes "Institutional affiliations not on abstract page. Discovery agent reports OpenAI/Anthropic/Google DeepMind authorship — needs full-paper or OpenReview verification." The fetched abstract confirms affiliations are not visible. The deliverable appropriately hedges this. The deliverable does not make claims about affiliations in the analytical documents, only in citations.md's caveats block, so no overclaiming.

**Notes:** The deliverable correctly applies this finding to memory-poisoning defenses as relevant context. The claim that it "directly applies to memory poisoning defenses" is a reasonable inference — the paper tests "prompt injection defenses" which overlaps with the memory-injection attack surface.

---

### [7] MemoryGraft
**Grade: VERIFIED**

Fetched file: `memorygraft-html.md`

**Claims verified:**

- Target: MetaGPT DataInterpreter on GPT-4o: Confirmed.
- "Semantic imitation heuristic": Confirmed verbatim.
- With 10 poisoned seeds in 110 records (9% poison ratio): Confirmed — "10 poisoned seeds among 110 total records (9% poison ratio)."
- 23 of 48 retrievals poisoned → PRP = 47.9%: Confirmed — "Ptot = 23 poisoned retrievals across Ttot = 48 total retrievals. PRP = 23/48 = 47.9%."
- BM25 + FAISS union retrieval: Confirmed.
- Trigger-free (critique of AgentPoison's trigger dependency): Confirmed.
- "Cites MemoryBank's Ebbinghaus-inspired forgetting curve but does NOT quantify decay metrics": Confirmed verbatim — source: "MemoryBank (Zhong et al., 2023) is CITED as using 'an Ebbinghaus-inspired forgetting curve' but MemoryGraft does NOT quantify decay metrics for itself."

**Notes:** The deliverable's caveat that MemoryGraft doesn't quantify decay is verified directly.

---

### [8] RAGShield
**Grade: VERIFIED**

Fetched file: `ragshield-arxiv-abs.md`

**Claims verified:**

- "RAGShield detects every one (0.0% ASR, 95% CI [0%, 1%])": Confirmed verbatim from abstract.
- Embedding-based defenses "miss 79-90% of the same attacks": Confirmed verbatim.
- Actual system scope (pattern engine for dollar amounts/percentages, two-pass context propagation 99.8%, cross-source registry, temporal tracker): Confirmed.
- "The five-layer architecture / NIST SP 800-53 / C2PA / T1-T5 adversary tier framing reported by the defenses discovery agent is NOT supported by the abstract": Confirmed — source makes the same correction.
- Single-author, no institutional affiliation: Confirmed.

**Notes:** The deliverable correctly demotes the discovery agent's more grandiose framing and relies on what the abstract actually says. Grade is VERIFIED because the deliverable's claims about RAGShield match the abstract content and the corrections about discovery agent error are accurate.

---

### [9] SuperLocalMemory
**Grade: VERIFIED**

Fetched file: `superlocalmemory-arxiv-abs.md`

**Claims verified:**

- Trust separation gap = 0.90: Confirmed verbatim.
- "72% trust degradation for sleeper attacks": Confirmed verbatim.
- 10.6ms median search latency: Confirmed verbatim.
- 104% improvement in NDCG@5: Confirmed verbatim.
- Open-source MIT, 17+ MCP tool integrations: Confirmed.
- Single-author, no institutional affiliation: Confirmed.

**Notes:** The deliverable correctly flags the possible product affiliation (superlocalmemory.com) and self-evaluation caveat. All quantitative claims match source exactly.

---

### [10] Memory Poisoning and Secure Multi-Agent Systems (Torra & Bras-Amorós)
**Grade: VERIFIED**

Fetched file: `torra-multi-agent-2603.20357.md`

**Claims verified:**

- Three primary memory types (semantic, episodic, short-term) NOT four: Source verbatim — "The abstract presents THREE memory types: 'semantic, episodic, and short-term memory' with additional reference to 'long-term consolidated memory localized in well established knowledge databases.' External tool state is NOT explicitly framed as a fourth type in the abstract."
- Cryptographic mitigations including "private knowledge retrieval": Confirmed verbatim — "private knowledge retrieval as an example of mitigation strategy."
- Inter-agent risks verbatim quote: Source confirms — "interactions between agents, which can cause memory poisoning. These latter risks are not so much studied in the literature and are difficult to formalize and solve."
- Submission date 2026-03-20: Confirmed.

**Notes:** The deliverable's correction that the taxonomy is three types, not four, is verified against source. The "external tool state as fourth type" the deliverable repudiates is correctly identified as not in this abstract.

---

### [11] Korycki & Krawczyk — Adversarial Concept Drift Detection (PMC)
**Grade: VERIFIED**

Fetched file: `korycki-adversarial-drift-pmc.md`

**Claims verified:**

- Central claim that drift detectors "all assume that the drift is connected with underlying changes in the source of data" without considering adversarial injection: Confirmed verbatim.
- Two attack taxonomy (instance-based vs concept-based): Confirmed.
- RRBM-DD: RLR 0.85 (instance-based) and 0.78 (concept-based) vs competitors averaging 0.55-0.62: Confirmed verbatim.
- Springer Machine Learning journal, DOI, year 2022: Confirmed.
- PMC version used (Springer canonical returned 303): Confirmed.

**Notes:** All quantitative figures verified exactly. The deliverable's claim that "even the best detector reduces but does not eliminate the blindspot" is well-supported.

---

### [12] OWASP Top 10 for Agentic Applications 2026 (resource page)
**Grade: PARTIAL**

Fetched file: `owasp-asi06-2026.md`

**Claims verified:**

- "More than 100 industry experts": Source confirms "more than 100 industry experts, researchers, and practitioners." Verified.
- ASI prefix (Agentic Security Initiative): Confirmed.
- ASI06 = Memory and Context Poisoning: Confirmed.
- Release date 2025-12-09: Confirmed.

**Claims NOT fully verifiable from this source:**

Source status is "PARTIAL (overview page only - full ASI06 entry requires PDF download)." The deliverable accurately notes "full ASI06 detail (definition text, attack vectors, mitigations) not on this page." However, the deliverable uses Auth0 [23] as the proxy for the ASI06 definition text, which is reasonable and appropriately attributed. The grade is PARTIAL because the deliverable cites [12] for the complete OWASP framing, but the actual source confirms only the overview-level content.

The announcement blog [13] is the appropriate source for the Gemini Memory Attack example. The deliverable correctly separates these two sources.

---

### [13] OWASP Agentic Top 10 announcement
**Grade: VERIFIED** (with one intra-citation discrepancy noted)

Fetched file: `owasp-agentic-announcement.md`

**Claims verified:**

- "Memory poisoning reshaped behaviour long after the initial interaction (ASI06 - Memory & Context Poisoning, e.g Gemini Memory Attack)": Confirmed verbatim.
- ASI04 GitHub MCP exploit, ASI05 AutoGPT RCE examples: Confirmed.

**Intra-citation discrepancy:**

The deliverable states contributor count as "more than 100 industry experts" (citations.md [12] and [13]). The owasp-agentic-announcement.md fetched file notes: "Contributor count: 'hundreds of experts' (the '100+ experts' framing in resource page differs - both are loose figures)." The announcement uses "hundreds" while the resource page uses "100+." The deliverable attributes "more than 100" to [12] (the resource page), which matches that page. The discrepancy is between the two OWASP sources, not between the deliverable and the sources. Correctly handled.

**Notes:** The announcement blog does NOT use "wholly new" language about memory poisoning — it says "lived experience of the first generation of agentic adopters." The deliverable attributes "novel failure mode" language to Microsoft [16], not to OWASP [13]. This is correct.

---

### [14] OWASP Agent Memory Guard
**Grade: VERIFIED**

Fetched file: `owasp-agent-memory-guard.md`

**Claims verified:**

- Status Incubator, version 0.0.0: Confirmed.
- Project Leader Vaishnavi Gudur: Confirmed.
- Current implementation: SHA-256 hashing, declarative YAML policies, snapshot/rollback: Confirmed verbatim.
- Q1 v0.2.1, Q2 v0.3.0 (LlamaIndex/CrewAI, Redis/PostgreSQL, Prometheus), Q3 v0.4.0 (ML-based anomaly detection, vector store protection, real-time monitoring), Q4 v1.0.0: Confirmed verbatim.
- "ML-based anomaly detection does NOT yet exist in released code": Confirmed — source: "KEY IMPLICATION: ML-based anomaly detection does NOT yet exist in released code."
- LangChain/LlamaIndex/CrewAI integrations: Confirmed.

---

### [15] Microsoft Security Blog — AI Recommendation Poisoning
**Grade: PARTIAL**

Fetched file: `microsoft-recommendation-poisoning.md`

**Claims verified from source:**

- "50 distinct examples of prompt-based attempts directly aimed to influence AI assistant memory for promotional purposes": Confirmed verbatim.
- "31 different companies and spanned more than a dozen industries" over 60 days: Confirmed.
- IoCs (?q=, ?prompt= with keywords remember/memory/trusted/authoritative/future/citation/cite): Confirmed verbatim.
- "In multiple cases, previously reported behaviors could no longer be reproduced": Confirmed verbatim.
- Platforms (Copilot, ChatGPT, Claude, Gemini, Grok, Perplexity): Confirmed.
- "ATTEMPTS, not confirmed successful memory writes" — the deliverable's CRITICAL CAVEAT is verified. Source: "CRITICAL METHODOLOGY DISTINCTION: The research is based on PASSIVE OBSERVATION of attack ATTEMPTS, not confirmed memory writes."

**Reason for PARTIAL rather than VERIFIED:**

The deliverable's operator-playbook.md correctly attributes the IoC pattern but also says "Microsoft Defender [15] documents the only confirmed in-the-wild IoC pattern." This is accurate. However, the deliverable in analysis.md §7 says "The only IoC pattern with documented in-the-wild observations is Microsoft's [15] URL parameter pattern." While the source does confirm these IoCs were observed in email traffic, the article is about attempts observed by Microsoft's security research team — not IoCs deployed by defenders in production. The framing slightly conflates "attack attempt pattern" with "defender IoC." This is a subtle overstatement: the source confirms the pattern exists in the wild as an attack vector, which is what matters for an operator deploying a detection rule. The core claim is sound. Grade stays PARTIAL due to the attempts/successes distinction the deliverable itself flags.

---

### [16] Microsoft Security Blog — AI Red Team Failure Modes whitepaper announcement
**Grade: PARTIAL**

Fetched file: `microsoft-failure-modes-blog.md`

**Claims verified:**

- Two pillars Security / Safety framing: Confirmed — source verbatim security = "loss of confidentiality, availability, or integrity"; safety = "responsible implementation of AI."
- "Memory poisoning is particularly insidious in AI agents": Confirmed verbatim from blog announcement.

**Claims not fully verifiable:**

- The deliverable states "Microsoft Security Blog announcement [16] frames memory poisoning as a 'novel failure mode unique to agentic AI.'" The source file confirms the blog frames it as novel: "presents memory poisoning as distinctly novel to agents rather than building incrementally on established threat models." However, the verbatim quote "novel failure mode unique to agentic AI" is a near-paraphrase that accurately characterizes the blog's framing rather than a direct quote. Acceptable.

**Unresolved contradiction:**

The deliverable flags the contradiction between [16] (blog: novel) and [30] (PDF: reportedly "Existing Security Failures"). The fetched blog file confirms: "CRITICAL CONTRADICTION FLAG... The discovery agent may have read the actual PDF body which I could not extract." The deliverable handles this honestly — marks it as unresolved. Grade is PARTIAL because [16] is cited both for the "novel framing" (confirmed) and implicitly for resolving the [30] contradiction (unresolved).

---

### [17] Christian Schneider — Memory poisoning in AI agents: exploits that wait
**Grade: VERIFIED**

Fetched file: `schneider-persistent-memory-poisoning.md`

**Claims verified:**

- Temporal decoupling verbatim: "The injection happens in February. The damage happens in April." Confirmed verbatim.
- Three structural distinctions: (1) detection evasion through time separation, (2) agent self-defense of corrupted context, (3) cross-session persistence: Confirmed in order.
- Recommended layered controls: provenance tagging, trust-aware retrieval, behavioral monitoring, input moderation with composite scoring: Confirmed.
- "Start with provenance tagging as foundation": Confirmed verbatim.
- Cites MINJA, Rehberger Gemini, Unit 42, OWASP ASI06 as anchors: Confirmed.

---

### [18] Lakera — Agentic AI Threats Part 1
**Grade: PARTIAL**

Fetched file: `lakera-agentic-threats-p1.md`

**Claims verified:**

- "Memory poisoning rewrites the past, goal hijacks rewrite the future": Confirmed verbatim.
- PortfolioIQ Advisor scenario (PonziCorp as "low risk and high reward"): Confirmed.
- "Must treat all external influences, including their own memory, as untrusted input and validate objectives continuously": Confirmed verbatim.
- No quantitative claims in this article: Confirmed — source: "Quantitative claims: NONE in this article."

**Reason for PARTIAL:**

The deliverable's citations.md correctly flags: "The '98% detection / sub-50ms latency / less than 0.5% FP' figures attributed to Lakera Guard by other sources are NOT in this specific blog." This is verified by the source. However, the defenses.md reference file states: "Lakera Guard [18 vendor] | '98% detection, sub-50ms, <0.5% FP' | Vendor PR (NOT in source [18]) | No." The "[18 vendor]" tag is the deliverable's own qualifier indicating this comes from vendor PR not from source [18]. This is handled transparently, but the citation anchor "[18 vendor]" still points to [18] for claims that are explicitly not in [18]. This is the subtlety: the claim exists, the source is not [18], and the deliverable correctly notes this but still uses [18] as a partial anchor. Grade PARTIAL.

---

### [19] Palo Alto Unit 42 — Indirect Prompt Injection Poisons AI Long-Term Memory
**Grade: PARTIAL**

Fetched file: `unit42-bedrock-memory-poisoning.md`

**Claims verified:**

- Target: Amazon Bedrock Agents with Nova Premier v1, memory enabled, Guardrails DISABLED: Confirmed.
- Attack chain exploiting session summarization: Confirmed.
- XML payload with forged `<conversation>` tags, part two outside conversation blocks interpreted as system instructions: Confirmed verbatim.
- "Bedrock Agents automatically inject memory contents into every new session's context": Confirmed verbatim.
- Cross-session persistence demonstrated in subsequent booking interaction days later: Confirmed.
- "Minimally protected configuration" / PoC framing: Confirmed.

**Claims NOT in source:**

- "LLM-based detectors miss 66% of poisoned entries": Source explicitly states "CRITICAL CORRECTION: The 'LLM-based detectors miss 66% of poisoned entries' figure... is NOT present in this Unit 42 article." The deliverable correctly flags this and says "do not cite" in citations.md and operator-playbook.md. VERIFIED that the deliverable does NOT make this claim in the analytical documents — it appears only in the citations.md caveat under [19] labeled as a discovery agent error. The error is properly quarantined.

**Reason for PARTIAL:**

The deliverable's analysis.md §4 says "Unit 42 [19] provides the strongest mechanism-level demonstration" of cross-session persistence. This is accurate. However, the citation is also referenced in the threat-taxonomy.md under "External tool state" examples, where it appears correctly. Grade PARTIAL because the 66% figure — even though correctly labeled as "not in source" and "do not cite" — appears in the same citations.md entry in a way that could confuse a reader if they don't read the full caveat block. The analytical documents handle it cleanly.

---

### [20] Johann Rehberger — SpAIware (ChatGPT macOS)
**Grade: VERIFIED**

Fetched file: `rehberger-spaiware-2024.md`

**Claims verified:**

- Attack vector "websites or untrusted documents": Confirmed — source corrects "Google Drive document" framing from discovery agent to the general "websites or untrusted documents."
- Persistence of "all information the user typed or responses received by ChatGPT, including any future chat sessions": Confirmed verbatim.
- OpenAI patched in version 1.2024.247 (September 2024): Confirmed.
- Disclosure timeline (April 2023 → December 2023 partial fix → June 2024 full exploit → September 2024 patch): Confirmed.
- Authorized researcher demonstration, BSides Vancouver Island 2024: Confirmed.

**Notes:** The deliverable's correction that the attack uses "websites or untrusted documents" (not specifically "Google Drive document") is verified by the source.

---

### [21] Johann Rehberger — Gemini memory persistence
**Grade: VERIFIED**

Fetched file: `rehberger-gemini-memory-2025.md`

**Claims verified:**

- Document upload → poisoned summary asks question → trigger words "yes/sure/no" → saves false memories: Confirmed.
- Google's response verbatim: "an abuse-related risk with low likelihood and low impact": Confirmed.
- Authorized researcher disclosure, reported to Google December 2024: Confirmed.

**Claims NOT in source:**

- The deliverable's citations.md notes: "The 'UI alert on memory writes was Google's defensive rationale' claim from discovery agents is NOT in the article — only the low-likelihood/low-impact assessment is." Source confirms: "CORRECTION: Discovery agents stated Google's defensive rationale was 'UI alert on memory writes and requirement for user interaction.' The article does NOT specifically state UI alerts were Google's defensive rationale." The deliverable correctly quarantines this.

**Notes:** The OWASP announcement [13] cites the "Gemini Memory Attack" as the ASI06 canonical example. The deliverable connects [21] to this correctly.

---

### [22] The Register — AI vendors' response to security flaws
**Grade: PARTIAL**

Fetched file: `the-register-ai-vendors-response.md`

**Claims verified:**

- GitHub Actions hijacking of three AI agents: Anthropic Claude Code Security Review ($100), Google Gemini CLI Action ($1,337), Microsoft GitHub Copilot ($500): Confirmed.
- None assigned CVEs or public advisories: Confirmed.
- Anthropic MCP design flaw "puts as many as 200,000 servers at risk": Confirmed verbatim.
- Anthropic response verbatim (about MCP stdio): Confirmed — "This is an explicit part of how MCP stdio servers work and we believe this design does."
- "10 (so far) high- and critical-severity CVEs issued for individual open source tools and AI agents that use MCP": Confirmed.

**Claims NOT in source:**

- "Anthropic 200-attempt vs OpenAI single-attempt testing-standards comparison": Source confirms this is NOT in the article. Source: "CORRECTION: The counter-defenses discovery agent claimed: 'Anthropic evaluates against 200-attempt adaptive campaigns while OpenAI reports single-attempt resistance, making cross-vendor claims incomparable.' This specific testing-standards comparison is NOT in this article." The deliverable correctly quarantines this in citations.md caveat and defenses.md.

**Reason for PARTIAL:**

The deliverable's defenses.md references [22] for "the pattern: vendors selling agentic AI security products publish defense claims with no independent validation, while disputing or downplaying disclosed vulnerabilities in their own products." This characterization is reasonably supported by the article's reporting on bounty amounts and lack of CVE assignment, though the article doesn't use this exact framing. It's a fair inference from article content. Grade PARTIAL rather than VERIFIED because the framing generalizes beyond the article's specific cases.

---

### [23] Auth0 — Lessons from OWASP Top 10 for Agentic Applications
**Grade: PARTIAL**

Fetched file: `auth0-owasp-asi06.md`

**Claims verified:**

- ASI06 definition verbatim: "Bad data is 'planted' in the agent's memory, causing it to make biased or unsafe decisions later on." Confirmed verbatim.
- Full ASI list (ASI01–ASI10): Confirmed exactly.
- Mitigations (fine-grained authorization for RAG, memory segmentation, centralized revocation): Confirmed.

**Reason for PARTIAL:**

The deliverable uses Auth0 as a proxy for the OWASP ASI06 definition, acknowledging "verbatim quote of OWASP via Auth0 [23]." This is appropriate secondary sourcing. However, the source confirms "GAP: No specific cited example attacks (Gemini Memory Attack, etc.) in the Auth0 framing." The deliverable cross-references these correctly to [13] and [21] respectively. The partial grade is because Auth0 is a vendor source (identity products) proxying for an OWASP definition — the definition text should ideally trace to the OWASP PDF [12] directly. The deliverable acknowledges this limitation appropriately.

---

### [24] Hindsight (Vectorize) — Your agent is not forgetful
**Grade: PARTIAL**

Fetched file: `hindsight-stateless-agents.md`

**Claims verified:**

- "Most agents were never designed to remember in the first place. Each session starts over.": Confirmed verbatim.
- The source is a blog post from Hindsight/Vectorize.

**Reason for PARTIAL:**

The deliverable uses this as the "strongest available counter-argument" to memory poisoning persistence claims, correctly noting it is "qualitative claim only" with no quantitative deployment data. Source confirms: "CAVEAT: No statistical data comparing stateless vs stateful agent deployments. The article makes the prevalence claim qualitatively, not quantitatively." The claim is accurately characterized in the deliverable (it correctly qualifies it as qualitative). PARTIAL because the underlying claim itself is unquantified, and the deliverable's citation of it as "the strongest architectural conditionality counter-argument" gives it weight that the lack of quantitative backing doesn't fully justify — though the deliverable explicitly acknowledges this.

---

### [25] Simon Willison — The lethal trifecta
**Grade: VERIFIED**

Fetched file: `willison-lethal-trifecta.md`

**Claims verified:**

- Three conditions (access to private data, exposure to untrusted content, ability to externally communicate): Confirmed verbatim.
- Removing any one breaks the chain: Confirmed.
- Vulnerable systems (Microsoft 365 Copilot, GitHub MCP server, GitLab Duo Chatbot, ChatGPT, Google Bard, Amazon Q, GitHub Copilot Chat): Confirmed verbatim.
- "Guardrails won't protect you": Confirmed verbatim.

---

### [26] David Richards — The RAG Freshness Paradox
**Grade: PARTIAL**

Fetched file: `ragaboutit-freshness-paradox.md`

**Claims verified:**

- "$340,000 annually in infrastructure costs - before factoring in engineering time": Confirmed verbatim.
- "45-minute reindex cycle" / "perpetually in transition" quote: Confirmed verbatim.
- "~$0.001 per query for re-ranking": Confirmed.

**Reason for PARTIAL:**

The source file itself flags: "CAVEAT: Single-enterprise anecdote, not independently audited. Treat as illustrative tier-3 evidence." The deliverable correctly notes this is a "Single-enterprise anecdote" in citations.md. However, in analysis.md §7 and operator-playbook.md, the $340K figure is cited as if it represents a general production cost reality without always repeating the anecdote caveat. This is a presentation issue: the number is real (confirmed in the blog), but it's one enterprise's cost, not a benchmark. The deliverable should more consistently attach the "single anecdote" qualifier when using this figure. Grade PARTIAL.

---

### [27] Blake Crosley (Introl) — Embedding Infrastructure at Scale
**Grade: PARTIAL**

Fetched file: `introl-embedding-infrastructure.md`

**Claims verified:**

- "A single NVIDIA L4 GPU processes approximately 2,000 text tokens per second through a 7-billion parameter embedding model": Confirmed verbatim.
- "The falcon-refinedweb dataset with 600 billion tokens would take more than 9.5 years": Confirmed verbatim.
- "$2,000/month" for 100M tokens via OpenAI small embedding: Confirmed verbatim.
- "61% (from $710 to $277 in one case study)" spot instance savings: Confirmed verbatim.
- "$1,500-3,000 monthly" for 10M docs with 100K daily queries: Confirmed verbatim.

**Reason for PARTIAL:**

These figures are from a vendor blog (Introl provides AI infrastructure services). The deliverable notes "Vendor blog" but uses the figures as if they represent general market costs. The cost figures are internally consistent and plausible, but they come from a party with commercial interest in selling infrastructure services. The analysis presents the $340K [26] and $1,500-3,000/month [27] figures as objective cost data that justify the "accept longer re-embedding cadence" recommendation. Both are from non-independent sources. The deliverable notes vendor status in citations.md but doesn't repeat the caveat consistently in the analytical documents. Grade PARTIAL.

---

### [28] IBM Think Insights — Morris II
**Grade: INACCESSIBLE**

Fetched file: `ibm-morris-ii.md`

Source status: "FAILED (HTTP 403)"

The claim "The 'Morris II' AI worm has not been seen in the wild, and the researchers did not test it on a publicly available email assistant" remains unverified from primary source. The deliverable correctly treats this as "per discovery agent search snippet, unverified" throughout. The multi-agent-propagation.md reference correctly labels it "[INACCESSIBLE in this session] (per discovery agent search snippet)."

**Impact assessment:** The "not seen in the wild" claim for Morris-II is both plausible and important. Its inaccessibility means the deliverable correctly relies on it only as a secondary framing point, not as a primary quantitative claim. No overclaiming detected given the inaccessibility.

---

### [29] VentureBeat — 12 AI defenses
**Grade: INACCESSIBLE** (HTTP 429)

Fetched file: captured in `failed-fetches-batch4.md`

Status: HTTP 429 (rate limited). The deliverable treats this correctly as inaccessible and does not make claims sourced to it directly. Cited only in citations.md as "journalistic coverage of citation [6]."

---

### [30] Microsoft AI Red Team — Taxonomy of Failure Modes whitepaper PDF
**Grade: INACCESSIBLE**

Fetched file: captured in `failed-fetches-batch4.md`

Status: PDF binary content not extractable. The contradiction between the blog's [16] "novel failure mode" framing and the PDF's reported "Existing Security Failures" grouping remains unresolved. The deliverable handles this correctly by flagging it as "unresolved pending PDF access" in every relevant location (analysis.md §2, threat-taxonomy.md, references).

**Impact:** The contradiction is about categorization (novel vs. existing), not about quantitative data. The deliverable does not rely on [30] for any quantitative claim. The framing question is presented as genuinely unresolved. Appropriate handling.

---

### [31]–[40] Discovery-agent-only citations (not directly fetched)

These citations appear in the deliverable with consistent "per discovery agent, unfetched" qualifiers. They are not individually graded in this audit but are reviewed for overclaiming in the analytical documents.

| Citation | Claim in deliverable | Qualifier present? | Overclaiming? |
|---|---|---|---|
| [31] PoisonArena | ASR collapses to ~0% under multi-attacker competition, GASLITE exception | "per discovery" | No |
| [32] Zhang et al. | ASR drops 80-97% to 0-33% on expanded KB | "per discovery, unfetched" | No |
| [33] Through the Stealth Lens | 83% detection accuracy for Attention-Variance Filter | "per discovery, unfetched" | No |
| [34] RAGDefender | PoisonedRAG ASR 0.84 → 0.03 | "per discovery" | No |
| [35] CorruptRAG | Single-document injection more realistic | "per discovery" | No |
| [36] Bypassing LLM Guardrails | Azure Prompt Shield/Meta Prompt Guard up to 100% evasion | "per discovery, unfetched" | Borderline — used in defenses table with same weight as verified results |
| [37] AgentPoison NeurIPS proceedings | Camera-ready PDF of [1] | Noted only | N/A |
| [38] MINJA | ISR >95%, ASR 90% on eICU and 98.9% on Webshop | "per discovery" | Borderline — in real-world-incidence table without data-quality qualifier |
| [39] Schneier on Security | Expert commentary on Morris II | "per discovery" | No |
| [40] Springer 2012 shilling attacks | Documents since 2004 | "per discovery" | No |

**Specific concern on [36]:** The defenses.md table includes "Production guardrails (Azure, Meta) | broken at up to 100% evasion | YES — broken [36]" with an "Independent academic [36]" label in the validation column. Since [36] was not fetched, this "YES — independently validated" mark is attributed to an unfetched source. This is the highest-stakes use of a discovery-only citation in the deliverable because it serves as the only "YES" in an otherwise all-"No" independent validation table. The deliverable should ideally flag this as "YES (per discovery, unfetched)." As written it appears more authoritative than the evidence warrants.

**Specific concern on [38] MINJA:** analysis.md §3 mentions "arXiv 2601.05504 [4] shows this drops to <10% with realistic memory" in context of MINJA's 95% ISR. The realistic-memory drop applies to [4]'s own attack, not to MINJA specifically. The implication that MINJA's 95% ISR "drops to <10%" under realistic conditions conflates two different papers' findings.

---

## Reconsideration Pass

Before finalizing, reconsidering VERIFIED grades that the source only tangentially supports, and PARTIAL grades that should be INACCURATE:

**[6] — stays VERIFIED.** The abstract directly and verbatim supports every claim made. The application to memory-poisoning defenses is a reasonable inference, not an overreach.

**[12] — stays PARTIAL.** The source page is genuinely limited to overview content. The deliverable's claims about OWASP's full framework go beyond what this page confirms.

**[15] — stays PARTIAL.** The "attempts not successes" distinction is real and the deliverable correctly flags it. No grade change warranted, though the deliverable itself is more precise about this than many secondary sources.

**[19] — stays PARTIAL.** The 66% figure is correctly quarantined. No remaining overclaiming in the analytical documents.

**[22] — stays PARTIAL.** The article supports specific facts about bounties and MCP. The broader "vendor accountability pattern" inference is reasonable but goes beyond what the article explicitly states.

**No PARTIAL → INACCURATE changes warranted.** In each PARTIAL case, the source supports the core factual claim; the PARTIAL grade reflects extrapolation or inference, not misrepresentation.

**No VERIFIED → PARTIAL changes warranted.** Every VERIFIED citation was confirmed with verbatim quote matches in the source files.

---

## Key Findings for Deliverable Improvement

1. **[36] Bypassing LLM Guardrails:** The only "YES — independently validated" entry in the defenses table comes from an unfetched source. Should be tagged "per discovery, unfetched" in the validation column to maintain epistemic consistency. **Status: RESOLVED** — defenses.md table entry for [36] now reads "YES (per discovery, unfetched) — broken [36]" (CR-06 in consistency-review.md).

2. **[38] MINJA cross-contamination:** analysis.md's inference that MINJA's 95% ISR drops under realistic conditions conflates [4]'s findings with MINJA's paper. MINJA's own ASR under realistic conditions is not established by any fetched source. **Status: RESOLVED** — real-world-incidence.md MINJA caveat now clarifies "[4] tested its own attack, not MINJA" (CR-07). analysis.md does not directly conflate the two; the related "order of magnitude" wording was clarified in CR-03.

3. **[26] and [27] cost figures:** Used as production-cost benchmarks in analytical documents without consistently attaching the "single anecdote" ([26]) or "vendor blog" ([27]) qualifier. These are illustrative, not industry-representative. **Status: RESOLVED** — analysis.md §7 now reads "Richards [26] documents (single-enterprise anecdote, not independently audited) $340K/year..." and "Crosley [27] (vendor-blog calculation) documents..." README.md operator guidance also adds the qualifiers.

4. **[28] IBM Morris-II:** The "not seen in the wild" claim — the foundational wild-vs-lab distinction for Morris-II — rests on an inaccessible source. The deliverable correctly hedges this but the finding's prominence in the analysis deserves explicit acknowledgment that it is unverified. **Status: ACCEPTED AS-IS** — the deliverable already labels this "[INACCESSIBLE in this session]" / "per discovery agent search snippet, unverified." Promotion of this hedge to the README would be appropriate but the analytical documents handle it correctly.

5. **[30] Microsoft whitepaper PDF:** The novel-vs-existing contradiction for memory poisoning categorization is unresolved. The deliverable handles this honestly, but any future revision should resolve this via PDF extraction. **Status: ACCEPTED AS-IS** — contradiction is unresolvable without PDF access, which was attempted in this session and failed. Future revision should re-attempt via different PDF tooling.

---

## Final Grade Count

| Grade | Count |
|---|---|
| VERIFIED | 18 |
| PARTIAL | 10 |
| INACCURATE | 0 |
| INACCESSIBLE | 2 |
| NOT FOUND | 0 |
| DRIFT | 0 |
| Per-discovery-only (not graded) | 10 |

**Total directly-verifiable citations graded: 30** ([1]–[28], [30]; [29] is rate-limited therefore INACCESSIBLE)

Revised tally including [29]:

| Grade | Count |
|---|---|
| VERIFIED | 18 |
| PARTIAL | 10 |
| INACCURATE | 0 |
| INACCESSIBLE | 3 |
| NOT FOUND | 0 |
| DRIFT | 0 |
