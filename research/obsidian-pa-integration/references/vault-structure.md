# Vault Structure and Linking

## Dimension Coverage

This reference covers best practices for organizing an Obsidian vault that is both human-browsable and machine-writable — folder conventions, linking strategies, and tag taxonomies.

For source details, see [citations.md](../citations.md).

## Folder Organization

### Obsidian CEO's Approach

Steph Ango (Obsidian CEO) uses a minimal folder structure with most notes at the root level [20]:

| Folder | Purpose |
|---|---|
| Root | Personal content — journal, essays, evergreen notes [20] |
| References/ | External subjects (books, movies, people, places) [20] |
| Clippings/ | Articles by others [20] |
| Attachments/ | Media files (hidden from navigation) [20] |
| Daily/ | Daily notes as YYYY-MM-DD.md (hidden) [20] |
| Templates/ | Note templates (hidden) [20] |

### Key Conventions

- Pluralize all categories and tags [20]
- YYYY-MM-DD date format universally [20]
- File names match source titles [20]
- Individual thoughts use `YYYY-MM-DD HHmm` format [20]
- Properties defined in `.obsidian/types.json` [20]

### Type-Based vs Topic-Based

Community consensus favors type-based folder organization (daily notes, meetings, templates, references) over topic-based organization (projects, work, personal), because topic boundaries are fluid while note types are stable [20].

## Linking Strategy

### Wikilinks vs Markdown Links

Obsidian supports two internal link formats [4]:

| Format | Syntax | Backlink Support |
|---|---|---|
| Wikilinks | `[[note name]]` | Full backlink support |
| Markdown links | `[text](note.md)` | Limited backlink support |

Wikilinks are recommended for Obsidian-internal workflows. Markdown links provide better cross-platform compatibility but may lack full backlink support (unverified from discovery agents — this claim was not verified in fetched sources).

### Unresolved Links

"Unresolved links are important because they are breadcrumbs for future connections between things" [20]. This philosophy encourages linking freely, even to notes that don't exist yet.

## Tag Taxonomy

Tags support nested hierarchy via forward slash syntax (e.g., `#project/active`) [20].

### Conventions for PA Integration

For a machine-writable vault, structured tags enable programmatic filtering:

```yaml
---
tags:
  - source/calendar
  - type/task
  - status/open
  - priority/high
---
```

This frontmatter structure is directly queryable by Dataview [8] and searchable by the REST API [6].

## Patterns for Machine-Writable Vaults

Based on the research across all dimensions, a PA-optimized vault structure would be:

```
vault/
├── Daily/                    # PA writes daily notes here
│   └── 2026-03-30.md
├── Tasks/                    # PA creates task notes
│   └── review-q1-report.md
├── Calendar/                 # PA syncs calendar events
│   └── 2026-03-30-standup.md
├── Canvas/                   # PA generates visual boards
│   └── task-board.canvas
├── Templates/                # Templater templates
│   └── daily-template.md
├── References/               # Human-created reference notes
├── Dashboards/               # Dataview query notes
│   └── open-tasks.md
└── Attachments/              # Media files
```

Key principles:
1. **Separate PA-written folders** from human-written content to minimize conflict [19][20]
2. **Consistent frontmatter schema** across PA-generated notes for Dataview queryability [8]
3. **Type-based folders** rather than topic-based [20]
4. **Standard date formats** (YYYY-MM-DD) for temporal notes [20]

## PA Integration Assessment

**Built-in vs plugin:** Vault structure, folders, and linking are built-in. Tags are built-in. Querying structured data requires Dataview plugin [7].

**Requires Obsidian running:** No — vault files are plain markdown on disk. The PA can create and modify them directly.

**Works against files on disk:** Yes — this is the foundational principle. Obsidian vaults are folders of markdown files.

## Gaps and Limitations

- Performance implications for large vaults (10k+ notes) with deep folder hierarchies not documented
- No official guidance on machine-writable vault conventions — the patterns above are synthesized from multiple sources
- Wikilinks vs markdown links backlink behavior needs verification from official docs (dynamic page content was not extractable)
- `.obsidian/types.json` for property type enforcement is mentioned but not documented in detail [20]
