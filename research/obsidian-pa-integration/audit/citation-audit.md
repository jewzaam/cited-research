# Citation Audit Report

**Research:** Obsidian PA Integration
**Audit Date:** 2026-03-30
**Auditor:** Claude Code (Sonnet 4.5)
**Methodology:** Source verification - comparing document claims against pre-fetched source content

## Summary Table

| Citation | Grade | Status |
|---|---|---|
| [1] Obsidian CLI Help | VERIFIED | All claims supported |
| [2] Obsidian CLI Landing | VERIFIED | All claims supported |
| [3] CLI Guide Blog | VERIFIED | All claims supported |
| [4] Obsidian URI Docs | VERIFIED | All claims supported |
| [5] Advanced URI GitHub | VERIFIED | All claims supported |
| [6] Local REST API GitHub | VERIFIED | All claims supported |
| [7] Dataview GitHub | VERIFIED | All claims supported |
| [8] Dataview Metadata | VERIFIED | All claims supported |
| [9] Dataview Query Types | VERIFIED | All claims supported |
| [10] Templater GitHub | VERIFIED | All claims supported |
| [11] Templater Introduction | VERIFIED | All claims supported |
| [12] Templater Settings | VERIFIED | All claims supported |
| [13] Periodic Notes GitHub | VERIFIED | All claims supported |
| [14] JSON Canvas Spec | VERIFIED | All claims supported |
| [15] JSON Canvas GitHub | VERIFIED | All claims supported |
| [16] PyCanvas GitHub | VERIFIED | All claims supported |
| [17] Obsidian Git GitHub | VERIFIED | All claims supported |
| [18] URI Linux Setup | VERIFIED | All claims supported |
| [19] External Changes Forum | VERIFIED | All claims supported |
| [20] Steph Ango Vault | VERIFIED | All claims supported |
| [21] Notion API Limits | VERIFIED | All claims supported |
| [22] Obsidian Headless | VERIFIED | All claims supported |
| [23] XDA Developers | NOT FOUND | Not fetched; discovery snippets only |
| [24] Git Issue #803 | NOT FOUND | Not fetched; discovery snippets only |
| [25] Custom Git Driver Blog | NOT FOUND | Not fetched; discovery snippets only |
| [26] Sync vs Git Comparison | NOT FOUND | Not fetched; discovery snippets only |
| [27] Git Alternative Medium | NOT FOUND | Not fetched; discovery snippets only |
| [28] Troubleshoot Sync | NOT FOUND | Dynamic page; not extractable |
| [29] Logseq CLI npm | NOT FOUND | HTTP 403; discovery snippets only |
| [30] Logseq Plugin API | NOT FOUND | Not fetched; discovery snippets only |
| [31] PKM Comparison 2026 | NOT FOUND | Not fetched; discovery snippets only |
| [32] MkDocs | NOT FOUND | Not fetched; discovery snippets only |
| [33] Material for MkDocs | NOT FOUND | Not fetched; discovery snippets only |
| [34] File Explorer Reload | NOT FOUND | Not fetched; discovery snippets only |
| [35] Wayland Configuration | NOT FOUND | Not fetched; discovery snippets only |
| [36] URI Forum Thread | NOT FOUND | Not fetched; discovery snippets only |
| [37] AppImage %u Bug | NOT FOUND | Not fetched; discovery snippets only |

## Grade Distribution

- VERIFIED: 22
- PARTIAL: 0
- INACCURATE: 0
- INACCESSIBLE: 0
- NOT FOUND: 15

## Detailed Citation Analysis

---

### [1] Obsidian CLI Help
**URL:** https://obsidian.md/help/cli
**Grade:** VERIFIED

**Claims made:**
- Over 80 commands covering file management, daily notes, search, tasks, properties, sync, publishing, developer tools
- Requires Obsidian app to be running; "If Obsidian is not running, the first command you run launches Obsidian"
- Obsidian 1.12+ required
- Platform setup: macOS uses ~/.zprofile, Linux creates symlink at /usr/local/bin/obsidian (requires sudo)
- Parameter syntax: parameter=value
- Output formats: json, csv, tsv, yaml
- TUI mode available

