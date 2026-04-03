# Embedding Model Selection for Mixed Corpora

This reference covers dimension 2: which embedding models handle the semantic range from technical research prose to terse JIRA summaries to conversational transcripts, and trade-offs between local vs. API models.

## Top Models by MTEB Retrieval Score (2026)

Prem.ai's 2026 benchmark guide [24] ranks models by retrieval-specific NDCG@10 (more relevant than overall MTEB averages for RAG):

| Model | MTEB Score | Cost/1M tokens | Context | Dims | Self-Host |
|---|---|---|---|---|---|
| Qwen3-Embedding-8B | 70.58 | Free | 32k | 7,168 | Yes (Apache 2.0) |
| NV-Embed-v2 | 69.32 | Free | 32k | 4,096 | Yes (CC-BY-NC-4.0) |
| Gemini Embedding-001 | 68.32 | $0.15 | 2k | 3,072 | No |
| voyage-3-large | ~67+ | $0.06 | 32k | 2,048 | No |
| text-embedding-3-large | 64.6 | $0.13 | 8k | 3,072 | No |

Note: MTEB scores are self-reported and may not reflect real-world performance [24]. The recommendation is to use MTEB to narrow options, then benchmark on your own dataset.

## Key Selection Criteria for Heterogeneous Corpora

### Context Length

Content types vary significantly in typical length:
- JIRA issue summaries: 50-200 tokens
- Email messages: 100-500 tokens
- Meeting transcript segments: 200-1000 tokens
- Markdown research sections: 500-2000+ tokens

Models with larger context windows (32k tokens for Qwen3, NV-Embed-v2) can embed longer documents in a single pass, reducing the need for aggressive chunking. However, embeddings from very large documents become too general and diluted — optimal chunks are typically much smaller than maximum capacity [24].

### Short vs. Long Text

Models optimized for sentence-level semantics (SBERT variants) work best for short text like JIRA summaries and queries [24]. For longer documents, standard BERT truncates at 512 tokens, while BGE-M3 supports 8,192 tokens and Qwen3 supports 32,000 tokens [24].

### Matryoshka Representation Learning (MRL)

Some models (Nomic Embed, text-embedding-3-large) support MRL, enabling smaller embedding dimensions (e.g., 256 instead of 3072) with maintained performance [24]. This reduces storage and improves query speed — relevant for lightweight deployments.

## Local vs. API Trade-offs

| Factor | Local/Self-Hosted | API-Based |
|---|---|---|
| Cost structure | Hardware + electricity | Per-token pricing |
| Privacy | Full control | Data leaves your network |
| Latency | Depends on hardware | Network + inference |
| Fine-tuning | Full control | Limited/impossible |
| Maintenance | Self-managed | Provider-managed |
| Best for | Large-scale, privacy-sensitive | Rapid prototyping, small workloads |

For a lightweight standalone system where resilience is not critical, local models eliminate API dependency and recurring costs. The top self-hostable options are Qwen3-Embedding-8B (Apache 2.0, highest MTEB) and BGE-M3 (MIT license, 100+ languages, multi-paradigm: dense + sparse + multi-vector) [24].

## Recommendations for Heterogeneous Corpora

1. **Start with a general-purpose model** rather than domain-specific — the corpus spans technical docs, operational data, and conversational content
2. **BGE-M3** is a strong default for private/self-hosted RAG: MIT license, 8192-token context, MTEB score 63.0, supports dense + sparse + multi-vector retrieval natively [24]
3. **Qwen3-Embedding-8B** offers highest MTEB scores but requires more compute (8B params) [24]
4. **Build a test set of 100+ real queries** spanning all content types before committing to a model
5. **Consider asymmetric embeddings**: queries are typically short while documents vary in length — models trained with asymmetric objectives may perform better

## Gaps and Limitations

- No benchmark specifically evaluates embedding models on mixed corpora containing markdown + JSON + email + transcripts
- JIRA issue embedding (structured JSON with nested fields) lacks dedicated evaluation
- The optimal approach for embedding structured metadata alongside content text is addressed in the [metadata-enriched retrieval](metadata-enriched-retrieval.md) reference
- MTEB leaderboard data could not be directly extracted (JavaScript-rendered page) — rankings sourced from secondary analysis [24]
