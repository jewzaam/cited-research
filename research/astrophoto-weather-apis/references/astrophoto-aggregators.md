# Astrophotography-Specific Weather Aggregators

**Dimension covered:** Existing astrophoto-specific weather sites/APIs that already aggregate multi-layer cloud cover and astronomy-relevant variables. Astrospheric, Clear Outside, Meteoblue Astronomy, Clear Sky Chart, 7Timer!, plus aggregator vs raw-API tradeoff.

Sources: [`citations.md`](../citations.md).

## Headline finding

**The build-vs-buy decision favors raw APIs (with caveats) for any app that needs:** geographic flexibility (Astrospheric and Clear Sky Chart cover only North America), API access (Astrospheric Pro is the only one with a usable astronomy-specific API at $2.99/mo for 100 credits/day = ~20 forecasts), or transparency about model provenance.

**Aggregators are useful as cross-checks** but are wrappers on 2–3 primary NWP feeds (RDPS, GFS, ECMWF, ICON) — checking two aggregators that share a feed gives the illusion of independent confirmation while providing none.

## Aggregator comparison table

| Aggregator | Data source | API? | Free? | Geographic coverage | Variables | Forecast horizon | Cite |
|---|---|---|---|---|---|---|---|
| Astrospheric | RDPS (primary, 6h cycles), GFS, NAM, RAP (smoke), NBM (1h, 36h, blends 40+ models incl. HRRR/ECMWF) | Yes — REST API requires Pro membership | Free web/app; $2.99/mo or $29.99/yr Pro for API | CONUS + Canada + partial Mexico (excludes Hawaii) | Cloud, transparency, seeing (0–5 Allan Rahill CMC algorithm), T, dew, wind, sun/moon/planets, ISS, wildfire smoke (AOD via GFS) | 81-hour API; ~7-day web | [124], [125], [126], [127] |
| Clear Outside | Powered by Meteosource Weather API (commercial aggregator) — likely GFS + ICON + ECMWF blend | No public API; embed widget only | Free | Global (UK-default display) | Low/medium/high cloud + total obscuration (%), dew, fog, RH, T, wind, precip, moon phase, sun, twilight, Bortle, magnitude limit, ISS, ozone | 7 days | [129], [130] |
| Meteoblue Astronomy view | Proprietary NEMS (NEMS = GFS-based; NEMS_E = ECMWF-based); also ingests GFS, ECMWF IFS, DWD ICON, AROME ARPEGE | Yes — paid commercial API tiers | Free 3-day; paid 7-day; API €0 / €1,200 / €2,400 / €4,800/yr | Global | Cloud at 0–4 / 4–8 / 8–15 km ASL; Seeing Index 1 (turbulent layer integration), Index 2 (density/flicker); jet stream; "bad layers"; visible planets | 3 days free / 7 days paid | [131], [132], [133] |
| Clear Sky Chart (cleardarksky.com) | CMC GEM (primary, processed by Allan Rahill); ECMWF added 2020 to some charts | No public API; static PNG charts | Free | North America; 6,100+ fixed sites; **no arbitrary lat/lon** | Cloud (with cirrus-specific modeling), transparency, seeing, sky darkness, wind, RH, T | 48 hours (hard cap) | [134], [135], [136] |
| 7Timer! | GFS only (~20 km / 0.25°) | Yes — free open API (PNG + JSON/XML); non-commercial only | Free | Global (~1.5M points) | Cloud, lifted index (seeing proxy), atmospheric transparency, T2m, RH2m, wind, precipitation type/amount, MSL pressure | 3 days for ASTRO product | [138] |

## Astrospheric in depth

**Models [124]:**
- Primary: Canadian Meteorological Centre Regional Deterministic Prediction System (RDPS), 6-hour cycles. RDPS is the basis for Allan Rahill's seeing/transparency methodology.
- Secondary: GFS (aerosol optical depth, long-range cloud, jet stream) — 6h cycles.
- NAM, 6h cycles.
- RAP (NOAA experimental) — smoke variables.
- NBM (National Blend of Models) — 1-hour cycles, 36-hour horizon. Astrospheric describes NBM as blending "40+ models including ECMWF and HRRR."
- Ensemble view [109]: combines RDPS + ICON + GFS + NBM with per-model percentages and color-coded agreement.

