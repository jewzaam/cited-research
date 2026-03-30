# Citations

All sources were visited in-session via WebSearch or WebFetch on 2026-03-30.

**[1]** "Obsidian CLI." *Obsidian Help*, 2026.
<https://obsidian.md/help/cli>
**Tier:** 2
Data extracted: Complete CLI command reference (80+ commands), installation requirements (Obsidian 1.12+, app must be running), platform-specific setup (macOS/Linux/Windows), output formats (json/csv/tsv/yaml), TUI mode, parameter syntax.

**[2]** "Obsidian CLI." *Obsidian*, 2026.
<https://obsidian.md/cli>
**Tier:** 2
Data extracted: CLI landing page with four use cases (Develop, Collaborate, Automate, Tinker), key commands, installation steps, headless sync overview.

**[3]** "Obsidian 1.12 CLI: The Ultimate Guide." *wenhaofree blog*, 2026.
<https://blog.wenhaofree.com/en/posts/articles/obsidian-1-12-cli-ultimate-guide/>
**Tier:** 3
Data extracted: Practical CLI command examples, vault= parameter usage, daily note commands, search commands, limit parameter.

**[4]** "Obsidian URI." *Obsidian Help*, n.d.
<https://obsidian.md/help/Extending+Obsidian/Obsidian+URI>
**Tier:** 2
Data extracted: Complete URI scheme documentation — 7 actions (open, new, daily, unique, search, choose-vault, hook-get-address), parameters per action, encoding requirements, shorthand formats, x-callback-url support, Linux setup requirements.

**[5]** Vinzent03. "obsidian-advanced-uri." *GitHub*, 2026.
<https://github.com/Vinzent03/obsidian-advanced-uri>
**Tier:** 2
Data extracted: Advanced URI plugin capabilities — file operations, content editing (append/prepend/overwrite), frontmatter editing, command execution via URI, daily note integration, search/replace. v1.46.1, MIT license, 1.1k stars.

**[6]** coddingtonbear. "obsidian-local-rest-api." *GitHub*, n.d.
<https://github.com/coddingtonbear/obsidian-local-rest-api>
**Tier:** 2
Data extracted: Complete REST API documentation — 11 endpoint groups, CRUD operations, PATCH surgical edits (heading/block-reference/frontmatter targets), Bearer token auth on https://127.0.0.1:27124, Dataview DQL and JsonLogic search, periodic note management, command execution, API extensibility. MIT license.

**[7]** blacksmithgu. "obsidian-dataview." *GitHub*, n.d.
<https://github.com/blacksmithgu/obsidian-dataview>
**Tier:** 2
Data extracted: Dataview overview — vault as queryable database, frontmatter + inline fields, 4 query modes (DQL, DataviewJS, inline expressions, inline JS), security warning about JavaScript query privileges.

**[8]** "How to add Metadata." *Dataview Documentation*, n.d.
<https://blacksmithgu.github.io/obsidian-dataview/annotation/add-metadata/>
**Tier:** 2
Data extracted: YAML frontmatter syntax, inline field syntax (Key:: Value), bracket syntax for embedded fields, hidden key syntax (parentheses), field naming rules (sanitization to lowercase-dashes), supported data types (text, numbers, dates, objects), implicit fields (file.cday, file.outlinks, file.etags).

**[9]** "Query Types." *Dataview Documentation*, n.d.
<https://blacksmithgu.github.io/obsidian-dataview/queries/query-types/>
**Tier:** 2
Data extracted: Four query types — LIST (bullet-point file links), TABLE (tabular data with columns/AS aliases), TASK (interactive checkbox list that modifies source), CALENDAR (monthly view with date dots). WITHOUT ID variants, GROUP BY, WHERE support.

**[10]** SilentVoid13. "Templater." *GitHub*, 2026.
<https://github.com/SilentVoid13/Templater>
**Tier:** 2
Data extracted: Templater overview, security warning about arbitrary JavaScript and system command execution, GNU AGPLv3 license, v2.18.1, TypeScript (75%), 4.7k stars.

**[11]** "Introduction." *Templater Documentation*, n.d.
<https://silentvoid13.github.io/Templater/introduction.html>
**Tier:** 2
Data extracted: Template syntax (<% tp.function() %>), 9 internal function modules (tp.app, tp.config, tp.date, tp.file, tp.frontmatter, tp.hooks, tp.obsidian, tp.system, tp.web), user functions (scripts + system commands), command types.

**[12]** "Settings." *Templater Documentation*, n.d.
<https://silentvoid13.github.io/Templater/settings.html>
**Tier:** 2
Data extracted: Trigger on new file creation, folder templates (deepest-match logic), file regex templates, startup templates, template hotkeys, user script functions, user system command functions.

