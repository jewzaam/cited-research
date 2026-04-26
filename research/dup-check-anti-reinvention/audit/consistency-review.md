# Consistency review

Status: PASS with 3 minor notes (no blocking issues).

---

## Numerical inconsistencies (if any)

No contradictory numbers were found. The key figures reported across files are consistent:

- **"150+ languages"** (jscpd): consistent in analysis.md, references/clone-detection.md, and citations.md [1].
- **"192 FURB rules"**: stated only in citations.md [27]. Neither analysis.md nor references/stdlib-preference-rules.md repeats this number, so there is no cross-file conflict. The files that do reference refurb cite the import-conditional rule list (FURB107/118/134/140/152/180) without claiming any total count.
- **"23–52% structurally undetectable"**: stated consistently in analysis.md (lines 129, 247), README.md, and references/ai-code-quality-tools.md. The companion figures (detection range 14–85%, upper bound 48.5–77%) appear in citations.md [59] and references/ai-code-quality-tools.md; the complement relationship is arithmetically correct and used consistently.
- **"924 violations"** (Great Expectations PTH): analysis.md says "924 violations across the codebase." citations.md [23] gives the full quote: "276 violations in core code, 924 across full codebase." references/stdlib-preference-rules.md says "924 violations across their codebase." All three state the full-codebase number; the distinction is not hidden or inconsistent — it is a refinement in the citation.
- **MegaLinter "v9.4.0, Feb 2025"**: consistent across analysis.md, references/packaged-tools.md, and citations.md [35].
- **Qlty "v0.625.0, April 24, 2026"**: consistent across analysis.md and references/packaged-tools.md (both cite [36]).
- **sloppylint "v0.5.1, December 2025"**: consistent across analysis.md and references/ai-code-quality-tools.md.
- **PMD CPD "~26 languages"**: consistent across analysis.md and references/clone-detection.md.
- **MegaLinter bundles "jscpd@4.0.8"**: citations.md [12] states this explicitly. analysis.md correctly notes jscpd's standalone latest is v4.0.9 [3], creating a 4.0.8 vs 4.0.9 difference that is not a contradiction — it is the expected version-lag of a bundled dependency. No file claims MegaLinter bundles 4.0.9.
- **"9 existing rules"** in `python/lang/best-practice`: consistent in analysis.md (line 168), references/custom-rule-maintenance.md (lines 19, 67), and citations.md [33].

**Minor note 1 — "51%+" contributor concentration figure**: analysis.md (Dimension 1, caveat 4) states "one contributor accounts for 51%+ of contributions." Citation [4] is the Snyk Advisor jscpd page, which covers general maintenance health but does not explicitly document a "51%+" concentration figure in the extracted data recorded in citations.md [4]. The claim is hedged in analysis.md ("Per agent search of LFX Insights (citation [4] is the closest direct source)"), making clear this is not a directly-fetched figure. No other file repeats or contradicts the 51%+ number. This is a precision-of-attribution note, not a cross-file inconsistency.

---

## Citation issues

### Cited but not defined

None. Every `[N]` reference found across all files corresponds to a defined entry in citations.md. The full citation set spans [1]–[74] with no gaps in the definitions. No inline reference exceeds [74].

### Definitions never cited inline

Two citations are defined in citations.md but do not appear as `[N]` inline references in any content file:

- **[32]** — flake8-use-pathlib (PyPI). Defined in citations.md; not cited inline in any file.
- **[48]** — Ruff adoption stats post (Johal blog). Defined in citations.md; not cited inline in any file.

Per task instructions, unused citations are acceptable. These are noted for completeness, not flagged as errors.

### Cross-citation discrepancies

None found. No citation is used to support contradictory claims across files. Spot-checks of the most substantive citations:

