# Theoretical Foundations

EEM draws on four foundational works from classical AI and epistemology, plus Tulving's memory taxonomy from cognitive psychology.

## Doyle's Truth Maintenance System (1979)

Jon Doyle introduced the first domain-independent Justification-based Truth Maintenance System (JTMS) [3]. A TMS is a problem solver subsystem that records and maintains reasons for program beliefs, enabling programs to make assumptions and revise beliefs when discoveries contradict them [3][20].

EEM places the LLM in Doyle's "exogenous problem-solver slot" — the TMS handles structural operations (justifications, propagation, backtracking) while the problem solver handles semantic operations [1]. LLMeem renamed TMS to "Belief Maintenance System" (BMS) to emphasize the epistemic framing [1].

| Concept | Definition |
|---------|-----------|
| SL Justification | Node is IN when all antecedents are IN; multiple justifications supported [3] |
| IN/OUT propagation | Nodes carry truth values; changes cascade through dependency network [3] |
| Non-monotonic reasoning | New information can invalidate old beliefs via outlist mechanism [3][20] |
| Dependency-directed backtracking | Traces contradictions to responsible premise for minimal disruption [3] |

1,976+ citations per Semantic Scholar [3].

## de Kleer's Assumption-Based TMS (1986)

de Kleer extended Doyle's work with ATMS, which manipulates assumption sets rather than single justifications [4]. ATMS maintains multiple contexts simultaneously, enabling efficient context switching and work with inconsistent information [4].

LLMeem chose BMS over ATMS because "revision matters more than maintaining multiple environments when the problem solver (LLM) produces 13-37% errors" [1]. The key architectural decision: single-context revision with retraction cascades rather than multi-context assumption tracking.

## AGM Belief Revision (1985)

Alchourrón, Gärdenfors, and Makinson formalized rational belief revision with three operations [5][8]:

| Operation | Symbol | Description |
|-----------|--------|-------------|
| Expansion | K+p | Add p to belief set K without removing anything |
| Revision | K*p | Add p while ensuring consistency |
| Contraction | K÷p | Remove p from K |

LLMeem approximates AGM entrenchment principles in its backtracking entrenchment scoring — when resolving nogoods, it retracts the premise with the fewest dependents, a "crude approximation of AGM" [1]. The formal AGM postulates assume logical omniscience and perfect reasoning [8], which LLMs do not possess.

### AGM Limitations Relevant to EEM

The Stanford Encyclopedia documents nine criticisms [8]:
1. **Recovery postulate controversy** — most debated AGM postulate; produces counterintuitive results [8]
2. **Logical omniscience assumption** — agents treated as perfect reasoners with unlimited cognitive capacity [8]
3. **Iterated revision failure** — AGM addresses only single-step changes [8]
4. **Cannot handle conditionals** — Gärdenfors impossibility theorem shows Ramsey test incompatible with revision postulates [8]

## McCarthy & Hayes Frame Problem (1969)

The frame problem asks how to write formulae describing action effects without explicitly stating everything that does not change [6]. The narrow technical version was solved by the end of the 1980s (successor state axioms, circumscription), but the broader epistemological version remains open [6].

LLMeem addresses the frame problem through "staleness checking" — detecting when source files change under existing beliefs [1]. The `check-stale` command compares source file hashes to detect when the ground truth under a belief has shifted [2].

## Tulving's Memory Taxonomy (1972)

Endel Tulving distinguished semantic memory ("mental thesaurus" for general knowledge) from episodic memory (temporally-dated personal experiences) [7]. EEM classifies itself as semantic memory in Tulving's taxonomy — persistent structured knowledge that survives across sessions, model swaps, and time boundaries [1].

The distinction matters architecturally: EEM does not track conversation episodes but stores justified factual claims. This is persistent knowledge in the Tulving sense, not experience replay [7][50].

## Gaps and Limitations

1. **Theoretical age**: Foundational works (1969–1985) predate modern understanding of LLM limitations in non-monotonic reasoning [43][44]
2. **LLM non-monotonic reasoning failures**: Multiple 2025–2026 studies show LLMs exhibit "curse of complexity" in non-monotonic reasoning that persists even with larger models [43]; LLMs fail to maintain stable beliefs when adding supporting or unrelated information [44]
3. **AGM assumes perfect reasoning**: LLMs are not logically omniscient agents — the AGM framework's rationality postulates may not apply [8]
4. **Neuro-symbolic integration**: The hybrid symbolic BMS + neural LLM architecture faces unresolved challenges including scalability, integration complexity, and lack of consensus architecture [52]
