# Consistency Review — Video Game Design Fundamentals

**Review date:** 2026-05-10
**Reviewer role:** Independent internal consistency reviewer. No context from the research conversation.
**Files reviewed:** README.md, analysis.md, citations.md, and all seven reference files in `references/`.

**Resolution note (added 2026-05-10):** All 9 issues found by this review were addressed in the same session. Fixes applied:
- C-01: $82B IAP citation in analysis.md changed from [52] to [51].
- C-02: citations.md [43] body now explains the 5,836 vs 5,863 URL/article discrepancy.
- C-03: D30 corrected to D28 in analysis.md TL;DR and failure-modes reference.
- C-04: README METR clause now says "predicting a 24% speedup beforehand and self-reporting a 20% speedup afterward."
- C-05: analysis.md changed Dwarf Fortress duration from "~22 years" to "20+ years and counting since 2002."
- C-06: 6× claim removed from analysis.md and critical-cultural-success.md, replaced with source-supported "smaller than organic" framing.
- C-07: citations.md [34] updated to use "52%" instead of "Half of all developers."
- C-08: critical-cultural-success.md now flags the 30K (Wikipedia [61]) vs 27K (Vice [66]) snapshot difference explicitly.
- C-09: failure-modes-indie-mobile.md table updated to "~79% (14,951 reported)" — removes the implied false multiplication.
**Review scope:** Numerical consistency, citation accuracy, formula validity, completeness, contradiction check, suppressed contradictions, estimation markers, caveat honesty, cross-reference links, and scope fit.

---

## Summary Table

| ID | Severity | File(s) | Check type | One-line description | Status |
|---|---|---|---|---|---|
| C-01 | CRITICAL | analysis.md (line 123), citations.md ([51]/[52]) | Citation accuracy + number | $82B IAP attributed to [52] but [52] says $81B; $82B is from [51] | RESOLVED |
| C-02 | CRITICAL | citations.md ([43]) | Citation accuracy | [43] title URL says 5,836 but citation body and all other files say 5,863 | RESOLVED |
| C-03 | CRITICAL | analysis.md (line 28), failure-modes-indie-mobile.md (line 31) | Numerical consistency | D28 median retention (~0.85%) labelled as "D30" in two places; source [17] measures D28 only | RESOLVED |
| C-04 | MODERATE | README.md (line 15) | Numerical consistency | METR pre-study prediction collapsed to "20% speedup" — drops the actual 24% prediction; 20% is only the post-study self-report | RESOLVED |
| C-05 | MODERATE | analysis.md (line 87), production-process-tiny-teams.md (line 15), citations.md ([26]) | Numerical consistency | Dwarf Fortress duration: analysis says "~22 years"; production reference says "20+ years" (from 2021 article); actual span is ~24 years as of research date 2026 | RESOLVED |
| C-06 | MODERATE | analysis.md (line 137), critical-cultural-success.md (line 51) | Completeness / orphan claim | "~6× more effective than sponsored" — stated in both files with no citation number; [68] only says "organic streams increase players ~3%" | RESOLVED |
| C-07 | MINOR | citations.md ([34]) | Numerical consistency | Citation [34] text says "half of all developers" but disciplines-solo-duo-with-ai.md and analysis.md correctly say "52%" — minor rounding mismatch in the citation's own text | RESOLVED |
| C-08 | MINOR | citations.md ([61]), critical-cultural-success.md (line 75) | Numerical consistency | Vampire Survivors concurrent players: [61] says "30,000+" by late Jan 2022; critical-cultural-success.md says "27,000+" "within weeks" — numbers from different sources ([61] vs [66]); no contradiction flagged | RESOLVED |
| C-09 | MINOR | failure-modes-indie-mobile.md (line 11) | Formula validity | 79% × 18,945 = 14,966, not 14,951. The 14,951 is from SteamDB directly; 79% is the rounded ratio 14,951/18,945 = 78.91%. The table presents "79% (~14,951 of 18,945)" implying 79% × 18,945 = 14,951, which does not compute. | RESOLVED |
| C-10 | MINOR | analysis.md, references | Scope fit | Stack Overflow 84% AI adoption [31] and METR study [29] cover general software developers, not game devs. Both files correctly flag this with caveats; no silent scope drift. | PASS |

