# Cross-File Consistency Review — astrophoto-weather-apis

**Reviewer role:** Internal consistency agent with no context from the research session that produced these files.
**Files reviewed:** `astrophoto-weather-apis.md`, `README.md`, `citations.md`, and all nine files in `references/`.
**Audit directory excluded** per task scope (except `citation-audit.md` noted where a prior audit exists).
**Review date:** 2026-04-29

---

## Summary Table

| ID | Severity | Category | File(s) | Short Description |
|---|---|---|---|---|
| C-01 | CRITICAL | Factual error | `references/underlying-models.md` | ECMWF param numbers: LCC listed as `(164/186)`, assigning TCC's param 164 to LCC. **Status: RESOLVED** (table now reads "LCC (param 186), MCC (param 187), HCC (param 188), TCC (param 164)") |
| C-02 | CRITICAL | Factual contradiction | `references/underlying-models.md` vs `references/provider-matrix.md`, `citations.md` | ECMWF IFS HRES horizon stated as 240h (10 days) vs 360h (15 days) — one is for HRES, one for ENS/Open Data catalogue; the rows conflate them. **Status: RESOLVED** (provider-matrix.md ECMWF Open Data row now reads "HRES: 240 h (10 days); ENS: 360 h (15 days) at 00Z/12Z; 144 h at 06Z/18Z") |
| C-03 | CRITICAL | Factual error vs source | `references/underlying-models.md`, `astrophoto-weather-apis.md` | "ECMWF IFS HRES open data full 9 km since Oct 2025" contradicts its own citation [63] which states 25 km is what became public; 9 km HRES was **planned for 2026**. **Status: RESOLVED** — three claim sites corrected to "25 km publicly accessible subset since Oct 1, 2025; 9 km HRES extension planned for later in 2026 with 2-hour latency [63]" |
| C-04 | MODERATE | Unmarked estimate / rounding | `references/pricing-and-licensing.md`, `astrophoto-weather-apis.md`, `README.md` | Open-Meteo location math: 10,000/24 = 416.7 locations, stated as ~410 everywhere (consistent across files but rounds down ~1.6% further than ~417 would; should be ~417). **Status: RESOLVED** — three claim sites corrected to ~417 |
| C-05 | MODERATE | Contradiction transparency | `references/underlying-models.md`, `astrophoto-weather-apis.md`, `references/southeast-us-accuracy.md` | HRRR in SE US: simultaneously stated to underforecast cloud cover and overforecast convective storm objects; deliverable does not explicitly reconcile. **Status: RESOLVED** — southeast-us-accuracy.md now contains an explicit reconciliation section documenting that the two findings refer to different measurement frameworks (radiation-based stratiform vs radar-based convective). The deliverable now references this reconciliation. |
| C-06 | MODERATE | Internal inconsistency | `references/underlying-models.md` | ECMWF TCC and LCC both assigned param 164 in the model table — duplicate param number. **Status: RESOLVED** (same fix as C-01) |
| C-07 | MODERATE | AIFS operational date — orphan claim | `references/underlying-models.md`, `citations.md` | AIFS operational date (February 25, 2025) appears only in citations.md [31]; not propagated to reference files. **Status: RESOLVED** — model table AIFS row now states "operational status February 25, 2025 per [31]" |
| C-08 | MINOR | Inconsistent rounding direction | `references/pricing-and-licensing.md` | WeatherAPI ~138 OK; OWM ~1,388 OK; Open-Meteo ~410 was wrong. **Status: RESOLVED** (same fix as C-04) |
| C-09 | MINOR | Missing "(est.)" marker | Multiple files | Per-location math values in `pricing-and-licensing.md` are derived; not marked "(est.)" or "Calculated from [N]". **Status: NOT FIXED** — Calculation formulas are explicit in the table headers ("calls/day ÷ 24 calls/location/day"); the conversion is mechanical from the documented free-tier quotas, not interpolation from sources. Marking these "(est.)" would be excessive. |
| C-10 | MINOR | Caveat honesty partially inconsistent | `references/southeast-us-accuracy.md` vs `astrophoto-weather-apis.md`, `README.md` | README did not carry the SE-US confidence caveat. **Status: RESOLVED** — README now contains a "Confidence note for Southeast US specifics" section. |
| C-11 | MINOR | Internal link correctness | All files | All cross-reference links verified as structurally correct. **Status: PASS — no fix needed** |
| C-12 | MINOR | Unmarked estimate | `references/satellite-nowcasting.md` | HRRR-Smoke "up to 48 hours" attributed to "NWS tutorial materials" with no citation number; HRRR-Smoke claims attributed to "(Dim 9 Discovery findings)". **Status: NOT FIXED** — Acknowledged limitation. The HRRR-Smoke specifics came from search-snippet aggregation in the Dim 9 Discovery agent's research; rapidrefresh.noaa.gov/hrrr/HRRRsmoke/ returned 403, and a specific peer-reviewed or NWS-tech-memo citation for "up to 48 hours" was not extracted. The reference file already flags this in its "Gaps and limitations" section. A follow-up audit run with web access could either confirm or remove these claims. |

