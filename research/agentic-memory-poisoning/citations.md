# Citations — Memory Poisoning of Agentic AI

Numbered list of every source consulted. Each entry includes the URL, source quality tier, the specific data extracted, and any caveats (vendor conflict, accessibility issue, contradictions).

**Source tiers:**
- **Tier 1**: Peer-reviewed papers, government/institutional reports
- **Tier 2**: Manufacturer specs, established reference sites, university publications
- **Tier 3**: Industry blogs, conference talks, well-known practitioners
- **Tier 4**: Forums, personal blogs, GitHub discussions, social media

---

## Academic primary sources

### [1] AgentPoison — Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases
- **URL:** https://arxiv.org/abs/2407.12784 (HTML body: https://arxiv.org/html/2407.12784v1)
- **Authors:** Zhaorun Chen, Zhen Xiang, Chaowei Xiao, Dawn Song, Bo Li
- **Venue:** NeurIPS 2024
- **Tier:** 1
- **Data extracted (verified against HTML body):** Per-agent results — Agent-Driver (ASR-r 80.0%, ASR-t 56.8%, corpus 23,000, 20 poisoned); ReAct-StrategyQA (65.5%/58.6%, 10,000, 4); EHRAgent (98.9%/58.3%, 700, 2). Embedders tested: DPR, ANCE, BGE, REALM, ORQA, text-embedding-ada-002. Threat model requires "white-box access to the RAG embedder of the victim agent for trigger optimization" with empirical transferability to black-box.
- **Caveats:** The abstract's headline ">80% ASR at <0.1% poison rate" conflates ASR-r (retrieval) with end-to-end ASR-t (~58% average). EHRAgent poison rate is 2/700 = 0.286%, exceeding the <0.1% claim. White-box embedder access is not realistic for closed-API embedders.

### [2] Morris-II / "Here Comes The AI Worm" / "Preventing the Propagation of Adversarial Self-Replicating Prompts Within GenAI Ecosystems"
- **URL:** https://arxiv.org/abs/2403.02817 (HTML v2: https://arxiv.org/html/2403.02817v2)
- **Authors:** Stav Cohen, Ron Bitton, Ben Nassi (Cornell Tech, Technion, Intuit)
- **Venue:** ACM CCS 2025 (DOI 10.1145/3719027.3765196)
- **Tier:** 1
- **Data extracted (verified against HTML v2):** GenAI backends — primary Gemini Flash 1.5; resilience analysis on GPT4oMini, Gemini 1.5 Flash, Gemini 1.5 Pro, Claude 3.5 Sonnet. Payload type: TEXT only (no adversarial images in v2). Two attack scenarios — data exfiltration and ecosystem disruption. Propagation: "the worm is expected to propagate to new clients every five emails a user receives/sends" (k=20 context). Replication/payload success >90% through hop 11, degrading to 40-80% by hop 20. Virtual Donkey defense: TPR 1.0, FPR 0.015 on in-distribution, AUC 0.96-1.0 OOD.
- **Caveats:** Worm tested only on researcher VMs, not on any publicly available system. Per IBM Think (per discovery snippet, source [28] inaccessible) the worm "has not been seen in the wild." Discovery agent reported text + image payloads — only text confirmed in v2.

