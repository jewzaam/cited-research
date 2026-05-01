# Intersection with agentic-research-bias — drift, poisoning, and the boundary problem

This file covers the question topics5.md poses: at what point does benign distributional drift in a research agent's corpus become indistinguishable from adversarial poisoning?

See [citations.md](../citations.md) for source details.

## The technical answer: standard drift detectors cannot tell the difference

The foundational source is **Korycki and Krawczyk (2022)** [11] in the Springer journal Machine Learning. Their central technical claim (verbatim): existing methods "all assume that the drift is connected with underlying changes in the source of data" without considering "a malicious injection of false data that simulates a concept drift."

They identify two attack modalities:
- **Instance-based poisoning:** individual corrupted instances scattered through the stream that degrade adaptation speed or cause overfitting.
- **Concept-based poisoning:** structured, coherent adversarial distributions forming false concepts that either trigger spurious drift signals or completely mask legitimate changes — the more dangerous category.

Their proposed RRBM-DD detector (Robust Restricted Boltzmann Machine Drift Detector) achieves average RLR scores of **0.85 (instance-based)** and **0.78 (concept-based)** vs competitors averaging **0.55-0.62**. Even the best detector reduces but does not eliminate the blindspot.

**Key implication:** The fields of drift detection and poisoning detection are technically incompatible — different statistical tests, different threat models, different response actions. A drift detector tuned to fire on adversarial poisoning will also fire on benign distribution shift. A poisoning detector tuned for adversarial intent will miss organic drift. The two are complementary in the sense that you need both independently, not that one informs the other.

## Microsoft "AI Recommendation Poisoning" — bias or attack?

Microsoft's February 2026 finding [15] sits exactly on this boundary. The observed behavior: 50 distinct prompts from 31 companies attempting to manipulate AI assistant memory features for promotional purposes. The intent is **commercial bias injection** — not data theft, not system compromise, but skewing recommendations.

Two competing framings:

**Framing as "AI security":** Microsoft labels this "Memory Poisoning" and assigns it to the agentic security threat class. Detection is at the network layer (URL parameters, source [15]).

**Framing as "rebrand of shilling attacks":** Per the counter-bias-intersection discovery agent (sources unfetched), shilling attacks against recommender systems have been documented since at least 2004 (Lam & Riedl WWW 2004; Burke ICDM 2005; Chirita 2005; Springer 2012 survey [40]). Profile injection to promote items is structurally identical. The novelty is the delivery mechanism (URL parameter into AI assistants with persistent memory), not the threat class itself.

Both framings are defensible. The choice has consequences:
- AI-security framing → SOC tooling, CVE disclosure, threat-intel sharing.
- Recommender-manipulation framing → trust & safety teams, content policy, marketplace enforcement.

Microsoft itself implicitly acknowledges the SEO-poisoning parallel.

## Fair ML and adversarial robustness are in tension

Per discovery counter-bias-intersection (sources unfetched, but the structural argument is widely known):
- arXiv 2006.08669 shows fairness constraints and adversarial robustness are NOT complementary by design — robustifying a fair model can destroy fairness.
- arXiv 2511.08331 (Chan et al. 2025): naive bias mitigation does not protect against poisoning targeting fairness.

This means the operational suggestion "use bias-mitigation tools for poisoning detection (and vice versa)" is wrong. They optimize for different objectives that can actively conflict.

## What's actually shared between the two domains

The Korycki paper [11] is the strongest published bridge: both bias-mitigation and poisoning-defense need *some* mechanism to detect distributional change. But:
- Bias mitigation cares about *direction* of drift (toward minority underrepresentation, etc.)
- Poisoning defense cares about *intent* of drift (adversarial vs organic)

A single detector cannot infer both from the symptom alone. Both fields can use distributional-change detection as input, but they then route to different response logic.

## The agentic-research-bias intersection (per topics5.md)

The specific question topics5.md asks is: a research agent's corpus accumulates bias from the documents it ingests. At what point does the bias become indistinguishable from poisoning?

Per the agentic-research-bias work (already in this repo, see `research/agentic-research-bias/`), benign distributional drift in research-agent corpora produces measurable shifts in conclusion patterns. **There is no published method that distinguishes "bias acquired through normal corpus accumulation" from "bias acquired through adversarial document injection"** at the symptom level.

The pragmatic operator answer: **provenance is the only signal that distinguishes them.** Documents from controlled sources (peer review, organizational policy, audited ingest pipelines) get treated as "drift candidates." Documents from open web ingest get treated as "poisoning candidates." This is closer to a classification of risk class than to detection of attack, and it shifts the problem from algorithmic detection to ingestion-pipeline governance.

## Gaps and limitations

- No published study tests bias-mitigation tooling for poisoning-detection effectiveness (or vice versa).
- The Microsoft AI Recommendation Poisoning case [15] is the only empirical data point sitting on the bias/attack boundary; its narrow scope (commercial promotion) limits generalizability to research-agent contexts.
- Korycki & Krawczyk [11] is from 2022, predating the agentic AI wave. The same fundamental detection-incompatibility problem applies but has not been studied specifically in vector-store / RAG settings.
- The Microsoft Recommendation Poisoning blog [15] frames the technique as new; counter-perspective sources frame it as a rebrand of 2004-era shilling attacks. Neither side has formally engaged the other in the published literature.
- The discovery-agent claims about CSA MAESTRO framework's "Bias in Security AI Agents" category (per bias-intersection discovery, unfetched) could not be independently verified.
