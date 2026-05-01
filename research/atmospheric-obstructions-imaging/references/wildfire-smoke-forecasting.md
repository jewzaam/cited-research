# Wildfire smoke forecasting

**Dimension scope:** programmatic data sources for forecasting wildfire smoke
arrival, transport, and dissipation 0–72 hours out, with assessment of forecast
skill ceilings and how column-vs-surface confounds affect astrophotography use.

See [citations.md](../citations.md) for full source details.

## Data product matrix

| Product | Type | Coverage | Resolution | Forecast horizon | Access | Cost |
|---|---|---|---|---|---|---|
| **HRRR-Smoke** [53, 54] | Forecast (NOAA WRF-based) | CONUS + AK | 3 km | 18 h std, 48 h extended | NOMADS GRIB2, AWS S3 mirror `noaa-hrrr-bdp-pds` | Free |
| **NAQFC** | Forecast (NOAA NWS) | CONUS, AK, HI | ~5 km / 6 km / 2.5 km | 51 h | AWS S3 `noaa-nws-naqfc-pds` | Free |
| **RRFS-Smoke/Dust** | Experimental forecast (NOAA GSL) | North America | 3 km | 18 h / 3-day 4×/day | Restricted access (403 on direct fetch) | Experimental |
| **CAMS Global Atmospheric Composition Forecast** [33] | Forecast (ECMWF) | Global | ~40 km | 5 day | CDS API (cdsapi Python) | Free with registration |
| **CAMS GFAS** [34] | Fire emissions analysis | Global | 0.1° | Analysis only (24 h means) | CDS API | Free, CC-BY |
| **NOAA HMS smoke polygons** [55] | Observational (analyst-drawn from satellite) | North America | Polygon | None (current state only) | HTTP shapefile/GeoTIFF/KML | Free |
| **NASA FIRMS** [56] | Active fire detection | Global | VIIRS 375 m, MODIS 1 km | None (observation) | REST API | Free MAP_KEY, 5000 tx/10 min |
| **AirNow Fire & Smoke Map** [57] | Composite (HMS + monitors + PurpleAir) | US | Variable | Current + 24/48 h forecast | AirNow API [23] | Free |
| **GOES-R ABI ADP** | Smoke/dust detection (daytime only) | Americas | 2 km | None (observation) | AWS S3 `noaa-goes16/18` | Free |
| **NOAA HYSPLIT smoke** [63] | Transport model | CONUS/AK/HI | Variable | 48 h | Shapefiles at airquality.weather.gov | Free |
| **FireSmoke.ca (BlueSky-Canada)** [64] | Forecast (UBC) | Canada (extends to N. US) | Variable | 2 day | NetCDF/KMZ HTTP | Free, seasonal Apr–Sep |

## HRRR-Smoke specifics

GRIB2 variables [53, 54]:

- `MASSDEN` — Mass density at 8 m AGL, kg/m³ (near-surface PM2.5-from-smoke
  proxy). **Note**: pre-2021-12-21 the field was mislabeled as µg/m³;
  corrected thereafter (per discovery agent extraction from NOAA GSL forum;
  not independently verified).
- `COLMD` — Column-integrated mass density (entire atmosphere). **This is
  what astrophotographers actually want** — it represents the column starlight
  passes through.

Files at `https://nomads.ncep.noaa.gov/pub/data/nccf/com/hrrr/prod/`,
filename pattern `hrrr.tCCz.wrfsfcfHH.grib2`. AWS S3 mirror at
`noaa-hrrr-bdp-pds` (anonymous access).

## Forecast skill: peer-reviewed verification

The 2021 ACP Williams Flats fire model intercomparison [59] is the most
direct evidence on operational smoke forecast skill:

- **12 systems compared** (3 global + 9 regional, including HRRR-Smoke,
  NAQFC, CAMS, GEOS-FP, NRL NAAPS).
- Williams Flats fire (44,446 acres, Washington, August 2019) intensively
  observed during FIREX-AQ field campaign.
- **All 12 models underpredicted AOD.** Normalized mean bias range:
  −87.4% to −4.3%.
- **Spatial correlation r ≤ 0.50** for all models.
- FRP-based emission inventories produced estimates **6.4× higher on average**
  than hotspot-based; FRP-based models generally outperformed hotspot-based.