**Source evidence:**
```
"Obsidian app must be running. If Obsidian is not running, the first command you run launches Obsidian."

Command Categories (80+ commands)
- File Management: create, read, append, move, delete, rename
- Daily Notes: daily, daily:append, daily:prepend, daily:path
[...complete list matches claim...]

Platform-Specific Setup
- macOS: Adds binary to PATH via ~/.zprofile
- Linux: Creates symlink at /usr/local/bin/obsidian; AppImage and Snap have special considerations

Output formatting options (json, csv, tsv, yaml)
```

**Assessment:** Source directly supports all specific claims. The "80+ commands" count, the requirement for Obsidian to be running, platform-specific setup, and output formats are all explicitly stated in the source.

---

### [2] Obsidian CLI Landing
**URL:** https://obsidian.md/cli
**Grade:** VERIFIED

**Claims made:**
- Four use cases: Develop, Collaborate, Automate, Tinker
- Installation requires enabling in Settings → General
- Headless sync overview mentioned

**Source evidence:**
```
Four primary use cases:
- Develop: Build plugins and themes faster...
- Collaborate: Deploy documentation, sync shared vaults to servers...
- Automate: Orchestrate workflow with cron jobs, shell scripts...
- Tinker: Programmatic read/write/search with agentic tool support.

enable "Command line interface" in Settings → General

Headless Sync enables encrypted synchronization without GUI for remote backups, automated publishing, and server integration.
```

**Assessment:** All claims directly supported. The four use cases, settings location, and headless sync mention are verbatim from the source.

---

### [3] CLI Guide Blog
**URL:** https://blog.wenhaofree.com/en/posts/articles/obsidian-1-12-cli-ultimate-guide/
**Grade:** VERIFIED

**Claims made:**
- Practical CLI command examples
- vault= parameter usage
- daily note commands
- search commands with limit parameter

**Source evidence:**
```
Daily Notes: obsidian daily, obsidian daily:append content="text" open, obsidian tasks daily total
Search: obsidian search query="term", obsidian search:context query="term" limit=10
vault="Name" — must be first argument for multi-vault targeting
limit=number — restricts result count
```

**Assessment:** All specific command examples and parameter usage cited in the research documents are present in the source.

---

### [4] Obsidian URI Docs
**URL:** https://obsidian.md/help/Extending+Obsidian/Obsidian+URI
**Grade:** VERIFIED

**Claims made:**
- 7 actions: open, new, daily, unique, search, choose-vault, hook-get-address
- Parameters per action (vault, file, path, content, etc.)
- Encoding requirements (forward slashes → %2F, spaces → %20)
- Shorthand formats available
- x-callback-url support
- Linux requires .desktop file with MimeType=x-scheme-handler/obsidian and %u parameter

**Source evidence:**
```
Available Actions
1. open — Access notes or vaults
2. new — Create notes
3. daily — Daily notes
4. unique — Unique notes
5. search — Search interface
6. choose-vault — Vault manager
7. hook-get-address — Hook integration

Encoding Requirements
Values must be properly URI encoded. Forward slashes → %2F, spaces → %20.

x-callback-url Parameters
Returns: name (filename without extension), url (obsidian:// URI), file (file:// URL, desktop only).

Linux: requires obsidian.desktop file with Exec=executable %u directive
```

**Assessment:** All 7 actions enumerated correctly, encoding requirements match, x-callback-url support confirmed, Linux setup requirements verified.

---

### [5] Advanced URI GitHub
**URL:** https://github.com/Vinzent03/obsidian-advanced-uri
**Grade:** VERIFIED

**Claims made:**
- File operations, content editing (append/prepend/overwrite)
- Frontmatter editing
- Command execution via URI
- Daily note integration
- Search/replace
- v1.46.1, MIT license, 1.1k stars

**Source evidence:**
```
Core Capabilities
- Creating new files
- Editing existing files
- Appending content to notes
- Automated search and replace
- Command execution via command IDs
- Frontmatter reading and editing
- Daily note integration

TypeScript (99.3%), MIT License, 87 releases, latest v1.46.1 (Jan 26, 2026), 1.1k stars.
```

**Assessment:** All capability claims verified. Version, license, and star count match exactly.

---

### [6] Local REST API GitHub
**URL:** https://github.com/coddingtonbear/obsidian-local-rest-api
**Grade:** VERIFIED

**Claims made:**
- 11 endpoint groups
- CRUD operations
- PATCH surgical edits (heading/block-reference/frontmatter targets)
- Bearer token auth on https://127.0.0.1:27124
- Dataview DQL and JsonLogic search
- Periodic note management
- Command execution
- API extensibility
- MIT license

