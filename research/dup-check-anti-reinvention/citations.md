# Citations

Sources for [analysis.md](analysis.md) and the per-dimension reference files. Numbered sequentially. Each entry records the exact data extracted and any access concerns. Sources flagged INACCESSIBLE could not be fetched in-session and rely on agent search-snippet evidence — treat their claims as lower confidence.

---

## Dimension 1 — Clone detection landscape

**[1]** jscpd repository — https://github.com/kucherenko/jscpd
- License: MIT.
- Languages: "more than 150 programming languages and digital formats of documents."
- Algorithm: Rabin-Karp.
- README does NOT mention a `--diff` flag or built-in changed-files mode.
- Tier 2 (official project repo).

**[2]** jscpd issue #254 (diff/commit comparison feature request) — https://github.com/kucherenko/jscpd/issues/254
- Opened 2019-07-29. Closed without documented resolution. No maintainer response visible.
- Confirms jscpd does not have a built-in diff-only mode as of 2026-04-26.
- Tier 2.

**[3]** jscpd on npm — https://www.npmjs.com/package/jscpd
- INACCESSIBLE (HTTP 403 during in-session fetch).
- Per agents' search snippets: latest version 4.0.9 published mid-April 2026; weekly downloads in the 344k–703k range.
- Tier 2 (registry page); claims unverified by direct fetch this session.

**[4]** Snyk Advisor — jscpd — https://snyk.io/advisor/npm-package/jscpd
- Per agent search snippet: maintenance rated "Healthy"; at least one release in past 3 months as of 2026-04.
- Tier 3 (third-party health rating); not directly fetched.

**[5]** PMD CPD official documentation — https://pmd.github.io/pmd/pmd_userdocs_cpd.html
- Languages enumerated: Java, JSP, C/C++, C#, Go, Kotlin, Ruby, Swift, Apex, HTML, Dart, Fortran, Gherkin, JavaScript, Lua, Matlab, Modelica, Objective-C, Perl, PHP, PL/SQL, Python, Scala, T-SQL, Velocity Template Language, XML dialects (~26 languages).
- Output formats: text (default), xml, csv, csv_with_linecount_per_file, vs, markdown. (Audit note: original draft included "xslt" — not in fetched docs; removed.)
- Runtime: JVM. Memory tunable via `PMD_JAVA_OPTS`.
- Exit codes: status 4 (since 5.0) or 5 (since 7.3.0) on duplicates found, unless `--no-fail-on-violation`.
- Documentation does NOT mention diff-only or changed-files-only flag.
- Tier 2.

**[6]** PMD release page — https://github.com/pmd/pmd/releases/tag/pmd_releases/7.22.0
- Per agent search snippet: PMD 7.22.0 released 27-February-2026.
- Tier 2 (official release page); date claim from search snippet, not directly fetched.

**[7]** PMD issue #5066 (CPD OOM regression) — https://github.com/pmd/pmd/issues/5066
- Per agent counter-discovery: documents `java.lang.OutOfMemoryError: Java heap space` on medium-size projects starting CPD release 7.1.0+, described as "no longer work[ing] on even medium size projects."
- Tier 2 (project issue tracker); claim from agent search snippet.

**[8]** Simian official site — https://simian.quandarypeak.com/
- Per agent counter-discovery: site states Simian was open-sourced under Apache 2.0 by Quandary Peak Research (date of transition unconfirmed).
- Tier 2 (official site); claim from agent search snippet, exact transition date not verified.

**[9]** SonarQube duplication exclusion docs — https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/analysis-functions/analysis-scope/exclude-from-coverage-duplication
- Per audit correction: this page documents EXCLUDING files from duplication analysis via path patterns, NOT configuring CPD token/line thresholds. (Threshold configuration belongs to source [39].) The original draft mischaracterized this page.
- Tier 2.

**[10]** SonarQube quality gates docs — https://docs.sonarsource.com/sonarqube-server/2025.5/quality-standards-administration/managing-quality-gates/introduction-to-quality-gates
- Per agent discovery: SonarQube has a native "new code" concept — quality gates apply duplication conditions only to new/changed lines relative to target branch. "Fudge factor" ignores duplication on PRs adding fewer than 20 new lines.
- Tier 2.

**[11]** SonarLint duplication community thread — https://community.sonarsource.com/t/does-sonarlint-supports-duplicate-code-check-in-ide/112257
- Per agent discovery: confirms duplication detection is server-side only in SonarLint — IDE plugin does not detect duplicates standalone.
- Tier 3 (community forum, often citing official source).

