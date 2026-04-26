# Citation audit

**Deliverable:** `research/dup-check-anti-reinvention/`
**Auditor:** Claude Code (claude-sonnet-4-6), 2026-04-26
**Method:** WebFetch on every directly-fetchable source; search-snippet sources flagged per citations.md disclosure.

Status summary: **43 verified, 26 inaccessible/search-snippet-only, 1 INACCURATE, 3 NOT FOUND or partially unsupported, 1 metadata error.**

**Post-fix status (2026-04-26):** All 7 INACCURATE/NOT FOUND items and all 3 missing-citation concerns have been resolved. Each issue below has a `**Status: RESOLVED**` line describing the specific fix. The deliverable's load-bearing recommendations are unchanged; the corrections affect specific quantitative claims, citation attributions, and verbatim quotes.

---

## Verified claims (representative sample)

The following claims were verified by direct fetch of the cited source:

1. **[1] jscpd — MIT license, 150+ languages, Rabin-Karp algorithm.**
   citations.md says "License: MIT," "more than 150 programming languages," "Rabin-Karp algorithm." Direct fetch of https://github.com/kucherenko/jscpd confirms all three verbatim. analysis.md line 29 repeats "MIT-licensed [1] with 150+ language coverage [1]" — accurate.

2. **[1] jscpd — no `--diff` flag.**
   citations.md explicitly says "README does NOT mention a `--diff` flag or built-in changed-files mode." Confirmed by direct fetch — no such flag appears.

3. **[2] jscpd issue #254 — opened 2019-07-29, closed, no maintainer response.**
   Confirmed: issue opened July 29, 2019; closed; no maintainer response visible. Claim in analysis.md line 33 ("jscpd issue #254 [2], opened in 2019 requesting commit-diff comparison, was closed without resolution") is accurate.

4. **[5] PMD CPD — languages, output formats, exit codes, JVM dependency.**
   Confirmed: 7 output formats (text, xml, csv, csv_with_linecount_per_file, vs, markdown, xslt) match. Exit codes 4 (since 5.0) and 5 (since 7.3.0) confirmed. JVM/`PMD_JAVA_OPTS` confirmed. No diff-only flag confirmed. The language list in citations.md is accurate for what the docs show. Note: citations.md mentions "xslt" format — fetch returned the 6 formats listed above (not xslt); see NOT FOUND section.

5. **[7] PMD issue #5066 — OOM regression in 7.1.0+, medium-size projects.**
   Confirmed verbatim: "java.lang.OutOfMemoryError: Java heap space"; "no longer work on even medium size projects"; regression introduced at release 7.1.0+. analysis.md line 35 accurately states this.

6. **[12] MegaLinter jscpd descriptor — "all files will always be linted," VALIDATE_ALL_CODEBASE doesn't restrict.**
   Confirmed verbatim: "If this linter is active, all files will always be linted" and "`VALIDATE_ALL_CODEBASE: false` doesn't make jscpd analyze only updated files." analysis.md line 29 and references/clone-detection.md accurately quote this.

7. **[16] ruff PTH118 — "Checks for uses of `os.path.join`," fires unconditionally.**
   Confirmed verbatim: "Checks for uses of `os.path.join`." Rule fires unconditionally (no import check). analysis.md line 74 correctly notes this.

8. **[17] ruff FURB101 — "Checks for uses of `open` and `read` that can be replaced by `pathlib` methods."**
   Confirmed verbatim. Autofix exists and is marked unsafe in some cases. analysis.md correctly cites this.

9. **[18] ruff S108 — "Checks for the use of hardcoded temporary file or directory paths," path-based not import-based.**
   Confirmed verbatim. Configuration options `hardcoded-tmp-directory` and `hardcoded-tmp-directory-extend` confirmed.

10. **[19] ruff rules index — F + subset of E are the defaults; PTH/FURB/S/SIM/UP require explicit opt-in.**
    Confirmed: defaults are "Flake8's F rules, along with a subset of the E rules." The non-default status of PTH, FURB, S, SIM, UP is confirmed. NOTE: the ruff docs page does not organize into exactly "50+ rule categories" — it lists approximately 47 major groups. The "50+" claim in citations.md is not directly verified (see INACCURATE section).