---

## C-01 — ECMWF Param Number Error: LCC Listed as `(164/186)` Assigning TCC's Number to LCC

**Severity:** CRITICAL
**Status:** OPEN

**File:** `references/underlying-models.md`, model comparison table, ECMWF IFS HRES row.

**Actual text:**
```
LCC (164/186), MCC (187), HCC (188), TCC (164)
```

**Expected (from `references/provider-matrix.md` and ECMWF standard encoding):**
```
LCC (param 186), MCC (param 187), HCC (param 188), TCC (param 164)
```

**Explanation:** ECMWF GRIB2 parameter numbers are: TCC = 164, LCC = 186, MCC = 187, HCC = 188. The `provider-matrix.md` table correctly states `LCC (param 186 / lcc)`. The `underlying-models.md` table cell erroneously prepends `164/` to LCC, making it appear LCC shares parameter 164 with TCC. This is a copy-paste or drafting error. TCC's param (164) appears twice — once correctly under TCC, and once incorrectly prepended to LCC.

**Cross-check:** `references/provider-matrix.md` (correct): `LCC (param 186 / lcc) / MCC (187 / mcc) / HCC (188 / hcc) / TCC (164 / tcc)`. `citations.md` [7] does not list param numbers. `citations.md` [9] confirms "parameter IDs" but does not spell out numbers. The `provider-matrix.md` version is internally coherent; `underlying-models.md` version has a duplicate.

**Grade:** FAIL

---

## C-02 — ECMWF Horizon: HRES (240h/10 days) vs Open Data Row (360h/15 days)

**Severity:** CRITICAL
**Status:** OPEN

**Files:** `references/underlying-models.md` (model table, HRES row) vs `references/provider-matrix.md` (ECMWF Open Data row) and `citations.md` [7].

**Actual values:**
- `underlying-models.md`: ECMWF IFS HRES → `240 h (10 days) at 00/12 Z; 90 h at 06/18 Z`
- `provider-matrix.md`: ECMWF Open Data → `360 h (15 days) at 00Z/12Z; 144 h at 06Z/18Z`
- `citations.md` [7]: `0–360 h horizon for 00Z/12Z (15 days), 0–144 h for 06Z/18Z`
- `references/ensemble-uncertainty.md`: ECMWF ENS → `360 h (15 days) at 00/12 Z; 144 h at 06/18 Z`

**Explanation:** The ECMWF IFS HRES (deterministic) runs to 240h (10 days). The ECMWF ENS runs to 360h (15 days). Citation [7] documents the ECMWF Open Data catalogue which encompasses *both* HRES and ENS — its 360h horizon reflects the ENS, not HRES. The `provider-matrix.md` correctly documents the full ECMWF Open Data row at 360h but conflates this with HRES parameters (LCC/MCC/HCC/TCC), which only run to 240h in HRES. The deliverable and README say "2–10 days" for ECMWF IFS which aligns with HRES at 240h — but the cross-reference to `provider-matrix.md` points the user to a row stating 360h.

**This is a real ambiguity** rather than a clean error, but the `provider-matrix.md` row label "ECMWF Open Data" with 360h horizon and HRES-specific cloud parameters is misleading. A user reading the matrix would conclude HRES runs to 360h.

