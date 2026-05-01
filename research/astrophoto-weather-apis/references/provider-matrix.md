# Provider Matrix — Multi-Layer Cloud Cover APIs

**Dimension covered:** Which weather APIs expose low/mid/high cloud cover separately (vs. a single aggregate), at what cadence, with what schema, region coverage, and forecast horizon.

Sources: [`citations.md`](../citations.md).

## Headline finding

**Definitions of "low / mid / high cloud" are not comparable across providers.** ECMWF uses sigma-coordinate boundaries that are terrain-relative [8]. WMO's International Cloud Atlas defines bases by altitude in km, **latitude-dependent**: high-cloud bases at 3 km (polar), 5 km (temperate), 6 km (tropical) [15]. NOAA SPC uses absolute pressure cutoffs (high 350–150 hPa, mid 642–350 hPa, low <642 hPa). Open-Meteo's `cloud_cover_low/mid/high` derives from RH at pressure levels when native model fields are unavailable [1]. Comparing one provider's `low cloud` to another's is comparing different physical quantities under the same name.

## Comparison table

| Provider | Low/mid/high separately? | Free-tier endpoint | Region coverage | Max horizon | Native cadence | Schema/format | Layer definition | Cite |
|---|---|---|---|---|---|---|---|---|
| Open-Meteo | Yes — `cloud_cover_low` (0–3 km) / `_mid` (3–8 km) / `_high` (8 km+) | `https://api.open-meteo.com/v1/forecast` | Global | 16 days (default 7) | Hourly | JSON | Altitude-band, fixed | [1] |
| MET Norway | Yes — `cloud_area_fraction_low` (<2000 m) / `_medium` (2000–5000 m) / `_high` (>5000 m) | `https://api.met.no/weatherapi/locationforecast/2.0/{compact|complete}` | Global (Nordic 2.5 km MEPS, elsewhere ECMWF-derived) | ~10 days | 1h first ~60 h then 6h | JSON | Altitude-band, fixed | [3], [4] |
| Meteomatics | Yes — `low_cloud_cover` (0–1800 m AGL) / `medium_cloud_cover` (1800–6300 m AGL) / `high_cloud_cover` (>6300 m AGL) | `https://api.meteomatics.com/{datetime}/{params}/{loc}/{format}` | Global | varies | Hourly + intervals (1h/2h/6h/12h/24h means) | JSON, CSV, NetCDF, GRIB | Altitude-band AGL, fixed | [11], [12] |
| ECMWF Open Data | Yes — LCC (param 186 / `lcc`) / MCC (187 / `mcc`) / HCC (188 / `hcc`) / TCC (164 / `tcc`) | `https://data.ecmwf.int/forecasts/` (GRIB2 files) | Global | **HRES: 240 h (10 days)**; ENS: 360 h (15 days) at 00Z/12Z; 144 h at 06Z/18Z. The Open Data catalogue covers both. | 3 h to 144 h, then 6 h | GRIB2 | **Sigma-based**, terrain-relative: LCC σ>0.8, MCC σ 0.45–0.8, HCC σ<0.45 (dimensionless sigma values are exact; the pressure-level approximations sometimes given in secondary sources are derivative) | [7], [8], [9] |
| OpenWeatherMap | **No** — single aggregate `clouds` field only | `https://api.openweathermap.org/data/3.0/onecall` | Global | 48 h hourly + 8 days daily | Hourly | JSON | N/A | [10] |
| Tomorrow.io | **No** — `cloudCover` (aggregate %), `cloudBase` (km), `cloudCeiling` (km) only | `https://api.tomorrow.io/v4/...` | Global | varies | Hourly | JSON | N/A — but `cloudCeiling` useful for minimum-clearing-height filter | [13] |
| Visual Crossing | **No** — single aggregate `cloudcover` field | Timeline API | Global | 15 days | Hourly | JSON, CSV | N/A | [14] |
| NOAA/NWS api.weather.gov | **No** — `skyCover` (single aggregate %) | `https://api.weather.gov/gridpoints/{office}/{x},{y}` | CONUS / US territories | ~7 days hourly | Hourly | JSON | N/A | [5], [6] |

## Layer-definition incompatibility — worked example

Take a cumulus cloud with base at 700 hPa and top at 600 hPa over the Carolinas (sea-level surface pressure ~1013 hPa). For the SAME physical cloud:

- **ECMWF (sigma-based)** [8]: σ at 700 hPa over a 1013 hPa surface = 700/1013 ≈ 0.69 (est.) → falls in MCC band (0.45–0.8). Reported as `MCC`.
- **Open-Meteo (altitude-based)** [1]: 700 hPa ≈ 3 km AGL, falls at the boundary of "low" (0–3 km) and "mid" (3–8 km). Reported as either or split.
- **Meteomatics (altitude AGL)** [11]: 700 hPa ≈ 3000 m AGL, well within the medium band (1800–6300 m). Reported as `medium_cloud_cover`.
- **MET Norway (altitude)** [3]: 3 km AGL → falls in `cloud_area_fraction_medium` (2000–5000 m).
- **NOAA SPC (pressure)**: 700 hPa is below the 642 hPa threshold → reported as low cloud.

The same physical cloud is reported as low in NOAA's framework, mid in ECMWF/Meteomatics/MET Norway, and split between low/mid in Open-Meteo. **An app that surfaces raw `low/mid/high` from multiple providers without harmonizing definitions will display incoherent information.**

## Documented data-quality issues

- **Open-Meteo bug #416 [2]:** At elevated sites (>500 m elevation), `cloudcover_low` includes pressure levels physically below the terrain (1000 hPa ≈ sea level, 975 hPa ≈ 300 m). Result: clear-sky 100% low-cloud reports at Appalachian / Blue Ridge sites. Issue remains open in the snapshot examined. **Direct relevance to SE US users at elevated dark-sky sites.**
- **Open-Meteo issue #1135 [17]:** ECMWF History API silently returned null for `cloud_cover` and `weather_code` for October 12–16, 2024 across all coordinates. Closed without disclosed resolution.
- **OWM cloud-cover inversion claim [56]:** Home Assistant integration #119873 reported OWM cloud cover inverted (0% = overcast). Closed "not planned"; whether the fault is OWM or the integration mapping is unconfirmed.
- **Pirate Weather discontinuity [16]:** "Currently" block can jump discontinuously between RTMA-RU analysis cycles; cloud cover is a model-blend output, not from a single coherent source.

## Provider behavior at the edges

- **NWS** is a national-scale forecast that exposes only an aggregate `skyCover` percentage. The OpenAPI spec lists no `lowClouds`/`midClouds`/`highClouds` fields [5], [6]. NWS does not feed an astrophoto-grade multi-layer signal.
- **Open-Meteo "ECMWF API" sub-endpoint** can serve LCC/MCC/HCC for those who want sigma-based ECMWF semantics, separately from the main `/v1/forecast` endpoint that uses altitude bands. Worth verifying whether values agree on the same lat/lon (open question — flagged as gap below).
- **Pirate Weather** wraps GFS + HRRR + NBM by region; useful as a Dark Sky drop-in but layer fields and definitions are not centrally documented [16].

## Provider behavior outside North America

For users targeting global coverage (or future expansion):
- **MET Norway** drops from 2.5 km MEPS to ECMWF-derived global outside Nordic — accuracy in SE US Carolinas falls back to global ECMWF [3].
- **Open-Meteo `minutely_15`** is HRRR-backed inside CONUS, ICON-D2 / AROME inside Central Europe; elsewhere it interpolates from hourly [91], [92] (covered in Dim 5).
- **Astrophoto-specific aggregators** with their own model stack (Dim 8) sit on top of these primary feeds and add their own limitations.

## Gaps and limitations

- The Tomorrow.io enterprise tier was not directly queried for whether it exposes layered cloud beyond `cloudCover/Base/Ceiling`. The base API does not appear to expose them; enterprise-only fields are unverified.
- Visual Crossing premium fields were not queried beyond the public docs. The aggregate `cloudcover` is the only documented cloud field.
- The exact Meteomatics URL token strings (`low_cloud_cover:p`, `low_cloud_cover_1h:p`, etc.) are described in docs but no working sample URL was extracted.
- Whether NOAA NDFD raw GRIB exposes layered cloud beyond the JSON API's `skyCover` aggregate is unverified; the JSON API definitively does not.
- A direct field-by-field comparison of the SAME lat/lon at the SAME forecast hour across these providers was not performed. Doing so would be the strongest empirical demonstration of the layer-definition incompatibility identified above.
- Open-Meteo's cloud-cover bug #416 [2] resolution status was not re-checked at deliverable time; for SE US Appalachian users, this is a non-trivial defect that should be re-verified.