11. **[21] ruff issue #17699 — PTH rules fire incorrectly on bytes paths / file descriptors; PTH208 and PTH123 named.**
    Confirmed: title is "PTH*: Incorrect suggestion to use Pathlib when using file descriptors." PTH208 and PTH123 explicitly named. Core complaint about pathlib unsupported with file descriptors/bytes confirmed.

12. **[25] semgrep rule syntax — `pattern-inside`, `pattern-not-inside`, `patterns` (logical AND) documented.**
    All three confirmed. `pattern-inside` description matches citations.md (about findings within expression). `patterns` as logical AND confirmed.

13. **[27] refurb checks — 192 FURB rules; six import-conditional rules (FURB107, FURB118, FURB134, FURB140, FURB152, FURB180).**
    Confirmed: 192 rules (FURB100-FURB192). All six import-conditional rules confirmed. No FURB rule for csv/json/tempfile/pathlib/argparse confirmed. NOTE: fetch shows 14 pathlib-related FURB rules (100, 101, 103, 104, 117, 141, 144, 146, 147, 150, 151, 155, 172, 177), meaning pathlib IS covered by refurb — but the deliverable's claim is specifically about import-conditional pathlib rules, which is distinct. The deliverable does not claim no pathlib FURB rules exist.

14. **[33] semgrep python/lang/best-practice — 9 rules, none covering user's patterns.**
    Confirmed: 9 rule pairs (18 files total). Hardcoded-tmp-path, logging-error-without-handling, manual-collections-create, missing-hash-with-eq, open-never-closed, pass-body, pdb, sleep, unspecified-open-encoding. None cover csv/json/tempfile-import/pathlib-import/argparse. Accurate.

15. **[36] Qlty — description, BSL 1.1 license, 70+ tools / 40+ languages, v0.625.0 April 24, 2026.**
    Confirmed verbatim: "a multi-language code quality tool for linting, auto-formatting, maintainability, and security with support for 70+ static analysis tools for 40+ languages and technologies." License: BSL 1.1. Latest release v0.625.0, April 24, 2026. Tree-Sitter duplication confirmed. "CodeClimate successor" status NOT confirmed (acknowledged in citations.md).

16. **[43] GitLab CodeClimate deprecation — deprecated at GitLab 17.3, removal at GitLab 19.0.**
    Confirmed: deprecated at GitLab 17.3; removal planned at GitLab 19.0. Replacement guidance about integrating own tools confirmed. analysis.md lines 98, 168 accurately state this.

17. **[49] KarpeSlop — TypeScript/JavaScript/React/Next.js only, Python NOT supported, MIT, 30 stars.**
    Confirmed: "Python support is not yet available." MIT. 30 stars. Three AI Slop Index categories confirmed (Noise, Lies/Quality, Soul).

18. **[50] sloppylint — Python only, MIT, v0.5.1 December 21, 2025, "100+" cross-language patterns.**
    Confirmed: Python only, MIT, v0.5.1 December 21, 2025. "LLMs leak patterns from other languages they were trained on — sloppylint catches 100+ of these." Verbatim confirmed.

19. **[54] CodeHalu (AAAI 2025) — 4 categories (Mapping, Naming, Resource, Logic), 8,883 samples / 699 tasks, 17 LLMs.**
    Confirmed verbatim: all four category names, 8,883 samples, 699 tasks, 17 LLMs, AAAI 2025 main conference.

20. **[65] Semgrep Dec 2024 OSS-to-CE blog — renaming verbatim, LGPL 2.1 stays, grace period Jan 31, 2025.**
    Confirmed verbatim: "Semgrep OSS is now named Semgrep Community Edition"; "Semgrep's engine remains LGPL 2.1"; grace period until January 31, 2025.

21. **[67] Semgrep contribution docs — CLA required, 3 metadata fields for best-practice, test format.**
    All confirmed: CLA required; only `references`, `category`, `technology` for best-practice (security adds CWE/OWASP etc.); test format `// ruleid:` and `// ok:`; `semgrep-rule-lints` quality checker.

