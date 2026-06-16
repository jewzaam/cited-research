# Practical Usage and Integration

## Installation

Three installation methods [2]:

```
pip install ftl-reasons
uv tool install ftl-reasons
uvx ftl-reasons <command>
```

A simpler companion tool is also available: `pip install ftl-beliefs` [17].

## Two CLI Tools

### `beliefs` — Simple Markdown Knowledge Base

Tracks claims with provenance using markdown files (beliefs.md, nogoods.md) [17]. Version 0.2.0, MIT license, 54 downloads/month [17]. Best for independent facts that don't need dependency tracking.

### `reasons` — Full Belief Maintenance System

Full BMS with automatic propagation, cascades, backtracking, and LLM-driven operations [2]. Version 0.47.0, 321 downloads/month [18]. SQLite-backed (reasons.db) [2].

Key commands [2]:

| Category | Commands |
|----------|---------|
| Setup | `init` |
| Add beliefs | `add ID "text"`, `add ID "text" --sl a,b`, `add ID "text" --sl a --unless y` |
| State changes | `retract ID`, `assert ID` |
| Query | `status`, `show ID`, `explain ID`, `search QUERY`, `list`, `trace ID` |
| LLM operations | `derive`, `review-beliefs` |
| Dialectic | `challenge ID "reason"`, `defend TARGET CHALLENGE "reason"` |
| Contradictions | `nogood A B ...` |
| Import/Export | `import-beliefs FILE`, `export`, `export-markdown` |
| Maintenance | `propagate`, `log`, `hash-sources`, `check-stale`, `compact --budget N` |

## Typical Workflow

1. `reasons init` — create SQLite database [2]
2. `reasons add` — add premises from source material [2]
3. `reasons add --sl` — add derived beliefs with SL justification links [2]
4. `reasons derive` — LLM discovers implicit connections [1][2]
5. `reasons review-beliefs` — audit pass; expect 13–37% retraction [1]
6. `reasons export-markdown` — export to human-readable beliefs.md [2]

## Agent Integration Pattern

Agents query the knowledge base before generating answers [1]:

1. `reasons search QUERY` — find relevant beliefs
2. `reasons show ID` — get belief details and justifications
3. `reasons explain ID` — trace why a belief is IN or OUT
4. Agent cites node IDs for auditability
5. `reasons nogood` — record detected contradictions

The "humble generic prompt produces better results because agent consults knowledge base instead of trusting expertise" [1] — the expert prompt paradox.

## Multi-Agent BMS

Agents import beliefs from other agents [1]:
- SL justifications include `agent:active` as antecedent
- Belief remains IN only if originating agent is active AND original justification holds
- Extends truth maintenance across agent boundaries

## Knowledge Base Scale

40+ expert knowledge bases built [1]:

| KB | Beliefs |
|----|---------|
| aap-expert (smallest) | 237 |
| redhat-expert (largest) | 12,731 |

## Public Belief Registry

expert.ftl2.com hosts a public belief registry [19]:
- ~45 visible beliefs in eem-expert KB
- All beliefs marked [IN] (currently justified)
- Two types: OBSERVATION (empirical) and DERIVED (concluded from other beliefs)
- Available in HTML, Markdown, JSON export
- Topic search with 20 indexed topics

## Storage

SQLite database (reasons.db) [2]. The `reasons` CLI manages all database operations. Export to markdown via `export-markdown` for human-readable querying and grep-able access [2].

Dependencies include langchain-anthropic, langchain-google-vertexai, sentence-transformers, scikit-learn, langfuse, mcp [18].

## Test Coverage

211 tests covering [2]:
- Propagation
- Retraction cascades
- Restoration
- Multiple justifications
- Diamond dependencies
- Nogoods and backtracking
- Non-monotonic justifications
- Dialectical argumentation (challenge/defend)

## Gaps and Limitations

1. **Concurrency**: No documented multi-agent collision handling for concurrent access to reasons.db
2. **Performance at scale**: No published benchmarks for large KBs (10K+ beliefs)
3. **Derive algorithm**: Internal mechanics of LLM-driven derivation not documented
4. **Review criteria**: How `review-beliefs` selects beliefs for retraction not specified
