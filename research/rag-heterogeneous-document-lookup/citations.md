# Citations

All sources accessed during research session on 2026-04-02.

## [1] Anthropic. "Introducing Contextual Retrieval." Anthropic News, 2024.
- **URL:** https://www.anthropic.com/news/contextual-retrieval
- **Tier:** 1 (Official vendor research publication)
- **Data extracted:** Contextual retrieval failure rate reductions (35%, 49%, 67%), cost ($1.02/M tokens), chunk size (800 tokens), reranking pool (150→20), evaluation metric (1 - recall@20)
- **Access:** OK

## [2] Sarthi, P., Abdullah, S., Tuli, A., Khanna, S., Goldie, A., Manning, C.D. "RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval." ICLR 2024.
- **URL:** https://arxiv.org/abs/2401.18059
- **Tier:** 1 (Peer-reviewed, ICLR)
- **Data extracted:** 20% absolute accuracy improvement on QuALITY benchmark with GPT-4, recursive clustering methodology
- **Access:** OK (abstract only; full paper behind PDF)

## [3] Es, S., James, J., Espinosa-Anke, L., Schockaert, S. "RAGAS: Automated Evaluation of Retrieval Augmented Generation." arXiv:2309.15217.
- **URL:** https://arxiv.org/abs/2309.15217
- **Tier:** 1 (Peer-reviewed)
- **Data extracted:** Reference-free RAG evaluation framework, metric definitions (faithfulness, context precision/recall, answer relevancy)
- **Access:** OK (abstract only)

## [4] Adaptive Chunking Framework. arXiv:2603.25333, March 2026.
- **URL:** https://arxiv.org/abs/2603.25333
- **Tier:** 1 (Peer-reviewed)
- **Data extracted:** Five intrinsic metrics (RC, ICC, DCC, BI, SC), correctness improvement 62-64% → 72%, answered questions +30%
- **Access:** OK

## [5] Bennani, M., Moslonka, C. "Systematic Chunking Analysis." arXiv:2601.14123, January 2026.
- **URL:** https://arxiv.org/abs/2601.14123
- **Tier:** 1 (Peer-reviewed)
- **Data extracted:** Overlap provides no measurable benefit with SPLADE, sentence chunking matches semantic up to ~5k tokens, context cliff at ~2.5k tokens
- **Access:** OK

## [6] Metadata Utilization in RAG. arXiv:2601.11863, January 2026.
- **URL:** https://arxiv.org/abs/2601.11863
- **Tier:** 1 (Peer-reviewed)
- **Data extracted:** Four metadata strategies compared, prefixing and unified embeddings outperform baselines, RAGMATE-10K dataset
- **Access:** OK

## [7] Metadata-Driven RAG for Financial QA. arXiv:2510.24402.
- **URL:** https://arxiv.org/abs/2510.24402
- **Tier:** 1 (Peer-reviewed)
- **Data extracted:** Contextual chunks produce most significant gains, reranker essential for precision, custom metadata reranker as cost-effective alternative
- **Access:** OK

## [8] Shah, S., Ryali, S., Venkatesh, R. "SRAG: Structured RAG." arXiv:2603.26670, January 2026.
- **URL:** https://arxiv.org/abs/2603.26670
- **Tier:** 1 (Peer-reviewed)
- **Data extracted:** 30% QA improvement (p-value=2e-13), structured metadata components (topics, sentiments, KG triples, semantic tags)
- **Access:** OK

## [9] Liu, H., Wang, Z., Chen, X. et al. "HopRAG: Multi-Hop Reasoning for Logic-Aware RAG." arXiv:2502.12442, February 2025.
- **URL:** https://arxiv.org/abs/2502.12442
- **Tier:** 1 (Peer-reviewed)
- **Data extracted:** Passage graph with LLM-generated pseudo-queries as edges, retrieve-reason-prune mechanism
- **Access:** OK (abstract; specific accuracy claim not confirmed in abstract)
- **Caveat:** The 76.78% improvement claim from discovery was not verified in the abstract

