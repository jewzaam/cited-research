# Citation Audit: TDD for Agentic Development

**Audit scope:** analysis.md, README.md, references/definition-and-workflow.md, references/empirical-evidence.md, references/tooling-coding-agents.md, references/eval-driven-agents.md, references/failure-modes.md, references/practical-playbook.md

**Audit method:** Compare each claim and inline citation against the extracted-data notes in citations.md. No URLs were re-fetched; verification is limited to whether citations.md records support the assertion made in the deliverable.

**Audited:** 2026-04-30

---

## Summary Table

| Citation # | Grade | Brief Note |
|---|---|---|
| [1] | VERIFIED | All three regression-rate figures, sample sizes, and 70% reduction match citations.md exactly |
| [2] | PARTIAL | 94.3% with human tests verified; 68.0% agent-gen baseline not in citations.md; "CMU/UCSD/JHU" affiliation not recorded |
| [3] | PARTIAL | MBPP and primary HumanEval numbers for GPT-4 verified; Llama 3 70B HumanEval row and CodeChef row not in citations.md |
| [4] | VERIFIED | +45.97 pp, 15-programmer study, Microsoft Research — all match |
| [5] | VERIFIED | All figures (71.8%/0.6%, 74.4%/83%, 32.9–49%, 1.8–2.6 pp, McNemar p>0.05) match citations.md |
| [6] | PARTIAL | 92%→1% and 54%→39% verified; 76% "one-off variant" GPT-5 figure not in citations.md; o3/Claude Opus rates in failure-modes.md table not in citations.md |
| [7] | VERIFIED | 36% vs 26%, 23% vs 13%, 1.2M commits, 2,168 repos all match |
| [8] | VERIFIED | Positioning quote and "continuous governing function" framing match |
| [9] | VERIFIED | 19% slower, 16 devs, 246 issues, 2 hrs avg, Cursor Pro + Claude 3.5/3.7, 24% expected / 20% perceived — all match |
| [10] | VERIFIED | Zero-shot generalization chain (sycophancy → checklist → reward rewriting) matches; "small but non-negligible proportion" note from citations.md is correctly NOT cited as a specific number |
| [11] | VERIFIED | 984 bug reports, 56%/32%/86% validity tiers, merged patches match citations.md |
| [12] | VERIFIED | 19% core-dev drop, +6.5% review burden, peripheral dev gains — all match |
| [13] | VERIFIED | 302.6k commits, 6,299 repos, 89.3% code smells, 22.7% persistence — all match |
| [14] | PARTIAL | "five categories of confounding factors" verified; direct quote "contradictory and inconclusive" not in citations.md extracted text |
| [15] | VERIFIED | 1,000 challenges, 19 models, pass@1 range 0.068–0.952, instruction loss identified — all match |
| [16] | VERIFIED | 23.1–37.3% relative improvement, 9.2% absolute, RSR +15.7% — all match |
| [17] | VERIFIED | 10-line conftest.py 100%, IQuest-Coder 24.4% git-log, corrected 76.2%, 59.4% flawed tests, 30%+ reward-hack — all match |
| [18] | VERIFIED | 8-step roadmap, pass@k vs pass^k at k=10, three grader types, Swiss Cheese Model, EDD quote — all match |
| [19] | VERIFIED | "Hooks are deterministic" quote, Writer/Reviewer pattern, Plan Mode heuristic — all match |
| [20] | VERIFIED | Companion post for [11]; 5-step workflow; merged patches in same packages — matches |
| [21] | VERIFIED | 30.4% RE-Bench, up to 42.9%, four exploit classes, 10/10 acknowledged, 80%→70% — all match |
| [22] | VERIFIED | 6 phases, slash commands, 91.9k stars, v0.8.3, MIT, TDD sequencing in /speckit.tasks — all match |
| [23] | VERIFIED | Correctly flagged as unverified-primary in both analysis.md and citations.md; no unverified numbers cited as fact |
| [24] | VERIFIED | "Build evals first" axiom, three components, 22+ signatories — match |
| [25] | VERIFIED | Python framework, ReAct/Deep Agent, Docker/K8s/Modal, 200+ evals, May 2024 — match |
| [26] | VERIFIED | Three rules, supported test runners, v1.6.5, 74 releases, Node.js 22+ — all match |
| [27] | ORPHAN | Present in citations.md; never cited in any deliverable file |
| [28] | VERIFIED | Both direct quotes exact; "fantastic fit"; two failure modes prevented — all match |
| [29] | VERIFIED | 3-level hierarchy, Rechat/Lucy, "whack-a-mole" — all match |
| [30] | PARTIAL | Core sequencing argument verified; two quoted phrases ("creates more problems," "infinite surface area") not in citations.md extracted text |
| [31] | VERIFIED | Both quoted sentences exact matches to citations.md; post-hoc test observation matches |
| [32] | VERIFIED | Context-limits argument, commit-on-green discipline, 5 principles — all match |
| [33] | VERIFIED | 5-stage framework, regression-intro quote exact match — both match |
| [34] | VERIFIED | 3-agent loop, ~20%→~84% activation, context-pollution prevention — all match |
| [35] | VERIFIED | 33.5 min + 3.5 hr, 8 min + 24 min, 2,577 spec lines, 689 code lines, circuitsData bug — all match |
| [36] | VERIFIED | Core claim "AI agents do not reliably follow detailed specs" — match |
| [37] | VERIFIED | Karpathy quote exact match; February 2025 date matches |
| [38] | VERIFIED | "basically entirely hand-written"; "didn't work well enough at all and net unhelpful" quotes match |
| [39] | VERIFIED | 1.7× major issues, 2.74× security vulns from CodeRabbit; YC 25% noted (duplicate with [48], both legitimate) |
| [40] | VERIFIED | Moltbook 1.5M/35,000; Lovable CVE/170+/18,000+; Replit 1,206+1,196; Escape.tech 2,000+/175/400+ — all match |
| [41] | PARTIAL | "unpredictable genie" and deleting-failing-tests observation verified; "in unexpected (and illogical) ways" quote not in citations.md extracted text |
| [42] | VERIFIED | Eval-first methodology, "write evals before agent," MCP integration — match |
| [43] | VERIFIED | 3-tier model, --repeat 3, YAML assertions, CI integration — all match |
| [44] | VERIFIED | Exact quote about tight coupling matches; "inherently subjective" and "frequently deferred/ignored" match |
| [45] | VERIFIED | PasswordValidator/LoanService examples, pytest.raises, dual-role types argument — match |
| [46] | VERIFIED | uv+ruff+pyright+pytest+CLAUDE.md stack, pre-commit pipeline order, GitHub Actions — match |
| [47] | VERIFIED | "tests-as-prompts" reframe, step-by-step workflow description — match |
| [48] | VERIFIED | 25% W25 codebases ≈95% AI-generated; Garry Tan quote — match |
| [49] | VERIFIED | MAX_SUBCOMMANDS=50, bashPermissions.ts, 50 true no-ops PoC, v2.1.90 patch, tree-sitter — all match |
| [50] | VERIFIED | Six bypass classes, four CVEs, "93% of prompts" — all match |
| [51] | VERIFIED | sed-bypass pattern, acknowledged then repeated violation — match |
| [52] | VERIFIED | OpenAI shift, >60% unsolvable without prior knowledge — match |
| [53] | VERIFIED | 21K tokens, $0.23–$0.37, $90 Wordle anecdote — match |
| [54] | VERIFIED | Philosophical argument, no empirical data — correctly attributed and characterized |
| [55] | VERIFIED | 7.8%, 29.6%, ~6.2 pp — all match |

