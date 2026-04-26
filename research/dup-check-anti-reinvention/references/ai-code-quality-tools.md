# Reference: AI-code-quality-specific tools

Sources cited inline as `[N]` against [citations.md](../citations.md).

## What this dimension covers

Has anyone shipped a quality gate explicitly framed around LLM-generated reinvention / hallucination patterns — not generic linters relabeled "AI"? If yes, are they credible and maintained?

## Two distinct tool categories

The market splits in 2024-2026 into two recognizable categories:

### Category A: AI-specific lint-style tools (substantive, niche)

These tools detect specific patterns that LLMs produce and human developers usually don't.

| Tool | Languages | What it detects | Maintenance | License |
|---|---|---|---|---|
| **sloppylint** [50] | Python | Hallucinated imports (non-existent packages); cross-language leakage (`.push()`, `.equals()`, `.each` in Python); placeholder code; bare except | v0.5.1 published 2025-12-21 | MIT |
| **KarpeSlop** [49] | TypeScript / JavaScript / React / Next.js | Hallucinated imports; `any` abuse; "vibe coding" patterns; comment quality | 30 stars; activity unclear | MIT |
| **AI-SLOP-Detector** [51] | Per agent: Python | Unimplemented stubs; phantom imports; placeholder-heavy paths; "jargon inflation" | v3.5.0 in 2025 | Open source |
| **GPTLint** [52] | LLM-assisted, generic | Markdown-defined custom rules; two-pass weak/strong model design | Last commit July 2024 — likely stalled | MIT |

### Category B: AI code review platforms (substantive, broader scope)

These review entire diffs/PRs with codebase-aware AI agents. They review all code, not just AI-generated code, but the architecture (multi-agent, codebase-indexed) targets problems generic linters miss.

| Tool | Approach | Maintenance | Notes |
|---|---|---|---|
| **CodeRabbit** [53] | ast-grep (deterministic AST) → LLM with RAG | Active SaaS | Explicitly NOT positioned as AI-specific — generic code reviewer |
| **Cursor BugBot** [62] | PR review agent; logic bugs not style; self-improves | Shipped July 2025; 80% resolution rate, 2M+ PRs/month | Reviews all code |
| **Greptile** [56] | Codebase-indexed semantic graph; cross-file context | Active; YC-backed; 82% catch rate (vendor benchmark) | Closest architecture for "this duplicates an existing internal abstraction" detection |
| **Korbit** [63] | LLM-as-judge with Chain-of-Thought; "Undetermined" classification | Active commercial | Detects hallucinations in **its own** review output (FP suppression), not in code being reviewed |
| **DiffRay** [64] | 10+ specialized agents (security, concurrency, etc.) | Launched 2024-2025 | Vendor claims of "87% fewer FPs" not independently verified |
| **Snyk AI** [61] | Taint analysis treating LLM-library outputs as untrusted sources | Active commercial | Substantive AI-specific security capability |

## Independent academic frame

**CodeHalu (AAAI 2025)** [54] is the canonical academic taxonomy. Defines 4 categories of LLM code hallucination:
1. Mapping hallucinations
2. Naming hallucinations
3. Resource hallucinations
4. Logic hallucinations

Plus a benchmark (CodeHaluEval, 8,883 samples, 699 tasks) for evaluating LLMs.

**Zhang et al. 2025** [55] proposes a different 3-category taxonomy that includes **Project Context Conflicts** — the LLM not knowing what already exists in the project's codebase. This is the closest academic match for "reinvention" — the model writing a new function that duplicates an existing internal abstraction.

**Static analysis hallucination ceiling paper (April 2026)** [59]: empirical finding that static analysis tools detect 14-85% of library-use hallucinations, with a manually-determined upper bound of 48.5-77%. Meaning **23-52% of library hallucinations are structurally undetectable by any pattern-matching approach** — they require semantic context. This is a hard limit on the user's semgrep-based approach (and on every linter), not a critique of the user's specific rules.

## Counter-evidence on Category B credibility