A 2022 Berkeley study of HRRR-Smoke during the 2018 Camp Fire [61] documented
**up to 70% PM2.5 underprediction** in week two due to satellite blindness:
thick smoke obscured fire detection, so the model's forcing weakened while
the actual fire intensified.

**The persistence assumption is the central failure mode.** Smoke models
assume the fire as last observed by satellite continues unchanged. When a
fire grows rapidly overnight (when satellites are less effective or smoke
itself obscures detection), the next 24–36 h forecast starts with
systematically underestimated emissions [59].

## Geostationary smoke detection has a nighttime gap

GOES visible-band smoke detection requires solar or lunar illumination [60].
At night, smoke "is not present at all in the infrared imagery" unless
extraordinarily thick [60]. VIIRS Day-Night Band can retrieve nighttime AOD
in rural areas via reflected moonlight, but only away from city lights and
only with sufficient lunar phase. **For an astrophotography app, nighttime
smoke detection is structurally limited** — exactly when it matters most.

## AirNow Fire & Smoke Map limitations

AirNow F&S Map composites HMS smoke polygons + regulatory monitors +
EPA-corrected PurpleAir into a unified visualization [57]. Limitations:

- **NowCast lag**: minimum 3-hour effective averaging floor [25]. A fast-onset
  smoke front can be 60–95 minutes stale by the time NowCast reflects it.
- **PurpleAir correction breaks at extreme smoke**: only 5 of 15 smoke-impacted
  sites met EPA performance targets at hourly averages [22]. Above
  300 µg/m³, the standard Barkjohn equation [18] underestimates; a piecewise
  quadratic correction has been proposed but introduces a different positive
  bias at 150–300 µg/m³ [22].
- **Sensors systematically underestimate dust events** [62].

## Column vs surface — the key astrophotography distinction

**Astrospheric, the existing astrophotography app, addresses this explicitly**
[58]:

> "The smoke layer presented on Astrospheric integrates smoke and aerosols
> in the entire column of air above a particular point... The smoke forecast
> should not be used as an air quality forecast."

A 2025 AMT case study [from Dim2 counter agent, citing AMT 17, 6735] found that
the same overhead smoke plume produced surface PM2.5 < 15 µg/m³ in one case
and > 150 µg/m³ in another, depending on whether the planetary boundary layer
was growing or collapsing at the time of plume arrival.

**Practical implication**: an app that uses surface PM2.5 as a smoke proxy
will be wrong in two predictable ways:

1. False clear: lofted smoke (Canadian wildfire transport, often above the
   PBL) gives "Good" surface AQI but high column AOD → poor transparency.
2. False degraded: ground-trapped smoke or boundary-layer collapse can give
   high surface PM2.5 with negligible column-AOD impact for column-integrated
   transparency. The astrophotographer cares about column AOD.

## Recommended fetch strategy

For a planning app:

1. **Primary forecast (24–48 h horizon)**: HRRR-Smoke COLMD (column-integrated)
   from AWS S3 — this is the variable that maps to transparency.
2. **Now-state observation**: NOAA HMS smoke polygons (analyst-drawn,
   updated daily, North America) [55] for "is there smoke overhead now?"
3. **Active fire detection (upstream input)**: NASA FIRMS [56] for "is there
   a fire near me right now?"
4. **Long-range global**: CAMS Global Atmospheric Composition Forecast [33]
   for users outside North America.
5. **Surface PM2.5 cross-check**: AirNow [23] / PurpleAir [28] for human
   air-quality alerts (separate from transparency assessment).

## Gaps and limitations

- **HRRR-Smoke direct documentation page returned 403** during this run [53].
  Variable specifics rely on discovery-agent extraction from NOAA GSL forum
  threads.
- **Astrospheric data source is not publicly disclosed** [58] — discovery
  agent reported "RAP-Smoke" but this is not on the cited page.
- **Forecast skill beyond 24 h is poorly characterized in public literature**;
  the Williams Flats study [59] is a single-fire case study. Multi-season
  systematic skill scores by lead time are not published in accessible form.
- **No source provides smoke-AOD-to-narrowband-extinction conversion** for
  amateur narrowband imaging (Ha 656 nm, OIII 500 nm). Smoke is fine-mode
  (Ångström α 1.5–2.5 [5]) so OIII is more affected than Ha — but this has
  not been empirically validated for typical western US smoke composition.
