# General aerosols and PM2.5

**Dimension scope:** programmatic data sources for ambient aerosol/PM2.5
concentrations in the US and globally — coverage, refresh cadence, sensor
types (regulatory FRM/FEM vs. low-cost), license terms, and the practical
limitations of each for an astrophotography planning app.

See [citations.md](../citations.md) for full source details.

## API matrix

| Source | Sensor type | Coverage | Refresh | Auth | License | Notes |
|---|---|---|---|---|---|---|
| **AirNow API** [23, 24] | FRM/FEM regulatory | US, CA, MX | Hourly | Free key | US gov, public | 2,500+ stations; bbox query; rate limit ~500 req/hr per discovery [23] |
| **EPA AQS Data Mart** [27] | FRM/FEM regulatory | US | **6+ month lag** | Free key | US gov, public | Not real-time; PM2.5 FRM = parameter code 88101; row cap 2M; 10 req/min suggested |
| **OpenAQ v3** [26] | Mixed (regulatory + low-cost) | Global | Variable | X-API-Key | Per-location (often US Public Domain) | Pass-through, no QA/QC at ingestion (per discovery agent) |
| **PurpleAir API** [28] | Plantower PMS5003 (low-cost) | Dense in US/EU | ~2-min real-time | Free key | Points-based pricing (~$0.01/sensor/day at 10-min poll) | A/B channel agreement is QC; needs Barkjohn correction [18] |
| **EEA Air Quality Service** [32] | EU regulatory | EU members | E2a NRT, E1a annual verified | Free | EU public | Parquet format |
| **WAQI (aqicn.org)** [29] | Aggregated regulatory | 11,000+ stations global | Hourly | Free token | **NON-COMMERCIAL only** | License blocker for paid app |
| **IQAir AirVisual** [30] | Mixed | Global | Hourly | Free key (limited) / paid | **Default ToS = personal/non-commercial only** | Raw PM2.5 behind paid tier |
| **Sensor.Community** (Luftdaten) [31] | Plantower SDS011/PMS5003 (low-cost) | Europe-heavy, sparse US | ~5-min | None (User-Agent required) | Open | No correction applied at source |
| **CAMS PM2.5 (model)** [33] | Reanalysis + 5-day forecast | Global | Twice daily NRT | CDS API | Free, CC-BY | ~40 km — too coarse for urban resolution |
| **NASA LANCE VIIRS NRT AOD** [from Dim4 Discovery] | Satellite (column AOD) | Global | <3 hr from overpass | Free Earthdata login | Free | Column AOD, not surface PM2.5 |
| **NASA SEDAC global PM2.5 grids** [from Dim4 Discovery] | Satellite-derived | Global | Annual (1998–2022) | Free Earthdata login | Free | Long-term climate baseline only |

## Tier ranking for an astrophotography planning app

**Tier 1 (regulatory, authoritative):**

- AirNow [23] — primary US/CA/MX choice. Hourly; FRM/FEM only.
- EPA AQS [27] — 6+ month lag → use only for historical baselines.
- EEA [32] — EU equivalent for v2 international.

**Tier 2 (aggregated, mixed quality):**

- OpenAQ [26] — global cover; mixes Tier 1 and low-cost; user must filter.
- WAQI [29] — broad coverage but non-commercial license blocker.

**Tier 3 (low-cost, dense, requires correction):**

- PurpleAir [28] — apply Barkjohn EPA correction [18]; aware of dust failure
  [19].
- Sensor.Community [31] — open but no correction.

## The PurpleAir EPA correction

Verified equation [18]:

```
PM2.5_corrected = 0.524 × PA_cf_1 − 0.0862 × RH + 5.75
```

where `PA_cf_1` is the CF=1 channel-averaged PurpleAir reading and `RH` is
relative humidity in percent. Reduces RMSE from 8 µg/m³ to 3 µg/m³.

**Important calibration scope** [18]:

- 50 sensors, 16 states, 39 sites — geographic gaps in southern South,
  Northern Rockies, Ohio Valley.
- Only 3 rural sites in calibration set.
- Validity at high concentration (>60 µg/m³) and low temperature (<−12 °C) is
  uncertain.

**Critical aerosol-type-specific failure** [19]: corrected PurpleAir data
are accurate in smoke (slope 0.99 at Keeler CA) and urban (slope 1.00) but
**too low by factor 5–6 in dust** (slope 5.6 at Keeler CA). An app applying
this correction uniformly during a Saharan dust event will display PM2.5
~1/5 of the actual surface concentration.

For wildfire smoke at extreme concentrations [22]: only 5 of 15 smoke-impacted
sites met EPA performance targets at hourly averages. Above 300 µg/m³, the
standard equation underestimates by ~20%; a piecewise quadratic correction
introduces a different positive bias at 150–300 µg/m³.

