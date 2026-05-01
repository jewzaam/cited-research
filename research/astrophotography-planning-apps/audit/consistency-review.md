# Consistency Review — Astrophotography Planning Apps & Gap Landscape

Independent internal consistency check. No web access was used. All findings are derived solely from reading
`README.md`, `analysis.md`, `citations.md`, and `references/01–10`. Conducted April 2026.

---

## Summary Table

| # | Severity | File(s) | Issue |
|---|---|---|---|
| F-01 | CRITICAL | `references/09-market-viability.md` | "smart-telescope segment grew 38% YoY in 2023" attributed to [191][193] — neither citation's description supports this figure. **Status: RESOLVED** — claim removed; replaced with the actually-cited 7.8% telescope-CAGR figure from [191] and 5M-amateur-astronomer figure from [193] |
| F-02 | MODERATE | `README.md` | `audit/citation-audit.md` linked as an existing file; directory and file are absent. **Status: STALE** — finding was correct at the time of this review's first pass; `citation-audit.md` was written by the coordinator concurrently with this review and now exists in `audit/`. No fix required. |
| F-03 | MODERATE | `README.md`, `analysis.md` | "$200K-$300K ARR" ceiling for planning-only tools stated as fact without "(est.)" marker; the per-app inferences that underpin it are never summed to produce this figure. **Status: RESOLVED** — narrowed to "~$200K ARR (est.)" with explicit derivation in README.md, analysis.md, and 09-market-viability.md (Astrospheric upper inference $162K + Telescopius ~$29K Patreon) |
| F-04 | MODERATE | `references/09-market-viability.md`, `README.md`, `analysis.md` | "8-9% CAGR" is a blended range of two separate figures (8.2% telescope [193], 8.9% cameras [192]); the blending is not stated. **Status: RESOLVED** — replaced with explicit attribution: "telescope market ~7.8% CAGR per a 2020 paid report [191]; astrophotography-camera market 8.9% CAGR per Verified Market Reports [192]" |
| F-05 | MINOR | `references/02-planning-tools.md` | SkySafari 8 macOS availability asserted with [56][57][58]; [58] is the iOS App Store listing and does not establish macOS. **Status: RESOLVED** — softened to "macOS asserted by the vendor product page [57] but a Mac App Store listing was not retrieved at fetch — treat macOS support as vendor-claimed" |
| F-06 | MINOR | `citations.md` ([209]) | Citation [209] (SkySafari free + Basic App Store data) is never referenced in any claim in analysis.md or any reference file — orphan citation. **Status: RESOLVED** — [209] now cited in 09-market-viability.md SkySafari section ("17,301 reviews, 4.7 stars, 669K+ downloads tracked") |
| F-07 | MINOR | `citations.md` ([176]) | Citation [176] (Telescopius donations page) returned 403 at fetch; the citation is nowhere cited in analysis.md or reference files — orphan citation with disclosure. **Status: RESOLVED** — [176] added to Telescopius row in 08-pricing.md alongside [38][45][46] |
| F-08 | MINOR | `references/09-market-viability.md` | "$50K/yr in years 1-3" appears as a specific projection in the Conclusion without "(est.)" or derivation trace. **Status: RESOLVED** — marked as "(est.; based on early Astrospheric-style conversion at the low end of the inferred range)" in 09-market-viability.md and as "(est.)" in analysis.md Build new section |
| F-09 | MINOR | `analysis.md` | Internal link `[Reference 09](references/09-market-viability.md)` in several places uses relative path; all links verified structurally correct given directory layout — no broken link found, PASS |

---

## F-01 — CRITICAL: "38% YoY in 2023" smart-telescope claim lacks supporting citation

**File:** `C:/Users/jewza/source/cited-research/research/astrophotography-planning-apps/references/09-market-viability.md`

**Section:** Hobby growth trajectory

