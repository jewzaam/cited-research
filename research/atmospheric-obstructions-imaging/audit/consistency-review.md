# Internal Consistency Review
# Atmospheric Obstructions for Astrophotography

**Reviewer:** Isolated agent (no conversation context from research session)  
**Date:** 2026-04-29  
**Scope:** All markdown files in `research/atmospheric-obstructions-imaging/`  
**Method:** Read all files; manually verify numerical claims against stated inputs;
check cross-file consistency; recalculate derived values where possible.

---

## Summary Table

| ID | Severity | Category | File(s) | Short description | Status |
|---|---|---|---|---|---|
| C-01 | **CRITICAL** | Formula error | `references/particulates-to-imaging-impact.md`, `atmospheric-obstructions-guide.md` | Worked-example AOD values do not match stated α = 1.5 | **RESOLVED** — both tables recomputed with correct α=1.5 values |
| C-02 | **MODERATE** | Numerical inconsistency | `references/saharan-dust-transport.md` vs `citations.md` [66] | SAL peak start date: "late June" vs "mid-June" | **RESOLVED** — corrected to "mid-June through mid-August" |
| C-03 | **MODERATE** | SAL altitude description | `README.md`, `atmospheric-obstructions-guide.md`, `references/saharan-dust-transport.md` | "1–3.5 mi above surface" conflates base and top of the SAL layer | **RESOLVED** — rephrased as "base ~1 mi above surface, layer 2–2.5 mi thick" |
| C-04 | **MINOR** | Estimation marker | `atmospheric-obstructions-guide.md` | Severity-scale note says "synthesis judgment" inline but not labeled "est." in header | **RESOLVED** — tier boundaries explicitly marked (est.) in README and regional-priority-matrix |
| C-05 | **MINOR** | Caveat propagation | `atmospheric-obstructions-guide.md` | Citation [89] INACCESSIBLE status surfaced in gap text but not in the relevant factual claim | **RESOLVED** — inline INACCESSIBLE marker added in the gaps section near [89] |
| C-06 | **MINOR** | Orphan claim | `references/equipment-protection-thresholds.md` | "~50 Tg/yr" Saharan dust to Caribbean — no citation number assigned | **RESOLVED** — added citation [108] to citations.md and inline reference |
| C-07 | **MINOR** | Caveat propagation | `references/volcanic-stratospheric-haze.md` | Citation [76] INACCESSIBLE status: clearly flagged in equipment-protection ref; partially propagated in volcanic ref (not directly relevant, pass) | PASS |

---

## Verified-as-consistent items