---

## Verified Items

The following were checked and found consistent across all relevant files:

- **$249 median gross / $174 net** — consistent in README, analysis.md, citations.md [42], commercial-success reference, failure-modes reference.
- **66% under $1K, 90% under $50K, 0.5% over $1M** — consistent across README, analysis.md, citations.md [42], commercial-success reference.
- **79% "Limited" Steam 2024** — consistent across README, analysis.md, citations.md [77], failure-modes reference.
- **83% mobile games fail within 3 years** — consistent across README, analysis.md, citations.md [73], failure-modes reference.
- **-95% sponsored Twitch ROI** — consistent across README, analysis.md, citations.md [68], critical-cultural-success reference, commercial-success reference.
- **~0.5% indie financial viability** — consistent across README, analysis.md, citations.md [60], failure-modes reference, commercial-success reference.
- **10.76% zero dark patterns** and **96.8% of "dark" games F2P** — consistent in README, analysis.md, citations.md [14], player-psychology reference.
- **METR: 19% longer, n=16, 246 issues, Cursor+Claude 3.5/3.7** — consistent in analysis.md, production-process reference, disciplines reference, citations.md [29].
- **METR pre-study: 24% predicted; post-study self-report: 20%** — consistent in analysis.md and both reference files (README is the exception, flagged as C-04).
- **54.83% SDT descriptive-only, 259 papers reviewed (Tyack & Mekler)** — consistent in analysis.md, citations.md [12], player-psychology reference.
- **Flow: 24 operationalizations across 42 studies** — consistent in analysis.md, citations.md [20], player-psychology reference.
- **Quantic Foundry: 1.75M+ players, 12 motivations, 6 clusters** — consistent in analysis.md and player-psychology reference; citations.md [16] notes "140K+ (later 1.75M+)".
- **Tower of Guns: 3,850 hours, 600 days, 983 hours marketing (≈25%)** — consistent across analysis.md, citations.md [23], production-process reference, disciplines reference, README.
- **Last Humble Bee: 9-month estimate / 27-month actual** — consistent in analysis.md, citations.md [22], production-process reference.
- **Stardew Valley: ~5 years, 50M+ copies** — consistent in analysis.md, citations.md [25], production-process reference, critical-cultural-success reference.
- **Hades: Metacritic 93, 700K EA, 300K in three days, ~1M+** — consistent in analysis.md, citations.md [62], critical-cultural-success reference.
- **Balatro: 5M copies by Jan 2025** — consistent in analysis.md, citations.md [64], critical-cultural-success reference.
- **SAG-AFTRA: 95.04% ratification, ~2,600 workers** — consistent in analysis.md, citations.md [37], disciplines reference.
- **GameAnalytics D28 median: ~0.85%; D7: 3.42–3.94%; D1: ~15%** — consistent in citations.md [17], player-psychology reference table, analysis.md section 2 paragraph, analysis.md failure modes bullet, and README. (D30 labelling errors tracked separately as C-03.)
- **Match D30: 7.15%; Hyper-casual D30: 1.38% → ~5× difference** — consistent in citations.md [18], player-psychology reference, analysis.md; formula verified (7.15/1.38 = 5.18× ≈ 5×).
- **Median wishlist conversion: 0.15× (25K+ wishlists)** — consistent in analysis.md, citations.md [46], commercial-success reference.
- **7,000 wishlist threshold** — consistently described as "approximate Steam Popular Upcoming threshold" across README, analysis.md, commercial-success reference.
- **Stegosaurus tail: Lethal Company 507×, Class of '09 106×, Pizza Tower 22.5×, median 2.64×** — consistent in citations.md [50], commercial-success reference, critical-cultural-success reference.
- **Long tail median: Year 1 = 4×, Year 5 = 8.77×, EA Year 5 = 20.34×** — consistent in citations.md [49], commercial-success reference, critical-cultural-success reference.
- **F2P: 2.3% of players spend; top 10% of payers = 64% of revenue** — consistent in analysis.md, citations.md [55], commercial-success reference.
- **Tencent full-year 2024: $6.2B** — consistent in analysis.md, citations.md [57], commercial-success reference.
- **Tencent H1 2024: $3.2B** — consistent in citations.md [56], commercial-success reference.
- **Appodeal ARPU: Hypercasual $0.86, Match $2.99, Merge-3 $14.83** — consistent in analysis.md, citations.md [53], commercial-success reference.
- **Metacritic 90+ → ~800K copies; 80–89 → ~250K** — consistent in analysis.md, citations.md [70], critical-cultural-success reference.
- **Internal markdown links in reference files** all use `../citations.md` (correct for one directory down). analysis.md uses `citations.md` (correct, same directory). README uses `citations.md` (correct).
- **SDT three needs: autonomy, competence, relatedness** — characterized consistently in analysis.md, player-psychology reference, and citations.md [11].
- **Planet Centauri 130K wishlists / 581 units** — correctly marked "secondary-attested, unverified at audit" in both failure-modes reference and citations.md. Consistent.
- **The Wreck: RPS Bestest Best, ~20K wishlists, ~1,000 sales** — consistent in analysis.md, citations.md [83], commercial-success reference, failure-modes reference.
- **GDC 2025: 36% personally use gen AI, 30% believe it harms industry, n=3,000+** — consistent in analysis.md, citations.md [32], disciplines reference, production-process reference.
- **Google Cloud [33]: 90% "AI in workflows", n=615** — consistent in analysis.md, citations.md [33], disciplines reference. Caveat about survey design applied consistently.

