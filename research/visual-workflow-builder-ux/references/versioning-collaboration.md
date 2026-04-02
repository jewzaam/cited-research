# Versioning and Collaboration

Covers Dimension 6: undo/redo, version history, draft/publish workflows, collaborative editing, and visual workflow diff.

See [citations.md](../citations.md) for full source details.

## Version History by Platform

| Tool | Versioning Model | Retention | Key Features |
|------|-----------------|-----------|--------------|
| Power Automate | Draft/Publish with Dataverse storage [4] | Drafts: 6 months, Published: 12 months [4] | Version grouped by day, restore as new draft [4] |
| Retool | Semantic versioning (Major/Minor/Patch) [6] | Full history preserved [6] | Auto-increment, "Live" tag, revert preserves history [6] |
| n8n | Auto-save + Publish [24] | Named versions on Pro/Enterprise (Agent D) | Production uses published version only [24] |
| Zapier | Version rollback [23] | Plan-dependent (Agent D) | "Edit from this version" creates new draft (Agent D) |
| Prefect | Automatic on every update [29] | All versions retained [29] | UI-based rollback, Git SHA tracking [29] |
| Airflow 3 | Automatic structural versioning [28] | All versions in UI [28] | Structural change detection, DAG bundles [28] |

## Draft/Publish Model

The draft/publish pattern is universal across modern workflow builders:

- **Power Automate**: "Save a draft whenever you want, even with errors" — flow state (Draft/Published) visible next to title [4]. Only available for solution-aware cloud flows [4]. Available to all regions February 7, 2025 [4].
- **Retool**: "Any changes you make to a Retool workflow are automatically saved to the current working version" — "Only the published version is used by Retool" [6].
- **n8n**: Save stores changes in draft state; publish activates for production execution [24].

## Version Restore Approaches

| Tool | Restore Mechanism |
|------|-------------------|
| Power Automate | Select previous version → Restore → becomes latest draft [4] |
| Retool | "Revert the current working version... all changes since this version are discarded but still remain in the history" [6] |
| Prefect | "Find the last known good version" → "Roll back" → applies to next scheduled run [29] |
| Airflow 3 | Versioned bundles default to original code; checkbox for "Run with latest bundle version" [28] |

## Version Comparison and Diff

Visual workflow diff is notably rare across platforms:

- **Power Automate**: "Side-by-side comparison of versions isn't available at this time" [4]
- **Airflow 3**: DAG versions visible in graph options, grid views, and code tabs, enabling historical inspection but not visual diff [28]

This is a significant industry gap — version history exists but structural comparison between versions is absent in major workflow builders.

## Airflow 3 Versioning

Airflow 3 introduced automatic structural versioning [28]:

- New version created when "a DAG run is created for a DAG that has undergone a structural change since the last run" [28]
- Structural changes: modifications to parameters, dependencies, task IDs, adding/removing tasks [28]
- **Runtime protection**: "The DAG run finishes using the bundle version it started with" [28]
- **DAG Bundles**: LocalDagBundle (unversioned) vs GitDagBundle (versioned per commit) [28]

## Prefect Versioning Best Practices

- "Use Git SHAs and image digests for guaranteed consistency" rather than branch names or tags [29]
- Pin specific Docker image digests in job_variables [29]
- pull_steps and job_variables define what code Prefect executes — critical for reliable rollbacks [29]
- Automatic Git metadata collection from CI environments [29]

## Collaborative Editing

### OT vs CRDT

| Aspect | OT | CRDT |
|--------|----|----|
| Architecture | Requires server coordination [19] | Peer-to-peer, no mandatory server [19] |
| Intent capture | "Sophisticated transformations understanding semantic meaning" [19] | "Sacrifices intent awareness" at granular data levels [19] |
| Offline support | Limited (needs connectivity) [19] | Native support [19][20] |
| Industry adoption | Google, Microsoft, CKSource [19] | Yjs, Automerge (growing) [20] |

"Every single one" CRDT-based rich editor involves "compromises in depth of features" [19].

### Yjs CRDT

Yjs is "a high-performance CRDT for building collaborative applications that sync automatically" [20]:
- Shared types: Y.Map, Y.Array, Y.Text [20]
- "Doesn't make any assumptions about the network technology you are using" [20]
- Claims to be "the fastest CRDT implementation by far" [20]
- Supports "Local-First software" models [20]

### Figma's Approach

Figma uses a custom server-authoritative, per-property last-writer-wins approach rather than OT or pure CRDT [35]. Figma rejected OT as "unnecessarily complex" for their use case [35]. This is notable because it demonstrates that established collaboration approaches (OT/CRDT) are not the only viable patterns.

**Note:** Figma blog content could not be fully extracted (JavaScript-rendered page). Claims sourced from Agent D search snippets.

## Undo/Redo Patterns

The command pattern is the standard approach for undo/redo in canvas editors (Agent D discovery):

- Dual stacks: undo stack for history, redo stack for undone operations
- New action after undo clears redo stack
- Alternative Memento pattern stores full state snapshots but consumes more memory

No workflow builder documentation specifies undo/redo history limits or memory management strategies.

## Gaps and Limitations

- Visual workflow diff is absent from all major platforms studied.
- No workflow builder currently supports real-time collaborative editing (unlike design tools like Figma).
- Undo/redo implementation details are undocumented across platforms.
- Version history cannot be filtered or annotated (notes/titles) in Power Automate [4].
- Only last published version exports in Power Automate solutions — no draft/history export [4].
