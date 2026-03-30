# Agentic Documentation Lifecycle

How general-purpose AI coding agents (Claude Code, Cursor, Copilot) serve as primary documentation authors — generating, maintaining, validating, and reviewing project docs. Sources: [citations.md](../citations.md).

## The Four Lifecycle Stages

| Stage | What the Agent Does | Tooling Gate |
|-------|--------------------|--------------|
| **Generate** | Creates docs from code, specs, or transcripts | Vale + markdownlint must pass |
| **Maintain** | Detects code-doc drift, updates docs when code changes | CI drift detection |
| **Validate** | Verifies docs against actual code behavior | Automated testing, link checking |
| **Review** | Audits docs against quality frameworks (Diátaxis, style guides) | LLM-as-reviewer prompt |

## Generation

### Multi-Agent Architecture (DocAgent)

DocAgent (ACL 2025) demonstrates that multi-agent architectures outperform single-agent approaches for code documentation [46]. Five specialized agents collaborate:

- **Reader**: Processes and analyzes code structure
- **Searcher**: Locates relevant context and dependencies
- **Writer**: Generates documentation content
- **Verifier**: Validates accuracy and completeness
- **Orchestrator**: Coordinates the collaboration

The system uses topological code processing — analyzing code in dependency order so each component's documentation builds on already-documented dependencies. Ablation study "confirms the vital role of the topological processing order" [46]. Evaluation measures completeness, helpfulness, and truthfulness [46].

This maps directly to how a coding agent like Claude Code generates docs: it reads the codebase (Reader), searches for context (Searcher), writes documentation (Writer), and can be prompted to verify its own output (Verifier). The human serves as Orchestrator.

### Practical Agent Workflow

A documented Claude Code workflow uses five modular skills [47]:

1. `@update-product-doc` — generates user-focused markdown with structured sections
2. `@capture-screenshots` — uses Computer Use API to navigate apps and capture visuals
3. `@sync-docs` — converts markdown to knowledge base formats
4. `@create-changelog` — produces channel-specific announcements
5. `@create-release` — orchestrates all skills in sequence

The synchronization strategy: Claude analyzes actual implementation to understand "what actually exists" rather than relying on outdated specifications [47]. This is spec-from-code, not code-from-spec.

**Time savings**: Documentation overhead reduced from "1-5 hours per feature" to approximately 15 minutes of human review time [47].

### Generation Best Practices

"AI can produce accurate and relevant documentation that aids in code comprehension and maintenance" [50]. But:

- **Treat agent output as first drafts** for human review [50]
- **Document business logic separately** — agents struggle with rationale and edge cases [50]
- **Regenerate after significant code changes** rather than patching [50]
- Agent-generated docs "often produce incomplete, unhelpful, or factually incorrect outputs" when architecture isn't designed to prevent this [46]

### Quality Risk: Hallucination

A systematic review of AI-powered documentation systems found hallucination rates ranging from 3-27% across studies [51]. This is the central risk of agentic documentation — the agent generates plausible but incorrect descriptions of code behavior. Mitigation:

1. **Linting gates**: Vale + markdownlint catch structural and style issues (but not factual errors)
2. **Verification step**: Separate agent pass (or human review) specifically checking claims against code
3. **CI validation**: Automated tests that exercise documented procedures
4. **Multi-agent separation**: Writer and Verifier as distinct roles, not one agent doing both [46]

## Maintenance: Drift Detection

### The Drift Problem

"The implementation — the actual code — evolves, but the API contracts, help guides, and internal docs are left behind" [48]. Causes: tight deadlines, unclear ownership, informal communication channels, code-first development where docs are afterthoughts [48].

### AI-Powered Drift Detection

AI integrated into CI/CD can [48]:

1. Parse specification files (OpenAPI/Swagger, or structured docs)
2. Analyze actual codebase implementation
3. Identify mismatches in endpoints, data types, deprecated features
4. Automatically flag discrepancies

### Automated Responses to Drift

When drift is detected, the system can trigger [48]:

- **Pull requests** with corrective documentation changes
- **Notifications** alerting maintainers
- **Build failures** preventing deployment until docs are updated

### GitHub Agentic Workflows

GitHub Agentic Workflows (technical preview, February 2026) enable "continuous documentation" — "keep READMEs and documentation aligned with code changes" [49]. Workflows are defined as Markdown files with YAML frontmatter specifying triggers, permissions, and allowed outputs [49].

Key security property: "Workflows run with read-only permissions by default. Write operations require explicit approval through safe outputs, which map to pre-approved, reviewable GitHub operations such as creating a pull request" [49].

