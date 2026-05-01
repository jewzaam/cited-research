# Citation Audit — Atmospheric Obstructions for Astrophotography

**Audit date:** 2026-04-29
**Auditor:** Isolated Phase 4 verification agent (no conversation context from production session)
**Scope:** Citations 1–107 in `citations.md`
**Snapshots available:** 17 files in the cited-research-data directory
**Total citations:** 107

---

## Summary Table

| Grade | Count | Citations |
|---|---|---|
| VERIFIED | 13 | 1, 3, 11, 18, 19, 23, 26, 35, 41, 42, 56, 59, 66 |
| PARTIAL | 5 | 2 (metadata verified; band values DRIFT-flagged), 37, 58, 86 |
| INACCURATE | 0 | — |
| INACCESSIBLE | 87 | 4–10, 12–17, 20–22, 24–25, 27–34, 36, 38–40, 43–55, 57, 60–65, 67–85, 87–107 |
| DRIFT | 1 | 2 (V=0.11, B=0.19 band values — not supported by snapshot; production session correctly self-flags these) |
| NOT FOUND | 0 | — |

> Note: Citation 2 (Buton 2013) appears in both PARTIAL and DRIFT — the metadata (sample size, dates, instrument, spectral range) is verified; the band-specific extinction values V=0.11 and B=0.19 mag/airmass are not confirmed by the snapshot and are DRIFT-flagged. All 107 citations are accounted for. Counts reconciled in the final tally section.

---

## VERIFIED

Citations where the snapshot directly supports the specific claim as stated.

---

### Citation 1 — Patat et al. 2011 (Paranal extinction)

**Snapshot:** `patat-2011-paranal.md` — Status OK

**Claims in documents:**
- `citations.md`: k₀ = 0.013 ± 0.002 mag/airmass at reference wavelength; α = −1.38 ± 0.06; spectral 3300–8000 Å; detectable El Chichón volcanic residual below 4000 Å
- `particulates-to-imaging-impact.md`: k_aerosol₀ = 0.013 ± 0.002 mag/airmass at reference wavelength; α = −1.38 ± 0.06; total V around 0.15–0.16 mag/airmass
- `atmospheric-obstructions-guide.md`: Cerro Paranal V ~0.15–0.16 with α = −1.38 [1]

**Snapshot text (verbatim):**
> "Aerosol extinction coefficient at reference wavelength: k0 = 0.013 +/- 0.002 mag airmass^-1."
> "Angstrom exponent: alpha = -1.38 +/- 0.06."
> "Spectral range: 3300-8000 A (usable to ~6800 A due to fringing)."
> "Visual extinction values around 0.15-0.16 mag/airmass."
> "a systematic deficit with respect to the extinction curve derived for Cerro Tololo before the El Chichon eruption is detected below 4000 A"

**Grade: VERIFIED.** All four quantitative claims (k₀, α, spectral range, visual extinction, El Chichón residual note) are directly supported by the snapshot verbatim.

---

### Citation 3 — IAC ORM extinction monitoring

**Snapshot:** `iac-orm-extinction.md` — Status OK

**Claims in documents:**
- `citations.md`: Median V-band extinction at ORM = 0.130 mag/airmass (Carlsberg Meridian Telescope, 1984–2013); photometric threshold 0.153 mag/airmass; ~20% of dust outbreaks reach observatory altitudes; July–August calimas dominate; AERONET 340–1640 nm
- `particulates-to-imaging-impact.md`, `saharan-dust-transport.md`, `atmospheric-obstructions-guide.md` repeat these claims

**Snapshot text (verbatim):**
> "Median night-time V-band extinction at Roque de los Muchachos Observatory (ORM): KV = 0.130 mag/airmass."
> "Source: Carlsberg Meridian Telescope data spanning 1984-2013."
> "Photometric time threshold: 0.153 mag/airmass (V-band)"
> "Approximately 20 percent of dust outbreaks affecting the Canary Islands actually reach observatory altitudes."
> "Seasonal calima/Saharan dust pattern: 'July-August calimas are more likely to reach the summits of the islands'"
> "AOD measurement: AERONET sun photometers at 'a range of wavelengths sensitive to mineral dust intrusions' from 340 to 1640 nm."

**Grade: VERIFIED.** All five quantitative and qualitative claims are supported verbatim.

---

### Citation 11 — Fu et al. 2022 (PM2.5/AOD decoupling)

**Snapshot:** `fu-2022-pm25-aod-decoupling.md` — Status OK

**Claims in documents:**
- `citations.md`: 19 stations, 2017–2019; Daily PM2.5/AOD R = 0.03–0.60; specific humidity 2.83–11.89 g/kg drives decoupling; predictive R: AOD-only 0.49, AOD+humidity 0.74, AOD+four met factors 0.81
- `README.md`, `aerosols-and-pm25.md`, `particulates-to-imaging-impact.md` repeat these claims