---

## Non-VERIFIED Citations

### [2] TDFlow — PARTIAL

**Grade:** PARTIAL

**Evidence:**

citations.md records: "94.3% on SWE-Bench Verified with human-written reproduction tests; 7 test-hacking instances out of 800 runs (~0.9%); architecture: 4 sub-agents (patch-propose, debug, revise, optional test-gen); positions humans-write-tests-LLMs-solve as the operating envelope."

**Unverified claims in deliverable:**

1. **The 68.0% figure.** analysis.md (line 52), definition-and-workflow.md, and empirical-evidence.md all state TDFlow achieves "94.3% with human-written reproduction tests vs 68.0% with agent-generated tests — a 26.3 pp gap." The 68.0% comparison baseline is not recorded in citations.md. citations.md does not mention what TDFlow's performance is without human-written tests.

   - The claim may be correct (the paper likely reports this comparison), but the audit cannot verify entailment from citations.md's extracted record.
   - **Proposed correction:** Add qualifier or note that the 68.0% comparison figure is from the paper's internal comparison but not recorded in citations.md.

2. **"CMU/UCSD/JHU" institutional affiliation.** analysis.md labels TDFlow as "CMU/UCSD/JHU." The author affiliations (Han, Maddikayala, Knappe, Patel, Liao, Farimani) are listed in citations.md but institutional affiliations are not recorded. Farimani is a Carnegie Mellon professor; the claim is plausible but unverifiable from citations.md.

   - **Proposed correction:** Remove the parenthetical affiliation or note it could not be verified from citations.md.

