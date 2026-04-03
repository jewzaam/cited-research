# Lightweight Tooling Stack

This reference covers dimension 8: concrete tools and libraries for a standalone RAG system where resilience is not critical, targeting single-user or small-team use.

## Vector Database Comparison

Based on the 2026 comparison [25]:

| Database | Scale | Latency | Deployment | License | Best For |
|---|---|---|---|---|---|
| **ChromaDB** | 100Ks of vectors | Varies | Embedded, in-process | BSD-3 | Prototyping, MVPs |
| **LanceDB** | Millions | Varies | Embedded, disk-based | Apache 2.0 | Larger-than-memory, privacy |
| **Qdrant** | 100Ms | 8ms p50 (est.) | Self-hosted or cloud | Apache 2.0 | Production, complex filtering |
| **FAISS** | Millions | Fastest in-memory | Library only, no persistence | MIT | Batch search, benchmarking |
| **pgvector** | Millions | 5-50ms | Postgres extension | PostgreSQL | Existing Postgres shops |
| **Milvus** | Billions | 12ms p50 (est.) | Distributed clusters | Apache 2.0 | Enterprise scale, GPU |

### For Lightweight Standalone Use

**ChromaDB** and **LanceDB** are the strongest candidates [25]:

- **ChromaDB**: embedded/in-process, zero infrastructure, Python-native. Performance degrades above hundreds of thousands of vectors [25]. Best for rapid prototyping and corpora under 100K chunks.
- **LanceDB**: disk-based IVF-PQ indexing enables larger-than-memory datasets [25]. Zero-copy columnar format. Better for larger corpora that exceed RAM but don't need distributed infrastructure.

### SQLite-Based RAG [23]

A notable lightweight option: SQLite-Vector for vector storage + SQLite-AI for local embedding generation + FTS5 for keyword search, all combined via RRF:

| Metric | Value |
|---|---|
| Query response time | ~370ms average |
| Memory usage | ~100 MB |
| Embedding model | Gemma Embedding 300M Q8 |
| Hybrid search | FTS5 + sqlite-vector via RRF |

Single-file database, edge-deployable, no external services required [23].

## Framework Comparison

### LangChain vs. LlamaIndex

| Aspect | LangChain | LlamaIndex |
|---|---|---|
| Focus | General-purpose agent orchestration | Document retrieval and indexing |
| Overhead (est.) | ~10ms | ~6ms |
| Token usage (est.) | ~2.40k | ~1.60k |
| Strengths | Multi-step workflows, agent chains | Hierarchical chunking, auto-merging, sub-question decomposition |
| Best for | Complex multi-step workflows | Document-heavy RAG applications |
| License | MIT | MIT |

Discovery sources report a trend toward hybrid usage: LlamaIndex for indexing/retrieval + LangChain (or LangGraph) for agent flow control.

### Raw SDK vs. Framework

| Factor | Raw SDK | Framework |
|---|---|---|
| Development time | Weeks (est.) | Hours (est.) |
| Control | Full | Abstracted |
| Lock-in | None | Framework-dependent |
| Minimum stack | LLM + embedding model + vector DB | Framework + LLM + embedding model + vector DB |

For a lightweight system, starting with a framework reduces time-to-value. LlamaIndex is better suited when the primary task is document retrieval (this use case).

## Recommended Lightweight Stack

For indexing research docs, JIRA, email, meeting notes, and transcripts in a standalone, single-user or small-team setup:

### Option A: Minimal (Embedded)

```
Embedding: BGE-M3 (local, MIT, 8192 context, dense+sparse)
Vector DB: ChromaDB (embedded, in-process)
Keyword:   ChromaDB metadata filtering (limited)
Framework: LlamaIndex (document-focused)
LLM:       Local (Ollama) or API
```

Pros: Zero infrastructure, runs on a laptop
Cons: No native BM25/hybrid search, limited scale

### Option B: Hybrid Search (SQLite)

```
Embedding: Gemma Embedding 300M Q8 or BGE-M3 (local)
Vector DB: SQLite-Vector (embedded)
Keyword:   SQLite FTS5 (BM25)
Fusion:    RRF (in-application code)
Framework: LlamaIndex or custom
LLM:       Local (Ollama) or API
```

Pros: True hybrid search, single-file database, ~100MB memory [23]
Cons: Newer ecosystem, less community support

### Option C: Production-Ready Lightweight

```
Embedding: BGE-M3 or Qwen3-Embedding-8B (local)
Vector DB: Qdrant (single-node Docker)
Keyword:   Qdrant sparse vectors (BM25-like)
Fusion:    Built-in RRF
Framework: LlamaIndex
LLM:       Local (Ollama) or API
```

Pros: Real hybrid search, advanced filtering, scales to millions
Cons: Requires Docker, more operational overhead

## Memory and Scaling Estimates

For a corpus of ~10K documents (research + JIRA + email + meetings):
- Assuming ~5 chunks per document average = ~50K chunks
- At 384 dimensions × float32: ~50K × 384 × 4 bytes ≈ 75 MB vectors
- At 768 dimensions: ~150 MB vectors
- At 4096 dimensions: ~800 MB vectors

All options above handle this comfortably. ChromaDB and LanceDB scale well to hundreds of thousands of vectors [25].

## Gaps and Limitations

- ChromaDB's native hybrid search capabilities are limited compared to Qdrant or dedicated BM25 engines
- SQLite-Vector + SQLite-AI ecosystem is young (2026) with limited community support and documentation [23]
- Framework overhead estimates (~6-10ms) come from a single source and lack methodology details [24]
- No benchmark compares these lightweight stacks specifically on heterogeneous document corpora
- LanceDB benchmarks for RAG workloads are scarce compared to ChromaDB and Qdrant
- Zvec (Feb 2026, claiming >8000 QPS) is too new to evaluate for production readiness
