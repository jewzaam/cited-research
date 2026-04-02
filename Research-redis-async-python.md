# Research Brief: Redis Caching Patterns for Async Python

## Context

The application (the backend project) uses Redis for caching and temporary
data storage (e.g., activity streaming results). The application is fully
async (FastAPI + asyncpg + async SQLAlchemy). Redis sits alongside
PostgreSQL — PostgreSQL for persistent state, Redis for ephemeral/cached
data. The project chose Redis partly to align with AAP (Ansible Automation
Platform) licensing.

## Research Questions

1. What are the current best practices for Redis in async Python — redis-py
   async, aioredis (merged into redis-py), connection pooling, pipeline
   batching?
2. What caching patterns apply (cache-aside, write-through, write-behind)
   and how do they map to FastAPI dependency injection?
3. How do teams handle cache invalidation in async systems — TTL strategies,
   event-driven invalidation, pub/sub for cache busting across instances?
4. What are the patterns for using Redis as a temporary result store for
   streaming/polling use cases (the pattern application uses for activity results)?
5. How does Redis Streams compare to pub/sub for real-time event delivery
   in Python async applications?
6. What are the operational considerations — memory limits, eviction
   policies, persistence (RDB vs AOF), and monitoring for a cache-only
   Redis deployment?
7. What are the alternatives to Redis for async Python caching (Valkey,
   memcached, in-process caches like cachetools) and their trade-offs?

## Relationship to Existing Research

No overlap with existing research topics.

## Why This Matters

Redis handles ephemeral state and caching in application. Understanding async
connection management, caching patterns, and the temporary-result-store
pattern is necessary for working on performance, streaming features, or
scaling the application.