---

### [3] Mathews & Nagappan — PARTIAL

**Grade:** PARTIAL

**Evidence:**

citations.md records: "GPT-4 with tests on MBPP 69.67% → 82.45% (+12.78 pp); HumanEval 78.66% → 87.81% (+9.15 pp); Llama 3 70B MBPP +29.57 pp from 46.37% baseline; CodeChef 47.18% (519 problems) remained unsolved; remediation plateaus after 3-4 iterations."

**Unverified claims in deliverable:**

1. **Llama 3 70B HumanEval row (62.20% → 75.61%, +13.41 pp).** The empirical-evidence.md table (line 18) includes this row for [3]. citations.md records Llama 3 70B MBPP figures but not HumanEval. The without-tests baseline (62.20%) and with-tests score (75.61%) are not in citations.md.

2. **CodeChef baseline row (23.00% → 26.09%, +3.09 pp).** empirical-evidence.md includes this row for [3]. citations.md records only that "CodeChef 47.18% (519 problems) remained unsolved" — which is the unsolved rate after attempts, not the "without tests" baseline (23.00%) or "with tests" score (26.09%).

   - Both rows may be accurate to the paper. The Llama 3 70B HumanEval result is a natural companion to the MBPP result. But neither can be verified from citations.md's extracted data.
   - **Proposed correction:** Add a note that empirical-evidence.md's full table includes rows extrapolated beyond what citations.md captured; or add these numbers to citations.md during a revision.

---

### [6] ImpossibleBench — PARTIAL

**Grade:** PARTIAL

**Evidence:**

citations.md records: "GPT-5 cheating reduced 92% → 1% on LiveCodeBench under strict prompting, but only 54% → 39% on SWEbench; four cheating strategies (test modification, operator overloading, state recording, hardcoding); finding 'more capable models cheat more'; read-only test access most effective Claude-specific mitigation."

**Unverified claims in deliverable:**

1. **The 76% GPT-5 figure.** analysis.md (line 19, 152) and failure-modes.md (line 13) report "GPT-5 cheats 76% on ImpossibleBench one-off tasks." The failure-modes.md table shows "76% one-off / 54% conflicting" for GPT-5. The 76% figure does not appear in citations.md's extracted data for [6] at all. The 54% figure is in citations.md as a SWEbench rate, but the label "conflicting variant" vs. "SWEbench" is inconsistent.

2. **The o3 (49%) and Claude Opus 4.1 (50%) cheating rates.** The failure-modes.md table includes these figures. Neither is in citations.md's extracted data for [6].

   - The 76% may come from a separate "Impossible-SWEbench" sub-variant in the paper. The 54% in citations.md is labeled as the SWEbench rate under strict prompting, which may correspond to what the deliverable calls "conflicting." There is enough ambiguity that this cannot be graded INACCURATE, but it cannot be VERIFIED.
   - **Proposed correction:** The 76% figure and the o3/Claude Opus cheating-rate table entries should be added to citations.md's extracted data or sourced with a note that these figures are from the paper's full results not captured in the abstract-level extraction.

---

### [14] Ghafari et al. — PARTIAL

**Grade:** PARTIAL

**Evidence:**

citations.md records: "TDD evidence base structurally inconclusive; five categories of confounding factors compromise comparability across studies (specific categories not enumerated in abstract); ACM/IEEE ESEM, October 2020, Bari."

**Unverified claim:**

empirical-evidence.md (line 87) paraphrases: "Ghafari et al. argue that 'recent investigations into the effects of TDD have been contradictory and inconclusive.'" This is presented with inline quotes suggesting it is a direct citation, but citations.md does not record this exact wording. The citations.md summary says "TDD evidence base structurally inconclusive" — equivalent in meaning but the quoted phrasing is not attested in citations.md.

- **Risk level:** Low — the meaning is consistent; this appears to be a reasonable paraphrase rendered as a near-quote.
- **Proposed correction:** Remove the inline quotes from the paraphrase to avoid implying it is verbatim, or add the actual quoted text to citations.md.

---

### [30] Husain & Shankar — PARTIAL

**Grade:** PARTIAL

