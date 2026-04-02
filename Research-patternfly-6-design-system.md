# Research Brief: PatternFly 6 Enterprise Design System

## Context

The frontend project (the frontend project) uses PatternFly 6 as its UI
component library. PatternFly is Red Hat's open-source design system. The
project uses PatternFly React components, PatternFly icons (preferring
RhUi-prefixed variants), and PatternFly design tokens for custom CSS.

## Research Questions

1. What is PatternFly 6 — architecture, component catalog, design token
   system — and what changed from PatternFly 5?
2. How does PatternFly compare to alternatives for enterprise React
   applications (MUI, Ant Design, Chakra UI, Radix + Tailwind)?
3. What are PatternFly's accessibility guarantees — WCAG compliance level,
   built-in ARIA patterns, keyboard navigation?
4. How do teams customize PatternFly — design token overrides, component
   composition patterns, dark mode support?
5. What are the known limitations and pain points (bundle size, styling
   conflicts, component gaps, upgrade friction between major versions)?
6. How does PatternFly integrate with modern React patterns (React 19,
   Server Components, React Compiler)?
7. What is the PatternFly community and maintenance model — release
   cadence, contribution process, roadmap visibility?

## Relationship to Existing Research

No overlap with existing research topics. The dark-theme-calendar-ui
research (`research/dark-theme-calendar-ui/`) covers color design but for
tkinter, not PatternFly.

## Why This Matters

Every UI component in frontend is built on PatternFly. Understanding its
design token system, component patterns, and limitations is necessary for
building new features, debugging styling issues, or evaluating whether
PatternFly constraints shape architectural decisions.