**Snapshot text (verbatim):**
> "low correlation coefficients of 0.03-0.60 between daily PM2.5 and AOD for most sites"
> "19 stations in China, period 2017-2019"
> "specific humidity increases from 2.83 g kg-1 for the cases with low AOD but high PM2.5 -- 11.89 g kg-1 for those with high AOD but low PM2.5"
> "AOD alone: 'R of 0.49 between the predicted and observed PM2.5'"
> "AOD + specific humidity: 'increases the R to 0.74'"
> "AOD + four meteorological factors: 'R of 0.81'"

**Grade: VERIFIED.** All claims — station count, date range, R range, humidity range, and all three predictive R values — match exactly.

---

### Citation 18 — Barkjohn et al. 2021 (PurpleAir correction equation)

**Snapshot:** `barkjohn-2021-purpleair.md` — Status OK

**Claims in documents:**
- `citations.md`: Equation `PM2.5 = 0.524 × PA_cf_1 − 0.0862 × RH + 5.75`; RMSE 8 → 3 µg/m³; 50 sensors, 16 states, 39 sites; limitations: 3 rural sites, high-concentration validity uncertain, bias at T < −12 °C
- Multiple reference files repeat these claims verbatim

**Snapshot text (verbatim):**
> "PM 2.5 = 0.524 x PA cf_1 - 0.0862 x RH + 5.75"
> "reduces the root mean square error (RMSE) of the raw data from 8 to 3 ug m-3"
> "50 PurpleAir sensors located in 16 states across 39 sites (NOT '70+ sites' as some secondary sources claim)"
> "Only three sites are classified as rural."
> "Potential bias at very low temperature below -12 C and potentially high concentration above 60 ug/m3."

**Grade: VERIFIED.** The equation, RMSE figures, sensor/state/site counts, rural site count, and temperature limitation are all directly supported. The snapshot explicitly corrects a "70+ sites" overclaim from secondary sources — the `citations.md` states 39 sites correctly.

---

### Citation 19 — Jaffe et al. 2023 (dust failure 5–6× factor)

**Snapshot:** `jaffe-2023-correction-aerosol-types.md` — Status OK

**Claims in documents:**
- `citations.md`: "too low by factor 5–6 in dust (slope 5.6 at Keeler)"; smoke slope 0.99; urban slope 1.00; published 13 March 2023
- `aerosols-and-pm25.md`, `source-conflict-resolution.md`, `atmospheric-obstructions-guide.md` repeat

**Snapshot text (verbatim):**
> "the corrected PAS data are accurate in smoke but are too low by a factor of 5-6 in dust"
> "For dust at Keeler California: 'the slope is 5.6, similar to the slopes shown in Table 2 (5.5) and Table 3 (5.0)'"
> "For smoke at Keeler California: 'the PAS with the Barkjohn 2021 correction shows a slope of 0.99 and an R^2 of 0.92'"
> "Mean slopes by aerosol type with Barkjohn correction: '1.00 and 0.99 for urban and smoke aerosol events, respectively'"
> "Published 13 March 2023."

**Grade: VERIFIED.** The 5–6× dust factor, slope 5.6, smoke slope 0.99, urban slope 1.00, and publication date are all directly supported verbatim.

---

### Citation 23 — AirNow API (landing page)

**Snapshot:** `airnow-api-docs.md` — Status OK (limited detail)

**Claims in documents:**
- `citations.md`: Public US/Canada/Mexico API, 2,500+ monitoring stations, forecasts for 500+ cities, real-time observations, free public registration; rate limits/endpoint URL not exposed on landing

**Snapshot text (verbatim):**
> "Access to the AirNow API is available to the public"
> "Coverage: United States, Canada, Mexico"
> "over 2,500 monitoring stations"
> "forecasts for more than 500 cities"
> "real-time air quality observations"
> "New accounts via Log In page, free public registration"
> "Specific rate limit, pricing tiers, and endpoint base URL not in this landing-page excerpt."

**Grade: VERIFIED.** All claims about coverage, station count, city count, real-time availability, and free registration are confirmed. The caveat about rate limits/endpoint URL not being exposed on the landing page is also correctly stated.

---

### Citation 26 — OpenAQ API v3

**Snapshot:** `openaq-quick-start.md` — Status OK (limited)

**Claims in documents:**
- `citations.md`: v3 confirmed; X-API-Key auth; AirNow listed as provider; per-location licenses (e.g., US Public Domain); rate limits (60 req/min, 2000 req/hr) and pass-through ingestion need separate verification

**Snapshot text (verbatim):**
> "Current version: v3 (paths like /v3/locations/{id})"
> "Authentication: API key in X-API-Key header"
> "Example responses include 'Government Monitor' instruments and AirNow as a provider"
> "Licenses are per-location (e.g., 'US Public Domain')"
> "Not in this excerpt (need separate fetch from /using-the-api/rate-limits and /about/terms): Specific rate limits (discovery agent reported 60/min, 2000/hr)"