- **[21]** (ruff issue #17699): cited in analysis.md, references/stdlib-preference-rules.md to support the claim that PTH fires unconditionally and produces false positives on file-descriptor and bytes paths. Usage is identical in both files.
- **[59]** (hallucination ceiling paper): cited in analysis.md (twice), README.md (referenced by number in text), and references/ai-code-quality-tools.md. All four usages describe the same empirical finding with consistent framing.
- **[57]** (DeepSource benchmarks critique): cited in analysis.md and references/ai-code-quality-tools.md. Both usages describe Greptile 82% vs Augment 45% on the same 5 repos, with the "37-point swing" characterization. Consistent.
- **[12]** (MegaLinter jscpd descriptor): cited across analysis.md, references/clone-detection.md, and references/packaged-tools.md. All three usages correctly attribute the whole-codebase default behavior and the jscpd-as-sole-COPYPASTE-linter claim.

**Minor note 2 — inline ruff issue #14490 reference without [N] citation**: references/stdlib-preference-rules.md (line 51) mentions "ruff issue #14490 for PTH208" inline without a formal `[N]` citation. PTH208 is also mentioned in [21] (ruff issue #17699). The omission is not a contradiction — #14490 and #17699 are separate issues — but the #14490 reference is uncitable as written. No cross-file conflict results from this.

---

## Verdict / recommendation discrepancies

No discrepancies found.

### Per-dimension verdicts

The TL;DR table in analysis.md, the verdict-per-dimension table in README.md, and the per-dimension "Verdict" sections in references/*.md all agree:

| Dimension | analysis.md TL;DR | README.md verdict | Reference file verdict |
|---|---|---|---|
| 1. Clone detection | Off-the-shelf available — keep jscpd | Off-the-shelf available — keep jscpd | Off-the-shelf available — keep jscpd |
| 2. Stdlib-preference rules | Mixed (1/2/5 novel; 3 partial; 4 substantial overlap different semantic) | Mixed (same breakdown) | Mixed: rule 4 substantive overlap, rule 3 partial, 1/2/5 no equivalent |
| 3. Packaged tools | Partial — MegaLinter/Qlty bundle both, custom layer still needed | Partial — same | Partial — MegaLinter and Qlty bundle both |
| 4. AI-code-quality tools | Partial — sloppylint/KarpeSlop exist, different patterns | Partial — same | Partial — AI-specific tools exist but address adjacent patterns |
| 5. Maintenance burden | Bounded — simple structural rules insulated from churn | Bounded — simple structural rules insulated | Bounded; contribution path feasible but carries relicensing cost |

### Rule-by-rule Effective Cover table

analysis.md and references/stdlib-preference-rules.md both carry a rule-by-rule table. Values are identical:

| Rule | analysis.md | references/stdlib-preference-rules.md |
|---|---|---|
| csv-stdlib | 0 — novel | 0 |
| json-stdlib | 0 — novel | 0 |
| tempfile-stdlib | ~0.3 | ~0.3 |
| pathlib-over-ospath | ~0.7 | ~0.7 |
| argparse-over-sysargv | 0 — novel | 0 |

### Final recommendation

Both analysis.md and README.md recommend option (d) hybrid: keep jscpd and the 5 custom rules, layer ruff for incidental coverage, publish the 5 rules as a Trail of Bits-style external pack. Neither file recommends dropping the custom rules or contributing upstream. The recommendations are consistent.

**Minor note 3 — README omits option (d) label, analysis.md uses it explicitly**: The final recommendation section in analysis.md introduces option (d) as a labeled fourth option and calls it out by name throughout. README.md states the same substance without using the "(d)" label. This is an intentional level-of-detail difference (the README is a summary), not a contradiction.

---

## Logical contradictions

None found. Specific checks performed:

1. **"MegaLinter bundles jscpd@4.0.8" vs "jscpd v4.0.9 is current"**: These coexist without contradiction; they describe two separate version facts (the bundle snapshot vs. the current release). All files that address both state both correctly.

2. **"PTH fires unconditionally" vs "user's rule 4 overlaps with PTH at ~0.7"**: No contradiction. The ~0.7 cover acknowledges the underlying check exists; the semantic-distinction explanation explains why it is not a full replacement. This framing is consistent across analysis.md, references/stdlib-preference-rules.md, and README.md.

3. **sloppylint described as "closest tool to the user's space"** (analysis.md Dim 4) vs **"catches different patterns"**: Both statements are made together in the same paragraph and are not in conflict. The Dim 4 verdict in all files uses the same framing: sloppylint is the closest positioned tool but detects fictional imports rather than the user's "real import but reimplemented" pattern.

4. **Contribution path framing**: analysis.md says "contribution path is feasible but carries a relicensing cost" and recommends the external-pack model. references/custom-rule-maintenance.md says the same. No file says contributing upstream is impossible — they agree it is feasible but not recommended. Consistent.

5. **Greptile "82% catch rate"**: cited as a vendor benchmark in analysis.md, ai-code-quality-tools.md, and citations.md [56]. In all cases it is immediately contextualized by [57] (DeepSource critique). No file presents the 82% figure as authoritative without the counter-evidence. Consistent.

---

## Final assessment

The deliverable is internally consistent across all five files. Key numbers (effective cover values, language counts, version numbers, violation counts, percentage figures) match wherever they appear in more than one place. All 74 citations are defined; every inline `[N]` resolves to a defined entry; two unused definitions ([32], [48]) are present but benign. The per-dimension verdicts, the rule-by-rule Effective Cover table, and the final recommendation (hybrid option d) are stated identically — at different levels of detail — across analysis.md and README.md, with no substantive divergence. Three minor notes are flagged: an unverified "51%+" contributor-concentration figure attributed to a citation that does not directly record it; an inline ruff issue reference (#14490) that lacks a formal `[N]` citation; and the README's omission of the "(d)" label for the hybrid recommendation. None of these constitute contradictions or materially affect the research conclusions.
