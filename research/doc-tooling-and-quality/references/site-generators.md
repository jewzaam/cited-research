# Documentation Site Generators

Comparison of site generators for small-to-medium open source projects maintained by a solo developer. Sources: [citations.md](../citations.md).

## Comparison Matrix

| Generator | Language | Markdown | Search | Versioning | GitHub Pages | Setup Complexity | Solo Viability |
|-----------|----------|----------|--------|------------|--------------|------------------|----------------|
| MkDocs Material | Python | Native (Python-Markdown) | Built-in, offline [1] | Via mike plugin [10] | Official workflow [8] | Low — `pip install`, YAML config [1] | High |
| Docusaurus | Node.js/React | MDX (Markdown + JSX) [3] | Algolia integration [3] | Native [3] | Via GitHub Actions [3] | Medium — React/Node.js knowledge helps [2] | Medium |
| Starlight | Astro | Markdown/Markdoc/MDX [4] | Built-in (Pagefind) [4] | Not built-in | Via Astro action [4] | Low-Medium — TypeScript config [4] | High |
| VitePress | Vue/Vite | Markdown + Vue components [5] | Built-in full-text [5] | Not built-in | Via GitHub Actions [5] | Low-Medium — Vue knowledge helps [5] | High |
| mdBook | Rust | Native [6] | Built-in [6] | Not built-in | Via GitHub Actions [6] | Low — `cargo install` [6] | High (simple) |
| Sphinx | Python | Via MyST-Parser [2] | Built-in or Algolia [2] | Via Read the Docs | Via GitHub Actions [2] | High — extension configuration [2] | Medium |
| GitBook | Cloud SaaS | Limited [2] | AI semantic [7] | Built-in | N/A (hosted) | Very Low (but locked in) | Low (cost) |
| Jekyll | Ruby | Native | Via plugins | Not built-in | Native integration [2] | Low | Medium (dated) |

## Detailed Analysis

### MkDocs Material — Recommended for Solo Developers

Trusted by 50,000+ individuals and organizations [1]. Python-based with YAML configuration — no JavaScript framework knowledge needed. Built-in search runs entirely in browser and works offline [1]. Plugin ecosystem covers blogging, versioning (via mike [10]), social cards, and performance optimization [1]. Supports 60+ languages [1]. MIT-licensed [1].

Key advantage: style separation enables reusability across projects — the same theme configuration works across multiple repos with minimal adaptation.

MkDocs Material's own comparison page notes that Docusaurus requires "steep learning curve requiring JavaScript expertise" and has "high maintenance due to ecosystem volatility" [2]. Sphinx has "high complexity with reStructuredText" [2]. GitBook is "closed-source, paid for proprietary use" with "many projects migrated away" [2].

### Docusaurus

Meta-maintained, React-based [3]. Native versioning is a differentiator — copies `docs/` to `versioned_docs/` directories automatically [3]. MDX enables embedding React components in documentation. Algolia DocSearch integration is built-in [3]. Users include Redux, Supabase, Testing Library [3].

Concerns for solo developers: build performance degrades at scale — reports of 26-minute builds and 10GB+ RAM usage on larger sites [9]. The 250-dependency package size adds maintenance overhead [9]. React/MDX knowledge required for customization makes the learning curve steeper than Markdown-only tools [2].

### Starlight (Astro)

Newer entrant with strong fundamentals. Built-in Pagefind search works without external services [4]. Framework-agnostic — supports React, Vue, Svelte, Solid components [4]. Accessibility-focused by design [4]. Frontmatter validation with TypeScript type-safety prevents configuration errors [4].

Good fit for solo developers who want modern tooling without framework lock-in. Less mature ecosystem than MkDocs or Docusaurus.

### VitePress

Vue-powered with Vite for fast builds [5]. Static HTML on initial load, SPA for subsequent navigation [5]. Best fit for Vue ecosystem projects. v2.0.0-alpha.17 indicates still maturing [5].

### mdBook

Simplest option. Rust-based, single binary [6]. Best for book-format documentation (tutorials, courses). Used by The Rust Programming Language book [6]. Limited plugin ecosystem compared to MkDocs or Docusaurus. No versioning, no blogging, no i18n.

### Sphinx

The legacy standard for Python projects. Auto-generates API docs from Python docstrings (autodoc) — no other generator matches this capability [2]. MyST-Parser enables Markdown authoring [2]. Read the Docs offers free hosting with build limits. Overkill for non-Python projects.

### GitBook

Cloud-only, no self-hosting [7]. Per-site pricing starts at $65/month for a custom domain [7]. Free tier limited to 1 user and gitbook.io subdomain [7]. Many open source projects have migrated away [2]. Not viable for budget-conscious solo developers maintaining multiple projects.

## Gaps and Limitations

- No systematic benchmarks comparing build times across generators on standardized hardware/content
- Setup time claims ("minutes") are from marketing materials, not controlled measurements
- Single-maintainer viability is inferred from complexity analysis, not longitudinal studies
- Hugo (Go-based, very fast builds) omitted from detailed analysis — its templating complexity and lack of default theme make it less suited for documentation despite raw speed