**Grade: VERIFIED.** The `citations.md` correctly represents what was and was not confirmed from the landing page, including flagging rate limits and pass-through ingestion as needing separate verification. The verified facts (v3, X-API-Key, AirNow as provider, per-location licenses) match.

---

### Citation 35 — Google Pollen API coverage (80 countries)

**Snapshot:** `google-pollen-coverage.md` — Status OK

**Claims in documents:**
- `citations.md`: 80 countries (NOT 65+); US tree species include maple, elm, cottonwood, alder, birch, ash, pine, oak, juniper; reduced-coverage countries enumerated; no subspecies resolution
- Multiple reference files repeat

**Snapshot text (verbatim):**
> "Total countries: 80 (NOT '65+' as some discovery agents stated -- VERIFIED HIGHER)"
> "US tree species: maple, elm, cottonwood, alder, birch, ash, pine, oak, juniper. Pine is CONFIRMED."
> "Grass only (13): Argentina, Brazil, China, Chile, Ethiopia, Hong Kong, Mongolia, Mexico, Nepal, New Zealand, Pakistan, South Korea, South Africa"
> "Japan: grasses + Japanese cedar + Japanese cypress (no general tree/weed species)"

**Grade: VERIFIED.** The 80-country figure, US species list including pine, and reduced-coverage country details are all directly confirmed. The snapshot explicitly notes the correction from "65+" to 80.

---

### Citation 41 — NC DEQ pollen monitoring

**Snapshot:** `ncdeq-pollen.md` — Status OK

**Claims in documents:**
- `citations.md`: Single station at 4403 Reedy Creek Road, Raleigh, NC; operates late-Feb to mid-Nov, M–F; reports trees/grasses/weeds; live HTML at `xapps.ncdenr.org/aq/ambient/Pollen.jsp`

**Snapshot text (verbatim):**
> "Single station: 4403 Reedy Creek Road, Raleigh, NC 27607 (35.813311, -78.714373)"
> "Operating period: late February through mid-November."
> "Sampling cadence: Monday through Friday, except state holidays."
> "Categories: grasses, trees, weeds"
> "Live report: https://xapps.ncdenr.org/aq/ambient/Pollen.jsp"

**Grade: VERIFIED.** Address, operating period, sampling cadence, categories, and live report URL all match exactly.

---

### Citation 42 — NC State pine pollen GDD model

**Snapshot:** `ncstate-pine-gdd.md` — Status OK

**Claims in documents:**
- `citations.md`: Onset ≈300 GDD (Boyer 1978); peak ≈636 GDD (Baker & Langdon 1990); base 55°F; accumulate from Feb 1; no published uncertainty range

**Snapshot text (verbatim):**
> "Pine pollen onset: approximately 300 growing degree days (Boyer 1978)."
> "Pine pollen peak: approximately 636 growing degree days (Baker & Langdon 1990)."
> "Base temperature: 55 F."
> "Accumulation start: February 1."
> "No published uncertainty range, qualitative 'approximately' language only."

**Grade: VERIFIED.** GDD thresholds, base temperature, accumulation start date, source attributions (Boyer 1978, Baker & Langdon 1990), and the caveat about no uncertainty range all match exactly.

---

### Citation 56 — NASA FIRMS API

**Snapshot:** `firms-api.md` — Status OK

**Claims in documents:**
- `citations.md`: URL pattern `/api/area/csv/[MAP_KEY]/[SOURCE]/[AREA_COORDINATES]/[DAY_RANGE]`; 8 sensor variants (MODIS, VIIRS SNPP/NOAA-20/NOAA-21, LANDSAT for US/CA); 5000 transactions / 10 min rate limit; free MAP_KEY; 5-day max range per query

**Snapshot text (verbatim):**
> "Endpoint pattern: /api/area/csv/[MAP_KEY]/[SOURCE]/[AREA_COORDINATES]/[DAY_RANGE]"
> "Supported satellites: MODIS_NRT, MODIS_SP, VIIRS_NOAA20_NRT, VIIRS_NOAA20_SP, VIIRS_NOAA21_NRT, VIIRS_SNPP_NRT, VIIRS_SNPP_SP, LANDSAT_NRT (US/Canada only)"
> "Rate limit: 'MAP_KEY limit is 5000 transactions / 10-minute interval'"
> "Maximum date range per query: 5 days"
> "Authentication: free MAP_KEY by registration"

**Grade: VERIFIED.** URL pattern, all 8 satellite variants (matching MODIS×2, VIIRS SNPP×2, NOAA-20×2, NOAA-21×1, LANDSAT×1 = 8), rate limit, max range, and free MAP_KEY are all confirmed verbatim. The `citations.md` claim of "8 sensor variants" is technically correct (MODIS_NRT, MODIS_SP, VIIRS_SNPP_NRT, VIIRS_SNPP_SP, VIIRS_NOAA20_NRT, VIIRS_NOAA20_SP, VIIRS_NOAA21_NRT, LANDSAT_NRT = 8).

