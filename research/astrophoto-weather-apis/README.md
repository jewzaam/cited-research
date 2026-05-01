# Weather APIs and Multi-Layer Cloud Forecasting for Astrophotography

How an indie astrophotography session-planning app should source cloud cover for go/no-go decisions, with citation-backed accuracy and pricing data for the Southeast US (Carolinas / Piedmont / Blue Ridge).

## TL;DR

No single API solves cloud forecasting. The right architecture is **layered by lead time**, with redundancy across vendors:

| Lead time | Source | Why |
|---|---|---|
| Now / next 0–3 h | **GOES-19 ABI ACM** via `noaa-goes19` AWS S3 (free, no auth, 5-min CONUS) | Observation, not forecast — beats NWP at this horizon |
| 3–18 h | **HRRR** via Open-Meteo or NOMADS | 3 km, hourly, CONUS; FH0–2 spin-up caveat |
| 18–48 h | **HRRR Extended** (00/06/12/18 Z) | 48-hour CONUS forecast |
| 2–10 days | **ECMWF IFS** (Open Data, free since Oct 2025) + **ECMWF ENS** for probability | Highest medium-range skill globally |
| Cross-check | **MET Norway** layered cloud (free, no key) | Independent feed |

GOES-19 became operational GOES-East on April 7, 2025, replacing GOES-16. Use `noaa-goes19`.

## Why this is harder than it looks

- **Layer definitions are not interoperable.** ECMWF uses sigma coordinates, WMO uses latitude-dependent altitude, NOAA SPC uses pressure cutoffs, Open-Meteo derives from RH at pressure levels. The same physical cloud is reported as `low` by NOAA, `mid` by ECMWF/Meteomatics/MET Norway, and split between `low/mid` by Open-Meteo. Multi-provider apps must harmonize before display.
- **Half the major APIs only expose aggregate `cloudCover`** — not multi-layer. NOAA NWS, OpenWeatherMap, Tomorrow.io, Visual Crossing all expose a single percentage.
- **HRRR delays SE US afternoon convective initiation by 1–2 hours** (NSSL EWP 2024). Evening clearing forecasts after summer storms are systematically too aggressive.
- **Persistence beats short-horizon NWP.** Ye & Chen 2013 (MNRAS): persistence is best for cloud forecasting at lead times under 6 hours. For 0–3 hours, satellite-observed cloud + extrapolation beats forecast.
- **AI weather models (GraphCast, Pangu, FourCastNet) do not output cloud cover.** ECMWF AIFS does, with documented flat-distribution bias (under-predicts both clear and overcast extremes).
- **"70% chance of clear" is structurally hard.** Cloud cover ensembles are systematically underdispersive (Hemri et al. 2016); intermediate probabilities are physically sparse (cloud is bimodal at 0/8 oktas); standard EMOS post-processing fails for cloud where it succeeds for temperature.

## Provider matrix at a glance

| Provider | Layered cloud? | Free quota | Commercial-use OK on free? | Best use |
|---|---|---|---|---|
| **Open-Meteo** | Yes (low/mid/high) | 10K/day | **No** (non-commercial only) | Primary forecast for non-monetized apps |
| **MET Norway** | Yes (low/medium/high) | unbounded (>20 req/s = "heavy") | Yes | Cross-check feed |
| **Meteomatics** | Yes (low/medium/high) | 500/day | **No** (private only) | Not viable at indie scale |
| **ECMWF Open Data** | Yes (LCC/MCC/HCC) | 500 connections | Yes (CC-BY-4.0) | Medium-range outlook |
| **NOAA NWS** | Aggregate `skyCover` only | unbounded by quota | Yes (public domain) | Backup/cross-check |
| **OpenWeatherMap** | Aggregate only | 1M/month | Yes (with attribution) | Aggregate-cloud fallback |
| **WeatherAPI.com** | Aggregate only | 100K/month | Yes (with attribution) | Commercial-OK fallback |
| **Astrospheric Pro** | Curated (RDPS+GFS+NAM+NBM) | $2.99/mo, 100 credits/day = ~20 forecasts/day | API exists | UI reference, not backend |
| **Astrospheric web/app** | Curated | Free | N/A — no API | Cross-check via web |
| **Clear Outside** | Yes (low/medium/high) | Free, no API | N/A | Embed widget |
| **Clear Sky Chart** | Curated | Free, no API; fixed sites only | N/A | Reference UX |
| **Meteoblue Astronomy** | Yes (0–4/4–8/8–15 km) | Free 3-day; paid €1,200+/yr API | (paid commercial) | Global niche |
| **7Timer!** | Yes via GFS | Free open API | **No** (non-commercial) | Free global cross-check |

