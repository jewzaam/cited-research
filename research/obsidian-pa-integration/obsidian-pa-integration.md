# Obsidian.md for Personal Assistant Documentation and Automation

## Executive Summary

This research evaluates Obsidian.md as the human-facing documentation layer for a CLI-first personal assistant (PA) that currently uses a TkInter dashboard, Google Calendar integration via GWS CLI, git-backed JSON state, and task management. The question: can Obsidian serve as the surface that the PA writes to programmatically and the user reads and navigates interactively?

**The answer is yes, with caveats.** Obsidian's architecture — a vault of plain markdown files on disk — is fundamentally compatible with a PA that writes files programmatically. The PA can create, modify, and append to notes using standard file I/O without Obsidian running. When Obsidian is running, three additional integration layers become available: the official CLI (80+ commands) [1], the Local REST API plugin (CRUD + surgical edits) [6], and the `obsidian://` URI scheme [4][5]. Dataview renders live dashboards from PA-written frontmatter [7], and Canvas files (.canvas JSON) can be generated as visual task boards [14].

The primary risk is that several key integrations depend on community plugins (REST API, Dataview, Templater) rather than built-in features. The mitigation is that the PA's core write path — plain file I/O — requires no plugins.

## Integration Methods Matrix

| Feature | Method | Plugin Required | Obsidian Must Be Running | Works on Disk |
|---|---|---|---|---|
| Read notes | CLI `read` [1] | No | Yes | N/A |
| Create notes | CLI `create` [1] or file I/O | No | CLI: Yes; File I/O: No | Yes |
| Append to notes | CLI `append` [1], REST API PATCH [6] | REST API: Yes | Yes | File I/O: Yes |
| Search vault | CLI `search` [1], REST API `/search/` [6] | REST API: Yes | Yes | No |
| Surgical edit (by heading) | REST API PATCH [6] | Yes | Yes | No |
| Set frontmatter properties | CLI `property:set` [1], REST API PATCH [6] | REST API: Yes | Yes | File I/O: Yes |
| Daily note operations | CLI `daily:append` [1], REST API `/periodic/` [6] | REST API: Yes | Yes | File I/O: Yes |
| Live dashboards | Dataview DQL [7][8][9] | Yes | Yes (for rendering) | PA writes files |
| Visual task boards | Canvas JSON [14] | No | No | Yes |
| Open specific note | URI `obsidian://open` [4] | No | Launches if not running | N/A |
| Execute commands | URI `obsidian://adv-uri` [5], REST API [6] | Advanced URI or REST API | Yes | No |

## Detailed Analysis by Dimension

### 1. Obsidian CLI

The official CLI was released in Obsidian v1.12.0 (February 2026) [1][2]. It provides over 80 commands covering file management, daily notes, search, tasks, properties, sync, publishing, and developer tools [1].

**Key constraint:** The Obsidian desktop app must be running. "If Obsidian is not running, the first command you run launches Obsidian" [1].

On Linux, the CLI creates a symlink at `/usr/local/bin/obsidian` (requires sudo for AppImage) [1]. Commands use `parameter=value` syntax with output format options including json, csv, tsv, and yaml [1]. Multi-vault targeting uses `vault="Name"` as the first argument [3].

A separate **headless client** (`obsidian-headless`, installed via npm, requires Node.js 22+) provides Sync and Publish without the desktop app, but does not support the full CLI command set [22]. It is currently in open beta [22].

For full details, see [references/obsidian-cli.md](references/obsidian-cli.md).

### 2. URI Scheme

The built-in `obsidian://` protocol supports 7 actions: open, new, daily, unique, search, choose-vault, and hook-get-address [4]. On Windows and macOS, the protocol registers automatically on first run [4]. On Linux, it requires a manual `.desktop` file with `MimeType=x-scheme-handler/obsidian` and the `%u` parameter in the Exec line [4][18].

The **Advanced URI** community plugin (v1.46.1, MIT, 1.1k stars) [5] extends this significantly — adding content append/prepend modes, search and replace, command execution by ID, frontmatter editing, and canvas movement [5].

For full details, see [references/uri-scheme.md](references/uri-scheme.md).

### 3. Local REST API Plugin

The `obsidian-local-rest-api` plugin (MIT, by coddingtonbear) [6] runs on `https://127.0.0.1:27124` with self-signed HTTPS and Bearer token authentication [6]. It provides 11 endpoint groups covering file CRUD, surgical PATCH edits (targeting headings, block references, or frontmatter fields), periodic note management, search (including Dataview DQL and JsonLogic queries), command execution, and tag queries [6].

**This is the most capable programmatic integration point** for a Python-based PA when Obsidian is running. A PA can:
- Create and update task notes via `PUT /vault/{path}` [6]
- Append to daily notes via `POST /periodic/daily/` [6]
- Search with Dataview queries via `POST /search/` with DQL content type [6]
- Set frontmatter fields via `PATCH /vault/{path}` targeting frontmatter [6]

