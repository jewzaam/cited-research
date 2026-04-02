# Research Brief: Multi-Agent System Observability

## Context

The application (the backend project) has a split observability model:
Prometheus-compatible metrics (in-memory 24-hour store, per-component) and
anonymous telemetry to Segment.com (fire-and-forget, no PII). It uses
structlog for structured JSON logging. The system orchestrates multiple
AI agents via LangGraph within Temporal workflows, creating complex
execution traces that span multiple services.

## Research Questions

1. What are the specific observability challenges for multi-agent AI systems
   — distributed traces across agent hops, token usage attribution, tool
   call latency, LLM response quality metrics?
2. What does OpenTelemetry offer for LLM/agent observability — are there
   semantic conventions for GenAI operations, and what is their maturity?
3. How do teams trace execution through LangChain/LangGraph — LangSmith,
   Langfuse, custom OpenTelemetry instrumentation?
4. What patterns exist for correlating Temporal workflow traces with
   LangGraph agent traces (cross-system trace propagation)?
5. How do teams monitor LLM costs, token budgets, and rate limits in
   production multi-agent systems?
6. What alerting patterns are effective for agent systems (latency
   degradation, hallucination rate, tool failure rate, cost anomalies)?

## Relationship to Existing Research

- **otel** (`research/otel/`) — covers Python logging + OpenTelemetry on
  OpenShift. This topic extends into agent-specific observability concerns.
  Consider updating the otel research with agent-relevant findings, or
  cross-linking.

## Why This Matters

The application orchestrates AI agents in production workflows. Without proper
observability, debugging agent misbehavior, tracking costs, and identifying
performance bottlenecks becomes guesswork. This is especially critical as
the system scales to more agent types and concurrent workflows.
