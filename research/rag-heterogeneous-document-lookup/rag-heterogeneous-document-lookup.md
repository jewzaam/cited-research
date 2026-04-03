# RAG for Effective Heterogeneous Document Lookup

## Overview

This document synthesizes citation-backed research on building a Retrieval-Augmented Generation (RAG) system for effective lookup across heterogeneous document types: research documents (long-form markdown with citations), JIRA issues (structured JSON with parent-child hierarchies), email threads, meeting notes, transcripts, calendar metadata, and associated structured data. The focus is on a lightweight, standalone deployment where infrastructure resilience is not critical.

The analysis spans 8 dimensions: chunking strategies, embedding model selection, metadata-enriched retrieval, hybrid search architecture, hierarchical document handling, indexing pipeline design, retrieval quality evaluation, and lightweight tooling. Full methodology and per-dimension detail are in the [reference files](references/).

---

## Key Findings

### 1. Chunk by Document Type, Not Uniformly

The most impactful finding across multiple sources: **no single chunking strategy works well across all document types**. Microsoft's architecture guide [12] and the Adaptive Chunking framework [4] both demonstrate that document-aware strategies significantly outperform uniform approaches.

| Content Type | Recommended Strategy | Rationale |
|---|---|---|
| Markdown research docs | Header-based splitting [33] | Preserves logical structure at H2/H3 boundaries |
| JIRA issues (JSON) | Whole-document or field-concatenation | Issues are typically context-coherent; chunk comments separately |
| Email threads | Thread-aware, ~512 tokens per thread [32] | Group by thread_id, maintain chronological flow |
| Meeting transcripts | Speaker-aware segmentation [28] | Segment on speaker changes, 1000+ char chunks |
| Calendar events | Whole-event with metadata | Short enough for single chunks; metadata is the value |

**Chunk size sweet spot:** 512-1024 tokens for analytical queries [13], with a quality cliff beyond ~2.5k tokens [5]. Overlap is retrieval-method-dependent: beneficial for dense retrieval but showed no measurable benefit with SPLADE sparse retrieval [5].

### 2. Embed Metadata with Content

Metadata is not just a filter — it belongs in the embedding itself. Research comparing four metadata integration strategies found that **prefixing metadata as text and unified embeddings consistently outperform plain-text baselines** [6]. Anthropic's contextual retrieval prepends 50-100 tokens of chunk-specific context, reducing retrieval failure by 35-67% depending on configuration [1].

The SRAG approach [8] goes further, enriching chunks with topics, sentiments, knowledge graph triples, and semantic tags, achieving a 30% QA improvement (p=2e-13).

**Practical approach:** For each chunk, prepend a brief context line containing the source type, document title, date, and any parent relationship. Example: `"JIRA Story PROJ-1234 (Epic: PROJ-1200, Status: In Progress, 2026-03-15): <chunk text>"`. This is cheap, one-time during indexing, and provides the embedding model with disambiguating structural cues [6].

### 3. Hybrid Search Is Non-Negotiable for Mixed Content

Pure vector search fails on exact identifiers (JIRA keys, error codes, API endpoints, section references) that are common in operational content [22]. Hybrid search combining dense embeddings with BM25 keyword search achieves +18.5% MRR and +7.2% Recall@5 over dense-only [20], with benefits scaling proportionally to vocabulary mismatch between queries and documents [21].

**Architecture:** Run BM25 and dense retrieval in parallel, fuse with Reciprocal Rank Fusion (RRF, k=60) [11], then rerank top results with a cross-encoder. Adding reranking on top of hybrid retrieval achieves the largest single precision improvement — Anthropic measured 67% total failure rate reduction with this full pipeline [1].

**When BM25 alone is sufficient:** queries for exact identifiers (SKUs, error codes, API paths, legal clause numbers), structured technical content, and protocol-specific lookups [22].

### 4. Preserve Document Relationships, Don't Flatten Them

JIRA issues have parent-child-grandchild trees. Research documents cross-reference each other. Meeting notes link to calendar events. Flattening these into independent chunks destroys valuable retrieval signals.

**Approaches by cost:**
- **Metadata linking** (low cost): Store `parent_id`, `epic_key`, `thread_id` as filterable metadata. Retrieve related documents via metadata queries after initial semantic retrieval.
- **Parent-child retrieval** (medium cost): Index small child chunks for precision, return larger parent chunks for context [27]. +20-35% relevance improvement on structured documents (est., from practitioner reports).
- **Graph RAG** (high cost): Build knowledge graphs with entity/relationship extraction [15]. Enables multi-hop reasoning but costs $50-200 per 500 pages [39] — likely excessive for a lightweight system.

**Recommendation for lightweight deployment:** Metadata linking with parent-child retrieval as needed. Skip GraphRAG unless multi-hop reasoning across unrelated documents is a primary requirement.

### 5. Lightweight Tooling Is Sufficient for This Scale

For a corpus of ~10K documents (research + JIRA + email + meetings), all lightweight vector databases handle the scale comfortably:

| Stack | Hybrid Search | Memory | Complexity |
|---|---|---|---|
| ChromaDB + LlamaIndex | Limited (metadata only) | Low | Minimal |
| SQLite-Vector + FTS5 | Full (RRF) | ~100 MB [23] | Low |
| Qdrant (single-node) + LlamaIndex | Full (built-in) | Moderate | Docker required |

