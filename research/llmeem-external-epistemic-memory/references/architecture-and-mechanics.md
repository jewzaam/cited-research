# Architecture and Mechanics

LLMeem implements a hybrid symbolic-neural architecture where a symbolic Belief Maintenance System handles structural operations and an LLM handles semantic operations [1].

## Core BMS Mechanics

### SL Justifications

A node holds one or more SL (Support List) justifications [3]. A node is IN when all antecedents in at least one justification are IN [1][3]. Multiple justifications provide redundancy — a node stays IN if any single justification holds [1].

Non-monotonic reasoning is supported via the outlist mechanism: a justification can specify nodes that must be OUT for the justification to hold [3]. This enables default reasoning ("believe X unless Y is believed") [2][3].

### Retraction Cascades

When a node transitions to OUT, all dependent nodes whose justifications become invalid also cascade to OUT automatically and transitively [1][2]. One retraction triggers network-wide recomputation [2]. The `propagate` command recomputes all truth values across the network [2].

### Nogoods and Dependency-Directed Backtracking

A nogood records a set of nodes that cannot simultaneously hold IN status [1][2]. When a contradiction is detected, the system traces backward through the justification graph and retracts the responsible premise with the fewest dependents to minimize disruption [1][2].

### Challenge/Defend Dialectic

The challenge/defend mechanism provides dialectical argumentation [1][2]:
- `challenge ID "reason"` forces a node OUT
- `defend TARGET CHALLENGE "reason"` neutralizes the challenge, restoring the target

Multi-level chains are supported. Unlike simple retraction, challenge/defend preserves the original argument structure [1].

### Restoration

When a previously retracted node returns to IN, all dependents are automatically recomputed without manual rederivation [1][2].

## Derive-Then-Review Pipeline

The core knowledge generation workflow intentionally over-generates, then prunes [1]:

1. **Derive**: LLM discovers implicit connections between existing beliefs using `reasons derive` [1][2]
2. **Review**: `reasons review-beliefs` audits existing beliefs; 13–37% retracted per review round [1]
3. **Cascade**: Retraction cascades propagate corrections through the dependency network [1]

The productive tension between over-generation and over-pruning yields insight — derive produces "connections the source doesn't make explicit" [1].

## Dual-Path Retrieval

Queries use three passes [1]:

| Pass | Source | Purpose |
|------|--------|---------|
| BMS path | Pre-computed justified beliefs | Structured knowledge with provenance |
| FTS path | Source chunk search (traditional RAG) | Raw document fragments |
| Merge pass | Combined results | Final synthesis |

Each pass operates within a "cognitive budget" concept borrowed from graphics frame budgets [1]. Mixing beliefs and document chunks in a single prompt degraded Opus 4.6 from 95.5% to 86%; three separated passes achieved 100% [1].

## Model Stacking

A layered pipeline with provenance tracking [1]:

1. Model A generates candidate beliefs
2. BMS records beliefs with provenance (source, justification)
3. Review critiques occur (machine + human)
4. Model B receives only validated beliefs and derives further
5. Each layer gets fresh context with critique pipeline as quality gate

## Multi-Agent BMS

Agents import beliefs from other agents using SL justifications with `agent:active` as an antecedent [1]. A belief remains IN only if both:
- The originating agent is active
- The original belief's justification holds

This extends Doyle-style truth maintenance across agent boundaries [1].

## CLI Tools

Two tools serve different use cases [1][2]:

| Tool | Purpose | Storage |
|------|---------|---------|
| `beliefs` | Structured markdown KB with provenance | Markdown files (beliefs.md, nogoods.md) |
| `reasons` | Full BMS with automatic propagation | SQLite (reasons.db) |

The `reasons` CLI provides 25+ commands including `init`, `add`, `retract`, `assert`, `derive`, `review-beliefs`, `search`, `show`, `explain`, `nogood`, `challenge`, `defend`, `trace`, `export-markdown`, `compact`, and `check-stale` [2].

## Construction Pipeline

Building an expert knowledge base follows these stages [1]:

1. Chunk source material
2. Propose beliefs from chunks
3. Human accept/reject
4. Derive connections between accepted beliefs
5. Review derivations
6. Export finalized KB

Cost model: O(chunks) + O(beliefs × rounds) to build, O(queries) amortized at query time [1].

## Gaps and Limitations

1. **Computational complexity**: TMS computation is Σ₂ᵖ-complete [24]; retraction cascades in large networks may be expensive
2. **Single-developer architecture**: No published stress testing at scale beyond 12,731 beliefs [1]
3. **Hybrid integration challenges**: Neural components may relearn mechanistic parts yielding redundant models [52]
4. **Dual-path retrieval latency**: Hybrid search latency equals sum of slowest retriever plus fusion process time
