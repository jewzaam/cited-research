# Reference: All-in-one packaged tools

Sources cited inline as `[N]` against [citations.md](../citations.md).

## What this dimension covers

Is there a single CLI / platform that bundles clone detection AND anti-reinvention/stdlib-preference linting? Or is the current state-of-the-art "compose jscpd + ruff/refurb yourself"?

## Comparison

| Tool | Self-host / SaaS / CLI | Clone detection? | Anti-reinvention rules? | License | CI per-PR fit | Last activity |
|---|---|---|---|---|---|---|
| **MegaLinter** | Docker / npm CLI | YES — bundles jscpd [12][34] | Delegated — bundles ruff with FURB/UP/SIM/PTH; pylint; bandit [34] | AGPL v3 [34] | Yes by design [12]; jscpd runs whole-codebase by default [12] | v9.4.0, 2025-02-28 [35] |
| **Qlty** (Qlty Software) | CLI (Rust) + cloud [36] | YES — Tree-Sitter AST detection [36][37] | Delegated — bundles Ruff/Pylint/Flake8/Bandit/Black/Mypy [36] | BSL 1.1 (free for commercial) [36] | Yes — CLI-friendly | v0.625.0, 2026-04-24 [36] |
| **SonarQube Server** | Server + scanner CLI / SonarCloud SaaS [38] | YES — CPD on Python `.py` files [13][39] | Partial — 500+ Python rules; no specific "prefer-stdlib" category surfaced [38] | Community Build = LGPL/SSALv1 mixed; Server = commercial | Native diff/new-code mode [10] but per-PR features (branch analysis, PR decoration) **require paid Developer Edition** [40] | SonarQube Server 2025.5/2025.6 active in 2026 [9] |
| **Qodana** (JetBrains) | Docker / `qodana-cli` | Partially — DuplicatedCode inspection (PyCharm-derived); separate Clone Finder product status uncertain [41] | Inspections from PyCharm Pro; OWASP Top 10; structural search [42] | Community for Python = free; paid: Ultimate, Ultimate Plus | Yes by design; recent native mode reduces Docker overhead | qodana-action v2025.3.2 (per agent) |
| **DeepSource** | SaaS only | No confirmed shipping feature for clone detection | 150+ Python issue categories; Django/Flask aware; some "consider built-in" detections (per agent) | Proprietary freemium | PR-only analysis | Active |
| **Codacy** | SaaS + CLI v2 | YES (cloud only — uses PMD CPD); CLI v2 lint-only | 60+ analyzers including Pylint, Ruff, Bandit | SaaS freemium; CLI is open source | Cloud yes; local CLI lint-only | CLI v2 active 2026 |
| **GitLab Code Quality** | CI feature | CodeClimate-based bundle includes duplication; **deprecated, removed in GitLab 19.0 (May 2026)** [43][44] | None bundled — users integrate own tools | GitLab CE (MIT) / EE | Framework for ingesting external tool reports | Deprecation in flight |
| **Sourcery** | `sourcery-cli` + IDE | Clone detection paid + VS Code-only [45] | YES (default refactoring rules) — strongest among surveyed [31] | Proprietary freemium | `sourcery review --check` for CI; but clone detection is paid+IDE-only | Active |

## Key findings

### MegaLinter is the closest "single-CLI" answer

MegaLinter [12][34] bundles jscpd as the COPYPASTE-category linter and Ruff (with FURB, UP, SIM, PTH rule sets) as the Python lint layer. It also bundles pylint, black, flake8, isort, bandit, mypy, pyright, nbqa. Single Docker invocation runs everything. Latest release v9.4.0, February 2025 [35] — confidence on subsequent 2025-2026 releases is lower (no fetch confirmed activity past Feb 2025 in this session).

Tradeoff: MegaLinter is a heavyweight Docker image that runs all tools whole-codebase by default [12]. The user's lean per-commit gate would either accept that runtime, or reach into the Docker image for individual binaries — at which point it's no longer "one tool."

### Qlty is the next closest, with native AST clone detection