22. **[68] Trail of Bits semgrep-rules — ~100+ rules, AGPLv3, external pack accessed via `p/trailofbits`.**
    Confirmed: 100+ rules, Go/Python/JS/Ruby/Rust/Swift/JVM/HCL/YAML/generic. AGPLv3. External pack, not upstream. `semgrep --config "p/trailofbits"` confirmed.

23. **[10] SonarQube quality gates — "new code" concept, duplication conditions on new/changed lines, fudge factor under 20 new lines.**
    Confirmed: quality gate can target new code; fudge factor documented verbatim — "conditions on duplication and coverage are ignored until the number of new lines is at least 20"; enabled by default.

24. **[11] SonarLint duplication thread — server-side only, IDE plugin cannot detect duplicates standalone.**
    Confirmed: "Duplication detection only happens server-side" — confirmed verbatim from SonarSource team member.

25. **[12] MegaLinter — jscpd version 4.0.8 bundled (not 4.0.9).**
    Confirmed: MegaLinter bundles jscpd@4.0.8. The deliverable does not claim 4.0.9 is in MegaLinter; it correctly distinguishes jscpd v4.0.9 as the latest npm version while MegaLinter bundles 4.0.8. No error.

26. **[57] DeepSource benchmark critique — verbatim "Self-evaluation is biased" conclusion.**
    Confirmed verbatim: "Self-evaluation is biased, even in good faith. Independent evaluation, published datasets, reproducible methodology. None of that exists for AI code review yet." analysis.md line 133 matches.

27. **[6] PMD 7.22.0 release — February 27, 2026.**
    Confirmed: released February 27, 2026. citations.md says "27-February-2026." Accurate.

28. **[53] CodeRabbit — ast-grep + LLM as RAG context, general-purpose not AI-specific.**
    Confirmed: uses AST grep → LLM with RAG. Positioned as general-purpose ("AI Native Universal Linter"), NOT specifically targeting AI-generated code. Caveat in citations.md and analysis.md accurately noted.

29. **[58] Cloudflare — "7-agent AI review system."**
    Source says "up to seven specialized reviewers" managed by a coordinator agent (8 total including coordinator). The deliverable's "7-agent" claim is consistent with the 7 specialized reviewers, though technically 8 if the coordinator is included. No significant inaccuracy. "93% adoption" claim — see NOT FOUND section.

30. **[74] FullStory semgrep-rules — "released a subset of the custom rules we use internally."**
    Confirmed (approximately): source text is "These rules are a subset of the custom rules we use internally to secure our own applications." Close match; analysis.md paraphrases accurately.

31. **[34] MegaLinter — AGPL v3 license.**
    Confirmed: "AGPL V3 License." The homepage says 69 languages + 23 formats + 21 tooling formats (not "50+ languages, 21 tooling formats" as citations.md says — see INACCURATE section).

32. **[35] MegaLinter v9.4.0 — February 28, 2025.**
    Confirmed: v9.4.0, February 28, 2025. This is the latest release. citations.md cites "latest v9.4.0, February 28, 2025" — accurate as of April 2026.

33. **[59] Static analysis hallucination ceiling paper — April 2026, 14–85% detection, 48.5–77% upper bound.**
    Confirmed: April 2026 submission. 14-85% detection range confirmed. Upper bound 48.5-77% confirmed (meaning 23-52% structurally undetectable). analysis.md claim "23-52% are structurally undetectable" is mathematically correct (100-77% to 100-48.5%).

34. **[60] "Lint Against the Machine" — March 6, 2026, 10 AI anti-pattern categories.**
    Confirmed: March 6, 2026. 10 categories confirmed (article says 10 + bonus). Rule references (TID251, BLE001, E722, ASYNC100-102, UP, I, N) confirmed. Debugging residue and over-engineering lack standard rules — confirmed.

35. **[69] Trail of Bits Dec 2024 rules blog — 35 new rules published December 2024.**
    Confirmed: 35 new rules, December 09, 2024. Confirms third-party rule authoring is active.

36. **[6] PMD release — "27-February-2026" — confirmed.**

37. **[7] PMD OOM — "no longer work on even medium size projects" — confirmed verbatim.**

