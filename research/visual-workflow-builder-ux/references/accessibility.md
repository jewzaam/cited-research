# Accessibility

Covers Dimension 7: keyboard navigation, screen reader support, WCAG compliance, WAI-ARIA patterns, React Flow accessibility, alternative views, and color-blind design.

See [citations.md](../citations.md) for full source details.

## Keyboard Navigation

### React Flow Built-in Support

React Flow provides comprehensive keyboard accessibility out of the box [5]:

| Interaction | Key | Behavior |
|------------|-----|----------|
| Navigate nodes/edges | Tab | "Moves focus through all focusable nodes and edges" with tabIndex={0} and role="group" [5] |
| Select | Enter/Space | Selects focused element [5] |
| Deselect | Escape | Clears selection [5] |
| Move node | Arrow keys | When nodesDraggable and nodesFocusable both enabled [5] |
| Fast move | Shift + Arrow | Increases movement speed [5] |
| Auto-pan | autoPanOnNodeFocus | Focused nodes scroll into view automatically [5] |

### Azure ML Designer

Pipeline graph organized as nested list for screen readers [17]:
- Tab: Move to first node → each port → next node [17]
- Up/down arrows: Navigate between nodes by position in graph [17]
- Ctrl+Shift+H: Focus on canvas [17]
- Ctrl+G: Navigate to connected ports [17]

### Accessible Workflow Builder (Synergy Codes)

WCAG 2.1 compliant workflow builder with [18]:
- WSAD keys for movement, F2 for editing, Delete/Backspace for removal [18]
- "Focus indicators highlight the active element, giving users full control without a mouse" [18]
- ARIA attributes "to describe hierarchy shifts, status changes, and transitions in real time" [18]
- Lazy loading "renders only visible diagram elements in real-time" for performance [18]

## Screen Reader Support

### MIT CSAIL Research (2022)

Three design dimensions for accessible data visualization [30]:

1. **Structure**: Chart elements as traversable forms (lists, tables, trees) [30]
2. **Navigation**: Structural (hierarchy), Spatial (directional), Targeted (direct jumping) [30]
3. **Description**: Text narration with configurable verbosity [30]

Technical approach: "in-memory data structures" with event listeners updating position on keypresses, writing to "ARIA-Live regions" for screen reader output [30]. Arrow keys for structural navigation; WASD for spatial grid [30].

Key finding: Screen reader users engage in "constant hypothesis testing and pattern-making" while building mental models [30]. All 13 participants rated prototypes as "more-than-useful" [30].

### Azure ML Designer Screen Reader Testing

Tested with Narrator and JAWS [17]. Reader announces port information including whether port is valid connection source [17]. Component connection workflow: Tab to focus ports → Access key + C → Tab through destinations → Enter to complete [17].

## WAI-ARIA and Drag-and-Drop Accessibility

**No official WAI-ARIA drag-drop pattern exists** (Agent D discovery). The deprecated `aria-grabbed` and `aria-dropeffect` properties have no official replacement.

### React Aria (Adobe) — Current Best Practice

Provides "full parity for keyboard and screen reader input" [11]:
- Enter to initiate drag → Tab to navigate targets → Enter to drop [11]
- During drag mode, "all elements other than valid drop targets are hidden from screen readers" [11]
- Prompts localized into 30+ languages [11]
- Fixed "at least 13 different browser bugs" in HTML drag-and-drop API [11]
- No standard existed — team "conducted extensive research, prototyping interactions across diverse devices" [11]

### Four Accessible Drag-and-Drop Patterns (Salesforce)

Jesse Hausler identified four patterns [16]:

1. **List sorting**: ARIA listbox + arrow keys + assertive live regions [16]
2. **Canvas objects**: Coordinate-based positioning + keyboard controls [16]
3. **Between-list transfer**: WAI-ARIA menu patterns with popup buttons [16]
4. **1D resizing**: Native HTML `<input type="range">` with inherent screen reader feedback [16]

Core principle: Each pattern communicates "Identity, Operation, State" [16].

## SVG vs Canvas for Accessibility

Strong consensus that SVG is preferable for accessible graph visualization (Agent D discovery):

- SVG creates DOM elements accessible to screen readers individually
- SVG elements naturally receive keyboard focus
- Canvas renders as "single flat bitmap with no inherent structure"
- Canvas accessibility requires building parallel ARIA/JavaScript structure

React Flow uses SVG for edges and HTML divs for nodes (from React Flow documentation; [2] confirms SVG rendering in minimap), providing a reasonable accessibility foundation.

## Color-Blind Safe Design

Status indicators should use at least two visual elements — never color alone (Agent D discovery):

| Safe Combination | Unsafe |
|-----------------|--------|
| Blue + Orange | Red + Green |
| Blue + Red | Red + Orange (for some types) |
| Blue + Brown | |
| Color + Shape + Icon | Color alone |

Minimum 3:1 contrast between status indicator colors and between indicator and background (Agent D discovery).

Status color semantics: red (danger/error), orange (serious warning), yellow (regular warning), green (success), blue (passive notification) (Agent D discovery).

## Alternative Views

Limited adoption found across workflow builders:

- **Retool**: Graph view and Tree view (vertical layout) [1]
- **Airflow**: Grid view, Graph view, Gantt chart view [27]
- Most workflow builders offer only a single canvas view

Airflow's multiple views each serve distinct purposes [27]:
- Grid: Execution history overview (column = run, square = task)
- Graph: DAG structure and dependencies
- Gantt: Timeline for bottleneck identification ("Look for long bars" [27])

## Gaps and Limitations

- No WCAG compliance audit results published for any major workflow builder.
- Table/list alternative views for visual workflows are rare outside Airflow.
- Academic research identifies five barriers for visually impaired programmers but limited evidence of application to workflow builder design.
- Mobile accessibility for workflow builders is undocumented.
- The Olli library from MIT research [30] is available but adoption in workflow builders is unknown.