- Barkjohn equation coefficients: **0.524 × PA_cf_1 − 0.0862 × RH + 5.75** — identical in citations.md [18], aerosols-and-pm25.md, source-conflict-resolution.md, atmospheric-obstructions-guide.md.
- Barkjohn calibration: **50 sensors, 39 sites, 16 states** — consistent in citations.md [18], aerosols-and-pm25.md, source-conflict-resolution.md. The "70+ sites" claim is explicitly repudiated in the guide (Phase 1 correction noted); absent from all files.
- Jaffe 2023 dust factor: **5–6× (slope 5.6 at Keeler)** — consistent across citations.md [19], aerosols-and-pm25.md, source-conflict-resolution.md, atmospheric-obstructions-guide.md.
- Patat 2011: **k₀ = 0.013 ± 0.002, α = −1.38 ± 0.06** — consistent in citations.md [1] and particulates-to-imaging-impact.md.
- Fu 2022 R range: **0.03–0.60 across 19 stations**; predictive R **0.49 / 0.74 / 0.81** — consistent across citations.md [11], aerosols-and-pm25.md, particulates-to-imaging-impact.md, README.md, atmospheric-obstructions-guide.md.
- Google Pollen: **80 countries** (not 65+) — consistent in citations.md [35], pollen-data-sources.md, atmospheric-obstructions-guide.md, regional-priority-matrix.md.
- NC State GDD: **onset 300 GDD, peak 636 GDD, base 55°F, start Feb 1** — consistent in citations.md [42], pollen-data-sources.md, equipment-protection-thresholds.md, regional-priority-matrix.md, atmospheric-obstructions-guide.md. Verified by citation-audit.md.
- Williams Flats: **12 models (3 global + 9 regional), NMB −87.4% to −4.3%, r ≤ 0.50** — consistent in citations.md [59], wildfire-smoke-forecasting.md, atmospheric-obstructions-guide.md, README.md.
- NASA FIRMS: **5000 tx/10 min, 5-day max range** — consistent in citations.md [56], wildfire-smoke-forecasting.md, atmospheric-obstructions-guide.md.
- AOML SAL geometry: **2–2.5 mile thick, base ~1 mile** — consistent between citations.md [66] and saharan-dust-transport.md (direct quote preserved).
- Pinatubo AOD: **0.1–0.15 global average, 0.4 local peak, ~17 Mt SO₂** — consistent in citations.md [86], volcanic-stratospheric-haze.md, particulates-to-imaging-impact.md, README.md.
- IAC ORM: **0.130 mag/airmass V-band median** — consistent in citations.md [3], particulates-to-imaging-impact.md, atmospheric-obstructions-guide.md.
- Conversion factor: **1.086 = 2.5/ln(10)** — stated explicitly in particulates-to-imaging-impact.md; mathematically correct (2.5 / 2.30259 = 1.08574 ≈ 1.086).
- Pinatubo magnitude conversion: **AOD 0.12 → 0.13 mag/airmass; AOD 0.40 → 0.43 mag/airmass** — 1.086 × 0.12 = 0.1303 ≈ 0.13 ✓; 1.086 × 0.40 = 0.4344 ≈ 0.43 ✓; airmass-2 doubling 0.43 × 2 = 0.86 ✓.
- Estimation markers: worked example in particulates-to-imaging-impact.md is labeled "(est.)" on each derived AOD and Δm value; Pinatubo conversions in particulates-to-imaging-impact.md and volcanic-stratospheric-haze.md are labeled "(calculated, est.)"; severity scale in README.md and regional-priority-matrix.md both note it is a "synthesis" judgment, not an established convention.
- Citation [76] and [89] INACCESSIBLE status: surfaced in citations.md with bold warnings; carried into equipment-protection-thresholds.md [76], volcanic-stratospheric-haze.md [89], and atmospheric-obstructions-guide.md gaps section. Not silently hidden.
- Vendor disagreement on pollen damage (Astro-Physics vs Baader vs ASO): all three positions are cited in equipment-protection-thresholds.md with explicit source numbers; disagreement is not silently resolved. Guide restates the span and flags the ASO 403.
- Pollen settles overnight: pollen-data-sources.md and equipment-protection-thresholds.md both acknowledge the "settles overnight" assumption is species-dependent, citing the same evidence [50, 51, 52]. No contradiction.
- SAL dust reaching the surface: saharan-dust-transport.md says it reaches surface via subsidence after 24–48 hr; equipment-protection-thresholds.md notes PM2.5 at "unhealthy" levels during dust events in Florida/Caribbean. These are consistent (both acknowledge surface deposition occurs).
- Astrospheric column-vs-surface: citations.md [58], wildfire-smoke-forecasting.md, and atmospheric-obstructions-guide.md all quote the same text and use it consistently to support the column-AOD argument.
- PurpleAir correction validity across files: the ">60 µg/m³ / <−12 °C" boundary is stated in citations.md [18], aerosols-and-pm25.md, and source-conflict-resolution.md consistently; the "300 µg/m³ extreme-smoke failure" is stated in wildfire-smoke-forecasting.md, aerosols-and-pm25.md, and source-conflict-resolution.md consistently. These are not in conflict — they address different concentration regimes.
- Cross-reference links within reference files use relative paths (e.g., `equipment-protection-thresholds.md` from within `references/`); links from README and guide use `references/filename.md`. Both patterns resolve correctly for the directory structure.

---

## Detailed Issue Sections

---

### C-01 — CRITICAL: Worked-example AOD values inconsistent with stated α = 1.5

**Status:** RESOLVED  
**Files:** `references/particulates-to-imaging-impact.md` (lines 44–54), `atmospheric-obstructions-guide.md` (lines 199–206)  
**Category:** Formula error — numerical inconsistency between stated parameter and derived values

**Expected values** (Ångström formula: AOD(λ) = AOD(λ₀) × (λ/λ₀)^(−α), with α = 1.5, λ₀ = 550 nm, AOD(550) = 0.20):

| Band | Wavelength | Correct AOD | Correct Δm | File states AOD | File states Δm |
|---|---|---|---|---|---|
| B | 440 nm | **0.280** | **0.30** | 0.262 (est.) | 0.28 (est.) |
| OIII | 500 nm | **0.231** | **0.25** | 0.218 (est.) | 0.24 (est.) |
| V | 550 nm | 0.200 | 0.22 | 0.200 | 0.22 ✓ |
| Ha | 656 nm | **0.154** | **0.17** | 0.164 (est.) | 0.18 (est.) |
| SII | 671 nm | **0.148** | **0.16** | 0.160 (est.) | 0.17 (est.) |