## [10] Tang, Y. et al. "MultiHop-RAG: Benchmarking Retrieval-Augmented Generation for Multi-Hop Queries." COLM 2024.
- **URL:** https://arxiv.org/abs/2401.15391
- **Tier:** 1 (Peer-reviewed)
- **Data extracted:** Benchmark with knowledge base of English news articles, existing RAG methods perform unsatisfactorily on multi-hop queries
- **Access:** OK (abstract only)

## [11] Microsoft. "Hybrid Search Scoring (RRF) - Azure AI Search." Microsoft Learn.
- **URL:** https://learn.microsoft.com/en-us/azure/search/hybrid-search-ranking
- **Tier:** 1 (Official documentation)
- **Data extracted:** RRF formula: 1/(rank + k), k=60 default, parallel query execution, vector weighting support
- **Access:** OK

## [12] Microsoft. "Develop a RAG Solution - Chunking Phase." Azure Architecture Center.
- **URL:** https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-chunking-phase
- **Tier:** 1 (Official documentation)
- **Data extracted:** Chunking approach taxonomy (fixed-size, semantic, custom code, LLM augmentation, document layout analysis, graph-based), document structure categories, overlap guidance
- **Access:** OK

## [13] NVIDIA. "Finding the Best Chunking Strategy for Accurate AI Responses." NVIDIA Developer Blog.
- **URL:** https://developer.nvidia.com/blog/finding-the-best-chunking-strategy-for-accurate-ai-responses/
- **Tier:** 2 (Manufacturer blog)
- **Data extracted:** FinanceBench: 1024 tokens = 0.579 accuracy (best), 2048 = 0.506, page-level = 0.566, 15% overlap optimal
- **Access:** OK

## [14] Unstructured.io. "Open Source Introduction/Overview." Unstructured Documentation.
- **URL:** https://docs.unstructured.io/open-source/introduction/overview
- **Tier:** 1 (Official documentation)
- **Data extracted:** Four capabilities (partitioning, cleaning, extracting, chunking), 20+ source/destination connectors, open source limitations
- **Access:** OK

## [15] Microsoft. "GraphRAG." Microsoft Research.
- **URL:** https://microsoft.github.io/graphrag/
- **Tier:** 1 (Official documentation)
- **Data extracted:** Architecture (TextUnits → entity extraction → Leiden clustering → community summarization), search modes (Global, Local, DRIFT, Basic)
- **Access:** OK

## [16] Merola, A., Singh, R. "Contextual Retrieval vs Late Chunking." arXiv:2504.19754, April 2025.
- **URL:** https://arxiv.org/abs/2504.19754
- **Tier:** 1 (Peer-reviewed)
- **Data extracted:** Contextual retrieval preserves semantic coherence but high compute; late chunking offers efficiency but sacrifices relevance
- **Access:** OK (abstract only)

## [17] Saad-Falcon, J. et al. "ARES: An Automated RAG Evaluation System." NAACL 2024.
- **URL:** https://arxiv.org/abs/2311.09476
- **Tier:** 1 (Peer-reviewed, NAACL)
- **Data extracted:** Finetuned lightweight LM judges, synthetic training data, PPI, evaluated across KILT/SuperGLUE/AIS, few hundred human annotations
- **Access:** OK (abstract only)

## [18] Ravi, S. et al. "Luna: An Evaluation Foundation Model to Catch Language Model Hallucinations." arXiv:2406.00975.
- **URL:** https://arxiv.org/abs/2406.00975
- **Tier:** 1 (Peer-reviewed)
- **Data extracted:** DeBERTA-large (440M params), 97% cost reduction, 91% latency reduction vs GPT-3.5, generalizes across verticals
- **Access:** OK

