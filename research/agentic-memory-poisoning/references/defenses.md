# Defenses — what the literature claims, what is independently validated, and where vendor self-report dominates

This file evaluates the defenses proposed against memory poisoning, separating claims with independent validation from those resting on vendor self-report or single-author preprints.

See [citations.md](../citations.md) for source details.

## The headline finding: defenses break under adaptive attack

The single most important defense paper is **"The Attacker Moves Second"** [6] (arXiv 2510.09023, October 2025, 14 authors).

Verbatim from abstract: **"12 recent defenses (based on a diverse set of techniques)"** were tested. **Original defense claims:** "the majority of defenses originally reported near-zero attack success rates." **Under adaptive attacks:** "attack success rate above 90% for most." Adaptive methods used: "gradient descent, reinforcement learning, random search, and human-guided exploration." Both jailbreak AND prompt injection defenses were tested.

This finding directly applies to memory poisoning defenses, which are evaluated under the same lab conditions as the prompt-injection defenses tested in [6].

## Defense families and their evidence

### 1. Input/output moderation with composite trust scoring

Proposed in arXiv 2601.05504 [4]. Combines "static heuristics, keyword matching, and LLM-based semantic classification" with multi-signal trust scoring.

**Calibration challenge — the central failure:** The paper itself reports no usable operating point [4]:
- GPT-4o-mini set conservatively rejected all 23 candidate entries (zero utility — agent unusable)
- Gemini-2.0-Flash accepted 54 confirmed malicious entries with trust score 1.0 (defense bypassed)

Authors' framing: "the defense layer operated essentially as a 'confidence filter' rather than a 'security filter.'"

This is empirical evidence that input/output moderation as currently formulated does not produce both acceptable utility AND acceptable false-negative rate.

### 2. Memory sanitization with temporal decay filtering

Also proposed in [4]. Trust scores at append time, then exponential decay during retrieval, plus pattern-based filtering.

No independent evaluation against adaptive attacks. The temporal decay component creates **recency bias**: fresh injections outweigh established legitimate context, which Schneider [17] flags as exploitable.

No paper measures how much temporal-decay defense degrades legitimate long-horizon use cases (operators retrieving institutional knowledge from months ago).

### 3. Vector-store provenance signing / cryptographic integrity

**RAGShield** [8] (arXiv 2604.00387) claims: "RAGShield detects every one (0.0% ASR, 95% CI [0%, 1%])" across 430 attacks. Embedding-based defenses "miss 79-90% of the same attacks."

**Caveat:** Single-author paper, no institutional affiliation visible. The "five-layer architecture / NIST SP 800-53 mapping / C2PA-inspired attestation / T1-T5 adaptive adversary tier" framing reported by the discovery agent is **not in the abstract**. The actual abstract describes a narrower system (pattern engine for dollar amounts/percentages, two-pass propagation, cross-source registry, temporal tracker). No latency/throughput overhead numbers in abstract. No independent replication.

**Provenance signing at web scale fails:** Longpre et al. (ICML 2024 spotlight, per discovery agent counter-defenses, unfetched) document that content-authenticity techniques have "limited scope," watermarking is "vulnerable to removal," and the Data Provenance Initiative's expert-human-review approach "limits scale." There is no signing infrastructure that functions on arbitrary web-crawl data.

### 4. ML-based anomaly detection (OWASP Agent Memory Guard Q3 2026)

The OWASP Agent Memory Guard project [14] roadmap places ML-based anomaly detection at **v0.4.0, planned for Q3 2026**. **It does not yet exist in released code.** Any defense effectiveness claim attributed to OWASP Agent Memory Guard's ML detection is premature as of April 2026.

The current released implementation (v0.0.0, Incubator) provides SHA-256 cryptographic baselines, declarative YAML policies on read/write operations, and snapshot/rollback. Effectiveness numbers are not published.

### 5. Bayesian trust scoring (SuperLocalMemory)