**Verification of stated AOD → Δm step:** the Δm values in the table are arithmetically correct given the stated AOD values (e.g., 1.086 × 0.218 = 0.2367 ≈ 0.24 ✓). The error is exclusively in the AOD column — the stated AODs are inconsistent with α = 1.5.

**What alpha would produce these AOD values?** Working backwards from the OIII entry: AOD(500) / AOD(550) = 0.218/0.200 = 1.09 = (550/500)^α = 1.1^α → α = ln(1.09)/ln(1.1) = 0.0862/0.0953 ≈ 0.90. No single consistent α reproduces all tabulated values simultaneously at the precision stated.

**Impact:** The qualitative conclusion — "OIII suffers more than Ha during fine-mode events" — is directionally correct regardless of the exact α used (OIII at shorter wavelength always sees more extinction than Ha during fine-mode). However, the specific magnitude values are wrong, and a developer implementing the table would compute systematically incorrect per-band extinction corrections.

**Both files are affected equally.** The guide (atmospheric-obstructions-guide.md) reproduces only the OIII/V/Ha rows; the reference file includes B and SII as well.

**Note:** The "(est.)" markers are present on all affected values, which correctly signals derived status. The estimation marker does not, however, exempt the values from being internally consistent with the stated α.

---

### C-02 — MODERATE: SAL peak start date inconsistency ("late June" vs "mid-June")

**Status:** RESOLVED  
**Files:** `references/saharan-dust-transport.md` (line 19) vs `citations.md` (citation [66])  
**Category:** Numerical inconsistency — temporal claim

**citations.md [66]** (verified source, direct quote from NOAA AOML):
> "Active mid-June through mid-August (peak), declining after."

**saharan-dust-transport.md** (line 19):
> "Peak intensity: **late June through mid-August**."

**Actual value (per citation):** active (peak) period starts **mid-June**.  
**File states:** peak starts **late June**.

The reference file has silently narrowed the peak window from "mid-June" (per the cited source) to "late June." The remainder of the document and the regional-priority-matrix.md ("mid-June to mid-August") and atmospheric-obstructions-guide.md ("mid-June and mid-August") correctly use "mid-June." Only saharan-dust-transport.md deviates.

This is a minor factual drift — "mid-June" vs "late June" spans about two weeks, which affects the seasonal window signaling in the app. In NC, mid-June vs late June is meaningful for trigger logic.

---

### C-03 — MODERATE: SAL altitude description conflates base and extent

**Status:** RESOLVED  
**Files:** `README.md` (line 29), `atmospheric-obstructions-guide.md` (line 109), `references/saharan-dust-transport.md` (line 63)  
**Category:** Ambiguous phrasing — not a numerical error but misleading

**Source [66] says:** "2 to 2.5-mile-thick layer of the atmosphere with the base starting about 1 mile above the surface."

This gives:
- Base: ~1 mile above surface
- Top: ~1 + 2 to 2.5 = **3 to 3.5 miles** above surface
- Altitude range occupied by the SAL: approximately 1–3.5 miles

**What the files say:** README.md and atmospheric-obstructions-guide.md both write "SAL sits 1–3.5 mi above surface." saharan-dust-transport.md writes "SAL sits **1 to 3.5 miles above the surface**."

The phrasing "1–3.5 mi above surface" correctly describes the altitude range the SAL occupies (base to top). However, a reader could misread it as "the base of the SAL ranges from 1 to 3.5 miles above the surface," which would be incorrect — the base is consistently ~1 mile, not variable up to 3.5 miles. The unambiguous statement would be "SAL base ~1 mile above surface, extends to ~3–3.5 miles (2–2.5 mile thick layer)."

This is not a factual error but a phrasing ambiguity that could mislead an app developer implementing the SAL altitude logic.

---

### C-04 — MINOR: Severity-scale estimation label in README

**Status:** RESOLVED  
**File:** `README.md` (lines 56–68)  
**Category:** Estimation marker completeness

The README severity table (lines 58–63) presents four ΔV tiers without "(est.)" on the tier boundaries. The explanatory text immediately below the table does state "Severity tiers are a synthesis from this research; not an established astronomical convention." That note is present and adequate, but the table itself does not carry any per-row annotation.

