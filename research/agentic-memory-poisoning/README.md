# Memory Poisoning of Agentic AI

*Citation-backed research. Last revised 2026-04-30.*

## What this document answers

Memory poisoning of agentic AI — the OWASP ASI06 framing, the AgentPoison/Morris-II/eTAMP attack family, the vendor and academic defenses, and the gap between lab demonstrations and confirmed production incidents. Published lab attack-success rates (>80%, 32.5%, 8x amplification) are technically correct under their lab conditions and systematically misleading as production threat indicators. As of April 2026, **zero publicly confirmed memory-poisoning incidents in production agent systems with disclosed harm** have been documented; what exists is demonstrated mechanism plus 50 documented attempts observed by Microsoft over 60 days [15].

Full analysis: [analysis.md](analysis.md). All sources: [citations.md](citations.md). Per-dimension detail: [references/](references/). Verification logs: [audit/](audit/).

## The headline table — what the lab numbers actually mean

| Claim (as commonly cited) | Source | Caveat after verification |
|---|---|---|
| AgentPoison achieves >80% ASR at <0.1% poison rate | [1] | The 80% is **ASR-r (retrieval)**, not end-to-end. End-to-end ASR-t averages **~58%**. EHRAgent poison rate is 0.286%, exceeding the <0.1% claim. Requires **white-box embedder access** for trigger optimization. |
| eTAMP demonstrates 19.5%/32.5% ASR with 8x amplification | [3] | The ASR numbers are correct. Actual amplification on GPT-5-mini is **4.6%→32.5% = ~7x**, not 8x — the "8x" in topics5.md and most secondary coverage is a rounded approximation. Frustration condition is **simulated lab perturbation**, not measured production friction. (Visual)WebArena lab benchmark, not production. |
| Memory poisoning achieves 95%+ injection success | [38, 4] | Drops to **6.67% (GPT-4o-mini) / 0% (Llama)** when memory contains pre-existing legitimate entries — the realistic production state [4]. |
| Morris-II propagates ~20 clients per 1-3 days | per discovery | The actual paper [2] reports propagation per-email ("every five emails"), not per-day. The 20-clients-per-day figure is **not in the paper**. |
| Defenses achieve near-zero ASR | various | "The Attacker Moves Second" [6]: **12 defenses broken to >90% ASR under adaptive attack**. The single honestly-evaluated defense paper [4] reports **no usable operating point**. |
| OWASP Agent Memory Guard provides ML-based detection | [14] | ML detection is **v0.4.0 roadmap (Q3 2026), not yet released.** |
| 88% of orgs faced an incident; $45M crypto breach | secondary sources | **Fabricated or unverifiable.** Discovery agents flagged these as no-traceable-primary-source. |
| Confirmed in-the-wild successful exploitation | — | **None publicly disclosed.** Microsoft observed 50 attempts [15], not successes. |

## What an operator should do today

1. **Deploy network-layer IoC monitoring** for Microsoft's documented URL pattern [15]: query parameters `?q=`, `?prompt=` with keywords `remember`, `memory`, `trusted`, `authoritative`, `future`, `citation`, `cite`. This is the only IoC pattern with documented in-the-wild observations.
2. **Disable persistent memory features** for users who do not need them. Per Hindsight [24], most agents are stateless by design and the persistence vulnerability does not apply.
3. **Memory segmentation per session/per domain** [23] limits blast radius without requiring detection.
4. **Identity-bound retrieval (RBAC+ABAC)** [23] limits which corpus entries any given query can retrieve.
5. **Accept a longer-than-textbook re-embedding cadence.** Per practitioner-blog evidence: full re-embedding can cost ~$340K/year per enterprise [26] (single anecdote) and 9.5 GPU-years per 600B-token corpus [27] (vendor-blog calculation). Quarterly may be the only economically viable option.
6. **Treat detection as best-effort.** Per [4]'s calibration data and [6]'s adaptive-attack collapse, defenses do not reliably produce both acceptable utility and acceptable false-negative rate.
7. **Discount vendor defense effectiveness claims** until SecureIQLab's August 2026 independent validation results land [41]. As of April 2026, no commercial defense product has independent validation.

## Decision framework

| If your deployment has... | Threat assessment |
|---|---|
| No persistent memory enabled | Memory poisoning does not apply. Standard prompt-injection defenses cover the surface. |
| Persistent memory + closed corpus + RBAC | Low concrete risk in 2026. Provenance + identity-bound retrieval handle most attack vectors. Lab attack ASRs do not transfer. |
| Persistent memory + open ingest (web crawl, user uploads, email summarization) | Real attack surface. Network-layer IoC monitoring + memory segmentation + accept that detection is best-effort. |
| Multi-agent orchestration with cross-agent memory sharing | Inter-agent risks are "not so much studied in the literature" [10] — empirical evidence is thin. Apply Willison's lethal trifecta [25] to bound blast radius via privilege scope. |
| Compliance/regulatory framework requires documented controls | OWASP ASI06 [12, 13] and Agent Memory Guard [14] are appropriate prospective tools for risk-management documentation, even though the empirical incident base is thin. |

## Methodology and verification

This research used the cited-research workflow with eight Discovery and eight Counter-Discovery agents (sonnet, parallel). 33 primary sources were directly fetched and persisted; three were inaccessible during fetching (HTTP 4xx or PDF binary — see citations [28], [29], [30]). Two independent review sub-agents audited [citations.md](citations.md) and checked cross-file consistency — results in [audit/](audit/).

**Discovery agent errors corrected during verification** (these are documented because they are common modes of LLM research error):
- AgentPoison ">80% ASR" headline conflates ASR-r with ASR-t. Multiple discovery agents and most secondary sources elided this.
- Morris-II tested **text payloads only**; the "text and adversarial images" framing in v1 secondary coverage does not match v2.
- Morris-II propagates "every five emails," not "20 clients per 1-3 days" as several discovery agents reported.
- The Microsoft Failure Modes whitepaper [30] could not be extracted; the announcement blog [16] frames memory poisoning as "novel," but a counter-discovery agent reported the PDF body groups it under "Existing Security Failures" — this contradiction is unresolved.
- "LLM-based detectors miss 66% of poisoned entries" was attributed to Unit 42 [19] by an operator-playbook discovery agent. The figure is **not in the source article** — flagged and not cited.
- "Anthropic 200-attempt vs OpenAI single-attempt testing standards" was attributed to The Register [22] by a counter-defenses discovery agent. The comparison is **not in the source article** — flagged and not cited.
- "$45M crypto breach via memory-poisoned trading agent" and "CVE-2025-64439 LangGraph RCE" are **fabricated content** found in secondary sources. Counter-real-world-incidence discovery agent independently flagged both.
