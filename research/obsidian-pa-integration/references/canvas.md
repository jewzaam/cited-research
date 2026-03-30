# Canvas

## Dimension Coverage

This reference covers Obsidian's Canvas feature, the JSON Canvas open specification, and programmatic generation for task boards and relationship maps.

For source details, see [citations.md](../citations.md).

## JSON Canvas Specification (v1.0)

JSON Canvas is "an open file format for infinite canvas data" [15]. It uses `.canvas` files containing standard JSON [14][15]. The format was originally developed for Obsidian but is designed to be freely implemented by any application [15].

### Top-Level Structure

```json
{
  "nodes": [...],
  "edges": [...]
}
```

Both arrays are optional [14].

### Node Types

All nodes share these required properties: `id` (string), `type` (string), `x`/`y` (integers, pixel position), `width`/`height` (integers, pixel dimensions), and optional `color` [14].

| Type | Additional Properties |
|---|---|
| `text` | `text` (required, Markdown content) [14] |
| `file` | `file` (required, file path), `subpath` (optional, starts with `#`) [14] |
| `link` | `url` (required) [14] |
| `group` | `label` (optional), `background` (optional, image path), `backgroundStyle` (optional: cover/ratio/repeat) [14] |

### Edge Properties

| Property | Required | Description |
|---|---|---|
| `id` | Yes | Unique identifier [14] |
| `fromNode` | Yes | Source node ID [14] |
| `toNode` | Yes | Target node ID [14] |
| `fromSide` / `toSide` | No | top, right, bottom, left [14] |
| `fromEnd` / `toEnd` | No | none or arrow (defaults: none, arrow) [14] |
| `color` | No | canvasColor format [14] |
| `label` | No | Edge label text [14] |

### Color Format

Accepts hex format (`"FF0000"`) or preset numbers 1-6 mapping to: 1=red, 2=orange, 3=yellow, 4=green, 5=cyan, 6=purple [14].

### License and Adoption

MIT license [15]. 3.3k stars on GitHub [15]. Designed for longevity, readability, interoperability, and extensibility [15].

## Programmatic Generation

### Python (PyCanvas)

PyCanvas is "an open-source project for generating diagrams with nodes and edges" [16]. It supports group, file, and text node types [16]. MIT license, in active development (10 commits) [16].

### Direct JSON Generation

Since `.canvas` files are standard JSON, any language can generate them by constructing the nodes/edges arrays and writing valid JSON [14][15]. No special tooling required beyond a JSON serializer.

### Example: PA-Generated Task Board

```json
{
  "nodes": [
    {"id": "g1", "type": "group", "x": 0, "y": 0, "width": 400, "height": 600, "label": "To Do", "color": "1"},
    {"id": "g2", "type": "group", "x": 450, "y": 0, "width": 400, "height": 600, "label": "In Progress", "color": "2"},
    {"id": "g3", "type": "group", "x": 900, "y": 0, "width": 400, "height": 600, "label": "Done", "color": "4"},
    {"id": "t1", "type": "text", "x": 20, "y": 50, "width": 360, "height": 100, "text": "## Review Q1 report\nDue: 2026-04-01"}
  ],
  "edges": []
}
```

Calculated from [14]: Group nodes define columns, text nodes within groups represent cards, edges define dependencies between tasks.

## PA Integration Assessment

**Built-in vs plugin:** Canvas is a built-in core feature [15]. The `.canvas` format is an open standard [15].

**Requires Obsidian running:** No — `.canvas` files are plain JSON that the PA can write directly to disk. Obsidian renders them when opened.

**Works against files on disk:** Yes — this is the strongest programmatic generation story of any Obsidian feature. The PA writes JSON, the user sees a visual board.

## Gaps and Limitations

- No documented limits on canvas size, node count, or edge count [14]
- No Canvas-specific plugin API events or hooks documented [14]
- z-order/layering for overlapping nodes not specified in the spec [14]
- PyCanvas is early-stage (10 commits) and may not cover all spec features [16]
- Community plugins for task boards (Kanvas, Task Board) exist but their `.canvas` manipulation APIs are not documented
