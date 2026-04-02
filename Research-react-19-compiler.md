# Research Brief: React 19 and React Compiler

## Context

The frontend project (the frontend project) uses React 19 with the React
Compiler (babel-plugin-react-compiler) enabled. This means manual
useMemo/useCallback are not needed — the compiler handles memoization
automatically. The project also uses React.lazy() for route-level code
splitting.

## Research Questions

1. What are React 19's significant changes — new hooks (use, useActionState,
   useOptimistic), Actions, Server Components readiness, ref as prop,
   document metadata, stylesheet support?
2. What is the React Compiler — how does it analyze component code, what
   memoization decisions does it make, and what are its known limitations?
3. What code patterns break or degrade React Compiler optimization — and
   how should codebases be structured to maximize compiler benefit?
4. How does React 19 + Compiler interact with state management libraries
   (Zustand, TanStack Query) — are there known compatibility issues?
5. What is the migration experience from React 18 to 19 — common breakages,
   deprecated patterns, ecosystem library compatibility?
6. How does React 19 compare to the current state of alternatives (Solid,
   Svelte 5, Vue 3.5) on performance, DX, and ecosystem maturity?

## Relationship to Existing Research

No overlap with existing research topics.

## Why This Matters

React 19 and the Compiler change how components should be written. The
Compiler eliminates manual memoization but requires understanding what
patterns it can and cannot optimize. This affects how new components should
be structured and how performance issues should be debugged.
