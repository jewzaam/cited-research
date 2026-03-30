# Citations

All sources visited in-session via WebSearch or WebFetch on 2026-03-30.

## Site Generators

[1] MkDocs Material — Official Documentation. squidfunk.github.io/mkdocs-material/. Tier 2.
Data extracted: 50,000+ users/organizations, built-in offline search, 10,000+ icons, 60+ language support, MIT license, YAML configuration, PyPI installation.

[2] MkDocs Material — Alternatives Comparison. squidfunk.github.io/mkdocs-material/alternatives/. Tier 2.
Data extracted: Comparative analysis vs Docusaurus, Jekyll, Sphinx, GitBook. Docusaurus requires JavaScript expertise and has "high maintenance due to ecosystem volatility." Jekyll has "limited Markdown capabilities." Sphinx has "high complexity with reStructuredText."

[3] Docusaurus — Official Site. docusaurus.io/. Tier 2.
Data extracted: Meta maintains it. React + MDX. Native versioning, Algolia search, i18n. v3.9.2. Users: Redux, Supabase, Testing Library, IOTA, Temporal. Deploys to Netlify and GitHub Pages.

[4] Starlight — Official Documentation. starlight.astro.build/. Tier 2.
Data extracted: Built on Astro. Markdown/Markdoc/MDX with frontmatter validation. Built-in search (Pagefind), i18n, dark mode. Framework-agnostic components (React, Vue, Svelte, Solid). Accessibility-focused.

[5] VitePress — Official Site. vitepress.dev/. Tier 2.
Data extracted: Vue + Vite powered. Instant server startup, HMR. Static HTML initial load, SPA navigation. Full-text search. v2.0.0-alpha.17 (current), v1.6.4 (stable).

[6] mdBook — Official Documentation. rust-lang.github.io/mdBook/. Tier 2.
Data extracted: Rust-based. Integrated search, syntax highlighting, customizable themes, preprocessor support. Used by The Rust Programming Language book.

[7] GitBook — Pricing Page. gitbook.com/pricing. Tier 2.
Data extracted: Free (1 user/site, GitHub/GitLab sync), Premium ($65/site/month + $12/user/month), Ultimate ($249/site/month + $12/user/month + AI Assistant), Enterprise (custom). Translation: $25 for first 50K words.

[8] MkDocs Material — Publishing Your Site. squidfunk.github.io/mkdocs-material/publishing-your-site/. Tier 2.
Data extracted: Official GitHub Actions workflow, gh-deploy command, Python setup. (From discovery agent — not directly fetched but referenced by agent.)

[9] Docusaurus — GitHub Discussions #3132. github.com/facebook/docusaurus/discussions/3132. Tier 4.
Data extracted: Build time concerns — 26-minute builds, 10GB+ RAM usage reported. (From discovery agent.)

[10] Mike — MkDocs Versioning Tool. github.com/jimporter/mike. Tier 2.
Data extracted: Git-based version management for MkDocs. (From discovery agent.)

## Linting and Review Tools

[11] Vale — Official Site. vale.sh/. Tier 2.
Data extracted: Open-source CLI editorial style enforcer. Runs offline. macOS/Windows/Linux. 3M+ downloads, 1.5M+ Docker pulls, 4,500+ GitHub stars, 40+ contributors. Integrates with VS Code, Chrome, GitHub Actions.

[12] Vale — Styles Documentation. vale.sh/docs/styles. Tier 2.
Data extracted: YAML-based rules. 11 check types: existence, substitution, occurrence, repetition, consistency, conditional, capitalization, metric, spelling, sequence, script. Rules require `extends` and `message` fields. Severity levels: suggestion/warning/error.

[13] Earthly Blog — Linting Markdown and Documentation. earthly.dev/blog/markdown-lint/. Tier 3.
Data extracted: markdownlint "can't be beaten for dealing with markdown structure." Vale "fast and configurable but not necessarily easy to get started with." textlint "harder to set up and configure: you have to install each plug-in separately." Recommended: markdownlint + Vale for comprehensive coverage. Vale's style separation enables reusability across projects.