**[12]** MegaLinter jscpd descriptor — https://megalinter.io/latest/descriptors/copypaste_jscpd/
- jscpd is the COPYPASTE category linter. Verbatim: "If this linter is active, all files will always be linted." `VALIDATE_ALL_CODEBASE: false` does not restrict jscpd to changed files only.
- Bundles jscpd@4.0.8 in the MegaLinter Docker image.
- Tier 2 (official project docs).

**[13]** SonarQube Python language docs — https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/python
- Confirmed: "Analysis does not measure code duplication at this time" applies ONLY to Jupyter Notebooks, NOT to standard `.py` files.
- Could NOT confirm via this fetch: total Python rule count, edition gating of CPD, anti-reinvention rule presence.
- Tier 2.

**[14]** Pylint R0801 (duplicate-code) docs — https://pylint.readthedocs.io/en/stable/user_guide/messages/refactor/duplicate-code.html
- Per agent discovery: `min-similarity-lines` option tunes sensitivity. Cannot be disabled per-file via inline comments. No native diff-only flag.
- Tier 2.

**[15]** ACM 2025 evaluation paper on clone detection — https://dl.acm.org/doi/10.1145/3723178.3723206
- Per agent counter-discovery: 2025 academic comparative evaluation. Field's intellectual momentum is shifting toward LLM/ML-based clone detection; productized tools have not yet emerged.
- Tier 1 (peer-reviewed); not directly fetched.

---

## Dimension 2 — Stdlib-preference / anti-reinvention rule packs

**[16]** ruff PTH118 (os-path-join) docs — https://docs.astral.sh/ruff/rules/os-path-join/
- Verbatim "what it does": "Checks for uses of `os.path.join`."
- Fires UNCONDITIONALLY — does NOT require `pathlib` to be imported in the same file.
- Tier 2.

**[17]** ruff FURB101 (read-whole-file) docs — https://docs.astral.sh/ruff/rules/read-whole-file/
- Verbatim: "Checks for uses of `open` and `read` that can be replaced by `pathlib` methods, like `Path.read_text` and `Path.read_bytes`."
- Documentation does not require pathlib to already be imported. Autofix exists.
- Tier 2.

**[18]** ruff S108 (hardcoded-temp-file) docs — https://docs.astral.sh/ruff/rules/hardcoded-temp-file/
- Verbatim: "Checks for the use of hardcoded temporary file or directory paths."
- Path-based, not import-based. Does NOT require `tempfile` import.
- Configurable via `hardcoded-tmp-directory` and `hardcoded-tmp-directory-extend`.
- Tier 2.

**[19]** ruff rules index — https://docs.astral.sh/ruff/rules/
- Lists ~47 major rule category groups (audit corrected from "50+"). Default rule set: F (Pyflakes) + subset of E (pycodestyle errors).
- PTH, FURB, S, SIM, UP, PERF are NOT enabled by default. Require explicit opt-in via `select` or `extend-select`.
- Tier 2.

**[20]** ruff linter docs — https://docs.astral.sh/ruff/linter/
- Recommended example shown: `["E", "F", "UP", "B", "SIM", "I"]` — described as "popular" guidance (not defaults).
- Tier 2.

**[21]** ruff issue #17699 (PTH false positives) — https://github.com/astral-sh/ruff/issues/17699
- Title: "PTH*: Incorrect suggestion to use Pathlib when using file descriptors."
- Verbatim: "pathlib rules recommend the use of `pathlib.Path` over their `os` equivalent even when they're used with a bytes string or directory descriptor which aren't supported by pathlib."
- Specific rules: PTH208, PTH123. Confirms PTH rules do not check import context, type context, or parameter context before firing.
- Tier 2.

**[22]** ruff issue #21274 (FURB101 autofix adds import) — https://github.com/astral-sh/ruff/issues/21274
- Per agent discovery: confirms FURB101's intended autofix INSERTS `import pathlib` — meaning FURB101 fires on files that do not yet use pathlib. Migration semantic, not consistency semantic.
- Tier 2; not directly fetched.

**[23]** Great Expectations PTH adoption PR #7290 — https://github.com/great-expectations/great_expectations/pull/7290
- Per agent counter-discovery: enabling PTH rules surfaced 276 violations in core code, 924 across full codebase.
- Confirms PTH does a bulk migration sweep, not import-conditioned consistency check.
- Tier 3 (project-internal PR).