### [3] Poison Once, Exploit Forever — Environment-Injected Memory Poisoning Attacks on Web Agents (eTAMP)
- **URL:** https://arxiv.org/abs/2604.02623 (HTML: https://arxiv.org/html/2604.02623)
- **Authors:** Wei Zou, Mingwen Dong, Miguel Romero Calvo, Shuaichen Chang, Jiang Guo, Dongkyu Lee, Xing Niu, Xiaofei Ma, Yanjun Qi, Jiarong Jiang
- **Submission:** 2026-04-03 (v1), 2026-04-07 (v2)
- **Tier:** 1
- **Data extracted (verified against HTML body Table 1):** ASRB by model — GPT-5-mini: 4.6% baseline, 32.5% best (Frustration+Chaos); GPT-5.2: 1.8% / 23.4%; GPT-OSS-120B: 19.5% (no improvement under stress); Qwen3.5-122B-A10B: 1.8% / 12.0%. Frustration amplification on GPT-5-mini: ~7x (4.6% → 32.5%, the topics5.md "8x" claim is approximate). 280 task pairs across three cross-site directions (Reddit→Classifieds 84, Reddit→Shopping 93, Shopping→Reddit 103-106). Chaos Monkey: Click Drop p=0.4, Scroll Swap p=1, Type Transform (Caesar) p=1. Premature trigger ASRA = 0% on most models (exceptions Qwen3.5-122B 0.35%, Qwen3-VL-32B 0.71%).
- **Caveats:** Controlled (Visual)WebArena lab benchmark — NOT production observation.

### [4] Memory Poisoning Attack and Defense on Memory-Based LLM-Agents
- **URL:** https://arxiv.org/abs/2601.05504 (HTML: https://arxiv.org/html/2601.05504v2)
- **Authors:** Balachandra Devarangadi Sunil, Isheeta Sinha, Piyush Maheshwari, Shantanu Todmal, Shreyan Mallik, Shuchi Mishra (University of Massachusetts)
- **Submission:** 2026-01-09 (v1)
- **Tier:** 1
- **Data extracted (verified against HTML):** Realistic-memory dilution: GPT-4o-mini ASR 62% (empty memory) → 6.67% (with legitimate memories); Llama-3.1-8B-Instruct ASR 0% with relevant initial memories despite 99.95% ISR. Authors' best-case figures under realistic retrieval: 38% GPT-4o-mini, 28% Llama. Defenses: (D1) Input/output moderation with composite trust scoring; (D2) Memory sanitization with temporal decay. Calibration failure: GPT-4o-mini rejected all 23 candidate entries (zero utility); Gemini-2.0-Flash accepted 54 malicious entries with trust score 1.0. Authors' framing: "the defense layer operated essentially as a 'confidence filter' rather than a 'security filter.'"
- **Caveats:** MIMIC-III EHR experiment, 5 victim-target patient ID pairs, small-N. The realistic-memory dilution is the strongest published evidence that the attack does not generalize to populated memory stores at scale.

### [5] PoisonedRAG — Knowledge Corruption Attacks to RAG of LLMs
- **URL:** https://arxiv.org/abs/2402.07867
- **Authors:** Wei Zou, Runpeng Geng, Binghui Wang, Jinyuan Jia
- **Venue:** USENIX Security 2025
- **Tier:** 1
- **Data extracted (abstract only):** "PoisonedRAG could achieve a 90% attack success rate when injecting five malicious texts for each target question." Solutions for both black-box and white-box settings. Write access to KB required.
- **Caveats:** Per-dataset ASR (NQ 97%, HotpotQA 99%, MS-MARCO 91%) and model list (PaLM 2, GPT-3.5, GPT-4, LLaMA-2, Vicuna) reported by discovery agent are NOT in abstract — full PDF needed for verification. The PoisonArena results separately show ASR collapses to ~0% under multi-attacker competition (citation [31]).

### [6] The Attacker Moves Second — Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections
- **URL:** https://arxiv.org/abs/2510.09023 (OpenReview: https://openreview.net/forum?id=7B9mTg7z25)
- **Authors:** Nasr, Carlini, Sitawarin, Schulhoff, Hayes, Ilie, Pluto, Song, Chaudhari, Shumailov, Thakurta, Xiao, Terzis, Tramèr (14 authors)
- **Submission:** 2025-10-10
- **Tier:** 1
- **Data extracted:** "12 recent defenses (based on a diverse set of techniques)" tested. Original defense claims: "the majority of defenses originally reported near-zero attack success rates." Under adaptive attacks: "attack success rate above 90% for most." Methods: "gradient descent, reinforcement learning, random search, and human-guided exploration." Both jailbreak AND prompt injection defenses tested.
- **Caveats:** Institutional affiliations not on abstract page. Discovery agent reports OpenAI/Anthropic/Google DeepMind authorship — needs full-paper or OpenReview verification.

