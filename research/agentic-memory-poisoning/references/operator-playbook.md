# Operator playbook — detection, rotation, and the cost reality

This file covers the practical SRE/security-ops view: how would an operator detect a poisoned vector store, what rotation strategy makes sense, and what the cost-of-defense looks like compared to the cost-of-attack.

See [citations.md](../citations.md) for source details.

## Detection: what signals exist?

### Indicators of compromise (IoCs) that have been observed in production

Microsoft Defender [15] documents the only confirmed in-the-wild IoC pattern: URL parameters (`?q=`, `?prompt=`) embedding keywords `remember`, `memory`, `trusted`, `authoritative`, `future`, `citation`, `cite`. These appear in `Summarize with AI` button URLs in email traffic. The specific pattern is detectable at the network-layer (email gateway, proxy logs), not at the model output layer.

This is the **only** IoC pattern with documented in-the-wild observations as of April 2026.

### Detection mechanisms proposed in research

| Mechanism | Source | Reported effectiveness | Caveats |
|---|---|---|---|
| LLM activation analysis (RevPRAG) | per discovery agent operator-playbook (arXiv 2411.18948), unfetched | 98% TPR / ~1% FPR | Requires white-box LLM access — incompatible with hosted/API deployments |
| Behavioral drift / response anomaly | OWASP Agentic Top 10 [12]; BeyondScale (per discovery, unfetched) | Qualitative | No quantitative baseline |
| Canary document monitoring | DevSecOps Now (per discovery, unfetched) | Qualitative | No published methodology for canary design or refresh rate |
| Trusted-model audit scan | BeyondScale, NeuralTrust (per discovery, unfetched) | Qualitative | Recursive trust problem (which model audits the auditor?) |
| RAG-Defender clustering | [34] (per discovery, unfetched) | Reduces PoisonedRAG ASR 0.84 → 0.03 | Self-evaluated |
| Composite trust scoring | [4] | No usable operating point — see below | Calibration failure |
| Bayesian trust scoring | [9] | 72% trust degradation for sleepers | Single-author, self-evaluated |

The composite trust scoring approach in [4] illustrates the calibration problem operators actually face: GPT-4o-mini set conservatively rejected all 23 candidate entries (zero utility); Gemini-2.0-Flash accepted 54 confirmed malicious entries with trust score 1.0. **No usable operating point** — the defense produces either zero utility or 50%+ false-negative rate.

### Discovery-agent-claimed figure flagged as error

The operator-playbook discovery agent reported "LLM-based detectors miss 66% of poisoned entries" attributed to Unit 42 [19]. This figure is **NOT in the Unit 42 article** [19]. It should not be cited.

## Rotation strategy

### What the practitioner literature recommends (per discovery agents, unfetched primaries)

- **Re-evaluation cadence:** every 6 months against current top-3 embedding models. Trigger re-embedding if a new model exceeds current corpus performance by more than 5% on domain-specific benchmarks (Prem AI 2026, per discovery, unfetched).
- **MTEB leaderboard shift rate:** meaningful changes every 3-4 months with 3-5% retrieval improvements (Prem AI, per discovery).
- **Quarterly full index rebuild from verified snapshots** plus key rotation as security hygiene floor (DevSecOps Now SRE runbook fragments, per discovery).
- **Security-driven rotation** differs from quality-driven: after confirmed poisoning, rebuild from last known-good snapshot regardless of cadence window.

### What the cost reality says

The "rotation strategy" recommendations conflict with the operational economics of production-scale embedding.

**RAG Freshness Paradox (Richards 2025-12-30) [26]:**
- "$340,000 annually in infrastructure costs - before factoring in engineering time" for one enterprise's overlapping refresh layers on a "moderately-sized RAG agent system."
- "If your vector database update takes 45 minutes to complete... moving from daily to hourly updates means your database is perpetually in transition."

**Introl Embedding Infrastructure (Crosley 2026-02-24) [27]:**
- "A single NVIDIA L4 GPU processes approximately 2,000 text tokens per second through a 7-billion parameter embedding model."
- "The falcon-refinedweb dataset with 600 billion tokens would take more than 9.5 years" on a single machine.
- API cost: "$2,000/month" for 100M tokens via OpenAI's small embedding model.
- "A production RAG system processing 10 million documents with 100,000 daily queries might cost $50-100 per day in embedding operations alone — $1,500-3,000 monthly."

The implication: full corpus re-embedding at the cadence security best-practice recommends (quarterly or after every confirmed incident) is **financially and temporally infeasible** for many production deployments. Operators face a real trade-off, not a rhetorical one.

## Corpus provenance — the unsolved problem

RAGShield [8] proposes provenance verification as a defense layer. The single-author paper claims 0.0% ASR (CI 0-1%) over 430 attacks but provides no latency/throughput overhead numbers and has no independent replication.

The Longpre et al. provenance work (per discovery counter-defenses, unfetched) is the structural argument against provenance as a general solution: web-scraped data is "widely sourced and bundled without tracking original sources, creator intentions, or licensing status." Watermarking is "vulnerable to removal." There is no signing infrastructure that functions on arbitrary crawl data.

**At ingestion-time:** Trust classification tiers (public / internal / confidential / restricted / regulated) attached as metadata, used for retrieval-time RBAC+ABAC enforcement (per discovery operator-playbook, unfetched). This is the most practical recommendation but applies only to controlled enterprise corpora, not to web-scraped data.

## Cost asymmetry

The defender-attacker cost asymmetry is concrete:

- **Attack cost (PoisonedRAG [5]):** Five malicious documents achieve 90% ASR against millions of clean entries. Marginal cost is the cost of generating five documents — effectively zero.
- **Defense cost:** $340K/year per enterprise (Richards [26]); 9.5 years of GPU time per corpus refresh (Crosley [27]); $1,500-3,000/month for embedding operations on 10M docs.

The USENIX economics analysis (per discovery counter-operator-playbook, unfetched): "Growing inference costs at the frontier may benefit well-resourced attackers who can selectively target high-value assets, while defenders struggle to protect their entire attack surface."

## What an operator can actually do today

Synthesizing the verified evidence:

1. **Network-layer IoC monitoring** for the Microsoft URL patterns [15] — the only IoC with confirmed wild observations.
2. **Memory segmentation** per session/per domain [23] — limits blast radius without requiring detection.
3. **Disable persistent memory features for users who do not need them** — per Hindsight [24], most agents are stateless by design and the persistence vulnerability does not apply.
4. **Identity-bound retrieval (RBAC+ABAC)** [23] — limits which corpus entries any given query can retrieve.
5. **Accept a longer-than-textbook re-embedding cadence** — given the cost data [26, 27], quarterly full rebuild may be the only economically viable option for most deployments.
6. **Treat detection as best-effort, not catch-all** — given the calibration failure documented in [4] and the adaptive-attack collapse in [6], detection alone is not sufficient.

The honest summary: there is no operator playbook today that combines acceptable utility, acceptable false-negative rate, and economically sustainable cost.

## Gaps and limitations

- No source provides a concrete cost-per-document re-embedding benchmark for major cloud providers.
- RevPRAG's 98% TPR requires white-box LLM access — production deployability for hosted/API-only models is unclear.
- The operator-playbook discovery agent reported the "66% LLM-detector miss" figure incorrectly attributed to Unit 42 [19] — confirmed to NOT be in the source.
- IronCore Cloaked AI key rotation cadence guidance was not surfaced.
- Canary document methodology (selection criteria, refresh rate, alert thresholds) is absent from all sources found.