---

## Detailed Issue Reports

### C-01 — CRITICAL: $82B IAP attributed to [52] but [52] says $81B

**Status:** OPEN

**File:** `analysis.md`, line 123

**Affected text:**
> "Mobile is bigger but more concentrated: $82B IAP in 2024, but **top 1% of publishers generate 90%+ of store revenue** [52]."

**Expected:** The $82B figure should be attributed to [51] (Sensor Tower "State of Mobile Gaming 2025"), which explicitly states "$82B IAP revenue from mobile games in 2024." Citation [52] (Sensor Tower "$150 Billion Spent on Mobile") says "$81B IAP."

**Actual:** The combined sentence's single citation [52] is used to support both the $82B IAP figure (from [51]) and the 90%+ concentration figure (from [52]). The $82B is mislabelled.

**Detail:** The commercial-success reference correctly treats both numbers as coming from [51] and [52] together: "Mobile game IAP revenue: $82B in 2024 (+4% YoY); $81B in 2025 (flat)" — attributing [51] for the 2024 figure and [52] for the 2025 figure. The $1B discrepancy between the two Sensor Tower reports is not a fabrication but a genuine difference between two Sensor Tower publications; analysis.md should cite [51], [52] together and acknowledge the minor discrepancy.

**Fix:** Change "[52]" to "[51], [52]" and note the $1B difference between sources, or attribute $82B to [51] and 90% concentration to [52] separately.

---

### C-02 — CRITICAL: Citation [43] URL slug says 5,836 but citation body says 5,863

**Status:** OPEN

**File:** `citations.md`, entry [43]

**Affected text:**
> [43] ... "Valve says 5,836 titles earned over $100,000 on Steam in 2025." ... **5,863 games earned $100,000+ in 2025**

**Expected:** The figure should be internally consistent. All reference files and analysis.md use 5,863.

**Actual:** The article title (embedded in the URL slug) says 5,836. The citation body says 5,863. The discrepancy may reflect a correction in the article body after publication, or the citation body extracted the wrong figure from the article.

**Impact:** All consuming files (analysis.md, commercial-success reference) use 5,863, which matches the citation body. If 5,836 is the correct headline figure (from the article title), all consuming files are wrong by 27.

