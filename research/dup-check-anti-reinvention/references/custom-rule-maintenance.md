# Reference: Custom rule-pack maintenance burden

Sources cited inline as `[N]` against [citations.md](../citations.md).

## What this dimension covers

How others maintain custom semgrep / lint rule sets: contribution paths, false positive rates, semgrep version churn, and whether contributing the user's 5 rules upstream is realistic. Added as the Dim 5 the user requested in Phase 0.

## Contribution paths to semgrep-rules — concrete bar

The semgrep contribution docs [67] specify:

- **CLA required.** Contributors must sign the GitHub CLA.
- **Test format**: filename matches rule, ≥1 true positive marked `// ruleid: rule-id`, ≥1 true negative marked `// ok: rule-id`.
- **Quality checker** `semgrep-rule-lints` evaluates conformance.
- **Maintainer approval required.**
- **Best-practice category metadata bar is light**: only `references`, `category`, `technology` required (vs. security category which adds CWE/OWASP/confidence/likelihood/impact/subcategory/vulnerability_class).

The user's 5 rules already have `*.test.py` files matching the test-format expectation. They would fit `python/lang/best-practice/` namespace. The 9 existing rules in that directory [33] (hardcoded-tmp-path, logging-error-without-handling, manual-collections-create, missing-hash-with-eq, open-never-closed, pass-body, pdb, sleep, unspecified-open-encoding) confirm the user's "stdlib-preference" rules are a category-fit.

## The CLA + Semgrep Rules License v1.0 catch

In December 2024 [65], Semgrep transitioned its maintained rules to "Semgrep Rules License v.1.0," which restricts use to "internal, non-competing, and non-SaaS contexts." Contributing to `semgrep/semgrep-rules` means accepting this license — the user grants Semgrep, Inc. a permanent license to relicense contributions.

For a hobbyist contributor, this means:
- The rules become part of Semgrep's commercial offering surface.
- The user cannot relicense their own rule for commercial reuse outside Semgrep without re-implementing it.
- The CLA itself is standard but stacks with the rules-license shift.

## The Trail of Bits external-pack model

Trail of Bits maintains `github.com/trailofbits/semgrep-rules` [68] as a public external pack with ~100+ rules across Go, Python, JavaScript, Ruby, Rust, Swift, HCL, JVM, YAML, and generic patterns. License: AGPLv3.

The pack is **NOT contributed upstream**. Instead, it's indexed in the Semgrep registry, accessed via `semgrep --config "p/trailofbits"`. This avoids the CLA + Semgrep Rules License v1.0 entirely while preserving registry discoverability.

Trail of Bits also published 35 new rules in December 2024 [69] — confirming third-party rule authoring is still active and the ecosystem supports external packs as a first-class distribution model. Their introduction guide [70] explicitly recommends internal repos for org-specific rules and peer review on every new rule before going live.

For 5 Python rules covering stdlib-preference patterns, the ToB model is the obvious match: the user publishes their own GitHub repo with the 5 rules, requests indexing in the Semgrep registry, and retains full ownership.

## Semgrep version churn — the actual risk

The big disruption was December 2024 [65][66], not a syntax change:

- **Renaming**: OSS → Community Edition.
- **Engine features moved to commercial**: The blog [65] confirms "Experimental Features" migrated. Practitioner post-mortem [66] confirms specific features broken in CE: join mode rules, nosemgrep inline suppression for JSON output (only SARIF retained it).
- **Engine itself stayed LGPL 2.1** [65] — the core engine is still open.

Semgrep has been developing an experimental rule syntax separate from the stable v1 patterns [73]. The migration is gradual, not forced — old syntax still works in 2026. **Simple structural rules using `pattern`, `pattern-either`, `pattern-inside` (which is exactly what the user's 5 rules use) are not on the migration path.** The user's rules avoid taint mode, dataflow, cross-function reasoning — they're insulated from the highest-churn surfaces.

The Opengrep fork [72] (January 2025) is rule-format-compatible with Semgrep. The user's rules would run unchanged on Opengrep if Semgrep CE continues regressing. (Windows support was a launch-post roadmap item, not shipped at launch; current status not verified in this session.) The rule-format compatibility itself provides the escape hatch regardless.

## False positive rates for custom rules

Semgrep's official FP-reduction KB [71] explicitly states: "users write a lot of custom internal rules too, and those rules don't go through the same tuning process" as registry rules. Recommended monitoring signal: track `# nosemgrep` suppression rate per rule.

The pattern the user's rules use — gating detection on `import X` being present via `pattern-inside: import csv\n...` — IS the canonical FP-reduction strategy that Semgrep's own docs recommend [71]. Restricting matches to files where the target library is actually in use limits noise to genuine inconsistencies. The user's rules are designed in a way that aligns with Semgrep's FP-management best practice.

For a 5-rule pack of simple structural patterns (no taint, no cross-function, no broad ellipsis matching), the realistic maintenance cost is:
- Re-test on each Semgrep release (low — `semgrep --test` against the existing test files).
- Adjust patterns if the user's codebase evolves new legitimate use of `split(",")`, `os.path.join`, etc. that the rules now flag falsely (low to moderate — has happened once or twice over multi-year periods for similar small packs).
- Eventually migrate to syntax 2.0 if Semgrep deprecates 1.0 (low — the user's patterns map cleanly to the new operators).

## Industry pattern: small public-subset + internal pack

FullStory's announcement [74] documents the common practice: maintain a larger internal rule pack, publish a "subset of the custom rules we use internally" for community benefit. This is the model most companies use — internal rules stay private, polished/general rules go public.

For the user's situation, the 5 rules are general-purpose enough (any Python codebase using these stdlib modules can benefit) that they would be net-additive if published. None of the 9 existing `python/lang/best-practice` rules [33] cover the user's patterns — there's no overlap to negotiate.

## Verdict for Dimension 5

**Maintenance burden is bounded; contribution path is feasible but carries a relicensing cost.**

For ongoing maintenance (option: keep as-is), the 5 rules are at the low end of the cost spectrum — simple structural patterns, insulated from taint/dataflow/syntax 2.0 churn, with built-in test infrastructure already in place.

For contribution upstream (option: PR to semgrep-rules), the technical bar is light (3 metadata fields, existing test files conform), but the CLA + Semgrep Rules License v1.0 [65] mean the user grants permanent relicensing rights. If the user is comfortable with that, the rules fit the `python/lang/best-practice` namespace cleanly [33].

For external-pack distribution (option: own GitHub repo, registry index), the Trail of Bits model [68] is the established pattern — keeps ownership, gets discoverability, no CLA. This is the recommended path if the user wants public visibility without relicensing.

## Gaps and limitations

- Actual PR merge turnaround time for `python/lang/best-practice` contributions in 2024-2025 is undocumented from search — sparse PR history, dominated by bot-driven merges.
- Whether Trail of Bits' GitHub Action sync to the registry requires a Semgrep AppSec Platform account is unclear; the user might be able to register the rule pack without that overhead, but the path is not documented end-to-end.
- Opengrep's current production readiness as a Semgrep alternative was not directly verified in this session.
- The Semgrep Rules License v1.0 text was not directly fetched — claims about "internal, non-competing, non-SaaS" restrictions are quoted from the December 2024 blog [65] rather than from the license itself.
