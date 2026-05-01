# Weather APIs and Multi-Layer Cloud Forecasting for Astrophotography

Citation-backed analysis of which weather APIs and observational data sources expose multi-layer cloud cover (low / mid / high) suitable for astrophotography go/no-go decisions, at what cost, with what license, and with what accuracy in the Southeast US (Carolinas / Piedmont / Blue Ridge).

Dimensions detailed in:
- [Provider matrix](references/provider-matrix.md)
- [Underlying NWP models](references/underlying-models.md)
- [Pricing and licensing](references/pricing-and-licensing.md)
- [Southeast US accuracy](references/southeast-us-accuracy.md)
- [Temporal resolution](references/temporal-resolution.md)
- [Ensemble / uncertainty](references/ensemble-uncertainty.md)
- [Caching / rate-limit strategy](references/caching-rate-limit-strategy.md)
- [Astrophoto aggregators](references/astrophoto-aggregators.md)
- [Satellite imagery and nowcasting](references/satellite-nowcasting.md)

All sources: [`citations.md`](citations.md).

---

## TL;DR

For an indie astrophotography session-planning app in the Southeast US:

1. **No single API is a complete solution.** The architecturally robust pattern is layered: satellite-observed cloud for now / next 0–3 hours, NWP forecast for 3+ hours, ensemble probabilistic outlook for 1–7 days.
2. **Multi-layer cloud cover (low / mid / high) is exposed by 4 providers** — Open-Meteo, MET Norway, Meteomatics, and ECMWF Open Data — but **the layer definitions are not comparable across providers**. ECMWF uses sigma coordinates, WMO uses latitude-dependent altitude, NOAA SPC uses absolute pressure, Open-Meteo derives from RH at pressure levels [1], [3], [8], [11], [15].
3. **NOAA NWS, OpenWeatherMap, Tomorrow.io, and Visual Crossing expose only an aggregate `cloudCover` percentage** — not suitable for transparency-sensitive astrophotography decisions [5], [10], [13], [14].
4. **HRRR is the highest-resolution operational NWP for Southeast US** (3 km, hourly, CONUS-only), but has documented summer convective biases — including a **1–2 hour delay in afternoon convective initiation in the SE specifically** [90] and overforecasting of convective storm objects most pronounced in the Southeastern US [79].
5. **Persistence beats short-horizon NWP for cloud cover up to ~6 h** — but with a critical qualifier from Ye & Chen 2013 (MNRAS, only peer-reviewed study targeting astronomy): "this is not meaningful as the GFS model data are not available after approximately 4–5 h" [82]. The "persistence wins at <6h" finding is partly an **operational availability artifact** — by the time GFS data reaches the user (~4–5h post-initialization), persistence has been the only signal during the gap. Architecturally: observed-conditions sources (GOES-19 ABI ACM, all-sky cameras) cover the latency gap; NWP takes over once a fresh cycle arrives.
6. **GOES-19 became operational GOES-East on April 7, 2025**, replacing GOES-16 [151]. The current SE US satellite bucket is `noaa-goes19` (free, no AWS account required, 5-min CONUS cadence) [149], [152].
7. **Free-tier API economics are fragile.** AccuWeather killed perpetual free in September 2025; Dark Sky shut down in 2023; OpenWeatherMap 2.5 deprecated June 2024 [75], [76]. The robust pattern is multi-vendor abstraction with NWS + Open-Meteo + MET Norway + ECMWF Open Data as the redundant base [67], [49], [60], [63].
8. **"70% chance of clear" requires per-member ensemble + post-processing — and is unavailable as a packaged product** from any major free API. The build path: query Open-Meteo Ensemble API or ECMWF Open Data ENS, count members with TCC ≤ threshold client-side. Cloud cover ensembles are demonstrably worse-calibrated than temperature/precipitation ensembles [104], [106], [107].

## What the question's framing missed

This research's plan-mode framing challenge surfaced three assumptions in the original topic file that the deliverable should explicitly address:

1. **"Weather API" was treated as the primary go/no-go input.** For lead times < 3 hours, satellite-observed cloud (GOES-19 ABI ACM at 5-min cadence) outperforms NWP forecast. The deliverable's recommended architecture distinguishes forecast-driven decisions (tonight vs. tomorrow) from nowcast-driven decisions (the next 90 minutes). See [`satellite-nowcasting.md`](references/satellite-nowcasting.md).
2. **"Build atop raw model APIs" was the implicit goal.** Astrophoto-specific aggregators (Astrospheric, Clear Outside, Meteoblue Astronomy, Clear Sky Chart) already do multi-layer aggregation. The build-vs-buy axis is evaluated explicitly in [`astrophoto-aggregators.md`](references/astrophoto-aggregators.md) — Astrospheric Pro at $2.99/mo offers the only usable astronomy-specific API but is capped at ~20 forecasts/day, which is structurally inadequate for a session-planning app querying many user locations.
3. **Deterministic forecasts were the default frame.** The deeper question is calibration — when an ensemble says "70% chance of clear," does that pan out 70% of the time? Cloud cover ensembles are systematically underdispersive (Hemri et al. 2016 [106]); standard EMOS post-processing fails for cloud where it succeeds for temperature (Dai & Hemri 2021 [107]). Cloud cover is bimodal at 0/8 oktas, so intermediate probabilities are physically sparse — not a calibration artifact that can be fully fixed.

The topic correctly scopes to cloud cover. Transparency, seeing, and dew are explicitly out of scope and slated for separate research topics in the same batch.

## Provider matrix at a glance

Detailed in [`provider-matrix.md`](references/provider-matrix.md). The headline:

| Provider | Layered cloud? | Free | Commercial use on free? | Multi-layer definition |
|---|---|---|---|---|
| Open-Meteo | Yes (low/mid/high at 0–3 / 3–8 / 8+ km) | Yes (10K/day) | **No (non-commercial only)** | Altitude-band, fixed [1] |
| MET Norway | Yes (low/medium/high at <2000 / 2000–5000 / >5000 m) | Yes | Yes (with attribution) | Altitude-band, fixed [3] |
| Meteomatics | Yes (low/medium/high at 0–1800 / 1800–6300 / >6300 m AGL) | Free 500/day | **No (private only)** | Altitude-band AGL [11] |
| ECMWF Open Data | Yes (LCC/MCC/HCC) | Yes (CC-BY-4.0) | Yes | **Sigma-based**, terrain-relative [7], [8] |
| NOAA NWS | **Aggregate `skyCover` only** | Yes | Yes (public domain) | N/A [5] |
| OpenWeatherMap | **Aggregate `clouds` only** | Yes (1M/mo) | Yes (with attribution) | N/A [10] |
| Tomorrow.io | **Aggregate + cloudBase + cloudCeiling** | Free 500/day | Unconfirmed | N/A — but ceiling useful [13] |
| Visual Crossing | **Aggregate only** | Yes (1K/day) | Yes (with attribution) | N/A [14] |

**The layer-definition incompatibility is the deepest finding here.** A cumulus cloud with base at 700 hPa over the Carolinas is reported as `MCC` by ECMWF (sigma 0.69), `medium` by Meteomatics and MET Norway (3 km AGL), boundary-of-`low/mid` by Open-Meteo, and `low` by NOAA SPC (below 642 hPa pressure cutoff). An app that surfaces raw `low/mid/high` from multiple providers without harmonizing definitions will display incoherent information [1], [3], [8], [11], [15].

## NWP model coverage

Detailed in [`underlying-models.md`](references/underlying-models.md).

For Southeast US astrophotography:
- **0–18h forecast:** HRRR (3 km, CONUS-only, hourly cycles, 18-hour horizon; 48 h on 00/06/12/18 Z extended cycles) [21], [22]. HRRR has documented cloud-spin-up issues at FH0–2 [78] and 1–2h delay of afternoon convective initiation in SE US [90]; FH3–18 is the sweet spot.
- **18–48h:** HRRR Extended at 00/06/12/18 Z, or NAM 12 km parent + 3 km nests [24].
- **2–10 day:** ECMWF IFS HRES at 9 km native, served via the ECMWF Open Data catalogue (full real-time catalogue open under CC-BY-4.0 since October 1, 2025 at a **25 km publicly accessible subset**; 9 km HRES extension planned for later in 2026 with 2-hour latency [63]); GFS at 0.25° as backup.
- **AI models do not output cloud cover.** GraphCast (227 variables, no cloud), Pangu (69 variables, no cloud), FourCastNet (73 channels, TCWV proxy only) are not options for cloud forecasting today [42], [43], [44]. ECMWF AIFS Single v1 does output tcc/lcc/mcc/hcc but with documented flat-distribution bias (under-predicts both clear and overcast extremes) [32], [171].