**Fix:** Verify the Game Developer article at the cited URL. If the article body says 5,863 and the title was an error or rounding, note the discrepancy in the citation. If the article says 5,836, update all downstream references.

---

### C-03 — CRITICAL: D28 median retention labelled as D30 in two locations

**Status:** OPEN

**Files and locations:**

1. `analysis.md`, line 28 (Layer 2 paragraph):
   > "Median mobile **D30** retention is **~0.85%**, not the widely-cited 10% [17]."

2. `references/failure-modes-indie-mobile.md`, line 31:
   > "Mobile retention base rates [17]: median **D30** is **~0.85% across all games.**"

**Expected:** D28 — citation [17] (GameAnalytics 2025) explicitly measures D1, D7, and **D28**, not D30. The data column in the player-psychology reference table is correctly labelled D28. The README table is correctly labelled "Median mobile D28 retention | ~0.85%".

**Actual:** Two files substitute "D30" for "D28", creating a false claim (the actual D30 figure from [17] is not stated; D28 is the deepest cohort day measured).

**Impact:** This is a concrete factual error repeated in a summary context (analysis.md TL;DR) and the failure-modes base-rate section. Readers using the D30 label to compare against "good benchmarks" of D30 ≥ 10% are comparing different time periods, slightly overstating how bad retention is.

**Fix:** Replace "D30" with "D28" in both locations.

---

### C-04 — MODERATE: README collapses METR prediction (24%) and self-report (20%) into one "20% speedup"

**Status:** OPEN

**File:** `README.md`, line 15

**Affected text:**
> "The METR randomized controlled trial found experienced developers **took 19% longer with AI** despite predicting and self-reporting a 20% speedup."

**Expected:** "predicting 24% speedup and self-reporting 20% speedup" — per analysis.md (line 40), production-process reference (line 60), disciplines reference (line 31), and citations.md [29].

**Actual:** "predicting and self-reporting a 20% speedup" — this collapses two distinct numbers (24% pre-study prediction, 20% post-study self-report) into a single "20%", dropping the 24% prediction entirely. The 24% is a substantively different — and arguably more striking — number than the post-study 20%.

**Impact:** Moderate. The structural finding (developers feel faster than they are) is intact, but a reader of the README alone will not see the prediction vs. self-report distinction. Minor misrepresentation of the METR study's methodology.

**Fix:** Update README to "predicting 24% speedup and self-reporting 20% speedup afterward."

---

### C-05 — MODERATE: Dwarf Fortress duration "~22 years" in analysis.md contradicts source and other files

**Status:** OPEN

**Files:**
- `analysis.md`, line 87: "Dwarf Fortress [26] (~22 years, ~711K LoC)"
- `references/production-process-tiny-teams.md`, line 15: "20+ years and counting"
- `citations.md`, [26]: "700,000 lines of code, 20 years" (article title; published 2021, development since 2002)

**Expected:** Consistent duration language anchored to the source.

**Actual:** The source is a 2021 Stack Overflow Blog article titled "20 years." The production reference correctly says "20+ years and counting" (appropriate for a still-ongoing project cited via a 2021 article). Analysis.md says "~22 years" — an unsupported interpolation. As of research date (2026-05-10), development since 2002 is ~24 years, not 22.

**Impact:** "~22 years" is neither the source figure (20), nor a correct extrapolation to 2026 (24). It appears to be an estimate with no stated basis. Moderate severity since the point being made (long project, depth-over-time tradeoff) is not materially affected by 20 vs 22 vs 24.

**Fix:** Replace "~22 years" with "20+ years" to match the cited source and the production reference, or update to "~24 years (as of 2026)" if an extrapolation is intentional and noted.

---

### C-06 — MODERATE: "~6× more effective than sponsored" — no citation in either file

**Status:** OPEN