[14] markdownlint — GitHub Repository. github.com/DavidAnson/markdownlint. Tier 2.
Data extracted: 60+ built-in rules, 32 support autofix. Custom rules via JavaScript API. Node.js implementation. (From discovery agent.)

[15] markdownlint-cli2 — GitHub Repository. github.com/DavidAnson/markdownlint-cli2. Tier 2.
Data extracted: Performance-optimized CLI for large repositories. .gitignore mode for faster processing. (From discovery agent.)

[16] textlint — Official Site. textlint.org/. Tier 2.
Data extracted: Pluggable JavaScript/Node.js linter. No built-in rules — each plugin installed separately. Node.js >= 20 required. Configuration via .textlintrc.json. (From discovery agent.)

[17] alex — Official Site. alexjs.com/. Tier 2.
Data extracted: Inclusive language linter. Detects gender, race, religion, ableist, condescending language. Sources: retext-equality, retext-profanities. Configuration: .alexrc.js, .alexignore. (From discovery agent.)

[18] lychee — Official Documentation. lychee.cli.rs/. Tier 2.
Data extracted: Rust-based async link checker. "Designed for speed, making it perfect for large projects." Markdown and HTML support. Single static binary. JSON output for CI.

[19] lychee — GitHub Action. github.com/lycheeverse/lychee-action. Tier 2.
Data extracted: CI integration for link checking. Configuration parameters for args, format, output, fail. (From discovery agent.)

[20] Vale GitHub Action. github.com/vale-cli/vale-action. Tier 2.
Data extracted: Reporter options: github-pr-check, github-pr-review, github-check. Requires Vale >= 2.16.0. (From discovery agent.)

[21] proselint — PyPI. pypi.org/project/proselint/. Tier 2.
Data extracted: Python-based prose linter. Python >= 3.8.1. Aggregates writing advice from Bryan Garner, David Foster Wallace, etc. (From discovery agent.)

[22] write-good — npm. npmjs.com/package/write-good. Tier 2.
Data extracted: Node.js prose linter. Detects passive voice, lexical illusions, "so" at sentence start, weakening adverbs. (From discovery agent.)

## Quality Frameworks

[23] Divio Documentation System (Diátaxis). docs.divio.com/documentation-system/. Tier 3.
Data extracted: Four types: tutorials, how-to guides, technical reference, explanation. Two axes: theory/practice and studying/working. Creator: Daniele Procida. "There isn't one thing called documentation, there are four."

[24] Tom Johnson — What is the Diátaxis Documentation Framework. idratherbewriting.com/blog/what-is-diataxis-documentation-framework. Tier 3.
Data extracted: Comparison with DITA, Information Mapping, Good Docs Project. "Not four rigid buckets." Framework offers simplicity for solo developers. Johnson created "a reliable one-stop shop for reference on key concepts."

[25] Sequin Blog — We Fixed Our Documentation with the Diátaxis Framework. blog.sequinstream.com/we-fixed-our-documentation-with-the-diataxis-framework/. Tier 4.
Data extracted: Before/after case study. Rebuilt quickstart to ~3 minutes. "If a guide felt too complex, we'd revisit the feature design." Used "phantom links" as doc map. "Engineers instinctively over-explain."

[26] The Good Docs Project — Official Site. thegooddocsproject.dev/. Tier 3.
Data extracted: Open source templates in "packs." v1.5.0 ("Helix"). 75+ technical writers maintain it. Three-step process: pick templates, share, write.

[27] Tom Johnson — API Documentation Quality Checklist. idratherbewriting.com/learnapidoc/docapis_quality_checklist.html. Tier 3.
Data extracted: ~75 criteria in 6 categories: Findability (11), Accuracy (9), Relevance (7), Clarity (24), Completeness (8), Readability (16). Shortened version: 12 core items. "It might take more than a year working with the docs" to fully assess.