**[24]** napari PTH disable issue #5589 — https://github.com/napari/napari/issues/5589
- Per agent counter-discovery: napari decided NOT to enable PTH rules because "changes may be controversial" and they are "not compatible with the current codebase."
- Tier 3.

**[25]** semgrep rule syntax docs — https://semgrep.dev/docs/writing-rules/rule-syntax
- Confirms `pattern-inside` ("Keep findings that lie inside this pattern"), `pattern-not-inside`, and `patterns` (logical AND) operators.
- The `patterns: [pattern: X, pattern-inside: import Y\n...]` idiom IS used in practice for import-conditional rules — this is exactly the pattern the user's rules employ.
- Tier 2.

**[26]** semgrep "match the absence" KB — https://semgrep.dev/docs/kb/rules/match-absence
- Per agent counter-discovery: documents `pattern-not-regex` and negative pattern operators for detecting absence/presence of statements elsewhere in file.
- Tier 2.

**[27]** refurb checks documentation — https://github.com/dosisod/refurb/blob/master/docs/checks.md
- 192 FURB rules total (FURB100-FURB192).
- IMPORT-CONDITIONAL rules confirmed: FURB107 (use-with-suppress, on `contextlib.suppress`), FURB118 (use-operator, on `operator` import), FURB134 (use-cache, on `functools` import), FURB140 (use-starmap, on `itertools` import), FURB152 (use-math-constant, on `math` import), FURB180 (use-abc-shorthand, on `ABC` or `ABCMeta`).
- NO FURB rule covers csv/json/argparse/tempfile/pathlib in the user's specific "imported X but reimplementing X" pattern.
- Tier 2.

**[28]** pylint R1732 (consider-using-with) docs — https://pylint.pycqa.org/en/latest/user_guide/messages/refactor/consider-using-with.html
- Per agent discovery: fires when `tempfile.TemporaryDirectory()` or `tempfile.NamedTemporaryFile()` are assigned without a `with` block. Lifecycle concern, not construction-path concern. Partial overlap with the user's tempfile rule (different aspect).
- Tier 2; not directly fetched.

**[29]** pylint W0611 (unused-import) — https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/unused-import.html
- Per agent counter-discovery: detects when an import is literally never referenced. Does NOT cross-correlate with the "imported but reimplemented" pattern (which involves the import being used legitimately elsewhere while one specific call is hand-rolled).
- Tier 2; not directly fetched.

**[30]** bandit B108 (hardcoded_tmp_directory) — https://bandit.readthedocs.io/en/latest/plugins/b108_hardcoded_tmp_directory.html
- Per agent discovery: detects `/tmp`, `/var/tmp`, `/dev/shm` as hardcoded temp paths. Same pattern as ruff S108 (which is derived from B108).
- Tier 2; not directly fetched.

**[31]** Sourcery `path-read` rule — https://docs.sourcery.ai/References/Sourcery-Rules/Python/Default-Rules/path-read/
- Per agent discovery: refactors `with open(f) as fh: contents = fh.read()` → `Path(f).read_text()`. Adjacent to FURB101.
- Tier 2; not directly fetched.

**[32]** flake8-use-pathlib PyPI — https://pypi.org/project/flake8-use-pathlib/
- Per agent discovery: upstream source of all PTH rules in ruff. Covers PTH100-PTH211.
- Tier 2; not directly fetched.

**[33]** semgrep python/lang/best-practice tree — https://github.com/semgrep/semgrep-rules/tree/develop/python/lang/best-practice
- Directory contents (9 files): hardcoded-tmp-path, logging-error-without-handling, manual-collections-create, missing-hash-with-eq, open-never-closed, pass-body, pdb, sleep, unspecified-open-encoding.
- NONE match the user's "imported X but reimplementing X" pattern for csv/json/tempfile/pathlib/argparse.
- Tier 2.

---

## Dimension 3 — All-in-one packaged tools

**[34]** MegaLinter homepage — https://megalinter.io/latest/
- Bundles 69 programming languages, 23 formats, and 21 tooling formats (audit corrected — original draft said "50+ languages"). Bundles jscpd (clone detection) + Ruff (lint with FURB/UP/SIM/PTH stdlib-preference rules) + many more in single Docker/CLI invocation.
- License: AGPL v3.
- Tier 2.

