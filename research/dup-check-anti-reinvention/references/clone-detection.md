# Reference: Clone detection landscape

Sources cited inline as `[N]` against [citations.md](../citations.md).

## What this dimension covers

The user runs `npx jscpd` on Python files in the most recent commit as their clone-detection layer. The question: has anything better emerged since jscpd, and is jscpd still the right pick for portable, multi-language, npx-installable, diff-friendly CI gating?

## Comparison table

| Tool | Languages | Install | Output | License | Diff/changed-files mode | Last release / activity |
|---|---|---|---|---|---|---|
| **jscpd** | 150+ formats [1] | npx (Node.js) [1] | console, HTML, JSON, XML, SARIF, badge, AI [1][12] | MIT [1] | NO native flag [1][2]; external `git diff --name-only \| --pattern` workaround | v4.0.9, mid-April 2026 (per agent search) [3] |
| **PMD CPD** | ~26: Java, JSP, C/C++, C#, Go, Kotlin, Ruby, Swift, Apex, HTML, Dart, Fortran, Gherkin, JavaScript, Lua, Matlab, Modelica, Objective-C, Perl, PHP, PL/SQL, Python, Scala, T-SQL, Velocity, XML [5] | JVM [5] | text (default), xml, csv, csv_with_linecount_per_file, vs, markdown [5] | BSD-style [5] | NO native flag [5]; analysis cache helps but for PMD rules, CPD-specific behavior unconfirmed | v7.22.0, 27-Feb-2026 (per agent search) [6]; OOM regression in 7.1.0+ [7] |
| **Simian** | Java, C#, C/C++, COBOL, Ruby, JSP, ASP, HTML, XML, Visual Basic, Groovy, Python (initial), Objective-C++ (per agent search [8]) | JVM [8] | plain text (default), XML, YAML, editor-friendly [8] | Apache 2.0 (re-licensed; transition date unconfirmed) [8] | NO native flag | latest v4.1.2 per agent snippet; date not confirmed [8] |
| **SonarQube CPD** | Wide (Python `.py` confirmed [13][39]) | Server (Java) + sonar-scanner CLI; SaaS as SonarCloud | Web UI dashboard, REST API, PR decoration | Community Build = LGPL/SSALv1 (mixed); Server = commercial | YES native — quality gate "new code" mode applies duplication conditions only to new/changed lines vs. target branch [10] | SonarQube Server 2025.5/2025.6 active in 2026 [9] |
| **SonarLint** | IDE-side | IDE plugin | IDE inline | proprietary | N/A — duplication is server-side only [11] | Active |
| **Pylint R0801** | Python only | pip | pylint reporter (text/JSON) | GPL-2.0 | NO native flag [14] | Active (PyCQA) |
| **Open-NiCad** | C, C#, Java, Python (extensible via TXL) | TXL on Linux/Unix; not pip/npx | XML; VisCad viewer | NOT confirmed in fetch | NO | v7.0, 15-Jan-2024 per agent snippet |
| **dupl** (mibk) | Go only | `go install` / binary | console, HTML, plumbing | NOT confirmed | NO native; pass file list via `-files` stdin | Likely dormant per agents |
| **Microsoft near-duplicate-code-detector** | C#, F#, Java, JS, Python (extensible) | .NET CLI | JSON groups, CSV similarity | NOT confirmed | Not designed for CI | Research-oriented; status unclear |
| **boyter/dcd** | Not confirmed in fetch | Native binaries (Linux/macOS) | NOT confirmed | AGPL-3.0 (per agent) | NO | Activity unclear |
| **CodeAnt AI (SaaS)** | 30+ incl. Python, JS, Go, Rust | SaaS / GitHub App | PR decoration, dashboard | Proprietary; $10/user/mo Basic | YES — operates on PR diff by design (per agent snippet) | Active 2024-2026 startup |

## Key findings

### jscpd remains the default for the npx/portable niche

No new npx-installable, multi-language, zero-dependency clone-detection CLI emerged in 2024-2026 that meaningfully challenges jscpd [counter-evidence per agent search]. jscpd is still actively maintained — v4.0.9 published mid-April 2026 [3], with weekly downloads in the 344k-703k range (per agent search of Snyk Advisor [4]). MegaLinter — a widely-used CI lint aggregator — bundles jscpd as the **sole** COPYPASTE-category tool with no announced replacement [12].