Documented model biases relevant to cloud forecasting:
- HRRR systematic cloud underprediction → excessive surface SW; summer fix only 35% effective vs 80–84% in fall/winter [77].
- HRRR overforecasts convective objects most in the southeastern US [79]. Note: this and the underforecast-cloud finding are physically consistent — they refer to different measurement frameworks (radiation-based stratiform cloud verification vs radar-based convective-object verification). HRRR's parameterizations are eager to fire deep convection but poor at maintaining diffuse cloud cover; both error modes affect SE US astrophotography forecasts in different regimes. See [southeast-us-accuracy.md](references/southeast-us-accuracy.md) for reconciliation.
- ECMWF IFS Cycle 47r3 (Oct 2021) introduced a +3-4% global cloud cover bias (up to +15% locally) — explicit ECMWF-acknowledged regression [29], [30].
- GFS Arakawa-Schubert convective scheme is "very susceptible to grid scale convective blow-ups in moist/unstable airmasses"; warm-season precipitation overforecast bias ~1.6 [174].
- WeatherReal benchmark: total cloud cover has the **highest RMSE of any surface variable** evaluated across all NWP/AI models [173].

## Pricing and licensing — practical math

Detailed in [`pricing-and-licensing.md`](references/pricing-and-licensing.md).

For one location polled hourly (24 calls/day):
- Open-Meteo non-commercial: ~417 locations on free tier (10,000 / 24) — but commercial use blocked [49], [50].
- WeatherAPI.com Free: ~138 locations (100K/month, commercial OK) [64].
- OpenWeatherMap general API Free: ~1,388 locations (1M/month, commercial OK with attribution) [53] — but only aggregate cloud.
- MET Norway, NWS, ECMWF Open Data: unbounded by quota (bounded by ToS / infrastructure stability).
- Astrospheric Pro: ~20 forecasts/day at $2.99/month [126], [127].

The "free tier turns hostile" pattern documented in [75], [76]: weather underground → Yahoo → Dark Sky (2023) → AccuWeather (2025) all eliminated free APIs. Multi-vendor abstraction is structural, not optional.

For the Southeast US user, the recommended primary stack:
1. **Forecast feed:** Open-Meteo if non-commercial (highest quota, multi-layer cloud); WeatherAPI.com if commercial (commercial-OK free tier, but aggregate cloud only — pair with a multi-layer source).
2. **Cross-check:** MET Norway (layered cloud + free + dual NLOD/CC-BY licensed; strict ToS on User-Agent and caching).
3. **Medium-range:** ECMWF Open Data via `ecmwf-opendata` Python client (LCC/MCC/HCC at 0.25°, free CC-BY-4.0).
4. **Real-time:** GOES-19 ABI ACM via `noaa-goes19` AWS S3 (free, no auth, 5-min CONUS).

## Southeast US accuracy

Detailed in [`southeast-us-accuracy.md`](references/southeast-us-accuracy.md).

**No SE-US-specific peer-reviewed cloud verification study was found.** The closest direct evaluation is Burlingame et al. 2019 in northern Alabama (HRRRv2) [80], full text not fetched in this research. Most quantitative accuracy assessment for SE US comes from CONUS-wide studies (SURFRAD, USCRN, NY State Mesonet) [77], [87] plus Skinner et al. 2021's specific finding that **HRRR overforecasts convective storm objects most in the southeastern US** [79].

Three converging lines of evidence:
1. **HRRR cloud underprediction** is well-supported across multiple peer-reviewed papers [77], [78], [87]. Summer is the hardest regime to fix.
2. **HRRR delays afternoon convective initiation by 1–2 hours in the SE US** specifically (NSSL EWP 2024 operational note) [90]. Direct relevance: SE US apps will see HRRR clear the sky too aggressively after afternoon storms.
3. **For lead times < 6 hours, persistence beats GFS** (Ye & Chen 2013, MNRAS, the only peer-reviewed study targeting astronomy) [82]. Architecturally: use observation-based signals for the next 6 hours, NWP for 6+ hours.

Confidence in this dimension is **moderate, not strong**. Several key papers' full text was not directly fetched (AMS journals returned 403 throughout); James & Turner 2025 was ahead-of-print [77]. Quantitative numbers from search snippets / abstracts should be re-verified during Phase 4 audit.

## Temporal resolution — sub-hourly is mostly an illusion