**[35]** MegaLinter releases — https://github.com/oxsecurity/megalinter/releases
- Per agent discovery: latest v9.4.0, February 28, 2025. (Subsequent releases unconfirmed in this session.)
- Tier 2.

**[36]** Qlty repo — https://github.com/qltysh/qlty
- Verbatim: "a multi-language code quality tool for linting, auto-formatting, maintainability, and security with support for 70+ static analysis tools for 40+ languages and technologies."
- License: Business Source License 1.1 with Delayed Open Source Publication. Free for commercial use.
- Bundles Tree-Sitter-based AST clone detection + Ruff/Flake8/Pylint/Mypy/Bandit/Black for Python.
- Latest release: v0.625.0, April 24, 2026.
- "CodeClimate successor" status NOT confirmed in this fetch.
- Tier 2.

**[37]** Qlty duplication docs — https://docs.qlty.sh/duplication
- Per agent discovery: Tree-Sitter-based detection with variable name normalization. Python supported.
- Tier 2; not directly fetched.

**[38]** SonarQube Server Python docs (versioned) — https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/languages/python
- Per agent discovery: 500+ Python rules covering bugs, security, code smells. Frameworks: Django, Flask, FastAPI, Pandas, NumPy. Python 2.7 and 3.0–3.13.
- Tier 2; not directly fetched.

**[39]** SonarQube CPD on Python community thread — https://community.sonarsource.com/t/detecting-code-duplications-within-the-same-python-file-in-sonarqube/140038
- Per agent discovery: CPD works on Python `.py` files. Token-based with `sonar.cpd.py.minimumTokens` and `sonar.cpd.py.minimumLines` configuration. No edition gate found on this feature.
- Tier 3.

**[40]** SonarQube Community Build limitations community thread — https://community.sonarsource.com/t/sonarqube-community-edition-limitations/63448
- Per agent counter-discovery: Community Build (formerly Community Edition, renamed late 2024) is described as having narrower features than paid editions.
- Audit caveat: the cited forum thread does NOT contain the specific limitations originally attributed to it ("main branch only", "no PR decoration without paid Developer Edition"). Those limitations are independently well-established from SonarQube's own documentation (and from related thread [PR decoration should not require Developer Edition](https://community.sonarsource.com/t/pull-request-decoration-should-not-require-the-developer-edition/2696) per agent discovery), but [40] alone is not the primary source.
- Tier 3 — use as supplementary signal only.

**[41]** Qodana Clone Finder docs — https://www.jetbrains.com/help/qodana/about-clone-finder.html
- Per agent discovery: Clone Finder is a separate Qodana product. EAP since 2021. Currently absent from the Qodana 2026.1 Python feature table — current GA status uncertain.
- Tier 2; not directly fetched.

**[42]** Qodana Python docs — https://www.jetbrains.com/help/qodana/python.html
- Per agent discovery: based on PyCharm Professional inspections. Includes structural search, security analysis (OWASP Top 10), vulnerability checker.
- Tier 2; not directly fetched.

**[43]** GitLab Code Quality CodeClimate scanning docs (deprecation) — https://docs.gitlab.com/ci/testing/code_quality_codeclimate_scanning/
- Per agent discovery: CodeClimate-based template (which included duplication detection) is DEPRECATED as of GitLab 17.3. Planned removal in GitLab 19.0 (May 2026).
- Replacement guidance: integrate own tools (Ruff, Flake8, Pylint, Bandit) directly in CI and emit Code Quality artifacts.
- Tier 2; not directly fetched.

**[44]** Aaron Goldenthal "Goodbye CodeClimate" post — https://aarongoldenthal.com/posts/a-better-gitlab-code-quality---part-1--goodbye-codeclimate/
- Per agent counter-discovery: practitioner post on the GitLab CodeClimate deprecation and the move toward composable tooling.
- Tier 3.

**[45]** Sourcery clone detection changelog — https://sourcery.ai/changelog/clone-detection
- Per agent discovery: clone detection is a paid (Sourcery Pro) and IDE-only (VS Code) feature. NOT in the free CLI tier.
- Tier 2; not directly fetched.

**[46]** SonarQube slow analysis community thread — https://community.sonarsource.com/t/sonar-analysis-extremely-slow-with-version2025-3-1/147167
- Per agent counter-discovery: 8-minute scans where 1 minute was expected after upgrading to v2025.3.1.
- Tier 3.