The 4.x series added forward-looking features: an MCP server, an `ai` reporter for LLM pipelines, and integration with Claude Code / Copilot agent skills [1]. This is active feature development, not maintenance mode.

### jscpd does NOT have a native diff-only flag

jscpd issue #254 [2] is a 2019 feature request for diff/changed-files mode that was closed without a documented resolution and without a maintainer response. The capability exists only via external scripting — pipe `git diff --name-only` into `--pattern` glob to scope analysis to changed files. The MegaLinter integration [12] explicitly confirms this: "If this linter is active, all files will always be linted. `VALIDATE_ALL_CODEBASE: false` doesn't make jscpd analyze only updated files."

This matters for the user's most-recent-commit scoping: jscpd in CI requires either external `--pattern` glue or accepting whole-codebase scans.

### PMD CPD has more output formats but a JVM dependency and a recent OOM regression

PMD CPD covers ~26 languages [5] vs jscpd's 150+ [1]. It produces 7 output formats including the standard CSV/XML/text triplet and exits with status 4 or 5 on duplicates found [5]. The JVM dependency makes it less portable in Node-centric CI environments. PMD GitHub issue #5066 [7] documents a `java.lang.OutOfMemoryError` regression in CPD starting at PMD 7.1.0+, described as making CPD "no longer work on even medium size projects" — a concrete functional regression, not theoretical.

### SonarQube has the best diff-mode story but the worst install footprint

SonarQube has a native "new code" concept [10] — quality gates apply duplication conditions only to lines added/changed since a target branch. A "fudge factor" ignores duplication on PRs adding fewer than 20 new lines. This is the only tool surveyed with first-class diff/PR-scoped duplication gating.

The cost: SonarQube requires server deployment (or SonarCloud SaaS), and the free tier (Community Build) does NOT include branch analysis or PR decoration [40] — those require paid Developer Edition. Effectively, free SonarQube cannot per-PR gate. This makes it inappropriate for the user's lightweight per-commit gate use case.

### Simian status partially uncertain

Per the agent's snippet read of simian.quandarypeak.com [8], Simian was re-licensed under Apache 2.0 by Quandary Peak Research. The transition date and current maintenance signal could not be verified by direct fetch this session. Even with the new license, Simian retains the JVM dependency and has minimal public development community.

### Pylint R0801 is Python-only and has tuning limitations

Pylint's `duplicate-code` (R0801) message [14] is Python-only and tunable via `min-similarity-lines`. Known limitation per agents' references: the message cannot be disabled per-file via inline `# pylint: disable` comments, complicating noise tuning. No native diff-only flag.

### Long-term momentum is shifting to LLM-based clone detection — but no productized CLI

Multiple 2024-2025 papers focus on transformer/LLM-based clone detection (per agent counter-discovery, e.g. ACM 2025 evaluation [15]). These remain research artifacts without usable CLI tools as of 2026-04. jscpd's token-hashing approach is the dominant productized choice today, even as the academic field moves elsewhere.

## Verdict for Dimension 1

**Off-the-shelf available — keep jscpd.** No credible portable npx-installable replacement has emerged. PMD CPD is more powerful for Java-heavy stacks but inferior for Node-CI portability and currently has a documented OOM regression. SonarQube is the only tool with first-class diff/PR scoping but the install/cost overhead is incompatible with a lightweight per-commit gate. The user's "jscpd via npx" choice is consistent with current best practice; the diff-only scoping the user wants is solved with a small `git diff --name-only` wrapper rather than a tool swap.

The framing-challenge note from Phase 0 applies here: clone detection over the latest commit alone is weaker signal than the user might hope, because clones often span files where the copy lives outside the diff. A periodic full-repo jscpd run (e.g., nightly) complements the per-commit pre-commit gate. This is a scope question, not a tool question.

## Gaps and limitations

- jscpd v4.0.9 publish date and weekly download counts come from agent search snippets [3][4], not direct npm registry fetch (npm returned 403 in-session).
- Simian's Apache 2.0 re-licensing date [8] is unverified.
- PMD CPD analysis cache behavior for CPD specifically (vs. PMD rules) is undocumented.
- The boyter/dcd, Microsoft near-duplicate-code-detector, and dupl tools have minimal in-session verification — listed for completeness but not recommended.
