# Chunking Strategies for Heterogeneous Document Types

This reference covers dimension 1: how to chunk markdown prose, structured JSON, email threads, meeting transcripts, and calendar metadata differently for RAG retrieval.

## Strategy Taxonomy

Microsoft Azure Architecture Center [12] provides a comprehensive taxonomy of chunking approaches organized by document structure:

| Document Type | Structure Level | Recommended Approach |
|---|---|---|
| Forms (W-2, insurance cards) | Structured | Prebuilt/custom models |
| Invoices, web pages, markdown | Semi-structured | Document analysis models |
| Legal documents, regulations | Inferred | Custom code |
| Emails, notes, transcripts | Unstructured | Sentence-based or fixed-size with overlap |

## Chunk Size and Overlap

### Optimal Size

NVIDIA's FinanceBench evaluation [13] tested chunk sizes from 128 to 2048 tokens:

| Chunk Size | Accuracy |
|---|---|
| 1024 tokens | 0.579 (best) |
| Page-level | 0.566 |
| 2048 tokens | 0.506 |

The relationship is non-linear — larger chunks do not consistently improve results [13]. A sweet spot exists around 512-1024 tokens for analytical queries requiring broader context [13].

### Overlap

**Sources disagree on overlap effectiveness.** Findings are contradictory:

- NVIDIA found 15% overlap performed best with 1024-token chunks on FinanceBench [13]
- Microsoft Azure recommends 25% overlap (128 tokens for 512-token chunks) if retrieval recall is low [12]
- Bennani & Moslonka (2026) found overlap provides **no measurable benefit** with SPLADE retrieval and increases indexing cost [5]

The discrepancy likely reflects retrieval method dependence: overlap benefits dense retrieval more than sparse retrieval [5].

### Context Cliff

A systematic analysis found quality degrades beyond approximately 2.5k tokens — a "context cliff" where embedding quality drops sharply rather than gradually [5]. Sentence chunking matches semantic chunking performance up to ~5k tokens [5].

## Strategy Comparisons

### Recursive Character Splitting

Scored 69% accuracy on the FloTorch benchmark of 50 academic papers [29]. Recommended as the safest default strategy across multiple sources [12] [29]. Weaviate reports 85-90% recall at 400 tokens [31].

### Semantic Chunking

Achieved 91.9% recall in Chroma's evaluation but only 54% end-to-end accuracy in FloTorch [29]. The disconnect is due to semantic chunking producing fragments averaging only 43 tokens — too small for effective LLM generation [29]. Weaviate reports 91-92% recall [31].

### Agentic Chunking

An LLM processes each sentence and allocates to existing or new chunks based on content analysis. MoRA-RAG achieved 94.5% accuracy, a 4% improvement over fixed-token methods [30]. The trade-off: an LLM call per sentence creates prohibitive latency and cost at scale.

### Adaptive Chunking

The Adaptive Chunking framework [4] automatically selects optimal strategies per document using five intrinsic metrics:

1. References Completeness (RC)
2. Intrachunk Cohesion (ICC)
3. Document Contextual Coherence (DCC)
4. Block Integrity (BI)
5. Size Compliance (SC)

This improved answer correctness from 62-64% to 72% and increased successfully answered questions by 30% [4].

## Document-Type-Specific Strategies

### Markdown Research Documents

LangChain's MarkdownTextSplitter uses headers (#, ##, ###) as natural breakpoints, preserving logical structure and associating header metadata with each chunk [33]. This is a form of structure-aware chunking that outperforms naive splitting for well-organized documents.

### JSON (JIRA Issues, Metadata)

Microsoft Azure describes structure-aware chunking for JSON that leverages document format to create meaningful chunks from text, table, and list blocks [12]. For JIRA issues specifically, individual tickets may not require chunking if already context-coherent — the focus shifts to relationship modeling rather than splitting.

### Email Threads

The RAG-Mail project demonstrates thread-aware processing: grouping by thread_id, constructing chronological flow, and chunking at ~1800 characters (~512 tokens) [32]. Email should not be chunked at the individual message level but at the conversation level [32]. Challenges include handling quoted text, signatures, and thread forks.

### Meeting Transcripts

Cohere recommends speaker-aware chunking: segmenting whenever a new speaker begins, using unique delimiters (###) to mark speaker changes [28]. Chunk sizes should be larger (1000+ characters) to keep complete speeches intact [28]. Content-dependent strategies outperform content-independent ones for transcripts because they maintain speaker attribution [28].

### Calendar Events

No dedicated research was found on calendar event chunking. Calendar events are typically short enough to be treated as individual chunks, with rich metadata (title, description, attendees, time, recurrence) attached as filterable fields rather than embedded in the text.

## Advanced Techniques

### Late Chunking

Apply the transformer layer to the entire text first, then chunk — leveraging long context windows in modern embedding models (8192+ tokens) [45]. This preserves cross-chunk context that traditional chunk-then-embed approaches lose. Trade-off: requires long-context embedding models [16].

### Parent-Child Chunking

Small child chunks (100-500 tokens) for precise vector similarity search, large parent chunks (500-2000 tokens) returned for context-rich LLM responses [27]. Typical gains of +20-35% relevance on structured documents. LangChain's ParentDocumentRetriever and LlamaIndex's recursive retrieval both support this pattern.

### Auto-Merging

Haystack's AutoMergingRetriever creates hierarchical document trees; if 60%+ of matched leaf chunks belong to the same parent, the parent is returned instead [27]. Testing on BBC news articles consolidated 10 retrieved documents into 7, merging redundant leaves into 3 parents [27].

## Gaps and Limitations

- No peer-reviewed research specifically compares chunking strategies across all heterogeneous types (markdown + JSON + email + transcript) in a single evaluation
- Calendar event chunking lacks dedicated study
- Optimal chunk sizes for JIRA JSON structures remain empirically untested
- The overlap debate (helpful vs. wasteful) depends on retrieval method and is not settled
- Cross-document reference handling during chunking (e.g., a markdown doc citing a JIRA issue) is not addressed by current chunking frameworks
