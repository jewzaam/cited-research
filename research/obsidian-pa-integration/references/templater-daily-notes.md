# Templater and Daily Notes

## Dimension Coverage

This reference covers the Templater plugin, the core Daily Notes plugin, and the Periodic Notes community plugin — focusing on automated note generation that a PA could leverage.

For source details, see [citations.md](../citations.md).

## Templater Plugin

"Templater is a template language that lets you insert variables and functions results into your notes. It will also let you execute JavaScript code manipulating those variables and functions" [11].

### Template Syntax

Templates use the delimiter syntax `<% tp.function() %>` [11].

### Internal Function Modules

| Module | Purpose |
|---|---|
| `tp.app` | Application-level operations [11] |
| `tp.config` | Configuration access [11] |
| `tp.date` | Date manipulation and formatting [11] |
| `tp.file` | File metadata and operations [11] |
| `tp.frontmatter` | YAML frontmatter handling [11] |
| `tp.hooks` | Event-based triggers [11] |
| `tp.obsidian` | Obsidian integration [11] |
| `tp.system` | System-level operations (shell commands) [11] |
| `tp.web` | External web data retrieval [11] |

### Automation Settings

| Setting | Description |
|---|---|
| Trigger on new file creation | Monitors file creation events, applies matching template rules [12] |
| Folder Templates | Auto-apply templates to folders/subfolders using deepest-match logic [12] |
| File Regex Templates | Match new file paths against regex; first match applies [12] |
| Startup Templates | Execute once on Templater initialization; for event hooks [12] |
| Template Hotkeys | Bind templates to keyboard shortcuts [12] |

### System Commands (tp.system)

Allows executing shell commands from templates [10]. Requires configuring shell binary location [10].

**Security warning:** "Templater allows you to execute arbitrary JavaScript code and system commands. It can be dangerous to execute arbitrary JavaScript code or system commands from untrusted sources" [10].

### Technical Details

GNU AGPLv3 license, TypeScript (75%), v2.18.1 (January 29, 2026), 4.7k stars [10].

## Core Daily Notes Plugin

The Daily Notes plugin is a **core plugin** (built-in, not community) [4].

### Configuration

| Setting | Detail |
|---|---|
| Date format | Default: YYYY-MM-DD [13] |
| Folder | Where daily notes are stored [13] |
| Template file | Template applied when creating daily notes [13] |
| Auto-open | Open daily note on Obsidian startup [13] |

## Periodic Notes Plugin (Community)

"Expands on the idea of daily notes and introduces weekly and monthly notes" [13].

### Supported Periods

Weekly and monthly notes (daily through integration) [13].

### Template Variables

| Period | Variables |
|---|---|
| Weekly | `{{title}}`, `{{date}}`, `{{time}}`, `{{sunday}}` through `{{saturday}}` [13] |
| Monthly | `{{title}}`, `{{date}}`, `{{time}}` [13] |

### Default Formats

- Weekly: `gggg-[W]ww` [13]
- Monthly: `YYYY-MM` [13]

### Integration

Calendar plugin integration for week number displays [13]. Settings migration from Calendar plugin's legacy weekly notes [13].

## PA Pre-Population Strategy

A PA could pre-populate daily notes before the user opens Obsidian using this approach:

1. **Write the daily note file directly to disk** — The PA creates `Daily/2026-03-30.md` with today's calendar, pending tasks, and recommended actions. This is plain file I/O, no Obsidian required.

2. **Templater processes on open** — When the user opens Obsidian, Templater's "Trigger on new file creation" can apply additional template logic to new files [12]. If the file already exists (PA wrote it), Templater won't re-process it — the PA's content persists.

3. **Alternative: PA uses CLI** — If Obsidian is running, `obsidian daily:append content="..."` [1][3] appends to the daily note without overwriting existing content.

4. **Periodic notes** — The PA can also create weekly/monthly summary notes following the format conventions (`gggg-[W]ww`, `YYYY-MM`) [13].

## PA Integration Assessment

**Built-in vs plugin:**
- Daily Notes: built-in core plugin [4]
- Templater: community plugin (AGPLv3) [10]
- Periodic Notes: community plugin [13]

**Requires Obsidian running:**
- Writing daily note files to disk: No
- Templater processing: Yes
- CLI append: Yes [1]

**Works against files on disk:** Yes — the PA can write daily/periodic note files as plain markdown with YAML frontmatter. Obsidian and its plugins process them when opened.

## Gaps and Limitations

- Templater's security model is trust-based — untrusted templates can execute arbitrary code [10]
- If the PA writes a file that Templater later processes, Templater may overwrite PA content (depends on template design)
- Periodic Notes does not mention quarterly or yearly support in its README [13]
- Template execution order between Daily Notes and Templater plugins not documented [12]