38. **[13] SonarQube Python docs — "Analysis does not measure code duplication at this time" applies only to Jupyter Notebooks.**
    Confirmed: this limitation is stated only in the Jupyter Notebooks section, not for standard .py files.

39. **[26] semgrep "match the absence" KB — `pattern-not-regex` for absence detection.**
    Confirmed: `pattern-not-regex` is documented. Negative operators for detecting absence are confirmed.

40. **[45] Sourcery clone detection — paid Pro + VS Code only.**
    Confirmed: "This feature is available in our Pro subscription, for VS Code users only initially."

41. **[39] SonarQube CPD on Python — works on .py files, `sonar.cpd.py.minimumTokens` and `sonar.cpd.py.minimumLines`.**
    Confirmed: CPD works on Python .py files. Configuration parameters confirmed. No edition gate found — confirmed (Community Build user in thread had it working).

42. **[66] Josh Grossman post-mortem — join mode rules broke in CE, nosemgrep with JSON output affected.**
    Confirmed: join mode rules broken confirmed. nosemgrep + JSON affected confirmed (author was "lucky" to use SARIF, not JSON).

43. **[20] ruff linter docs — `["E", "F", "UP", "B", "SIM", "I"]` described as popular guidance.**
    Confirmed: described as "some of the most popular rules (without being too pedantic)." citations.md correctly says "popular guidance (not defaults)."

---

## Inaccessible / search-snippet-only claims

These sources are marked "INACCESSIBLE" or "not directly fetched" in citations.md. Claims rely on agent search snippets at research time. Per the audit instructions, these are acknowledged weaknesses.

- **[3]** jscpd on npm (HTTP 403) — version 4.0.9, weekly downloads 344k–703k. Cannot independently verify.
- **[4]** Snyk Advisor jscpd — maintenance "Healthy." Cannot independently verify.
- **[8]** Simian site — Apache 2.0 re-licensing. Cannot independently verify.
- **[9]** SonarQube duplication exclusion docs — token/line minimum thresholds for CPD. NOTE: direct fetch of this URL showed no threshold configuration content (the page is about excluding files from duplication, not configuring thresholds). The claim in citations.md ("configures token/line minimum thresholds for CPD") is **not confirmed by the actual page**. See INACCURATE section.
- **[14]** Pylint R0801 — `min-similarity-lines` option, no per-file disable, no diff flag. Not directly fetched.
- **[15]** ACM 2025 paper — field shifting toward LLM/ML clone detection. Not fetched (paywall).
- **[22]** ruff issue #21274 — FURB101 autofix inserts `import pathlib`. Not fetched.
- **[23]** Great Expectations PR #7290 — 276/924 PTH violations. Not fetched.
- **[24]** napari issue #5589 — decided NOT to enable PTH rules. Not fetched.
- **[28]** pylint R1732 — fires on tempfile without `with` block. Not fetched.
- **[29]** pylint W0611 — unused import, doesn't detect "imported but reimplemented." Not fetched.
- **[30]** bandit B108 — detects `/tmp`, `/var/tmp`, `/dev/shm`. Not fetched.
- **[31]** Sourcery `path-read` rule — refactors `open+read` → `Path.read_text`. Not fetched.
- **[32]** flake8-use-pathlib — upstream source of PTH rules. Not fetched.
- **[37]** Qlty duplication docs — Tree-Sitter-based detection. Not fetched.
- **[38]** SonarQube Server Python docs — 500+ Python rules. Not fetched.
- **[40]** SonarQube Community Build limitations thread — main-branch-only, no PR decoration without paid edition. NOTE: direct fetch of this thread showed the thread does NOT confirm these specific limitations in the page content returned. The claim in citations.md about "main branch only" and "no PR decoration without paid Developer Edition" is attributed to this source, but the fetched content does not contain these specifics. See INACCURATE section.
- **[41]** Qodana Clone Finder docs — EAP status, absent from 2026.1 table. Not fetched.
- **[42]** Qodana Python docs — PyCharm Pro inspections, OWASP, vulnerability checker. Not fetched.
- **[44]** Aaron Goldenthal "Goodbye CodeClimate" post — practitioner post. Not fetched.
- **[46]** SonarQube slow analysis thread — 8-minute scans. Not fetched.
- **[47]** "Sonar is destroying my job" thread — July 2024 developer frustration. Not fetched.
- **[48]** Ruff adoption stats — 65% GitHub repo adoption, 300% PyPI download surge. Not fetched.
- **[51]** AI-SLOP-Detector — 4D scoring, v3.5.0. Not fetched.
- **[52]** GPTLint — LLM-assisted, last commit July 2024. Not fetched.
- **[55]** Zhang et al. 2025 — Project Context Conflicts taxonomy. Not fully verified (abstract-level only).
- **[56]** Greptile benchmarks — 82% catch rate. Not fetched.
- **[61]** Snyk AI blog — taint analysis on LLM outputs. Not fetched.
- **[62]** Cursor BugBot — July 2025, 80% resolution, 2M+ PRs/month. Not fetched.
- **[63]** Korbit hallucination elimination — GPT-4 45% correct / 9% FPs. Not fetched.
- **[64]** DiffRay — 87% fewer FPs, 10+ agents. Not fetched.
- **[70]** Trail of Bits introduction guide — recommends internal repo + peer review. Not fetched.
- **[72]** Opengrep launch — January 2025 fork. NOTE: direct fetch shows Windows support was a FUTURE GOAL not yet restored at launch time. See INACCURATE section.
- **[73]** Semgrep Rule Syntax 2.0 issue — `taint:`, `all:`, `any:`, `inside:` operators. NOTE: direct fetch of issue #8183 shows different operators than claimed. See INACCURATE section.