Detailed in [`temporal-resolution.md`](references/temporal-resolution.md).

**No major free API provides genuinely skillful sub-hourly cloud cover forecast for the SE US.**
- HRRR's sub-hourly product (`wrfsubhf`) **does not include cloud cover variables** (LCDC/MCDC/HCDC/TCDC absent) [19].
- Open-Meteo's `minutely_15` cloud cover is **interpolated from hourly** via wgrib2-style linear interpolation [91], [98].
- MET Norway Nowcast covers Norway/Sweden/Finland/Denmark only — irrelevant for SE US [93].

Solar industry practice is the strongest empirical signal: "Neither NWP or WRF methods have been adopted operationally for intra-hour horizons by solar power plant managers" [97]. The financial incentive is strong; the rejection is technical, not commercial.

For lead times < 1 hour, **persistence beats NWP** [95], [96]. For 0–3 hours over CONUS, **observation-driven satellite extrapolation (GOES-19 ACM at 5-min cadence)** beats NWP interpolation. The right architectural choice is observation-based, not NWP-based, for sub-hourly cloud.

Astrophotography session planning operates at hourly cadence in practice (Astrospheric, Clear Outside, Clear Sky Chart all use hourly) — so the question of sub-hourly cloud forecast utility is largely moot for go/no-go decisions [124], [129], [134].

## Ensemble probability

Detailed in [`ensemble-uncertainty.md`](references/ensemble-uncertainty.md).

