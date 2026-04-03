# RAG for Effective Heterogeneous Document Lookup

## TL;DR

Building a RAG system for lookup across mixed content (research docs, JIRA issues, email, meeting notes, transcripts, calendar metadata) requires **document-type-specific chunking** (not one-size-fits-all), **metadata embedded with content** (not just as filters), and **hybrid search** (BM25 + dense vectors + metadata filtering). For a lightweight standalone deployment, the recommended stack is BGE-M3 embeddings (local, MIT) + Qdrant single-node or SQLite-Vector+FTS5, with RRF fusion and optional cross-encoder reranking.

## Key Results

| Finding | Evidence |
|---|---|
| Chunk by document type, not uniformly | Adaptive chunking improved correctness 62→72% [4] |
| Embed metadata with content text | Contextual retrieval reduced failure 35-67% [1] |
| Use hybrid search (BM25 + dense) | +18.5% MRR, +7.2% Recall@5 over dense-only [20] |
| Add reranking for largest precision gain | 67% total failure rate reduction [1] |
| Preserve document relationships as metadata | +20-35% relevance with parent-child retrieval |
| BGE-M3 for self-hosted embeddings | MIT, 8k context, dense+sparse, 100+ languages [24] |
| SQLite-based RAG for minimal infra | ~370ms response, ~100MB memory, single file [23] |

## Decision Framework

1. **Hybrid search?** Yes — your content contains exact identifiers (JIRA keys, section numbers)
2. **Vector DB?** ChromaDB (quick start) → SQLite (hybrid-in-a-file) → Qdrant (full-featured)
3. **Embeddings?** BGE-M3 (local, free) or Qwen3-Embedding-8B (higher accuracy, more compute)
4. **Graph RAG?** Skip — metadata linking covers relationship needs at lower cost
5. **Evaluation?** Hit Rate@10 + MRR on 50 queries → Luna for faithfulness spot-checks

## Files

| File | Contents |
|---|---|
| [rag-heterogeneous-document-lookup.md](rag-heterogeneous-document-lookup.md) | Full analysis with methodology |
| [citations.md](citations.md) | All 47 sources with URLs and quality tiers |
| [references/chunking-strategies.md](references/chunking-strategies.md) | Chunking by document type |
| [references/embedding-models.md](references/embedding-models.md) | Embedding model comparison |
| [references/metadata-enriched-retrieval.md](references/metadata-enriched-retrieval.md) | Metadata integration strategies |
| [references/hybrid-search.md](references/hybrid-search.md) | BM25 + dense + structured filters |
| [references/hierarchical-documents.md](references/hierarchical-documents.md) | Parent-child and graph retrieval |
| [references/indexing-pipeline.md](references/indexing-pipeline.md) | Multi-format ingestion architecture |
| [references/retrieval-evaluation.md](references/retrieval-evaluation.md) | Quality metrics and frameworks |
| [references/lightweight-tooling.md](references/lightweight-tooling.md) | Vector DBs, frameworks, deployment |
| [audit/citation-audit.md](audit/citation-audit.md) | Independent citation verification |
| [audit/consistency-review.md](audit/consistency-review.md) | Cross-file consistency check |
