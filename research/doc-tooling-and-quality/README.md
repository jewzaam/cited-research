# Documentation Tooling and Quality Assessment

Research into tools, frameworks, and practices for authoring, reviewing, and evaluating open source project documentation — focused on a solo developer maintaining multiple Markdown-based projects.

## TL;DR

The $0 stack that covers authoring, quality enforcement, and deployment:

| Layer | Tool | Role |
|-------|------|------|
| Site generator | **MkDocs Material** | YAML config, built-in search, 50,000+ users |
| Prose linting | **Vale** | Offline style enforcement, reusable across repos |
| Structure linting | **markdownlint** | 60+ rules, 32 autofix |
| Link checking | **lychee** | Rust async, single binary |
| Quality framework | **Diátaxis** | 4-type doc classification and audit process |
| Style guide | **Google Dev Docs** | Free, CC-licensed, Vale package available |
| CI/CD | **GitHub Actions** | Official workflows for all tools above |

## Quick Decision Framework

1. **Now** (30 min): Install Vale + markdownlint, run on existing docs
2. **Week 1**: Apply Diátaxis audit — classify pages, separate mixed types
3. **Week 2**: Set up MkDocs Material for one project, deploy to GitHub Pages
4. **Week 3**: Add CI pipeline, copy config to other projects
5. **Ongoing**: 12-item quality checklist + LLM structural review

## Key Findings

- **MkDocs Material** beats Docusaurus for solo developers — YAML config vs React/JS expertise, and Docusaurus has reported build performance issues at scale (26-min builds, 10GB+ RAM)
- **Vale + markdownlint** is the recommended linting combination — Vale handles prose quality, markdownlint handles structure, neither alone is sufficient
- **Diátaxis** is the most practical quality framework — clear audit process, no tooling dependency, proven in case studies
- **Commercial AI doc platforms** aren't worth the cost for solo developers — Mintlify's free tier is the exception if you want hosted docs
- **Vale's style reusability** is the key multi-repo enabler — define standards once, enforce everywhere
- **Agents as primary authors** changes the tooling role — Vale and markdownlint become CI gates agent output must pass, Diátaxis becomes a prompt constraint, and writer/reviewer separation is critical (3-27% hallucination rates in AI-generated docs)

## Files

- [doc-tooling-and-quality.md](doc-tooling-and-quality.md) — Full analysis with methodology
- [citations.md](citations.md) — All 45 sources, numbered
- [references/site-generators.md](references/site-generators.md) — Generator comparison matrix
- [references/linting-and-review.md](references/linting-and-review.md) — Linting tool analysis
- [references/quality-frameworks.md](references/quality-frameworks.md) — Framework comparison
- [references/ai-assisted-tools.md](references/ai-assisted-tools.md) — AI tool assessment
- [references/ci-integration.md](references/ci-integration.md) — CI pipeline patterns
- [references/agentic-doc-lifecycle.md](references/agentic-doc-lifecycle.md) — Agent-as-author workflow
- [audit/citation-audit.md](audit/citation-audit.md) — Independent source verification
- [audit/consistency-review.md](audit/consistency-review.md) — Cross-file consistency check