**[47]** "Sonar is destroying my job" community thread — https://community.sonarsource.com/t/sonar-is-destroying-my-job-and-its-driving-me-to-despair/92438
- Per agent counter-discovery: July 2024. Substantial public documentation of developer frustration with SonarQube noise.
- Tier 3.

**[48]** Ruff adoption stats post — https://www.johal.in/ruff-linting-rules-python-black-flake8-alternatives-configuration-2025/
- Per agent counter-discovery: 65% GitHub repo adoption by Q1 2025 (cited as GitHub Octoverse), 300% PyPI download surge in 2025.
- Tier 3 (third-party blog citing primary stats); primary source not independently verified.

---

## Dimension 4 — AI-code-quality-specific tools

**[49]** KarpeSlop repo — https://github.com/CodeDeficient/KarpeSlop
- Detects three "AI Slop Index" categories: Information Utility (Noise), Information Quality (Lies — including hallucinated imports), Style/Taste (Soul). Inspired by Andrej Karpathy framing.
- Languages: TypeScript, JavaScript, React, Next.js. **Python NOT supported.**
- License: MIT. 30 stars; activity level unclear.
- Tier 2.

**[50]** sloppylint repo — https://github.com/rsionnach/sloppylint
- Python-only. Four categories: Noise, Lies, Soul, Structure.
- Detects hallucinated imports (non-existent packages), cross-language leakage (.push() / .equals() / .each in Python), placeholder code, bare except.
- Verbatim: "LLMs leak patterns from other languages they were trained on — sloppylint catches 100+ of these."
- Latest release: v0.5.1, December 21, 2025. License: MIT.
- Tier 2.

**[51]** AI-SLOP-Detector repo — https://github.com/flamehaven01/AI-SLOP-Detector
- Per agent discovery: 4D scoring system with self-calibration loop (v3.5.0). Detects unimplemented stubs, disconnected pipelines, phantom imports, placeholder-heavy production paths, "jargon inflation."
- Tier 2; not directly fetched.

**[52]** GPTLint repo — https://github.com/gptlint/gptlint
- Per agent discovery: LLM-assisted lint with two-pass approach (weak model generates, strong model filters). Custom rules in Markdown.
- Caveat: last commit July 2024 — activity stalled. Open source (MIT).
- Tier 2; not directly fetched.

**[53]** CodeRabbit ast-grep + LLM blog — https://www.coderabbit.ai/blog/ai-native-universal-linter-ast-grep-llm
- Approach: ast-grep extracts deterministic patterns → fed to LLM as RAG context.
- IMPORTANT: positioned as a "generic code quality tool", NOT specifically targeting AI-generated code patterns. CodeRabbit is general-purpose.
- Tier 2.

**[54]** CodeHalu paper (AAAI 2025) — https://arxiv.org/abs/2405.00253
- Defines four code-hallucination categories: Mapping, Naming, Resource, Logic.
- Benchmark: CodeHaluEval (8,883 samples, 699 tasks). 17 LLMs evaluated.
- "Reinvention" pattern doesn't fit cleanly into these four — Resource is closest but the taxonomy lacks a "project context" axis.
- Tier 1 (peer-reviewed AAAI 2025).

**[55]** Zhang et al. 2025 — https://arxiv.org/abs/2409.20550
- Per agent counter-discovery: paper classifies LLM code hallucinations into a multi-category taxonomy. Three categories cited in the original draft: Task Requirement Conflicts, Factual Knowledge Conflicts, and **Project Context Conflicts** (model not knowing what already exists in the repo).
- Audit caveat: arxiv abstract confirms the paper is about LLM hallucinations in code generation and mentions "complex contextual dependencies" but does not enumerate the three category names at the abstract level. The specific three-category taxonomy and the term "Project Context Conflicts" derive from the full paper body, not the abstract — unverified at abstract level in this session.
- Tier 1 (peer-reviewed); abstract-only verification.

**[56]** Greptile benchmarks — https://www.greptile.com/benchmarks
- Per agent counter-discovery: Greptile's own benchmark — 82% catch rate on 50 real bugs across 5 OSS repos (July 2025). Codebase-aware review architecture.
- Tier 3 (vendor-published benchmark; see [57] for independent critique).

