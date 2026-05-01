# Underlying NWP Models

**Dimension covered:** The numerical weather prediction models that drive cloud forecasts in the APIs reviewed in [`provider-matrix.md`](provider-matrix.md). Spatial resolution, forecast horizon, update cadence, geographic coverage, cloud-cover output products, and dominance regimes.

Sources: [`citations.md`](../citations.md).

## Headline finding

For the Southeast US (Carolinas / Piedmont / Blue Ridge):
- **HRRR** is the highest-resolution operational NWP source (3 km, hourly), CONUS-only, 18-hour horizon (48-hour on 00/06/12/18Z extended cycles) [19], [20], [21].
- **GFS** is the global default for medium-range (16-day) forecasts at 0.25° (~28 km output grid) [24].
- **ECMWF IFS HRES** is the highest-skill global model for medium range (10-day at 240h, 9 km native; full real-time catalogue open under CC-BY-4.0 at **25 km publicly accessible subset since October 1, 2025**, with 9 km HRES extension **planned for later in 2026** with 2-hour latency) [27], [28], [63].
- **AI-based models** (GraphCast, Pangu-Weather, FourCastNet) **do not output cloud cover** — they trained on ERA5 pressure-level variables that exclude cloud fraction [42], [43], [44].
- **HRRR / RAP / NAM are scheduled for retirement** when RRFS becomes operational, with timeline now in flux as of February 2026 [47], [48].

## Model comparison table

| Model | Operator | Resolution | Forecast horizon | Update cadence | Region | Cloud cover output | Cloud-resolving? | Cite |
|---|---|---|---|---|---|---|---|---|
| HRRR | NOAA NCEP | 3 km | 18 h (48 h on 00/06/12/18 Z extended cycles) | Hourly | CONUS only | LCDC, MCDC, HCDC, TCDC + cloud ceiling/base/top in hourly `wrfsfcf`; **no cloud-fraction in 15-min `wrfsubhf`** | Yes (convection-allowing) | [19], [20], [21], [22] |
| RAP | NOAA NCEP | 13 km, 50 levels | 21 h (51 h on 03/09/15/21 Z) | Hourly | North America | LCDC, MCDC, HCDC, TCDC + cloud ceiling/base/top | No | [23] |
| GFS | NOAA NCEP | 0.25° (~13 km native T1534, ~28 km output); degrades to ~70 km past day 7 | 384 h (16 days) | 4×/day (00/06/12/18 Z) | Global | TCDC + standard NCEP layered cloud (LCDC/MCDC/HCDC inferred from convention; not directly verified in inventory access) | No (Arakawa-Schubert convection parameterization) | [24] |
| NAM | NOAA NCEP | 12 km parent + 3 km nests (CONUS, AK, HI, PR) + 1.5 km fire weather | 84 h (parent), 60 h (nests), 36 h (fire) | 4×/day | North America | TCDC + layered cloud per NCEP convention | Nested 3 km is convection-allowing | [24] |
| ECMWF IFS HRES | ECMWF | 9 km native (since Cycle 41r2, March 2016); 137 levels. **Open data: 25 km publicly accessible subset since Oct 1, 2025; 9 km HRES extension planned for later in 2026 with 2-hour latency [63]** | 240 h (10 days) at 00/12 Z; 90 h at 06/18 Z | 4×/day | Global | LCC (param 186), MCC (param 187), HCC (param 188), TCC (param 164) — **sigma-based** boundaries [8] | No | [27], [28], [63] |
| ECMWF AIFS Single v1 | ECMWF | 28 km grid spacing | (matches IFS, exact horizon not directly confirmed) | 6 h | Global | tcc, lcc, mcc, hcc — first AI model to output them (cloud-variable list per [32]; operational status February 25, 2025 per [31]) | No | [31], [32] |
| ICON Global | DWD | 13 km (0.1° output), 90 levels | 180 h (00/12 Z), 120 h (06/18 Z) | 4×/day | Global | CLCL, CLCM, CLCH, CLCT | No | [34] |
| ICON-EU | DWD | 6.5 km (~7 km output), 60 levels | 120 h + 30 h extra runs | 4×/day | Europe nested | CLCL, CLCM, CLCH, CLCT | Partly | [34] |
| ICON-D2 | DWD | 2.2 km, 65 levels | 48 h | Every 3 h (8×/day) | Germany + neighbors | CLCL, CLCM, CLCH, CLCT | Yes | [34] |
| AROME France / HD | Météo-France | 2.5 km / 1.5 km HD | 42–51 h (HD 15-min: 6 h) | Every 3 h | France + neighbors | Low/mid/high cloud | Yes | (Météo-France official sources, via Open-Meteo) |
| GraphCast | Google DeepMind | 0.25° (~25 km) | 240 h (10 days) in 6-h steps | (not operationally scheduled) | Global | **None — cloud cover not in 227-variable output set** | N/A | [42] |
| Pangu-Weather | Huawei | 0.25° | 1–168 h | (not operationally scheduled) | Global | **None — 69 variables on pressure levels and surface, no cloud fraction** | N/A | [43] |
| FourCastNet | NVIDIA | 0.25° | autoregressive 6-h steps | (not operationally scheduled) | Global | **None — TCWV is closest proxy** | N/A | [44] |
| RRFS (forthcoming) | NOAA NCEP | 3 km CONUS + 2.5 km HI/PR | 18 h (84 h on 00/06/12/18 Z) | Hourly | CONUS + AK | (not yet documented in accessible sources) | Yes | [47], [48] |