**Files:**
- `analysis.md`, line 137: "Organic streams ~3% player gain; ~6× more effective than sponsored."
- `references/critical-cultural-success.md`, line 51: "Organic effects are roughly **6× more effective** than sponsored streams."

**Expected:** A citation number (presumably [68] or [69]).

**Actual:** The 6× figure appears in both files without any citation. Citation [68] (Kellogg Insight) says "organic streams increase players ~3%"; it does not state a 6× comparison ratio. Citation [69] (Huang & Morozov, Marketing Science) provides the decay-rate finding (30% per subsequent hour) but no 6× comparison ratio is documented in either citation's extracted data.

**Impact:** The 6× figure may be derived from data in [68]/[69] not extracted into the citation entries, but as presented it is an orphan claim — a specific quantified comparison that cannot be traced to a citation.

**Fix:** Add citation [68] or [69] if the 6× figure is derivable from the published data, or remove the specific multiplier and replace with qualitative language ("substantially more effective").

---

### C-07 — MINOR: Citation [34] body says "half" but files say "52%"

**Status:** OPEN

**File:** `citations.md`, entry [34]

**Affected text in citation:**
> "Half of all developers think AI is bad for the industry per the GDC 2026 follow-up survey."

**Actual figure used in files:** 52% (analysis.md lines 50, 97, 222; disciplines reference line 75).

**Assessment:** "Half" and 52% are directionally consistent. The citation text uses a rounding/paraphrase while the reference files use the precise number. This is a minor internal inconsistency in how the citation records its own extracted data.

**Fix:** Update the citation [34] text from "Half of all developers" to "52% of game industry professionals" to match the specific number used throughout.

---

### C-08 — MINOR: Vampire Survivors concurrent peak — two different numbers from two different sources, not harmonized

**Status:** OPEN

**Files:**
- `citations.md`, [61] (Wikipedia): "Reached 30,000+ concurrent by late January 2022; 70,000+ following month."
- `citations.md`, [66] (Vice): Article title "27,000 People Playing at Once" — same-day spike from 14 to 1,143.
- `references/critical-cultural-success.md`, line 75: "within weeks, 27,000+" — uses the Vice framing.

**Assessment:** The two sources give different peak figures — 27,000 (Vice, article title, January 2022) vs 30,000+ (Wikipedia, late January 2022) vs 70,000+ (Wikipedia, February 2022). These are different time snapshots, not directly contradictory. However, the critical-cultural-success reference uses "27,000+" (the earlier/lower peak from the Vice article) without acknowledging that Wikipedia gives a higher subsequent figure.

**Impact:** Minor. The Vice 27K and Wikipedia 30K+ figures represent different points in the same growth curve, but a reader might interpret "27,000+" as the peak when a higher concurrent was reached. No explicit contradiction is stated; the disagreement is not surfaced.

**Fix:** Add a note that the peak climbed further to 30,000+ by late January 2022 and 70,000+ in February 2022 per [61], so "27,000+" is the Vice snapshot, not the final peak.

---

### C-09 — MINOR: Formula check — 79% × 18,945 ≠ 14,951

**Status:** OPEN

**File:** `references/failure-modes-indie-mobile.md`, line 11

**Affected text:**
> "2024 Steam releases classified 'Limited' by Valve | **79% (~14,951 of 18,945)**"

**Formula check:** 79% × 18,945 = 14,966.55 ≈ 14,967. The table implies that 14,951 = 79% × 18,945, but that computation yields ~14,967.

**Actual relationship:** 14,951 / 18,945 = 78.91%, which rounds to 79%. The 14,951 figure is the SteamDB-sourced count; the 79% is the rounded ratio. The denominator 18,945 is a derived/implied total not explicitly stated in citation [77] (which only says "~19,000 new games" in the headline and "~14,951" in the body). The table notation "79% (~14,951 of 18,945)" suggests exact mathematics that does not hold.

**Impact:** Minor. The base finding (roughly 4 in 5 games fail) is accurate. The inconsistency is in the implied precision.