**[57]** DeepSource AI code review benchmarks critique — https://deepsource.com/blog/ai-code-review-benchmarks
- Per agent counter-discovery: same 5 repos that Greptile scored 82% on, Augment scored 45%. 37-point methodology swing.
- Verbatim conclusion: "Self-evaluation is biased, even in good faith. None of this [independent datasets, reproducible methodology] exists for AI code review yet."
- Tier 3 (vendor blog), but provides important counter-evidence.

**[58]** Cloudflare AI code review post — https://blog.cloudflare.com/ai-code-review/
- Multi-agent AI review system: up to 7 specialized reviewers + a coordinator agent. 131,246 review runs across 48,095 merge requests in 5,169 repositories in a single month. 0.6% developer override rate. Blocks merges on critical findings.
- (Earlier draft cited a "93% adoption in one year" figure which does not appear in the cited source — corrected after audit.)
- Tier 2 (production deployment post).

**[59]** Static analysis hallucination ceiling paper — https://arxiv.org/abs/2604.07755
- Per agent counter-discovery: April 2026 empirical study. Static analysis detects 14–85% of library-use hallucinations across benchmarks. Manual analysis sets upper bound at 48.5–77% — meaning 23–52% of library hallucinations are structurally undetectable by static analysis regardless of rule quality.
- Tier 1; not directly fetched.

**[60]** "Lint Against the Machine" Medium article — https://medium.com/@montes.makes/lint-against-the-machine-a-field-guide-to-catching-ai-coding-agent-anti-patterns-3c4ef7baeb9e
- Date: March 6, 2026.
- Catalogs 10 AI anti-pattern categories. References existing rules (Ruff TID251 / BLE001 / E722 / ASYNC100-102 / UP / I / N; ESLint @typescript-eslint/no-explicit-any). (Audit note: Pyright strict mode was in original draft but not confirmed in fetched content — removed.)
- Acknowledges anti-patterns WITHOUT standard rules: debugging residue, over-engineering, test validation issues.
- Tier 3 (practitioner blog).

**[61]** Snyk AI-generated code blog — https://snyk.io/blog/snyk-code-secures-ai-builds/
- Per agent discovery: taint analysis treating any data returned from OpenAI/Anthropic/HuggingFace/Google LLM libraries as untrusted regardless of hardcoded prompt. Tracks data flows for security.
- Tier 2; not directly fetched.

**[62]** Cursor BugBot — https://cursor.com/bugbot
- Per agent discovery: PR review agent targeting logic bugs (not style). Self-improves from past reviews. Shipped July 2025; 80% resolution rate; reviews 2M+ PRs/month.
- NOT specifically about AI-generated reinvention — reviews all code.
- Tier 2; not directly fetched.

**[63]** Korbit hallucination elimination blog — https://www.korbit.ai/post/eliminating-hallucinations-in-ai-code-reviews-2
- Per agent discovery: LLM-as-judge with Chain-of-Thought, "Undetermined" classification, context augmentation. Reports GPT-4 correctly identifies 45% of hallucinations with 9% FPs.
- IMPORTANT: detects hallucinations in Korbit's own review output (FP suppression), NOT detecting reinvention in the code being reviewed.
- Tier 2; not directly fetched.

**[64]** DiffRay homepage — https://diffray.ai/
- Per agent discovery: multi-agent (10+ specialized) framework. Claims 87% fewer FPs and 3x more real bugs than single-agent tools. Documents existing tools hallucinate at 29-45%. Vendor claims unverified by independent benchmarks.
- Tier 3 (vendor self-report).

---

## Dimension 5 — Custom rule-pack maintenance

**[65]** Semgrep December 2024 OSS-to-CE blog — https://semgrep.dev/blog/2024/important-updates-to-semgrep-oss/
- Verbatim: "Semgrep OSS is now named Semgrep Community Edition, reflecting its role as a free, community-focused tool."
- Verbatim: "Experimental Features" migrated to commercial engine.
- Verbatim: Semgrep-maintained rules transitioned to "Semgrep Rules License v.1.0, restricting use to internal, non-competing, and non-SaaS contexts."
- Verbatim: "Semgrep's engine remains LGPL 2.1."
- Grace period until January 31, 2025 for vendors using Semgrep-maintained rules in competing products.
- Tier 2.

**[66]** Josh Grossman post-mortem on Dec 2024 changes — https://joshcgrossman.com/2025/01/28/whats-going-on-with-sem-open-grep/
- Per agent counter-discovery: practitioner write-up confirming join mode rules broke in Community Edition, nosemgrep inline suppression stopped working with JSON output (only SARIF retained it).
- Tier 3.