**API [126]:**
- Endpoint: `https://astrosphericpublicaccess.azurewebsites.net/api/`
- Authentication: requires Pro membership.
- Quota: 100 credits/day. `GetForecastData_V1` = 5 credits/call → ~20 forecast calls/day per Pro account; `GetSky_V1` = 1 credit/call → 100 sky calls/day.
- Returns 81-hour forecast at lat/lon.

**Pricing [127]:** Free tier (web/app); Pro $2.99/month or $29.99/year.

**Coverage [125]:** Continental US + Canada + partial Mexico. RDPS excludes Hawaii. NBM has a smaller sub-domain (CONUS + Alaska only). **Southeast US is within RDPS domain** — Astrospheric is fully usable for Carolinas / Piedmont / Blue Ridge.

**Self-disclosure [128]:** Astrospheric's own FAQ states **"It will be wrong at times. Even the Cloud Ensemble will be wrong at times."** RDPS generates 200M+ predictions per 6-hour cycle; errors are inevitable. Worldwide expansion described as "prohibitively expensive."

**Practitioner experience [139], [144], [145]:** Generally top-ranked for North American astrophotographers. Documented failure modes: lake-effect clouds in Ontario [139]; occasional false-clear and false-cloudy in both directions [144]. AstroBackyard reports it as their go-to tool, paired with GOES-16/Zoom Earth satellite for near-real-time go/no-go [145].

**For an app builder considering Astrospheric:** the API access at $2.99/month is unique among astrophoto aggregators. The 100 credits/day = 20 forecast calls/day quota is **structurally inadequate** for a session-planning app querying multiple user locations. No higher-volume B2B tier is publicly documented.

## Clear Outside in depth