**Source evidence:**
```
API Endpoints [table with 11 rows confirming all endpoint groups]

PATCH Operations (Surgical Edits)
Three operations: Append, Prepend, Replace
Target types: heading, block-reference, frontmatter

Authentication
Server: https://127.0.0.1:27124
Self-signed HTTPS certificate
Bearer token authentication: Authorization: Bearer <your-api-key>

Search Functionality
Dataview DQL: Content-Type: application/vnd.olrapi.dataview.dql+txt
JsonLogic: Content-Type: application/vnd.olrapi.jsonlogic+json

License: MIT
```

**Assessment:** All technical claims verified. The 11 endpoint groups, PATCH operations with three target types, authentication mechanism, search modes, and license all confirmed.

---

### [7] Dataview GitHub
**URL:** https://github.com/blacksmithgu/obsidian-dataview
**Grade:** VERIFIED

**Claims made:**
- Vault as queryable database
- Frontmatter + inline fields
- 4 query modes (DQL, DataviewJS, inline expressions, inline JS)
- Security warning about JavaScript query privileges

**Source evidence:**
```
"Treat your Obsidian Vault as a database which you can query from."

Data Annotation Methods
Frontmatter: YAML metadata enclosed by --- at document top.
Inline Fields: Key:: Value syntax embedded in markdown content.

Query Types
1. DQL (Dataview Query Language): Pipeline-based, SQL-like syntax
2. Inline Expressions: DQL embedded in markdown, evaluated in preview mode
3. DataviewJS: Full-access JavaScript API with rendering utilities
4. Inline JS Expressions: JavaScript executed inline within markdown

Security Warning
JavaScript queries operate at plugin-level access, allowing file creation/deletion and network calls.
```

**Assessment:** All claims verified. The four query modes are enumerated, data annotation methods confirmed, and security warning about JavaScript privileges is present.

---

### [8] Dataview Metadata
**URL:** https://blacksmithgu.github.io/obsidian-dataview/annotation/add-metadata/
**Grade:** VERIFIED

**Claims made:**
- YAML frontmatter syntax
- Inline field syntax (Key:: Value)
- Bracket syntax for embedded fields
- Hidden key syntax (parentheses)
- Field naming rules (sanitization to lowercase-dashes)
- Supported data types (text, numbers, dates, objects)
- Implicit fields (file.cday, file.outlinks, file.etags)

**Source evidence:**
```
Frontmatter (YAML)
"All YAML Frontmatter fields will be automatically available as Dataview fields."

Inline Fields
Standalone: Basic Field:: Some random Value
Embedded (bracket): I would rate this a [rating:: 9]!
Hidden key (parentheses): This will not show the (longKeyIDontNeedWhenReading:: key).

Field Naming Rules
- Spaces/capitals sanitized to lowercase with dashes (Basic Field → basic-field)

Supported Data Types
Text, Numbers, Dates (ISO YYYY-MM-DD), Objects (YAML nested structures)

Implicit Fields (auto-indexed)
file.cday (creation date), file.outlinks (links), file.etags (tags), file.lists, file.tasks
```

**Assessment:** All syntax forms, naming rules, data types, and implicit fields verified exactly as claimed.

---

### [9] Dataview Query Types
**URL:** https://blacksmithgu.github.io/obsidian-dataview/queries/query-types/
**Grade:** VERIFIED

**Claims made:**
- Four query types: LIST, TABLE, TASK, CALENDAR
- LIST: bullet-point file links
- TABLE: tabular data with columns/AS aliases
- TASK: interactive checkbox list that modifies source
- CALENDAR: monthly view with date dots
- WITHOUT ID variants
- GROUP BY and WHERE support

**Source evidence:**
```
LIST
Outputs bullet-point list of file links or group names.
LIST WITHOUT ID variant hides file names.

TABLE
Renders tabular data with multiple columns.
Syntax: TABLE column1, column2 AS "Header Name" [data_commands]
TABLE WITHOUT ID removes default "File" column.

TASK
Displays interactive checkbox-enabled task list.
Operates at task level, modifies source files when tasks checked.

CALENDAR
Shows monthly calendar with results as dots on dates.
Requires date-type metadata field.
```

**Assessment:** All four query types described accurately. The key features (WITHOUT ID, AS aliases, task modification, calendar date dots) all verified.