### [7] MemoryGraft — Persistent Compromise of LLM Agents via Episodic Memory Poisoning
- **URL:** https://arxiv.org/abs/2512.16962 (HTML: https://arxiv.org/html/2512.16962v1)
- **Authors:** Saksham Sahai Srivastava, Haoyu He (School of Computing, University of Georgia)
- **Submission:** 2025-12
- **Tier:** 1
- **Data extracted:** Targets MetaGPT DataInterpreter on GPT-4o via "semantic imitation heuristic" (agents replicate patterns from retrieved successful tasks). With 10 poisoned seeds in 110 records (9% poison ratio): 23 of 48 retrievals are poisoned → PRP = 47.9%. Retrieval architecture: BM25 lexical + FAISS embedding union. Trigger-free (cited as critique of AgentPoison's trigger dependency). Cites MemoryBank's Ebbinghaus-inspired forgetting curve but does NOT quantify decay metrics.
- **Caveats:** Preprint, no peer-review venue confirmed.

### [8] RAGShield (provenance-verified RAG defense)
- **URL:** https://arxiv.org/abs/2604.00387
- **Author:** KrishnaSaiReddy Patil (single author, no institutional affiliation listed)
- **Submission:** 2026-04
- **Tier:** 1 (but yellow flag — single-author, self-evaluated)
- **Data extracted (abstract only):** "RAGShield detects every one (0.0% ASR, 95% CI [0%, 1%])" across 430 attacks. Embedding-based defenses "miss 79-90% of the same attacks." Mechanisms: pattern-based engine for dollar amounts/percentages, two-pass context propagation (99.8% entity detection), cross-source registry verification, temporal tracker.
- **Caveats:** The "five-layer architecture / NIST SP 800-53 / C2PA / T1-T5 adversary tier" framing reported by the defenses discovery agent is NOT supported by the abstract. The actual paper appears more narrowly scoped. No latency/throughput overhead numbers in abstract. Single-author, no independent replication.

### [9] SuperLocalMemory — Privacy-Preserving Multi-Agent Memory with Bayesian Trust Defense
- **URL:** https://arxiv.org/abs/2603.02240
- **Author:** Varun Pratap Bhardwaj (single author, no institutional affiliation visible)
- **Submission:** 2026-02-17
- **Tier:** 1 (yellow flag — single-author, self-evaluated, possible product affiliation)
- **Data extracted:** Trust separation gap = 0.90; "72% trust degradation for sleeper attacks"; 10.6ms median search latency; 104% improvement in NDCG@5. Open-source (MIT) with 17+ MCP tool integrations.
- **Caveats:** No institutional affiliation. Mention of superlocalmemory.com domain suggests possible product offering. Self-evaluated.

### [10] Memory Poisoning and Secure Multi-Agent Systems
- **URL:** https://arxiv.org/abs/2603.20357
- **Authors:** Vicenç Torra, Maria Bras-Amorós (affiliations not on abstract page; per discovery: Umeå University and Universitat Politècnica de Catalunya)
- **Submission:** 2026-03-20
- **Tier:** 1
- **Data extracted:** Memory taxonomy: "semantic, episodic, and short-term memory" plus "long-term consolidated memory localized in well established knowledge databases" — THREE primary types, not four as some discovery agents reported. Cryptographic mitigations including "private knowledge retrieval" as defense. Inter-agent risks (verbatim): "interactions between agents, which can cause memory poisoning. These latter risks are not so much studied in the literature and are difficult to formalize and solve."

### [11] Adversarial concept drift detection under poisoning attacks for robust data stream mining
- **URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC9162121/ (Springer canonical: https://link.springer.com/article/10.1007/s10994-022-06177-w — returned 303)
- **Authors:** Łukasz Korycki, Bartosz Krawczyk
- **Venue:** Machine Learning (Springer), DOI 10.1007/s10994-022-06177-w
- **Year:** 2022
- **Tier:** 1
- **Data extracted:** Existing drift detectors "all assume that the drift is connected with underlying changes in the source of data" without considering "a malicious injection of false data that simulates a concept drift." Two attack taxonomies — instance-based vs concept-based poisoning. RRBM-DD detector: RLR scores 0.85 (instance-based) and 0.78 (concept-based) vs competitors averaging 0.55-0.62.
- **Caveats:** Springer canonical URL returned 303; PMC version used for extraction.

---

## Institutional and framework sources

### [12] OWASP Top 10 for Agentic Applications 2026 (resource page)
- **URL:** https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- **Publisher:** OWASP GenAI Security Project
- **Publication:** 2025-12-09
- **Tier:** 2
- **Data extracted:** Identifier prefix is "ASI" (Agentic Security Initiative). Developed with "more than 100 industry experts." ASI06 = Memory and Context Poisoning.
- **Caveats:** Overview page only — full ASI06 detail (definition text, attack vectors, mitigations) not on this page. Need PDF download for completeness.

### [13] OWASP Agentic Top 10 announcement
- **URL:** https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/
- **Publication:** 2025-12-09
- **Tier:** 2
- **Data extracted (verbatim):** "Memory poisoning reshaped behaviour long after the initial interaction (ASI06 - Memory & Context Poisoning, e.g Gemini Memory Attack)." Other examples: ASI04 GitHub MCP exploit, ASI05 AutoGPT RCE.

### [14] OWASP Agent Memory Guard project page
- **URL:** https://owasp.org/www-project-agent-memory-guard/
- **Project Leader:** Vaishnavi Gudur
- **Status:** Incubator, version 0.0.0
- **Tier:** 2
- **Data extracted:** Current implementation: SHA-256 hashing, declarative YAML policies, snapshot/rollback. 2026 roadmap: Q1 v0.2.1 (project setup); Q2 v0.3.0 (LlamaIndex/CrewAI integrations, Redis/PostgreSQL backends, Prometheus metrics); **Q3 v0.4.0 (ML-based anomaly detection, vector store protection, real-time monitoring dashboard — NOT YET RELEASED)**; Q4 v1.0.0 stable + Lab promotion application. LangChain/LlamaIndex/CrewAI integration.
- **Caveats:** ML-based anomaly detection is roadmap, not released — defenses attributed to it cannot be cited as effective today.

### [15] Microsoft Security Blog — AI Recommendation Poisoning
- **URL:** https://www.microsoft.com/en-us/security/blog/2026/02/10/ai-recommendation-poisoning/
- **Authors:** Noam Kochavi, Shaked Ilan, Sarah Wolstencroft (Microsoft Defender Security Research)
- **Publication:** 2026-02-10
- **Tier:** 2
- **Data extracted (verbatim):** "50 distinct examples of prompt-based attempts directly aimed to influence AI assistant memory for promotional purposes. These attempts originated from 31 different companies and spanned more than a dozen industries" (60-day observation). IoCs: URL parameters ?q= and ?prompt= with keywords "remember", "memory", "trusted", "authoritative", "future", "citation", "cite". Mitigation status: "In multiple cases, previously reported behaviors could no longer be reproduced." Platforms targeted: Copilot, ChatGPT, Claude, Gemini, Grok, Perplexity.
- **Critical caveat:** Microsoft observed ATTEMPTS in email traffic, NOT confirmed successful memory writes against real users. Attack class is promotional/commercial spam, not full system compromise.

### [16] Microsoft Security Blog — AI Red Team Failure Modes whitepaper announcement
- **URL:** https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/
- **Publication:** 2025-04-24
- **Tier:** 2
- **Data extracted:** Two pillars — Security ("loss of confidentiality, availability, or integrity") and Safety ("responsible implementation of AI"). Announcement frames memory poisoning as a NOVEL failure mode unique to agentic AI: "memory poisoning is particularly insidious in AI agents."
- **Caveats:** The full whitepaper PDF (https://cdn-dynmedia-1.microsoft.com/.../Taxonomy-of-Failure-Mode-in-Agentic-AI-Systems-Whitepaper.pdf) returned binary content that could not be extracted. The counter-threat-taxonomy discovery agent claimed Microsoft groups memory poisoning under "Existing Security Failures" — this is contradicted by the announcement and unverified against the PDF body. **Flagged contradiction.**

---

## Practitioner and vendor sources

### [17] Christian Schneider — Memory poisoning in AI agents: exploits that wait
- **URL:** https://christian-schneider.net/blog/persistent-memory-poisoning-in-ai-agents/
- **Author:** Christian Schneider (independent application/AI security architect)
- **Publication:** 2026-02-26
- **Tier:** 3
- **Data extracted:** Temporal decoupling concept (verbatim): "The injection happens in February. The damage happens in April." Three structural distinctions from prompt injection: (1) detection evasion through time separation; (2) agent self-defense of corrupted context; (3) cross-session persistence. Cites MINJA, Rehberger Gemini, Unit 42, OWASP ASI06 as anchors. Recommends: provenance tagging, trust-aware retrieval, behavioral monitoring, input moderation with composite scoring. "Start with provenance tagging as foundation."

### [18] Lakera — Agentic AI Threats Part 1: Memory Poisoning and Long-Horizon Goal Hijacks
- **URL:** https://www.lakera.ai/blog/agentic-ai-threats-p1
- **Publication:** 2025-11-12
- **Tier:** 3 (vendor blog — Lakera sells Lakera Guard, Lakera Red)
- **Data extracted (verbatim):** "Memory poisoning rewrites the past, goal hijacks rewrite the future." PortfolioIQ Advisor scenario: AI ingests malicious due-diligence PDF, reframes "PonziCorp" fraud as "low risk and high reward." Defense principle: "must treat all external influences, including their own memory, as untrusted input and validate objectives continuously."
- **Caveats:** No quantitative claims in this article. The "98% detection / sub-50ms latency / less than 0.5% FP" figures attributed to Lakera Guard by other sources are NOT in this specific blog. Vendor-product conflict.

### [19] Palo Alto Unit 42 — Indirect Prompt Injection Poisons AI Long-Term Memory
- **URL:** https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/
- **Authors:** Jay Chen, Royce Lu
- **Publication:** 2025-10-09
- **Tier:** 2
- **Data extracted:** Target — Amazon Bedrock Agents with Nova Premier v1, memory enabled, Bedrock Guardrails DISABLED for PoC. Attack chain — exploits session summarization. XML payload uses forged `<conversation>` tags fragmenting payload into three parts; part two outside conversation blocks is interpreted as system instructions. Cross-session persistence: "Bedrock Agents automatically inject memory contents into every new session's context." Demonstrated exfiltration in subsequent booking interaction days later. Explicitly framed as PoC in "minimally protected configuration" — NOT production incident.
- **Critical caveat:** The "LLM-based detectors miss 66% of poisoned entries" figure attributed to Unit 42 by the operator-playbook discovery agent is NOT in this article. **Flagged as discovery agent error — do not cite.**

### [20] Johann Rehberger — SpAIware (ChatGPT macOS persistent data exfiltration)
- **URL:** https://embracethered.com/blog/posts/2024/chatgpt-macos-app-persistent-data-exfiltration/
- **Author:** Johann Rehberger
- **Publication:** 2024-09-20
- **Tier:** 3
- **Data extracted:** Vector — "websites or untrusted documents" containing prompt injection invoking ChatGPT memory tool, payload exfiltrates via image render to attacker-controlled server. Persistence: "all information the user typed or responses received by ChatGPT, including any future chat sessions." OpenAI patched in version 1.2024.247 (Sept 2024). Disclosure timeline: April 2023 → December 2023 partial url_safe fix → June 2024 full exploit reported → September 2024 patch.
- **Caveats:** Authorized researcher demonstration via responsible disclosure (BSides Vancouver Island 2024). Discovery agent referenced "Google Drive document" specifically — actual blog says "websites or untrusted documents" generally.

### [21] Johann Rehberger — Gemini memory persistence via delayed tool invocation
- **URL:** https://embracethered.com/blog/posts/2025/gemini-memory-persistence-prompt-injection/
- **Author:** Johann Rehberger
- **Publication:** 2025-02-10
- **Tier:** 3
- **Data extracted:** Document upload → poisoned summary asks user response question → trigger words "yes/sure/no" → Gemini saves false memories. Google's response (verbatim): "an abuse-related risk with low likelihood and low impact."
- **Caveats:** Authorized researcher disclosure. The "UI alert on memory writes was Google's defensive rationale" claim from discovery agents is NOT in the article — only the low-likelihood/low-impact assessment is.

### [22] The Register — AI vendors' response to security flaws: it wasn't me
- **URL:** https://www.theregister.com/2026/04/19/ai_vendors_response_to_security/
- **Author:** Jessica Lyons
- **Publication:** 2026-04-19
- **Tier:** 2
- **Data extracted:** GitHub Actions hijacking of three AI agents — Anthropic Claude Code Security Review ($100 bounty), Google Gemini CLI Action ($1,337), Microsoft GitHub Copilot ($500). None assigned CVEs or public advisories. Anthropic MCP design flaw "puts as many as 200,000 servers at risk." Anthropic response: "This is an explicit part of how MCP stdio servers work and we believe this design does" (the article quotes this in context of NOT representing secure defaults). "10 (so far) high- and critical-severity CVEs issued for individual open source tools and AI agents that use MCP."
- **Caveats:** Counter-defenses agent's claim "Anthropic 200-attempt vs OpenAI single-attempt" testing inconsistency is NOT in this article — **flagged as discovery error**.

### [23] Auth0 — Lessons from OWASP Top 10 for Agentic Applications
- **URL:** https://auth0.com/blog/owasp-top-10-agentic-applications-lessons/
- **Publication:** 2026-02-20
- **Tier:** 3 (vendor blog — Auth0 sells identity products)
- **Data extracted:** ASI06 definition (verbatim quote of OWASP): "Bad data is 'planted' in the agent's memory, causing it to make biased or unsafe decisions later on." Full ASI list: ASI01 Agent Goal Hijack, ASI02 Tool Misuse, ASI03 Identity & Privilege Abuse, ASI04 Agentic Supply Chain Vulnerabilities, ASI05 Unexpected Code Execution, ASI06 Memory & Context Poisoning, ASI07 Insecure Inter-Agent Communication, ASI08 Cascading Failures, ASI09 Human-Agent Trust Exploitation, ASI10 Rogue Agents. Mitigations: fine-grained authorization for RAG, memory segmentation, centralized revocation.
- **Caveats:** Vendor-aligned mitigations.

---

## Counter-perspective sources

### [24] Hindsight (Vectorize) — Your agent is not forgetful
- **URL:** https://hindsight.vectorize.io/blog/2026/04/23/your-agent-is-not-forgetful
- **Publication:** 2026-04-23
- **Tier:** 3
- **Data extracted (verbatim):** "Most agents were never designed to remember in the first place. Each session starts over."
- **Caveats:** No quantitative data on stateless vs stateful deployment ratios — qualitative claim only. The strongest available "architectural conditionality" counter-argument to the persistence claim.

### [25] Simon Willison — The lethal trifecta
- **URL:** https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- **Author:** Simon Willison
- **Publication:** 2025-06-16
- **Tier:** 3 (well-known practitioner)
- **Data extracted (verbatim):** Three conditions — (1) "Access to your private data", (2) "Exposure to untrusted content", (3) "The ability to externally communicate." Removing any one breaks the chain. Vulnerable systems cited: Microsoft 365 Copilot, GitHub MCP server, GitLab Duo Chatbot, ChatGPT, Google Bard, Amazon Q, GitHub Copilot Chat. Caveat (verbatim): "guardrails won't protect you."

### [26] David Richards — The RAG Freshness Paradox
- **URL:** https://ragaboutit.com/the-rag-freshness-paradox-why-your-enterprise-agents-are-making-decisions-on-yesterdays-data/
- **Author:** David Richards
- **Publication:** 2025-12-30
- **Tier:** 3
- **Data extracted (verbatim):** "$340,000 annually in infrastructure costs - before factoring in engineering time" for overlapping refresh layers on a "moderately-sized RAG agent system." 45-minute reindex cycle makes hourly rotation perpetually incomplete. "~$0.001 per query for re-ranking."
- **Caveats:** Single-enterprise anecdote, not independently audited.

### [27] Blake Crosley (Introl) — Embedding Infrastructure at Scale
- **URL:** https://introl.com/blog/embedding-infrastructure-scale-vector-generation-production-guide-2025
- **Publication:** 2026-02-24
- **Tier:** 3
- **Data extracted (verbatim):** "A single NVIDIA L4 GPU processes approximately 2,000 text tokens per second through a 7-billion parameter embedding model." "The falcon-refinedweb dataset with 600 billion tokens would take more than 9.5 years" on a single machine. OpenAI small embedding API: "$2,000/month" for 100M tokens. Spot instance savings: "61% (from $710 to $277 in one case study)."
- **Caveats:** Vendor blog (Introl provides AI infrastructure services).

---

## Inaccessible / unverified sources

These were referenced by discovery agents and are needed for complete coverage but could not be fetched in this session. Listed for transparency.

### [28] IBM Think Insights — Morris II self-replicating malware
- **URL:** https://www.ibm.com/think/insights/morris-ii-self-replicating-malware-genai-email-assistants
- **Status:** **INACCESSIBLE** (HTTP 403)
- **Why it matters:** Per discovery agent search snippet (UNVERIFIED): "The 'Morris II' AI worm has not been seen in the wild, and the researchers did not test it on a publicly available email assistant." This is the foundational source for the lab-vs-wild distinction.
- **Action:** Phase 4 verification will retry. If still inaccessible, the claim must be sourced elsewhere or downgraded to "per discovery snippet, unverified."

### [29] VentureBeat — 12 AI defenses claimed near-zero attack success, researchers broke all of them
- **URL:** https://venturebeat.com/security/12-ai-defenses-claimed-near-zero-attack-success-researchers-broke-all-of-them
- **Status:** **INACCESSIBLE** (HTTP 429)
- **Why it matters:** Journalistic coverage of citation [6] with vendor credibility framing.

### [30] Microsoft AI Red Team — Taxonomy of Failure Modes in Agentic AI Systems (whitepaper PDF)
- **URL:** https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Taxonomy-of-Failure-Mode-in-Agentic-AI-Systems-Whitepaper.pdf
- **Status:** **INACCESSIBLE** (binary PDF content not extractable)
- **Why it matters:** Source of the disputed "memory poisoning under Existing Security Failures" framing reported by counter-threat-taxonomy agent. The companion blog [16] frames it differently as "novel failure mode."
- **Action:** Phase 4 verification will retry with PDF-aware fetching.

---

## Additional sources referenced by discovery agents (not directly extracted)

The following were identified by discovery agents with verifiable URLs but were not individually fetched in this session due to volume. Listed for citation completeness — substantive claims using these sources are tagged with "(per discovery agent, unfetched)" in reference files.

### [31] PoisonArena — Uncovering Competing Poisoning Attacks
- **URL:** https://poison-arena.github.io/
- **Tier:** 1 (academic project page)
- **Data per discovery agent:** Attack success collapses to ~0% for most methods under multi-attacker competition. GASLITE is exception, maintaining >80% ASR.

### [32] Benchmarking Poisoning Attacks against RAG (Zhang et al., 2025)
- **URL:** https://arxiv.org/abs/2505.18543
- **Tier:** 1
- **Data per discovery agent:** ASR drops from 80-97% to 0-33% on expanded knowledge bases. PaLM 2 deprecation broke prior reproducibility for several baselines.

### [33] Through the Stealth Lens — Attention-Aware Defenses Against Poisoning in RAG
- **URL:** https://openreview.net/forum?id=PS43wqCSME (also https://arxiv.org/abs/2506.04390 per discovery)
- **Tier:** 2 (OpenReview)
- **Data per discovery agent:** Attention-Variance Filter detects high-ASR attacks at 83% accuracy. Adaptive attacks that minimize signal achieve only ~35% ASR and require orders-of-magnitude more compute.

### [34] RAGDefender — Rescuing the Unpoisoned
- **URL:** https://arxiv.org/abs/2511.01268
- **Tier:** 1
- **Data per discovery agent:** Reduces PoisonedRAG ASR from 0.84 to 0.03 using clustering detection.

### [35] CorruptRAG (Wei et al., 2025)
- **URL:** https://arxiv.org/abs/2504.03957
- **Tier:** 1
- **Data per discovery agent:** Critiques multi-document injection assumptions in prior attacks; single-document attack is more realistic.

### [36] Bypassing LLM Guardrails (Hackett et al., 2025)
- **URL:** https://arxiv.org/abs/2504.11168
- **Tier:** 1
- **Data per discovery agent:** Microsoft Azure Prompt Shield and Meta Prompt Guard achieve up to 100% evasion under character injection and AML evasion.

### [37] AgentPoison NeurIPS 2024 proceedings
- **URL:** https://proceedings.neurips.cc/paper_files/paper/2024/file/eb113910e9c3f6242541c1652e30dfd6-Paper-Conference.pdf
- **Tier:** 1
- **Note:** Camera-ready PDF version of [1].

### [38] MINJA — A Practical Memory Injection Attack against LLM Agents
- **URL:** https://arxiv.org/abs/2503.03704
- **Tier:** 1
- **Data per discovery agent:** ISR >95%, ASR 90% on eICU and 98.9% on Webshop with GPT-4o. Benign degradation <2%.

### [39] Schneier on Security — LLM prompt injection worm
- **URL:** https://www.schneier.com/blog/archives/2024/03/llm-prompt-injection-worm.html
- **Tier:** 3 (well-known security practitioner)
- **Data per discovery agent:** Expert commentary on Morris II.

### [40] Springer 2012 survey on shilling attacks (recommender systems history)
- **URL:** https://link.springer.com/article/10.1007/s10462-012-9364-9
- **Tier:** 1
- **Data per discovery agent:** Shilling attacks documented since at least 2004 (Lam & Riedl, Burke 2005, Chirita 2005). Establishes "AI Recommendation Poisoning" is a rebrand of known attack class.

### [41] SecureIQLab — Independent AI Firewall Vendor Validation announcement
- **URL:** https://www.prnewswire.com/news-releases/up-to-20-ai-firewall-vendors-face-first-independent-security-validation-302724473.html
- **Source:** PR Newswire (per defenses discovery agent, not directly fetched)
- **Tier:** 2
- **Data per discovery agent:** First non-commissioned vendor test of up to 20 AI firewall vendors. Testing window April 2026 - July 2026. Results expected at Black Hat USA 2026 (~August 2026). Includes Retrieval Firewall scenarios 22-24.
- **Caveats:** Source not directly fetched in this session. PR Newswire press release is a vendor-marketing channel — substantive testing methodology requires the SecureIQLab primary publication when results are released.