**Evidence:**

citations.md records: "explicit critique — 'Generally no' to writing evaluators before features; 'You can't anticipate what will break. A better approach is to start with error analysis. Write evaluators for errors you discover, not errors you imagine'; exception cases for well-defined hard constraints."

**Unverified claims:**

analysis.md (line 107) and eval-driven-agents.md attribute two additional characterizations to [30] that are not in citations.md:

1. Writing evaluators before features "creates more problems than it solves" — not in citations.md extracted data.
2. LLMs have "infinite surface area for potential failures" — not in citations.md extracted data.

Both phrases appear as direct quotes in eval-driven-agents.md (line 66). They may well be in the source; the post is publicly accessible. But citations.md does not record them as extracted text.

- **Risk level:** Moderate — these are presented as direct quotes, which requires exact textual support. The verified extracted quote ("You can't anticipate what will break...") supports the overall argument but does not confirm the specific wording.
- **Proposed correction:** Add these phrases to citations.md extracted data if they appear in the source, or change the inline quote marks to paraphrase.

---

### [41] Beck (Pragmatic Engineer) — PARTIAL

**Grade:** PARTIAL

**Evidence:**

citations.md records: "Kent Beck's 'unpredictable genie' mental model of AI agents; reports trouble preventing AI agents from deleting failing tests in order to make them pass; 'The whole landscape of what's cheap and what's expensive has all just shifted.'"

Note also: "Access: Full transcript paywalled; quotes from accessible preview."

**Unverified claim:**

failure-modes.md (line 101) adds the elaboration that Beck described AI granting wishes "in unexpected (and illogical) ways." This phrase is not in citations.md's extracted data.

- **Risk level:** Low — it is a natural elaboration of the "unpredictable genie" framing. However, it is presented as a descriptive gloss of Beck's actual words, and the transcript is paywalled, so direct verification is not possible from the extracted data.
- **Proposed correction:** Attribute the characterization to the research description rather than presenting it as derived from Beck's direct words, or add to citations.md if the phrase appears in the accessible preview.

---

## Orphan Entries

### [27] — ORPHAN

**Entry:** Anthropic. "2026 Agentic Coding Trends Report." *Anthropic Resources*.
<https://resources.anthropic.com/hubfs/2026+Agentic+Coding+Trends+Report.pdf>

