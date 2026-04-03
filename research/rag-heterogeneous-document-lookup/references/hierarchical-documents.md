# Hierarchical and Relational Document Handling

This reference covers dimension 5: preserving and exploiting parent-child relationships, cross-references, and document graphs in RAG retrieval.

## Parent-Child Retrieval

### Concept

Small child chunks (100-500 tokens) are indexed for precise vector similarity search, while larger parent chunks (500-2000 tokens) are returned to the LLM for context-rich responses. This decouples retrieval granularity from generation context [27].

### Implementations

- **LangChain ParentDocumentRetriever**: maps child chunks to parent documents via configurable storage backends [33]
- **LlamaIndex Recursive Retrieval**: supports node reference patterns with query-time expansion [27]
- **Haystack AutoMergingRetriever**: if 60%+ of matched leaf chunks belong to the same parent, returns the parent instead [27]

### Performance

Typical gains of +20-35% relevance on structured documents compared to flat chunking (est., from practitioner reports). Haystack testing on BBC news: BM25Retriever retrieved 10 documents, AutoMergingRetriever returned 7 by consolidating into 3 parent articles [27].

## RAPTOR: Recursive Tree Retrieval

RAPTOR [2] constructs hierarchical summaries by:
1. Recursively embedding and clustering text chunks
2. Generating summaries of each cluster
3. Building a tree with differing levels of summarization from bottom up
4. Retrieving from multiple tree levels at query time

**Performance:** 20% absolute accuracy improvement on QuALITY benchmark with GPT-4 [2]. Particularly effective for multi-step reasoning across lengthy documents.

## Graph-Based RAG

### Microsoft GraphRAG [15]

Architecture:
1. Divide corpus into TextUnits with fine-grained references
2. Extract entities, relationships, and claims
3. Apply Leiden community detection for hierarchical clustering
4. Generate community summaries at multiple abstraction levels

Query modes:
- **Global Search**: broad corpus questions using community summaries
- **Local Search**: specific entity exploration via neighbors
- **DRIFT Search**: local search with community context
- **Basic Search**: vector similarity fallback

**Cost:** $50-200 for a 500-page corpus with 45-minute indexing; LightRAG indexes the same for $0.50 in 3 minutes; traditional vector RAG costs under $5 [39].

### HopRAG [9]

Constructs a passage graph where:
- Text chunks are vertices
- LLM-generated pseudo-queries are edges (logical connections)
- Retrieve-reason-prune mechanism explores multi-hop neighbors guided by pseudo-queries and LLM reasoning

Designed for queries requiring multi-hop reasoning where relevant passages are logically but not lexically/semantically similar.

## Multi-Hop Retrieval Challenges

The MultiHop-RAG benchmark [10] found that existing RAG methods perform unsatisfactorily on queries requiring retrieval and reasoning over multiple pieces of supporting evidence. Over 60% of retrieved passages are indirectly relevant or irrelevant for multi-hop QA tasks.

## Contextual Retrieval vs. Late Chunking [16]

| Approach | Strength | Weakness |
|---|---|---|
| Contextual retrieval | Preserves semantic coherence effectively | Substantial computational overhead |
| Late chunking | Superior operational efficiency | Sacrifices some relevance and completeness |

Contextual retrieval prepends 50-100 tokens of explanatory context to each chunk before embedding [1], achieving 35-67% failure rate reductions depending on configuration.

## Applying to Heterogeneous Content

### JIRA Issue Hierarchies

JIRA's default hierarchy is Epic → Story → Subtask. Approaches:
- Store `parent_id`, `epic_key`, `issue_type` as metadata for filtered retrieval
- Individual tickets may not need chunking if context-coherent
- Issue comments and descriptions should be chunked separately with parent issue metadata
- Issue links (blocks, relates-to, duplicates) can be modeled as graph edges

### Meeting Notes + Calendar Events

A case study on contextual RAG for meetings [37] enriches text with:
- Semantic labels: risk, decision, action item
- Domain anchors: JIRA ID, launch name, project reference

This enables filtered retrieval by decision type or project association rather than pure semantic similarity.

### Email Threads

Thread-aware processing groups messages by thread_id and constructs chronological flow [32]. Cross-references to JIRA issues or calendar events within emails should be extracted and stored as metadata links.

### Research Documents with Cross-References

Document cross-references (citations, "see Section X", links to other docs) are typically lost in text-to-vector workflows. Graph-based systems can follow references programmatically with configurable depth parameters. For a lightweight system, storing cross-reference targets as metadata fields offers a simpler alternative.

## Gaps and Limitations

- GraphRAG costs ($50-200 per 500 pages) may be prohibitive for a lightweight standalone system [39]
- No benchmark specifically evaluates hierarchical retrieval on mixed JIRA/email/meeting content
- Calendar event linking to meeting notes via temporal reasoning lacks dedicated tooling
- The HopRAG accuracy improvement claim (76.78%) was not confirmed in the accessible abstract [9]
- Auto-merging threshold tuning guidance for different document types is limited to general recommendations