[28] Nielsen Norman Group — 10 Usability Heuristics. nngroup.com/articles/ten-usability-heuristics/. Tier 2.
Data extracted: Heuristic #10: documentation must be "easy to search," presented "in context right at the moment that the user requires it," and "list concrete steps to be carried out." Author: Jakob Nielsen.

[29] Google Developer Documentation Style Guide. developers.google.com/style. Tier 2.
Data extracted: Editorial guidelines for technical docs. Reference hierarchy (project-specific > this guide > third-party). "Break any of these rules sooner than say anything outright barbarous." Creative Commons Attribution 4.0 license.

[30] Write the Docs — Documentation Principles. writethedocs.org/guide/writing/docs-principles/. Tier 3.
Data extracted: Community-driven best practices. Structure for scannability, begin documenting before development, include everyone, accept repetition, focus on likely questions, include examples. (From discovery agent — site blocked by Cloudflare during direct fetch.)

[31] Nielsen Norman Group — Information Scent. nngroup.com/articles/information-scent/. Tier 2.
Data extracted: Users follow "scent" cues to estimate information value. Strong scent suggests user is moving toward goal. Forms: pictures, link descriptions, related content. (From discovery agent.)

[32] Every Page is Page One — Mark Baker. everypageispageone.com/. Tier 3.
Data extracted: Bottom-up information architecture. Every page is potential entry point. Topic-based writing for non-linear navigation. Each topic must be self-sufficient but interconnected. (From discovery agent.)

## AI-Assisted Tools

[33] Mintlify — Official Site. mintlify.com/. Tier 2.
Data extracted: "Intelligent Knowledge Platform." LLMs.txt & MCP support. Context-aware Agent. Customers: Anthropic (2M+ devs), Coinbase, HubSpot, Perplexity, Notion, PayPal. SOC 2 compliant.

[34] Mintlify — Pricing. mintlify.com/pricing. Tier 2.
Data extracted: Hobby (free): full platform, custom domain, LLM optimizations. Pro ($250/month): AI Assistant (250 messages included, $0.25/overage), preview deployments. Extra seats: $20/seat/month. Enterprise: contact sales, 99.99% SLA.

[35] ReadMe — AI Features. readme.com/ai. Tier 2.
Data extracted: AI Linter (10-point scoring), Agent Owlbert (writing assistant), Ask AI (natural language API querying), MCP Server (one-click, compatible with Claude/OpenAI/Gemini/Copilot/Grok/DeepSeek), Docs Audit (voice/terminology/structure).

[36] GitBook — Features/AI. gitbook.com/features/ai. Tier 2.
Data extracted: GitBook Agent (proactive suggestions from Intercom/GitHub), GitBook Assistant (MCP-powered Q&A), llms.txt support. Uses GPT-4o, does not use content for model training. (From discovery agent.)

[37] Swimm — Code-Coupled Documentation. swimm.io/. Tier 2.
Data extracted: Code-coupled documentation with Smart Tokens that auto-update when code changes. Continuous Documentation paradigm. IDE plugins for VS Code and JetBrains. Markdown stored in git. (From discovery agent — page content not extractable via WebFetch.)

[38] Grammarly — Technical Writing Guide. grammarly.com/blog/business-writing/how-to-use-grammarly-like-a-technical-writing-pro/. Tier 2.
Data extracted: Audience selection (knowledgeable/expert), domain selection (engineering, CS, medicine). Limitations: "Incorrect suggestions for discipline-specific or overly technical work." Synonym swapping inappropriate for technical docs. (From discovery agent.)

[39] Grammarly — Business Pricing. grammarly.com/business/pricing. Tier 2.
Data extracted: Pro for Teams (2-149 users), Enterprise (150+), $12-25/user/month. (From discovery agent.)

## CI Integration

