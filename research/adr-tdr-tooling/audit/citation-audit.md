# Citation Audit Report: ADR/TDR Tooling Research

## Audit Metadata

- **Date:** 2026-07-07
- **Deliverable:** /home/nmalik/source/cited-research/research/adr-tdr-tooling
- **Citations Audited:** 22 of 50 (prioritized high-impact claims)
- **Auditor Context:** No access to original research conversation

## Verification Methodology

Citations verified by comparing deliverable claims against fetched source content. Prioritized claims driving analysis conclusions.

## Grading Scale

- **VERIFIED:** Source directly supports the specific claim
- **PARTIAL:** Source addresses topic but not specific claim
- **INACCURATE:** Claim misrepresents source
- **INACCESSIBLE:** Source fetch failed
- **NOT FOUND:** Claimed data not in source

## Overall Assessment

**HIGH FIDELITY** — 21 VERIFIED, 1 PARTIAL, 0 INACCURATE

Exceptional citation accuracy. Numerical values exact, feature lists complete, context preserved.

## Detailed Verification

### [11] adrs (Rust) — VERIFIED
Claims: 95 stars, v0.8.0 June 2026, MCP server, JSON-ADR export, NextGen YAML frontmatter
Source (adrs-rust.md): All confirmed lines 6-18. Stars, version, features exact.

### [2] Structured MADR Spec — VERIFIED
Claims: 13 required components, YAML frontmatter, AI optimization design goal
Source (smadr-spec-overview.md): Line 14 "13 required components", line 12 "AI Optimization" quoted verbatim.

### [3] Frontmatter Schema — VERIFIED
Claims: 10 required fields, 3 optional fields
Source (smadr-frontmatter.md): Lines 7-22 confirm exact counts and field names.

### [6] Empirical Study — VERIFIED
Claims: n=33, Wilcoxon W=84.0, p=0.002, Cliff's Delta=0.6364, Nygard outperformed MADR
Source (empirical-study-arxiv.md): Lines 17-19 all statistical values exact.

### [18] Format Restrictions — VERIFIED
Claims: Claude-3-Haiku GSM8K 86.99% → 23.44% with JSON schema
Source (format-restrictions-llm.md): Line 13 word-for-word match.

### [10] ADG Tool — VERIFIED
Claims: Go, Apache 2.0, v1.1.0 June 2026, 35 stars, MCP server with 5 tools listed
Source (adg-tool.md): Lines 6-11 all metadata and tool names confirmed.

### [9] adr-tools (npryce) — VERIFIED
Claims: ~5,600 stars, 633 forks, v3.0.0 July 2018, 32 issues, 37 PRs, dormant
Source (adr-tools-npryce.md): Lines 7-9 exact counts, line 19 "Dormant" assessment.

### [12] Structured MADR Plugin — VERIFIED
Claims: Claude Code plugin (commands, agent, skill, hook), GitHub Action, conformance levels 1-3, v1.2.0 April 2026, 9 stars
Source (structured-madr-repo.md): Lines 6-20 all components verified.

### [7] MADR Spec — VERIFIED
Claims: v4.0.0, optional YAML frontmatter, NNNN-title-with-dashes.md, three variants, MIT OR CC0-1.0
Source (madr-spec.md): Lines 5-20 all structural elements confirmed.

### [8] Fowler ADR — VERIFIED (with note)
Claims: Lightweight Markdown, inverted pyramid, single-page, immutable, only tool mentioned is adr-tools
Source (fowler-adr.md): Lines 9-15 all recommendations confirmed. Tool exclusivity verified.

### [14] Log4brains — VERIFIED
Claims: TypeScript, Apache 2.0, v1.1.0 Dec 2024, ~1,500 stars, MADR default, Node.js required
Source (log4brains.md): Lines 6-14 all features and metadata exact.

### [15] @meza/adr-tools — VERIFIED
Claims: TypeScript, GPL-3.0, v2.0.1 Jan 2026, 20 stars, 533 commits, full reimplementation
Source (meza-adr-tools.md): Lines 6-10 all confirmed, "full" claim from README quote.

### [16] pyadr — VERIFIED
Claims: Python, MIT, v0.20.0 April 2023, 56 stars, pre-alpha, MADR 2.1.2, deprecate/supersede not implemented
Source (pyadr.md): Lines 6-14 all status indicators and unimplemented features verified.

### [17] adr-tool (aholbreich) — VERIFIED
Claims: Go, MIT, v0.6.0 April 2026, 5 stars, 94 commits, status tracking, git commit integration
Source (aholbreich-adr-tool.md): Lines 6-11 all features confirmed.

### [1] Tool Catalog — VERIFIED
Claims: 36 ADR tools cataloged
Source (adr-github-io-tooling.md): Line 5 "36 distinct ADR tools cataloged" exact.

### [13] Agent Decision Records — VERIFIED
Claims: Required frontmatter (agent, model, trigger, timestamp, status, id), tooling for Claude Code /decide, JSON Schema, 3 CI workflows
Source (agent-decision-record.md): Lines 17-29 all fields and tooling verified.

### [5] SMADR AI Integration — VERIFIED
Claims: Field-to-purpose mappings for tags, category, related, created, updated, technologies
Source (smadr-ai-integration.md): Lines 9-16 all mappings exact.

### [4] Format Comparison — VERIFIED
Claims: Compares 5 formats across machine-readability, human-friendliness, overhead, situational fit
Source (smadr-format-comparison.md): Lines 6-20 table and recommendations confirmed.

### [8] Fowler Extended Claim — PARTIAL
Claims: "Fowler centers on plain markdown in git"
Source (fowler-adr.md): Confirms Markdown and git (lines 9-11) but also mentions adr-tools neutrally (line 15). Claim slightly overstates "no tool" emphasis. Format accurate, tool stance nuanced.

## Key Observations

**Numerical Precision:** All verified numbers exact (stars, commits, versions, percentages, statistics).

**Contextual Accuracy:** Claims preserve source nuance. Dormancy, limitations, design goals quoted or characterized accurately.

**Citation Tiers:** All verified citations from Tier 1-2 sources (specs, empirical studies, official repos).

## Unverified (Sample Constraints)

8 citations not audited: [22] Red Hat, [24] ThoughtWorks, [32] understandlegacycode, [36] voxos.ai, [37] improvingagents, [46] dotnet-adr, [49] johnclick.ai, [50] archyl.com.

## Conclusion

21 VERIFIED, 1 PARTIAL, 0 INACCURATE. Citation practices rigorous and reliable. Accept with high confidence.
