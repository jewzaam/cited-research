# AgentPoison and similar attacks — methodology, claims, and what the headline numbers actually mean

This file covers the family of RAG/memory-poisoning attacks: AgentPoison, MemoryGraft, MINJA, PoisonedRAG, and their reproducibility under realistic conditions.

See [citations.md](../citations.md) for source details.

## AgentPoison: the metric the headline obscures

AgentPoison [1] is the most-cited memory-poisoning attack. Its headline claim — **">80% attack success rate at <0.1% poison rate, no model retraining required"** — appears in dozens of secondary sources without qualification.

Two qualifications matter.

### 1. The headline ASR is retrieval, not end-to-end

The paper defines three distinct metrics:

| Metric | Definition (per [1] HTML body) |
|---|---|
| **ASR-r** | "Percentage of test instances where all retrieved demonstrations are from the poisoned set." |
| **ASR-a** | "Percentage of test instances where the agent generates the target action conditioned on successful retrieval of poisoned instances." |
| **ASR-t** | "Percentage of test instances where the agent achieves the final adversarial impact on the environment that depends on the entire agent system." |

The **>80%** figure refers to **ASR-r** (retrieval). End-to-end success (ASR-t) averages around 58% across the three tested agents [1]:

| Agent              | ASR-r | ASR-t | ACC   | Corpus  | Poisoned |
|--------------------|-------|-------|-------|---------|----------|
| Agent-Driver       | 80.0% | 56.8% | 91.1% | 23,000  | 20       |
| ReAct-StrategyQA   | 65.5% | 58.6% | 65.7% | 10,000  | 4        |
| EHRAgent           | 98.9% | 58.3% | 72.9% |    700  | 2        |

The end-to-end attack succeeds in roughly 6 in 10 attempts, not 8 in 10.

### 2. The "<0.1%" claim does not hold for EHRAgent

Computing the ratios: Agent-Driver 20/23,000 = 0.087%; ReAct-StrategyQA 4/10,000 = 0.040%; **EHRAgent 2/700 = 0.286%**, which exceeds the "<0.1%" claim by nearly 3x. The abstract figure is an average that obscures the fact that one of three tested agents required a higher poison ratio.

### 3. The threat model requires white-box embedder access

Verbatim from [1]: "we allow the attacker to have white-box access to the RAG embedder of the victim agent for trigger optimization." Most production deployments use closed API embedders (OpenAI, Cohere, Vertex). The paper claims transferability to black-box embedders empirically but does not validate this against the OpenAI/Cohere production APIs at scale.

## Other RAG poisoning attacks

| Attack | Headline ASR | Realistic poison rate | Attacker access | Independent reproduction? |
|---|---|---|---|---|
| AgentPoison [1] | 80% (ASR-r) / 58% (ASR-t) | 0.087-0.286% (varies) | White-box embedder + KB write | None published |
| PoisonedRAG [5] | 90% with 5 docs | "Few" docs in millions-doc corpus | Black-box or white-box, KB write | USENIX Security 2025 (peer review) |
| MINJA [38, per discovery] | ISR >95%, ASR 90% (eICU) / 98.9% (Webshop) on GPT-4o | Query-only interactions | No KB write needed | None published |
| MemoryGraft [7] | PRP 47.9% at 9% poison | 9% (much higher than AgentPoison) | KB write (README files) | None published |
| BadRAG [per discovery, unfetched] | 98.2% retrieval with 10 passages | 0.04% | KB write | None published |
| ConfusedPilot [per discovery, unfetched] | No published quantitative ASR | Any user with SharePoint write access | KB write | DEF CON presentation only |

## Realistic-condition findings: ASR collapses

The strongest empirical pushback on AgentPoison's headline numbers is **arXiv 2601.05504** [4]:

> ASR fell from **62%** (empty memory) to **6.67%** (with legitimate memories) for GPT-4o-mini.
> Llama-3.1-8B-Instruct dropped from successful injection (99.95% ISR) to **0%** ASR with relevant initial memories.

In a realistic deployment with populated memory and competing legitimate retrievals, the attack effectiveness drops by roughly an order of magnitude.

The Zhang et al. benchmarking paper [32, per discovery, unfetched] reports the same direction at the corpus level: ASR drops from 80-97% on sparse benchmark corpora to 0-33% on expanded knowledge bases with semantically relevant correct-answer texts.

PoisonArena [31, per discovery, unfetched] further shows ASR collapses to ~0% under multi-attacker competition for most methods (GASLITE excepted).

## Reproduction status

No independent third-party reproduction of AgentPoison's ASR table was identified in this session's searches. The official code repo is published (https://github.com/AI-secure/AgentPoison). PoisonedRAG was peer-reviewed at USENIX Security 2025 [5] but the search did not surface a head-to-head replication.

The detection paper "Through the Stealth Lens" [33, per discovery, unfetched] reports that high-ASR attacks like PoisonedRAG produce detectable attention-pattern anomalies (83% detection accuracy via Attention-Variance Filter), and adaptive attacks that minimize this signal achieve only ~35% ASR with orders-of-magnitude more compute.

## Gaps and limitations

- The full PoisonedRAG paper PDF was not extracted; the per-dataset ASR breakdown (NQ 97%, HotpotQA 99%, MS-MARCO 91%) reported by discovery agents could not be verified.
- BadRAG, ConfusedPilot, MINJA, and CorruptRAG papers were not directly fetched; their claims are tagged as "per discovery agent, unfetched."
- No paper directly tests AgentPoison's threat model against a production OpenAI/Cohere embedder API in a realistic enterprise corpus. The white-box assumption survives transfer claims but has not been validated at scale.
