# Atmospheric Obstructions for Astrophotography

Forecasting and reacting to non-cloud atmospheric obstructions — pollen,
wildfire smoke, Saharan dust, urban aerosols, and volcanic stratospheric
haze — for an astrophotography planning app. Southeast US (NC) primary,
global parity for v2.

## TL;DR

The standard astro-weather forecast (cloud cover, seeing, dew point) has
a particulates blind spot. Closing it requires **distinct signals for
two different decisions**:

1. **Will the night be transparent?** → column AOD (not surface PM2.5).
2. **Is it safe to deploy expensive optics?** → pollen + dust deposition.

Surface PM2.5 monitors measure neither well. They poorly predict column
AOD (R = 0.03–0.60 across 19 China stations [11]) and they are not
designed to forecast equipment-contamination risk.

## Recommended primary data sources

| Decision | Primary | Secondary | Notes |
|---|---|---|---|
| Tonight's transparency (column) | **CAMS dust+aerosol AOD** [33] OR **AERONET nearest** [73] | HRRR-Smoke COLMD [53] for wildfire periods | Skip surface PM2.5 as a transparency proxy |
| Tonight's surface air quality | **AirNow** [23] | EPA-corrected PurpleAir [18, 28] | Show as separate health indicator |
| Pollen / equipment risk | **Google Pollen API** [35] | NC State pine pollen GDD model [42] for SE-US window | Pine = visible yellow film, not the dominant allergen |
| Wildfire smoke transport | **HRRR-Smoke COLMD** [53] | CAMS [33] for global; NOAA HMS [55] for now-state | Forecast skill r ≤ 0.50 — surface uncertainty [59] |
| Saharan dust (June–Aug SE-US) | **CAMS dust AOD** [68] | NOAA AOML SAL hub [66] | SAL base ~1 mi above surface, layer 2–2.5 mi thick — column matters |
| Volcanic / stratospheric | GloSSAC baseline [98] + Smithsonian GVP weekly | TROPOMI SO₂ [99] | Background most of the time; activate on VEI ≥ 5 |

See [citations.md](citations.md) for full source list.

## Quick decision framework for a planning-app night-of forecast

1. **Pull column AOD** at 550 nm from AERONET nearest station [73] or
   CAMS forecast [33]. Convert to per-band Δm (mag/airmass at zenith)
   via `Δm = 1.086 × AOD(λ)` [4].
2. **Apply Ångström exponent** for the dominant aerosol regime [5]:
   - Wildfire smoke active → α ≈ 1.7 (fine-mode)
   - Saharan dust active → α ≈ 0.3 (coarse-mode)
   - Routine urban → α ≈ 1.5 (fine-mode default)
3. **Display per-band Δm** for V (broadband planning), Ha (narrowband),
   OIII (narrowband). Note OIII suffers more than Ha during fine-mode
   events.
4. **Surface PM2.5 separately** for human comfort, with regulatory source
   (AirNow) preferred over corrected PurpleAir during dust events [19].
5. **Trigger equipment-protection alerts** independently:
   - Pollen >1,500 grains/m³ with **pine** named → "consider deferring
     SCT/exposed-corrector deployment"
   - Active SAL outbreak in season → "silica abrasion risk; clean
     before next session"
6. **Stratospheric haze advisory** runs in background; surface only
   when GloSSAC anomaly > 0.02 SAOD or after VEI ≥ 5 eruption [91, 98].

## Severity scale (synthesis, not a standard convention — all tier boundaries est.)

| ΔV (mag/airmass) | Severity | Imaging rec |
|---|---|---|
| < 0.05 (est.) | Excellent | Full session — broadband + narrowband + planetary |
| 0.05 – 0.15 (est.) | Good | Slight extinction; broadband fine, narrowband fine |
| 0.15 – 0.40 (est.) | Degraded | Shorter exposures or favor narrowband (Ha less affected) |
| > 0.40 (est.) | Poor | Limited deep-sky utility; planetary at zenith may still work |

Severity tiers are a synthesis from this research; not an established
astronomical convention. Pinatubo's local AOD peak of 0.4 [86]
translates to ~0.43 mag/airmass at zenith (calculated, est.) — the
upper-bound anchor.

## Files

| File | Content |
|---|---|
| [atmospheric-obstructions-guide.md](atmospheric-obstructions-guide.md) | Full deliverable with API tradeoffs, decision algorithms, and gap analysis |
| [citations.md](citations.md) | All 108 sources, numbered, tiered, with verification status |
| [references/pollen-data-sources.md](references/pollen-data-sources.md) | Google Pollen, Ambee, Tomorrow.io, NC DEQ, NAB, GDD model |
| [references/wildfire-smoke-forecasting.md](references/wildfire-smoke-forecasting.md) | HRRR-Smoke, NAQFC, CAMS, FIRMS, HMS, AirNow F&S Map; forecast skill |
| [references/saharan-dust-transport.md](references/saharan-dust-transport.md) | CAMS dust, AOML SAL, AERONET, Worldview, Barcelona DRC, ICAP |
| [references/aerosols-and-pm25.md](references/aerosols-and-pm25.md) | AirNow, OpenAQ, PurpleAir, EEA, WAQI, IQAir, Sensor.Community |
| [references/particulates-to-imaging-impact.md](references/particulates-to-imaging-impact.md) | AOD→Δm physics, observatory baselines, Ångström, narrowband |
| [references/equipment-protection-thresholds.md](references/equipment-protection-thresholds.md) | Vendor positions, NC pine pollen specifics, deposition risks |
| [references/regional-priority-matrix.md](references/regional-priority-matrix.md) | Which signals matter where/when |
| [references/source-conflict-resolution.md](references/source-conflict-resolution.md) | Barkjohn correction, dust failure, fusion vs disagreement |
| [references/volcanic-stratospheric-haze.md](references/volcanic-stratospheric-haze.md) | Hunga Tonga, Pinatubo, pyroCb, VAACs, USGS, Hawaii VOG |
| [audit/citation-audit.md](audit/citation-audit.md) | Phase 4: isolated agent verifies cited claims against sources |
| [audit/consistency-review.md](audit/consistency-review.md) | Phase 4: isolated agent verifies internal consistency |

## Honest gaps

- **Pollen → astronomical magnitude conversion** is undocumented. No
  paper provides grains/m³ → V-band Δm for pine specifically.
- **The widely-quoted "5–7 minute corrector contamination window" claim**
  [76] traces to one Tier 3 source whose page returned 403 during this
  research — not independently verified.
- **Pinatubo / Hunga Tonga in standard amateur photometric magnitudes**
  is missing from the literature; observatory-tier data only.
- **Wildfire smoke deposition on telescope optics**: undocumented gap.
- **No standard insurance product** for contamination damage.

See the main [guide](atmospheric-obstructions-guide.md) for a fuller
gaps-and-limitations section and Phase 4 audit reports for what was
re-verified and what was accepted on Phase 1 confidence.
