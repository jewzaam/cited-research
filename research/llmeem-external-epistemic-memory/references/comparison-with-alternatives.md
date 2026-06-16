# Comparison with Alternatives

EEM positions itself against five alternative approaches to LLM knowledge management: RAG, context windows, parametric knowledge, knowledge graphs, and MCP servers.

## EEM vs. RAG

| Dimension | EEM | RAG |
|-----------|-----|-----|
| State | Persistent justified beliefs | Stateless per-query retrieval |
| Justification | Full dependency chains with IN/OUT truth values | Chunk provenance only |
| Retraction | Automatic cascading when beliefs invalidated | No retraction mechanism |
| Contradiction handling | Nogood recording + backtracking | No built-in contradiction detection |
| Audit trail | Justification graph traversal via `explain` | Source document references |
| Query cost | O(queries) amortized | O(embed + search + generate) per query |
| Build cost | O(chunks) + O(beliefs × rounds) | O(embed) once + incremental |

RAG's core limitation from EEM's perspective: "RAG is stateless by default, and every step toward statefulness requires deliberate work" [1]. Chunking "destroys document structure" — entity relationships and cross-source contradictions are lost [1].

However, modern RAG improvements narrow the gap. Hybrid search (BM25 + vector) adds 11–15% accuracy. Re-ranking adds 10–40% precision improvement. CoRAG achieves 72.5 EM on multi-hop QA vs. 58.0 baseline [counter-discovery findings].

## EEM vs. Context Windows

EEM argues context windows are fundamentally ephemeral [1]:

| Limitation | Evidence |
|-----------|---------|
| Lost in the middle | 30%+ accuracy drops for mid-window content [41] |
| Compaction destroys justifications | 88% token reduction loses "subtle but critical context" [42] |
| Working memory bottleneck | Effective context far below advertised maximums [41] |
| Session boundary reset | No persistence across conversations [1] |

LLMeem measured context compaction destroying justification networks across 33 compaction events [1]. After 2–3 compactions, agents "behave as if the session just started" [42].

Context expansion doesn't solve the problem — a smaller, governed context outperforms a large stale one [41].

## EEM vs. Parametric Knowledge

Parametric knowledge (model weights) provides no audit trail [1]. LLMeem frames this as the central limitation: "you cannot ask 'how do you know that?' and get a traceable answer from parametric knowledge" [1].

Tool-memory conflicts (divergence between parametric knowledge and external tools) affect 14–83% of test instances depending on model size [counter-discovery findings]. The parameter threshold around 70B marks the boundary for better alignment.

## EEM vs. Knowledge Graphs / GraphRAG

Knowledge graphs share EEM's emphasis on structured relationships and traceability but differ in representation:

| Dimension | EEM (BMS) | Knowledge Graph |
|-----------|-----------|----------------|
| Structure | Dependency network with justifications | Entity-relationship graph |
| Truth values | Explicit IN/OUT per node | No built-in truth maintenance |
| Retraction | Automatic cascading | Manual graph updates |
| Reasoning | Non-monotonic via outlists | Graph traversal / pattern matching |
| Construction | LLM + human review pipeline | LLM extraction or manual |

GraphRAG (Microsoft Research) outperforms baseline RAG on comprehensiveness and diversity while maintaining similar faithfulness [counter-discovery findings]. Vector RAG scores 0% on schema-bound queries where Graph RAG achieves 90%+ [34], but GraphRAG shows 13.4% lower accuracy than vanilla RAG on Natural Questions [35].

Neither approach consistently outperforms — 85% of enterprises adopting hybrid systems by 2026 [54].

## EEM vs. MCP Servers as Knowledge Stores

MCP (Model Context Protocol) is a connectivity protocol, not a knowledge representation layer [11][12][38]:

| Dimension | EEM | MCP |
|-----------|-----|-----|
| Purpose | Justified persistent knowledge | Standardized tool/data access |
| Analogy | Knowledge system | "USB-C port" [11] |
| Justification chains | Yes (SL justifications, dependency graph) | No |
| Truth values | IN/OUT per belief | No |
| Retraction cascades | Yes | No |
| Persistence | SQLite-backed belief store | External system state |
| Audit trail | Full justification graph traversal | Tool-dependent logging |

MCP servers can expose domain knowledge as tool definitions with tool responses serving as knowledge retrieval [12]. However, this "strips away critical details (authentication flows, error handling, rate limits, governance)" that robust knowledge systems need [38].

MCP and EEM are complementary rather than competing:
- MCP provides the connectivity layer (how to access data)
- EEM provides the epistemic layer (what is justified and why)

An MCP server could wrap an EEM knowledge base, exposing `reasons search`, `reasons show`, and `reasons explain` as MCP tools — providing both the connectivity standard and the justification infrastructure.

## EEM vs. LLM Wiki (Karpathy Pattern)

The LLM Wiki pattern uses markdown files compiled and maintained by an LLM [counter-discovery findings]:

| Dimension | EEM | LLM Wiki |
|-----------|-----|----------|
| Structure | Dependency graph with truth values | Markdown pages with cross-references |
| Maintenance | Derive-then-review pipeline | LLM ingests, queries, lints |
| Error detection | Retraction cascades + nogoods | Lint pass for contradictions |
| Compounding | Belief dependencies explicit | Error compounding risk |
| Scale | 237–12,731 beliefs per KB | 20–50 documents optimal |

LLM Wiki excels at compiled expertise in bounded domains with simple infrastructure. EEM adds formal belief maintenance at the cost of architectural complexity.

## EEM vs. Agent Memory Systems

Modern agent memory systems (Mem0, A-MEM, MemGPT) focus on user personalization and session continuity [39][13]:

| Dimension | EEM | Agent Memory |
|-----------|-----|-------------|
| Retrieval precision | N/A (structured query) | 0.05–0.08 mean precision (Mem0, Zep, Hindsight) [13] |
| Justification | Full dependency chains | No |
| Contradictions | Nogood recording + backtracking | Limited conflict resolution |
| Persistence | Survives model swaps | Session-based or cloud-backed |
| Scale | 237–12,731 beliefs | Varies |

The PrecisionMemBench study found comparison memory systems achieve 0.05–0.08 mean retrieval precision with zero active retrieval passes [13]. The central claim: cross-session memory is "a state management problem, not a search problem" [13] — aligning with EEM's structured approach over similarity-based retrieval.

## Summary

EEM occupies a unique position: it is the only approach that combines formal truth maintenance (justification chains, retraction cascades, nogoods) with LLM-driven semantic operations. No other system reviewed provides automatic dependency-directed backtracking for LLM knowledge.

The trade-off: formal belief maintenance adds architectural complexity and computational cost that simpler approaches (RAG, LLM Wiki, MCP tools) avoid. Whether that complexity is justified depends on whether the use case requires auditability and consistency guarantees or can tolerate retrieval imprecision.

## Gaps and Limitations

1. **No head-to-head benchmarks**: No published comparison of EEM against GraphRAG, Mem0, or LLM Wiki on identical evaluation sets
2. **Scale comparison absent**: No data on how EEM performs relative to alternatives as knowledge base sizes grow
3. **Cost comparison missing**: No published cost analysis comparing EEM construction vs. RAG embedding vs. KG construction
4. **MCP integration untested**: The MCP-wrapping-EEM architecture is theoretical, not demonstrated