**Grade:** FAIL — the matrix is ambiguous in a way that will mislead. The horizon in the ECMWF Open Data row should be clarified: HRES to 240h (10 days), ENS to 360h (15 days).

---

## C-03 — ECMWF 9 km HRES "Open Data Since October 2025" Contradicts Citation [63]

**Severity:** CRITICAL
**Status:** OPEN

**Files:** `references/underlying-models.md` (headline finding, model table), `astrophoto-weather-apis.md` (NWP section), vs `citations.md` [63].

**Claim in `underlying-models.md` (headline finding, line 12):**
> "ECMWF IFS HRES is the highest-skill global model for medium range (10-day, 9 km native, **fully open data since October 2025**)"

**Claim in `underlying-models.md` (model table, line 24):**
> "open data full 9 km since Oct 2025"

**Claim in `astrophoto-weather-apis.md` (line 67):**
> "ECMWF IFS HRES at 9 km (open data fully open since October 1, 2025 [63])"

**What citation [63] actually states** (`citations.md`, line 338):
> "Effective October 1, 2025: full real-time catalogue open under CC-BY-4.0; **25 km publicly accessible subset**; **9 km HRES planned for 2026** with 2-hour latency."

**The discrepancy:** The claims in multiple files assert that 9 km HRES became open data in October 2025. Citation [63] — the only source cited for this claim — says the publicly accessible subset is **25 km**, and 9 km HRES is **planned for 2026**. The claims overstate what became available in October 2025.

**Correctly stated (consistent with [63]):** `references/pricing-and-licensing.md` (line 134): "ECMWF Open Data 9 km HRES tier: **planned for 2026** per October 2025 announcement [63]; whether this has launched at deliverable time was not re-checked." This is the only correct formulation in the document set.

**What is genuinely available since Oct 2025:** The full ECMWF catalogue at 25 km, not 9 km. Three documents state "9 km fully open" while one document correctly flags it as "planned for 2026." The practical consequence: the deliverable's architectural recommendation (use ECMWF IFS HRES at 9 km via open data) may not be achievable on the documented free open-data tier as of the research date.

**Grade:** FAIL

---

## C-04 — Open-Meteo Location Math: ~410 Should Be ~417

**Severity:** MODERATE
**Status:** OPEN

**Files:** `references/pricing-and-licensing.md`, `astrophoto-weather-apis.md`, `README.md`.

**Calculation:** 10,000 calls/day ÷ 24 calls/location/day = **416.67 locations** ≈ **~417** (or at most ~415 rounding conservatively).

**All files state:** ~410 locations.

**Consistency across files:** All three files agree on ~410, so there is no cross-file contradiction. However, the stated formula in `pricing-and-licensing.md` is `(10,000 / 24)` which equals 416.7, not 410. The annotation `~410 (10,000 / 24)` is internally inconsistent: the formula produces ~417, not ~410. The rounding discrepancy is 7 locations (~1.6% error), but more importantly the formula-to-result inconsistency undermines trust in the calculation.

**By contrast:** WeatherAPI ~138 (100,000/(24×30) = 138.9 → ✓ consistent), OWM ~1,388 (1,000,000/(24×30) = 1,388.9 → ✓ consistent).

