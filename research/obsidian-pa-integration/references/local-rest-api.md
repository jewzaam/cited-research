# Local REST API Plugin

## Dimension Coverage

This reference covers the obsidian-local-rest-api community plugin — its CRUD operations, surgical editing, authentication, search, and external integration.

For source details, see [citations.md](../citations.md).

## Overview

The plugin provides "scripts, browser extensions, and AI agents a direct line into your Obsidian vault via a secure, authenticated REST API" [6]. It runs on `https://127.0.0.1:27124` with a self-signed HTTPS certificate and Bearer token authentication [6].

## API Endpoints

| Endpoint | Methods | Purpose |
|---|---|---|
| `/vault/{path}` | GET, PUT, PATCH, POST, DELETE | File CRUD operations [6] |
| `/active/` | GET, PUT, PATCH, POST, DELETE | Currently open file [6] |
| `/periodic/{period}/` | GET, PUT, PATCH, POST, DELETE | Today's periodic note [6] |
| `/periodic/{period}/{year}/{month}/{day}/` | GET, PUT, PATCH, POST, DELETE | Specific date periodic note [6] |
| `/search/simple/` | POST | Full-text search [6] |
| `/search/` | POST | Dataview DQL or JsonLogic queries [6] |
| `/commands/` | GET | List available commands [6] |
| `/commands/{commandId}/` | POST | Execute command [6] |
| `/tags/` | GET | List tags with counts [6] |
| `/open/{path}` | POST | Open file in UI [6] |
| `/` | GET | Server status (no auth required) [6] |

## Surgical Editing (PATCH)

The PATCH method supports three operations specified via HTTP headers [6]:

| Operation | Description |
|---|---|
| Append | Add content after a target [6] |
| Prepend | Add content before a target [6] |
| Replace | Substitute target content [6] |

Target types [6]:

| Target Type | Description |
|---|---|
| `heading` | Modify specific section by heading name |
| `block-reference` | Edit content at block references |
| `frontmatter` | Alter YAML frontmatter field values |

Example: Replace a frontmatter "status" field to "done" using the Replace operation with JSON content-type [6].

## Search Functionality

| Mode | Content-Type / Method | Description |
|---|---|---|
| Simple search | `/search/simple/?query=terms` | Obsidian's built-in fuzzy search with context snippets [6] |
| Dataview DQL | `application/vnd.olrapi.dataview.dql+txt` | TABLE queries returning matching files with field values [6] |
| JsonLogic | `application/vnd.olrapi.jsonlogic+json` | Evaluate expressions against note metadata [6] |

## Authentication

| Property | Detail |
|---|---|
| Protocol | HTTPS with self-signed certificate [6] |
| Auth method | Bearer token in `Authorization: Bearer <key>` header [6] |
| Key location | Settings → Local REST API [6] |
| Status endpoint | `/` requires no auth [6] |
| Certificate download | `https://127.0.0.1:27124/obsidian-local-rest-api-certificate.crt` [6] |

## Python Integration

```bash
curl -k -H "Authorization: Bearer <key>" \
  https://127.0.0.1:27124/vault/path/to/note.md
```
[6]

A third-party Python wrapper (`obsidian_python_api`) exists but its maintenance status is unknown [6]. Direct `requests` library usage is straightforward with certificate handling [6].

## API Extensibility

The plugin supports custom route registration by other plugins via an "API extension interface" [6].

## PA Integration Assessment

**Plugin-dependent:** Yes — this is a community plugin, not built-in.

**Requires Obsidian running:** Yes — the REST API server is hosted by the Obsidian plugin.

**Works against files on disk:** No — operates through Obsidian's plugin system.

**Best fit for PA:** This is the strongest programmatic integration point for a PA that needs CRUD + search + surgical edits while Obsidian is running. The REST API is the most natural interface for a Python CLI application.

## Gaps and Limitations

- Requires Obsidian to be running [6]
- Self-signed certificate requires special handling in HTTP clients [6]
- No documented rate limits or performance characteristics [6]
- Concurrent access behavior not documented [6]
- No webhooks or event subscriptions for vault changes [6]
- Network binding is localhost only — no remote access [6]
- License: MIT [6]
