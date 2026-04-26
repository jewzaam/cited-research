# Dup-check / anti-reinvention checks for AI-generated code

**Last revised:** 2026-04-26

## Question

Is the custom dup-check stage (jscpd via npx + 5 custom semgrep rules for "imported X but reimplementing X") reinventing tooling that already exists, or filling a real gap?

## Answer (one paragraph)

**It's filling a real gap, with bounded maintenance cost.** jscpd remains the right portable npx-installable clone detector — no credible replacement has emerged. Of the 5 custom semgrep rules, three (csv, json, argparse) have no off-the-shelf equivalent in any tool surveyed; one (tempfile) overlaps partially with bandit S108 on a different aspect; one (pathlib) overlaps substantially with the ruff PTH series, but ruff's PTH fires unconditionally — a different (noisier) semantic than the user's import-conditional design. Single-CLI bundles like MegaLinter and Qlty exist but delegate their lint layer to Ruff with the same unconditional PTH semantics, so the custom layer is still doing work no off-the-shelf tool replicates. Recommendation: **keep the rules, layer ruff for incidental coverage, publish the 5 rules as a Trail of Bits-style external pack** rather than contributing upstream.

## Verdict-per-dimension table

| Dimension | Verdict |
|---|---|
| 1. Clone detection landscape | **Off-the-shelf available — keep jscpd.** |
| 2. Stdlib-preference rules | **Mixed.** Rules 1/2/5 (csv, json, argparse) novel; rule 3 (tempfile) partial; rule 4 (pathlib) substantial overlap with different semantic. |
| 3. All-in-one packaged tools | **Partial.** MegaLinter/Qlty bundle both, but neither replaces the user's custom layer. |
| 4. AI-code-quality tools | **Partial.** sloppylint/KarpeSlop exist but catch *different* AI patterns. No tool markets "anti-reinvention" specifically. |
| 5. Custom rule-pack maintenance | **Bounded.** Simple structural rules are insulated from semgrep's churn surfaces. |

## Rule-by-rule mapping (the answer to the user's main question)

| User's rule | Closest existing check | Effective cover | Verdict |
|---|---|---|---|
| **csv-stdlib** | None | 0 | **Novel — keep** |
| **json-stdlib** | None | 0 | **Novel — keep** |
| **tempfile-stdlib** | bandit S108 / ruff S108 (path-only, not import-aware); pylint R1732 (lifecycle) | ~0.3 | **Mostly gap — keep** |
| **pathlib-over-ospath** | ruff PTH series (unconditional migration sweep, not consistency check) | ~0.7 | **Best-covered, but noisier alternative — keep for precision** |
| **argparse-over-sysargv** | None | 0 | **Novel — keep** |

## Quick decision framework

1. **Are you using jscpd today?** Keep it. No replacement has emerged.
2. **Do you have a Python project that already uses csv/json/tempfile/pathlib/argparse?** The user's 5 rules add value above any combination of ruff/refurb/pylint/bandit. Keep them.
3. **Are you pre-commit gating?** Add ruff with `extend-select = ["PTH", "FURB", "SIM", "UP", "S"]` for incidental coverage. Run jscpd diff-scoped (via `git diff --name-only` + `--pattern`) on each commit AND full-repo periodically (clones span files).
4. **Are you maintaining the rules privately?** Consider publishing as an external Semgrep pack (Trail of Bits model — your repo, your license, indexed in the Semgrep registry). This avoids the Semgrep Rules License v1.0 relicensing that contributing upstream would impose.
5. **Don't rebrand as "AI-specific."** The patterns the rules catch are old human anti-patterns. AI is the *frequency* driver, not the pattern source.

## Files

- [`analysis.md`](analysis.md) — full deliverable with verdict-per-dimension, rule mapping table, and final recommendation
- [`citations.md`](citations.md) — all 74 sources with extraction notes and tier classification
- [`references/clone-detection.md`](references/clone-detection.md) — Dimension 1 detail
- [`references/stdlib-preference-rules.md`](references/stdlib-preference-rules.md) — Dimension 2 detail (the rule-by-rule mapping)
- [`references/packaged-tools.md`](references/packaged-tools.md) — Dimension 3 detail
- [`references/ai-code-quality-tools.md`](references/ai-code-quality-tools.md) — Dimension 4 detail
- [`references/custom-rule-maintenance.md`](references/custom-rule-maintenance.md) — Dimension 5 detail
- [`audit/`](audit/) — citation audit and consistency-review reports

## Confidence

Highest confidence: jscpd is the right clone-detection choice; rules 1/2/5 have no equivalent; ruff PTH is unconditional and not an import-conditional drop-in for rule 4.

Lower confidence: vendor-published AI-tool benchmarks (Greptile, DiffRay) lack independent verification; some Tier-3 sources (community forum threads, blog posts) rely on agent search snippets rather than direct fetches; jscpd npm registry page returned 403 in-session so version/download stats are from agent search snippets rather than direct registry read.

Hard limit: per the April 2026 hallucination-ceiling paper [59 in citations.md], 23-52% of library hallucinations are structurally undetectable by static analysis. The user's rules (like all linters) operate within this ceiling — they catch a subset of reinvention; some patterns will always require human or AI-augmented review.