For full details, see [references/local-rest-api.md](references/local-rest-api.md).

### 4. Dataview Plugin

Dataview (by blacksmithgu) [7] indexes all note metadata — both YAML frontmatter and inline fields (`Key:: Value` syntax) [8] — and provides four query types: LIST, TABLE, TASK, and CALENDAR [9]. DQL is sandboxed and safe; DataviewJS provides full JavaScript access with plugin-level privileges [7].

**PA dashboard pattern:** The PA writes structured notes with frontmatter like `status: open`, `priority: high`, `source: calendar` [8]. A dashboard note contains Dataview queries that render live tables of these notes [9]. The PA writes files; Dataview renders the views. Implicit fields like `file.cday` and `file.etags` are auto-indexed without any frontmatter [8].

For full details, see [references/dataview.md](references/dataview.md).

### 5. Templater and Daily Notes

The core **Daily Notes** plugin creates notes with YYYY-MM-DD format in a configurable folder with a configurable template [4]. **Periodic Notes** (community, by liamcain) extends this to weekly (`gggg-[W]ww`) and monthly (`YYYY-MM`) periods with template variables like `{{date}}`, `{{time}}`, and `{{sunday}}` through `{{saturday}}` [13].

**Templater** (community, v2.18.1, AGPLv3, 4.7k stars) [10] provides 9 internal function modules including `tp.system` for shell command execution [11]. Its "Trigger on new file creation" setting auto-applies templates based on folder or regex rules [12]. **Startup Templates** execute once on initialization — useful for setting up event hooks [12].

**PA strategy:** The PA writes the daily note file directly to disk before the user opens Obsidian. If Obsidian is running, `obsidian daily:append content="..."` appends without overwriting [1][3]. Templater won't re-process files that already exist, so PA content persists [12].

For full details, see [references/templater-daily-notes.md](references/templater-daily-notes.md).

### 6. Canvas

Canvas uses the **JSON Canvas** open format (v1.0, MIT) [14][15] — standard JSON files with `.canvas` extension. The specification defines 4 node types (text, file, link, group) and edges with directional connections [14]. Colors use hex or preset numbers 1-6 (red, orange, yellow, green, cyan, purple) [14].

**PA task board generation:** The PA can write `.canvas` files as JSON with group nodes for columns (To Do, In Progress, Done), text nodes for task cards, and edges for dependencies [14]. No Obsidian interaction needed — the PA writes JSON, the user sees a visual board. **PyCanvas** (Python, MIT, early-stage) provides a library for this [16], but direct JSON generation is straightforward [14].

For full details, see [references/canvas.md](references/canvas.md).

### 7. Vault Structure and Linking

Obsidian CEO Steph Ango uses a minimal folder structure with most notes at root, dedicated folders for References, Clippings, Daily, Templates, and Attachments [20]. Key conventions: pluralize categories/tags, YYYY-MM-DD dates, file names matching source titles [20].

**For PA integration,** type-based folders (Daily/, Tasks/, Calendar/, Canvas/) separate PA-written content from human-written notes [20]. Consistent YAML frontmatter schemas across PA-generated notes enable Dataview queryability [8]. Unresolved links serve as "breadcrumbs for future connections" [20].

For full details, see [references/vault-structure.md](references/vault-structure.md).

### 8. Linux Desktop Integration

Obsidian is available on Linux as AppImage, Flatpak (verified on Flathub), Snap (`--classic`), and .deb [1]. For PA integration, AppImage or .deb provide the most straightforward filesystem access — Flatpak's sandbox and Snap's confinement add complexity [17].

Wayland requires manual configuration for Electron-based apps [35]. The `obsidian://` URI handler needs a `.desktop` file at `~/.local/share/applications/obsidian.desktop` with `MimeType=x-scheme-handler/obsidian` and `%u` in the Exec line, followed by `update-desktop-database` [18].

For full details, see [references/linux-integration.md](references/linux-integration.md).

### 9. Sync and Conflict Handling

**Critical finding:** Obsidian does **not** automatically reload files modified externally while open. Users must navigate away and back to see changes [19]. This creates a data loss risk if the user edits a stale cached version [19].

**Obsidian Sync** uses diff-match-patch for markdown merges and last-modified-wins for binary files [28]. **Obsidian Git** plugin (by Vinzent03) provides auto commit/pull/push but has no built-in conflict resolution [17][24]. Custom Git merge drivers can handle specific file types [25]. Mobile Git is complex — iOS requires Working Copy; Android uses an unstable JS implementation [27].

**PA mitigation:** Write to dedicated PA folders the user won't have open. Use append-only operations. Use CLI/REST API when Obsidian is running to let Obsidian mediate access [1][6].

For full details, see [references/sync-conflicts.md](references/sync-conflicts.md).

### 10. Alternatives Comparison