The DeepSource analysis [57] is the most damning external critique of vendor benchmarks: the same 5 OSS repos that Greptile claimed an 82% catch rate on, Augment scored 45% on. Methodology choices (what counts as "caught", scoring rules) produce 37-point swings. Verbatim from DeepSource: "Self-evaluation is biased, even in good faith. None of this [independent datasets, reproducible methodology] exists for AI code review yet."

Cloudflare's production deployment post [58] is the strongest counter to "AI review is just marketing": their multi-agent system (up to 7 specialized reviewers + a coordinator) ran 131,246 reviews across 48,095 merge requests in 5,169 repositories in a single month, with a 0.6% developer override rate. The system blocks merges on critical findings. Their published architecture (separate agents for security, performance, compliance, release management) is not replicable with any combination of ruff/pylint/SonarQube — it requires intent and business context understanding.

## Practitioner field guide

The "Lint Against the Machine" article (March 6, 2026) [60] is the most actionable practitioner reference. It explicitly maps AI anti-patterns to existing linter rules:

- Banned APIs → ruff TID251
- Blind exception catching → ruff BLE001
- Bare except → ruff E722
- Blocking calls in async → ruff ASYNC100-102
- Deprecated APIs → ruff UP rules
- TS `any` abuse → `@typescript-eslint/no-explicit-any`

And acknowledges patterns WITHOUT existing rules:
- Debugging residue (`rateLimiter_v2.py` style variant files) — "requires filesystem-level detection"
- Over-engineering (AbstractStrategyFactoryBuilder for a 50-LOC need) — "requires human judgment"
- Test validation issues — "tests that validate assumptions rather than behavior" need manual review

This article supports the user's framing: existing linters cover SOME AI anti-patterns. The user's "imported X but reimplementing X" pattern fits in the gap that needs custom rules.

## Are any tools positioned around AI reinvention specifically?

**No tool surveyed explicitly positions around "anti-reinvention" or "you imported the right API but reimplemented it" detection.** The closest is:

- **sloppylint's "lies" / "hallucinated imports" category** [50] — detects imports of packages that don't exist (Python-only). Different from the user's pattern: sloppylint detects fictional imports; the user's rules detect that the developer imported a real, correct module but didn't use it.
- **Greptile's codebase-aware architecture** [56] — could in principle detect "this function duplicates `utils/parse_csv.py`," but no public case study confirms it as a primary use case.
- **Project Context Conflicts category** [55] — the Zhang et al. paper names exactly the right pattern, but as research framework, not a tool.

## Verdict for Dimension 4

**Partial: AI-specific tools exist but address adjacent patterns, not the user's specific niche.** sloppylint [50] is the only Python-targeted, AI-positioned tool catching anti-reinvention-flavored patterns — and it catches **different** patterns (hallucinated imports, cross-language leakage). KarpeSlop [49] doesn't support Python. Commercial review platforms (CodeRabbit, Greptile, Cursor BugBot, etc.) review all code with general-purpose architectures; none publish a benchmark specifically for "imported-X-but-reimplementing-X" detection.

The most defensible position: the user's specific patterns are not currently covered by any maintained AI-specific tool. The framing assumption (Phase 0: "AI-generated code reinvention is a distinct class") is supported by sloppylint's existence and the academic taxonomies — but the specific patterns the user wrote are still new ground, more closely matched to "Project Context Conflicts" [55] than to any of the 4 CodeHalu categories [54].

## Gaps and limitations

- All Category A tool maintenance signals are weak: KarpeSlop has 30 GitHub stars [49], sloppylint is one developer, GPTLint may be abandoned [52]. None of these reach Trail-of-Bits-class maintenance.
- Vendor benchmarks (Greptile [56], DiffRay [64]) are self-reported and lack independent verification per [57]. Cloudflare's published usage figures [58] are internal data, not externally reproducible.
- The April 2026 hallucination-ceiling paper [59] was not directly fetched; cited via agent counter-discovery snippet.
- No tool was found that specifically markets "anti-reinvention" as a feature category. This is a true market gap as of 2026-04, with the academic terminology ("Project Context Conflicts" [55]) yet to be picked up by any productized tool.
