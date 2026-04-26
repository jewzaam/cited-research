# Off-the-shelf duplication / anti-reinvention checks for AI-generated code

A citation-backed comparison: is the user's custom dup-check stage (jscpd via npx + 5 custom semgrep rules) reinventing tooling that already exists, or filling a real gap?

Sources are numbered `[N]` against [citations.md](citations.md). Per-dimension detail lives in the [`references/`](references/) directory.

---

## TL;DR

| Dimension | Verdict |
|---|---|
| Dim 1 — Clone detection | **Off-the-shelf available — keep jscpd.** No portable npx-installable replacement has emerged. SonarQube has the only first-class diff-mode but the wrong cost shape. |
| Dim 2 — Stdlib-preference rules | **Mixed.** Rule 4 (pathlib) substantially overlaps with ruff PTH. Rule 3 (tempfile) partially overlaps with bandit S108/B108. Rules 1, 2, 5 (csv, json, argparse) have **no equivalent** in any tool surveyed. |
| Dim 3 — Packaged tools | **Partial — MegaLinter and Qlty bundle clone + lint** in a single CLI, but the lint layer is delegated to Ruff (unconditional FURB/PTH semantics). The user's import-conditional layer is still not replicated. |
| Dim 4 — AI-code-quality tools | **Partial — sloppylint and KarpeSlop exist** but catch *different* AI patterns (hallucinated imports, cross-language leakage). No tool publicly markets "anti-reinvention" detection. |
| Dim 5 — Maintenance burden | **Bounded.** 5 simple structural rules using `pattern-inside` are insulated from semgrep's highest-churn surfaces. Contribution upstream is feasible but carries the Semgrep Rules License v1.0 relicensing cost. |

