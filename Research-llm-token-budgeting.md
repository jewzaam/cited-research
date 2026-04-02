# Research Brief: LLM Token Budgeting and Context Management

## Context

The application (the backend project) has a context manager component that
controls token usage across agent invocations. The system routes prompts
to specialist agents via LangGraph and needs to manage context window
limits, token costs, and conversation history across multi-turn agent
interactions. It supports multiple LLM providers via OpenRouter.

## Research Questions

1. What are the established patterns for token budgeting in multi-agent
   systems — per-agent limits, shared budgets, priority-based allocation?
2. How do teams manage context windows in production — truncation
   strategies, summarization, retrieval-augmented approaches, sliding
   windows?
3. What is the state of token counting libraries and APIs — tiktoken,
   provider-specific tokenizers, estimation vs exact counting trade-offs?
4. How do teams track and control LLM costs in production — per-request
   cost attribution, budget alerts, rate limiting by cost rather than
   requests?
5. What patterns exist for conversation memory management in LangChain/
   LangGraph — buffer memory, summary memory, vector-backed memory, and
   their accuracy/cost trade-offs?
6. How do teams handle context overflow gracefully — what happens when an
   agent's context fills up mid-task, and what recovery patterns exist?

## Relationship to Existing Research

No overlap with existing research topics. The engineering-estimate research
touches on AI productivity but not operational token management.

## Why This Matters

Token management directly affects the application's cost, reliability, and response
quality. Overfilling context windows causes failures; underfilling wastes
model capability. Understanding budgeting patterns is necessary for the
context manager and for scaling to more agents and longer conversations.
