# Indexing Pipeline Architecture

This reference covers dimension 6: practical design for ingesting multiple source formats into a unified index, including parsers, normalization, incremental updates, and schema design.

## Pipeline Architecture

The standard RAG indexing pipeline follows an ETL pattern [36] [41]:

1. **Extract**: Read/parse documents from multiple sources
2. **Transform**: Chunk, enrich with metadata, normalize
3. **Load**: Generate embeddings and store in vector database

Spring AI formalizes this with typed interfaces: DocumentReader, DocumentTransformer, DocumentWriter [41]. AWS describes large-scale patterns integrating with OpenSearch and pgvector [40].

## Multi-Format Document Parsing

### Unstructured Library [14]

Four core capabilities:
1. **Partitioning**: extraction of structured content from raw documents
2. **Cleaning**: sanitizing output, removing unwanted content
3. **Extracting**: isolating relevant information
4. **Chunking**: semantically intelligent splitting using document format understanding

Supports 20+ source connectors and 20+ destination connectors [14]. The open-source version lacks fine-tuned OCR models, by-page/by-similarity chunking, and VLM capabilities [14].

### Format-Specific Parsers

| Format | Parser | Notes |
|---|---|---|
| PDF | pdftotext, Document Intelligence | Layout preservation varies |
| DOCX | pandoc, python-docx | Handles styles and structure |
| Markdown | LangChain MarkdownTextSplitter [33] | Header-based splitting |
| JSON | Custom parsers | Structure-aware field extraction |
| Email (.eml, .msg) | Unstructured [14] | Thread reconstruction needed |
| HTML | BeautifulSoup, lxml | Tag-based structure |
| Transcripts | Custom + speaker detection | Speaker-aware segmentation [28] |

## Pipeline Design for Heterogeneous Sources

For a system ingesting research docs, JIRA, email, meeting notes, and transcripts:

```
Source-specific extractors
    ├── Markdown parser (research docs)
    ├── JSON parser (JIRA issues, calendar metadata)
    ├── Email parser (thread reconstruction)
    ├── Transcript parser (speaker detection)
    └── PDF parser (meeting attachments)
         ↓
Normalization layer
    ├── Common metadata schema
    ├── Temporal normalization
    └── Cross-reference extraction
         ↓
Chunking layer (strategy per type)
    ├── Header-based (markdown)
    ├── Whole-document (JIRA issues)
    ├── Thread-based (email)
    ├── Speaker-based (transcripts)
    └── Fixed-size with overlap (fallback)
         ↓
Embedding generation
         ↓
Vector store + metadata index
```

## Incremental Updates

For a living corpus where JIRA issues change status, new emails arrive, and meetings occur:

- **Content hashing**: hash document content to detect changes; if hash changes, re-process [36]
- **Hybrid update strategy**: incremental updates on change events, full re-index periodically for consistency
- **Idempotent uploads**: use document_id + chunk_id keys to avoid duplicates
- **Batch processing**: ingest 100-1000 vectors at a time for efficiency

## Metadata Schema Design

A unified metadata schema for heterogeneous sources:

```json
{
  "doc_id": "unique-identifier",
  "source_type": "jira|email|markdown|transcript|calendar",
  "title": "Document title or subject",
  "created_at": "ISO-8601 datetime",
  "updated_at": "ISO-8601 datetime",
  "author": "Creator name or email",
  "tags": ["label1", "label2"],
  "parent_id": "Parent document ID (optional)",
  "project": "Project or category",
  "status": "Active status (optional)",
  "source_url": "Original source location",
  "chunk_index": 0,
  "total_chunks": 1
}
```

Source-type-specific fields extend this base schema (e.g., `issue_type` and `priority` for JIRA, `thread_id` for email, `attendees` for meetings).

## Processing Considerations

### JSON Documents (JIRA, Calendar Metadata)

JSON requires flattening or selective field extraction before embedding. Strategies:
- Concatenate key fields into a text representation (summary + description + comments)
- Preserve hierarchical relationships as metadata (parent issue, epic, linked issues)
- Index structured fields (status, priority, assignee) as filterable metadata, not embedded text

### Email

Challenges include quoted text removal, signature stripping, thread reconstruction from In-Reply-To/References headers, and attachment handling. The RAG-Mail approach [32] groups by thread_id and constructs chronological flow documents.

### Meeting Notes + Transcripts

Speaker attribution and temporal markers require preprocessing. Semantic labels (risk, decision, action item) and domain anchors (JIRA ID, project name) should be extracted during indexing for filtered retrieval [37].

## Gaps and Limitations

- No turnkey pipeline handles all heterogeneous types described here — custom integration is required
- Calendar event normalization (recurring events, timezone handling) lacks dedicated tooling
- Cross-document deduplication (same info in JIRA description and meeting notes) is a recognized but unsolved challenge
- Processing throughput benchmarks for heterogeneous ingestion pipelines are limited
- The Unstructured open-source version has significant limitations compared to its commercial offering [14]
