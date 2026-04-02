# Research Brief: LangGraph Agent Orchestration Patterns

## Context

The application (the backend project) uses LangGraph to orchestrate AI agents.
Agents are nodes in a routing graph — a base agent pattern enforces a Template
Method (log → execute → log/record metrics), and automatic routing sends
invocations to specialist agents (GenericAgent, WorkflowGeneratorAgent) based
on invocation type. The system also uses LangChain for tool management and
MCP adapter integration.

## Research Questions

1. What is LangGraph's programming model — state graphs, nodes, edges,
   conditional routing, checkpointing — and how does it differ from plain
   LangChain chains?
2. What are the established patterns for multi-agent routing (supervisor,
   hierarchical, swarm) and how do they compare in reliability and latency?
3. How does LangGraph handle agent failures, retries, and human-in-the-loop
   interrupts?
4. What is the state of LangGraph's checkpointing and persistence — can it
   recover from mid-execution crashes?
5. What are the alternatives to LangGraph for agent orchestration (CrewAI,
   AutoGen, Claude Agent SDK, raw function graphs) and their trade-offs?
6. What patterns exist for combining LangGraph with external workflow engines
   like Temporal (which the application does — Temporal for durable execution,
   LangGraph for agent routing within an "agentic" activity)?

## Relationship to Existing Research

- **agent-sdk-vs-skills** (`research/agent-sdk-vs-skills/`) — covered Claude
  Agent SDK and skills but not LangGraph. Findings here could inform a
  comparison dimension.

## Why This Matters

The agent orchestrator is where the application's AI reasoning happens. Understanding
LangGraph's model, limitations, and alternatives is necessary for working on
agent routing, adding new agent types, or debugging agent behavior.