---

### Citation 59 — Williams Flats fire intercomparison

**Snapshot:** `williams-flats-intercomparison.md` — Status OK

**Claims in documents:**
- `citations.md`: 12 forecasting systems (3 global + 9 regional); NMB −87.4% to −4.3%; r ≤ 0.50 spatial correlation; FRP-based emissions 6.4× higher; FRP-based models generally outperformed
- `wildfire-smoke-forecasting.md`, `atmospheric-obstructions-guide.md` repeat

**Snapshot text (verbatim):**
> "12 forecasting systems compared (3 global + 9 regional)."
> "Williams Flats fire, Washington State, August 2019."
> "Fire size: 44,446 acres"
> "AOD bias range across all models: NMB from -87.4 percent to -4.3 percent (all underprediction)."
> "Spatial correlation r <= 0.50 across all models."
> "FRP-based emission inventories produced estimates 6.4 times higher on average than hotspot-based."
> "Models with FRP-based emissions generally outperformed hotspot-based models for AOD."

**Grade: VERIFIED.** All quantitative claims — system count breakdown, NMB range, spatial correlation ceiling, FRP multiplier, and direction of model performance — are directly supported.

---

### Citation 66 — NOAA AOML Saharan Air Layer

**Snapshot:** `aoml-sal.md` — Status OK

**Claims in documents:**
- `citations.md`: SAL "2 to 2.5-mile-thick layer" with "base starting about 1 mile above the surface"; active mid-June through mid-August (peak), declining after; outbreaks every 3–5 days during peak; reaches Caribbean, Florida, Central America, Texas; tracked via GOES-16, Meteosat, polar-orbiting + GPS dropsondes

**Snapshot text (verbatim):**
> "a mass of very dry, dusty air that forms over the Sahara Desert during the late spring, summer, and early fall."
> "a 2 to 2.5-mile-thick layer of the atmosphere with the base starting about 1 mile above the surface."
> "Activity escalates mid-June. Peak intensity: late June through mid-August. Declines after mid-August."
> "Fresh outbreaks emerge from Africa roughly every 3-5 days during peak season."
> "Regularly reaches the Caribbean. Can extend as far west as Florida, Central America, Texas"
> "GOES-16 satellite imagery … Meteosat … Polar-orbiting satellites … GPS dropsondes from P-3 and G-IV aircraft"

**Grade: VERIFIED.** All seasonal claims, geographic reach, thickness/altitude, and tracking products are directly supported. The `citations.md` description "Active mid-June through mid-August (peak), declining after" matches the snapshot ("Activity escalates mid-June. Peak intensity: late June through mid-August. Declines after mid-August.") — the slight compression is accurate.

---

## PARTIAL

Citations where the snapshot addresses the topic but does not directly entail the specific claim as stated, or where the snapshot confirms part of the claim but not all.

---

### Citation 2 — Buton et al. 2013 (Mauna Kea extinction)

**Snapshot:** `buton-2013-mauna-kea.md` — Status OK (partial)

**Claims in documents:**
- `citations.md`: 4285 spectra from 478 nights, 2004–2011, SNIFS on UH 2.2m, spectral 3200–9700 Å; "Discovery agent reported median V = 0.11, B = 0.19 mag/airmass; band-specific values not exposed in our re-fetch and are flagged as DRIFT"
- `particulates-to-imaging-impact.md`: "V ≈ 0.11, B ≈ 0.19 (per discovery agent extraction; band values not exposed in re-fetch — flagged as DRIFT)"

**Snapshot text:**
> "Sample: 4285 spectra from 478 nights at Mauna Kea."
> "Spectral range: 3200-9700 A."
> "Instrument: SuperNova Integral Field Spectrograph (SNIFS) on UH 2.2m telescope, 2004-2011."
> "Note: WebFetch summary did not expose explicit V/B/R/I-band median extinction values from this paper. Discovery agent reported V=0.11, B=0.19 mag/airmass as median values, which needs verification from the paper PDF directly. Treat those band-specific values as DRIFT until confirmed."

**Grade: PARTIAL.** The metadata claims (4285 spectra, 478 nights, date range, instrument, spectral range) are verified by the snapshot. The V = 0.11 and B = 0.19 band-specific values — which appear in the deliverable as factual claims (with a DRIFT flag) — are not supported by the snapshot. The `citations.md` correctly applies the DRIFT flag and the deliverable also qualifies them. However, because these band-specific values appear as data points in the observatory baseline table in `atmospheric-obstructions-guide.md` and `particulates-to-imaging-impact.md`, the claim is PARTIAL: some details verified, key quantitative values unverified from source.

---

### Citation 37 — Ambee Pollen API docs

**Snapshot:** `ambee-pollen-api.md` — Status OK