Qlty [36] bundles Tree-Sitter-based AST clone detection (not jscpd) [37] and Python linters via plugin architecture (Ruff, Pylint, Flake8, Bandit, Black, Mypy). Single Rust CLI. License is BSL 1.1 (free for commercial). Active development with v0.625.0 on 2026-04-24 [36].

Worth noting: the agent's discovery report claimed Qlty is the "CodeClimate successor", but the direct repo fetch did not confirm that institutional relationship — listed only as "Qlty Software." Industry knowledge indicates same founders/team, but the repo itself does not document this lineage.

### SonarQube has the deepest analysis — but the wrong cost shape for per-commit gating

SonarQube has CPD for Python [13][39], 500+ Python rules [38], and the cleanest diff-mode quality-gate primitive [10] — only counts duplications in new/changed code. But: the free Community Build does **not** support branch analysis or PR decoration [40] — those gating features require paid Developer Edition.

Documented developer frustration with SonarQube noise is publicly visible [47] and the cited analysis-slowness thread [46] reports an 8-min-vs-1-min regression after a v2025.3.1 upgrade (the wider 5-20 minute range came from agent search snippets and is unverified by direct fetch). Mindshare in SAST is reportedly declining year-over-year per Konvu/PeerSpot data via agent counter-discovery (not directly fetched). For per-commit pre-merge gating in a small-team agentic-development context, SonarQube's costs (license, infra, latency) outweigh its sophistication.

### GitLab is institutionalizing the compose-it-yourself pattern

GitLab has deprecated its CodeClimate-based Code Quality scanning [43] (which previously bundled duplication detection). Replacement guidance: "integrate your own tools (Ruff, Flake8, Pylint, Bandit) directly in CI and emit Code Quality artifacts" [43][44]. Removal scheduled GitLab 19.0, May 2026.

This is a major platform endorsing the composable pattern — direct evidence that the industry is converging on the user's existing approach (jscpd + ruff/refurb wired together) rather than on bundled monoliths.

### Sourcery covers anti-reinvention well — but its clone detection is paywalled and IDE-bound

Sourcery's default rule set [31] is the strongest "stdlib-preference" coverage of any tool surveyed (e.g., `path-read`, `use-built-in-next`, `use-join`). But its clone-detection feature is paid and VS Code-only [45] — incompatible with a CLI-first CI gate.

### DeepSource and Codacy: SaaS-only with partial coverage

DeepSource has rich Python lint coverage but no confirmed shipping clone-detection feature. Codacy bundles PMD CPD in cloud only — local CLI v2 is lint-only. Both are SaaS-first models, mismatched to a self-hosted per-commit gate.

## Verdict for Dimension 3

**Partial — MegaLinter and Qlty bundle both.** The "single CLI for clone + lint" answer exists. MegaLinter [34] is the closest match for the user's exact composition (jscpd + Ruff with FURB/UP/SIM/PTH). Qlty [36] is the cleaner CLI alternative with its own AST clone detector instead of jscpd.

But neither bundle changes the answer to the user's main question. The reinvention-detection layer in both is delegated to Ruff (with the unconditional PTH/FURB semantics described in Dim 2) — not to anything import-conditional that would replace the user's 5 custom rules. The user can adopt MegaLinter as a wrapper if they want a one-tool runtime, but the custom semgrep layer is still doing work no off-the-shelf bundle does.

## Gaps and limitations

- MegaLinter v9.4.0 release date (2025-02-28) was fetched [35], but subsequent 2025-2026 releases not confirmed. Tool may be more or less actively maintained than this snapshot suggests.
- Qlty's "CodeClimate successor" status was not verified by primary source.
- SonarQube's exact list of "prefer-stdlib" rules was not enumerable from the docs page reached [13][38]. There may be more or fewer such rules than the 500+ count suggests.
- Qodana Clone Finder's current GA status is genuinely uncertain [41] — listed in some pages, absent from current product feature tables.
- DeepSource's clone-detection roadmap item URL redirects to homepage; status unknown.
