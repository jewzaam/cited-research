# Temporal Resolution: Hourly vs Sub-Hourly Cloud Forecasts

**Dimension covered:** Whether sub-hourly (15-min, 5-min) cloud cover is available from any free source, whether it has actual skill or is interpolation, and whether it changes session-planning decisions for astrophotography.

Sources: [`citations.md`](../citations.md).

## Headline finding

**No major free API provides genuinely skillful sub-hourly cloud cover forecast for the Southeast US.**
- HRRR's sub-hourly product (`wrfsubhf`) **does not include cloud cover variables** [19].
- Open-Meteo's `minutely_15` cloud cover is **interpolated from hourly**, not native [91], [92].
- MET Norway's Nowcast covers Norway/Sweden/Finland/Denmark only — irrelevant for SE US [93], [94].
- HRRR sub-hourly fields between hourly outputs are produced via wgrib2 linear time interpolation; no new meteorological information enters at the interpolated steps [98].

For lead times under ~3 hours, **satellite extrapolation (GOES-19 ABI at 5-min CONUS cadence)** is the genuinely sub-hourly cloud signal [95], [149], [152].

## Sub-hourly availability table

| Source | Native sub-hourly cloud cover? | Interpolation? | Region | Cadence | Notes | Cite |
|---|---|---|---|---|---|---|
| HRRR `wrfsubhf` | **No** — TCDC/LCDC/MCDC/HCDC absent | N/A (cloud not exposed) | CONUS | 15 min | Variables present: REFC, RETOP, VIL, DSWRF, precip types, ceiling/base/top heights, simulated GOES brightness temps | [19] |
| HRRR `wrfsfcf` (hourly) | LCDC/MCDC/HCDC/TCDC present | Hourly only | CONUS | 1 h | Source for hourly cloud fields | [20] |
| Open-Meteo `minutely_15` (NA) | **No (cloud interpolated)** | Linear from hourly HRRR | CONUS | 15 min | Native variables: T2m, RH, dew point, radiation, lightning, precip, wind. Cloud cover requires interpolation | [91], [92] |
| Open-Meteo `minutely_15` (Europe) | (varies — ICON-D2 / AROME native for some variables) | (varies) | Central Europe | 15 min | Closer to native sub-hourly via ICON-D2 (2.2 km, 3-hourly cycles) | [91] |
| Open-Meteo `minutely_15` (other) | **No (all interpolated)** | Linear from hourly | Global | 15 min | Outside NA / Central Europe, no native sub-hourly model | [91] |
| MET Norway Nowcast 2.0 | **No cloud cover at all** | N/A | Nordic only (Norway/Sweden/Finland/Denmark) | 5 min | Variables: weather symbol, T2m, precip rate/amount, RH, wind. No `cloudAreaFraction` | [93], [94] |
| GOES-19 ABI ACM | Observed cloud mask (not forecast) | N/A | Western Hemisphere; CONUS sector | 5 min CONUS, 60 sec mesoscale | Cloud detection (4 classes), not forecast | [149], [150], [152] |
| RAP | Hourly only — no sub-hourly product | N/A | North America | 1 h | RAP initializes HRRR; no sub-hourly outputs | [23] |

## Why sub-hourly NWP cloud is unreliable

### Operational cadence vs internal time step
**Mathiesen & Kleissl 2011 [81]:** Despite NWP internal time steps being on the order of minutes, operational model output is hourly (NAM) or every 3 hours (GFS, ECMWF). Therefore **"any patterns with characteristic time scales less than an hour are unresolved"** — a structural limitation, not a deployment choice.

### Solar industry practice
**Chu et al. 2021 [97]** (iScience review of intra-hour solar irradiance forecasting): "To the best of the authors' knowledge, neither NWP or WRF methods have been adopted operationally for intra-hour horizons by solar power plant managers over several years and under multiple seasons." The reason: **"the inherent temporal resolutions (>5 min) of RS and NWP models are inadequate for the relatively short forecast horizon."**

The solar energy industry — which has strong financial incentive to use every available signal — has rejected sub-hourly NWP for intra-hour forecasting. This is the strongest practical evidence that sub-hourly NWP cloud data does not add skill.

### Persistence beats NWP at sub-hourly horizons
**CloudCast 2024 [95]:**
- NWP MEPS (Norwegian operational ensemble) achieves a flat MAESS ~0.3 across all lead times for cloud cover.
- Eulerian persistence achieves perfect score at 0 lead time, drops to half by 1 hour.
- EXIM optical-flow nowcasting **falls below persistence at the 15-minute mark**.
- ML-based CloudCast (CNN on satellite imagery) achieves MAESS ~0.75 at 15-min lead — but this is observation-driven, not NWP.

**Lyman & Mahoney [96]** (mountain terrain): Cloud nowcast methods using wind displacement vectors **cannot beat simple persistence** over complex terrain (Utah/Wyoming); persistence leads by up to 10% CSI in winter. Direct relevance for Appalachian / Blue Ridge sites where SE US dark-sky observation occurs.

