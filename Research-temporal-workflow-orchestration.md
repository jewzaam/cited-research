# Research Brief: Temporal Workflow Orchestration Patterns

## Context

The application (the backend project) uses Temporal as its workflow execution
engine with YAML-driven workflow definitions, activity types (API, Script,
Agentic, Approval, AAP Job Template), and a background sync service that
keeps Temporal's internal state mirrored to PostgreSQL for audit/query.

## Research Questions

1. What are Temporal's core programming model concepts (workflows, activities,
   signals, queries, child workflows) and how do they map to common automation
   patterns?
2. What are proven patterns for YAML/JSON-driven workflow definitions on top
   of Temporal (vs. code-first workflows)?
3. How does Temporal handle failure, retry, and compensation — and what are
   the gotchas teams hit in production?
4. What is the operational cost of running Temporal (cluster sizing, database
   backend choices, monitoring)?
5. How does Temporal compare to alternatives (Celery, Airflow, Prefect,
   Windmill, n8n) specifically for multi-agent AI orchestration use cases?
6. What patterns exist for syncing Temporal execution state to an external
   database (the "activity sync" pattern application uses)?

## Relationship to Existing Research

- **n8n** (`research/n8n/`) — compared Temporal briefly from n8n's perspective.
  This topic goes deep on Temporal itself. Consider updating n8n's comparison
  table with findings from this research.

## Why This Matters

Temporal is the execution backbone of application. Understanding its model, failure
semantics, and operational characteristics is prerequisite to working on
workflows, activities, or the sync service.
