# Retrieval Quality Evaluation

This reference covers dimension 7: how to measure whether RAG retrieval is returning relevant chunks, including metrics, frameworks, and lightweight approaches.

## Evaluation Taxonomy

Evidently AI [19] distinguishes two axes:

| | Reference-Based | Reference-Free |
|---|---|---|
| **Retrieval** | Precision@k, Recall@k, NDCG@k, MRR, MAP | LLM-judged chunk relevance |
| **Generation** | Semantic similarity to ground truth | Faithfulness, completeness, tone |

Reference-free evaluation is preferred for production because it does not require labeled datasets [19].

## Core RAG Metrics

### Retrieval Metrics

| Metric | What It Measures | Formula |
|---|---|---|
| Precision@k | Fraction of top-k results that are relevant | relevant_in_k / k |
| Recall@k | Fraction of all relevant items found in top-k | relevant_in_k / total_relevant |
| Hit Rate | Binary: did at least one relevant item appear? | 0 or 1 |
| MRR | Average rank of first relevant result | 1/rank (averaged) |
| NDCG@k | Ranking quality with position-based discounting | DCG/ideal_DCG |
| MAP | Average precision across queries | mean of AP per query |

### Generation Metrics

| Metric | What It Measures | Ground Truth Needed? |
|---|---|---|
| Faithfulness | Does the answer contradict or invent beyond context? | No [3] |
| Answer Relevancy | Does the response address the question? | No [3] |
| Context Precision | Are relevant chunks ranked higher? | Depends on implementation |
| Context Recall | Does context contain all required information? | Yes (reference answer) [3] |
| Answer Correctness | Factual accuracy against reference | Yes |

## Evaluation Frameworks

### RAGAS [3]

Reference-free evaluation of RAG pipelines. Assesses retrieval quality (context relevance), LLM faithfulness, and generation quality without requiring human annotations. Includes synthetic test set generation using an evolutionary paradigm for question complexity.

**Limitation:** RAGAS Faithfulness failed for 83.5% of examples on FinanceBench [26]. The improved RAGAS++ variant reduced failures to near 0% [26].

### ARES [17]

Automated RAG Evaluation System (NAACL 2024). Finetunes lightweight language model judges using synthetically generated training data. Uses prediction-powered inference (PPI) with a small set of human-annotated datapoints. Evaluated across 8 knowledge-intensive tasks in KILT, SuperGLUE, and AIS using only a few hundred human annotations [17].

### Luna [18]

Evaluation foundation model (DeBERTA-large, 440M params) fine-tuned for hallucination detection. Achieves 97% cost reduction and 91% latency reduction vs. GPT-3.5 [18]. Outperforms GPT-3.5 on hallucination detection and generalizes across multiple industry verticals [18].

### Framework Comparison

| Framework | Approach | Ground Truth? | Cost |
|---|---|---|---|
| RAGAS | LLM-as-judge | No (reference-free) | LLM API calls |
| ARES | Finetuned classifier | Small labeled set | Training + inference |
| Luna | Finetuned DeBERTA | No | Low (local model) |
| TruLens | Feedback functions | No | LLM API calls |
| DeepEval | Pytest-style | Optional | LLM API calls |

TruLens achieved the highest discrimination ratio (4.2:1 correct to inverted judgments) in a comparative study [38]. WandB, TruLens, and RAGAS all achieved >94% Top-1 Accuracy under standard conditions [38].

## Hallucination Detection

Cleanlab's benchmarking study [26] compared five detection methods across four datasets (FinanceBench, PubMedQA, DROP, CovidQA):

- **TLM** (Trustworthy Language Model): consistently outperformed all others
- **RAGAS Faithfulness**: moderately effective for simple search-like queries but not complex ones [26]
- **RAGAS Answer Relevancy**: mostly ineffective — hallucinated responses remained relevant to queries [26]
- **LLM Self-Evaluation**: secondary performance
- **AUROC** used as primary evaluation metric [26]

## LLM-as-Judge

The RAG Triad evaluates three dimensions with LLM judges [35]:
1. Context relevance
2. Groundedness/faithfulness
3. Answer relevance

Cohen Kappa agreement with human annotators ranges from high moderate to substantial [35].

## Synthetic Test Data

For evaluation without large labeled datasets:
- RAGAS uses evolutionary generation for question complexity [3]
- Recommended dataset size: 50 questions minimum for stable metrics, 200-500 for regression tests [3]
- Use a different LLM for dataset creation than RAG generation to avoid self-enhancement bias
- Synthetic data suitable for retriever parameter tuning but limited reliability for generator evaluation

## Lightweight Evaluation Strategy

For a standalone system without production-grade evaluation infrastructure:

1. **Create a test set**: 50-100 real queries spanning all content types with expected relevant documents
2. **Measure Hit Rate@10 and MRR**: cheap to compute, no LLM calls needed
3. **Spot-check faithfulness**: use RAGAS or Luna on a subset of responses
4. **Iterate on chunking and retrieval**: change one variable at a time, re-measure

## Gaps and Limitations

- No evaluation framework specifically handles heterogeneous corpora (mixed content types with different relevance criteria)
- Cross-document type evaluation (did the system correctly retrieve a JIRA issue when the query was about a meeting?) lacks benchmarks
- Temporal relevance evaluation (did the system prefer recent JIRA updates over stale ones?) is not addressed by standard metrics
- RAGAS Faithfulness has known reliability issues on complex domains [26]
- Snowflake's LLM-as-judge benchmarking data could not be fully extracted due to page rendering issues [35]
