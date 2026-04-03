# Hybrid Search Architecture

This reference covers dimension 4: combining dense vector search with sparse keyword search (BM25) and structured filters for heterogeneous document retrieval.

## Core Architecture

Hybrid search combines three retrieval approaches [21] [22]:
1. **Sparse retrieval** (BM25/SPLADE): exact keyword matching
2. **Dense retrieval** (embeddings): semantic similarity
3. **Structured filtering** (metadata): categorical/temporal constraints

## Reciprocal Rank Fusion (RRF)

The standard fusion algorithm combines ranked results from multiple retrievers [11]:

```
score(d) = Σ 1/(rank_i(d) + k)
```

Where `k=60` is the default constant (Microsoft Azure AI Search) [11]. RRF is score-agnostic — it works on ranks, not raw scores — avoiding normalization problems inherent to other fusion methods [11].

### Alternatives to RRF

| Method | Formula | When to Use |
|---|---|---|
| RRF | 1/(rank + k) | Zero-config default, prototyping [21] |
| Convex Combination | α·dense + (1−α)·sparse | Outperforms RRF with 50+ labeled pairs [21] |
| DBSF | Distribution-based normalization | When dense/sparse score magnitudes vary [21] |

Alpha guidance for convex combination: ~0.3 for technical documentation, ~0.7 for conversational queries [21].

**Critical warning:** Poorly tuned hybrid configurations underperform dense baselines. One benchmark found initial hybrid setup scored 0.390 MRR vs. 0.410 dense baseline — tuning recovered performance to 0.486 [21].

## Performance Benchmarks

### Hybrid vs. Dense-Only

| Metric | Dense-Only | Hybrid | Improvement | Source |
|---|---|---|---|---|
| MRR | 0.410 | 0.486 | +18.5% | [20] |
| Recall@5 | 0.655 | 0.702 | +7.2% | [20] |
| NDCG (BEIR aggregate) | baseline | — | +26-31% | [21] |

Dataset: 494,094 Amazon Customer Reviews, 100 curated difficult queries, Qdrant with dual vector storage [20].

### With Reranking

Anthropic's contextual retrieval benchmark [1]:
- Contextual Embeddings alone: 35% failure rate reduction (5.7% → 3.7%)
- + Contextual BM25: 49% reduction (5.7% → 2.9%)
- + Reranking: 67% reduction (5.7% → 1.9%)

Reranking is the single largest precision improvement in the pipeline [1] [42].

### Latency

Hybrid search adds ~201ms per query (+24.5% over dense-only), with vector generation consuming >90% of total latency [20].

## When Each Method Wins

### BM25 Outperforms Semantic Search For [22]:
- **Exact identifiers**: error codes, API endpoints, function names, SKUs
- **Structured technical content**: API docs, legal clause references
- **Protocol-specific queries**: section numbers, case IDs
- **Keyword-heavy queries**: domain-specific jargon

### Semantic Search Wins For:
- Natural language questions
- Synonym/paraphrase variations
- Exploratory research
- Conceptual matching without exact vocabulary

### Hybrid Is Essential For [21]:
- Production RAG systems (pure vector fails 40-60% on complex retrieval)
- Heterogeneous content mixing exact terms with conceptual needs
- Enterprise scale (10k+ documents)

## SPLADE vs. BM25

SPLADE is a learned sparse model that expands both query and document representations with semantically related terms [21] [47]:

| Aspect | BM25 | SPLADE |
|---|---|---|
| Vocabulary expansion | None | Learned |
| GPU required | No | For indexing |
| BEIR performance | Baseline | Consistently higher [21] |
| Best for | Exact identifiers | Mixed vocabulary, enterprise docs |

## Cross-Encoder Reranking

Two-stage architecture: first-stage retriever narrows millions to tens; cross-encoder reranks to final results [42]:
- 10-25% accuracy improvement over pure retrieval [42]
- 35% reduction in LLM hallucinations [42]
- ColBERT late interaction: 2 orders of magnitude faster than full cross-encoders, 4 orders fewer FLOPs [46]

## Citation Anchoring

A practical pattern for ensuring citation accuracy in RAG [22]: after selecting top chunks semantically, run a lightweight BM25 check for key tokens you plan to cite (section numbers, endpoint paths, function names). If a chunk fails the check, it is a risky citation.

## Gaps and Limitations

- Hybrid search benefits scale with vocabulary mismatch — e-commerce catalogs show minimal gains (+1.7-1.9% NDCG) while research literature benefits significantly (+24% recall) [21]
- Optimal alpha tuning for heterogeneous corpora (research + JIRA + email + transcripts) is not established
- SPLADE production readiness (infrastructure, latency impacts) vs. BM25 simplicity trade-off needs more data for lightweight deployments
- Cross-encoder model selection guidance for technical/operational content is lacking
