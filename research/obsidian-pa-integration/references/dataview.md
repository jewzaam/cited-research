# Dataview Plugin

## Dimension Coverage

This reference covers the Dataview plugin — querying structured data from note frontmatter, live dashboards, DQL syntax, and DataviewJS.

For source details, see [citations.md](../citations.md).

## Overview

Dataview transforms an Obsidian vault into a queryable database: "Treat your Obsidian Vault as a database which you can query from" [7]. It indexes metadata from notes and provides multiple query interfaces [7].

## Data Annotation Methods

### YAML Frontmatter

```yaml
---
alias: "document"
last-reviewed: 2021-08-17
thoughts:
  rating: 8
  reviewable: false
---
```

"All YAML Frontmatter fields will be automatically available as Dataview fields" [8]. Frontmatter is natively supported by Obsidian core [8].

### Inline Fields

| Syntax | Example | Visibility |
|---|---|---|
| Standalone | `Basic Field:: Some random Value` | Key and value visible [8] |
| Embedded (brackets) | `I rate this [rating:: 9]!` | Value visible in text flow [8] |
| Tasks/lists | `- [ ] Send mail [due:: 2022-04-05].` | Value visible on task [8] |
| Hidden (parentheses) | `Text (hiddenKey:: value).` | Key hidden in preview [8] |

### Field Naming Rules

- Spaces and capitals sanitized to lowercase-with-dashes (`Basic Field` → `basic-field`) [8]
- Formatting tokens (bold/italic) stripped during indexing [8]
- UTF-8 supported; emojis require bracket syntax: `[🎅:: value]` [8]

### Supported Data Types

Text, numbers, dates (ISO YYYY-MM-DD), objects (YAML nested structures) [8].

### Implicit Fields (Auto-Indexed)

`file.cday` (creation date), `file.outlinks` (links), `file.etags` (tags), `file.lists`, `file.tasks` [8].

## Query Types

| Type | Output | Syntax | Key Feature |
|---|---|---|---|
| LIST | Bullet-point file links | `LIST [info] [data_commands]` | `WITHOUT ID` variant [9] |
| TABLE | Tabular data with columns | `TABLE col1, col2 AS "Header" [data_commands]` | `WITHOUT ID`, computed columns [9] |
| TASK | Interactive checkbox list | `TASK [data_commands]` | Modifies source files when checked [9] |
| CALENDAR | Monthly calendar with dots | `CALENDAR date_field [data_commands]` | Requires date-type field [9] |

All types support WHERE, SORT, and GROUP BY (except CALENDAR ignores SORT/GROUP BY) [9].

## Query Modes

| Mode | Description | Security |
|---|---|---|
| DQL | SQL-like pipeline syntax | Sandboxed, safe [7] |
| Inline expressions | DQL embedded in markdown text | Sandboxed, safe [7] |
| DataviewJS | Full JavaScript API with `dv` object | Plugin-level access — can modify files and network [7] |
| Inline JS | JavaScript within markdown text | Plugin-level access [7] |

**Security warning:** JavaScript queries "operate at plugin-level access, potentially allowing file creation/deletion and network calls" [7]. Regular DQL queries are sandboxed and safer [7].

## PA Dashboard Example

A PA could write structured notes with frontmatter and have Dataview render live dashboards:

```yaml
---
type: task
status: open
priority: high
source: calendar
due: 2026-03-31
---
```

Then a dashboard note could contain:

```
TABLE status, priority, due
FROM "tasks"
WHERE status = "open"
SORT priority DESC
```
[9]

This pattern works because:
1. The PA writes plain markdown files with YAML frontmatter (no Obsidian required) [8]
2. Dataview auto-indexes all frontmatter fields [8]
3. Dashboard queries update live as files change [7]

## PA Integration Assessment

**Plugin-dependent:** Yes — Dataview is a community plugin.

**Requires Obsidian running:** For rendering queries, yes. For writing structured notes with frontmatter that Dataview will later query — no, the PA writes plain files to disk.

**Works against files on disk:** Writing structured notes works directly on disk. Querying requires Obsidian + Dataview running.

## Gaps and Limitations

- Index update latency after external file modifications not documented [7]
- Memory footprint for large vaults not documented [7]
- DataviewJS security model relies on trust, not sandboxing [7]
- No programmatic API for external tools to execute DQL directly (but REST API plugin bridges this gap via `/search/` endpoint with DQL content type) [6]