SuperLocalMemory [9] reports trust separation gap = 0.90, "72% trust degradation for sleeper attacks," 10.6ms median search latency, 104% improvement in NDCG@5. Open-source MIT-licensed with 17+ MCP integrations.

**Caveat:** Single-author, no institutional affiliation. Mention of superlocalmemory.com domain suggests possible product offering. Self-evaluated.

### 6. Production guardrails (Microsoft Azure Prompt Shield, Meta Prompt Guard)

Per the Bypassing LLM Guardrails paper [36, per discovery, unfetched]: production guardrails achieve **up to 100% evasion** under character injection (Unicode zero-width, homoglyphs) and AML evasion. Production-deployed defenses do not provide meaningful protection against an adversarial attacker who knows the defense exists.

## The vendor-self-report pattern

Every effectiveness number in the table below is self-reported by authors or vendors. As of April 2026, no independent industry validation has published results.

| Defense | Reported effectiveness | Source | Independent validation? |
|---|---|---|---|
| RAGShield [8] | 0.0% ASR (CI 0-1%) on 430 attacks | Self (single author) | No |
| RAGDefender [34] | PoisonedRAG ASR 0.84 → 0.03 | Self (per discovery) | No |
| RobustRAG | 0-0.5% in one eval, 54-84% in another | Conflicting evaluations | No |
| Lakera Guard [18 vendor] | "98% detection, sub-50ms, <0.5% FP" | Vendor PR (NOT in source [18]) | No |
| ADO Sentinel-Strategist | Near-zero ASR | Self (per discovery) | No |
| SuperLocalMemory [9] | 72% trust degradation for sleepers | Self (single author) | No |
| Attention-Variance Filter [33] | 83% accuracy | Self (per discovery) | No |
| Microsoft Azure Prompt Shield | (broken at up to 100% evasion) | Independent academic [36] (per discovery, unfetched) | YES — broken (per discovery, unfetched) |

**The SecureIQLab independent validation** [41] announced April 2026 begins testing up to 20 AI firewall vendors that month, with results targeted for Black Hat USA 2026 (~August 2026). As of this research date (2026-04-30), **no independent validation results exist for any commercial defense product** [41].

## The Register reporting on vendor accountability

Jessica Lyons [22] documents three GitHub Actions AI agent hijacks affecting Anthropic Claude Code Security Review ($100 bounty), Google Gemini CLI Action ($1,337), Microsoft GitHub Copilot ($500). **None issued CVEs or public advisories.** Anthropic's MCP design flaw "puts as many as 200,000 servers at risk"; Anthropic's response was that the behavior is "an explicit part of how MCP stdio servers work" and not a vulnerability. Yet "10 (so far) high- and critical-severity CVEs issued for individual open source tools and AI agents that use MCP."

The pattern: vendors selling agentic AI security products publish defense claims with no independent validation, while disputing or downplaying disclosed vulnerabilities in their own products.

**Correction:** The counter-defenses discovery agent claimed The Register documented an Anthropic-vs-OpenAI testing-standards comparison ("200-attempt adaptive vs single-attempt resistance"). This claim is **not in the article** — flagged as discovery error.

## Honest gaps

- No defense paper has been independently replicated as of April 2026.
- No defense has been evaluated against a fully adaptive attacker who knows the defense mechanism in advance (RAGShield claims this via T5 tier per discovery agent, but the abstract does not confirm this).
- ML-based anomaly detection effectiveness for vector stores specifically has no peer-reviewed quantitative baseline.
- The temporal-decay defense breaks legitimate long-horizon use cases by some unmeasured amount.
- Provenance signing has no working infrastructure for arbitrary web-crawl data at scale.
- Vendor product claims (Lakera Guard's "98% detection") cannot be traced to a primary published source in the cited blog [18].
- Cost data for defenses (RAGShield latency, anomaly detection compute, provenance signing throughput) is absent from every defense paper found.