---

### [10] Templater GitHub
**URL:** https://github.com/SilentVoid13/Templater
**Grade:** VERIFIED

**Claims made:**
- Security warning about arbitrary JavaScript and system command execution
- GNU AGPLv3 license
- v2.18.1
- TypeScript (75%)
- 4.7k stars

**Source evidence:**
```
Security Warning
"Templater allows you to execute arbitrary JavaScript code and system commands. It can be dangerous to execute arbitrary JavaScript code or system commands from untrusted sources."

Technical Details
License: GNU AGPLv3
Language: Primarily TypeScript (75%)
Repository: 751 commits, 4.7k stars, 296 forks
Latest Release: Version 2.18.1 (January 29, 2026)
```

**Assessment:** All technical details match exactly. Security warning language verbatim.

---

### [11] Templater Introduction
**URL:** https://silentvoid13.github.io/Templater/introduction.html
**Grade:** VERIFIED

**Claims made:**
- Template syntax: <% tp.function() %>
- 9 internal function modules (tp.app, tp.config, tp.date, tp.file, tp.frontmatter, tp.hooks, tp.obsidian, tp.system, tp.web)
- User functions (scripts + system commands)
- Command types

**Source evidence:**
```
Template Syntax
Templates use delimiter syntax: <% tp.function() %>

Internal Functions (tp.* modules)
1. tp.app - Application-level operations
2. tp.config - Configuration access
3. tp.date - Date manipulation and formatting
4. tp.file - File metadata and operations
5. tp.frontmatter - YAML frontmatter handling
6. tp.hooks - Event-based triggers
7. tp.obsidian - Obsidian integration
8. tp.system - System-level operations (shell commands)
9. tp.web - External web data retrieval

User Functions
- User Scripts: Custom JavaScript implementations
- System Commands: Execute external system-level commands
```

**Assessment:** All 9 modules enumerated correctly, template syntax verified, user function types confirmed.

---

### [12] Templater Settings
**URL:** https://silentvoid13.github.io/Templater/settings.html
**Grade:** VERIFIED

**Claims made:**
- Trigger on new file creation
- Folder templates (deepest-match logic)
- File regex templates
- Startup templates
- Template hotkeys
- User script functions
- User system command functions

**Source evidence:**
```
Trigger on New File Creation
When enabled, Templater monitors file creation events and applies matching rules.

Automation & Configuration
- Template Hotkeys: Bind templates to keyboard shortcuts.
- Folder Templates: Auto-apply templates to specified folders/subfolders using deepest-match logic.
- File Regex Templates: Test new file paths against regex; first match applies template.
- Startup Templates: Execute once when Templater initializes; useful for event hooks without output.
- User Script Functions: Load JavaScript files as CommonJS modules.
- User System Command Functions: Create functions linked to system commands (with security warnings).
```

**Assessment:** All settings and automation features verified. The "deepest-match logic" terminology is directly from the source.

---

### [13] Periodic Notes GitHub
**URL:** https://github.com/liamcain/obsidian-periodic-notes
**Grade:** VERIFIED

**Claims made:**
- Weekly and monthly notes support
- Template variables ({{title}}, {{date}}, {{time}}, {{sunday}}–{{saturday}})
- Default formats (gggg-[W]ww weekly, YYYY-MM monthly)
- Calendar plugin integration

**Source evidence:**
```
"Expands on the idea of daily notes and introduces weekly and monthly notes."

Template Variables
Weekly: {{title}}, {{date}}, {{time}}, {{sunday}} through {{saturday}} (require format spec)
Monthly: {{title}}, {{date}}, {{time}}

Configuration
Filename format using date tokens (defaults: gggg-[W]ww for weekly, YYYY-MM for monthly)

Integration
- Calendar plugin integration for week number displays
```

**Assessment:** All claims verified. Template variables, default formats, and Calendar integration all confirmed.

---

### [14] JSON Canvas Spec
**URL:** https://jsoncanvas.org/spec/1.0
**Grade:** VERIFIED

**Claims made:**
- Complete specification with top-level nodes/edges arrays
- 4 node types (text/file/link/group) with all properties
- Edge properties (id/fromNode/toNode/fromSide/toSide/fromEnd/toEnd/color/label)
- Color format (hex or presets 1-6: red, orange, yellow, green, cyan, purple)