## Documented model biases relevant to cloud forecasting

### HRRR cloud underprediction
Multiple peer-reviewed studies converge:
- **James & Turner 2025 [77]** (MWR ahead of print): excessive surface shortwave at all 14 SURFRAD stations attributed to insufficient cloud attenuation; experimental fixes cut bias 80–84% in fall/winter, only **35% in summer** — summer is the regime hardest to fix.
- **Griffin & Otkin 2017 [78]** (JAMC): MODE/GOES verification shows HRRR has too many small cloud objects at initialization (especially August), transitioning to too few oversized objects by FH2. This is a documented "cloud spin-up" problem in the first 1–2 forecast hours.
- **Min et al. 2021 [87]** (JGR-Atmos): HRRR overcast/thick-cloud conditions during warm season are the main driver of positive SW↓ and warm-temperature biases.
- **Skinner et al. 2021 [79]** (Wea. Forecasting, 1,400-forecast sample): HRRR overforecasts convective storm objects over the southern and eastern US, **most pronounced in southeastern US**.
- **NSSL EWP 2024 [90]** (operational note): HRRR delays afternoon convective initiation by 1–2 hours in the Southeast (e.g., 17Z HRRR waits until 23Z vs observed 21–22 Z).

For an SE US astrophotography app, the practical implication is that HRRR may underforecast cloud cover during summer convective afternoons/evenings — clearing the sky too aggressively in the 1–12 h outlook after afternoon storms.

### GFS Arakawa-Schubert convective bias
- **WPC operational notes [174]**: Arakawa-Schubert is "very susceptible to grid scale convective blow-ups" in moist/unstable air; warm-season QPF bias ~1.6 (overforecast); peak convection forecast too early (15Z / 11 AM local).
- **Patel et al. 2021 [88]** (GRL): GFS at 25% sky cover shows 1°C warm bias at night and 2°C cold bias during the day — implicates GFS cloud-timing errors.

### ECMWF IFS Cycle 47r3 cloud regression
- ECMWF's own documentation [29], [30] confirms Cycle 47r3 (October 2021) introduced a **+3–4% global mean cloud cover increase, up to +15% locally** — a documented regression. ECMWF acknowledged this as needing a future cycle to fix.