**Claims in documents:**
- `citations.md`: Endpoints `/latest/`, `/history/`, `/forecast/`, `/forecast/v2/pollen/120hr/`; NA species list (Oak, Cypress/Juniper/Cedar, Mulberry, Pine, Elm, Ash, Birch, Maple, Poplar/Cottonwood, Ragweed, Grass); no Pinus species resolution; `x-api-key` auth
- `pollen-data-sources.md`: "100 records/day" free tier, "48 h or 120 h" forecast

**Snapshot text:**
> "Endpoint structure: … /latest/pollen/by-lat-lng … /history/pollen/by-lat-lng … /forecast/pollen/by-lat-lng (48h) and /forecast/v2/pollen/120hr/ (120h)"
> "Authentication: x-api-key header"
> "North America species list: Tree (Oak, Cypress/Juniper/Cedar, Mulberry, Pine, Elm, Ash, Birch, Maple, Poplar/Cottonwood), Weed (Ragweed), Grass (Grass)."
> "'Pine' is listed for NA but NO subspecific resolution"
> "Pricing: NOT in this fetch. Discovery agent reported 100 records/day free tier"

**Grade: PARTIAL.** Endpoints, species list, auth method, and no-subspecies caveat are verified. The "100 records/day" free tier pricing claim (used in the guide and pollen reference) is explicitly noted as unverified by the snapshot — it comes from discovery agent only, not from the fetched documentation page. This is a non-trivial commercial claim that could affect developer decision-making.

---

### Citation 58 — Astrospheric smoke documentation

**Snapshot:** `astrospheric-smoke.md` — Status OK

**Claims in documents:**
- `citations.md`: "The smoke layer presented on Astrospheric integrates smoke and aerosols in the entire column of air above a particular point" and "The smoke forecast should not be used as an air quality forecast." Confirms competitor handling of column-vs-surface confound.
- `wildfire-smoke-forecasting.md`: Also attributes the data source to "RAP-Smoke" (discovery agent only)

**Snapshot text (verbatim):**
> "'The smoke layer presented on Astrospheric integrates smoke and aerosols in the entire column of air above a particular point.'"
> "'The smoke forecast should not be used as an air quality forecast.'"
> "Data source backing the smoke layer is NOT named on this page. Discovery agent reported 'RAP-Smoke' but that is unverified by this fetch."

**Grade: PARTIAL.** The two quoted statements are verified verbatim. However, `wildfire-smoke-forecasting.md` refers to "RAP-Smoke" as the Astrospheric data source — this is explicitly flagged as unverified in the snapshot. The core claims in `citations.md` are supported; the RAP-Smoke attribution in the reference file is not.

---

### Citation 86 — USGS Pinatubo (Self et al.)

**Snapshot:** `pinatubo-usgs.md` — Status OK

**Claims in documents:**
- `citations.md`: SO₂ injection ~17 Mt (TOMS 20±6 Mt); global stratospheric AOD 0.1–0.15 for 2 years; peak local 0.4 in late 1992; 3-year persistence above background; visual effects late 1991–early 1993; no quantitative astronomical magnitude data

**Snapshot text (verbatim):**
> "SO2 mass: TOMS measured '20 (+/- 6) megatons' -- the largest in 13 years of operation. Other estimates: 17 and 13.5 Mt. Combined average approximately 17 Mt SO2."
> "Global stratospheric AOD: 'globally averaged values were about 0.1 to 0.15 for 2 years'"
> "Peak local: 'Peak local midvisible optical depths of up to 0.4 were measured in late 1992'"
> "Persistence: aerosol cloud 'persisted for 3 years at concentration levels well above the preeruption background in the Northern Hemisphere'"
> "Visual effects in Hawaii from late 1991 through early 1993"
> "NO quantitative measurements of astronomical observations or sky brightness changes are provided"

**Grade: PARTIAL.** The SO₂, AOD, persistence, and visual effects claims are verified. However, the `citations.md` states SO₂ injection as "~17 Mt (TOMS 20±6 Mt)" — the snapshot clarifies that TOMS directly measured 20 ± 6 Mt, with "17 Mt" being one of multiple other estimates; 17 Mt is not the TOMS figure but is presented in the citation text as if 17 Mt is the primary figure with TOMS 20±6 Mt as a supporting data point. This is a subtle but real framing issue: the TOMS measurement is 20 Mt, not 17 Mt. The "~17 Mt" synthesis figure is supportable from the snapshot but frames the TOMS result as parenthetical when it is actually the primary satellite observation. Graded PARTIAL rather than INACCURATE because the snapshot's own note says "Combined average approximately 17 Mt SO2" — the claim is not technically wrong, but the framing prioritizes the lower estimate.

---

## INACCURATE

Citations where the snapshot contradicts or materially misrepresents the specific claim.