## [19] Evidently AI. "RAG Evaluation." Evidently AI LLM Guide.
- **URL:** https://www.evidentlyai.com/llm-guide/rag-evaluation
- **Tier:** 2 (Established MLOps company)
- **Data extracted:** Reference-free vs reference-based taxonomy, retrieval metrics (Precision@k, Recall@k, Hit Rate, NDCG@k), generation metrics (faithfulness, completeness), evaluation best practices
- **Access:** OK

## [20] Hybrid RAG benchmark study. AIMultiple Research.
- **URL:** https://aimultiple.com/hybrid-rag
- **Tier:** 2 (Industry research)
- **Data extracted:** MRR 0.410→0.486 (+18.5%), Recall@5 0.655→0.702 (+7.2%), latency +201ms (+24.5%), dataset 494K Amazon reviews, Qdrant dual vector storage
- **Access:** OK

## [21] Prem.ai. "Hybrid Search for RAG: BM25, SPLADE, and Vector Search Combined."
- **URL:** https://blog.premai.io/hybrid-search-for-rag-bm25-splade-and-vector-search-combined/
- **Tier:** 2 (Industry blog with benchmarks)
- **Data extracted:** SPLADE vs BM25 comparison, fusion strategies (RRF, convex combination, DBSF), alpha guidance (~0.3 technical, ~0.7 conversational), BEIR aggregates (+26-31% NDCG)
- **Access:** OK

## [22] Redis. "Full-Text Search for RAG: The Precision Layer."
- **URL:** https://redis.io/blog/full-text-search-for-rag-the-precision-layer/
- **Tier:** 2 (Official vendor blog)
- **Data extracted:** When BM25 outperforms semantic search (exact identifiers, technical content, protocol queries), precision layer concept, three integration patterns, citation anchoring
- **Access:** OK

## [23] SQLite.ai. "Building a RAG on SQLite."
- **URL:** https://blog.sqlite.ai/building-a-rag-on-sqlite
- **Tier:** 2 (Official documentation)
- **Data extracted:** SQLite-Vector + SQLite-AI extensions, FTS5 hybrid search via RRF, ~370ms query response, ~100MB memory, Gemma Embedding 300M Q8
- **Access:** OK

## [24] Prem.ai. "Best Embedding Models for RAG 2026."
- **URL:** https://blog.premai.io/best-embedding-models-for-rag-2026-ranked-by-mteb-score-cost-and-self-hosting/
- **Tier:** 2 (Industry blog with benchmarks)
- **Data extracted:** Top models: Qwen3-Embedding-8B (70.58), Gemini Embedding-001 (68.32), NV-Embed-v2 (69.32), voyage-3-large (~67+), text-embedding-3-large (64.6), with cost/context/dimensions
- **Access:** OK

## [25] Encore.dev. "Best Vector Databases." 2026.
- **URL:** https://encore.dev/articles/best-vector-databases
- **Tier:** 2 (Technical comparison)
- **Data extracted:** Database comparison (pgvector, Pinecone, Qdrant, Milvus, Chroma, LanceDB) with latency, scaling, cost, deployment characteristics
- **Access:** OK

## [26] Cleanlab. "RAG TLM Hallucination Benchmarking."
- **URL:** https://cleanlab.ai/blog/rag-tlm-hallucination-benchmarking/
- **Tier:** 2 (ML company benchmark)
- **Data extracted:** TLM outperforms RAGAS Faithfulness across 4 datasets, RAGAS Faithfulness failed 83.5% on FinanceBench, RAGAS++ reduced to near 0%, AUROC primary metric
- **Access:** OK

## [27] Haystack (deepset). "Improve Retrieval with Auto-Merging."
- **URL:** https://haystack.deepset.ai/blog/improve-retrieval-with-auto-merging
- **Tier:** 2 (Official framework blog)
- **Data extracted:** Auto-merging algorithm, HierarchicalDocumentSplitter, AutoMergingRetriever with threshold (0.6), BBC news test results
- **Access:** OK