**Fix:** Either note the denominator is approximate ("79% (~14,951 of ~18,945)") or remove the denominator from the table and leave just "79% (~14,951)" as in citation [77].

---

## Contradiction Transparency Assessment

The following known tensions were checked to verify they are surfaced (not suppressed):

| Tension | Surfaced? |
|---|---|
| Scope creep: "killer" vs. "fundamental technique" (Tom Francis [8]) | YES — named explicitly in production-process reference and analysis.md reflection pass |
| Metacritic correlation with sales: bracket-correlation (strong) vs. practitioner counter (weak) vs. ML study (positive but low feature importance) | YES — all three positions are presented in critical-cultural-success reference and analysis.md §6 |
| AI productivity: "accelerates tasks" (Alharthi) vs. "19% slower" (METR) | YES — both explicitly cited; generalizability caveat applied |
| SDT: dominant framework vs. unquestioned paradigm critique | YES — both the foundational paper [11] and the Tyack/Mekler critique [12] are presented |
| "Find the fun" prototyping: orthodox vs. Margaris critique | YES — core-design-fundamentals reference names Margaris and Tom Francis as counter-positions |

---

## Estimation Marker Assessment

The following derived or interpolated figures were checked for labelling:

| Claim | Marked? | Assessment |
|---|---|---|
| "~1,700 of 5,863 are new 2025 titles" | YES — consistently labelled "Carless estimate" not Valve's confirmation | PASS |
| "0.5% financial viability" uses 50× review-multiplier | YES — flagged in analysis.md reflection pass and citations.md [60] | PASS |
| "~22 years" for Dwarf Fortress | NO — not marked as estimate; inconsistent with cited source | FAIL (see C-05) |
| "~6× more effective" for organic vs sponsored streams | NO citation | FAIL (see C-06) |
| 18,945 total 2024 Steam releases | Not present in [77] body; implied by the table calculation | Partially flagged (see C-09) |

---

## Caveat Honesty Assessment

Each reference file was checked for a "Gaps and limitations" section:

| File | Section present? |
|---|---|
| core-design-fundamentals.md | YES |
| player-psychology-engagement.md | YES |
| production-process-tiny-teams.md | YES |
| disciplines-solo-duo-with-ai.md | YES |
| commercial-success-indie-mobile.md | YES |
| critical-cultural-success.md | YES |
| failure-modes-indie-mobile.md | YES |

All reference files have the required section. Analysis.md has an "Open questions and honest gaps" section and a "Reflection pass" section that both perform the caveat function.

---

## Cross-Reference Link Assessment

| Link pattern | Location | Resolves? |
|---|---|---|
| `[citations.md](citations.md)` in analysis.md | Same directory | YES |
| `[../citations.md](../citations.md)` in all reference files | One level up from references/ | YES |
| `references/core-design-fundamentals.md` in analysis.md | Relative path from same directory | YES |
| `[`references/`](references/)` in README.md | Same directory | YES |
| `[audit/](audit/)` in README.md | Same directory | YES |

All internal markdown links use correct relative paths for their locations. No broken cross-reference links found.

---

## Scope Fit Assessment

The deliverable is scoped to "indie/mobile, 1–2 person team with AI augmentation." Scope drift checks:

- **METR RCT [29]** covers general OSS developers, not game devs. Both reference files applying this citation flag the generalizability caveat explicitly. Not a scope drift — correctly scoped as the best available proxy.
- **Stack Overflow [31]** covers all software developers. Flagged in disciplines reference as "general software." Not silent drift.
- **Ma et al. ML study [72]** covers all Steam games. Applied to "Steam specifically" with appropriate framing. PASS.
- **F2P dark pattern findings [14]** cover all mobile games, not just indie. Applied correctly to mobile generally, with indie-specific implications drawn explicitly. PASS.
- **Swrve whale data [55]** is from 2015 and covers all F2P. Correctly caveated ("2015 data; structural pattern persists"). PASS.

Overall scope fit: PASS. Where general-software or AAA-inclusive data is used, the files apply explicit caveats.