[40] GitHub Pages — Custom Workflows. docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages. Tier 2.
Data extracted: Actions sequence: configure-pages, upload-pages-artifact, deploy-pages. Permissions: pages: write, id-token: write. (From discovery agent.)

[41] peaceiris/actions-gh-pages — GitHub Action. github.com/peaceiris/actions-gh-pages. Tier 2.
Data extracted: Popular third-party deployment action for multiple generators. (From discovery agent.)

[42] GitHub Reusable Workflows Documentation. docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows. Tier 2.
Data extracted: workflow_call syntax, inputs/secrets passing, nesting limits (10 levels, 50 unique workflows). (From discovery agent.)

[43] GitHub Starter Workflows Repository. github.com/actions/starter-workflows. Tier 2.
Data extracted: Template structure, .properties.json metadata, categories (ci, deployments, automation, pages). (From discovery agent.)

[44] lychee — GitHub Action Recipes (Repository Checks). lychee.cli.rs/github_action_recipes/check-repository/. Tier 2.
Data extracted: Repository-wide link checking patterns, automated issue creation. (From discovery agent.)

[45] MkDocs — Deploying Your Docs. mkdocs.org/user-guide/deploying-your-docs/. Tier 2.
Data extracted: ghp-import tool usage, branch configuration, deployment strategies. (From discovery agent.)

## Agentic Documentation Lifecycle

[46] DocAgent: Multi-Agent Code Documentation Generation (ACL 2025). arxiv.org/abs/2504.08725. Tier 1.
Data extracted: Five-agent architecture (Reader, Searcher, Writer, Verifier, Orchestrator). Topological code processing for incremental context building. Evaluation on completeness, helpfulness, truthfulness. "DocAgent significantly outperforms baselines consistently."

[47] Productverse — Automating Docs with Claude Code. productver.se/p/automating-docs-with-claude-code. Tier 3.
Data extracted: Five modular skills (create-release, update-product-doc, capture-screenshots, sync-docs, create-changelog). Documentation overhead reduced from "1-5 hours per feature" to ~15 minutes human review. Claude analyzes actual implementation rather than relying on outdated specs.

[48] Kinde — Spec Drift: The Hidden Problem AI Can Help Fix. kinde.com/learn/ai-for-software-engineering/ai-devops/spec-drift-the-hidden-problem-ai-can-help-fix/. Tier 3.
Data extracted: "The implementation—the actual code—evolves, but the API contracts, help guides, and internal docs are left behind." AI detection via CI/CD: parse specs, analyze codebase, flag mismatches. Automated responses: PRs, notifications, build failures.

[49] GitHub Blog — Automate Repository Tasks with GitHub Agentic Workflows. github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/. Tier 2.
Data extracted: Announced February 2026, technical preview. "Continuous documentation" use case: "keep READMEs and documentation aligned with code changes." Read-only by default, write via "safe outputs." Workflow files: YAML frontmatter + Markdown instructions.

[50] Graphite — AI Code Documentation Automation. graphite.com/guides/ai-code-documentation-automation. Tier 3.
Data extracted: "AI can produce accurate and relevant documentation that aids in code comprehension and maintenance." Best practice: "treat AI output as first drafts for developer review." Limitation: "struggles with complex algorithms, business rationale, and edge cases without human input."

[51] PMC — Systematic Review of AI-Powered Documentation Systems. pmc.ncbi.nlm.nih.gov/articles/PMC11835907/. Tier 1.
Data extracted: Hallucination rates in AI-generated documentation range from 3-27% across studies. (From discovery agent.)

[52] Sequin Blog — Diátaxis Case Study (Claude as editor). blog.sequinstream.com/we-fixed-our-documentation-with-the-diataxis-framework/. Tier 4.
Data extracted: Used Claude to catch when explanation crept into how-tos or reference mixed improperly. (Same source as [25], cited here for the agent-as-reviewer pattern.)