## [28] Cohere. "Chunking Strategies." Cohere Documentation.
- **URL:** https://docs.cohere.com/v2/page/chunking-strategies
- **Tier:** 2 (Official documentation)
- **Data extracted:** Speaker-aware chunking for transcripts, ### delimiter approach, 1000+ char chunk sizes for speeches, content-dependent outperforms content-independent
- **Access:** OK

## [29] Prem.ai. "RAG Chunking Strategies: The 2026 Benchmark Guide."
- **URL:** https://blog.premai.io/rag-chunking-strategies-the-2026-benchmark-guide/
- **Tier:** 3 (Industry blog with benchmarks)
- **Data extracted:** Recursive splitting 69% accuracy FloTorch, semantic chunking 91.9% Chroma recall but 54% FloTorch accuracy, 43-token average fragment issue
- **Access:** Cited from discovery (not directly fetched)

## [30] MoRA-RAG Framework. arXiv:2511.14010.
- **URL:** https://arxiv.org/abs/2511.14010
- **Tier:** 1 (Peer-reviewed)
- **Data extracted:** Agentic chunking 94.5% accuracy, 4% improvement over fixed-token methods
- **Access:** Cited from discovery (not directly fetched)

## [31] Weaviate. "Chunking Strategies for RAG."
- **URL:** https://weaviate.io/blog/chunking-strategies-for-rag
- **Tier:** 3 (Vendor blog)
- **Data extracted:** Recursive 85-90% recall at 400 tokens, semantic 91-92% recall
- **Access:** Cited from discovery (not directly fetched)

## [32] RAG-Mail. GitHub Repository.
- **URL:** https://github.com/ManiAm/RAG-Mail
- **Tier:** 4 (GitHub project)
- **Data extracted:** Thread-aware email processing, 1800 char chunks (~512 tokens), thread_id grouping, bge-m3 8192-token context
- **Access:** Cited from discovery (not directly fetched)

## [33] LangChain. "MarkdownTextSplitter." LangChain Documentation.
- **URL:** https://docs.langchain.com/oss/python/integrations/splitters/markdown_header_metadata_splitter
- **Tier:** 1 (Official documentation)
- **Data extracted:** Header-based splitting at H1/H2/H3 boundaries, metadata preservation
- **Access:** Cited from discovery (not directly fetched)

## [34] Superlinked. "Optimizing RAG with Hybrid Search & Reranking."
- **URL:** https://superlinked.com/vectorhub/articles/optimizing-rag-with-hybrid-search-reranking
- **Tier:** 2 (Technical analysis)
- **Data extracted:** H=(1−α)K+αV formula, qualitative comparison of semantic vs hybrid on name/location queries
- **Access:** OK (no quantitative cascade accuracy data found)

## [35] Snowflake. "Benchmarking LLM-as-a-Judge for the RAG Triad Metrics."
- **URL:** https://www.snowflake.com/en/engineering-blog/benchmarking-LLM-as-a-judge-RAG-triad-metrics/
- **Tier:** 2 (Engineering blog)
- **Data extracted:** Cohen Kappa agreement with human annotators (high moderate to substantial)
- **Access:** PARTIAL (CSS only, substantive content not extracted)

## [36] LakeFS. "What is a RAG Pipeline?"
- **URL:** https://lakefs.io/blog/what-is-rag-pipeline/
- **Tier:** 2 (Technical blog)
- **Data extracted:** Three-stage pipeline (loading, splitting, embedding), ETL framework
- **Access:** Cited from discovery (not directly fetched)

## [37] Withluna.ai. "Contextual RAG for Product Meeting Notes and Slack."
- **URL:** https://withluna.ai/blog/contextual-rag-product-meeting-notes-slack
- **Tier:** 2 (Case study)
- **Data extracted:** Semantic labeling (risk, decision), domain anchor extraction (JIRA ID, launch name)
- **Access:** Cited from discovery (not directly fetched)

