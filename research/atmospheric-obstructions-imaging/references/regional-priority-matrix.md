# Regional priority matrix

**Dimension scope:** which atmospheric-obstruction signals matter most by
location and season — guidance for an app that adapts which data sources
it weights by the user's geography and time of year.

This is a synthesis dimension drawing on the data sources surveyed in the
other reference files. See [citations.md](../citations.md) for source details.

## Why regionalize

Generic astro-weather apps treat all atmospheric obstructions identically
(or ignore them). The actual signal-to-noise of each obstruction varies
strongly by region and season:

- **Saharan dust** is a 2-month/year SE US phenomenon (mid-June to
  mid-August) [66]. Showing a "dust" indicator year-round in NC wastes
  visual real estate.
- **Wildfire smoke** is dominant in the western US/Canada from June through
  October but increasingly affects the SE via Canadian boreal-fire long-range
  transport.
- **Pine pollen** is intensely SE-US (and other conifer regions) in late
  March through early May [42, 43]. Outside that window the GDD model [42]
  shows it is not deployment-relevant.
- **Volcanic stratospheric haze** is a global, multi-year phenomenon
  triggered by major eruptions (VEI ≥ 5–6) [86, 91]. Most of the time it is
  inactive.

## Regional priority matrix (by location)

### Southeast US (NC primary, also VA, SC, GA, AL, MS, FL)

| Period | Primary signal | Secondary signal | Tertiary |
|---|---|---|---|
| Late Feb – early May | Pine pollen [42, 43] | Routine PM2.5 [23] | Spring smoke (Pisgah/Nantahala fires) |
| May – early June | Routine PM2.5 [23] | Storm aerosols (transient) | — |
| Mid-June – mid-Aug | **Saharan dust** [66] | Routine PM2.5 [23] | Wildfire smoke (Canadian transport) |
| Mid-Aug – Sept | Wildfire smoke (CA/OR/WA/Canada late season) | Routine PM2.5 | Tropical-storm-stirred dust |
| Oct – Jan | Routine PM2.5 [23] | Cold-front haze (humidity, not aerosol) | — |

The SE US **never sees zero atmospheric obstruction signal**, but the
relative weighting of which APIs to highlight rotates by season.

### Western US (CA, OR, WA, NV, ID, UT, AZ, NM)

| Period | Primary signal | Secondary signal | Tertiary |
|---|---|---|---|
| Year-round | Wildfire smoke (peak Jul–Oct) | Routine PM2.5 [23] | Dust storms (deserts) |
| Spring | Tree pollen (cedar in TX/NM, juniper in UT/AZ) | — | — |
| Summer monsoon (AZ/NM) | Dust + thunderstorm haze | — | — |

**Wildfire smoke is the dominant feature.** HRRR-Smoke COLMD [53] should be
the app's prominent forecast layer.

### Mountain West (CO, MT, WY, alpine sites)

Generally cleaner than SE/W US but episodic:

- Wildfire smoke transport from CA/OR/WA in summer
- Saharan dust occasional during strong outbreaks
- Volcanic stratospheric haze (when active globally)

### EU (for v2 international coverage)

| Period | Primary signal | Secondary | Notes |
|---|---|---|---|
| Spring | Birch/grass pollen (CAMS [46], Open-Meteo [45]) | Routine PM2.5 (EEA [32]) | CAMS pollen is pan-European |
| Summer | Routine PM2.5 + occasional Saharan dust (S. Europe) | Wildfire smoke (Mediterranean) | EEA E2a NRT |
| Winter | Routine PM2.5 (anthropogenic) | — | Heating-season anthropogenic spike |

### Southern Hemisphere (AU, NZ, Chile, S. Africa)

**Significantly under-served by current APIs.**

- Google Pollen API is **grass-only** in Argentina, Brazil, Chile, NZ, S.
  Africa [35].
- Australia: no major US-style PM2.5 network; relies on state-level data.
- AERONET coverage thin; AOD comes from satellite (CAMS, MODIS).
- Wildfire smoke (AU Black Summer 2019–2020 type events) is the dominant
  variable.

The app should explicitly indicate "limited data coverage in this region"
rather than presenting confident but data-thin forecasts.

## Geographic API selection by region

| Region | Pollen | PM2.5 surface | Column AOD / smoke | Dust |
|---|---|---|---|---|
| SE US | Google Pollen [35] or Ambee [37] + NC-State GDD model [42] | AirNow [23] | HRRR-Smoke COLMD [53, 58], CAMS [33] | CAMS dust [68], NOAA AOML SAL hub [66] |
| W US | Google Pollen [35] | AirNow [23] | HRRR-Smoke COLMD [53] | CAMS dust [68] (less relevant) |
| Mountain West | Google Pollen [35] | AirNow [23] (sparse rural) | HRRR-Smoke + AERONET [73] | CAMS dust [68] (occasional) |
| EU | Google Pollen [35] OR CAMS [46] / Open-Meteo [45] | EEA [32] + Sensor.Community [31] | CAMS [33] | CAMS dust [68] |
| SH | Google Pollen [35] (limited; mostly grass-only [35]) | OpenAQ [26] (sparse) | CAMS [33] | CAMS dust [68] |

## Severity-weighting recommendations

Within each region, weight by an **effective transparency loss** estimate
(in mag/airmass at zenith) rather than by raw concentration:

```
ΔV ≈ 1.086 × AOD(550)
```

Map ΔV to a 4-tier severity:

All tier boundaries below are synthesis-judgment estimates (est.), not an
established astronomical convention.

| ΔV | Severity | Display | Imaging recommendation |
|---|---|---|---|
| < 0.05 (est.) | Excellent | green | Full session ok including planetary, broadband, narrowband |
| 0.05 – 0.15 (est.) | Good | yellow-green | Slight extinction; broadband still excellent, narrowband fine |
| 0.15 – 0.40 (est.) | Degraded | orange | Plan shorter exposures or narrowband (less affected at Ha) |
| > 0.40 (est.) | Poor | red | Limited utility for deep-sky imaging; planetary at zenith may still work |

Add a **separate equipment-protection severity** (independent of transparency)
based on pollen count, dust event status, and smoke deposition risk. See
[equipment-protection-thresholds.md](equipment-protection-thresholds.md).

## What "regional priority matrix" means in code

The app should:

1. Determine user's geography (geocoded location).
2. Determine current season (date).
3. From the matrix, identify 2–3 most-relevant atmospheric obstructions.
4. Fetch only those data sources (rather than all 9 dimensions for every
   user, every night).
5. Display the relevant signals prominently; demote currently-irrelevant
   signals to "more details" UI.

This is both a UX recommendation (less clutter for the user) and an
operational efficiency one (fewer API calls per user-night).

## Gaps and limitations

- The seasonal windows above are typical-year approximations. Climate
  variability means dates shift. The Spring 2024 NC pine pollen peak (April
  1, 5,219 grains/m³) was earlier than typical [from Dim6 Discovery via NC
  State Climate Office reporting].
- The severity-weighting tiers (ΔV bands) are a synthesis judgment from this
  research. They are **not** an established astronomical convention — no
  published source uses exactly these cuts.
- Southern Hemisphere data coverage limitations make the app substantially
  less useful for users below 0° latitude. There is no good fix until more
  regional networks become accessible.