**Data sources [129], [130]:**
- Live website footer: "Powered by Meteosource Weather API" — a commercial aggregator that itself draws on GFS, ICON, ECMWF, and others.
- 2022 First Light Optics blog [130] attribution: aggregate of UK Met Office, Norwegian Met Office, NOAA. The exact current model stack is opaque (Meteosource doesn't publicly enumerate which models it uses for which output).
- The original AROME attribution sometimes cited in third-party astronomy sites is not confirmed by Clear Outside.

**API:** No documented public API. Embed/widget only.

**Pricing:** Completely free. No paid tier.

**Coverage:** International on the web (default UK-centric display). Works at any lat/lon globally.

**Variables [129]:**
- Low, medium, high cloud cover + total cloud obscuration (%)
- Dew point, RH, fog probability, visibility
- Temperature, wind speed/direction
- Precipitation type/probability/amount
- Moon phase, rise/set, illumination
- Sun rise/set, civil/nautical/astronomical twilight windows
- Bortle scale classification (light pollution estimate)
- Estimated magnitude limit
- ISS pass times (calculated for exact lat/lon)
- Ozone levels

**Notable absences:** No seeing or transparency index — significant gap vs Astrospheric and Clear Sky Chart.

**Reputation:** Top recommended beginner-friendly tool. Considered less predictive than Astrospheric. Reportedly biased toward "cloudy when it could still be usable" (Stargazers Lounge community reports [144]).

**For an app builder considering Clear Outside:** No API → not usable as a backend data source. Useful as a visualization to embed; user-experience reference for what variables astrophotographers expect.

## Meteoblue Astronomy in depth

**Data sources [131], [132]:**
- Proprietary NEMS model family. Standard NEMS builds on GFS assimilation; NEMS2/NEMS_E variant builds on ECMWF assimilation.
- Also ingests GFS, ECMWF IFS, DWD ICON, AROME ARPEGE.
- The "METEOBLUE" consensus model blends ~20 models; the astronomy view uses NEMS as primary.
- The specific model powering the seeing index is not disclosed publicly.

**API [133]:**
- Free tier: 3-day forecast (no charge, program requirements apply).
- Paid: Bronze €1,200/yr, Silver €2,400/yr, Gold €4,800/yr.
- Credits-based: basic_1h forecast costs 8,000 credits/call; 200M credits = 25,000 calls.
- Astronomy widget available.

**Coverage [131]:** Global ("available for all places in the world").

**Variables (Astronomy Seeing view) [131]:**
- Cloud cover at 0–4 km, 4–8 km, 8–15 km ASL.
- Seeing Index 1 (turbulent layer integration approach).
- Seeing Index 2 (emphasizes density fluctuation / air flickering).
- Arcsecond measurement derived from seeing indices.
- Jet stream speed (>35 m/s correlates with poor seeing).
- "Bad layers" (temperature gradients >0.5 K/100m).
- Visible planets with azimuth, altitude, RA/Dec.

**Limitations:** Meteoblue's own documentation [131] labels the seeing index "experimental" and states "values may not reflect precisely reality"; fog excluded entirely; forecast unreliable above 4,000m. Astronomy view not available in mobile app (web-only for seeing detail).

**For an app builder considering Meteoblue:** Global coverage and explicit seeing index are unique. Pricing is steep for indie scale (€1,200/yr minimum for paid API). The seeing index methodology is not published in detail — Fried parameter formula not disclosed.

## Clear Sky Chart in depth

**Data sources [134], [135]:**
- Primary: Canadian Meteorological Centre (CMC) GEM (Global Environmental Multiscale) model. Allan Rahill's processing step specifically models cirrus clouds — a distinguishing feature.
- ECMWF forecast data added in 2020 to some charts (per Wikipedia [134]; exact charts/variables not documented on the official site).
- Author Attilla Danko has died; site maintenance is presumed continuing through community contributors. Active news pages observed through 2024.

**API:** No documented public API. Web-only. Charts are static PNG images. A community GitHub project (BGCastro89/nearest_csc) shows that image URL patterns can be accessed programmatically, but no official API exists.

**Pricing:** Free, web-only.

**Coverage [136], [137]:** Over 6,100 fixed sites in Canada, US, parts of Mexico and Caribbean. **Point forecasts only — 9-mile radius per chart. No arbitrary lat/lon lookup.** Southeast US sites exist (e.g., Houston, Atlanta, Charleston) but coverage density varies.

**Variables [134]:**
- Cloud cover (with cirrus-specific modeling)
- Astronomical transparency
- Astronomical seeing
- Sky darkness (Schaefer/Sugarman + Cinzano light pollution atlas)
- Wind, RH, T
- Forecast horizon: **48 hours hard cap**.

**Practitioner accuracy reports [141]:**
- 80% accuracy for "mostly clear" forecasts <12 hours ahead.
- 76% accuracy at 36–48 hours.
- One user reported 90% accuracy.
- Pixel-resolution critique: "varies by pixel" on the coarse grid.

**Documented failure case [140]:** A user drove 1.5 hours based on CSC "perfect conditions" and found 100% cloud cover; another gave up on CSC after a 3-day rain event under "good" CSC forecast.

**For an app builder considering Clear Sky Chart:** No API and fixed-site-only architecture rule it out as a backend data source. Useful as a reference UI design (the chart format is iconic) and as a cross-check for nearby sites.

## 7Timer! in depth

**Data source [138]:** Sole NWP source: NOAA/NCEP GFS. No multi-model blending, no regional high-resolution model.

**API [138]:**
- Graphical: PNG output via `astro.php?lon=X&lat=Y`.
- Data: JSON/XML via `api.pl?lon=X&lat=Y&product=astro&output=json`.
- No authentication required.
- Non-commercial use only per terms.

**Pricing:** Entirely free; non-commercial only.

**Coverage [138]:** Global at ~20 km (GFS 0.25°, ~28 km at equator). Cited as "1.5 million geographic points."

**Variables (ASTRO product) [138]:**
- Cloud cover
- Lifted index (seeing proxy)
- T2m, RH2m
- 10m wind speed and direction
- Precipitation type and amount
- Astronomical seeing (derived from lifted index)
- Atmospheric transparency
- MSL pressure
- Snow depth

**Forecast horizon:** 3 days for ASTRO product.

**Critique [143]:** Independent practitioner evaluation (Phil Hart) — "the seeing appears to almost always forecast a worst case"; GFS "not quite as good in terms of resolution as the Canadian model." 7Timer's seeing derivation methodology is not documented.

**For an app builder considering 7Timer:** Free open API + global coverage are unique. Non-commercial restriction blocks commercial use. GFS-only limits resolution and accuracy vs regional models. Best-suited for a quick global cross-check, not a primary data source.

## Build-vs-buy analysis

### When aggregators add value
- **Astrospheric** for North American astrophotographers wanting curated cloud/seeing/transparency without build effort. Limited by 100 credits/day API quota for app builders.
- **Meteoblue** for global coverage with explicit seeing index. Limited by paid-API pricing.
- **Clear Outside** as a reference UX/embed.
- **Clear Sky Chart** as a regional cross-check, not a primary data source.

### When raw APIs are better
- **Geographic flexibility** beyond North America (Astrospheric, CSC fail) or beyond Europe (Clear Outside / Meteoblue degraded).
- **Per-location query at scale** (CSC has fixed sites; Astrospheric Pro caps at 20/day).
- **Custom seeing/transparency derivation** (jaglab.org [147] and Home Assistant AstroWeather [146] demonstrate DIY parity using Open-Meteo + temperature/dew spread + wind + humidity).
- **Multi-model ensemble at any threshold** (aggregators' ensembles are 4-model blends; full ECMWF ENS at 51 members is more flexible).
- **Transparency about model provenance** (Meteosource doesn't publicly enumerate; Meteoblue NEMS family is opaque).

### When practitioner consensus says "use multiple sources"
**Cloudy Nights community consensus [142]:** Multi-app consensus (Astrospheric + Clear Outside + Clear Sky Chart + 7Timer + InTheSky + MetCheck + Meteoblue) **does not guarantee accuracy** — the cited thread title is "7 forecasts all agree but the sky doesn't." The aggregators share underlying NWP feeds, so their agreement is not statistical confirmation.

The robust pattern is: 2–3 *independent-feed* sources (e.g., HRRR via Open-Meteo + ECMWF via Open Data + GOES-19 ABI ACM observed) cross-checked, not 5 aggregators that all wrap GFS.

## Aggregator-level critique of seeing forecasts

The seeing index across all aggregators rests on shaky empirical ground:
- **Ye & Chen 2013 [82]** (MNRAS, peer-reviewed astronomy validation): GFS-based seeing forecasts (which underlie 7Timer) achieve cloud detection probability 30–90% (lower bound is worse than coin flip); seeing RMSE 0.2–0.4″. The paper attributes this to "poor capability of GFS/AXP model to simulate the effect of turbulence near ground and on sub-kilometer scale" and concludes the GFS forecast "may not be comparable with the human-participated forecast" — only "suitable for basic observing reference."
- **SPIE 2023 paper on optical turbulence** (cited in Dim 8 counter): NWP "cannot reliably predict seeing conditions" where boundary layer turbulence dominates; high-resolution NWP "do not follow the short-term evolution of the measurements."
- **Phil Hart [143]:** 7Timer APanel seeing "appears to almost always forecast a worst case."
- **Meteoblue's own docs [131]:** Seeing index labeled "experimental"; "values may not reflect precisely reality."

The Cloudy Nights community consensus is to treat seeing forecasts as directional rather than predictive, and to rely on real-time on-site monitoring (DIMM, all-sky cameras) for actual seeing measurement.

## DIY parity examples
- **AstroWeather Home Assistant integration [146]** built on MET Norway + Open-Meteo rather than aggregators — demonstrates aggregator features can be replicated.
- **jaglab.org Astro Forecast [147]** uses Open-Meteo directly; derives seeing index from T-dew spread, wind, RH — same physics aggregators use, transparently visible.
- **SkippySky [148]** is a low-maintenance GFS-based site that essentially reproduces 7Timer functionality with different visualization.

## Gaps and limitations

- **Astrospheric ECMWF/HRRR ingest:** the 2022 ATT article lists ECMWF and HRRR as Astrospheric sources; the official FAQ lists only RDPS, GFS, NAM, RAP, NBM. Whether ECMWF/HRRR enter only via NBM, or were previously direct sources that were removed, is unclear.
- **Astrospheric ensemble model list:** the current ensemble page lists RDPS + ICON + GFS + NBM. Earlier sources mention NAM. Whether NAM was replaced by ICON or both appear is unverified.
- **Clear Outside current model stack:** Meteosource doesn't publicly enumerate which NWP feeds it uses for which Clear Outside outputs.
- **Clear Sky Chart post-Danko maintenance:** site appears active through 2024 but the long-term data pipeline status (CMC GEM ingest, Rahill processing) was not confirmed.
- **Clear Sky Chart ECMWF coverage:** which specific charts have ECMWF overlay (added 2020) is not documented on the official site.
- **Meteoblue seeing index validation:** 2018 announcement promised 2019 validation; results were not found in published form.
- **Astrospheric Pro API B2B / higher-volume tier:** not publicly documented; would need direct contact for an indie astro app querying many locations.
- **No SE-US-specific accuracy comparison** of these aggregators was found in the literature; community accuracy reports are anecdotal.
- **Forum sources** ([139], [140], [141], [142]) returned 403 in this research; the cited claims rest on Google search snippet extractions and should be re-verified during Phase 4 audit.