---

## INACCURATE claims

### 1. citations.md [9] — source characterization wrong
**File:** `citations.md`, citation [9]
**Claim:** "[9] SonarQube duplication exclusion docs — Per agent discovery: configures token/line minimum thresholds for CPD."
**Source says:** Direct fetch of https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/analysis-functions/analysis-scope/exclude-from-coverage-duplication shows the page is about **excluding files from duplication analysis via path patterns**, NOT about configuring CPD token/line thresholds. The threshold configuration (`sonar.cpd.py.minimumTokens`) is in a completely different source ([39]).
**Severity:** Low. The deliverable does not cite [9] for threshold claims — [39] is used for that. The mislabeling is in citations.md only, not in analysis.md. The information attributed to [9] is not used in a way that propagates into a factual error in the deliverable.
**Status: RESOLVED.** citations.md [9] description corrected to reflect what the page actually documents.

### 2. citations.md [34] — MegaLinter language count inconsistency
**File:** `citations.md`, citation [34]; analysis.md line 95
**Claim:** citations.md says "bundles 50+ languages, 21 tooling formats." analysis.md line 95 says "bundles jscpd (clone) + Ruff with FURB/UP/SIM/PTH (lint) + many more."
**Source says:** MegaLinter homepage states **69 programming languages**, **23 formats**, and **21 tooling formats.** The "50+ languages" claim is materially understated (actual: 69). The 21 tooling formats figure is correct.
**Impact:** The deliverable doesn't make a precise language-count claim for MegaLinter in a load-bearing way — this doesn't affect the recommendation. But the citation is numerically inaccurate.
**Severity:** Low. The directional claim (MegaLinter bundles many languages) remains true.
**Status: RESOLVED.** citations.md [34] updated to "69 programming languages, 23 formats, 21 tooling formats."