**Source evidence:**
```
Overall Structure
Top level contains two optional arrays: nodes and edges.

Node Types (all share: id, type, x, y, width, height, optional color)
- Text Nodes: text (required string, Markdown syntax)
- File Nodes: file (required string, file path), subpath (optional)
- Link Nodes: url (required string)
- Group Nodes: label, background, backgroundStyle

Edges
Required: id, fromNode, toNode
Optional: fromSide/toSide (top/right/bottom/left), fromEnd/toEnd (none/arrow; defaults none and arrow), color, label

Color Format
Hex format ("FF0000") or preset numbers 1-6 mapping to red, orange, yellow, green, cyan, purple.
```

**Assessment:** Complete specification details verified. All 4 node types, edge properties, and color format including the preset 1-6 mapping are accurate.

---

### [15] JSON Canvas GitHub
**URL:** https://github.com/obsidianmd/jsoncanvas
**Grade:** VERIFIED

**Claims made:**
- Open file format for infinite canvas data
- MIT license
- .canvas extension
- Designed for longevity/readability/interoperability/extensibility
- 3.3k stars

**Source evidence:**
```
"An open file format for infinite canvas data."
Designed for longevity, readability, interoperability, extensibility.
Extension: .canvas, Format: JSON-based.
License: MIT, 85 commits, 3.3k stars, 139 forks.
```

**Assessment:** All claims verified including star count and design principles.

---

### [16] PyCanvas GitHub
**URL:** https://github.com/Bmitch44/PyCanvas
**Grade:** VERIFIED

**Claims made:**
- Python library for programmatic .canvas file generation
- Supports group/file/text nodes
- MIT license
- In active development (10 commits)

**Source evidence:**
```
Python library for creating dynamic visual diagrams programmatically.
"an open-source project for generating diagrams with nodes and edges."
"Nodes can represent various objects including groups, files, and text."
Status: In active development, 10 commits, MIT License.
```

**Assessment:** All claims verified. The "10 commits" status indicator and MIT license confirmed.

---

### [17] Obsidian Git GitHub
**URL:** https://github.com/Vinzent03/obsidian-git
**Grade:** VERIFIED

**Claims made:**
- Auto commit/pull/push
- Source control view, history view, diff view
- 30+ commands
- isomorphic-git for mobile
- Mobile limitations (no SSH, memory constraints, no rebase)
- Linux packaging notes

**Source evidence:**
```
Key Features
- Automatic commit, pull, push on configurable schedules
- Startup pull for remote changes

UI Components
- Source Control View: staging/unstaging, file-level commits
- History View: commit logs with metadata
- Diff View: side-by-side comparison

Commands: 30+ commands for change management, commits, sync, remote management, repo setup, utilities.

Architecture
Uses isomorphic-git (JavaScript Git reimplementation) for mobile. Desktop uses native Git.

Mobile Limitations
- No SSH authentication
- Memory-constrained repo sizes
- No rebase merge strategy

Linux Note
AppImage or native package recommended; Snap sandboxing and Flatpak restrictions create compatibility issues.
```

**Assessment:** All features and limitations verified. The "30+ commands" count and mobile constraints all confirmed.

---

### [18] URI Linux Setup
**URL:** https://amirrachum.com/obsidian-uri-linux/
**Grade:** VERIFIED

**Claims made:**
- Complete .desktop file contents for URI handler
- Placement at ~/.local/share/applications/
- MimeType=x-scheme-handler/obsidian
- %u parameter requirement
- update-desktop-database command
- xdg-open testing
- Chrome limitation

**Source evidence:**
```
.desktop File
Location: ~/.local/share/applications/obsidian.desktop
[complete .desktop file content shown]
MimeType=text/html;x-scheme-handler/obsidian;

Critical: %u parameter in Exec line passes URIs. Full paths, no tilde. No trailing whitespace.

Registration
update-desktop-database ~/.local/share/applications/

Testing
xdg-open "obsidian://new?vault=notes&name=note&content=content"

Known Limitation
"The single-user guide currently doesn't work for Chrome for some reason," Firefox works.
```

**Assessment:** All setup details verified including the Chrome limitation quote.

---

### [19] External Changes Forum
**URL:** https://forum.obsidian.md/t/is-there-a-way-to-auto-reload-changed-files/83006
**Grade:** VERIFIED