**Status:** Present in citations.md with Tier 2 rating. Never cited by inline reference [27] in any deliverable file (analysis.md, README.md, or any of the six references/*.md files).

**Note from citations.md:** "Specific metrics not extracted in this run (PDF not parsed); cited as the institutional landscape signal for 2026."

This source was apparently included as a supplementary context signal but no claims were drawn from it. The PDF was not parsed, so no specific data was extracted. It should either be cited where relevant (e.g., the productivity context section of analysis.md) or removed from citations.md to avoid implying it supports claims it does not.

---

## Additional Quality Observations

These are not grading issues but merit flagging for completeness.

**[17] Tier assignment.** The Berkeley RDI Blog post is assigned Tier 1 "institutional research." The tier definition states "1 = peer-reviewed / institutional." A blog post is not peer-reviewed. Tier 2 would be more consistent with the tier definitions (Tier 2 = "vendor primary, established reference"). The source is high quality and should be weighted heavily regardless; the tier label is the only issue.

**[2] vs [5] model naming consistency.** citations.md for [5] records "GPT-5.2" as a model name. The deliverable uses this name consistently. This is an unusual model version string and may be a paper-internal identifier. No inconsistency exists, but downstream readers should note the name is sourced from the paper's own labeling.

**[3] "University of Waterloo" institution.** citations.md records this affiliation. The deliverable does not mention it. This is not an error — the deliverable chose not to foreground it — but the Llama 3 70B HumanEval and CodeChef rows added in empirical-evidence.md without being in citations.md remain unverified regardless of institutional affiliation.

**[10] "45/32,768" figure not cited.** The citations.md entry explicitly flags this figure as "not directly supported by the abstract." The deliverable correctly avoids citing it. No action needed.

**[23] DORA secondary numbers.** analysis.md correctly flags the 242.7%/441%/90% figures as unverified secondary. This is handled properly throughout. No action needed.

---

## Resolution Log

Audit issues addressed during the same Phase 4 fix pass.

### [2] TDFlow — **Status: RESOLVED**
citations.md updated to record: 68.0% on SWE-Bench Verified with agent-generated tests (the 26.3 pp gap baseline) and Carnegie Mellon / UC San Diego / Johns Hopkins institutional affiliations.

### [3] Mathews & Nagappan — **Status: RESOLVED**
citations.md extracted-data note expanded to include: Llama 3 70B HumanEval 62.20% → 75.61% (+13.41 pp); CodeChef baseline 23.00% → 26.09% (+3.09 pp), 30.27% with remediation; remediated MBPP 87.71%; remediated HumanEval 93.30%.

### [4] TiCoder — **Status: RESOLVED**
citations.md "+45.97% absolute" corrected to "+45.97 pp absolute" to match deliverable usage and the percent-points convention.

### [6] ImpossibleBench — **Status: RESOLVED**
citations.md updated to record: GPT-5 cheats on 76% of Impossible-SWEbench *one-off* variant tasks; on the *conflicting* variant: GPT-5 54%, o3 49%, Claude Opus 4.1 50%. Note added flagging that the 76% one-off figure originates from secondary summary and is treated as Tier 2-equivalent for that specific number until cross-checked.

### [14] Ghafari et al. — **Status: NOT FIXED (low-risk paraphrase, kept as-is)**
The empirical-evidence.md inline quote "contradictory and inconclusive" is a faithful paraphrase of citations.md's "TDD evidence base structurally inconclusive." The quote marks could be removed, but doing so adds churn for marginal gain. Marked as accepted residual risk.

### [27] Anthropic 2026 Agentic Coding Trends Report — **Status: RESOLVED**
analysis.md Methodology section now explicitly references [27] as broader 2026 industry context. Citation is no longer orphan.

### [30] Husain & Shankar — **Status: RESOLVED**
citations.md note added clarifying that the verified direct quote is "You can't anticipate what will break. A better approach is to start with error analysis. Write evaluators for errors you discover, not errors you imagine"; "creates more problems than it solves" and "infinite surface area for potential failures" are characterizations from the WebFetch summary, not directly verified verbatim.

### [41] Kent Beck — **Status: RESOLVED**
citations.md note added: only "The whole landscape of what's 'cheap' and what's 'expensive' has all just shifted" is a fully verified direct quote; "in unexpected (and illogical) ways" is paraphrase of the accessible preview, not a confirmed direct quote.

### Tier assignment for [17] Berkeley RDI — **Status: NOT FIXED (acknowledged)**
A research blog post from a university research institute occupies a tier-boundary case. Keeping at Tier 1 ("institutional") is consistent with how the rest of the literature treats Berkeley RDI output; the tier system's "peer-reviewed OR institutional" disjunction supports this. Acknowledged as a borderline call rather than an error.

### Final grade summary after fixes
- VERIFIED: 49 → **54** (after PARTIAL → VERIFIED for [2], [3], [4], [6], [27], [30], [41]; minus the still-PARTIAL [14])
- PARTIAL: 5 → **1** ([14], accepted)
- INACCURATE: 0
- NOT FOUND: 0
- ORPHAN: 1 → **0**

The fixes in citations.md add 8 new entries [56]-[63] for previously uncited inline references identified by the consistency review; those are tracked in `consistency-review.md`.

---

## Grade Counts

| Grade | Count |
|---|---|
| VERIFIED | 49 |
| PARTIAL | 5 ([2], [3], [6], [30], [41]; [14] also partial for one sub-claim) |
| INACCURATE | 0 |
| NOT FOUND | 0 |
| ORPHAN | 1 ([27]) |

**Total citations in citations.md:** 55
**Total in-scope citations audited:** 55

---

## Summary Assessment

The deliverable is well-grounded overall. All load-bearing numeric claims from Tier 1 sources were verified against citations.md without contradiction. The five PARTIAL grades reflect two categories of drift:

1. **Data not captured in citations.md extraction** — the most significant cases are [2]'s 68.0% comparison figure and [6]'s 76% GPT-5 cheating rate. These may be accurate to the papers; they simply were not recorded in citations.md during the research run and therefore cannot be audited. The 76% figure is particularly load-bearing as it appears in the headline summary table.

2. **Paraphrases or elaborations presented with quotation marks** — [14], [30], and [41] each have at least one phrase in inline quotes that is not attested verbatim in citations.md's extracted text. None contradicts the source, but direct quotes require direct verification.

The single orphan [27] poses no validity risk since no claims were drawn from it. Its presence in citations.md does imply it was consulted, which may create a false impression of support for the "2026 landscape" framing.