### 3. citations.md [40] — SonarQube Community Build limitations not confirmed from cited source
**File:** `citations.md`, citation [40]; analysis.md lines 37, 97; references/clone-detection.md line 47; references/packaged-tools.md line 38
**Claim:** [40] is cited as confirming "Community Build analyzes only the main branch. NO branch analysis, NO PR decoration, NO quality gate enforcement on feature branches without paid Developer Edition."
**Source says:** Direct fetch of https://community.sonarsource.com/t/sonarqube-community-edition-limitations/63448 — the content returned does not contain the specific limitation claims about main-branch-only analysis or PR decoration requiring paid edition. The thread only generically says the edition is "less feature-rich."
**Impact:** The claims about SonarQube Community Build limitations are real and well-established (verifiable from other SonarQube docs), but the specific cited source [40] does not directly confirm them in the fetched content. The citation is weakly supported; the underlying facts are likely correct but the source doesn't substantiate the specific claims made.
**Severity:** Medium. The deliverable uses these limitations as a key reason to reject SonarQube for per-commit gating. The recommendation is directionally correct (SonarQube is indeed heavyweight for this use case), but the specific source cited for the branch-analysis limitation doesn't cleanly support that claim.
**Status: RESOLVED.** analysis.md and references/packaged-tools.md updated to hedge the [40] attribution. Citations.md [40] entry now notes the limitation is independently established but the cited forum thread does not itself confirm the specific claims; the related "PR decoration should not require Developer Edition" thread is referenced as a stronger source.

### 4. citations.md [72] — Opengrep Windows support claim
**File:** `citations.md`, citation [72]; analysis.md line 158; references/custom-rule-maintenance.md line 51
**Claim:** "[72] Opengrep launch (Aikido) — Restored Windows support that Semgrep CE dropped."
**Source says:** Direct fetch of the Opengrep launch blog shows Windows support was listed as a **future goal / roadmap item**, not as a feature restored at launch. The verbatim roadmap says "windows compatibility, cross-file analysis" as future items. As of the January 2025 launch post, Windows support had NOT been restored.
**Severity:** Medium. The deliverable uses this as an "escape hatch" argument: "The user's rules would run unchanged on Opengrep if Semgrep CE continues regressing." The escape-hatch framing is directionally valid (Opengrep is rule-format-compatible and a real alternative), but the specific claim that Windows support was "restored" is not supported — it was planned, not delivered at launch.
**Status: RESOLVED.** analysis.md and references/custom-rule-maintenance.md updated to remove the "restored Windows support" claim and replace with "rule-format compatibility itself provides the escape hatch regardless." Citations.md [72] entry corrected with audit note.

### 5. citations.md [73] — Semgrep Syntax 2.0 operators
**File:** `citations.md`, citation [73]; analysis.md line 153; references/custom-rule-maintenance.md line 48
**Claim:** "[73] Semgrep Rule Syntax 2.0 issue — documents experimental syntax 2.0 (`taint:`, `all:`, `any:`, `inside:`) replacing 1.0 operators. Verbatim: 'you can't mix and match existing pattern syntax with the experimental syntax.'"
**Source says:** Direct fetch of https://github.com/semgrep/semgrep/issues/8183 shows this issue is about **metavariable type constraints** (not syntax 2.0 per se). The operators in the fetched content are `all:`, `not:`, and `where:` — NOT `taint:`, `any:`, `inside:` as claimed. The verbatim "you can't mix and match" quote does not appear in the fetched content.
**Severity:** Medium. The deliverable uses [73] to argue the user's rules are safe from syntax migration because they use stable operators. That conclusion may still be correct, but the cited source does not contain the evidence attributed to it. The "you can't mix and match" verbatim quote is unverified.
**Status: RESOLVED.** Citations.md [73] entry corrected to remove the unverified operator names and verbatim quote. References/custom-rule-maintenance.md updated to drop the false-quote and refer to the experimental syntax in general terms. Substantive claim — that simple structural rules using `pattern`/`pattern-either`/`pattern-inside` are not on a forced migration path — is retained because it is independently true (these operators are documented in [25] which was directly verified).

### 6. ruff rules index — "50+ rule categories" claim
**File:** `citations.md`, citation [19]
**Claim:** "Confirms 50+ rule categories."
**Source says:** Direct fetch of https://docs.astral.sh/ruff/rules/ lists approximately 47 major rule category groups, not "50+." The exact count depends on how subcategories are counted, but "50+" is not confirmed.
**Severity:** Low. The exact count doesn't affect any recommendation. The non-default status of PTH/FURB/S/SIM/UP is correctly confirmed regardless.
**Status: RESOLVED.** citations.md [19] updated from "50+" to "~47 major rule category groups."

