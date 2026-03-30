# URI Scheme

## Dimension Coverage

This reference covers Obsidian's built-in `obsidian://` URI protocol and the Advanced URI community plugin.

For source details, see [citations.md](../citations.md).

## Built-in URI Scheme

Obsidian URI is "a custom URI protocol supported by Obsidian that lets you trigger various actions" [4]. The format is `obsidian://action?param1=value&param2=value` [4].

### Available Actions

| Action | Purpose | Key Parameters |
|---|---|---|
| `open` | Open vault or specific file | vault, file, path, paneType, prepend, append [4] |
| `new` | Create new note | vault, name/file, content, clipboard, silent, append, overwrite, x-success [4] |
| `daily` | Open/create daily note | Same as `new` (requires Daily Notes plugin) [4] |
| `unique` | Create unique note | vault, paneType, content, clipboard (requires Unique Note Creator plugin) [4] |
| `search` | Open search | vault, query [4] |
| `choose-vault` | Open vault switcher | None [4] |
| `hook-get-address` | Hook app integration | Returns Markdown link via x-success [4] |

### Encoding Requirements

Values must be URI-encoded: forward slashes → `%2F`, spaces → `%20` [4]. Navigate to headings with `Note%23Heading`, blocks with `Note%23%5EBlock` [4].

### Shorthand Formats

- `obsidian://vault/my vault/my note` — equivalent to open action [4]
- `obsidian:///absolute/path/to/my note` — absolute path format [4]

### x-callback-url Support

When `x-success` is provided, Obsidian returns: name (filename without extension), url (obsidian:// URI), file (file:// URL, desktop only) [4].

### Platform Registration

| Platform | Setup |
|---|---|
| Windows/macOS | Automatic on first run [4] |
| Linux | Requires `.desktop` file with `Exec=executable %u` [4] |

## Advanced URI Plugin (Community)

"Advanced URI allows you to control many different features in Obsidian just by opening some URIs" [5]. Uses the `obsidian://adv-uri?` prefix [5].

### Capabilities Beyond Built-in

| Feature | Built-in URI | Advanced URI |
|---|---|---|
| Open files | Yes [4] | Yes [5] |
| Create notes | Yes [4] | Yes [5] |
| Append/prepend content | Limited (`open` action only) [4] | Full support with `mode=append/prepend/overwrite` [5] |
| Search and replace | No | Yes [5] |
| Command execution | No | Yes (via `commandid=`) [5] |
| Frontmatter editing | No | Yes [5] |
| Canvas movement | No | Yes [5] |
| Heading/block navigation | Yes [4] | Yes [5] |
| Daily note integration | Yes [4] | Yes (with append/prepend modes) [5] |
| Clipboard integration | Yes [4] | Yes (`clipboard=true`) [5] |

### Key Examples

```
# Append clipboard to daily note
obsidian://adv-uri?vault=<vault>&daily=true&clipboard=true&mode=append

# Execute command by ID
obsidian://adv-uri?vault=<vault>&filepath=<file>&commandid=workspace%3Aexport-pdf

# Navigate to heading
obsidian://adv-uri?vault=<vault>&filepath=my-file&heading=Goal
```
[5]

### Technical Details

TypeScript (99.3%), MIT license, v1.46.1 (January 26, 2026), 1.1k stars, 87 releases [5].

## PA Integration Assessment

**Built-in vs plugin:** The built-in URI scheme handles basic open/create/search. Content manipulation (append/prepend) and command execution require the Advanced URI plugin [4][5].

**Requires Obsidian running:** Yes — URIs launch Obsidian if not running, but the target vault must be openable [4].

**Works against files on disk:** No — URIs operate through the Obsidian application, not directly on files.

## Gaps and Limitations

- Built-in URI cannot append/prepend content without the `open` action's limited support [4]
- Linux requires manual `.desktop` file configuration [4][18]
- Chrome may not handle `obsidian://` URIs on Linux [18]
- All URI actions require Obsidian to be running (or will launch it) [4]
- URI length limits not documented [4]
- Double-encoding may be needed for xdg-open on Linux (unverified)