**Claims made:**
- No auto-reload of external file changes
- Must navigate away and back
- Data loss risk from editing stale cache
- No official response
- Context: Google Drive sync between two PCs

**Source evidence:**
```
Obsidian does NOT automatically reload files when external changes are detected.
User reported: "The note in PC 2 stays the same. I have to manually click to another note, then go back into that note to see the changes."

Risk: "if you didn't know the note updated on another PC, when you make a change to that file, it will overwrite the more recently updated file." Potential data loss from editing stale cached versions.

Setup context: Same vault on two Windows 10 machines, vault in Google Drive.

No official response from Obsidian maintainers. Topic auto-closed after 90 days.
```

**Assessment:** All claims verified including the lack of official response.

---

### [20] Steph Ango Vault
**URL:** https://stephango.com/vault
**Grade:** VERIFIED

**Claims made:**
- Vault organization by Obsidian CEO
- Minimal folders, most notes at root
- Admin folders (Attachments/Daily/Templates)
- YYYY-MM-DD naming
- Unresolved links as breadcrumbs
- Fractal journaling pattern
- 7-point rating scale
- Author is CEO of Obsidian

**Source evidence:**
```
(Steph Ango is CEO of Obsidian)

Folder Structure
Most notes at root. Reference folders: References (books, movies, people), Clippings (articles by others).
Admin folders (hidden): Attachments, Daily (YYYY-MM-DD.md), Templates.

Naming Conventions
- YYYY-MM-DD date format universally
- Daily notes: YYYY-MM-DD.md

Linking Strategy
"Unresolved links are important because they are breadcrumbs for future connections between things."

Properties System
7-point rating scale (1-7). Consistent types in .obsidian/types.json.

Automation Patterns
Fractal Journaling: daily → weekly → monthly → yearly.
```

**Assessment:** All claims verified including author's role as CEO.

---

### [21] Notion API Limits
**URL:** https://developers.notion.com/reference/request-limits
**Grade:** VERIFIED

**Claims made:**
- Rate limits (3 req/s average, HTTP 429 + Retry-After)
- Size limits (1000 blocks/request, 500KB payload, 2000 char rich text, 100 elements per array)

**Source evidence:**
```
Rate Limits
Primary: "an average of three requests per second" per integration, with burst allowance.
Error: "rate_limited" error code, HTTP 429.
Retry: Retry-After response header (integer, seconds).

Size Limits
- Maximum 1000 block elements per request
- 500KB overall payload size
- Rich text: 2000 characters
- Arrays (blocks/rich text): 100 elements
```

**Assessment:** All rate and size limits verified exactly as claimed.

---

### [22] Obsidian Headless
**URL:** https://obsidian.md/help/headless
**Grade:** VERIFIED

**Claims made:**
- Headless client for Sync/Publish without desktop app
- Node.js 22+
- npm install -g obsidian-headless
- ob login/sync/publish commands
- Open beta status
- Standalone from desktop CLI

**Source evidence:**
```
Obsidian Headless is "a headless client for Obsidian services" enabling vault synchronization via command line without the desktop application.

Key Distinction
Unlike Obsidian CLI (which controls the desktop app), Headless operates as a standalone client requiring no desktop installation.

System Requirements
Node.js version 22 or later. Install via npm:
npm install -g obsidian-headless

Authentication
ob login (with optional email, password, MFA parameters).

Available Services
- Headless Sync: Command-line Obsidian Sync functionality
- Headless Publish: Command-line Obsidian Publish functionality

Status: Currently in open beta phase.
```

**Assessment:** All claims verified including Node.js version requirement, npm installation, commands, and beta status.

---

### [23] XDA Developers
**URL:** https://www.xda-developers.com/obsidian-cli-is-the-new-best-way-to-automate-your-notes/
**Grade:** NOT FOUND

**Claims made:**
- Referenced in discovery for CLI automation analysis
- Not directly fetched

**Source evidence:**
No pre-fetched file available. Citations.md notes: "Not directly fetched. Data sourced from discovery agent search snippets."

**Assessment:** Source was not fetched during research. Cannot verify claims. The research document correctly discloses this in the citations file.

---

### [24] Git Issue #803
**URL:** https://github.com/Vinzent03/obsidian-git/issues/803
**Grade:** NOT FOUND

**Claims made:**
- Current limitation of no built-in automated conflict resolution in Git plugin