**SQLite-based RAG** [23] is notable for lightweight deployments: single-file database, hybrid search via FTS5 + sqlite-vector combined with RRF, ~370ms query response, ~100MB memory. No external services required.

**Qdrant** (single-node Docker) offers the most feature-complete option with advanced payload filtering and native hybrid search, at the cost of Docker operational overhead.

### 6. BGE-M3 Is the Default Embedding Choice

For a self-hosted system indexing heterogeneous content, **BGE-M3** stands out [24]:
- MIT licensed, free to self-host
- 8,192 token context window (handles long research sections)
- Multi-paradigm: dense + sparse + multi-vector retrieval natively
- 100+ language support
- MTEB score: 63.0 (competitive, not top)

For higher accuracy at the cost of more compute, **Qwen3-Embedding-8B** (70.58 MTEB, Apache 2.0, 32k context) is the top self-hostable model [24]. For API-based simplicity, **voyage-3-large** ($0.06/1M tokens, 32k context) offers the best cost-performance ratio [24].

### 7. Evaluate Cheaply but Deliberately

Start with simple retrieval metrics before investing in LLM-as-judge frameworks:

1. **Create a test set**: 50-100 real queries across all content types with expected relevant documents
2. **Measure Hit Rate@10 and MRR**: no LLM calls needed, fast to compute [19]
3. **Spot-check faithfulness**: Run RAGAS or Luna [18] on a response subset (Luna: 97% cheaper than GPT-3.5-based evaluation [18])
4. **Iterate**: Change one variable (chunking, embedding, retrieval), re-measure

**Caution:** RAGAS Faithfulness has known reliability issues on complex financial and reasoning domains, failing on 83.5% of FinanceBench examples [26]. The improved RAGAS++ variant addresses this [26].

---

## Recommended Architecture

For a lightweight standalone system indexing heterogeneous content:

```
Sources
  ├── Markdown files → Header-based chunking [33]
  ├── JIRA JSON → Field concatenation + metadata extraction
  ├── Email (.eml) → Thread-aware chunking [32]
  ├── Transcripts → Speaker-aware chunking [28]
  └── Calendar JSON → Whole-event + metadata
         ↓
Metadata enrichment
  ├── Prepend context (source type, title, date, parent) [1] [6]
  ├── Extract cross-references (JIRA IDs, dates, people)
  └── Normalize temporal metadata
         ↓
Embedding: BGE-M3 (local, MIT) [24]
         ↓
Storage: Qdrant (single-node) or SQLite-Vector + FTS5 [23]
  ├── Dense index (semantic similarity)
  ├── Sparse index (BM25 keyword matching)
  └── Metadata index (structured filters)
         ↓
Retrieval: Hybrid search with RRF (k=60) [11]
         ↓
Reranking (optional): Cross-encoder on top 20-50 results [1]
         ↓
LLM generation with retrieved context
```

### Decision Framework

1. **Do I need hybrid search?** Yes, if your queries include exact identifiers (JIRA keys, error codes, section numbers). Almost certainly yes for this use case.
2. **Which vector DB?** ChromaDB for quick start, SQLite for hybrid-in-a-file, Qdrant for full-featured.
3. **Local or API embeddings?** Local (BGE-M3) for privacy, zero ongoing cost, and independence from external services.
4. **Graph RAG?** Skip unless multi-hop reasoning across unrelated documents is a primary requirement. Metadata linking covers most relationship needs at much lower cost.
5. **How much to invest in evaluation?** Start with Hit Rate@10 + MRR on 50 queries. Add Luna for faithfulness if generation quality matters.

---

## Cross-Cutting Concerns

### Temporal Relevance

Operational content (JIRA, email, meetings) has strong temporal dependencies — recent items are usually more relevant. Research documents are less time-sensitive. Normalize temporal metadata across sources and consider recency weighting in retrieval scoring.

### Cross-Document Deduplication

The same information often appears in multiple sources (JIRA description repeated in meeting notes, email thread summarizing a JIRA decision). This is an acknowledged but unsolved challenge. Practical mitigation: metadata filtering to prefer authoritative sources (JIRA over meeting notes for issue status).

### Incremental Updates

For a living corpus, use content hashing to detect changes and idempotent uploads (document_id + chunk_id keys) to avoid duplicates. Batch updates at 100-1000 vectors at a time for efficiency.

---

## Limitations

1. **No benchmark exists for mixed-corpus RAG.** All cited benchmarks evaluate single document types (financial filings, news articles, academic papers). Performance on heterogeneous corpora is extrapolated, not measured.

2. **Chunking strategy interactions are untested.** Using header-based chunking for markdown and speaker-based for transcripts within the same index has not been evaluated end-to-end.

3. **SQLite-Vector is young.** The SQLite-based RAG stack [23] is emerging (2026) with limited community support compared to ChromaDB or Qdrant.

4. **MTEB scores are self-reported** and may not reflect real-world performance on heterogeneous content [24].

5. **GraphRAG cost data** comes from a single practitioner comparison [39] and may vary significantly by implementation.

6. **Some arXiv claims were verified from abstracts only** — full paper data may contain additional nuance or caveats.

---

## Sources

All claims in this document are cited with numbered references. See [citations.md](citations.md) for full source details including URLs, access status, and quality tiers. Reference files by dimension are in [references/](references/).
