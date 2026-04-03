# Metadata-Enriched Retrieval

This reference covers dimension 3: using structured metadata (dates, issue types, relationships, tags, authors) as retrieval filters or re-ranking signals alongside vector similarity.

## Metadata Integration Strategies

A systematic comparison [6] identified four approaches to incorporating metadata into RAG retrieval:

| Strategy | Method | Performance |
|---|---|---|
| Metadata-as-Text (prefix) | Prepend metadata fields to chunk text before embedding | Consistently outperforms plain-text baselines [6] |
| Metadata-as-Text (suffix) | Append metadata after chunk text | Similar to prefix [6] |
| Unified Embedding | Dual-encoder fuses metadata and content into single index | Matches or exceeds prefix, easier maintenance [6] |
| Late-Fusion | Separate metadata and content encoders, combined at retrieval | Less consistent [6] |
| Query Reformulation | Rewrite queries to incorporate metadata awareness | Variable [6] |

## Why Metadata Improves Retrieval

Metadata integration via embedding space analysis shows [6]:
- **Increased intra-document cohesion**: related chunks cluster more tightly
- **Reduced inter-document confusion**: prevents mixing of similar but unrelated documents
- **Wider relevant/irrelevant separation**: structural cues provide strong disambiguating signals

This is particularly valuable for structured corpora where overlapping language is common (e.g., JIRA issues with similar templates, meeting notes with recurring agenda items) [6].

## Contextual Chunks

Embedding metadata directly with text produces the most significant performance gains [7]. Anthropic's contextual retrieval prepends 50-100 tokens of context to each chunk, reducing retrieval failure by 35% for embeddings alone and 49% combined with BM25 [1].

## Structured Metadata in RAG (SRAG)

The SRAG approach [8] enriches both queries and chunks with five structural elements:
- Topics and sentiments
- Query/chunk type classifications (informational, quantitative)
- Knowledge graph triples
- Semantic tags

This achieved a 30% improvement in QA scoring (p-value = 2e-13) [8], with particular effectiveness on comparative, analytical, and predictive questions.

## Pre-Filtering vs. Post-Filtering

| Approach | When to Use | Trade-off |
|---|---|---|
| Pre-filtering | Narrow search space before vector similarity | Faster but may exclude relevant edge cases |
| Post-filtering | Apply metadata constraints after retrieval | More complete but slower |
| Hybrid | Broad pre-filter + fine post-filter | Best accuracy, moderate complexity |

Pre-filtering dominates in practice because it reduces the vector search space, improving both speed and relevance [22].

## Metadata Fields for Heterogeneous Corpora

For a corpus spanning research docs, JIRA issues, email, meeting notes, and transcripts, consider these metadata dimensions:

| Field | Type | Purpose |
|---|---|---|
| `source_type` | categorical | Filter by content type (markdown, json, email, transcript) |
| `created_date` | datetime | Temporal filtering and recency weighting |
| `author` | string | Filter by creator/contributor |
| `tags`/`labels` | array | Topic-based filtering |
| `parent_id` | string | Link to parent document (JIRA epic, email thread) |
| `project`/`category` | string | Organizational grouping |
| `status` | string | Filter by lifecycle state (JIRA status, email read/unread) |

## Temporal Metadata

Date range filtering is critical for operational data where recency matters (recent JIRA activity, recent meetings) vs. research documents where currency is less volatile. Normalizing temporal metadata across sources is a practical challenge: JIRA has created/updated timestamps, emails have sent/received dates, transcripts have recording dates, markdown docs have file modification times.

## Gaps and Limitations

- No unified metadata schema standard exists for heterogeneous RAG corpora
- Temporal metadata normalization across heterogeneous sources lacks dedicated research
- The optimal number of metadata fields before retrieval performance degrades is not established
- JIRA-specific metadata patterns (status transitions, issue links, sprint associations) are not addressed in current RAG metadata research
- Meeting transcript metadata extraction (attendees, topics, decisions) requires NLP preprocessing not covered by standard chunking tools
