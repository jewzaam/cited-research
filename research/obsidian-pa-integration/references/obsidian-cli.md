# Obsidian CLI

## Dimension Coverage

This reference covers the official Obsidian CLI, the separate headless client, and their capabilities for programmatic vault interaction.

For source details, see [citations.md](../citations.md).

## Official CLI (v1.12+)

The Obsidian CLI was released in version 1.12.0 (February 2026) [1][2]. It provides over 80 commands organized across file management, daily notes, search, tasks, properties, sync, publishing, and developer tools [1].

### Requirements

| Requirement | Detail |
|---|---|
| Obsidian version | 1.12+ (minimum 1.12.4 for Windows) [1] |
| App must be running | Yes — "If Obsidian is not running, the first command you run launches Obsidian" [1] |
| Enable in settings | Settings → General → "Command line interface" [1] |
| Registration | Follow on-screen prompts to add binary to PATH [1] |

**Critical limitation for PA integration:** The CLI requires the Obsidian desktop app to be running. It is not a standalone headless tool [1].

### Platform Setup

| Platform | Setup |
|---|---|
| macOS | Adds binary to PATH via `~/.zprofile` [1] |
| Linux | Creates symlink at `/usr/local/bin/obsidian` (requires sudo); AppImage and Snap have special considerations [1] |
| Windows | Requires terminal redirector (`Obsidian.com`) added during 1.12.4+ installation [1] |

### Command Reference

| Category | Commands | Example |
|---|---|---|
| File operations | create, read, append, move, delete, rename | `obsidian create name="Note" content="text"` [3] |
| Daily notes | daily, daily:append, daily:prepend, daily:path | `obsidian daily:append content="text"` [3] |
| Search | search, search:context, backlinks, links, orphans, deadends | `obsidian search query="term"` [3] |
| Tasks | tasks, task (toggle/done/todo) | `obsidian tasks daily total` [3] |
| Properties | property:set, property:remove, property:read | — [1] |
| Sync | sync, sync:status, sync:history, diff, history | — [1] |
| Publishing | publish:add, publish:remove, publish:status | — [1] |
| Plugins | plugin:enable, plugin:disable, plugin:reload, theme:set | `obsidian plugin:reload id=plugin-name` [3] |
| Developer | devtools, dev:screenshot, eval, dev:console | — [1] |

### Parameter Syntax

Commands use `parameter=value` format [1]. Multi-vault targeting uses `vault="Name"` as the first argument [3]. Output supports json, csv, tsv, yaml formats [1]. Clipboard support via `--copy` flag [1]. Multiline content uses `\n` for newlines and `\t` for tabs [1].

### Operating Modes

1. **Single commands:** `obsidian help` [1]
2. **Terminal UI (TUI):** Interactive mode with autocomplete and command history [1]

## Headless Client (obsidian-headless)

A separate official package distinct from the desktop CLI [22].

| Property | Detail |
|---|---|
| Purpose | Sync and Publish without GUI [22] |
| Install | `npm install -g obsidian-headless` [22] |
| Node.js requirement | Version 22 or later [22] |
| Status | Open beta [22] |
| Requires desktop app | No — standalone client [22] |

### Headless Commands

- `ob login` — authenticate (optional email/password/MFA parameters) [22]
- `ob sync` / `ob sync --continuous` — synchronize vault [22]
- `ob publish` — publish vault [22]

**Key distinction:** The headless client provides Sync and Publish capabilities only. It does not support the full 80+ command set available in the desktop CLI [22][1].

## PA Integration Assessment

| Capability | CLI | Headless | Works without Obsidian running |
|---|---|---|---|
| Read notes | Yes [1] | No | No |
| Write/create notes | Yes [1] | No | No |
| Append to notes | Yes [1] | No | No |
| Search vault | Yes [1] | No | No |
| Manage tasks | Yes [1] | No | No |
| Set properties | Yes [1] | No | No |
| Sync | Yes [1] | Yes [22] | Headless only |
| Publish | Yes [1] | Yes [22] | Headless only |

**Built-in:** CLI is part of Obsidian core (v1.12+). Not a plugin.
**Requires Obsidian running:** Yes for CLI, no for headless (but headless is Sync/Publish only).

## Gaps and Limitations

- CLI requires Obsidian desktop app to be running — not suitable for fully headless server automation [1]
- Headless client only covers Sync and Publish — no file CRUD operations [22]
- CLI was released February 2026 and may still have breaking changes [2]
- Linux AppImage and Snap installations have "special considerations" for CLI setup [1]
- No documented batch/piping support beyond basic shell piping [1]
