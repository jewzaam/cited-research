# Alternatives Comparison

## Dimension Coverage

This reference compares Obsidian with Logseq, Notion API, and plain Markdown + static site generators for the use case of machine-writable, human-readable documentation surface.

For source details, see [citations.md](../citations.md).

## Comparison Matrix

| Capability | Obsidian | Logseq | Notion | Plain MD + SSG |
|---|---|---|---|---|
| **Storage** | Local files [7] | Local files [31] | Cloud database [21] | Local files |
| **File format** | Markdown [7] | Markdown/org-mode [31] | Proprietary (JSON API) [21] | Markdown |
| **CLI** | Yes (v1.12+, 80+ commands) [1] | Yes (@logseq/cli) [29] | No native CLI | N/A (shell tools) |
| **REST API** | Plugin (obsidian-local-rest-api) [6] | Plugin API [30] | Official REST API [21] | N/A |
| **Rate limits** | None documented [6] | None documented [29] | 3 req/s average [21] | N/A |
| **Offline** | Full [7] | Full [31] | Limited | Full |
| **Open source** | No (free, not OSS) | Yes (AGPL) [31] | No | Varies |
| **Query language** | Dataview DQL [7] | Built-in queries [31] | Database filters [21] | N/A |
| **Collaboration** | Limited | Limited | Strong [31] | Git-based |
| **Mobile** | Yes | Yes [31] | Yes | Reader only |
| **Plugin ecosystem** | 1500+ plugins | 150+ plugins [31] | Integrations via API | Varies |

## Obsidian

### Strengths for PA Integration
- Plain markdown files enable direct filesystem access — zero API overhead [7]
- CLI (80+ commands) for programmatic operations when Obsidian is running [1]
- REST API plugin for CRUD + surgical edits + Dataview queries [6]
- Dataview renders live dashboards from PA-written frontmatter [7][8]
- Canvas files are plain JSON, writable programmatically [14]
- Git-backed sync works naturally with the PA's existing git workflow [17]

### Weaknesses
- CLI and REST API require Obsidian to be running [1][6]
- No auto-reload of externally modified files [19]
- Not open source — plugin ecosystem is the extensibility mechanism
- Key integrations (REST API, Dataview, Templater) are community plugins with no guaranteed maintenance

## Logseq

### Strengths
- Open source (AGPL) [31]
- Block-based architecture with powerful built-in query language [31]
- Official CLI (`@logseq/cli`) for CI/CD: query, export, import, MCP server [29]
- Child blocks inherit parent tags — sophisticated automated filtering [31]
- Plugin API with modules for App, Editor, DB, Git, UI, Assets, FileStorage [30]

### Weaknesses
- Cannot re-index graphs via CLI — headless operation is limited [29]
- Block-based format adds complexity for machine writing (indentation-sensitive)
- Smaller plugin ecosystem (150+ vs Obsidian's 1500+) [31]
- Third-party CLI (`lsq`) needed for fast terminal operations [29]

## Notion

### Strengths
- Official, well-documented REST API [21]
- Strong team collaboration features [31]
- Hundreds of integrations via Zapier and official API [31]

### Weaknesses
- **Rate limits:** 3 requests/second average, HTTP 429 with Retry-After [21]
- **Size limits:** 1000 blocks/request, 500KB payload, 2000 char rich text, 100 elements per array [21]
- Cloud-only — no offline access to data [31]
- No local file access — all operations require API calls [21]
- JSON response parsing overhead for every operation [21]
- Data must be exported before use with LLMs [31]
- Not suitable for a PA that needs fast, frequent, offline-capable writes

## Plain Markdown + Static Site Generators

### Strengths
- Maximum portability — files work with any tool
- Git diffs work perfectly for tracking changes
- MkDocs: fast, simple, single YAML config [32]
- Material for MkDocs: Git integration plugins, automated deployment [33]
- Zero runtime dependency — no app needs to be running
- LLMs understand Markdown natively [31]

### Weaknesses
- No live query/dashboard capability (static rendering only)
- No interactive features (task checking, canvas, graph view)
- No plugin ecosystem for knowledge management
- Search requires building a search index at build time
- No URI scheme or command integration

## Decision Framework

For a CLI-first PA writing documentation programmatically:

| Requirement | Best Fit |
|---|---|
| PA writes files without any app running | Obsidian or Plain MD (both use local files) |
| Live dashboards from structured data | Obsidian (Dataview) |
| Visual task boards | Obsidian (Canvas) |
| REST API for surgical edits | Obsidian (REST API plugin) |
| No vendor lock-in | Logseq (open source) or Plain MD |
| Team collaboration | Notion |
| Minimal dependencies | Plain MD + SSG |
| Existing git-backed workflow | Obsidian or Plain MD |

## PA Integration Assessment

**Obsidian is the strongest fit** for this use case because:
1. Local files match the PA's git-backed architecture
2. The CLI, REST API, and Dataview provide three programmatic access layers
3. Canvas enables visual outputs the PA generates as JSON
4. The user-facing experience (graph view, live queries, plugins) is richer than alternatives

**The main risk** is dependency on community plugins (REST API, Dataview, Templater) that could become unmaintained. The mitigation is that the PA's core operations (file I/O) work without any plugins — plugins enhance the human experience, not the PA's write path.

## Gaps and Limitations

- Logseq CLI data sourced from search snippets (npm page returned 403) [29]
- Notion comparison data is from official API docs [21] but practical automation experience is from third-party sources
- Plain MD + SSG comparison is necessarily broad — specific tools (MkDocs, Hugo, Jekyll) each have distinct capabilities
- Performance comparison data (speed, resource usage) is not available for any tool