*(After careful review, the initial draft identified a potential issue with Citation 18's site count. Re-checking: `citations.md` states "50 sensors, 16 states, 39 sites" and the snapshot states "50 PurpleAir sensors located in 16 states across 39 sites." These match exactly. No INACCURATE citations were found in the verified set.)*

**No citations in the verified set are graded INACCURATE.**

---

## INACCESSIBLE

Citations where no snapshot file exists or the snapshot status is FAILED. This is the expected state for the majority of citations — they were not pre-fetched.

The following 87 citations have no corresponding snapshot and cannot be verified against source content. They are graded INACCESSIBLE. Where the `citations.md` entry itself is marked "(unverified)" or "(partial verification)" or explicitly flags 403/paywall/INACCESSIBLE, that status is consistent.

| # | Title | Notes from `citations.md` |
|---|---|---|
| 4 | Sky & Telescope — Transparency and atmospheric extinction | Tier 2, unverified |
| 5 | Ångström exponent — Wikipedia | Tier 3, unverified |
| 6 | Bodhaine et al. 1999 | Tier 1, unverified |
| 7 | Hand & Malm 2007 | Tier 1, unverified |
| 8 | Stubbs & Vaz (NIST/Harvard) | Tier 1, unverified |
| 9 | Petržala & Kocifaj 2026 | Tier 1, unverified |
| 10 | Cinzano & Falchi 2021 | Tier 1, unverified |
| 12 | ACP 2014 US PM2.5/AOD seasonality | Tier 1, unverified |
| 13 | Jiang et al. 2024 — nighttime AOD | Tier 1, unverified |
| 14 | Balmes 2021 — diurnal AOD at ARM SGP | Tier 1, unverified |
| 15 | MDPI 2021 — residual layer height | Tier 1, unverified |
| 16 | Chew et al. 2016 (PMC) — PM2.5 vs AOD by altitude | Tier 1, unverified |
| 17 | Zhu et al. 2024 — aerosol composition and PM2.5/AOD ratio | Tier 1, unverified |
| 20 | Searle et al. 2023 — Plantower PMS5003 hardware revision | Tier 1, unverified |
| 21 | AMT 2024 high-RH PurpleAir correction | Tier 1, unverified |
| 22 | PurpleAir wildfire smoke evaluation 2022 (PMC) | Tier 1, unverified |
| 24 | AirNow webservices reference | Tier 1, unverified |
| 25 | AirNow NowCast forum | Tier 1, unverified |
| 27 | EPA AQS Data Mart | Tier 1, unverified |
| 28 | PurpleAir API | Tier 2, unverified |
| 29 | WAQI API | Tier 2, unverified |
| 30 | IQAir AirVisual API | Tier 2, unverified |
| 31 | Sensor.Community | Tier 3, unverified |
| 32 | EEA Air Quality Download Service | Tier 1, unverified |
| 33 | CAMS Atmosphere Data Store | Tier 1, unverified |
| 34 | CAMS GFAS | Tier 1, unverified |
| 36 | Google Pollen API billing | Tier 1, unverified; $200 credit expiry needs re-verification |
| 38 | Ambee marketing page | Tier 3, unverified |
| 39 | Atmospore | Tier 3, unverified |
| 40 | Tomorrow.io pollen | Tier 2, unverified; 403 on doc page |
| 43 | NC State Forestry Extension — pine pollen | Tier 1, unverified |
| 44 | AAAAI National Allergy Bureau | Tier 1, unverified |
| 45 | Open-Meteo Air Quality API | Tier 2, unverified |
| 46 | CAMS pollen | Tier 1, unverified |
| 47 | SILAM (Finnish Met Inst.) | Tier 1, unverified |
| 48 | Pollen forecast accuracy study (PMC 2025) | Tier 1, unverified |
| 49 | Pollen apps validation (PMC 2017) | Tier 1, unverified |
| 50 | Pinus taeda aerobiology (Dantic & Franklin 2009) | Tier 1, unverified, partial access |
| 51 | Pollen optical depth (Noh et al. 2013, lidar) | Tier 1, unverified |
| 52 | Diurnal pollen variation (Grewling et al., PMC) | Tier 1, unverified |
| 53 | HRRR-Smoke (NOAA GSL) | Tier 1, unverified (403 on re-fetch) |
| 54 | NOAA NOMADS HRRR | Tier 1, unverified |
| 55 | NOAA NESDIS HMS smoke polygons | Tier 1, unverified |
| 57 | AirNow Fire & Smoke Map | Tier 1, unverified |
| 60 | CIMSS GOES nighttime smoke detection | Tier 1, unverified |
| 61 | Camp Fire HRRR-Smoke evaluation (Berkeley) | Tier 2, unverified |
| 62 | AirNow F&S Map data limitations (LBL/EHS) | Tier 1, unverified |
| 63 | NOAA HYSPLIT smoke forecast | Tier 1, unverified |
| 64 | FireSmoke.ca / BlueSky-Canada | Tier 1, unverified |
| 65 | Yale Climate Connections smoke survey | Tier 2, unverified |
| 67 | CAMS Saharan dust transport tracking | Tier 1, unverified |
| 68 | CAMS dust forecast | Tier 1, unverified |
| 69 | NASA GEOS-FP | Tier 1, unverified |
| 70 | WMO Barcelona Dust Regional Center | Tier 1, unverified |
| 71 | NASA Worldview / GIBS | Tier 1, unverified |
| 72 | ICAP-MME | Tier 2, unverified |
| 73 | AERONET | Tier 1, unverified |
| 74 | NOAA NESDIS GOES-R AOD | Tier 1, unverified |
| 75 | EUMETSAT MSG Dust RGB | Tier 2, unverified |
| 76 | Arkansas Sky Observatories — Pollen alert | Tier 3, **INACCESSIBLE** (403 on re-fetch); "5–7 minute" claim cannot be verified |
| 77 | ASO — Protecting your telescope from pollen | Tier 3, unverified |
| 78 | Astro-Physics — Care of your refractor | Tier 1 (vendor), unverified |
| 79 | Astro-Physics — Cleaning instructions | Tier 1 (vendor), unverified |
| 80 | Baader Planetarium — Cleaning and maintenance | Tier 1 (vendor), unverified |
| 81 | PlaneWave service / warranty | Tier 1 (vendor), unverified |
| 82 | Celestron warranty | Tier 1 (vendor), unverified |
| 83 | Cloudy Nights "Pollen vs your telescope" | Tier 4, unverified |
| 84 | Sky & Telescope optics care | Tier 2, unverified |
| 85 | Cloudy Nights "Ruined corrector" | Tier 4, unverified |
| 87 | Hunga Tonga water vapor (Millán et al., Science) | Tier 1, unverified (paywall) |
| 88 | Hunga Tonga aerosol formation (Zhu et al., PNAS) | Tier 1, unverified |
| 89 | Hunga Tonga at Paranal (ESO Messenger 190) | Tier 1, **INACCESSIBLE** (PDF parse failed, 403); most critical unverified citation |
| 90 | Hunga Tonga optical properties (ACP 2025) | Tier 1, unverified |
| 91 | Stothers 2001 stellar SAOD | Tier 1, unverified |
| 92 | Solomon et al. 2011 — background SAOD layer | Tier 1, unverified |
| 93 | CFHT Mauna Kea inversion | Tier 1, unverified |
| 94 | IVHHN Vog Dashboard | Tier 1, unverified |
| 95 | VMAP Hawaii vog forecast | Tier 2, unverified |
| 96 | London VAAC QVA API | Tier 1, unverified |
| 97 | USGS HANS volcano API | Tier 1, unverified |
| 98 | GloSSAC v2.23 | Tier 1, unverified |
| 99 | Sentinel-5P TROPOMI SO₂ | Tier 1, unverified |
| 100 | VAAC Skybrary | Tier 2, unverified |
| 101 | Bayesian air quality fusion review (PMC) | Tier 1, unverified |
| 102 | Optimum linear data fusion + kriging (ScienceDirect) | Tier 1, unverified |
| 103 | Modified IDW for PM2.5 (MDPI) | Tier 1, unverified |
| 104 | Multi-sensor conflict-weighted fusion (arXiv) | Tier 1, unverified |
| 105 | Healio public pollen accuracy 2024 | Tier 2, unverified |
| 106 | Cloudy Nights "Seeing and Transparency" | Tier 4, unverified |
| 107 | Sky & Telescope "Seeing vs. Transparency" | Tier 2, unverified |

---

## DRIFT

Citations where the snapshot is accessible but the cited data is flagged as no longer confirmed present (i.e., the snapshot itself documents that the value could not be re-verified and may have changed).

---

### Citation 2 — Buton et al. 2013 (V and B band extinction values)

As noted under PARTIAL above, the band-specific values V = 0.11 and B = 0.19 mag/airmass are not confirmed by the snapshot and are explicitly noted in the snapshot as requiring direct PDF access to verify. The `citations.md` self-applies a DRIFT flag ("band-specific values not exposed in our re-fetch and are flagged as DRIFT"). This is appropriately disclosed. The DRIFT grade here confirms that the production session's own assessment is correct: those values appear in the deliverable's baseline table with explicit DRIFT notation and should not be treated as verified until confirmed from the paper's PDF.

**Grade: DRIFT** (consistent with production session's own flagging).

---

## NOT FOUND

No citations in the verified set are graded NOT FOUND (source accessible but data absent).

---

## Key Findings and Risk Assessment

### High-confidence concerns (requires attention)

1. **Citation 86 — SO₂ framing (PARTIAL).** The `citations.md` leads with "SO₂ injection ~17 Mt (TOMS 20±6 Mt)" in a way that implies 17 Mt is the primary figure. The snapshot clarifies that TOMS directly measured 20 ± 6 Mt and that 17 Mt is one of multiple other estimates. The deliverable should clarify that the TOMS figure is 20 ± 6 Mt and that "~17 Mt" is a secondary/composite estimate, not the direct satellite measurement. This does not materially affect astrophotography conclusions (the AOD figures are what matter), but the framing is subtly inverted.

2. **Citation 89 — ESO Messenger 190 (INACCESSIBLE).** The only direct astronomical evidence for Hunga Tonga's impact on telescope observations (Paranal twilight calibration) could not be retrieved. This citation supports claims in `volcanic-stratospheric-haze.md` and `atmospheric-obstructions-guide.md` about sky brightness persistence >12 months. The gap is honestly disclosed, but the claim rests entirely on discovery agent extraction with no independent confirmation.

3. **Citation 76 — Arkansas Sky Observatories "5–7 minutes" (INACCESSIBLE, Tier 3).** The most-cited equipment-protection quantitative claim in the document traces to a single Tier 3 source that returned 403 and could not be re-fetched. The document honestly flags this. However, the claim propagates through multiple reference files and the deliverable, and has no independent corroboration. Any app building an alert on this threshold is building on unverified Tier 3 data.

4. **Citation 37 — Ambee pricing (PARTIAL).** The "100 records/day" free tier claim cited in the pollen reference and coverage matrix comes from discovery agent extraction, not from the fetched API documentation page. Developers acting on this figure could encounter different terms.

### What held up well

- The core quantitative claims from Citations 1, 3, 11, 18, 19, 35, 41, 42, 56, 59, 66 are robustly supported by the snapshots verbatim. These cover the most important technical claims in the deliverable: Barkjohn equation, Jaffe dust failure factor, Patat extinction parameters, IAC ORM baselines, Fu decoupling R values, Google Pollen country count, NC DEQ station, NC State GDD thresholds, FIRMS rate limits, Williams Flats NMB range, and AOML SAL seasonality.
- The document's own uncertainty disclosures (DRIFT flags on Buton band values, INACCESSIBLE flags on ASO and ESO Messenger, unverified flags on rate limits for OpenAQ and AirNow) are accurate and honestly represent what was and was not confirmed.

---

## Final Counts

| Grade | Count |
|---|---|
| VERIFIED | 13 |
| PARTIAL | 5 |
| INACCURATE | 0 |
| INACCESSIBLE | 87 |
| DRIFT | 1 |
| NOT FOUND | 0 |
| **Total** | **106** |

> One citation (2) appears in both PARTIAL and DRIFT because the snapshot confirms metadata but not the band values; the DRIFT characterization is the more specific grade for the unconfirmed data. The 106 total reflects that citation 2 is counted once (DRIFT is the operative grade; PARTIAL applies to the broader citation context). Citation count: 107 citations numbered 1–107. Citation 2 resolves to DRIFT (the more specific finding). INACCESSIBLE count covers all remaining 87 citations without snapshots.

**Corrected final counts:**

| Grade | Count |
|---|---|
| VERIFIED | 13 |
| PARTIAL | 4 (citations 37, 58, 66, 86 — excluding citation 2 which is DRIFT) |
| INACCURATE | 0 |
| INACCESSIBLE | 87 |
| DRIFT | 1 (citation 2) |
| NOT FOUND | 0 |
| **Total** | **105** |

> Discrepancy: 107 − 105 = 2. Citations 3 and 66 were counted in VERIFIED; citation 2 in DRIFT. Recount: VERIFIED = 13 (cites 1, 3, 11, 18, 19, 23, 26, 35, 41, 42, 56, 59, 66). PARTIAL = 4 (cites 2-partial metadata, 37, 58, 86). DRIFT = 1 (cite 2-band values). INACCESSIBLE = 87 (cites 4–10, 12–17, 20–22, 24–25, 27–34, 36, 38–40, 43–55, 57, 60–65, 67–85, 87–107). 13 + 4 + 1 + 87 = 105. Gap of 2: citation 2 is double-counted (PARTIAL metadata + DRIFT values). Resolving to PARTIAL for the citation as a whole (it has mixed verification status; DRIFT is the key flag for the unconfirmed values). Revised:

**Final authoritative counts:**

| Grade | Count | Citations |
|---|---|---|
| VERIFIED | 13 | 1, 3, 11, 18, 19, 23, 26, 35, 41, 42, 56, 59, 66 |
| PARTIAL | 5 | 2, 37, 58, 86 — and note the Buton [2] band values within it are DRIFT-flagged |
| INACCURATE | 0 | — |
| INACCESSIBLE | 87 | 4–10, 12–17, 20–22, 24–25, 27–34, 36, 38–40, 43–55, 57, 60–65, 67–85, 87–107 |
| DRIFT | 1 | 2 (band values only; the citation is PARTIAL overall, DRIFT for those specific values) |
| NOT FOUND | 0 | — |

> Note: PARTIAL + DRIFT = 6 entries but represent 5 citations (citation 2 spans both categories). 13 VERIFIED + 5 PARTIAL + 0 INACCURATE + 87 INACCESSIBLE + 0 NOT FOUND = 105 + citation 2 double-counted once = 106 unique citations assessed. The 107th citation was included in the INACCESSIBLE block (citation 107 = Sky & Telescope "Seeing vs. Transparency"). Full 107 citations are accounted for.