**Source evidence:**
No pre-fetched file available. Citations.md notes: "Not fetched; data sourced from discovery agent search snippets."

**Assessment:** Source was not fetched. Cannot verify the specific claim about conflict resolution limitations.

---

### [25] Custom Git Driver Blog
**URL:** https://blog.charlesdesneuf.com/articles/solving-obsidian-readwise-merge-conflicts-with-a-custom-git-driver/
**Grade:** NOT FOUND

**Claims made:**
- Custom Git merge drivers as workaround for conflict resolution

**Source evidence:**
No pre-fetched file available. Citations.md notes: "Not fetched; data sourced from discovery agent search snippets."

**Assessment:** Source was not fetched. Cannot verify.

---

### [26] Sync vs Git Comparison
**URL:** https://blog.thefix.it.com/how-does-obsidian-sync-differ-from-git-the-ultimate-comparison/
**Grade:** NOT FOUND

**Claims made:**
- Obsidian Sync: low-latency + mobile-native + 1-year version history
- Git: free + complex on mobile + full version control

**Source evidence:**
No pre-fetched file available. Citations.md notes: "Not fetched; data sourced from discovery agent search snippets."

**Assessment:** Source was not fetched. Cannot verify comparison claims.

---

### [27] Git Alternative Medium
**URL:** https://tr0.medium.com/obsidian-sync-alternative-obsidian-via-git-1dcd91459406
**Grade:** NOT FOUND

**Claims made:**
- iOS requires Working Copy app
- Android uses unstable JS Git implementation

**Source evidence:**
No pre-fetched file available. Citations.md notes: "Not fetched; data sourced from discovery agent search snippets."

**Assessment:** Source was not fetched. Cannot verify mobile Git implementation claims.

---

### [28] Troubleshoot Sync
**URL:** https://obsidian.md/help/sync/troubleshoot
**Grade:** NOT FOUND

**Claims made:**
- diff-match-patch for markdown merges
- last-modified-wins for non-markdown
- JSON merge for settings

**Source evidence:**
No pre-fetched file available. Citations.md notes: "Dynamic page; content not extractable via WebFetch. Data sourced from discovery agent search snippets."

**Assessment:** The research document correctly discloses that this dynamic page could not be extracted. The claims about merge strategies cannot be verified from fetched sources.

---

### [29] Logseq CLI npm
**URL:** https://www.npmjs.com/package/@logseq/cli
**Grade:** NOT FOUND

**Claims made:**
- Logseq CLI for CI/CD, offline operation, query, export, import, MCP server support

**Source evidence:**
No pre-fetched file available. Citations.md notes: "HTTP 403. Data sourced from discovery agent search snippets."

**Assessment:** npm page returned HTTP 403 during fetch. Cannot verify.

---

### [30] Logseq Plugin API
**URL:** https://plugins-doc.logseq.com/
**Grade:** NOT FOUND

**Claims made:**
- API modules for App, Editor, DB, Git, UI, Assets, FileStorage

**Source evidence:**
No pre-fetched file available. Citations.md notes: "Not fetched; data sourced from discovery agent search snippets."

**Assessment:** Source was not fetched. Cannot verify.

---

### [31] PKM Comparison 2026
**URL:** https://dasroot.net/posts/2026/03/obsidian-logseq-notion-pkm-systems-compared-2026/
**Grade:** NOT FOUND

**Claims made:**
- Obsidian: local-first + Zettelkasten + AI plugins
- Logseq: open-source + block-based + querying
- Notion: cloud + collaboration

**Source evidence:**
No pre-fetched file available. Citations.md notes: "Not fetched; data sourced from discovery agent search snippets."

**Assessment:** Source was not fetched. Cannot verify comparison.

---

### [32] MkDocs
**URL:** https://www.mkdocs.org/
**Grade:** NOT FOUND

**Claims made:**
- Fast/simple static site generation from Markdown, single YAML config

**Source evidence:**
No pre-fetched file available. Citations.md notes: "Not fetched; data sourced from discovery agent search snippets."

**Assessment:** Source was not fetched. Cannot verify.

---

### [33] Material for MkDocs
**URL:** https://squidfunk.github.io/mkdocs-material/
**Grade:** NOT FOUND

**Claims made:**
- Git integration plugins (revision dates, contributors)
- Automated GitHub Pages deployment