## [38] AIMultiple. "RAG Evaluation Tools."
- **URL:** https://aimultiple.com/rag-evaluation-tools (redirected from research.aimultiple.com)
- **Tier:** 2 (Industry analysis)
- **Data extracted:** WandB, TruLens, RAGAS >94% Top-1 Accuracy; TruLens discrimination ratio 4.2:1
- **Access:** Cited from discovery (not directly fetched)

## [39] Paperclipped. "Graph RAG in Production."
- **URL:** https://www.paperclipped.de/en/blog/graph-rag-production/
- **Tier:** 3 (Production comparison)
- **Data extracted:** Microsoft GraphRAG $50-200 for 500 pages, LightRAG $0.50, traditional vector RAG under $5
- **Access:** Cited from discovery (not directly fetched)

## [40] AWS. "Build a RAG Data Ingestion Pipeline for Large-Scale ML Workloads."
- **URL:** https://aws.amazon.com/blogs/big-data/build-a-rag-data-ingestion-pipeline-for-large-scale-ml-workloads/
- **Tier:** 1 (Official AWS documentation)
- **Data extracted:** Large-scale ingestion patterns, vector store integration (OpenSearch, pgvector)
- **Access:** Cited from discovery (not directly fetched)

## [41] Spring AI. "ETL Pipeline." Spring AI Documentation.
- **URL:** https://docs.spring.io/spring-ai/reference/api/etl-pipeline.html
- **Tier:** 1 (Official documentation)
- **Data extracted:** ETL component interfaces (DocumentReader, DocumentTransformer, DocumentWriter)
- **Access:** Cited from discovery (not directly fetched)

## [42] NVIDIA. "How Using a Reranking Microservice Can Improve Accuracy and Costs."
- **URL:** https://developer.nvidia.com/blog/how-using-a-reranking-microservice-can-improve-accuracy-and-costs-of-information-retrieval/
- **Tier:** 2 (Manufacturer blog)
- **Data extracted:** 35% hallucination reduction, 10-25% accuracy improvement
- **Access:** Cited from discovery (not directly fetched)

## [43] Databricks. "Vector Search Best Practices."
- **URL:** https://docs.databricks.com/aws/en/vector-search/vector-search-best-practices
- **Tier:** 2 (Official documentation)
- **Data extracted:** Dimensionality reduction 2x = 1.5x QPS, 20% latency reduction
- **Access:** Cited from discovery (not directly fetched)

## [44] OpenSearch. "Introducing Reciprocal Rank Fusion Hybrid Search."
- **URL:** https://opensearch.org/blog/introducing-reciprocal-rank-fusion-hybrid-search/
- **Tier:** 1 (Official documentation)
- **Data extracted:** RRF algorithm specification
- **Access:** Cited from discovery (not directly fetched)

## [45] Jina AI. "Late Chunking in Long-Context Embedding Models."
- **URL:** https://jina.ai/news/late-chunking-in-long-context-embedding-models/
- **Tier:** 3 (Vendor blog)
- **Data extracted:** Late chunking methodology, 8192+ token context windows
- **Access:** Cited from discovery (not directly fetched)

## [46] Cai, D. et al. "ColBERT: Efficient and Effective Passage Search." SIGIR 2020.
- **URL:** https://arxiv.org/abs/2004.12832
- **Tier:** 1 (Peer-reviewed, SIGIR)
- **Data extracted:** Late interaction architecture, MaxSim operators, 2 orders of magnitude faster than BERT re-rankers, 4 orders fewer FLOPs
- **Access:** Cited from discovery (not directly fetched)

## [47] Formal, T. et al. "SPLADE: Sparse Lexical and Expansion Model for First Stage Ranking." SIGIR 2021.
- **URL:** https://arxiv.org/abs/2107.05720
- **Tier:** 1 (Peer-reviewed, SIGIR)
- **Data extracted:** Learned sparse retrieval algorithm specification
- **Access:** Cited from discovery (not directly fetched)