**Final recommendation: hybrid (option d) — keep jscpd and the 5 custom rules, layer existing linters where they cover ground, and publish the 5 rules as a Trail of Bits-style external pack rather than contributing upstream.** Detail in the [Final recommendation](#final-recommendation) section.

---

## Dimension 1 — Clone detection landscape

Full detail: [`references/clone-detection.md`](references/clone-detection.md).

**Question**: Is jscpd still the right pick for a portable, multi-language, npx-installable check, or has something better emerged?

**Answer**: Yes — keep jscpd. No competitor surfaced for the npx-portable niche in 2024-2026. jscpd v4.0.9 was published mid-April 2026 [3]; it remains MIT-licensed [1] with 150+ language coverage [1] and active development including new MCP server / AI reporter features in the 4.x series [1]. MegaLinter — a major CI lint aggregator — uses jscpd as the sole COPYPASTE-category linter with no announced replacement [12].

**Critical caveats**:

1. **No native diff-only mode.** jscpd issue #254 [2], opened in 2019 requesting commit-diff comparison, was closed without resolution and remains unaddressed in 2026. Diff-scoping requires external `git diff --name-only | xargs` glue or `--pattern` config.

2. **PMD CPD has a documented OOM regression** in releases 7.1.0+ [7] — described in the GitHub issue as making CPD "no longer work on even medium size projects." This effectively rules out PMD CPD as a current alternative for non-trivial projects.

3. **SonarQube has the cleanest diff-mode primitive** [10] (only counts duplications in new/changed code), but its free Community Build does not support branch analysis or PR decoration [40] — those require paid Developer Edition. Per-PR gating with free SonarQube is effectively impossible without third-party plugins.

4. **jscpd has bus-factor risk.** Per agent search snippet of LFX Insights data, one contributor concentration is high (snippet reported 51%+ contributor concentration; specific figure not directly verified in this session — citation [4] is the closest fetched source for jscpd health signals but does not itself state the contributor percentage). Independently of the specific number, jscpd is a single-maintainer-shaped project. This is acceptable while the tool is working but worth tracking — if the maintainer steps back, the user should be ready to fork or migrate.

**Framing-challenge note**: clone detection over the latest commit alone is a weaker signal than over the full repo. A clone may live entirely outside the current diff. The user's per-commit jscpd is a fast first-pass; a periodic full-repo run (e.g., nightly) catches clones the diff misses. This is a scope question, not a tool question.

---

## Dimension 2 — Stdlib-preference / anti-reinvention rule packs

Full detail: [`references/stdlib-preference-rules.md`](references/stdlib-preference-rules.md).

### Rule-by-rule mapping

| User's rule | Closest existing check | Same semantic? | Effective cover |
|---|---|---|---|
| **1. csv-stdlib** (csv-imported + `line.split(",")`) | None found in ruff [19], refurb [27], pylint, semgrep registry [33], Sourcery | N/A | **0 — novel** |
| **2. json-stdlib** (json-imported + manual quote escape) | None found | N/A | **0 — novel** |
| **3. tempfile-stdlib** (tempfile-imported + manual `/tmp/<uuid>`) | ruff S108 (hardcoded-temp-file) [18] / bandit B108 [30] (path-only, NOT import-aware); pylint R1732 (consider-using-with) [28] (lifecycle, not construction) | Different aspect | **~0.3** |
| **4. pathlib-over-ospath** (pathlib-imported + `os.path.X`) | ruff PTH series — PTH118 [16] + ~20 sibling rules [19], all unconditional [21]; FURB101 [17] (autofix adds `import pathlib` per [22]); Sourcery `path-read` [31] | Different semantic — these are migration tools, not consistency checks | **~0.7** |
| **5. argparse-over-sysargv** (argparse/click-imported + `sys.argv[N]`) | None found | N/A | **0 — novel** |

### The architectural distinction

Existing Python linters fall into two camps:

- **Unconditional rules** (ruff PTH, FURB, bandit B108): fire on the bad pattern regardless of context. Migration tools — they push entire codebases onto a preferred API.
- **Import-conditional rules** (the user's, plus a *subset* of refurb): fire only when the relevant import is already present. Consistency tools — they catch the developer who already chose the right API but slipped on one specific call.

Refurb has FURB107, FURB118, FURB134, FURB140, FURB152, FURB180 [27] — six import-conditional rules covering `contextlib.suppress`, `operator`, `functools`, `itertools`, `math`, `ABC`. The architectural capability exists in refurb. **It just isn't directed at csv/json/tempfile/pathlib/argparse-vs-sys.argv.**

### Why the gap exists

Semgrep's `pattern-inside` operator [25] supports the idiom `patterns: [pattern: code, pattern-inside: import X\n...]` for matching code conditional on an import being present elsewhere in the file. This is the architectural primitive the user's rules exploit. Ruff's rules are implemented in Rust source code, not composable YAML — adding import-context to a PTH rule requires changing ruff itself, not authoring a rule.

### Documented downsides of the unconditional approach

- Ruff issue #17699 [21]: PTH rules suggest pathlib equivalents even when pathlib is unsupported (file descriptors, bytes paths). Specific rules cited: PTH208, PTH123.
- Great Expectations [23]: enabling PTH surfaced 924 violations across the codebase — a bulk migration sweep.
- Napari [24]: explicitly disabled PTH because it wasn't compatible with the codebase's style.
- Ruff defaults [19][20]: PTH/FURB/SIM/UP/S are NOT in the default rule set. Teams must explicitly opt in via `extend-select`.

### Verdict

**The user's rules 1, 2, 5 (csv, json, argparse) have no off-the-shelf equivalent.** Rule 3 (tempfile) has a related-but-different rule in S108/B108. Rule 4 (pathlib) substantially overlaps with the ruff PTH series, but at the cost of unconditional-migration noise the user's import-conditional version avoids.

The user's design (`patterns: [pattern, pattern-inside: import X]`) is exactly what semgrep's FP-reduction docs [71] recommend as the canonical noise-reduction strategy. The rules are noise-controlled by construction.

---

## Dimension 3 — All-in-one packaged tools

Full detail: [`references/packaged-tools.md`](references/packaged-tools.md).

**Question**: Is there a tool that bundles clone detection + anti-reinvention lint as a single CLI?

**Answer**: Yes — MegaLinter [34] and Qlty [36] bundle both. But neither replaces the user's custom layer.

- **MegaLinter** [34][12] bundles jscpd (clone) + Ruff with FURB/UP/SIM/PTH (lint) + many more, in a single Docker invocation. License: AGPL v3. Latest release v9.4.0, Feb 2025 [35]. Tradeoff: heavyweight Docker image runs everything whole-codebase.
- **Qlty** [36] bundles Tree-Sitter AST clone detection + Ruff/Pylint/Flake8/Bandit/Black/Mypy. Single Rust CLI, BSL 1.1 license, free for commercial. Latest v0.625.0, April 24, 2026.
- **SonarQube** [38] has CPD for Python [13][39] and 500+ Python rules. Per-PR gating in the free Community Build is constrained — branch analysis and PR decoration are paid features (limitation independently established from SonarQube docs; specific support thread [40] cited in the original draft does not itself confirm this — see audit). Documented as slow (community thread [46] reports an 8-min-vs-1-min regression after a 2025.3.1 upgrade — wider 5-20 min range came from agent search snippets and is unverified). Developer frustration with noise is publicly visible [47]. SAST mindshare reportedly declining year-over-year per agent counter-discovery search (Konvu/PeerSpot snippet, not directly fetched).
- **GitLab is institutionalizing the compose-it-yourself pattern**: GitLab deprecated its CodeClimate-based Code Quality (which included duplication detection) [43] with removal scheduled for GitLab 19.0 (May 2026). Replacement guidance: integrate own tools (Ruff, Flake8, Pylint, Bandit) directly in CI [43][44].

**The bundle that bundles your stack still doesn't bundle your layer.** Both MegaLinter and Qlty delegate the lint work to Ruff with its unconditional PTH/FURB semantics. None of them carry import-conditional anti-reinvention rules. The user can adopt MegaLinter as a wrapper if they want a one-tool runtime, but the custom semgrep layer still does work no off-the-shelf bundle does.

---

## Dimension 4 — AI-code-quality-specific tools

Full detail: [`references/ai-code-quality-tools.md`](references/ai-code-quality-tools.md).

**Question**: Has anyone published a quality gate specifically targeting LLM-generated code reinvention patterns?

**Answer**: Yes for AI-specific patterns generally. No for "imported X but reimplementing X" specifically.

The market has split into two recognizable categories in 2024-2026:

**Category A: AI-specific lint-style tools** (substantive but niche)

- **sloppylint** [50] — Python only, MIT, v0.5.1 (Dec 2025). Detects hallucinated imports, cross-language leakage (`.push()`/`.equals()` in Python), placeholder code, bare except. The closest tool to the user's space — but catches **different** patterns.
- **KarpeSlop** [49] — TypeScript/JavaScript/React/Next.js only (NOT Python). MIT. Andrej Karpathy "AI Slop Index" framing.
- **AI-SLOP-Detector** [51] — Python, structural-hollowness focus.
- **GPTLint** [52] — LLM-assisted, generic. Activity stalled (last commit July 2024).

**Category B: AI code review platforms** (substantive, broader scope)

- **CodeRabbit** [53], **Cursor BugBot** [62], **Greptile** [56], **Korbit** [63], **DiffRay** [64], **Snyk AI** [61]. None positioned specifically around "anti-reinvention." CodeRabbit is explicitly described as a generic code reviewer [53], not AI-specific. Greptile's codebase-aware architecture could in principle detect "this duplicates `utils/parse_csv.py`" but no public benchmark confirms it as a primary use case.

**Academic frame**:

- **CodeHalu (AAAI 2025)** [54] defines 4 hallucination categories (Mapping / Naming / Resource / Logic). The user's "reinvention" pattern doesn't fit cleanly.
- **Zhang et al. 2025** [55] proposes **Project Context Conflicts** as a separate category — the LLM not knowing what already exists in the repo. This is the **closest academic match for "reinvention."** But it's research framework, not a tool.
- **Static analysis hallucination ceiling paper (April 2026)** [59]: 23-52% of library hallucinations are **structurally undetectable** by static analysis regardless of rule quality. This is a hard limit on the user's semgrep-based approach — and on every linter.

**Practitioner field guide**: "Lint Against the Machine" (March 6, 2026) [60] explicitly maps AI anti-patterns to existing ruff/eslint rules where possible, and acknowledges patterns without rules (debugging residue, over-engineering, test-validation issues). The article supports the user's framing — existing linters cover some AI anti-patterns; the user's specific "imported X but reimplementing X" pattern is in the gap that needs custom rules.

**Counter-evidence on tool credibility**: DeepSource [57] is the most damning analysis — same 5 OSS repos that Greptile claimed 82% catch rate on, Augment scored 45%. Methodology produces 37-point swings. Conclusion: "Self-evaluation is biased, even in good faith. None of this [independent benchmarks] exists for AI code review yet."

**Framing-challenge note** (Phase 0): The patterns the user catches (manual CSV split, manual JSON build, /tmp/ paths) are old human anti-patterns. They long predate LLMs. The fact that they show up in AI-generated code isn't because AI invented these patterns — it's because AI was trained on humans who wrote them. The "AI code quality" framing doesn't change what should be detected; it changes how often you should run the detection (every commit, because AI commits are constant) and what you should be tolerant of (less, because AI doesn't learn from your team's review comments).

---

## Dimension 5 — Custom rule-pack maintenance burden

Full detail: [`references/custom-rule-maintenance.md`](references/custom-rule-maintenance.md).

**Question**: Are 5 custom semgrep rules cheap to maintain, and is contributing them upstream worth the effort?

**Answer**: Yes, low maintenance for simple structural rules. Contribution path is feasible but carries a relicensing cost; the Trail of Bits external-pack model is the better fit.

### Maintenance burden

The user's 5 rules use `pattern`, `pattern-either`, `pattern-inside` — all stable structural operators. None use:

- Taint mode (which broke in CE Dec 2024 [65][66])
- Cross-function/inter-procedural reasoning (commercial-only since Dec 2024)
- Broad `...` ellipsis matching (known performance ceiling per agent counter-discovery)
- Experimental rule-syntax features [73] (gradual migration, no forced cutover)

**The user's rules are insulated from the highest-churn surfaces of semgrep.** Plus, the import-conditional gating (`pattern-inside: import X\n...`) is the canonical FP-reduction strategy semgrep itself recommends [71].

The Opengrep fork [72] (January 2025) is rule-format-compatible with Semgrep — the user's rules would run unchanged on Opengrep if Semgrep CE continues regressing. (Windows support was on the launch-post roadmap rather than shipped at launch; current Windows status is unverified in this session.) Either way, the rule-format compatibility provides a usable escape hatch.

### Contribution paths

| Path | Pros | Cons |
|---|---|---|
| Contribute to `semgrep/semgrep-rules` upstream | Maximum visibility; rules ship with `--config p/python` defaults; tested-against-Semgrep-CI; only 3 metadata fields needed for best-practice category [67] | CLA required [67]; rules become subject to Semgrep Rules License v1.0 (no commercial reuse outside Semgrep) [65]; user grants permanent relicensing rights |
| External pack (Trail of Bits model) [68] | Keep ownership; choose own license (ToB uses AGPLv3); request registry indexing for `--config p/yourname` access; no CLA | Lower visibility than rules in the main repo; need to maintain own GitHub repo |
| Keep as-is (private rules in user's stagehand templates) | Zero public surface; full control | No community sharing; user is sole maintainer |

**The 5 rules would be net-additive to `python/lang/best-practice/`** — the existing 9 rules in that directory [33] (hardcoded-tmp-path, logging-error-without-handling, manual-collections-create, missing-hash-with-eq, open-never-closed, pass-body, pdb, sleep, unspecified-open-encoding) include zero overlap with the user's csv/json/tempfile/pathlib/argparse patterns.

### Maintenance burden in practice

For a 5-rule pack of simple structural patterns:
- Re-test on each Semgrep release: minutes (just `semgrep --test` against the existing test files).
- Adjust patterns when codebase evolves: occasional, low frequency.
- Migrate to syntax 2.0 if/when Semgrep deprecates 1.0: low cost — patterns map cleanly.

This is "pay an hour every 6-12 months" maintenance, not "a permanent project."

---

## Final recommendation

The user's prompt offered three options:
- (a) drop the custom rules and adopt an existing tool
- (b) keep them but contribute upstream
- (c) keep as-is because the niche is genuinely unfilled

The framing challenge from Phase 0 surfaced a fourth: **(d) hybrid — keep what fills a real gap, layer existing tools where they cover ground, distribute the gap-filling rules in a way that doesn't relicense them**.

**Recommended: option (d).** Concretely:

### Keep
- **jscpd via npx** for clone detection [1]. Still the right pick for the npx-portable niche. Add an external `git diff --name-only | xargs --pattern` wrapper for diff-only scoping (jscpd has no native diff flag [2]).
- **The 5 custom semgrep rules**, exactly as-is. Three of them (csv, json, argparse) have no equivalent in any tool surveyed [19][27][33]. Two (tempfile, pathlib) have only partially-overlapping rules in ruff and bandit, with different semantic (unconditional migration sweep vs. import-conditional consistency check) and well-documented noise problems [21][23][24].

### Layer
- **Add `ruff --select PTH,FURB,SIM,UP,S` to the gate** if not already present, and accept the bulk-migration noise as a separate signal from the consistency-check signal the user's rules produce. Ruff PTH covers ground rule 4 partially; ruff FURB covers some adjacent reimplementation patterns the user doesn't have rules for; ruff S108 [18] is a useful complement to rule 3.
- **Consider sloppylint** [50] as an additional Python-specific AI-code-quality layer. It catches different patterns (hallucinated imports, cross-language leakage) that the user's rules don't. MIT-licensed, recently published.

### Publish
- **Distribute the 5 custom rules as a Trail of Bits-style external pack** [68]. Own GitHub repo, own license (Apache 2.0 to match the user's stated standard), request indexing in the Semgrep registry for `--config p/yourname` access. This avoids the Semgrep Rules License v1.0 relicensing [65] that contributing to `semgrep/semgrep-rules` upstream would impose, while still making the rules publicly available.

### Don't
- **Don't adopt MegaLinter or Qlty as a replacement.** They bundle clone + lint, but the lint layer is delegated to Ruff with the same unconditional PTH/FURB semantics — they don't replace the user's custom rules. They might be worth adopting as a runtime *wrapper* if the user wants one-Docker-image invocation, but that's an orthogonal decision to keeping the custom rules.
- **Don't position the dup-check stage as "AI-specific."** The patterns the user's rules detect (manual CSV split, manual JSON build, manual /tmp/ paths) are old human anti-patterns. The "AI code review" framing is useful for *frequency* (run on every AI commit) and *tolerance* (don't let AI accumulate them) but doesn't change what should be detected. The user's 5 rules would benefit a human-only Python codebase exactly the same.

### What about "drop the custom rules entirely, use ruff alone"?
This is a defensible alternative if the user is willing to accept ruff's bulk-migration noise as the cost of dropping a maintenance burden. Concretely: enable ruff PTH (rule 4 partial coverage), ruff S108 (rule 3 partial coverage), and accept that rules 1, 2, 5 (csv, json, argparse) go uncovered. The trade-off is precision vs. simplicity. The recommendation above (option d) keeps the custom rules because (a) three of them have no equivalent at all, and (b) maintenance cost is low for simple structural patterns. If the user wants the simplest possible setup and is comfortable with three uncovered patterns, "ruff alone" is a real option — just not the optimal one.

### Diff-scope nuance
- **Diff-only scoping is the right default for the reinvention rules** — semgrep on changed files catches new violations cheaply.
- **Diff-only scoping is a weaker signal for clone detection** — clones span files, and a copy may live entirely outside the current diff. Run jscpd diff-scoped on every commit AND full-repo on a periodic schedule (e.g., nightly or weekly). This is a config change, not a tool change.

---

## What the user is reinventing (and what they're not)

| User's component | Reinventing something? |
|---|---|
| jscpd-via-npx for clone detection | No. Still the dominant choice; no credible replacement. |
| pathlib-over-ospath rule | Partial. Ruff PTH covers similar ground unconditionally — different semantic, with documented noise. The user's import-conditional version is a higher-precision design. |
| tempfile-stdlib rule | Partial. Bandit S108 covers `/tmp` literals; the user's version adds import-context and uuid-construction detection. |
| csv-stdlib, json-stdlib, argparse-over-sysargv | No. Genuinely unfilled niche. |
| Maintaining 5 simple structural rules | No. Bounded maintenance, insulated from semgrep's churn surfaces. |

**The user's specific niche (Python stdlib-preference rules with import-conditional gating) is genuinely unfilled by off-the-shelf tooling as of 2026-04.** The recommendation is to keep what works, add ruff for incidental coverage, and publish the gap-filling rules so other agentic-development teams can use them.

---

## Confidence and limitations

**Where the recommendation is most confident:**

- jscpd is the right clone detection choice for the npx-portable niche (multiple independent confirmations).
- Rules 1, 2, 5 have no off-the-shelf equivalent (exhaustive search across ruff, refurb, pylint, semgrep registry, Sourcery).
- Ruff PTH fires unconditionally and is not a drop-in replacement for the user's rule 4 (directly verified from ruff issue #17699 and ruff rule docs).
- 5 simple structural rules are low-maintenance (insulated from semgrep's high-churn surfaces).

**Where the recommendation is least confident:**

- DeepSource clone-detection feature status is unclear (roadmap URL redirects).
- Whether sloppylint's hallucinated-import detection is reliable in practice is unverified.
- Vendor-published benchmarks (Greptile, DiffRay) lack independent verification per [57].
- MegaLinter activity past Feb 2025 is not directly confirmed in this session.
- Some claims rely on agent search-snippet evidence rather than direct WebFetch (sources marked "not directly fetched" in [citations.md](citations.md)).

**Hard limit acknowledged**: The April 2026 hallucination-ceiling paper [59] establishes that 23-52% of library hallucinations are structurally undetectable by static analysis. The user's rules — like all linters — operate within this ceiling. They catch a subset of reinvention; some patterns will always require human review or AI-augmented review. This is not a critique of the user's design; it's a property of the problem space.