**[13]** liamcain. "obsidian-periodic-notes." *GitHub*, n.d.
<https://github.com/liamcain/obsidian-periodic-notes>
**Tier:** 2
Data extracted: Weekly and monthly notes support, template variables ({{title}}, {{date}}, {{time}}, {{sunday}}–{{saturday}}), default formats (gggg-[W]ww weekly, YYYY-MM monthly), Calendar plugin integration.

**[14]** "JSON Canvas Spec 1.0." *jsoncanvas.org*, n.d.
<https://jsoncanvas.org/spec/1.0>
**Tier:** 2
Data extracted: Complete specification — top-level nodes/edges arrays, 4 node types (text/file/link/group) with all properties, edge properties (id/fromNode/toNode/fromSide/toSide/fromEnd/toEnd/color/label), color format (hex or presets 1-6).

**[15]** "JSON Canvas." *GitHub (obsidianmd/jsoncanvas)*, n.d.
<https://github.com/obsidianmd/jsoncanvas>
**Tier:** 2
Data extracted: Open file format for infinite canvas data, MIT license, .canvas extension, designed for longevity/readability/interoperability/extensibility, 3.3k stars.

**[16]** Bmitch44. "PyCanvas." *GitHub*, n.d.
<https://github.com/Bmitch44/PyCanvas>
**Tier:** 4
Data extracted: Python library for programmatic .canvas file generation, supports group/file/text nodes, MIT license, in active development (10 commits).

**[17]** Vinzent03. "obsidian-git." *GitHub*, n.d.
<https://github.com/Vinzent03/obsidian-git>
**Tier:** 2
Data extracted: Git integration — auto commit/pull/push, source control view, history view, diff view, 30+ commands, isomorphic-git for mobile, mobile limitations (no SSH, memory constraints, no rebase), Linux packaging notes.

**[18]** Rachum, Amir. "Setting up Obsidian URI handler on Linux." *amirrachum.com*, n.d.
<https://amirrachum.com/obsidian-uri-linux/>
**Tier:** 3
Data extracted: Complete .desktop file contents for URI handler, placement at ~/.local/share/applications/, MimeType=x-scheme-handler/obsidian, %u parameter requirement, update-desktop-database command, xdg-open testing, Chrome limitation.

**[19]** "Is there a way to auto-reload changed files." *Obsidian Forum*, n.d.
<https://forum.obsidian.md/t/is-there-a-way-to-auto-reload-changed-files/83006>
**Tier:** 4
Data extracted: External file change behavior — no auto-reload, must navigate away and back, data loss risk from editing stale cache, no official response. Context: Google Drive sync between two PCs.

**[20]** Ango, Steph. "My Obsidian Vault." *stephango.com*, n.d.
<https://stephango.com/vault>
**Tier:** 3
Data extracted: Vault organization by Obsidian CEO — minimal folders, most notes at root, admin folders (Attachments/Daily/Templates), YYYY-MM-DD naming, unresolved links as breadcrumbs, fractal journaling pattern, 7-point rating scale. Note: Author is CEO of Obsidian.

**[21]** "Request limits." *Notion API Documentation*, n.d.
<https://developers.notion.com/reference/request-limits>
**Tier:** 2
Data extracted: Rate limits (3 req/s average, HTTP 429 + Retry-After), size limits (1000 blocks/request, 500KB payload, 2000 char rich text, 100 elements per array).

**[22]** "Obsidian Headless." *Obsidian Help*, 2026.
<https://obsidian.md/help/headless>
**Tier:** 2
Data extracted: Headless client for Sync/Publish without desktop app, Node.js 22+, npm install -g obsidian-headless, ob login/sync/publish commands, open beta status, standalone from desktop CLI.

**[23]** "Obsidian CLI is the New Best Way to Automate Your Notes." *XDA Developers*, 2026.
<https://www.xda-developers.com/obsidian-cli-is-the-new-best-way-to-automate-your-notes/>
**Tier:** 3
Data extracted: Referenced in discovery for CLI automation analysis. Not directly fetched.
**Access:** Not fetched; data sourced from discovery agent search snippets.

**[24]** "Obsidian Git plugin issue #803." *GitHub*, n.d.
<https://github.com/Vinzent03/obsidian-git/issues/803>
**Tier:** 4
Data extracted: Referenced in discovery — current limitation of no built-in automated conflict resolution in Git plugin.
**Access:** Not fetched; data sourced from discovery agent search snippets.

**[25]** "Solving Obsidian-Readwise merge conflicts with a custom git driver." *charlesdesneuf.com*, n.d.
<https://blog.charlesdesneuf.com/articles/solving-obsidian-readwise-merge-conflicts-with-a-custom-git-driver/>
**Tier:** 3
Data extracted: Referenced in discovery — custom Git merge drivers as workaround for conflict resolution.
**Access:** Not fetched; data sourced from discovery agent search snippets.

