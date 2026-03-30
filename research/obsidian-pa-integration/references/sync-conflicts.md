# Sync and Conflict Handling

## Dimension Coverage

This reference covers how Obsidian handles external file changes, conflict resolution in Obsidian Sync, and git-based sync as an alternative.

For source details, see [citations.md](../citations.md).

## External File Change Detection

Obsidian does **not** automatically reload files modified externally while they are open in an editor pane [19]. A user reported: "The note in PC 2 stays the same. I have to manually click to another note, then go back into that note to see the changes" [19].

### Behavior Summary

| Scenario | Behavior |
|---|---|
| File modified externally while open | Not auto-reloaded; must navigate away and back [19] |
| New file added to vault directory | May not appear without restart [34] |
| Bulk operations (copy/move/delete) | Not reflected in File Explorer; requires restart or "Reload app without saving" [34] |
| File watcher on network drives | Limited detection, especially in subdirectories [19] |

### Risk

"If you didn't know the note updated on another PC, when you make a change to that file, it will overwrite the more recently updated file" [19]. This is a **data loss risk** when a PA writes to a file that the user has open and unsaved.

### Mitigation for PA Integration

1. **Write to files the user is unlikely to have open** — dedicated PA folders (Tasks/, Calendar/) [20]
2. **Use append-only operations** — reduces overwrite risk
3. **Use CLI or REST API when Obsidian is running** — lets Obsidian mediate file access [1][6]
4. **Write when Obsidian is not running** — safest for bulk operations, then let Obsidian pick up changes on next launch

## Obsidian Sync Conflict Resolution

Obsidian Sync uses different merge strategies by file type [28]:

| File Type | Strategy |
|---|---|
| Markdown | Automatic merging via Google's diff-match-patch algorithm (three-way merge) [28] |
| Non-markdown (images, PDFs, Canvas) | Last-modified-wins [28] |
| JSON settings files | Special merge — applies local keys on top of remote keys [28] |

Version 1.9.7+ allows user configuration of conflict handling [28]. The "Create conflict file" option keeps the remote version in the original file and saves local changes to a separate conflict file [28].

**Note:** Obsidian Sync data for [28] was sourced from discovery agent search snippets because the help page uses dynamic content loading that WebFetch could not extract.

## Git-Based Sync

### Obsidian Git Plugin

The Obsidian Git plugin provides automatic commit/pull/push on configurable schedules [17]. It uses `isomorphic-git` (JavaScript Git reimplementation) on mobile and native Git on desktop [17].

| Feature | Desktop | Mobile |
|---|---|---|
| Automatic sync | Yes [17] | Yes (limited) [17] |
| SSH authentication | Yes [17] | No [17] |
| Submodule support | Yes (opt-in) [17] | No [17] |
| Rebase merge | Yes [17] | No [17] |
| Large repos | Yes [17] | May crash [17] |

### Conflict Handling in Git

The Git plugin does **not** have built-in automated conflict resolution [24]. Options:

1. Resolve manually in terminal [24]
2. Use custom Git merge drivers for specific file types [25]
3. Add `workspace.json`, `workspace-mobile.json` to `.gitignore` to prevent common conflicts [27]

### Obsidian Sync vs Git

| Property | Obsidian Sync | Git |
|---|---|---|
| Cost | Paid subscription [26] | Free (with GitHub/GitLab) [26] |
| Mobile | Native support [26] | Complex (iOS: Working Copy; Android: unstable JS) [27] |
| Latency | Low [26] | Depends on schedule [17] |
| Version history | ~1 year [26] | Full history [26] |
| Branching | No | Yes [26] |
| Conflict resolution | Auto-merge (markdown) [28] | Manual or custom drivers [24][25] |

## PA Integration Assessment

**For a git-backed PA:** Git sync is the natural choice since the PA already uses a git-backed JSON repo. The PA can commit vault changes through standard git operations. The key constraint is that the Obsidian Git plugin should be configured to pull before pushing to avoid divergence [17].

**Built-in vs plugin:** File watching is built-in (but limited). Obsidian Sync is a paid service. Git sync requires the community Obsidian Git plugin [17].

**Requires Obsidian running:** File writing works without Obsidian. Sync plugins require Obsidian running.

## Gaps and Limitations

- Obsidian's file watcher behavior lacks official documentation — behavior is inferred from forum reports [19][34]
- diff-match-patch merge details for Sync were not directly verifiable (dynamic page) [28]
- No webhooks or filesystem event callbacks for external tools to subscribe to [6]
- Git plugin crash risk on mobile with large repos [17]
- Concurrent write safety between PA and Obsidian is not guaranteed [19]