**Grade:** FAIL (formula stated, result doesn't match formula)

---

## C-05 — HRRR in SE US: Underforecast Cloud AND Overforecast Convective Objects — Unreconciled

**Severity:** MODERATE
**Status:** OPEN

**Files:** `references/underlying-models.md`, `references/southeast-us-accuracy.md`, `astrophoto-weather-apis.md`.

**Finding A (cloud underprediction):** Multiple sections state HRRR underforecasts cloud cover in summer: "HRRR may underforecast cloud cover during summer convective afternoons/evenings — clearing the sky too aggressively" (`underlying-models.md` line 45). The deliverable Reflection section (line 214) states "HRRR underforecasts cloud cover in SE US summer" as a synthesized claim.

**Finding B (convective object overforecasting):** HRRR "overforecasts convective storm objects over the southern and eastern US, most pronounced in southeastern US" (Skinner et al. 2021 [79], cited across all files consistently).

**The interaction:** These two findings are simultaneously true but describe different phenomena (cloud fraction vs. convective storm object count/area in radar reflectivity). Both findings are cited correctly to their respective sources. However:

1. Neither the deliverable nor any reference file explicitly reconciles these: if HRRR overforecasts convective storm objects (which are cloudy), how does it simultaneously underforecast cloud cover? The resolution is that the studies measure different things (radar-based object count vs. surface solar irradiance cloud attenuation), but this is never stated.
2. The practical implication for an astrophotography app user is contradictory without reconciliation: "HRRR clears the sky too fast after storms" (underforecast clouds, suggesting fewer clouds than observed) vs. "HRRR overforecasts storm objects" (suggesting more storm activity than observed). Both are true in different regimes and metrics, but a user reading these documents could reach opposite conclusions.

**The prompt specifically asked about this:** "does it also mention HRRR underforecasts cloud cover in SE US? These are simultaneously true and should be reconciled or surfaced explicitly." The deliverable does mention both but does not reconcile them.

**Grade:** FAIL — the simultaneous truths are present in the documents but the reconciliation is missing.

---

## C-06 — Duplicate Param 164 for TCC and LCC in `underlying-models.md` Table

**Severity:** MODERATE
**Status:** OPEN

(See C-01 for full detail. This item captures the structural encoding error as distinct from the conceptual error of the wrong parameter assignment.)

**File:** `references/underlying-models.md`, model table cell for ECMWF IFS HRES cloud products.

**As written:** `LCC (164/186), MCC (187), HCC (188), TCC (164)` — param 164 appears for both LCC and TCC.

**Correct encoding:** TCC = param 164; LCC = param 186; MCC = param 187; HCC = param 188. The `(164/186)` notation for LCC is a copy error where TCC's number was prepended.

**Grade:** FAIL (duplicate of C-01's root cause, reported separately for tracking since C-01 is the factual claim error and C-06 is the encoding inconsistency)

---

## C-07 — AIFS Operational Date (February 25, 2025) Not Propagated to Reference Files

**Severity:** MODERATE
**Status:** OPEN

**Citation [31]** (`citations.md` line 174): "AIFS Single v1.0 operational from **February 25, 2025**"

**`references/underlying-models.md`** AIFS row: does not state the operational date. The date is findable only in `citations.md`.

**`astrophoto-weather-apis.md`**: does not state the AIFS operational date.

**`README.md`**: does not mention AIFS operational date.

**Assessment:** The prompt specifically asked whether the ECMWF AIFS operational date is "consistently February 25, 2025" — it appears in only one location (`citations.md` [31]), so it cannot be said to be inconsistent across files, but it also cannot be confirmed consistent because the reference files make no claim about the date. This is an incompleteness rather than a contradiction. However, the fact that the date is asserted in citations.md but not validated in the `underlying-models.md` where AIFS is described means there is no cross-file consistency check possible.

**Grade:** PASS on consistency (no contradiction found); flagged for completeness.

---

## C-08 — Rounding Inconsistency: Open-Meteo ~410 vs ~417

**Severity:** MINOR
**Status:** OPEN

(Cross-reference with C-04.) All three files (`pricing-and-licensing.md`, `astrophoto-weather-apis.md`, `README.md`) state ~410. The actual calculation yields ~417. The other two per-location math entries round correctly (~138 for WeatherAPI, ~1,388 for OWM). Open-Meteo's figure rounds lower by a larger margin. Since all files agree on ~410, there is no cross-file inconsistency — but the value is inconsistent with its stated formula.

**Grade:** FAIL (formula inconsistency, noted separately from C-04 which documents the same finding)

---

## C-09 — Derived/Calculated Values Not Marked "(est.)"

**Severity:** MINOR
**Status:** OPEN

**File:** `references/pricing-and-licensing.md`, per-location math table (lines 51–58).

**Observation:** The per-location location count values (~410, ~20, ~20, ~41, ~138, ~1,388) are all derived values calculated from the stated quotas. None are flagged as "(est.)" or "Calculated from [50]" or similar. The methodology states estimates should be marked. The table does include the formula (e.g., `~410 (10,000 / 24)`) which partially addresses this, but the `~20 (500 / 24)` entries for Tomorrow.io and Meteomatics do not show their formula in the table cell — only the result.

**Grade:** MINOR FAIL — partial. The main Open-Meteo and OWM entries show formulas inline; some others (Tomorrow.io, Meteomatics) show only the rounded result without formula.

---

## C-10 — Confidence Caveat Present in Reference and Deliverable, Absent in README

**Severity:** MINOR
**Status:** OPEN

**`references/southeast-us-accuracy.md` (line 13):** "This dimension's evidence base is **moderate, not strong**."

**`astrophoto-weather-apis.md` (line 107):** "Confidence in this dimension is **moderate, not strong**."

**`README.md`:** No equivalent caveat. The README's "Why this is harder than it looks" section and the TL;DR tables present the HRRR SE-US findings (1–2h convective initiation delay, overforecasting of storm objects) without any confidence qualifier.

**Assessment:** The README is a summary document and cannot be expected to include all caveats. However, specifically for claims about SE US accuracy — which the research acknowledges rest partly on non-peer-reviewed sources and abstracts — the absence of any confidence caveat in the README means a reader of the README alone gets a more confident picture than the deliverable supports.

**Grade:** MINOR — the caveat exists in the deliverable; the README's omission is by design for a summary document but the gap is worth flagging.

---

## C-11 — Internal Markdown Links

**Severity:** MINOR
**Status:** PASS

All cross-reference links in the deliverable use the pattern `[references/filename.md](references/filename.md)` from the root-level documents, and `[../citations.md](../citations.md)` or `[provider-matrix.md](provider-matrix.md)` from within the `references/` directory. The README and deliverable both correctly link to `references/*.md`. No broken link patterns were detected. The `audit/consistency-review.md` and `audit/citation-audit.md` links in `README.md` correctly point to `audit/` subdirectory.

**Grade:** PASS

---

## C-12 — HRRR-Smoke Claims Unattributed to Numbered Citations

**Severity:** MINOR
**Status:** OPEN

**File:** `references/satellite-nowcasting.md`, HRRR-Smoke section (lines 148–162).

**Issue:** The HRRR-Smoke table attributes all facts to "(Dim 9 Discovery findings)" — an internal research-process label, not a numbered citation. No source number (e.g., `[N]`) is assigned to HRRR-Smoke operational date (2020), inputs (VIIRS/MODIS fire hot-spot + FRP), domains (CONUS + Alaska), or forecast horizon ("up to 48 hours"). The S3 access row does cite [160], but that citation (`citations.md` [160]) itself notes "HRRR-Smoke variables not separately confirmed in registry text."

**Grade:** MINOR FAIL — these claims are effectively orphan claims with no verifiable citation path.

---

## Verified as Consistent

The following items were spot-checked and found consistent across all relevant files:

| Item | Check result |
|---|---|
| GOES-19 operational date: April 7, 2025 | Consistent across `README.md`, `astrophoto-weather-apis.md`, `citations.md` [151], `satellite-nowcasting.md` |
| GOES-19 S3 bucket: `noaa-goes19` | Consistent across all files |
| Tzallas 2020 ACM overall accuracy: 86.0% | Consistent: `satellite-nowcasting.md`, `citations.md` [161] |
| Tzallas 2020 ACM cloud detection: 90.9% | Consistent: `satellite-nowcasting.md`, `citations.md` [161] |
| Tzallas 2020 ACM clear-sky detection: 74.8% | Consistent: `satellite-nowcasting.md`, `citations.md` [161] |
| Tzallas 2020 ACM daytime clear-sky: 66.6% | Consistent: `README.md`, `astrophoto-weather-apis.md`, `satellite-nowcasting.md`, `citations.md` [161] |
| Open-Meteo free-tier limits: 600/min, 5,000/hr, 10,000/day, 300,000/month | Consistent: `citations.md` [50], [73], `pricing-and-licensing.md`, `caching-rate-limit-strategy.md`, `README.md` |
| HRRR resolution: 3 km | Consistent across all files |
| HRRR standard horizon: 18h | Consistent across all files |
| HRRR extended cycles: 00/06/12/18Z, 48h | Consistent across all files |
| ECMWF IFS 47r3 cloud regression: +3–4% global, up to +15% locally | Consistent: `underlying-models.md`, `southeast-us-accuracy.md`, `astrophoto-weather-apis.md`, `citations.md` [29], [30] |
| Mode 6 cadence: Full Disk 10 min, CONUS 5 min, Mesoscale 60 sec | Consistent: `satellite-nowcasting.md`, `temporal-resolution.md`, `astrophoto-weather-apis.md`, `citations.md` [152] |
| Mode 6 cadence: Mesoscale single-domain 30 sec | Present in `satellite-nowcasting.md` (table row) and `citations.md` [152]; not in other files (those files only cite the 60-sec dual-domain figure) — not a contradiction, just incomplete propagation |
| MET Norway altitude bands: <2000 m / 2000–5000 m / >5000 m | Consistent: `provider-matrix.md`, `astrophoto-weather-apis.md`, `citations.md` [3], `README.md` |
| ECMWF sigma bounds: LCC σ>0.8, MCC σ 0.45–0.8, HCC σ<0.45 | Consistent: `provider-matrix.md`, `citations.md` [8] |
| Open-Meteo layer bands: 0–3 km / 3–8 km / 8 km+ | Consistent: `provider-matrix.md`, `astrophoto-weather-apis.md`, `citations.md` [1] |
| Meteomatics layer bands: 0–1800 m AGL / 1800–6300 m AGL / >6300 m AGL | Consistent: `provider-matrix.md`, `astrophoto-weather-apis.md`, `citations.md` [11] |
| GEFSv12 probability granularity: ~3.2% (100/31 = 3.226%) | Consistent: `ensemble-uncertainty.md`, `astrophoto-weather-apis.md` |
| ECMWF ENS probability granularity: ~2% (100/51 = 1.96%) | Consistent: `ensemble-uncertainty.md`, `astrophoto-weather-apis.md` |
| NWS rate-limit blocks: HTTP 403 not 429 | Consistent: `caching-rate-limit-strategy.md`, `astrophoto-weather-apis.md`, `citations.md` [71] |
| NWS CDN stale cache extreme: 981 hours (41 days) | Consistent: `caching-rate-limit-strategy.md`, `pricing-and-licensing.md`, `astrophoto-weather-apis.md`, `citations.md` [69] |
| Astrospheric Pro pricing: $2.99/mo, 100 credits/day, ~20 forecasts/day | Consistent across all files |
| HRRR spin-up: FH0–2, too many small objects → too few oversized by FH2 | Consistent: `underlying-models.md`, `temporal-resolution.md`, `southeast-us-accuracy.md`, `citations.md` [78] |
| HRRR delays SE US afternoon convective initiation 1–2 h | Consistent across all files citing [90] |
| HRRR overforecasts convective storm objects most in SE US | Consistent: `underlying-models.md`, `southeast-us-accuracy.md`, `astrophoto-weather-apis.md`, `citations.md` [79] |
| Persistence beats NWP for cloud cover at < 6h (Ye & Chen 2013) | Consistent across all files citing [82] |
| ECMWF ENS upgrade to 9 km: June 27, 2023 | Consistent: `citations.md` [28], `ensemble-uncertainty.md` |
| ECMWF ENS extended-range: 101 members | Consistent: `citations.md` [28], `ensemble-uncertainty.md` |
| Open-Meteo self-hosting cost: 500 GB+ storage, 2 TB+/day bandwidth, $4,800–9,000/month | Consistent: `pricing-and-licensing.md`, `caching-rate-limit-strategy.md`, `astrophoto-weather-apis.md`, `citations.md` [74] |
| ECMWF AIFS: flat cloud distribution, under-predicts clear and overcast extremes | Consistent: `underlying-models.md`, `astrophoto-weather-apis.md`, `citations.md` [32], [171] |
| Solcast AIFS irradiance bias: −8% vs IFS +2% vs GFS +5% | Consistent: `underlying-models.md`, `citations.md` [33] |
| WeatherAPI.com free tier: 100,000/month | Consistent: all files citing [64], [65] |
| HRRR summer fix: only 35% effective vs 80–84% fall/winter (James & Turner 2025) | Consistent: `underlying-models.md`, `southeast-us-accuracy.md`, `astrophoto-weather-apis.md`, `citations.md` [77] |
| ECMWF Open Data full real-time catalogue open: October 1, 2025 | Consistent: `pricing-and-licensing.md`, `astrophoto-weather-apis.md`, `citations.md` [63] |
| ECMWF Open Data 25 km publicly accessible subset (not 9 km) | Consistent in `citations.md` [63] and `pricing-and-licensing.md` gaps section — but contradicted by `underlying-models.md` and main deliverable as noted in C-03 |
| MRMS: 1 km, 2 min, 33 levels, operational since 2014 | Consistent: `satellite-nowcasting.md`, `citations.md` [158] |
| Clear Sky Chart: 6,100+ sites, 48h hard cap, no arbitrary lat/lon | Consistent: `astrophoto-aggregators.md`, `citations.md` [136], `README.md` |
| 7Timer!: GFS-only, non-commercial, global (~1.5M points) | Consistent: `astrophoto-aggregators.md`, `citations.md` [138] |
| MET Norway coordinates >4 decimal places trigger 403 | Consistent: `pricing-and-licensing.md`, `citations.md` [60] |
| ACM resolution: 2 km | Consistent: `satellite-nowcasting.md`, `citations.md` [153] |
| ACHA upgraded to 2 km on March 24, 2023 | Consistent: `satellite-nowcasting.md`, `citations.md` [155] |

---

## Reconsideration Pass

Before finalizing, reconsidering items I may have missed or accepted too readily:

1. **The ECMWF HRES 10-day vs 15-day tension (C-02):** I confirmed this is real. The `provider-matrix.md` row for "ECMWF Open Data" cites the Open Data catalogue horizon (360h / 15 days) but lists HRES-specific cloud parameters. The HRES itself runs to 240h. This creates a misleading entry. Confirmed CRITICAL.

2. **HRRR overforecast vs underforecast tension (C-05):** I was careful to note both are true in different senses. The deliverable's Reflection at line 214 says "HRRR underforecasts cloud cover in SE US summer" as a synthesis claim — this is legitimate because James & Turner 2025 [77] finds insufficient cloud attenuation (→ too little cloud), and the `underlying-models.md` conclusion (line 45) says "may underforecast cloud cover." The Skinner [79] overforecasting is for *convective storm objects* (radar-based), not cloud fraction. These are different metrics. The tension is real and unreconciled. Confirmed MODERATE.

3. **The "Mesoscale single domain 30 sec" item:** Listed in `satellite-nowcasting.md` table and `citations.md` [152] but the other files only say "Mesoscale every 60 sec." This is not a contradiction — the 30-sec mode is available only when both mesoscale sectors are combined into one. No file contradicts another; they just use the more common 60-sec figure. Confirmed PASS.

4. **ECMWF 500 connections "quota":** The README and `pricing-and-licensing.md` state "500 connections" as the ECMWF Open Data "free quota." The source ([7]) says "500 simultaneous connections" which is a concurrency limit, not a daily/monthly quota. This is accurately represented as a connection limit across all three files. Confirmed consistent.

5. **GraphCast at 0.25° described as "~25 km" in `underlying-models.md` but "~28 km" for GFS at 0.25°:** At the equator, 0.25° ≈ 27.8 km. The `underlying-models.md` table lists GraphCast as `0.25° (~25 km)` and GFS as `0.25° (~13 km native T1534, ~28 km output)`. The ~25 km for GraphCast is a slight understatement (should be ~28 km at equator). However, 25 km is a commonly used approximation for 0.25° in the atmospheric science literature, and the GFS entry correctly notes the distinction between native T1534 (~13 km) and output grid. This is a minor rounding inconsistency in the GraphCast entry (25 km vs the more accurate ~28 km) but it does not conflict with other files since GraphCast is only described once. Not escalating — this is a known conventional approximation.

6. **RAP cadence discrepancy noted in `underlying-models.md` gaps:** The file itself flags "RAP cadence: Wikipedia states 'every 3 hours' but NCEI and rapidrefresh.noaa.gov state hourly." This is a disclosed uncertainty, not an undetected inconsistency. Confirmed handled.