### AI model cloud limitations
- **Bonavita 2024 [45]** (GRL): Pangu-Weather, FourCastNet, GraphCast all heavily damp spectral modes above wavenumber ~60 at 12–24 h; physically inconsistent at small scales.
- **Olivetti & Messori 2024 [46]** (GMD): GraphCast and Pangu-Weather "blur" toward climatology at longer leads; underestimate 99th-percentile precipitation by 20–35% (vs HRES 10–15%).
- **AIFS distribution flaw [32]**, [171]: AIFS Single v1 produces flat cloud cover distribution vs observed U-shaped distribution; under-predicts both clear-sky and overcast extremes — attributed to MSE training as "an inherent limitation."
- **Solcast 2025 industry analysis [33]**: AIFS irradiance bias −8% vs IFS +2% vs GFS +5%, implying AIFS systematically over-predicts cloud opacity.

### NWP cloud parameterization at peak performance
- **BAMS DoD Workshop 2024 [169]**: emerging expert consensus that NWP microphysical schemes have "reached peak performance at two moments"; subgrid cloud fraction estimation via RH thresholds fundamentally inadequate.
- **Lamb 2026 [172]** (JAMES): double-moment microphysics shows "systematic biases persist" with "relatively minimal benefit" from further sophistication.
- **WeatherReal benchmark [173]**: total cloud cover has the **highest RMSE of any surface variable** evaluated across all NWP/AI models.

## Persistence vs NWP for cloud cover
**Ye & Chen 2013 [82]** (MNRAS, the only peer-reviewed evaluation targeting astronomy use): "the persistence model is best of all for τ < 6 h" for GFS cloud cover comparison. GFS detects fewer than half of convective cloud events globally (~45%). Persistence beats NWP at horizons under 6 hours — meaning a forecast app should use observed satellite/ground-truth conditions for the next ~6 hours rather than NWP cloud cover.

**Haiden et al. 2015 [86]** (ECMWF Newsletter 143): ECMWF HRES cloud cover skill drops below persistence at approximately day 3 — earlier than skill loss for temperature, geopotential, wind, or precipitation.

## Dominance regime by use case

| Lead time | Best signal | Why |
|---|---|---|
| 0–3 h | Satellite nowcast (GOES ABI ACM) | Observed cloud, 5-min cadence; persistence/optical-flow extrapolation [95], [149], [152] |
| 3–6 h | HRRR (CONUS) — but persistence still competitive [82] | 3 km, hourly cycles; cloud spin-up issue at FH0–2 [78] |
| 6–18 h | HRRR (preferred for SE US convective specifics, with caveats) | Convection-allowing; HRRR overforecasts convective objects in SE US per [79] |
| 18–48 h | HRRR Extended (00/06/12/18 Z) or NAM | HRRR Extended at 00/06/12/18 Z; NAM 12 km / 3 km nests |
| 2–5 days | ECMWF IFS HRES | Highest medium-range skill [86] |
| 5–10 days | ECMWF IFS or ENS | Skill drops sharply; ensembles preferred for go/no-go probability |
| 10+ days | GFS or extended ENS | Extended-range only; cloud skill near climatology |

## Gaps and limitations

- HRRR vertical level count was not directly confirmed (rapidrefresh.noaa.gov returned 403 [22]). The AMS 2022 system paper [21] is the authoritative reference.
- RAP cadence: Wikipedia states "every 3 hours" but NCEI and rapidrefresh.noaa.gov state hourly. The conflict may reflect RUC vs RAP version transitions; current operational behavior is not unambiguously documented in accessible sources.
- ECMWF AIFS forecast horizon was not explicitly stated in fetched ECMWF news pages [31].
- GFS and NAM detailed cloud-layer GRIB inventories were not directly fetched in this research; LCDC/MCDC/HCDC presence is inferred from standard NCEP GRIB2 Table 4.2-0-6 conventions and from confirmation in HRRR/RAP inventories.
- RRFS cloud-cover variable list and operational date are not yet documented in accessible sources [47], [48].
- No SE-US-specific peer-reviewed verification study was found for ECMWF or for GFS cloud cover. The northern Alabama HRRRv2 study [80] is the geographically closest direct evaluation; full text was not fetched in-session.
