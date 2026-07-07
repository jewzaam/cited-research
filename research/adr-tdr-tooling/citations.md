# Citations

All sources visited in-session on 2026-07-07 via WebSearch or WebFetch.

**[1]** "Decision Capturing Tools." *Architectural Decision Records (adr.github.io)*, 2024.
<https://adr.github.io/adr-tooling/>
**Tier:** 1
Comprehensive catalog of 36 ADR tools organized by template support, language, and maintenance status.

**[2]** "Overview — Structured MADR Specification v1.0.0." *smadr.dev*, 2026.
<https://smadr.dev/reference/specification/overview/>
**Tier:** 1
Specification of Structured MADR format: 13 required components, YAML frontmatter, JSON Schema validation, AI optimization design goal.

**[3]** "Frontmatter — Structured MADR Specification." *smadr.dev*, 2026.
<https://smadr.dev/reference/specification/frontmatter/>
**Tier:** 1
Complete YAML frontmatter schema: 10 required fields (title, description, type, category, tags, status, created, updated, author, project) and 3 optional fields (technologies, audience, related).

**[4]** "Format Comparison." *smadr.dev*, 2026.
<https://smadr.dev/explanation/format-comparison/>
**Tier:** 1
Side-by-side comparison of Nygard, MADR, Structured MADR, Y-Statement, and Tyree-Akerman formats across machine-readability, human-friendliness, overhead, and situational fit.

**[5]** "AI Integration Guide." *smadr.dev*, 2026.
<https://smadr.dev/guides/ai-integration/>
**Tier:** 2
Integration patterns for Claude Code, GitHub Copilot, and Cursor with Structured MADR. Describes how YAML frontmatter enables filtering, relationship tracking, and status-aware AI behavior.