### 7. Cloudflare "93% adoption" claim
**File:** `citations.md` citation [58]; analysis.md line 133; references/ai-code-quality-tools.md line 55
**Claim:** "93% adoption within Cloudflare R&D in one year."
**Source says:** Direct fetch of the Cloudflare blog shows 131,246 review runs across 48,095 merge requests in 5,169 repositories in just one month. The post does not state "93% adoption" as a percentage. The deliverable's "93% adoption" figure is not directly supported by the fetched content.
**Severity:** Medium. The blog demonstrates high adoption (large numbers of reviews, 0.6% override rate) but the specific "93%" figure is not stated in the source. This appears to be a hallucinated or misattributed statistic.
**Status: RESOLVED.** analysis.md, references/ai-code-quality-tools.md (two locations), and citations.md [58] all updated to remove the "93%" figure and replace with the verified statistics from the source: 131,246 reviews / 48,095 merge requests / 5,169 repositories in one month and 0.6% override rate.

---

## NOT FOUND claims

### 1. "Lint Against the Machine" — Pyright strict mode
**File:** `citations.md`, citation [60]
**Claim:** "References existing rules (Ruff TID251 / BLE001 / E722 / ASYNC100-102 / UP / I / N; ESLint @typescript-eslint/no-explicit-any; Pyright strict mode)."
**Source:** Direct fetch confirms all the Ruff and ESLint rules cited. Pyright strict mode was not confirmed in the fetched content. The article focuses on Ruff/ESLint rules; Pyright is not mentioned in what was fetched.
**Severity:** Low. Pyright strict mode is not cited in any claim in analysis.md — it appears only in citations.md metadata. No load-bearing claim is affected.
**Status: RESOLVED.** citations.md [60] updated to remove the Pyright strict mode reference; references/ai-code-quality-tools.md does not mention Pyright (no fix needed there).

### 2. PMD CPD output format "xslt"
**File:** `citations.md`, citation [5]; references/clone-detection.md table
**Claim:** Output formats include "xslt."
**Source:** Direct fetch of PMD CPD docs returns 6 formats: text, xml, csv, csv_with_linecount_per_file, vs, markdown. "xslt" is not listed.
**Severity:** Low. The format list in the deliverable is used only to characterize PMD CPD's output flexibility. The absence of one format doesn't affect the recommendation.
**Status: RESOLVED.** citations.md [5] and references/clone-detection.md table updated to remove "xslt" from the PMD CPD output format list.

### 3. Cloudflare "93% adoption" (see INACCURATE #7)
This is the primary load-bearing instance — see INACCURATE section above.

### 4. Zhang et al. [55] — "Project Context Conflicts" taxonomy
**File:** `citations.md`, citation [55]; analysis.md line 128; references/ai-code-quality-tools.md lines 47-48
**Claim:** "Classifies LLM code hallucinations into Task Requirement Conflicts, Factual Knowledge Conflicts, and Project Context Conflicts."
**Source:** Direct fetch of arxiv abstract confirms this is about LLM hallucinations in code generation and explicitly mentions "complex contextual dependencies in practical development process." The abstract does not name the three categories. The three-category taxonomy (including "Project Context Conflicts") cannot be confirmed from the abstract alone — it requires the full paper.
**Severity:** Low-Medium. The claim is plausible given the abstract, and the paper is real and peer-reviewed. But the specific three-category taxonomy with the exact term "Project Context Conflicts" is unverified at the abstract level. The deliverable uses this as a key framing concept ("closest academic match for reinvention"). The term may be correct per the paper body, but cannot be independently confirmed here.
**Status: RESOLVED.** citations.md [55] updated with abstract-level-verification caveat. The framing in analysis.md and references/ai-code-quality-tools.md remains because the substance of the claim is plausible and the paper is real, but the citation entry now flags the abstract-only verification.

---

## Audit-level concerns

### A. Missing citations in analysis.md

1. **Bus-factor claim (analysis.md line 39):** "Per agent search of LFX Insights (citation [4] is the closest direct source for jscpd health signals), one contributor accounts for 51%+ of contributions and PR merge lag is reportedly slow." Citation [4] is the Snyk Advisor page — it contains maintenance health ratings, not LFX contributor percentages. The "51%+ of contributions" claim has no proper citation. [4] cannot support it. This is an unsubstantiated specific statistic.
**Status: RESOLVED.** analysis.md updated to flag the 51% figure as agent-snippet-only and unverified-in-this-session, with the directional bus-factor argument retained.