**[67]** Semgrep contribution docs — https://semgrep.dev/docs/contributing/contributing-to-semgrep-rules-repository
- Confirmed: CLA REQUIRED.
- Best-practice rule metadata: only `references`, `category`, `technology` required.
- Test format: filename matches rule, ≥1 true positive (`// ruleid:`), ≥1 true negative (`// ok:`).
- Quality checker: `semgrep-rule-lints`. Maintainer approval required.
- Tier 2.

**[68]** Trail of Bits semgrep-rules repo — https://github.com/trailofbits/semgrep-rules
- ~100+ rules across Go, Python, JavaScript, Ruby, Rust, Swift, HCL, JVM, YAML, generic.
- Public external pack, NOT merged into upstream semgrep-rules. Indexed in registry; users access via `semgrep --config "p/trailofbits"`.
- License: AGPLv3.
- This is the canonical model for distributing custom rules without accepting the Semgrep Rules License v1.0.
- Tier 2.

**[69]** Trail of Bits Dec 2024 rules blog — https://blog.trailofbits.com/2024/12/09/35-more-semgrep-rules-infrastructure-supply-chain-and-ruby/
- Per agent discovery: published 35 new rules in December 2024 — confirms third-party rule authoring is active.
- Tier 2; not directly fetched.

**[70]** Trail of Bits introduction guide — https://blog.trailofbits.com/2024/01/12/how-to-introduce-semgrep-to-your-organization/
- Per agent discovery: recommends internal repo for org-specific rules. Explicitly advises peer review on every new internal rule before going live to reduce FPs.
- Tier 2; not directly fetched.

**[71]** Semgrep FP reduction KB — https://semgrep.dev/docs/kb/semgrep-code/reduce-false-positives
- Per agent counter-discovery: explicitly notes "users write a lot of custom internal rules too, and those rules don't go through the same tuning process" as registry rules.
- Recommends tracking `# nosemgrep` suppression rate as leading indicator of rule noise.
- Tier 2; not directly fetched.

**[72]** Opengrep launch (Aikido) — https://www.aikido.dev/blog/launching-opengrep-why-we-forked-semgrep
- January 2025 fork of Semgrep CE. Rule-format compatible.
- Audit correction: Windows support was listed as a future-roadmap item ("windows compatibility, cross-file analysis") at launch, NOT a feature restored at launch as the original draft claimed. Current Windows status not verified in this session. Rule-format compatibility itself provides the escape hatch regardless.
- Tier 3.

**[73]** Semgrep issue #8183 — https://github.com/semgrep/semgrep/issues/8183
- Audit correction: This issue is about metavariable type constraints, NOT the broader rule-syntax-2.0 migration. The original draft attributed specific operators (`taint:`, `any:`, `inside:`) and a verbatim "you can't mix and match" quote to this issue, neither of which appear in the fetched content. Operators visible in the fetched issue are `all:`, `not:`, `where:`.
- Substantive claim retained: a separate "experimental syntax" exists, gradual migration is the path, and simple structural rules using `pattern`, `pattern-either`, `pattern-inside` are not on a forced migration path. The specific verbatim quote is removed.
- Tier 2; URL canonical, content scope corrected.

**[74]** FullStory semgrep-rules announcement — https://www.fullstory.com/blog/announcing-our-semgrep-rules-repository/
- Per agent discovery: "released a subset of the custom rules we use internally" — confirms common practice of mixed private-internal/public-subset rule maintenance.
- Tier 2; not directly fetched.

---

## Notes on source quality and gaps

- Sources marked Tier 1 are peer-reviewed; Tier 2 are official project repos and docs; Tier 3 are practitioner blogs and community forum threads. When a Tier 3 source is the only support for a claim, the claim is qualified with "per agent search snippet" or similar.
- Sources marked "INACCESSIBLE" or "not directly fetched" rely on agent search-snippet evidence rather than direct WebFetch. These are weaker and should be treated as preliminary. The reference files note when they depend on these sources.
- Where vendor-published benchmarks are cited (Greptile [56], DiffRay [64]), counter-evidence on benchmark trustworthiness ([57]) is also cited so the reader can weigh both sides.
- The "Dual-error principle" applies: an inaccurate claim would require both a fabricated fact AND a fabricated citation. Spot-check any cell of any reference table by following the `[N]` to this file and the URL to the source.
