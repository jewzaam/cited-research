# Research Brief: Multi-Provider LLM Routing via Gateway APIs

## Context

The application (the backend project) uses OpenRouter as a unified LLM gateway,
supporting Claude (default: 3.5-sonnet), GPT-4, Gemini Pro, and Llama 3.1
70B. The agent orchestrator routes to different models based on invocation
type. This means the application depends on a third-party routing layer for all LLM
access.

## Research Questions

1. What is OpenRouter — architecture, pricing model (markup over provider
   pricing), reliability track record, rate limits?
2. How does OpenRouter compare to alternatives — LiteLLM (open-source proxy),
   Portkey, Martian, direct provider APIs with a thin adapter?
3. What are the trade-offs of using a unified gateway vs direct provider
   integration — latency overhead, failure modes, vendor lock-in, cost
   transparency?
4. What patterns exist for LLM routing decisions — model selection by task
   type, cost-based routing, latency-based routing, fallback chains?
5. How do teams handle provider outages and failover in multi-model
   architectures?
6. What are the security implications of routing all LLM traffic through a
   third-party gateway — data handling, API key management, compliance?
7. What is the state of the open-source LLM gateway ecosystem (LiteLLM,
   vLLM router, TGI) for self-hosted routing?

## Relationship to Existing Research

No overlap with existing research topics.

## Why This Matters

All of the application's AI capability flows through the LLM gateway. Understanding
the routing layer's reliability, cost, and alternatives informs whether
OpenRouter is the right choice or whether self-hosted routing would be
more appropriate for production use.