**Renewable & Sustainable Energy Reviews 2021** (cited in Dim 5 counter-discovery): Hourly-updated NWP (RAP/HRRR), Kalman-filtered or not, "do not possess significant advantage over the arguably simpler time series methods, in particular, the optimal convex combination of climatology and persistence." If even hourly NWP barely beats persistence, sub-hourly interpolated NWP cannot plausibly add further skill.

### HRRR spin-up artifact at FH0–2
HRRR has a documented pattern in its first forecast hours: too many small cloud objects at initialization, transitioning to too few oversized objects by FH2 [78]. The 1-hour forecast is "most accurate" only because subsequent hours are worse — not because it is good in absolute terms. Sub-hourly output sliced from this regime inherits the spin-up dynamics.

### wgrib2 time interpolation mechanics
**wgrib2 documentation [98]:** Sub-hourly HRRR fields between F+H and F+H+1 are produced via linear time interpolation. No mechanism exists for new meteorological information to enter at interpolated steps — the 15-min point at F+H+0.25 is mathematically `0.75 × F+H + 0.25 × F+H+1`.

## ML-based satellite nowcasting beats NWP at sub-hour
**CloudCast 2024 [95]:**
- ML model (CNN trained on satellite) achieves MAESS ~0.75 at 15-min lead.
- Maintains skill through the first hour.
- Outperforms NWP MEPS interpolated to 15-min by ~0.1 MAESS margin consistently.
- Skillful horizon: ~3 hours (beyond which ML extrapolation degrades).

**Implication:** For 0–3 hour cloud nowcasting, satellite-driven ML beats interpolated NWP. The right architectural choice for sub-hourly cloud is **observation-based** (GOES ABI ACM via NOAA Big Data Program — see [`satellite-nowcasting.md`](satellite-nowcasting.md)), not NWP-based.

## Practical session-planning utility for astrophotography
- Major astrophotography weather services (Astrospheric, Clear Outside, Clear Sky Chart, Scope Nights) all operate at **hourly resolution** [124], [129], [134].
- No astrophoto-specific weather product provides sub-hourly cloud forecasts.
- The MNRAS astronomy cloud-forecast study [82] used 3-hourly GFS and treated this as adequate.
- Practical session-planning decisions:
  - **Drive-to-site decision** (3+ hours ahead): hourly cadence is sufficient.
  - **Setup time decision** (60–90 min before imaging): hourly cadence is sufficient.
  - **Mid-session "is cloud arriving?"**: this is where sub-hourly observation (GOES ABI ACM at 5 min CONUS) matters — not sub-hourly NWP forecast.
  - **Subexposure-level abort decisions** (during a single 5-min sub): handled by all-sky cameras and human eyes, not weather APIs.

The use case for sub-hourly cloud data is real but maps to **observational** sources (satellite + all-sky camera + persistence), not to forecast models.

## Summary table — when each cadence matters

| Lead time | Best signal | Why |
|---|---|---|
| 0 – 30 min | All-sky camera + GOES-19 mesoscale (60 sec) | Observed; visual confirmation [149], [152] |
| 30 min – 3 h | GOES-19 ABI ACM (5 min CONUS) + ML extrapolation if available | Observation-driven nowcast skill exceeds NWP [95] |
| 3 h – 6 h | HRRR hourly (with persistence cross-check) | NWP regime where short-range models start to add value [82] |
| 6 h+ | HRRR / GFS / ECMWF hourly | Standard NWP forecast horizon |

## Gaps and limitations

- The **CloudCast paper's MAESS values** (0.75 ML, 0.3 NWP, EXIM-below-persistence-at-15-min) are sourced from a prose description of Fig. 5c in the Discovery agent's snippet extraction; the exact figure data was not extracted from the paper itself. Phase 4 verification should re-fetch and verify the specific numbers against the published figure [95].
- **HRRR `wrfsubhf` later forecast hours** (FH01+) inventory was not directly fetched; cloud-related variables might appear in later hours but the FH01 inventory page returned 404. This is unlikely (the FH00 base inventory is the documented schema), but should be verified [19].
- **HRRR GOES brightness temperature variables** (SBT113/114/123/124) are present in the sub-hourly product as simulated brightness temperatures. Whether these can serve as a practical cloud-cover proxy at 15-min cadence for applications that cannot use TCDC was not evaluated.
- **Open-Meteo's interpolation method** for cloud cover at minutely_15 was confirmed as "interpolation" but the exact algorithm (linear, cubic, persistence-weighted) was not documented [91], [92].
- **Tomorrow.io / Visual Crossing / Pirate Weather sub-hourly cloud cover** availability at native resolution was not fully evaluated; agent findings indicate they do not provide native sub-hourly cloud, but enterprise tiers were not exhaustively checked.
- **No published study** directly tests whether astrophotographers using 15-minute vs hourly cloud forecasts make different go/no-go decisions. The conclusion that hourly cadence is sufficient for session planning is supported by industry practice (every major astrophoto weather tool uses hourly) but is not empirically validated against a controlled comparison.