The regional-priority-matrix.md table (lines 107–112) carries the identical severity tiers and includes the same gap note ("not an established astronomical convention"), but neither table annotates the boundary values (0.05, 0.15, 0.40 mag/airmass) as estimated or synthesized within the table cells.

**Actual risk:** Low. The prose caveat is present in both locations. This is a consistency issue with the "(est.)" convention used in the worked example table, not a missing caveat.

---

### C-05 — MINOR: Citation [89] INACCESSIBLE caveat not adjacent to the claim it supports

**Status:** RESOLVED  
**File:** `atmospheric-obstructions-guide.md` (lines 294–298)  
**Category:** Caveat propagation

Citation [89] (ESO Messenger 190, Hunga Tonga Paranal observations) is INACCESSIBLE per citations.md. The guide's gap section (line 292–298) explicitly says: "ESO Messenger PDF was inaccessible in our re-fetch — relying on Dim9 Discovery agent extraction."

However, the claim supported by [89] — that Paranal twilight calibration showed sky brightness changes persisting >12 months after Hunga Tonga — also appears in the volcanic-stratospheric-haze.md reference file (lines 34–38) with the INACCESSIBLE flag prominently placed. The guide's gap section correctly identifies the limitation.

The only minor issue is that the factual claim at guide line 294–296 is cited as "[89]" without an inline "(INACCESSIBLE)" marker adjacent to the citation, whereas citations.md labels it boldly. A reader scanning the guide without the citation file might not realize [89] is unverified. This is a display-level propagation issue, not a factual error.

The volcanic-stratospheric-haze.md reference file handles this correctly with explicit inline flagging.

---

### C-06 — MINOR: Orphan claim — Saharan dust ~50 Tg/yr to Caribbean

**Status:** RESOLVED  
**File:** `references/equipment-protection-thresholds.md` (line 83)  
**Category:** Completeness — uncited factual claim

The equipment-protection-thresholds.md states: "Saharan dust transport to the Caribbean delivers **~50 Tg/yr** to the region (per Dim6 Discovery)."

The parenthetical "(per Dim6 Discovery)" identifies the extraction agent but does not map to any numbered citation in citations.md. No citation number is assigned. This is the only factual claim in the reference files that lacks a numbered citation.

**Expected:** a citation number pointing to a peer-reviewed or institutional source. Dim6 Discovery agent likely extracted this from a paper, but that paper is not in the citations.md list.

---

## Re-examination before finalizing

**Did I miss any numerical discrepancy?**

Checked and found none beyond C-01 and C-02. Specifically verified:
- The "R² collapses to 0.03–0.21 above 1.3 km" claim uses 1.3 km as the threshold for the R² breakdown and 1.35 km for the "58% mass above" measurement — these come from different studies ([16] Chew et al.) and are internally consistent: 1.3 km is the altitude threshold used in the regression analysis; 1.35 km is the scale-height measurement cutoff. Both numbers are correctly attributed to [16] and agree across all files.
- The Petržala & Kocifaj 2026 [9] claim: "R = 0.998 under controlled conditions but raw empirical PM2.5/AOD R² is 'well below 0.6'" — this is stated in citations.md and particulates-to-imaging-impact.md consistently, and is not contradicted by the Fu 2022 R = 0.03–0.60 range (different paper, different metric).
- Buton 2013 V ≈ 0.11, B ≈ 0.19 values are flagged as "DRIFT" in all files that mention them — no false precision is implied.

**Did I accept a contradiction as consistent?**

The SAL peak "mid-June vs late June" discrepancy in C-02 was initially read past before being caught on second pass. No other accepted-as-consistent items are actually contradictions.

**Is there an unmarked estimate I missed?**

The "2–3× the total extinction" for SE-US sea-level users vs high-altitude observatories is stated in particulates-to-imaging-impact.md (line 74) and atmospheric-obstructions-guide.md (line 229) without an "(est.)" marker. This is a rough qualitative comparison, not a calculated value, so the absence of "(est.)" is a marginal issue but not a material one given the explicit "roughly" qualifier.

The "for a NC SCT/refractor user" 1,500 grains/m³ threshold used in the equipment-protection alert logic is also not marked as estimated — it is described in equipment-protection-thresholds.md as "Very high is conventionally above ~1,500 grains/m³" without a source citation. The pollen-data-sources.md pollen API description of 5-day forecasts does not carry a citation for the "very high" threshold label. This is a minor unmarked synthesis but not a calculation.