## Plantower PMS5003 hardware revision

A silent hardware change to the PMS5003 board around June 2021 [20]:

- Reduces >0.3 µm particle counts by a factor of ~3
- Introduces a systematic low bias of ~3 µg/m³ for concentrations <16 µg/m³
- Affects more than 10% of the PurpleAir outdoor network without per-sensor
  notification

For astrophotography (where the difference between "excellent" and "good"
transparency lives in the 5–15 µg/m³ band), this is the wrong place to have
a 3 µg/m³ cohort-level bias.

## Surface PM2.5 ≠ column AOD

This is the central caveat for astrophotography use of PM2.5 data. The
PM2.5/AOD relationship is fundamentally **decoupled** [11]:

- Daily PM2.5/AOD R = **0.03 to 0.60** across 19 stations in China [11].
- The decoupling driver is hygroscopic growth: specific humidity from
  2.83 g/kg (low AOD, high PM2.5 cases) to 11.89 g/kg (high AOD, low PM2.5
  cases) [11].

Predictive performance for PM2.5 from AOD [11]:

- AOD alone: R = 0.49
- AOD + specific humidity: R = 0.74
- AOD + four meteorological factors: R = 0.81

**Above the boundary layer, surface PM2.5 stops predicting column AOD
entirely** [16]: R² = 0.29–0.54 for aerosol below 1.3 km, but R² = 0.03–0.21
above 1.3 km. **58% of aerosol scale-height measurements** placed mass above
1.35 km [16].

**Diurnal asymmetry** [13]: nighttime AOD below 1 km is 58.5% larger than
daytime in eastern China models, driven almost entirely by hygroscopic
growth — daytime surface monitors are essentially measuring a different
physical quantity than nighttime column aerosol.

**Boundary layer collapse at sunset** [15]: concentrates the same aerosol
mass into a shallower slab, spiking surface PM2.5 without changing column
AOD. An app ingesting real-time PM2.5 at 20:00 local time will see elevated
readings that reflect mixing-layer compression rather than increased
atmospheric loading.

## OpenAQ data quality

Per OpenAQ documentation [26]: data shared "without modification (other than
standardizing format)" from a mix of regulatory monitors and low-cost
sensors. **No QA/QC applied by OpenAQ at ingestion.** Attribution metadata
(`entity`, `instrument`) fields exist but are inconsistently populated.

A 2025 PMC study [from Dim8 Counter] documented an OpenAQ EEA adapter bug
where stale `value_datetime_inserted` caused the fetcher to discard most
hourly readings, reducing German/Estonian station coverage from hourly to
~2 points/day. Infrastructure-level data loss is a real risk.

## License gotchas

- **WAQI**: data "cannot be sold or included in sold packages" [29]. Hard
  blocker for any commercial app distributing AQ values.
- **IQAir / AirVisual**: default ToS is "personal, non-commercial use only"
  for the free Community tier [30]. Raw PM2.5 concentration requires paid
  Startup or Enterprise tier.
- **OpenAQ**: per-location licenses [26]. US Public Domain in many cases,
  but other providers may impose attribution or commercial-use restrictions
  that propagate downstream.

## Recommended fetch architecture

For a SE US astrophotography app:

1. **Primary surface PM2.5**: AirNow [23] — regulatory, free, real-time.
2. **Spatial fill where AirNow is sparse**: PurpleAir [28] with Barkjohn
   correction [18], **flagged as "may be 5× low during dust events"** [19].
3. **Column AOD (the actually relevant variable for transparency)**: AERONET
   [73] for nearest-station ground truth; CAMS [33] or VIIRS NRT for
   gridded column data.
4. **Cross-source disagreement surfaced to user** rather than averaged away
   (see [source-conflict-resolution.md](source-conflict-resolution.md)).
5. **PurpleAir A/B agreement** as a sensor-level confidence flag.
6. **For v2 EU coverage**: EEA service [32] (regulatory) + Sensor.Community
   [31] (low-cost spatial fill).

## Gaps and limitations

- The OpenAQ rate limits (60/min, 2000/hr per discovery agent) and pass-through
  ingestion behavior need separate verification from the rate-limits and
  terms subpages — only the quick-start was directly fetched in this run [26].
- AirNow's exact bbox endpoint URL pattern and rate limit specifics were not
  exposed on the landing page fetched [23] — discovery agent reported these
  but they need separate verification.
- WAQI's commercial-use language is from a search snippet, not a directly
  quoted ToS — the legal precise wording could not be retrieved.
- No source examined provides a vetted "PM2.5 + RH + altitude → column AOD"
  conversion algorithm suitable for production deployment. The Petržala &
  Kocifaj 2026 model [9] is the most relevant but was not directly fetched
  for full method.