To surface "70% chance of clear" properly, an app needs:
1. Per-member ensemble cloud cover (available via Open-Meteo Ensemble API for ICON-EPS/GFS Ensemble/ECMWF IFS [103]; via `ecmwf-opendata` for ECMWF ENS at 0.25° [102]).
2. Threshold logic to count members with TCC ≤ X (Open-Meteo's existing `precipitation_probability` formula generalizes [105]; cloud cover probability not implemented per GitHub #349 [104]).
3. Calibration against observed clear-sky frequencies — which **does not work well for cloud cover** because:
   - Raw ECMWF cloud ensemble is "clearly underdispersive" [106].
   - Cloud cover is bimodal at 0/8 oktas; intermediate probabilities are physically sparse [106].
   - Standard EMOS+ECC post-processing destroys spatial coherence; conditional GAN required [107].
   - ECMWF cloud skill drops below persistence at day 3 — earlier than for any other major variable [86].

The honest UX for cloud probability: **per-member fan / spaghetti plot** rather than calibrated probability number. If displaying as probability, label it as raw ensemble fraction (granularity ~3.2% for GEFSv12, ~2% for ECMWF ENS) and document explicitly that the underlying ensemble is underdispersive.

## Astrophoto aggregators — useful, but with caveats

Detailed in [`astrophoto-aggregators.md`](references/astrophoto-aggregators.md).

| Aggregator | Best use case | Limitation |
|---|---|---|
| Astrospheric | North American astrophotographers wanting curated cloud/seeing/transparency | API quota 100 credits/day = ~20 forecasts (inadequate for app scale); CONUS-Canada coverage only [124], [126] |
| Clear Outside | Beginner-friendly UI/embed | No API; biased toward cloudy [129] |
| Meteoblue Astronomy | Global coverage with explicit seeing index | Paid API (€1,200/yr minimum); seeing index "experimental" by Meteoblue's own admission [131] |
| Clear Sky Chart | Regional cross-check | No API; fixed sites only; 48h cap; CMC GEM-bound [134], [136] |
| 7Timer! | Free open API + global | GFS-only; non-commercial only [138] |

**Aggregators wrap 2–3 primary feeds.** Checking Astrospheric and Clear Outside against each other is illusory cross-validation — they share underlying NWP feeds. The robust pattern is independent feeds: HRRR (Open-Meteo) + ECMWF (Open Data) + GOES-19 (observed).

The **build-vs-buy** decision favors raw APIs for any app needing geographic flexibility beyond North America, per-location query at scale, or transparent model provenance. DIY parity examples (jaglab.org, Home Assistant AstroWeather) demonstrate that the seeing index physics (T-dew spread, wind, RH) are reproducible without aggregator pricing [146], [147].

**Seeing forecasts have low predictive skill.** Ye & Chen 2013 (MNRAS, peer-reviewed astronomy validation): GFS-based seeing forecasts achieve cloud detection probability 30–90% (lower bound is worse than coin flip); seeing RMSE 0.2–0.4″ [82]. SPIE 2023 paper: NWP "cannot reliably predict seeing conditions" where boundary-layer turbulence dominates. Phil Hart (independent practitioner): 7Timer seeing "appears to almost always forecast a worst case" [143]. Treat seeing as directional, not predictive.

## Caching and rate-limit strategy

Detailed in [`caching-rate-limit-strategy.md`](references/caching-rate-limit-strategy.md).

Recommended architecture:
- **NWS:** `If-Modified-Since` 304 conditional requests; cache `/points/{lat},{lon}` indefinitely; share forecast cache via NWS gridpoint URL.
- **Open-Meteo:** `openmeteo-requests` with 1-hour `expire_after`; snap lat/lon to ~2 decimals client-side; queue at ≤1 req/s to stay under 5K/hr; handle Open-Meteo's IP-based limit [73] (not compatible with Cloudflare Workers shared IPs without paid tier).
- **ECMWF Open Data:** `ecmwf-opendata` Python client; fetch only LCC/MCC/HCC/TCC GRIB2 fields needed; cache locally for 6 h between runs.
- **GOES-19 ABI ACM:** AWS S3 `--no-sign-request`; subscribe to SNS topic; cache locally for 5 min matching CONUS cadence.

**Documented gotchas:**
- NWS rate-limit blocks return **HTTP 403, not 429** — standard 429-retry libraries fail silently [71].
- NWS blocked Linode and DigitalOcean IPv6 ranges entirely on August 31, 2024 [70].
- Apple WeatherKit returned 2+ hour stale data with no fix ETA [72].
- NWS/Akamai CDN served forecasts up to 981 hours (41 days) stale due to corrupted-cache propagation [69].

**Self-hosting Open-Meteo is not cheaper than the paid API** at indie scale — bandwidth alone would cost $4,800–9,000/month vs $29/month Standard subscription [74]. The build-buy line is far above indie-app scale.

## Satellite imagery and nowcasting

Detailed in [`satellite-nowcasting.md`](references/satellite-nowcasting.md).

**Key 2025 update:** GOES-19 became operational GOES-East on April 7, 2025, replacing GOES-16. Real-time SE US data should be sourced from `noaa-goes19` AWS S3 bucket [149], [151]. The user's planning topic file mentions GOES-16 — that is now historical only.

Cadence: Full Disk every 10 min, **CONUS every 5 min**, Mesoscale every 60 sec [152]. ABI Level 2 cloud products at 2 km resolution: ACM (Clear Sky Mask, 4 classes), ACTP (Cloud Top Phase), ACHA (Cloud Top Height) [153]–[155].

Documented limitations:
- **GOES-16 ABI ACM daytime clear-sky accuracy: only 66.6%** — 1 in 3 clear pixels misclassified as cloudy in daytime [161]. ACM is more reliable as a "definitely cloudy" filter than a "definitely clear" filter.
- The 1.378 µm cirrus band is **daytime-only** (SZA < 80°) [163], [164]. Thin cirrus invisible to nighttime satellite is exactly the scenario most damaging to astrophotography transparency.
- Bi-spectral IR overstates low cloud at night over coastal regions where cool ocean upwelling lies beneath warm moist atmosphere — common over Carolina coastal sites [165].
- ASOS reports clouds only below 12,600 ft AGL — overcast at 15,000 ft reported as "clear" [167]. ASOS cannot serve as ground-truth for satellite cloud mask validation in cirrus-heavy regimes.

The architectural pattern: **satellite for now and the next 0–3 hours; NWP for 3+ hours.** Optical-flow satellite extrapolation has a skillful window of ~3 hours [95]; beyond that, it cannot create or dissipate clouds, only advect existing pixels.

## Recommended architecture (one-page)

```
┌────────────────────────────────────────────────────────────────────────┐
│ 0–30 min:  All-sky camera (user device) + GOES-19 mesoscale 60-sec    │
│ 0–3 h:     GOES-19 ABI ACM (5-min CONUS) + optical-flow extrapolation │
│ 3–18 h:    HRRR (Open-Meteo or NOMADS) — caveat: FH0–2 spin-up,        │
│             1-2h SE US convective initiation delay                     │
│ 18–48 h:   HRRR Extended (00/06/12/18 Z) — caveat: SE convective bias  │
│ 2–5 day:   ECMWF IFS HRES (Open Data via ecmwf-opendata)               │
│ 5–10 day:  ECMWF ENS or GFS GEFS — per-member fan plot                 │
│                                                                        │
│ Cross-check:  MET Norway layered cloud (free, no key; ToS strict UA)   │
│ Probability:  Compute client-side from per-member ensemble; label as   │
│                "raw ensemble fraction" — calibrated probability        │
│                requires post-processing not available out-of-box       │
└────────────────────────────────────────────────────────────────────────┘
```

## Reflection

Reviewing this document before writing the README:

1. **Cross-source synthesis areas.** The most synthesized claims are: (a) HRRR underforecasts cloud cover in SE US summer [77], [78], [79], [87], [90]; (b) layer definitions are not comparable across providers [1], [3], [8], [11], [15]; (c) ensemble cloud cover is harder to calibrate than other variables [86], [106], [107]. These are well-supported by multiple peer-reviewed sources but the claims about *direct* SE-US cloud accuracy rely on either (i) the NSSL operational note [90], or (ii) inference from convective-object verification [79] rather than direct cloud-fraction verification — flagged for Phase 4 audit attention.

2. **Confidence asymmetries.** Higher confidence: provider matrix (direct API doc fetches), satellite specs (NOAA/AWS direct sources), license terms (ToS pages directly fetched). Lower confidence: SE-US-specific accuracy quantitative numbers (peer-reviewed papers behind 403 walls in this research session); ensemble post-processing skill scores (not extracted from peer-reviewed papers in detail).

3. **Contradiction surfaced.** Astrospheric self-acknowledges its forecasts "will be wrong at times" [128]; Cloudy Nights documents "7 forecasts all agree but the sky doesn't" [142]. The deliverable should not over-promise about probabilistic forecast skill — the calibration limitations are real and known to ECMWF [106].

4. **What the user originally asked vs what they actually need.** The user's topic file framed this as "which APIs expose multi-layer cloud cover." The deeper finding is: **layer definitions are not interoperable**, and a transparency-sensitive astrophotography app should consume one provider's layered cloud and harmonize before display. The deliverable surfaces this in the headline finding rather than burying it in caveats.

5. **What's not addressed.** Transparency forecasting (aerosol optical depth, smoke), seeing forecasting (boundary-layer turbulence), and dew point — explicitly out of scope for this topic and slated for separate batches.

6. **Gaps that warrant Phase 4 attention.** AMS journal full-text inaccessibility means specific bias values (Burlingame 2019, Griffin 2017, James & Turner 2025) need direct re-fetch. Forum source 403s mean Cloudy Nights / Reddit anecdotes rest on Google snippet extraction. The cited-research methodology's 20–30% inaccessibility expectation is met but the specific high-priority sources should be flagged for the user during audit if they remain inaccessible.

## Limitations and gaps

- **No SE-US-specific peer-reviewed cloud verification study was found.** Burlingame 2019 (HRRRv2 northern Alabama) is the closest; full text not fetched.
- **NWS NDFD WFO sky cover verification portal** (sats.nws.noaa.gov/~verification/ndfd/) maintains GSP/RAH/ILM Heidke Skill Scores but was inaccessible.
- **AMS journal articles** returned 403 throughout — quantitative bias values from search snippets / abstracts need Phase 4 re-verification.
- **GOES-19 specific cloud product validation** has not been published (Tzallas et al. 2020 [161] validated GOES-16 ACM; transferability assumed).
- **HRRR-Smoke S3 sub-path and operational status in 2026** (vs RRFS integration) not directly verified.
- **Astrospheric Pro higher-volume / B2B API tier** not publicly documented — would need direct contact for an indie app.
- **ECMWF ENS open-data TCC date of addition and per-member coverage** not confirmed exactly.
- **Self-hosted Open-Meteo minimum viable variable subset** (HRRR + GFS only) and its true storage/bandwidth footprint not computed precisely.
- **Open-Meteo bug #416** (sub-terrain pressure level inflation of `cloudcover_low` at elevated SE US sites) resolution status not re-checked at deliverable time.
- **No empirical study tests whether sub-hourly vs hourly cloud forecasts change astrophotographer go/no-go decisions** — the conclusion that hourly is sufficient is supported by industry practice but not validated by controlled comparison.
- **Forum sources** (Cloudy Nights threads) returned 403; cited claims rest on Google snippet extraction.