| Tool | PA Write Path | Live Queries | Rate Limits | Open Source |
|---|---|---|---|---|
| Obsidian | File I/O (no API needed) [7] | Dataview DQL [7] | None [6] | No |
| Logseq | File I/O + CLI [29] | Built-in queries [31] | None [29] | Yes (AGPL) |
| Notion | REST API required [21] | Database views [21] | 3 req/s [21] | No |
| Plain MD + SSG | File I/O | None (static) | N/A | Varies |

Obsidian is the strongest fit because local files match the PA's git-backed architecture, three programmatic layers (CLI, REST API, URI) provide runtime integration, Dataview enables live dashboards, and Canvas enables visual outputs — all from plain files the PA writes [1][6][7][14].

For full details, see [references/alternatives.md](references/alternatives.md).

## Architecture Recommendation

### Two-Mode Operation

**Mode 1: Obsidian not running (file I/O)**
- PA writes daily notes, task notes, calendar event notes as markdown with YAML frontmatter
- PA generates `.canvas` files for visual boards
- PA commits changes to git
- No dependencies on Obsidian or plugins

**Mode 2: Obsidian running (API-enhanced)**
- PA uses CLI for quick operations (`obsidian daily:append`, `obsidian search`) [1]
- PA uses REST API for surgical edits and Dataview queries [6]
- PA detects Obsidian state by checking `https://127.0.0.1:27124/` (no auth required) [6]
- Graceful fallback to Mode 1 if Obsidian is not running

### Required Plugins

| Plugin | Purpose | License | Risk Level |
|---|---|---|---|
| obsidian-local-rest-api [6] | REST API for PA integration | MIT | Medium — single maintainer |
| obsidian-dataview [7] | Live dashboards from frontmatter | — | Low — widely adopted (large community) |
| Templater [10] | Daily note template processing | AGPLv3 | Low — 4.7k stars, active |
| obsidian-periodic-notes [13] | Weekly/monthly note support | — | Low — complements Daily Notes |
| obsidian-advanced-uri [5] | Extended URI actions | MIT | Low — 1.1k stars, active |
| obsidian-git [17] | Git sync from within Obsidian | — | Low — widely adopted |

*License fields marked "—" indicate license information was not extracted from the sources reviewed. All listed plugins are available as free community plugins.*

### Recommended Vault Structure

```
vault/
├── Daily/          # PA writes daily notes (YYYY-MM-DD.md)
├── Tasks/          # PA creates task notes with frontmatter
├── Calendar/       # PA syncs calendar events
├── Canvas/         # PA generates .canvas JSON files
├── Dashboards/     # Dataview query notes (human-created)
├── Templates/      # Templater templates (human-created)
├── References/     # Human-created reference notes
└── Attachments/    # Media files
```

## Methodology

This research was conducted using the cited-research methodology on 2026-03-30.

- **Discovery:** 5 parallel research agents searched across 10 dimensions using WebSearch
- **Deep read:** Key sources fetched via WebFetch and verified against claims
- **Sources:** 37 citations across official documentation (Tier 2), plugin GitHub repos (Tier 2), practitioner blogs (Tier 3), and community forums (Tier 4)
- **Verification:** Citation audit and consistency review conducted by independent sub-agents

### Source Accessibility

| Status | Count |
|---|---|
| Fetched and verified | 22 |
| Referenced from search snippets (not fetched) | 13 |
| Dynamic page (content not extractable) | 1 |
| HTTP 403 | 1 |

Obsidian's official help documentation uses dynamic content loading (JavaScript-rendered from `publish-01.obsidian.md`), making WebFetch extraction unreliable for some pages. The CLI documentation was successfully extracted via the raw content URL [1]. The sync/troubleshoot page [28] was not extractable; claims rely on discovery agent search snippets.

## Limitations

1. **Obsidian CLI is new** (February 2026) and may have breaking changes [1]
2. **File watcher behavior** is poorly documented — forum reports are the primary source [19][34]
3. **REST API concurrent access** and performance at scale are not documented [6]
4. **Community plugin longevity** is a structural risk — REST API and Dataview are single-maintainer projects
5. **Logseq CLI data** was partially sourced from search snippets due to npm page 403 [29]
6. **Obsidian Sync conflict resolution** details rely on search snippets rather than verified page content [28]

## Source Files

- [citations.md](citations.md) — All 37 sources with URLs, tiers, and extracted data
- [references/obsidian-cli.md](references/obsidian-cli.md)
- [references/uri-scheme.md](references/uri-scheme.md)
- [references/local-rest-api.md](references/local-rest-api.md)
- [references/dataview.md](references/dataview.md)
- [references/templater-daily-notes.md](references/templater-daily-notes.md)
- [references/canvas.md](references/canvas.md)
- [references/vault-structure.md](references/vault-structure.md)
- [references/linux-integration.md](references/linux-integration.md)
- [references/sync-conflicts.md](references/sync-conflicts.md)
- [references/alternatives.md](references/alternatives.md)
- [audit/citation-audit.md](audit/citation-audit.md)
- [audit/consistency-review.md](audit/consistency-review.md)
