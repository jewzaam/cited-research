# Reference: Stdlib-preference / anti-reinvention rule packs

Sources cited inline as `[N]` against [citations.md](../citations.md).

## What this dimension covers

The user has 5 custom semgrep rules of the form "you imported X but are reimplementing what X does":

1. **csv-stdlib** — flag `line.split(",")` when `import csv` is in the same file
2. **json-stdlib** — flag `.replace('"', '\\"')` when `import json` is in the same file
3. **tempfile-stdlib** — flag manual `/tmp/<uuid>` paths when `tempfile` is imported
4. **pathlib-over-ospath** — flag `os.path.join` etc. when `pathlib` is imported
5. **argparse-over-sysargv** — flag `sys.argv[N]` when `argparse`/`click` is imported

This dimension maps each rule to the closest existing check in semgrep's public registry, in ruff/pylint/refurb/Sourcery, and in the broader Python lint ecosystem.

## The architectural distinction

Most existing Python linters fire **unconditionally** on the bad pattern. The user's rules fire **conditionally** on the relevant import being present in the same file. The semantic difference is:

- **Unconditional rule** (ruff PTH, refurb most rules, bandit B108): "you used `os.path.join` anywhere — fix it."
- **Import-conditional rule** (user's, plus a subset of refurb): "you have `import pathlib` but are calling `os.path.join` — that's a consistency smell."

The unconditional rules are migration tools — they push entire codebases onto a preferred API. The import-conditional rules are consistency tools — they catch the developer who already committed to the right API but slipped on one specific call.

This distinction matters: refurb does have **some** import-conditional rules (FURB107, FURB118, FURB134, FURB140, FURB152, FURB180) [27] — but none cover the user's specific csv/json/tempfile/pathlib/argparse patterns.

## Rule-by-rule mapping

| User's rule | Closest existing check | Same semantic? | Verdict |
|---|---|---|---|
| **1. csv-stdlib** (csv-imported + line.split(",")) | None found in ruff, refurb, pylint, semgrep registry, Sourcery | N/A | **No equivalent.** Novel rule. |
| **2. json-stdlib** (json-imported + manual quote escape) | None found | N/A | **No equivalent.** Novel rule. |
| **3. tempfile-stdlib** (tempfile-imported + manual /tmp/uuid path) | ruff S108 (hardcoded-temp-file) [18] / bandit B108 [30] — flags hardcoded `/tmp` paths unconditionally; pylint R1732 (consider-using-with) [28] — covers tempfile lifecycle, not construction | Partial — different aspect. S108/B108 catches `/tmp` literals regardless of imports; pylint R1732 catches missing `with`-block lifecycle. Neither catches "imported tempfile but built /tmp/<uuid> manually." | **Partial overlap.** Most behavior is gap. |
| **4. pathlib-over-ospath** (pathlib-imported + os.path.X) | ruff PTH118 (os-path-join) [16], PTH100, PTH110, PTH111, PTH119, PTH120, PTH122, PTH123 (full PTH series, ~20 rules) — fires unconditionally on os.path usage [21]. ruff FURB101 (read-whole-file) [17] — migrates open+read to Path.read_text, autofix adds `import pathlib` [22]. Sourcery `path-read` [31] — refactors open+read to Path.read_text. | Different semantic. Ruff PTH and FURB are migration sweeps — they fire even when pathlib is NOT imported, and the fixes can be inappropriate (file descriptors, bytes paths) per ruff issue #17699 [21]. The user's rule fires only when the developer has already chosen pathlib, signaling an inconsistency. | **Partial overlap (best in class).** PTH covers the underlying check, but loses the "imported = developer intent" signal. |
| **5. argparse-over-sysargv** (argparse/click-imported + sys.argv[N]) | None found in ruff, refurb, pylint, semgrep registry, Sourcery | N/A | **No equivalent.** Novel rule. |

### Per-rule detail

**Rule 1 — csv-stdlib.** Search across ruff [19], refurb [27], pylint, semgrep public registry [33], and Sourcery returned zero matches for "flag `line.split(',')` when `csv` is imported." Pylint's W0611 (unused-import) [29] would flag `import csv` only when nothing from `csv` is referenced anywhere — a strict subset of the user's pattern that misses the common case where `csv` is imported for legitimate use elsewhere while one specific row-split is hand-rolled.

**Rule 2 — json-stdlib.** Same outcome as rule 1 — no existing rule for "flag manual quote escape when `json` is imported."

**Rule 3 — tempfile-stdlib.** Ruff S108 [18] and bandit B108 [30] catch hardcoded `/tmp`, `/var/tmp`, `/dev/shm` literals. The detection is **path-based, not import-based** [18] — fires regardless of whether `tempfile` is imported. The user's rule adds two things S108/B108 don't:

- The "you imported tempfile" signal — meaning the user already chose the right library.
- Detection of `/tmp/{uuid.uuid4()}` f-string construction, not just literal hardcoded paths.

Pylint R1732 [28] catches a different aspect: assigning `tempfile.NamedTemporaryFile()` without a `with` block. Lifecycle, not construction. The user's rule is closest to a yet-unwritten composite of S108 + R1732 + import-context.

**Rule 4 — pathlib-over-ospath.** This is the user's most "covered" rule. Ruff's PTH series [16] catches the full suite of `os.path.*` usages with unconditional, opt-in rules. The full PTH category includes at least PTH100, PTH101, PTH110, PTH111, PTH112, PTH113, PTH118, PTH119, PTH120, PTH122, PTH123, PTH201, PTH208 (per ruff rules index [19] and ruff issue #14490 for PTH208). FURB101 [17] and FURB103 augment this for open()/read()/write() patterns.

But two things matter:
1. **PTH is not in the default ruff rule set.** Ruff's defaults are F + subset of E only [19][20]. Teams must opt in via `extend-select = ["PTH"]` to get any of these.
2. **PTH fires unconditionally.** Ruff issue #17699 [21] documents that PTH rules suggest pathlib equivalents even when pathlib is unsupported (file descriptors, bytes paths). The Great Expectations team enabling PTH found 924 violations across their codebase [23] — a bulk migration sweep. Napari explicitly disabled PTH because it wasn't compatible with their codebase style [24].

The user's rule does something different: it fires only when `pathlib` is already imported in that file. That's a much smaller surface — files where the developer has already declared intent — and a much higher-precision signal (the violation is genuine inconsistency, not an unwanted migration nudge).

**Rule 5 — argparse-over-sysargv.** No existing rule in any tool surveyed flags `sys.argv` indexing conditional on argparse or click being imported. Novel.

## Why the gap exists: pattern-context support varies by linter

Semgrep's `pattern-inside` operator [25] supports the idiom `patterns: [pattern: code, pattern-inside: import X\n...]` for matching code conditional on an import being present elsewhere in the file. This is the architectural primitive the user's rules exploit. Semgrep also supports `pattern-not-regex` for absence detection [26].

Ruff's rules are implemented in Rust, not as composable YAML patterns — adding an import-context check requires a code change to ruff itself, not a rule definition. Pylint's plugin system theoretically permits import-context awareness but no plugin in the canonical ecosystem (per agent searches) implements it for these specific patterns.

Refurb is the partial counter-example: it has FURB107, FURB118, FURB134, FURB140, FURB152, FURB180 [27] — six import-conditional rules. So the architectural capability exists in refurb. It's just not directed at csv/json/tempfile/pathlib/argparse-vs-sys.argv.

## Verdict for Dimension 2

**Mixed: rule 4 has substantive overlap, rule 3 has partial overlap, rules 1/2/5 have no equivalent.**

| Rule | Best-existing-coverage | Effective Cover (0-1) |
|---|---|---|
| csv-stdlib | none | 0 |
| json-stdlib | none | 0 |
| tempfile-stdlib | S108 + R1732 (different aspects) | ~0.3 |
| pathlib-over-ospath | ruff PTH series (different semantic) | ~0.7 |
| argparse-over-sysargv | none | 0 |

A team running `ruff --select PTH,S,FURB` would get incidental coverage on rules 3 and 4 — at the cost of bulk-migration noise (per Great Expectations [23] and napari [24] experiences). The user's import-conditional rules represent a higher-precision, lower-noise approach for the specific "developer chose the right library but slipped" pattern.

## Gaps and limitations

- Refurb's full FURB rule list was inferred from search snippets and one direct fetch [27]. Some FURB rule-IDs may be conditional in ways not surfaced.
- Sourcery's full default rule catalog was only partially scanned — `path-read` was confirmed [31] but `path-write` and any csv/json/argparse-related Sourcery rules were not exhaustively verified.
- pylint's checker source code (refactoring_checker.py) was not inspected directly. Rare or recent pylint messages might cover one of the patterns.
- The "no equivalent in semgrep registry" verdict for rules 1, 2, 5 is based on agent search snippets and the directory listing of `python/lang/best-practice` [33]. Other registry namespaces (`security`, `correctness`) were not exhaustively enumerated.