**[26]** "Obsidian Sync vs Git: The Ultimate Comparison." *thefix.it.com*, n.d.
<https://blog.thefix.it.com/how-does-obsidian-sync-differ-from-git-the-ultimate-comparison/>
**Tier:** 3
Data extracted: Referenced in discovery — Obsidian Sync low-latency + mobile-native + 1-year version history; Git free + complex on mobile + full version control.
**Access:** Not fetched; data sourced from discovery agent search snippets.

**[27]** "Obsidian Sync Alternative: Obsidian via Git." *Medium (tr0)*, n.d.
<https://tr0.medium.com/obsidian-sync-alternative-obsidian-via-git-1dcd91459406>
**Tier:** 3
Data extracted: Referenced in discovery — iOS requires Working Copy app, Android uses unstable JS Git implementation.
**Access:** Not fetched; data sourced from discovery agent search snippets.

**[28]** "Troubleshoot Obsidian Sync." *Obsidian Help*, n.d.
<https://obsidian.md/help/sync/troubleshoot>
**Tier:** 2
Data extracted: Referenced in discovery — diff-match-patch for markdown merges, last-modified-wins for non-markdown, JSON merge for settings.
**Access:** Dynamic page; content not extractable via WebFetch. Data sourced from discovery agent search snippets.

**[29]** "@logseq/cli." *npm*, n.d.
<https://www.npmjs.com/package/@logseq/cli>
**Tier:** 2
Data extracted: Referenced in discovery — Logseq CLI for CI/CD, offline operation, query, export, import, MCP server support.
**Access:** HTTP 403. Data sourced from discovery agent search snippets.

**[30]** "Logseq Plugin API." *plugins-doc.logseq.com*, n.d.
<https://plugins-doc.logseq.com/>
**Tier:** 2
Data extracted: Referenced in discovery — API modules for App, Editor, DB, Git, UI, Assets, FileStorage.
**Access:** Not fetched; data sourced from discovery agent search snippets.

**[31]** "Obsidian, Notion, Logseq: PKM Systems Compared 2026." *dasroot.net*, 2026.
<https://dasroot.net/posts/2026/03/obsidian-logseq-notion-pkm-systems-compared-2026/>
**Tier:** 3
Data extracted: Referenced in discovery — Obsidian local-first + Zettelkasten + AI plugins, 1500+ plugins; Logseq open-source + block-based + querying, 150+ plugins; Notion cloud + collaboration.
**Access:** Not fetched; data sourced from discovery agent search snippets. Plugin counts from search snippet context.

**[32]** "MkDocs." *mkdocs.org*, n.d.
<https://www.mkdocs.org/>
**Tier:** 2
Data extracted: Referenced in discovery — fast/simple static site generation from Markdown, single YAML config.
**Access:** Not fetched; data sourced from discovery agent search snippets.

**[33]** "Material for MkDocs." *squidfunk.github.io*, n.d.
<https://squidfunk.github.io/mkdocs-material/>
**Tier:** 2
Data extracted: Referenced in discovery — Git integration plugins (revision dates, contributors), automated GitHub Pages deployment.
**Access:** Not fetched; data sourced from discovery agent search snippets.

**[34]** "File Explorer Reload Plugin." *GitHub (mnaoumov)*, n.d.
<https://github.com/mnaoumov/obsidian-file-explorer-reload>
**Tier:** 4
Data extracted: Referenced in discovery — confirms bulk operations outside Obsidian aren't reflected without plugin/restart.
**Access:** Not fetched; data sourced from discovery agent search snippets.

**[35]** "Obsidian Wayland Configuration Guide." *cstromblad.com*, n.d.
<https://cstromblad.com/posts/how-to-make-obsidian-play-nice-with-wayland/>
**Tier:** 3
Data extracted: Referenced in discovery — Wayland-specific setup, blurry text fixes for Electron-based apps.
**Access:** Not fetched; data sourced from discovery agent search snippets.

**[36]** "Obsidian URI set up for Linux." *Obsidian Forum*, n.d.
<https://forum.obsidian.md/t/obsidian-uri-set-up-for-linux-obsidian-desktop/7494>
**Tier:** 4
Data extracted: Referenced in discovery — .desktop file examples and troubleshooting for Linux URI handler.
**Access:** Not fetched; data sourced from discovery agent search snippets.

**[37]** "AppImage desktop file missing %u." *Obsidian Forum*, n.d.
<https://forum.obsidian.md/t/on-linux-the-appimages-obsidian-desktop-file-is-missing-u-at-end-of-exec-line-which-is-needed-for-xdg-open-to-work/27563>
**Tier:** 4
Data extracted: Referenced in discovery — critical %u parameter bug in AppImage .desktop file.
**Access:** Not fetched; data sourced from discovery agent search snippets.
