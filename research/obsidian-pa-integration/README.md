# Obsidian.md for Personal Assistant Integration

Can Obsidian serve as the human-facing documentation surface for a CLI-first personal assistant that writes to it programmatically? **Yes** — Obsidian vaults are folders of plain markdown files, so the PA writes files directly to disk. When Obsidian is running, three additional integration layers unlock: the official CLI (80+ commands), a REST API plugin (CRUD + surgical edits), and URI-based actions. Dataview renders live dashboards from PA-written frontmatter, and Canvas files are plain JSON the PA generates as visual boards.

## Key Integration Table

| PA Operation | Best Method | Obsidian Required |
|---|---|---|
| Create/update notes | File I/O to vault directory | No |
| Append to daily note | CLI `daily:append` or file append | CLI: Yes |
| Search vault | CLI `search` or REST API `/search/` | Yes |
| Edit by heading | REST API `PATCH` | Yes |
| Set frontmatter | CLI `property:set` or file I/O | CLI: Yes; File I/O: No |
| Live dashboards | Dataview queries (PA writes structured notes) | Yes (for rendering) |
| Visual task boards | Write `.canvas` JSON files | No |
| Open specific note | `obsidian://open?vault=X&file=Y` URI | Launches if needed |

## Decision Framework

1. **Can the PA write without Obsidian running?** Yes — vault files are plain markdown on disk. Canvas files are plain JSON. No API needed for writes.
2. **Should the PA use the CLI or REST API?** REST API for surgical edits (PATCH by heading/frontmatter). CLI for quick operations (daily append, search). Both require Obsidian running.
3. **How does the PA detect if Obsidian is running?** Check `https://127.0.0.1:27124/` (REST API status endpoint, no auth required). Fall back to file I/O if unavailable.
4. **What about file conflicts?** Obsidian does NOT auto-reload externally modified files. Write to dedicated PA folders, use append-only operations, or use CLI/REST API when Obsidian is running.
5. **What plugins are needed?** REST API (obsidian-local-rest-api) for API access, Dataview for dashboards, Templater for daily note templates. All community plugins — core PA writes work without them.

## Primary Risk

Key integrations (REST API, Dataview) are community plugins with single maintainers. Mitigation: the PA's core write path is plain file I/O that requires no plugins. Plugins enhance the human experience, not the PA's write path.

## Files

- [Full analysis](obsidian-pa-integration.md) — 10-dimension research with 37 cited sources
- [Citations](citations.md) — All sources with URLs and quality tiers
- [References](references/) — One file per research dimension
- [Audit reports](audit/) — Citation audit and consistency review