This means documentation updates by agents go through PR review, not direct commits — preserving human oversight.

### Practical Drift Detection for Solo Developers

Without GitHub Agentic Workflows (still in preview), a solo developer can implement drift detection with:

1. **Git hooks or CI checks**: Compare doc timestamps against related code file timestamps
2. **Agent review on PR**: Prompt the coding agent to check if the PR changes affect documented behavior
3. **Scheduled agent audit**: Weekly agent run that reads docs and checks claims against current code
4. **CLAUDE.md / AGENTS.md instructions**: Tell the agent to update docs whenever it modifies code that affects documented behavior

## Validation

Validation is distinct from review — it checks whether documented procedures actually work, not whether the writing is good.

### Automated Validation Approaches

1. **Code example execution**: Extract code blocks from docs and run them (language-specific)
2. **Link checking**: lychee catches broken internal and external links [18]
3. **API contract testing**: Compare documented endpoints/parameters against actual API (for API docs)
4. **Screenshot freshness**: Agent can re-capture screenshots and diff against documented versions [47]

### Agent-as-Validator Pattern

Prompt a coding agent to:

1. Read each documented procedure
2. Attempt to follow the steps against the actual codebase
3. Report where steps fail, are incomplete, or produce different results than documented
4. Flag outdated configuration values, renamed functions, changed CLI flags

This is the highest-value agent application for documentation quality — factual accuracy is the dimension where human review is most expensive and agent review is most effective (humans skim procedures; agents execute them literally).

## Review: Agent as Quality Auditor

### Diátaxis Classification Review

Agents can audit existing docs against the Diátaxis framework. The Sequin case study demonstrated using Claude to catch "when explanation crept into how-tos or reference material mixed improperly" [52]. The agent acts as a structural reviewer, not just a prose reviewer.

Prompt pattern for Diátaxis review:
- Feed the agent the four Diátaxis types with definitions
- Ask it to classify each doc page
- Flag pages that mix types
- Identify missing coverage (e.g., no tutorials, or reference without how-to guides)

### Style Guide Enforcement

Vale handles automated style enforcement in CI [11][12]. But agents can supplement Vale with semantic review:

- **Audience appropriateness**: Is the language calibrated for the target reader?
- **Completeness**: Are prerequisites stated? Are error cases covered?
- **Consistency**: Do terms match across documents?
- **Scannability**: Can a reader find what they need without reading everything?

### The Separation Principle

The same agent should not write and review its own documentation in a single pass. The DocAgent architecture enforces this with separate Writer and Verifier roles [46]. For a solo developer using Claude Code:

1. **Pass 1 (Generation)**: Agent writes docs from code/specs
2. **Pass 2 (Linting)**: Vale + markdownlint catch style/structure issues (automated, no agent needed)
3. **Pass 3 (Review)**: Agent reviews docs against Diátaxis, quality checklist, and code accuracy — in a separate session with no memory of having written them
4. **Human review**: Final pass, focusing on business logic, audience fit, and claims the agent can't verify

## How This Changes the Tooling Stack

When agents are the primary authors, the tools from dimensions 1-5 serve different roles:

| Tool | Human-Author Role | Agent-Author Role |
|------|-------------------|-------------------|
| MkDocs Material | Authoring environment | Build/deploy target (agent writes raw Markdown) |
| Vale | Writing assistant | **CI gate** agent output must pass |
| markdownlint | Writing assistant | **CI gate** agent output must pass |
| lychee | Periodic check | **CI gate** on every agent-generated PR |
| Diátaxis | Mental model for author | **Prompt constraint** for agent generation + review |
| Google style guide | Reference while writing | **Vale package** enforced automatically |
| GitHub Actions | Build/deploy automation | **Orchestrator** for multi-stage agent pipeline |

The key shift: tools move from "helping the human write better" to "ensuring the agent's output meets standards before it reaches the human."

## Gaps and Limitations

- DocAgent is the only peer-reviewed multi-agent documentation system found (ACL 2025) — the field is nascent [46]
- Hallucination rate data (3-27%) comes from clinical documentation, not software documentation [51] — rates may differ
- Time savings claim ("1-5 hours to ~15 minutes") is from a single practitioner report, not a controlled study [47]
- GitHub Agentic Workflows is in technical preview — not production-ready [49]
- No published benchmarks comparing agent-generated vs. human-authored documentation quality for software projects
- Drift detection tools are mostly conceptual or early-stage — no mature, widely-adopted solution exists
- The agent-as-validator pattern (checking if documented procedures work) is described conceptually but lacks tooling support