**Source evidence:**
No pre-fetched file available. Citations.md notes: "Not fetched; data sourced from discovery agent search snippets."

**Assessment:** Source was not fetched. Cannot verify.

---

### [34] File Explorer Reload
**URL:** https://github.com/mnaoumov/obsidian-file-explorer-reload
**Grade:** NOT FOUND

**Claims made:**
- Confirms bulk operations outside Obsidian aren't reflected without plugin/restart

**Source evidence:**
No pre-fetched file available. Citations.md notes: "Not fetched; data sourced from discovery agent search snippets."

**Assessment:** Source was not fetched. Cannot verify.

---

### [35] Wayland Configuration
**URL:** https://cstromblad.com/posts/how-to-make-obsidian-play-nice-with-wayland/
**Grade:** NOT FOUND

**Claims made:**
- Wayland-specific setup
- Blurry text fixes for Electron-based apps

**Source evidence:**
No pre-fetched file available. Citations.md notes: "Not fetched; data sourced from discovery agent search snippets."

**Assessment:** Source was not fetched. The research does cite [17] for Wayland mentions, but this specific blog was not fetched.

---

### [36] URI Forum Thread
**URL:** https://forum.obsidian.md/t/obsidian-uri-set-up-for-linux-obsidian-desktop/7494
**Grade:** NOT FOUND

**Claims made:**
- .desktop file examples and troubleshooting for Linux URI handler

**Source evidence:**
No pre-fetched file available. Citations.md notes: "Not fetched; data sourced from discovery agent search snippets."

**Assessment:** Source was not fetched. However, [18] provides similar content from a fetched source.

---

### [37] AppImage %u Bug
**URL:** https://forum.obsidian.md/t/on-linux-the-appimages-obsidian-desktop-file-is-missing-u-at-end-of-exec-line-which-is-needed-for-xdg-open-to-work/27563
**Grade:** NOT FOUND

**Claims made:**
- Critical %u parameter bug in AppImage .desktop file

**Source evidence:**
No pre-fetched file available. Citations.md notes: "Not fetched; data sourced from discovery agent search snippets."

**Assessment:** Source was not fetched. The %u requirement is verified in [18], but this specific bug report was not fetched.

---

## Findings

### Strengths

1. **High verification rate for core claims:** 22 out of 37 citations (59%) are VERIFIED with full source content supporting all claims.

2. **Accurate technical details:** All verified citations show precise technical accuracy including:
   - Version numbers, star counts, license types
   - API endpoint specifications
   - Command syntax and parameters
   - Configuration file formats
   - Security warnings

3. **No misrepresentation detected:** Zero PARTIAL or INACCURATE grades. Every fetched source fully supports the claims made.

4. **Proper disclosure:** The research documents clearly disclose which sources were not fetched and rely on discovery snippets (citations [23]-[37]).

### Weaknesses

1. **40% of citations not directly verified:** 15 citations rely on discovery agent search snippets rather than fetched source content.

2. **Key comparison data unverified:** The alternatives comparison section (citations [26], [27], [29], [30], [31]) lacks direct source verification.

3. **Sync conflict resolution details unverified:** Citation [28] about diff-match-patch and merge strategies could not be verified due to dynamic page content.

4. **Secondary sources for file reload behavior:** Citation [19] is a forum post without official response, representing user-reported behavior rather than official documentation.

### Recommendations

1. **For high-confidence use:** Rely on citations [1]-[22], which are all fully verified.

2. **For claims from citations [23]-[37]:** Treat as provisional. These are discovery-sourced and should be re-verified if used for critical decisions.

3. **For Obsidian Sync merge behavior (citation [28]):** Consider this a gap in the research. If precise merge strategy details are critical, additional verification is needed.

4. **Overall assessment:** The research is reliable for all core Obsidian integration capabilities. The unfetched sources are primarily comparison/alternative data and specific bug reports, not core functionality claims.

## Conclusion

This research demonstrates strong citation discipline. All directly fetched sources (22 citations) show complete accuracy with zero misrepresentation. The 15 unfetched citations are properly disclosed in the citations.md file. The core technical claims about Obsidian CLI, URI scheme, REST API, Dataview, Templater, Canvas, and Git integration are all fully verified.

The research is suitable for use in making architectural decisions about PA integration with Obsidian, with the caveat that alternative tool comparisons should be independently verified if those alternatives are being seriously considered.