**Claim:**
> "Telescope unit sales continued upward per market-research data; smart-telescope segment grew 38% YoY in 2023 [191][193]."

**Expected:** Both cited sources should contain or reasonably support the 38% YoY figure.

**Actual:**
- `citations.md` [191] is "Astronomy Technology Today — amateur telescope market 2020" — its description is "$218M → $294M; 7.8% CAGR (figures from a paid market report)." This is a 2020 article. There is no mention of smart telescopes or 2023 YoY growth in the citation description.
- `citations.md` [193] is "Business Research Insights — telescope market report" — its description is "5M global amateur astronomers (2023 estimate, paid report)." No mention of smart-telescope YoY growth.

The 38% figure appears in no citation description in citations.md. It has no traceable source in this deliverable.

**Grade:** FAIL

**Status:** OPEN

---

## F-02 — MODERATE: `audit/citation-audit.md` linked but absent

**File:** `C:/Users/jewza/source/cited-research/research/astrophotography-planning-apps/README.md`

**Section:** "What's in this directory" (line 66)

**Claim in README.md:**
```
- [citation-audit.md](audit/citation-audit.md)
- [consistency-review.md](audit/consistency-review.md)
```

**Expected:** Both files exist in the `audit/` directory.

**Actual:** The `audit/` directory contained no files at the time of this review. `consistency-review.md` is being created by this review. `citation-audit.md` is listed as a sibling but was not produced — no such file exists.

**Note:** If citation-audit.md was supposed to be produced by a parallel verification agent, it was either not run or its output was not written to disk.

**Grade:** FAIL

**Status:** OPEN

---

## F-03 — MODERATE: "$200K-$300K ARR" ceiling unmarked as estimate

