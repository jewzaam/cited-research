# Consistency Review — Memory Poisoning of Agentic AI

Reviewer: Claude Code (claude-sonnet-4-6)
Date: 2026-04-30
Scope: All markdown files in `research/agentic-memory-poisoning/` — README.md, analysis.md, citations.md, references/*.md. No web access; all findings derived from the deliverable files themselves.

This review is independent of the research conversation that produced the files. It does not have access to fetched source files and therefore cannot re-verify primary source claims — it checks *cross-file internal consistency* only. For primary-source verification, see `audit/citation-audit.md`.

---

## Summary Table

| ID | Severity | File(s) | Category | Status |
|----|----------|---------|----------|--------|
| CR-01 | MODERATE | README.md vs analysis.md, persistence-cross-session.md | Numerical inconsistency — 8x vs ~7x amplification | **RESOLVED** |
| CR-02 | MODERATE | citations.md [5] | Wrong citation number — PoisonArena referenced as [13] instead of [31] | **RESOLVED** |
| CR-03 | MODERATE | analysis.md §3 | Formula validity — "order of magnitude" claim not supported by stated numbers | **RESOLVED** |
| CR-04 | MODERATE | README.md, analysis.md, defenses.md | Orphan claim — SecureIQLab has no citation entry | **RESOLVED** |
| CR-05 | MINOR | README.md | Count inconsistency — "six inaccessible" vs three documented in citations.md | **RESOLVED** |
| CR-06 | MINOR | references/defenses.md | Unmarked unverified claim — [36] "YES — independently validated" based on unfetched source | **RESOLVED** |
| CR-07 | MINOR | references/real-world-incidence.md | Cross-contamination — [4]'s realistic-memory drop attributed to MINJA context | **RESOLVED** |
| CR-08 | MINOR | README.md vs citations.md [1] caveats | Rounding inconsistency — EHRAgent poison rate 0.286% vs 0.29% | **RESOLVED** |

**Resolution summary (applied 2026-04-30 after audit):**
- CR-01: README.md headline table caveat updated to acknowledge "8x" is rounded; actual is ~7x.
- CR-02: citations.md [5] caveats updated from "(citation [13])" to "(citation [31])".
- CR-03: analysis.md §3 reworded to apply "order of magnitude" to the correct 62%→6.67% comparison.
- CR-04: New citation entry [41] (SecureIQLab PR Newswire) added; inline [41] markers added in analysis.md, README.md, defenses.md.
- CR-05: README.md updated to "three were inaccessible" matching citations.md documented count.
- CR-06: defenses.md table entry for [36] tagged "(per discovery, unfetched)".
- CR-07: real-world-incidence.md caveat for MINJA reworded to clarify [4] tested its own attack, not MINJA.
- CR-08: citations.md [1] caveats updated from "0.29%" to "0.286%" matching analytical documents.

---

## Issue Detail

### CR-01 — MODERATE: 8x vs ~7x amplification factor inconsistency

**Category:** Numerical inconsistency  
**Files:** README.md line 16; analysis.md line 93; references/persistence-cross-session.md line 20; references/real-world-incidence.md line 59  
**Status:** OPEN

**The problem:**

README.md headline table (line 16):
> "eTAMP demonstrates 19.5%/32.5% ASR with 8x amplification | [3] | Real numbers and amplification factor are correct."

The caveat column says "Real numbers and amplification factor are correct," endorsing the 8x figure as accurate.

analysis.md §4 (line 93):
> "The '8x amplification under UI friction' claim in topics5.md is approximately right: GPT-5-mini 4.6% → 32.5% is **~7x**."

persistence-cross-session.md (line 20):
> "increased GPT-5-mini ASR by ~7x (4.6% → 32.5%). The '8x' figure cited in topics5.md and most secondary coverage is a rounded approximation; the actual amplification is closer to 7x."

**Calculation:** 32.5 ÷ 4.6 = 7.065x. The actual ratio is ~7x, not 8x.

**Verdict:** The README headline table says the amplification factor "is correct" (endorsing 8x), while analysis.md and the reference file both explicitly correct it to ~7x and call 8x an approximation. These three files contradict each other. The analysis.md and reference file are internally consistent with the arithmetic. The README is not.

**Expected:** README caveat should say "8x is a rounded approximation; actual ratio is ~7x" — consistent with analysis.md and persistence-cross-session.md.  
**Actual:** README says "amplification factor are correct" with no qualification.  
**Grade:** FAIL

---

### CR-02 — MODERATE: Wrong citation number for PoisonArena in citations.md [5]

**Category:** Citation accuracy  
**File:** citations.md, line 53 (under [5] PoisonedRAG entry)  
**Status:** OPEN

**The problem:**

citations.md [5] caveats block (line 53):
> "The PoisonArena results separately show ASR collapses to ~0% under multi-attacker competition (citation [13])."

[13] in citations.md is the **OWASP Agentic Top 10 announcement** (URL: genai.owasp.org/2025/12/09/...). PoisonArena is listed as **[31]** (URL: poison-arena.github.io).

Every other reference to PoisonArena in the deliverable correctly uses [31]:
- analysis.md line 78: "PoisonArena [31, per discovery]"
- references/agentpoison-attacks.md line 63: "PoisonArena [31, per discovery, unfetched]"

**Verdict:** The "[13]" in citations.md [5] caveats is a citation number error. It appears nowhere else; the analytical documents use the correct [31].

**Expected:** "(citation [31])"  
**Actual:** "(citation [13])"  
**Grade:** FAIL

---

### CR-03 — MODERATE: "Order of magnitude" claim not supported by stated numbers in analysis.md

**Category:** Formula validity  
**File:** analysis.md, line 76  
**Status:** OPEN

**The problem:**

analysis.md §3 (line 76):
> "Authors' best-case figures under realistic retrieval parameters: 38% (GPT-4o-mini), 28% (Llama). Roughly an order of magnitude below the empty-memory headline."

The "empty-memory headline" figures from the table immediately above (line 71–74) are 62% for GPT-4o-mini and "high (99.95% ISR)" for Llama.

Calculation: 38% ÷ 62% = 0.61 (a 1.6x ratio). This is not "roughly an order of magnitude" (which would require ~10x, i.e., the realistic figure being ~6.2% or below).

The "order of magnitude" characterization IS mathematically defensible for the pre-existing-memories row: 6.67% ÷ 62% = 0.107, a 9.3x drop. The companion reference file (agentpoison-attacks.md, line 59) correctly applies the phrase to the 62% → 6.67% comparison, not to the 38%/28% figures.

In analysis.md, "order of magnitude" is applied to the wrong pair of numbers. The sentence structure places "roughly an order of magnitude" immediately after "38% (GPT-4o-mini), 28% (Llama)" — those numbers are not an order of magnitude below 62%.

**Verdict:** Mathematical error in analysis.md. The agentpoison-attacks.md reference file uses "order of magnitude" correctly (for the 62% → 6.67% comparison). analysis.md applies it to a different, larger-scale reduction (38%) where the claim does not hold.

**Expected:** The "order of magnitude" characterization should follow the 6.67% / 0% row, not the 38% / 28% best-case row. Or the characterization should be removed from analysis.md §3 for the best-case figures and replaced with an accurate description (e.g., "roughly half the empty-memory rate").  
**Actual:** "Roughly an order of magnitude below the empty-memory headline" applied to 38%/28% vs 62%.  
**Grade:** FAIL

---

### CR-04 — MODERATE: SecureIQLab claim is an orphan — no citation entry

**Category:** Completeness / orphan claim  
**Files:** README.md line 32; analysis.md lines 17, 137, 197; references/defenses.md line 76  
**Status:** OPEN

**The problem:**

SecureIQLab is cited in four locations with specific factual claims:
- defenses.md: "begins testing **20 AI firewall vendors** that month, with results targeted for **Black Hat USA 2026 (~August 2026)**"
- analysis.md: "SecureIQLab independent validation only begins April 2026 with results expected August 2026"
- README.md: "SecureIQLab's August 2026 independent validation results"

These are specific, verifiable facts: named organization, count of vendors tested (20), start date (April 2026), target conference (Black Hat USA 2026, ~August 2026).

No entry for SecureIQLab appears anywhere in citations.md. There is no [N] citation number attached to the name in any of the four files.

**Verdict:** SecureIQLab claims are unanchored to any citation. Per the deliverable's own methodology, every factual claim should trace to a reference file and citation. The SecureIQLab statement is a high-stakes claim (operators are told to "discount vendor claims until SecureIQLab results land") with no traceable source.

**Expected:** A citation entry in citations.md and an inline citation [N] in all four files.  
**Actual:** No citation entry; no inline citation marker.  
**Grade:** FAIL

---

### CR-05 — MINOR: README count "six inaccessible" vs three documented in citations.md

**Category:** Count inconsistency  
**File:** README.md line 46  
**Status:** OPEN

**The problem:**

README.md (line 46):
> "33 primary sources were directly fetched and persisted; six were inaccessible (HTTP 4xx or PDF binary)."

citations.md documents three sources explicitly in its "Inaccessible / unverified sources" section:
- [28] IBM Think — HTTP 403
- [29] VentureBeat — HTTP 429
- [30] Microsoft whitepaper PDF — binary content

Additionally, [16]'s caveats mention the companion PDF URL returned binary content (but this is documented as part of [30], not a separate source). No other inaccessible sources are documented.

The gap between "six" and three (documented) is unexplained. The remaining three inaccessible sources are not named anywhere in citations.md.

**Verdict:** The README's methodology claim of "six inaccessible" cannot be reconciled with the three explicitly documented inaccessible entries in citations.md. Either the count is wrong, or three additional inaccessible sources were not documented.

**Expected:** Count in README matches the number of explicitly documented inaccessible sources in citations.md.  
**Actual:** README says 6; citations.md documents 3.  
**Grade:** FAIL (count mismatch, but does not affect analytical conclusions)

---

### CR-06 — MINOR: Defenses table marks [36] as "YES — independently validated" without qualification

**Category:** Unmarked estimate / epistemic status  
**File:** references/defenses.md, line 74  
**Status:** OPEN

**The problem:**

defenses.md (line 74, in the vendor self-report table):
> "Microsoft Azure Prompt Shield | (broken at 100% evasion) | Independent academic [36] | YES — broken"

[36] (Bypassing LLM Guardrails, Hackett et al.) is listed in citations.md under "Additional sources referenced by discovery agents (not directly fetched)" with the tag "per discovery agent." It was not fetched in this session.

Every other "YES" or "NO" in the independent validation column either reflects primary-fetched sources or appropriately tagged per-discovery claims. The [36] entry is the only "YES — independently validated" result in the table — and it rests on an unfetched source.

This is acknowledged in the accompanying citation-audit.md (issue #1 in Key Findings), which calls this "the highest-stakes use of a discovery-only citation in the deliverable." The defenses.md file itself does not flag the epistemic limitation.

**Expected:** "YES (per discovery, unfetched) — broken [36]"  
**Actual:** "YES — broken [36]" without qualification  
**Grade:** FAIL (acknowledged in citation-audit.md but not corrected in the source file)

---

### CR-07 — MINOR: real-world-incidence.md implies [4]'s realistic-memory drop applies to MINJA

**Category:** Cross-contamination between papers  
**File:** references/real-world-incidence.md, line 61  
**Status:** OPEN

**The problem:**

real-world-incidence.md (line 61), in the "Lab claims that should not be cited as production data" table:
> `"MINJA >95% ISR" | [38, per discovery] | Lab — and arXiv 2601.05504 [4] shows this drops to <10% with realistic memory`

The caveat column says [4] shows MINJA's ISR "drops to <10% with realistic memory." However, [4] (Devarangadi Sunil et al.) tests its own attack method against populated memory stores — it does not test MINJA specifically. MINJA's behavior under populated-memory conditions is unknown from any fetched source.

This same cross-contamination was flagged in citation-audit.md (Key Finding #2) for analysis.md, but the real-world-incidence.md instance was not corrected.

**Expected:** Caveat should say "[4] shows its own attack drops to 6.67% with realistic memory; MINJA's behavior under populated-memory conditions is untested."  
**Actual:** Implies [4]'s realistic-memory finding applies to MINJA.  
**Grade:** FAIL

---

### CR-08 — MINOR: EHRAgent poison rate rounding inconsistency

**Category:** Numerical consistency (rounding)  
**Files:** citations.md [1] caveats; README.md line 15; analysis.md line 63; references/agentpoison-attacks.md lines 35, 45  
**Status:** OPEN

**The problem:**

The computed value is 2 ÷ 700 × 100 = 0.28571...%

| File | Value stated |
|------|-------------|
| citations.md [1] caveats | "2/700 = **0.29%**" |
| README.md | "EHRAgent poison rate is **0.286%**" |
| analysis.md | "2 poisoned instances in a 700-document corpus is **0.286%**" |
| agentpoison-attacks.md (computation) | "EHRAgent **2/700 = 0.286%**" |
| agentpoison-attacks.md (table) | "0.087–**0.286%**" |

citations.md rounds to 2 decimal places (0.29%), while all analytical documents use 3 decimal places (0.286%). Both are arithmetically correct for different precision levels. The citation-audit.md confirms the source file itself uses "0.29%."

This is a presentation inconsistency rather than an error, but a reader comparing citations.md to the analytical documents will see different numbers.

**Expected:** Uniform rounding (either 0.286% or 0.29%) across citations.md and the analytical documents.  
**Actual:** 0.29% in citations.md; 0.286% in README.md, analysis.md, agentpoison-attacks.md.  
**Grade:** FAIL (minor — both are arithmetically correct)

---

## Items Verified Consistent

The following claims were checked and found consistent across all files that reference them.

**Numerical consistency:**
- eTAMP ASR table (GPT-5-mini 4.6%→32.5%, GPT-5.2 1.8%→23.4%, GPT-OSS-120B 19.5%, Qwen3.5-122B-A10B 1.8%→12.0%): consistent across citations.md [3], analysis.md §4, persistence-cross-session.md.
- eTAMP premature trigger ASRA = 0% on most models, exceptions Qwen3.5-122B 0.35%, Qwen3-VL-32B 0.71%: consistent across citations.md [3] and persistence-cross-session.md.
- AgentPoison ASR-r/ASR-t per-agent table (Agent-Driver 80.0%/56.8%/23,000/20; ReAct 65.5%/58.6%/10,000/4; EHRAgent 98.9%/58.3%/700/2): consistent across citations.md [1], analysis.md §3, agentpoison-attacks.md.
- Average ASR-t ~58% (56.8+58.6+58.3)/3 = 57.9%: consistent claim across README.md and analysis.md.
- Memory dilution 62% (empty) → 6.67% (populated) for GPT-4o-mini; Llama 0%: consistent across citations.md [4], analysis.md, agentpoison-attacks.md, persistence-cross-session.md.
- Best-case figures 38% (GPT-4o-mini) / 28% (Llama): consistent across citations.md [4], analysis.md, persistence-cross-session.md.
- Microsoft 50 examples / 31 companies / 60 days: consistent across citations.md [15], README.md, analysis.md, real-world-incidence.md, intersection-with-bias.md.
- $340K/year [26] and 9.5 GPU-years [27]: consistent across README.md, analysis.md, operator-playbook.md.

**Citation accuracy:**
- [2] Morris-II: "every five emails" propagation — consistent everywhere, "20 clients per day" correctly repudiated in all files.
- [14] OWASP Agent Memory Guard: Q3 2026 v0.4.0 ML-detection status (not yet released) — consistent across citations.md, analysis.md, defenses.md, threat-taxonomy.md.
- [6] "12 defenses broken to >90% ASR under adaptive attack" — consistent across citations.md, analysis.md, defenses.md.

**Contradiction transparency:**
- [16] vs [30] Microsoft "novel" vs "Existing Security Failures" contradiction: correctly flagged as unresolved in every relevant file (README.md, analysis.md §2, citations.md [16] caveats, citations.md [30], threat-taxonomy.md).
- Unit 42 "66% LLM-detector miss" figure correctly quarantined as discovery agent error in citations.md [19] caveats and operator-playbook.md; does not appear as a substantive claim in any analytical document.
- Anthropic-vs-OpenAI testing-standards claim correctly quarantined as discovery agent error in citations.md [22] caveats and defenses.md; does not appear in analytical documents.

**Structural consistency:**
- Torra & Bras-Amorós [10] three-not-four memory types: correctly handled and cited in analysis.md §2 and threat-taxonomy.md; no file claims four types as a canonical academic source.
- Willison lethal trifecta (3 conditions, not 4): consistent across citations.md [25], analysis.md, multi-agent-propagation.md.
- OWASP ASI06 list (ASI01–ASI10): consistent between citations.md [23] and threat-taxonomy.md.
- All 8 internal markdown links in analysis.md (e.g., `[threat-taxonomy.md](references/threat-taxonomy.md)`) resolve to existing files.
- All 8 reference files link to `../citations.md` using correct relative path.

**Estimation markers:**
- All "per discovery agent, unfetched" qualifiers appear consistently in citations.md [31]–[40] and in the reference files where those sources are used (agentpoison-attacks.md, multi-agent-propagation.md, operator-playbook.md, intersection-with-bias.md).
- [26] $340K/year and [27] $1,500-3,000/month figures: vendor/anecdote caveats in citations.md entries; underqualified in analytical documents (acknowledged in citation-audit.md Key Finding #3).

**Caveat honesty:**
- Every reference file contains a "Gaps and limitations" section explicitly naming what was not measured, unfetched, or unknown.
- The lab-vs-production distinction is consistently applied: no ASR figure is presented as a production measurement without qualification.
- Zero confirmed production incidents with disclosed harm is stated consistently across README.md, analysis.md §9, real-world-incidence.md.

---

## Reconsideration Pass

Before finalizing, reconsidering whether any issue was assessed too leniently or too harshly.

**CR-01 (8x vs ~7x):** The README explicitly says "Real numbers and amplification factor are correct" — this is a definitive endorsement of the 8x figure as accurate, directly contradicted by the arithmetic (7.065x) and the analysis.md text. Could be read as "approximately correct" but the word "are correct" without qualification is the stronger reading. Maintains MODERATE.

**CR-02 (PoisonArena [13] vs [31]):** This is unambiguous. The wrong number appears once, in a caveat block. It does not affect any analytical claim (PoisonArena is correctly cited as [31] in the analytical documents). Maintains MODERATE because a reader consulting citations.md for [13] will find OWASP, not PoisonArena.

**CR-03 (order of magnitude):** The mathematical relationship between 38% and 62% is definitively not "an order of magnitude." The agentpoison-attacks.md reference file applies the same phrase to the correct comparison (62% → 6.67%). The inconsistency is within the analytical documents, not between a document and a source. Maintains MODERATE.

**CR-04 (SecureIQLab orphan):** Five uses of specific factual claims about an organization's study with no citation. The "20 AI firewall vendors" count and "Black Hat USA 2026" are very specific. This is the kind of claim that should have a source. Could be CRITICAL if the details are wrong, but absent a source the reviewer cannot determine that. Maintains MODERATE.

**CR-05 (six vs three inaccessible):** Could the other three be the Springer canonical URL for [11] (returned 303, redirected to PMC), the Microsoft whitepaper counted separately from [30]'s listing, and possibly some other redirect? Without the original session logs this cannot be determined, but the README's claim of six is unverifiable from the delivered files. Maintains MINOR.

No severity changes warranted.