**[6]** "One Size Fits All? An Empirical Comparison of Architecture Decision Record Templates." *arXiv*, 2604.27333v1, 2026.
<https://arxiv.org/html/2604.27333v1>
**Tier:** 1
Controlled experiment (n=33) comparing five ADR templates. Nygard outperformed MADR (Wilcoxon W=84.0, p=0.002, Cliff's Delta=0.6364). Context-dependent selection recommended.

**[7]** "About MADR." *MADR (adr.github.io/madr)*, 2024.
<https://adr.github.io/madr/>
**Tier:** 1
Official MADR v4.0.0 specification: template structure, YAML frontmatter (optional), file naming convention (NNNN-title-with-dashes.md), three template variants (full, minimal, bare). License: MIT OR CC0-1.0.

**[8]** Fowler, Martin. "Architecture Decision Record." *martinfowler.com*, 2026.
<https://martinfowler.com/bliki/ArchitectureDecisionRecord.html>
**Tier:** 1
Canonical industry guidance on ADRs. Recommends lightweight Markdown, inverted pyramid writing, single-page brevity, immutable accepted records. Only tool mentioned: adr-tools.

**[9]** "adr-tools." *GitHub (npryce/adr-tools)*, 2018.
<https://github.com/npryce/adr-tools>
**Tier:** 1
Original ADR CLI. Shell scripts, ~5,600 stars, 633 forks. Last release v3.0.0 (July 2018). 32 open issues, 37 open PRs. Dormant but functional.

**[10]** "ad-guidance-tool (ADG)." *GitHub (adr/ad-guidance-tool)*, 2026.
<https://github.com/adr/ad-guidance-tool>
**Tier:** 1
Go-based ADR tool with built-in MCP server (5 tools: list_adrs, get_adr, get_dsl_reference, list_rule_files, validate_rule). Decision modeling, rule enforcement via DSL. Apache 2.0. v1.1.0 (June 2026), 35 stars.

**[11]** "adrs." *GitHub (joshrotenberg/adrs)*, 2026.
<https://github.com/joshrotenberg/adrs>
**Tier:** 1
Rust ADR tool. MCP server, JSON-ADR export/import, NextGen YAML frontmatter mode, full-text search, Graphviz graphs. MIT OR Apache-2.0. v0.8.0 (June 2026), 95 stars, 292 commits.

**[12]** "structured-madr." *GitHub (modeled-information-format/structured-madr)*, 2026.
<https://github.com/modeled-information-format/structured-madr>
**Tier:** 1
Structured MADR reference implementation. Claude Code plugin (commands, agent, skill, hook), GitHub Action validator on Marketplace, MIF JSON-LD conformance levels 1-3. MIT. v1.2.0 (April 2026), 9 stars.

**[13]** "Agent Decision Records (AgDR)." *GitHub (me2resh/agent-decision-record)*, 2026.
<https://github.com/me2resh/agent-decision-record>
**Tier:** 2
ADR variant for AI agent decisions. Required frontmatter: agent, model, trigger, timestamp, status, id. Tooling for Claude Code (/decide), Codex, Cursor, Copilot, Windsurf. JSON Schema validation, 3 CI workflows.

**[14]** "Log4brains." *GitHub (thomvaill/log4brains)*, 2024.
<https://github.com/thomvaill/log4brains>
**Tier:** 1
TypeScript ADR knowledge base with static site generation, hot-reload preview, timeline search. Apache 2.0. v1.1.0 (Dec 2024), ~1,500 stars. MADR default template. Requires Node.js.

**[15]** "@meza/adr-tools." *GitHub (meza/adr-tools)*, 2026.
<https://github.com/meza/adr-tools>
**Tier:** 2
TypeScript full reimplementation of npryce adr-tools. GPL-3.0. v2.0.1 (Jan 2026), 20 stars, 533 commits. npm install --save-dev @meza/adr-tools.

**[16]** "pyadr." *GitHub (opinionated-digital-center/pyadr)*, 2023.
<https://github.com/opinionated-digital-center/pyadr>
**Tier:** 2
Python ADR lifecycle tool. MIT. v0.20.0 (April 2023), 56 stars. Pre-alpha. MADR 2.1.2. Deprecate/supersede not implemented. pip install pyadr.

**[17]** "adr-tool." *GitHub (aholbreich/adr-tool)*, 2026.
<https://github.com/aholbreich/adr-tool>
**Tier:** 2
Go ADR CLI with status tracking, git commit integration, shell completions, RPM packaging. MIT. v0.6.0 (April 2026), 5 stars, 94 commits.

**[18]** "Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models." *arXiv*, 2408.02442v1, 2024.
<https://arxiv.org/html/2408.02442v1>
**Tier:** 1
Study of format restrictions on LLM reasoning. JSON schema dropped Claude-3-Haiku GSM8K accuracy from 86.99% to 23.44%. Key ordering forces direct answering over chain-of-thought. NL-to-Format two-step preserves performance.

**[19]** "ADR Templates." *Architectural Decision Records (adr.github.io)*, 2024.
<https://adr.github.io/adr-templates/>
**Tier:** 1
Template catalog: Nygard (5 sections), MADR (10 sections with annotated/bare variants), Y-Statement, Tyree-Akerman, arc42.

**[20]** Zimmermann, Olaf. "The Markdown ADR (MADR) Template Explained and Distilled." *ozimmer.ch*, 2022 (updated 2026).
<https://ozimmer.ch/practices/2022/11/22/MADRTemplatePrimer.html>
**Tier:** 1
MADR template deep-dive by co-creator. V4.0 renamed elements, introduced minimal variant. ADR anti-patterns: Mega-ADRs, Blueprint in Disguise, Novel/Epic.

**[21]** Zimmermann, Olaf. "How to Create ADRs." *ozimmer.ch*, 2023.
<https://ozimmer.ch/practices/2023/04/03/ADRCreation.html>
**Tier:** 1
ADR creation guidance. ADR Author Pledge recommends sizing adequately rather than rigid template adherence. Anti-patterns from over-standardization.

**[22]** "Architecture Decision Records." *Red Hat Blog*, n.d.
<https://www.redhat.com/en/blog/architecture-decision-records>
**Tier:** 2
Enterprise ADR guidance. Co-location with source code matters more than tooling. Standard git workflows sufficient. Multi-repo: use main repo + links.

**[23]** "Markdown Architectural Decision Records: Format and Tool Support." *CEUR Workshop Proceedings*, Vol-2072, 2018.
<https://ceur-ws.org/Vol-2072/paper9.pdf>
**Tier:** 1
**Access:** PDF extraction not attempted. Academic paper on MADR format and tooling. Referenced for MADR origin and citation.

**[24]** "Clarity from Chaos — Overcoming Tooling Fragmentation in Platform Engineering." *ThoughtWorks Insights*, 2025.
<https://www.thoughtworks.com/insights/blog/platforms/clarity-from-chaos--overcoming-tooling-fragmentation-in-platform>
**Tier:** 1
Tool fragmentation creates data silos, duplicated effort, training complexity, context-switching tax. Collection of tools ≠ platform.

**[25]** "The Danger in Tools Fragmentation." *StoneTusker*, n.d.
<https://stonetusker.com/the-danger-in-tools-fragmentation-why-minimizing-and-integrating-your-software-tools-matters>
**Tier:** 3
30% deployment time reduction after consolidating to integrated platform. Maintenance burden compounds as toolset grows.

**[26]** Strengholt, Piethein. "Building an Architecture Decision Record Writer Agent." *Medium*, 2025.
<https://piethein.medium.com/building-an-architecture-decision-record-writer-agent-a74f8f739271>
**Tier:** 3
ADR writer agent using OpenAI Agents SDK. Multi-agent pipeline with validation. MADR template for AI generation.

**[27]** "Accelerating Architectural Decision Records (ADRs) with Generative AI." *Equal Experts Blog*, n.d.
<https://www.equalexperts.com/blog/our-thinking/accelerating-architectural-decision-records-adrs-with-generative-ai/>
**Tier:** 2
Metaprompting approach for AI-generated ADRs. Template prompts with unique identifiers and standardized headings.

**[28]** Brown, Simon. "Visualising ADRs." *dev.to*, n.d.
<https://dev.to/simonbrown/visualising-adrs-3klm>
**Tier:** 3
Structurizr force-directed graph visualization of ADR relationships. Minimal tools lack visualization of decision chains.

**[29]** "ADRs as a Team Habit." *dev.to (maximeshr)*, n.d.
<https://dev.to/maximeshr/adrs-as-a-team-habit-the-fastest-path-to-better-engineering-decisions-2b2m>
**Tier:** 3
Three ADR failure modes: too much ceremony, no trigger points, tooling friction (manual folder/file/number/template creation).

**[30]** "ADR Manager." *GitHub (adr/adr-manager)*, n.d.
<https://github.com/adr/adr-manager>
**Tier:** 2
Web app and VS Code extension for form-based ADR editing. Connects to GitHub API. MADR 2.1.2. Origin: undergraduate research at U Stuttgart.

**[31]** Konishi, Hidekazu. "Architecture Decision Records: Templates and Operational Patterns." *hidekazu-konishi.com*, 2026.
<https://hidekazu-konishi.com/entry/architecture_decision_records_templates_and_operations.html>
**Tier:** 2
Same decision written in Nygard, MADR, and Y-Statement formats. "The act of writing the ADR is often more valuable than the ADR itself."

**[32]** "Earn Maintainers Esteem with ADRs." *understandlegacycode.com*, n.d.
<https://understandlegacycode.com/blog/earn-maintainers-esteem-with-adrs/>
**Tier:** 3
"Keep your ADRs stupid simple." Five essential elements sufficient. Format deliberately subordinated to substance.

**[33]** "MADR Issue #28: Concurrent numbering collision." *GitHub (adr/madr)*, n.d.
<https://github.com/adr/madr/issues/28>
**Tier:** 2
Race condition when multiple developers assign same ADR number simultaneously. Highlights need for automated numbering.

**[34]** "MADR Issue #75: Format inconsistency." *GitHub (adr/madr)*, n.d.
<https://github.com/adr/madr/issues/75>
**Tier:** 4
Options section uses flat list with Good/Bad prefixes while Outcome uses subsections. Prevents copy-paste workflow.

**[35]** "Enforcing Invariants in AI-Generated Code." *Bit by Byte (Substack)*, n.d.
<https://bitbytebit.substack.com/p/enforcing-invariants-in-ai-generated>
**Tier:** 3
Recording decisions pointless if agents never read them. Prose is suggestive not enforceable. Deterministic hooks needed for validation.

**[36]** "How to Give AI Coding Agents Long-Term Memory." *Voxos.ai Blog*, n.d.
<https://voxos.ai/blog/how-to-give-ai-coding-agents-long-term-m/index.html>
**Tier:** 3
Plain AGENTS.md files outperform vector databases (74% vs 68.5%). Instruction ceiling ~150-200 instructions. Lost-in-the-middle effects.

**[37]** "The Best Input Data Format for LLMs." *ImprovingAgents.com*, n.d.
<https://www.improvingagents.com/blog/best-input-data-format-for-llms/>
**Tier:** 2
Format accuracy ranking: Markdown-KV 60.7% vs CSV 44.3% vs NL 49.6%. Simple per-record labeling beats traditional structured formats.

**[38]** "Architecture Decision Record (ADR) examples." *GitHub (architecture-decision-record)*, n.d.
<https://github.com/architecture-decision-record/architecture-decision-record>
**Tier:** 2
Comprehensive ADR examples and conventions. Directory naming patterns, file naming conventions, template examples across formats.

**[39]** "Y-Statements." *Medium (olzzio/Olaf Zimmermann)*, n.d.
<https://medium.com/olzzio/y-statements-10eb07b5a177>
**Tier:** 1
Y-statement format: "In the context of [situation], facing [concern], we decided [option] to achieve [quality], accepting [downside]." Six-part single-sentence format.

**[40]** "adr.zone." *adr.zone*, n.d.
<https://www.adr.zone/>
**Tier:** 2
Web-based ADR generator. Supports Nygard, MADR, Y-Statement, ISO/IEC/IEEE 42010 formats. API for programmatic generation. No signup required.

**[41]** "8 Best Practices for Creating Architecture Decision Records." *TechTarget*, 2025.
<https://www.techtarget.com/searchapparchitecture/tip/4-best-practices-for-creating-architecture-decision-records>
**Tier:** 2
ADR best practices and tool overview. Updated 2025 with expanded tool list.

**[42]** "adr-viewer." *GitHub (mrwilson/adr-viewer)*, n.d.
<https://github.com/mrwilson/adr-viewer>
**Tier:** 2
Python tool generating HTML visualization from ADRs. Available via PyPI and Homebrew. Workflow activity as of Dec 2024.

**[43]** "The ADR Problem." *jensrantil.github.io*, n.d.
<https://jensrantil.github.io/posts/the-adr-problem/>
**Tier:** 3
Organizational governance as root cause of ADR failure. Vertical/horizontal scoping challenge.

**[44]** "Effective ADRs Guide for Software Architects." *developersvoice.com*, n.d.
<https://developersvoice.com/blog/architecture/effective-adrs-guide-for-software-architects/>
**Tier:** 3
"Write-Only Swamp" failure mode. Retroactive documentation as time sink. Warning against enforcing ADRs everywhere from day one.

**[45]** "ADR Process." *AWS Prescriptive Guidance*, n.d.
<https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html>
**Tier:** 1
ADR lifecycle states: Draft/Proposed, Accepted, Active, Superseded, Deprecated. Formal process for enterprise contexts.

**[46]** "dotnet-adr." *GitHub (endjin/dotnet-adr)*, n.d.
<https://github.com/endjin/dotnet-adr>
**Tier:** 2
Cross-platform .NET ADR tool. dotnet tool install -g adr. MADR default template. Apache 2.0. 123 stars.

**[47]** "Talo." *GitHub (canpolat/talo)*, n.d.
<https://github.com/canpolat/talo>
**Tier:** 2
.NET CLI for ADRs, RFCs, and custom document types. Export capability, custom templates.

**[48]** "RFCs vs ADRs." *designdoc.tech*, n.d.
<https://designdoc.tech/blog/rfcs-vs-adrs>
**Tier:** 3
ADRs should take 10-20 minutes to write. RFCs require hours/days. Process can kill momentum.

**[49]** "ADR-first Development." *johnclick.ai*, n.d.
<https://johnclick.ai/blog/adr-first-development-architecture-decision-records/>
**Tier:** 3
Four-tier system to prevent over-documentation. "Value is in the reasoning, not the formatting."

**[50]** "Architecture Decision Records: A Complete Guide." *archyl.com*, n.d.
<https://www.archyl.com/blog/architecture-decision-records-complete-guide>
**Tier:** 3
In-repo markdown most popular approach. Wikis are where ADRs "go to be forgotten." Abandonment risk with only 1-2 ADRs.