**Files:**
- `C:/Users/jewza/source/cited-research/research/astrophotography-planning-apps/README.md` (one-paragraph summary, Quick decision framework item 3)
- `C:/Users/jewza/source/cited-research/research/astrophotography-planning-apps/analysis.md` (TL;DR, Don't build at all section)
- `C:/Users/jewza/source/cited-research/research/astrophotography-planning-apps/references/09-market-viability.md` (Conclusion)

**Claim (representative instance in README.md):**
> "indie revenue tops out around ~$200K-$300K ARR for planning-only tools"

**Expected:** Either (a) a derivation showing how the specific tools' ARR figures sum to this range, or (b) an explicit "(est.)" or "inferred from…" marker.

**Actual:**
- The Astrospheric ARR range is computed and labeled "Pure inference" in 09-market-viability.md: "$29.99/yr × 1-5% conversion of 108K = $32K–$162K ARR." That is labeled correctly.
- No similar inline inference-marker or derivation appears for "$200K-$300K ARR" in any of the three files. The figure is stated as the category ceiling across all indie tools without showing which tools' numbers were combined or how the ceiling was set.
- The only number that comes close to supporting this range is the Astrospheric $32K–$162K inference, which is below $200K at the top. There is no citation or calculation that produces the $200K–$300K range.

**Grade:** FAIL

**Status:** OPEN

---

## F-04 — MODERATE: "8-9% CAGR" is an unstated blend of two separate market figures

**Files:**
- `C:/Users/jewza/source/cited-research/research/astrophotography-planning-apps/README.md` (one-paragraph summary)
- `C:/Users/jewza/source/cited-research/research/astrophotography-planning-apps/analysis.md` (TL;DR)

**Claim:**
> "8-9% CAGR for telescope and astrophotography-camera markets"

**Expected:** If this is a range derived from two separate cited CAGR figures, the derivation should be stated (e.g., "telescope 8.2% [193], cameras 8.9% [192]").

**Actual:**
- `references/09-market-viability.md` cites telescope market CAGR as (implied) 8.2% from [193] and camera market CAGR as 8.9% from [192].
- `citations.md` [191] describes telescope market with "7.8% CAGR" (ATT 2020 article). [193] (Business Research Insights) is cited for "5M global amateur astronomers" with no CAGR stated in its description. The telescope CAGR source is therefore ambiguous — [191] says 7.8%, not 8.2%.
- The "8-9%" range in the summary files is presented without cites and without stating that it combines two different markets from two different paid reports.

**Grade:** FAIL (incomplete — derivation and sources not shown at point of claim)

**Status:** OPEN

---

## F-05 — MINOR: SkySafari 8 macOS sourced to iOS App Store listing

**File:** `C:/Users/jewza/source/cited-research/research/astrophotography-planning-apps/references/02-planning-tools.md`

**Section:** SkySafari 8 (Plus / Pro)

**Claim:**
> "Platform: iOS, Android, macOS [56][57][58]."

**Expected:** At least one cite that confirms macOS availability.

**Actual:**
- [56] is "SkySafari 8 — versions / pricing" — vendor collections page; this plausibly covers macOS, but the citation description focuses on pricing only.
- [57] is "SkySafari 8 Pro — product page" — plausibly lists platforms.
- [58] is "SkySafari 8 Pro — App Store" — iOS App Store listing. By definition, the iOS App Store does not confirm macOS availability; it is a weak source for this claim.

No macOS-specific citation (Mac App Store listing, vendor "platforms" page, or review confirming macOS) is present.

**Grade:** FAIL (weak sourcing for macOS platform claim; the assertion may be correct but is not well-supported)

**Status:** OPEN

---

## F-06 — MINOR: Citation [209] is an orphan

**File:** `C:/Users/jewza/source/cited-research/research/astrophotography-planning-apps/citations.md`

**Citation [209]:**
> "SkySafari — App Store SkySafari (free + Basic). iOS listing; 17,301 reviews / 4.7 stars / 669K+ downloads tracked."

**Expected:** This citation is referenced in at least one factual claim in analysis.md or a reference file.

**Actual:** No reference to [209] was found in any of the 10 reference files or in analysis.md. The data (17,301 reviews / 4.7 stars / 669K+ downloads) does not appear in any summary claim.

**Note:** Orphan citations are low-risk (they don't assert anything false), but they indicate either unused research or a dropped citation chain.

**Grade:** FAIL (by completeness standard — no claim traces to this citation)

**Status:** OPEN

---

## F-07 — MINOR: Citation [176] is an orphan with 403 disclosure

**File:** `C:/Users/jewza/source/cited-research/research/astrophotography-planning-apps/citations.md`

**Citation [176]:**
> "Telescopius donations page — page returned 403 at fetch time; cited via consistent reporting in [45][46]."

**Expected:** If cited, it should appear in at least one reference file or analysis. If not cited, it should not be in the numbered list, or the 403 disclosure makes it effectively a failed source.

**Actual:** [176] does not appear in any reference file or in analysis.md. The underlying content (Telescopius donation model) is correctly documented via [45] and [46]. [176] is effectively an unused fallback citation.

**Grade:** FAIL (orphan; transparent 403 disclosure is good, but an uncited citation with no content retrieved is a gap)

**Status:** OPEN

---

## F-08 — MINOR: "$50K/yr in years 1-3" is an unmarked estimate

**Files:**
- `C:/Users/jewza/source/cited-research/research/astrophotography-planning-apps/analysis.md` (Build new section)
- `C:/Users/jewza/source/cited-research/research/astrophotography-planning-apps/references/09-market-viability.md` (Implication paragraph in Conclusion)

**Claim:**
> "Top-end revenue is ~$50K/yr in years 1-3, hard ceiling around $200K-$300K"

**Expected:** This specific figure should be flagged as speculative/estimated, e.g., "(est.)" or "no source; inferred from…"

**Actual:** No derivation or citation is attached to "$50K/yr in years 1-3." It is not the Astrospheric inference (which is $32K–$162K total, not year-1-3 specifically). No ramp curve or source is cited for this number. The surrounding paragraph in 09-market-viability.md does say "all revenue figures…are inferred or third-party-estimated" in the Gaps section, which partially mitigates this — but the specific figure is not individually marked.

**Grade:** FAIL (specific number presented without inline derivation or "(est.)" marker)

**Status:** OPEN

---

## F-09 — MINOR: Internal markdown links (structural check)

**Files:** `analysis.md`, `README.md`, all reference files

**Check:** All internal links of the form `[Reference 05](references/05-decision-aid-gap.md)` or `[citations.md](citations.md)` were verified against the actual directory structure.

**Result:** All 10 reference files exist at the paths listed in README.md and analysis.md. `citations.md` exists at the root of the research directory. `audit/consistency-review.md` is created by this review. `audit/citation-audit.md` is the only missing link (covered in F-02).

**Grade:** PASS (with the exception covered by F-02)

**Status:** CLOSED

---

## Items Spot-Checked and Verified Consistent

The following claims were cross-checked across all files and found to be internally consistent:

| # | Claim | Files checked | Result |
|---|---|---|---|
| V-01 | Astrospheric Pro: $2.99/mo or $29.99/yr | citations.md [2], 01-weather-tools.md, 08-pricing.md, README.md, analysis.md | PASS |
| V-02 | SkySafari 8 Pro: $39.99 sale / $49.99 list | citations.md [56], 02-planning-tools.md, 08-pricing.md | PASS |
| V-03 | SGP: $149 first year + $59/yr renewal | citations.md [110], 04-capture-software.md, 08-pricing.md | PASS |
| V-04 | Telescopius Patreon: 519–646 patrons, ~$2,415/mo gross | citations.md [46], 02-planning-tools.md, 09-market-viability.md | PASS |
| V-05 | $2,415/mo × 12 = ~$29K/yr (Telescopius) | 09-market-viability.md math check | PASS ($28,980 ≈ $29K) |
| V-06 | Astrospheric iOS: 4.77/5, ~390 ratings | citations.md [34], 01-weather-tools.md, 09-market-viability.md, 10-mobile-vs-desktop.md | PASS |
| V-07 | Astrospheric Android: 4.06/5, ~680 ratings | citations.md [35], 10-mobile-vs-desktop.md | PASS |
| V-08 | Sky Tonight iOS: 4.76/5, ~70K ratings | citations.md [140], 09-market-viability.md, 10-mobile-vs-desktop.md | PASS |
| V-09 | Sky Tonight Android: 4.6/5, ~78K reviews, 10M+ installs | citations.md [141], 09-market-viability.md, 10-mobile-vs-desktop.md | PASS |
| V-10 | AstroBackyard: 506K subscribers as of April 2025 | citations.md [197], README.md, 09-market-viability.md | PASS |
| V-11 | Cloudy Nights: ~180K registered members | citations.md [196], README.md, 09-market-viability.md | PASS |
| V-12 | PhotoPills: $10.99 one-time iOS | citations.md [85], 03-photo-planners.md, 08-pricing.md | PASS |
| V-13 | PhotoPills: ~$1M ARR (third-party estimate) | citations.md [185], 03-photo-planners.md, 09-market-viability.md, README.md, analysis.md | PASS (consistently marked as third-party estimate) |
| V-14 | Astrospheric estimated downloads: ~108K | citations.md [37], 09-market-viability.md | PASS (both marked as third-party estimate) |
| V-15 | Astrospheric ARR inference: $32K–$162K | 09-market-viability.md math check: 108K × 1% × $29.99 = $32,390; 108K × 5% × $29.99 = $161,946 | PASS (labeled "Pure inference") |
| V-16 | r/astrophotography: 2.6M members (2025) | citations.md [195], 09-market-viability.md | PASS |
| V-17 | Stellarium Mobile Plus iOS: $13.99 one-time | citations.md [53], 02-planning-tools.md, 08-pricing.md | PASS |
| V-18 | Stellarium Mobile Plus iOS rating: 4.0/5, ~8,347 reviews | citations.md [53] (8,347), 10-mobile-vs-desktop.md ("~8.3K") | PASS (8,347 rounds to 8.3K) |
| V-19 | ASIAIR Plus retail: ~$349 (256GB) | citations.md [179], 04-capture-software.md, 08-pricing.md | PASS |
| V-20 | Stellarium catalog: 600K+ stars, 80K+ DSOs default | citations.md [47], 02-planning-tools.md | PASS |
| V-21 | SkySafari Pro catalog: 100M+ stars, 780K DSOs, 3M galaxies, 750K solar-system objects, 20K Abell/Zwicky | citations.md [57], 02-planning-tools.md | PASS |
| V-22 | Astrospheric API: 100 credits/day; cloud-cover call 5 credits | citations.md [8], analysis.md | PASS |
| V-23 | 7Timer: ~1.5M points, 0.001° precision, non-commercial | citations.md [18], 01-weather-tools.md, 07-api-and-oss.md | PASS |
| V-24 | Good to Stargaze tiers: $0.99/$6.49, $3.99/$25.99, $6.99/$54.99 | citations.md [16], 01-weather-tools.md, 08-pricing.md | PASS |
| V-25 | StarCast: 6-variable composite, 4-tier breakpoints, $2.99/mo iOS | citations.md [136], 01-weather-tools.md, 05-decision-aid-gap.md, 08-pricing.md | PASS |
| V-26 | StarCast target modifiers: Milky Way / DSO / Planetary / Wide Field | citations.md [136], 01-weather-tools.md, 05-decision-aid-gap.md | PASS |
| V-27 | NINA license: MPL 2.0; closed-source plugins rejected | citations.md [102][109], 04-capture-software.md, 07-api-and-oss.md, README.md | PASS |
| V-28 | RevenueCat annual-plan 12-mo retention: 44.1% | citations.md [189], 09-market-viability.md, analysis.md | PASS |
| V-29 | Astrospheric smoke refresh cadence: 6 hours | citations.md [4], 06-particulate-integration.md | PASS |
| V-30 | Clear Dark Sky: ~6,100 fixed locations, North America | citations.md [11], 01-weather-tools.md | PASS |
| V-31 | Astrospheric coverage: continental US + Canada only | citations.md [1], 01-weather-tools.md, README.md, analysis.md, 06-particulate-integration.md | PASS (consistent across all files) |
| V-32 | SkySafari at acquisition: 4M downloads | citations.md [62], 09-market-viability.md | PASS |
| V-33 | Astrophotography camera market: $1.2B (2024) → $2.5B (2033), 8.9% CAGR | citations.md [192], 09-market-viability.md | PASS |
| V-34 | Stellarium version: v26.1 (2026) | citations.md [47], 02-planning-tools.md | PASS |
| V-35 | StellarMate OS: $69 one-time | citations.md [180], 04-capture-software.md, 08-pricing.md | PASS |
| V-36 | Scope Nights: $6.99 one-time, iOS-only | citations.md [181][182], 01-weather-tools.md, 08-pricing.md | PASS |
| V-37 | Astrospheric smoke: column-integrated PM2.5; NIFC fire data; GOES every 30 min | citations.md [5], 06-particulate-integration.md | PASS |
| V-38 | Astrospheric vendor warning: "not to be used as an AQI forecast" | citations.md [4], 06-particulate-integration.md | PASS (consistently quoted) |
| V-39 | Ouranos pricing: ~$40/yr user-reported (T4) | citations.md [144][145], 08-pricing.md, 10-mobile-vs-desktop.md | PASS (all mark as user-reported, not vendor-confirmed) |
| V-40 | Telescopius pricing: free, Patreon-supported | citations.md [45][46], 02-planning-tools.md, 07-api-and-oss.md, 08-pricing.md, 09-market-viability.md | PASS (model described consistently; terminology varies — "donation-supported," "freemium-by-donation," "free + donation" — all describe the same model) |

---

## Coverage of Gaps and Limitations Sections

Each of the 10 reference files was checked for the presence of a "Gaps and limitations" section:

| File | Section present | Notes |
|---|---|---|
| 01-weather-tools.md | YES | Covers Meteoblue validation gap, Astrospheric Pro feature table gap, Ouranos methodology gap, StarCast stability caveat |
| 02-planning-tools.md | YES | Covers Telescopius weather provider, SkySafari camera compat, KStars mosaic workflow, AstroPlanner release date |
| 03-photo-planners.md | YES | Covers TPE 3D price, LightTrac status, PhotoPills Night AR scope |
| 04-capture-software.md | YES | Covers SGP API 404, Voyager pricing, ASIAIR firmware, NINA Target Scheduler weather awareness |
| 05-decision-aid-gap.md | YES | Covers StarCast traction unknown, Astrospheric possible undiscovered feature, equipment-modifier user-study gap |
| 06-particulate-integration.md | YES | Covers Meteoblue AOD consumer page unverified, pollen developer plans absent, pollen imaging-impact not quantified |
| 07-api-and-oss.md | YES | Covers Telescopius API status, ASIAIR GPL compliance, Meteoblue validation, AirNow rate-limits unconfirmed |
| 08-pricing.md | YES | Covers Voyager Advanced pricing, Ouranos vendor confirmation, TPE 3D price, Good to Stargaze archive gap, PhotoPills Android |
| 09-market-viability.md | YES | Covers all revenue as inferred, retention benchmarks as general (not astro-specific), population proxy range |
| 10-mobile-vs-desktop.md | YES | Covers Astrospheric red-mode status, SkySafari Android regression confirmation, Touch-N-Stars remote scope, Good to Stargaze maintenance status |

All 10 files have Gaps and limitations sections. PASS.

---

## Suppressed Contradiction Check

No cases were found where two files state directly conflicting facts without the contradiction being acknowledged. Specific checks:

- **Astrospheric coverage:** Consistently "continental US + Canada" in all files. PASS.
- **StarCast pricing and inputs:** Consistent across [136], 01-weather-tools.md, 05-decision-aid-gap.md, 08-pricing.md. PASS.
- **SkySafari 8 platform:** 02-planning-tools.md and 10-mobile-vs-desktop.md both list iOS + Android; macOS appears in 02 but not 10 (no contradiction, just partial overlap; F-05 covers the sourcing weakness). PASS.
- **NINA license:** Consistently MPL 2.0 across all files. PASS.
- **Telescopius pricing model:** All files describe it as free/donation-based; terminology varies but no contradiction. PASS.
- **Ouranos $40/yr:** Consistently marked as user-reported (T4), not vendor-confirmed. PASS.
- **Clear Dark Sky smoke signal:** Consistently described as "partial" and "not well-calibrated" per developer note, in 01-weather-tools.md, 06-particulate-integration.md, and analysis.md. PASS.

---

## Final Reviewer Note

After completing the above analysis, one additional pass was performed specifically to look for:

1. Any numerical discrepancy missed — none found beyond those documented in F-01 through F-04.
2. Any contradiction accepted as consistent on first pass — the "8-9% CAGR" blend (F-04) was initially noted as minor but on second look the underlying telescope CAGR sourcing is ambiguous (citations.md [191] says 7.8%; [193]'s description does not give a CAGR at all). This makes F-04 more significant than a rounding note.
3. Any unmarked estimate accepted as labeled — "$50K/yr in years 1-3" (F-08) and "$200K-$300K ARR" (F-03) were re-examined and confirmed as inadequately labeled.

No additional issues found beyond those documented.

---

*Generated by: Claude Code (claude-sonnet-4-6)*
*Review date: 2026-04-30*
