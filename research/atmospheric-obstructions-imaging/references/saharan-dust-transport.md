# Saharan dust transport

**Dimension scope:** programmatic data sources for forecasting Saharan Air
Layer (SAL) dust transport across the Atlantic into the Caribbean and
Southeast US, where it reduces transparency during summer months.

See [citations.md](../citations.md) for full source details.

## What the SAL is, and when it matters

NOAA AOML [66]: the Saharan Air Layer is "a mass of very dry, dusty air that
forms over the Sahara Desert during the late spring, summer, and early fall…
a 2 to 2.5-mile-thick layer of the atmosphere with the base starting about
1 mile above the surface."

**Seasonal timing** [66]:

- Activity escalates **mid-June**.
- Peak intensity: **mid-June through mid-August**.
- Declines after mid-August.
- During peak season, fresh outbreaks emerge from Africa **every 3–5 days**.

**Geographic reach** [66]: regularly reaches the Caribbean; can extend west
to Florida, Central America, Texas. Coverage areas can span regions
"comparable in size to the continental US."

## Data product matrix

| Product | Type | Coverage | Resolution | Access | Cost / license |
|---|---|---|---|---|---|
| **CAMS Global Atmospheric Composition Forecast** [68] | Forecast | Global | ~40 km, twice daily, 5-day | CDS API (`cdsapi`); variable `composition_duaod550` (dust AOD 550 nm) | Free, CC-BY |
| **CAMS via Open-Meteo Air Quality** [45] | Wrapped CAMS forecast | Global | 45 km global, 11 km Europe | Free no-key REST JSON | Free non-commercial |
| **NASA GEOS-FP** [69] | Forecast (GMAO) | Global | 0.25°, 10 day, 3-hourly | OPeNDAP at `opendap.nccs.nasa.gov` | Free; HTTPS/OPeNDAP |
| **NASA Worldview / GIBS** [71] | Imagery (MODIS, MAIAC) | Global | 1 km (MAIAC), 10 km (MODIS) | WMTS tiles | Free imagery only — not gridded numbers |
| **NOAA NESDIS GOES-R AOD** [74] | Observation | CONUS | ~2 km nadir, 10-min | NOAA STAR / AWS S3 `noaa-goes16/18` | Free |
| **VIIRS L2/L3 AOD** | Observation (NOAA STAR) | Global | 6 km (L2), 0.1°/0.25° (L3) | AWS S3 anonymous + NOAA STAR HTTP | Free |
| **EUMETSAT Sentinel-3 SLSTR NRT AOD** [from Dim3 Discovery] | Observation | Global | 9.5 km, NRT < 3 hr | EUMETSAT Data Store API | Free with account |
| **EUMETSAT MSG Dust RGB** [75] | Imagery | Africa/Europe/Atlantic | Geostationary | EUMETSAT Data Store | Account required; image only |
| **WMO Barcelona Dust Regional Center (MONARCH)** [70] | Forecast (regional) | N. Africa, Europe, Mediterranean | 72-h regional | THREDDS/OPeNDAP/WMS/WCS | Public access embargoed >2 days; NRT institutional only |
| **NRL ICAP-MME** [72] | 9-model ensemble | Global | 6-hr to 120-hr | Visualization confirmed; programmatic NetCDF unclear | Visualization free |
| **AERONET** [73] | Ground truth | ~hundreds of sites | ~15-min cadence; 340–1640 nm | REST web service | Free |
| **NOAA HYSPLIT** [from Dim3 Discovery] | Backward trajectory | Global | Variable | READY web API (250 calls/day with key) | Free |
| **UW-CIMSS SAL tracking** [from Dim3 Discovery] | Imagery (GOES-16 split-window IR, water vapor, RGB) | Atlantic | 3-hr archive | HTTP image archive at `tropic.ssec.wisc.edu/real-time/sal/` | Free |
| **NOAA AOML SAL hub** [66] | Multi-source visualization | Atlantic / Caribbean | N/A | Web portal | Free |

## Recommended primary source for an app

**For a Southeast US planning app, CAMS dust AOD via the CDS API [68] is the
practical primary source**, supplemented by:

- **AOML's seasonal context** [66] for "is this the active season?" UI cue.
- **AERONET ground truth** [73] for nearest-station comparison when available
  (NC has limited AERONET coverage; nearest stations are typically in MD, VA,
  or FL).
- **CIMSS SAL imagery** for visual confirmation during active outbreaks.

Open-Meteo's wrap of CAMS [45] provides a no-key alternative — useful for
prototyping but with reduced resolution (45 km global vs CAMS native 40 km)
and a non-commercial license restriction.

## Column vs surface, again

The SAL has its **base ~1 mile above the surface** and is **2–2.5 miles thick** [66]. Surface PM2.5 will
not detect it directly during transit; it manifests as:

- Visibly reddened sun at sunrise/sunset
- Hazy whitish daytime sky
- Measurable AOD increase at AERONET stations
- Ground-level PM2.5 increase only when subsidence brings dust to surface
  (typically 24–48 hr after column arrival in the SE US)

Counter-perspective from observatory data [3]: at the Canary Islands ORM,
**only ~20% of dust outbreaks affecting the Canaries actually reach
observatory altitudes.** This implies that even a strong CAMS dust AOD
forecast may not translate to ground-observer transparency loss — the
dust may pass overhead at SAL altitude (1.5–5 km) without descending.

For SE US ground-based observers, dust transport detected by CAMS does not
guarantee imaging-quality degradation. The **column-integrated AOD** matters
for transparency (since starlight passes through the entire column), but the
height distribution affects scatter geometry.

## Forecast skill caveats

- **CAMS dust forecast skill in North America is not well characterized in
  open literature** found in this run. The 2024 Cy48R1 upgrade introduced
  larger negative biases over North America before subsequently improving
  [from Dim2 Counter agent extraction].
- **CAMS specifically assumes volcanic SO₂ injection at 500 hPa (~5 km)**,
  which is a known limitation for stratospheric eruptions but does not
  directly affect tropospheric SAL transport modeling.
- **ICAP-MME ensemble disagreement during specific events** is documented
  but not quantitatively characterized in accessible papers found.

## Gaps and limitations

- **CAMS direct API page** (`ads.atmosphere.copernicus.eu/api/v2`) was not
  individually re-fetched in this run. The dataset specifics (variable name
  `composition_duaod550`, 0.35° resolution, twice-daily run) come from
  discovery agent extraction and need re-verification before deploying
  against the API.
- **No paper found quantifying SAL-induced transparency loss in stellar
  magnitudes** at typical SE US elevations (sea level to 3,000 ft Piedmont).
  The Canary Islands ORM data [3] is the closest analog but is at 2,396 m
  elevation with very different atmospheric column.
- **Barcelona DRC NRT data is institutionally restricted** [70]; the public
  embargo of >2 days makes their MONARCH high-resolution regional forecast
  unusable for next-night planning by a hobbyist app.
- **No app currently surfaces a CAMS-dust-AOD-to-Bortle-equivalent conversion**
  that would be actionable for the user.
