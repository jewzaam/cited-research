# Research Brief: Visual Workflow Builder UX Patterns

## Context

The frontend project (the frontend project) has a visual workflow builder
where users create automation workflows by connecting nodes on a canvas.
The builder supports multiple node types (triggers, conditions, loops,
actions, AI agents, approvals), button edges for inline node insertion,
automatic Dagre-based layout, and a node registry system for extensibility.
This is the primary user-facing feature of the application.

## Research Questions

1. What UX patterns do production workflow builders use — node palettes,
   drag-and-drop vs click-to-add, inline editing vs side panels, zoom/pan
   behavior, minimap navigation?
2. How do workflow builders handle complexity — grouping/collapsing,
   sub-workflows, conditional branching visualization, parallel execution
   paths?
3. What are the usability findings from research on visual programming
   environments — cognitive load, learnability curves, error prevention?
4. How do leading workflow builders (n8n, Retool Workflows, Zapier,
   Power Automate, Prefect, Airflow) approach onboarding and progressive
   disclosure for non-technical users?
5. What patterns exist for workflow validation UX — showing errors inline
   on the canvas, pre-execution validation, type checking between node
   connections?
6. How do workflow builders handle undo/redo, version history, and
   collaborative editing?
7. What accessibility approaches exist for visual canvas-based editors —
   keyboard navigation, screen reader support, alternative views?

## Relationship to Existing Research

- **n8n** (`research/n8n/`) — covers n8n as a platform. This topic
  focuses on the UX design patterns across the workflow builder landscape.
- **Research-react-flow-workflow-editors.md** — covers the implementation
  technology. This topic covers the UX/design layer above it.

## Why This Matters

The workflow builder is the product's core differentiator. Understanding
what UX patterns work (and don't) across the industry informs design
decisions for new node types, canvas interactions, and the overall editing
experience. This is especially relevant as the builder grows more complex
with AI agent nodes and approval flows.
