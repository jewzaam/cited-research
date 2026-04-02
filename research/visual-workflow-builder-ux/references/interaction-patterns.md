# Interaction Patterns

Covers Dimension 1: node palettes, node addition methods, editing approaches, zoom/pan, minimap, grid/alignment, and auto-layout algorithms.

See [citations.md](../citations.md) for full source details.

## Node Palette Designs

| Tool | Palette Type | Location | Search/Filter | Keyboard Access |
|------|-------------|----------|---------------|-----------------|
| n8n | Fixed sidebar | Left panel | Filter input above palette | N key opens with search focus [13] |
| Node-RED | Fixed sidebar | Left panel | Filter input above palette | Ctrl/⌘-p toggle [8] |
| Retool | Tab-based sidebar | Left panel ("Blocks" tab) | Via Blocks tab | Standard tab navigation [1] |
| Power Automate Desktop | Actions pane | Side panel | Browse/search actions | Standard [34] |

Most workflow builders use a **left-side fixed palette** with categorized node lists [1][8][13]. Node-RED organizes nodes into collapsible categories with "Inputs, outputs and functions" at the top, and provides buttons to "collapse or expand all categories" simultaneously [8]. The palette can be hidden via a toggle button that appears "when the mouse is over the palette" [8].

n8n implements progressive disclosure in its palette: "showing users only the tools and options immediately relevant to their current task, while keeping additional functionality accessible but not distracting" [13].

## Node Addition Methods

| Method | Tools Using It | Description |
|--------|---------------|-------------|
| Drag from palette | n8n, Node-RED, Retool, Power Automate | Standard pattern — drag node from sidebar to canvas [1][8][13] |
| Click-to-add | Various (inferred) | Reduces screen traversal distance — theoretical benefit per Fitts's Law [25], not documented as named pattern in sources |
| Button-edge insertion | React Flow | Edge buttons trigger custom actions for inline node insertion [33] |
| Add-on-edge-drop | React Flow | Drop connection on empty canvas creates new node at drop position [33] |
| Plus icon on nodes | n8n | + icon on right side of existing nodes to add connected nodes [13] |

React Flow's add-node-on-edge-drop pattern uses `onConnectEnd` callback with `screenToFlowPosition()` coordinate conversion to create and auto-connect nodes at the drop position [33]. This eliminates intermediate steps — "users create nodes directly where needed during connection operations" [33].

## Editing Approaches

| Approach | When Used | Tools |
|----------|-----------|-------|
| Side panel (right) | Complex configuration | Retool (split view), n8n (contextual properties) [1][13] |
| Inline editing | Quick changes | n8n (expression editor), some node label editing [13] |
| Hybrid | Both available | Most modern builders combine inline + panel [13] |

Retool provides a **Split View** feature where users "open individual blocks in a dedicated editing pane for complex code, accessible via 'Open in tab' within block toolbars" [1]. n8n uses an expression system "enabling inline data manipulation without context switching" [13].

## Zoom, Pan, and Navigation Controls

| Feature | Implementation |
|---------|---------------|
| Panning | Click-drag on canvas; minimap drag [1][2] |
| Zooming | Controls, Cmd/Ctrl+scroll, trackpad pinch [1] |
| Fit to screen | "Fit view" button adjusts to show entire workflow [1] |
| Auto-pan on focus | React Flow: focused nodes scroll into view via `autoPanOnNodeFocus` [5] |

Retool provides zoom via "controls, keyboard shortcuts (Cmd/Ctrl + scroll), or trackpad pinch-to-zoom" with a "Fit view" button [1]. n8n places "zoom controls centered below canvas ensuring consistent accessibility regardless of workflow size" [13].

## Minimap

React Flow's `<MiniMap />` renders "an overview of your flow" by displaying "each node as an SVG element" and showing "where the current viewport is in relation to the rest of the flow" [2]. Key props:

- `pannable`: Drag within minimap to reposition viewport [2]
- `zoomable`: Scroll to adjust zoom levels [2]
- `ariaLabel`: Screen reader label (default: "Mini Map") [2]
- Default position: bottom-right corner [2]

## Auto-Layout Algorithms

| Algorithm | Size | Strengths | Weaknesses |
|-----------|------|-----------|------------|
| d3-hierarchy | 136 KB | Lightweight, basic linear flows | "No support for dynamic node sizing or spacing" [14] |
| Dagre.js | Moderate | "Dynamic spacing and more polished layout" | "Fixed node positioning wasn't supported out of the box" [14] |
| ELK.js | 7.8 MB | Dynamic sizing, custom spacing, smooth branching | Heavy file size [14] |

A real-world case study documented progression from d3-hierarchy to Dagre to ELK as workflow complexity increased [14]. ELK "proved to be the best fit for our use case, allowing us to fully realise the complex, interactive workflows" [14]. The team created a custom `useAutoLayout` hook to trigger recalculations based on user interactions [14].

## Drag-and-Drop Visual Feedback

Key patterns for drag-and-drop UX [15]:

- **Visual lift & elevation**: Elements float with shadows or become semi-transparent
- **Drop zone highlighting**: "The moment a user picks something up, your interface should shift to guide them" [15]
- **Drag handles**: Six-dot icon patterns (used by Notion, Zapier) [15]
- **Cursor transformation**: Changes to "grab" hand icon on hover [15]

Zapier's visual editor supports drag-and-drop for "both individual steps and entire paths" — previously, "reordering required sidebar navigation" [23].

## Gaps and Limitations

- No quantitative usability studies comparing sidebar vs floating vs search-first palette designs were found.
- Touch/mobile interaction patterns for workflow builders are undocumented in sources found.
- Grid snapping and alignment guide implementations are largely undocumented in workflow builder literature.
