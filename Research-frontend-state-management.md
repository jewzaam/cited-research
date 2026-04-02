# Research Brief: Frontend State Management Patterns (TanStack Query + Zustand)

## Context

The frontend project (the frontend project) uses a deliberate multi-layer
state management strategy:

- **TanStack Query 5** for server state (API data, caching, background sync)
- **Zustand 5** for client state (workflow builder editing state)
- **React useState/useContext** for local component state
- **Zustand (without React)** for WebSocket connection management

Key patterns include custom Zustand selectors to prevent broad re-renders,
batch operations for atomic state updates, and separation of mutable
editing state from immutable cached API data.

## Research Questions

1. What are the current best practices for separating server state (API
   cache) from client state (UI editing) in React applications?
2. How does TanStack Query 5 handle optimistic updates, cache invalidation,
   and background refetching — and what are the patterns for complex
   dependent queries?
3. What are Zustand 5's patterns for derived state, middleware (immer,
   devtools, persist), and subscription optimization via selectors?
4. How do teams combine TanStack Query and Zustand — what goes where, and
   what are the anti-patterns (duplicating server state in Zustand, using
   Query for client state)?
5. How does this combination compare to alternatives — Redux Toolkit +
   RTK Query, Jotai, Recoil, or going all-in on TanStack Query?
6. What patterns exist for managing real-time/WebSocket state alongside
   REST API cache state in React applications?
7. How do these libraries interact with React 19 and the React Compiler?

## Relationship to Existing Research

No overlap with existing research topics.

## Why This Matters

State management is the foundation of UI correctness and performance. The
multi-layer approach frontend uses is deliberate and nuanced. Understanding
why each layer exists and when to use which prevents state management
mistakes that cause bugs, stale data, or performance problems.