## Quick decision framework

1. **Is the app commercial (ads, subscription, app-store revenue)?** If yes, Open-Meteo non-commercial is off-limits — use WeatherAPI.com Free + MET Norway + ECMWF Open Data, or pay $29/mo for Open-Meteo Standard.
2. **Does the user need transparency-sensitive multi-layer cloud?** If yes, route to Open-Meteo or MET Norway for layered cloud. Aggregate-only providers (NWS, OWM, Visual Crossing) are insufficient. Harmonize layer definitions before display.
3. **Is the user in CONUS (including SE US)?** Use HRRR for 0–18 h; HRRR Extended for 18–48 h; ECMWF for 2–10 days. Outside CONUS, HRRR doesn't apply — fall back to ECMWF and ICON.
4. **Does the app need observation-now ("is it clear right now?")?** Add GOES-19 ABI ACM (`noaa-goes19` AWS S3, no auth, 5-min CONUS). Treat ACM as a "definitely cloudy" filter rather than "definitely clear" — daytime clear-sky accuracy is only 66.6%.
5. **Does the app need probability ("70% chance of clear")?** Use Open-Meteo Ensemble API or `ecmwf-opendata` to fetch per-member cloud cover; compute P(clear) client-side; **label it as raw ensemble fraction, not calibrated probability**.

## Confidence note for Southeast US specifics

The deeper accuracy findings for the Southeast US (Carolinas / Piedmont / Blue Ridge) rest on **moderate evidence, not strong**: no peer-reviewed cloud-cover verification study targets this region directly. The closest direct evaluation is HRRRv2 in northern Alabama (Burlingame 2019). Quantitative HRRR/GFS/ECMWF accuracy claims here are inferred from CONUS-wide studies (SURFRAD, USCRN, NY State Mesonet) plus the Skinner 2021 finding that HRRR convective object overforecasting is most pronounced in the SE US. Phase 4 audit flagged this dimension's confidence as the lowest in the document (~0.35 vs ~0.7 for other dimensions). Readers should treat SE-US-specific quantitative claims as directional rather than authoritative.

## Files in this directory

| File | Content |
|------|---------|
| [astrophoto-weather-apis.md](astrophoto-weather-apis.md) | Full deliverable with cross-cutting analysis |
| [citations.md](citations.md) | All sources, numbered, tier-rated |
| [references/provider-matrix.md](references/provider-matrix.md) | Which APIs expose layered cloud — and how their definitions differ |
| [references/underlying-models.md](references/underlying-models.md) | HRRR, GFS, ECMWF, ICON, AROME, AI models — specs and biases |
| [references/pricing-and-licensing.md](references/pricing-and-licensing.md) | Free/paid tiers, attribution, commercial-use restrictions |
| [references/southeast-us-accuracy.md](references/southeast-us-accuracy.md) | Documented HRRR/GFS/ECMWF accuracy in SE US |
| [references/temporal-resolution.md](references/temporal-resolution.md) | Sub-hourly cloud cover — mostly an illusion |
| [references/ensemble-uncertainty.md](references/ensemble-uncertainty.md) | Probabilistic forecasting — calibration limits |
| [references/caching-rate-limit-strategy.md](references/caching-rate-limit-strategy.md) | Practical engineering for indie apps |
| [references/astrophoto-aggregators.md](references/astrophoto-aggregators.md) | Astrospheric, Clear Outside, Meteoblue, CSC, 7Timer |
| [references/satellite-nowcasting.md](references/satellite-nowcasting.md) | GOES-19 ABI L2 cloud, MRMS, HRRR-Smoke |
| [audit/citation-audit.md](audit/citation-audit.md) | Independent citation verification (Phase 4) |
| [audit/consistency-review.md](audit/consistency-review.md) | Cross-file consistency (Phase 4) |