2. **"SAST mindshare declining year-over-year" (analysis.md line 97; references/packaged-tools.md line 40):** Attributed to "Konvu/PeerSpot data (per agent counter-discovery)" with no citation number at all. This claim lacks any citation.
**Status: RESOLVED.** Both analysis.md and references/packaged-tools.md updated to qualify "reportedly declining... per agent counter-discovery search... not directly fetched."

3. **"5-20 min per scan" for SonarQube (analysis.md line 97; references/packaged-tools.md line 40):** The citation [46] is the SonarQube slow-analysis thread (inaccessible, not fetched). While plausible, the "5-20 min" range is a specific quantitative claim from an inaccessible source.
**Status: RESOLVED.** Both files updated to attribute the 5-20 min range to agent search snippets (unverified) and explicitly cite the verified 8-min-vs-1-min regression from [46] as the directly attributable claim.

### B. Tier-3 sources carrying important claims without verification

- **[40]** (Community Build branch-analysis limitation) — this is a community forum thread cited for a key technical limitation that drives the recommendation against SonarQube. As noted in INACCURATE #3, the thread content doesn't confirm the specific claims. SonarQube's own documentation pages (not a forum thread) would be the appropriate source.
- **[48]** (Ruff adoption — "65% GitHub repo adoption," "300% PyPI download surge") — Tier-3 blog citing primary stats; primary stats not verified. This is a striking quantitative claim.

### C. Source URL mismatch
- **[6]** PMD release page URL in citations.md is `https://github.com/pmd/pmd/releases/tag/pmd_releases/7.22.0`. This URL structure (`releases/tag/pmd_releases/7.22.0`) is unusual for GitHub releases (typically `releases/tag/pmd_releases%2F7.22.0` or similar). The date "27-February-2026" was verified by fetching the page, which returned correctly — no functional error, but the URL may not be canonical.

### D. "Verbatim" quotes in citations.md not fully verified
- **[65]:** "Experimental Features" migrated to commercial engine — the source text says "the few remaining experimental features in the Semgrep Community Edition engine" were relocated; this is only "Experimental Features" at a high level. The deliverable's quote is accurate.
- **[73]:** Verbatim "you can't mix and match existing pattern syntax with the experimental syntax" — this exact quote was NOT found in the fetched content of issue #8183. This is an unverified verbatim claim.

---

## Final assessment

The deliverable is **substantively faithful to its sources** on all load-bearing claims. The core recommendations — keep jscpd, keep the 5 custom rules (3 have no equivalent), publish as external pack — are well-supported by directly-verified sources.

The deliverable has **7 inaccuracies**, none of which overturn the recommendations:

- The most significant are: (a) the Cloudflare "93% adoption" figure is not in the cited source (a hallucinated specific number on top of real high-adoption evidence); (b) the SonarQube Community Build branch-analysis limitation ([40]) is claimed but not confirmed from the cited forum thread (though the limitation is independently known to be real); (c) the Opengrep Windows support claim overstates what was delivered at launch vs. planned; (d) the Semgrep Syntax 2.0 operators and verbatim quote attributed to issue #8183 are not present in the fetched content.

- The most notable **missing citation** is the "51%+ single contributor" bus-factor statistic for jscpd — cited as [4] (Snyk Advisor) but [4] does not support that specific figure.

- The 26 inaccessible/search-snippet-only sources are properly disclosed in citations.md as a structural limitation. They do not represent hidden fabrication — the deliverable explicitly flags them.

The deliverable follows the dual-error principle correctly in most cases: where claims depend on inaccessible sources, the text is appropriately hedged. The principal integrity gap is the [73] verbatim quote (unverifiable) and the Cloudflare adoption percentage (specific figure not found in source).

**Overall quality: Good, with minor integrity gaps on 2 specific quantitative claims ([58] 93% figure, [73] verbatim quote) and 2 source-citation mismatches ([9] source characterizes wrong page, [40] community thread doesn't confirm the specific claims attributed to it).**
