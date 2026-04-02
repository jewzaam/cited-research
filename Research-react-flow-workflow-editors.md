# Research Brief: React Flow and Graph Layout for Workflow Editors

## Context

The frontend project (the frontend project) uses @xyflow/react (React Flow)
as its visual workflow canvas, with @dagrejs/dagre for automatic node
layout. The builder is the most complex module in the application — it
supports custom node types (triggers, conditions, loops, actions, AI
agents, approvals), custom edge types (including button edges for adding
nodes), and a bidirectional transformation between flat graph (UI) and
nested tree (backend API) representations.

## Research Questions

1. What is React Flow's architecture — nodes, edges, handles, custom types,
   viewport management, selection, drag-and-drop — and what is the current
   API surface?
2. How does Dagre's hierarchical layout algorithm work, and what are the
   alternatives (ELK, d3-hierarchy, custom force-directed) for workflow
   graph layout?
3. What are established patterns for building workflow/pipeline editors with
   React Flow — node registries, edge validation, undo/redo, copy/paste?
4. How do production workflow editors handle the flat-graph vs nested-tree
   transformation problem (the representation mismatch between visual
   editors and execution engines)?
5. What are the performance characteristics and limits of React Flow — max
   node/edge count, rendering strategies for large workflows, virtualization?
6. How do other visual workflow builders (n8n, Node-RED, Retool Workflows,
   Prefect UI) approach the same UX problems, and what patterns emerge?
7. What accessibility challenges exist for node-based visual editors, and
   what solutions have been implemented?

## Relationship to Existing Research

- **n8n** (`research/n8n/`) — covers n8n as a platform but not its visual
  editor implementation patterns. Findings here on workflow editor UX could
  cross-reference.

## Why This Matters

The workflow builder is the core user experience of frontend. Understanding
React Flow's capabilities, layout algorithm trade-offs, and production
patterns for workflow editors is necessary for extending the builder,
adding new node types, or improving the editing experience.
