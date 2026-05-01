# Pollen data sources

**Dimension scope:** which APIs and authoritative data sources expose pollen
counts and forecasts that an astrophotography planning app could ingest, with
what coverage, granularity, refresh cadence, and license terms. Special
attention to North Carolina pine pollen, which is the visible yellow-film
species that physically contaminates optics.

See [citations.md](../citations.md) for full source details.

## Programmatic API matrix

| Provider | Coverage | Species granularity | Forecast horizon | Free tier | License model |
|---|---|---|---|---|---|
| **Google Pollen API** [35] | 80 countries; full tree+grass+weed in US/EU/CA/AU; grass-only in 13 countries | Genus level (pine = single bucket, no Pinus species split) | 5-day daily | $200/mo credit (per [36], expired Feb 28 2025 — verify) | Pay-as-you-go, $10 CPM (Maps Platform pricing) [36] |
| **Ambee** [37, 38] | 150+ countries (vendor claim); validated mostly Northern Hemisphere [38] | Genus level for NA; "speciesRisk" param for some regions but not NA | 48 h or 120 h | 100 records/day | Tiered, paid above free; sales contact required |
| **Tomorrow.io Pollen Premium** [40] | US + global (claimed) | Behind sales wall, not publicly documented | Unknown | None (premium tier) | Enterprise contract |
| **Atmospore** [39] | Global (claimed); newer/smaller provider | Genus level | 7–14 day | 14-day trial | €9 / €39 / €149 per month |
| **Open-Meteo Air Quality** [45] | **Europe only** for pollen (alder, birch, grass, mugwort, olive, ragweed) | Species | 4-day | Yes (non-commercial) | Free; commercial requires paid plan |
| **CAMS Pollen** [46] | **Europe only** (6 species) | Species | 4-day | Yes (free with CDS API) | CC-BY |
| **SILAM (FMI)** [47] | Europe / N. Europe / SE Asia (no NA) | Species | 5-day | Yes (open code on GitHub) | Open-source |

**For North Carolina, the practical choice is Google Pollen API or Ambee.** Both
provide pine as a category but neither distinguishes *Pinus taeda* (the visible
yellow-film species) from other pines [35, 37].

## Authoritative ground-truth networks

- **NC DEQ pollen monitoring** [41]: a single station at 4403 Reedy Creek Road,
  Raleigh. Operates late February through mid-November, Monday–Friday, sampling
  the previous 24 hours (9 a.m. → 9 a.m.). Reports tree/grass/weed totals.
  No machine-readable API; the live HTML report at
  `xapps.ncdenr.org/aq/ambient/Pollen.jsp` is scrapeable but no published
  programmatic-access terms exist [41].
- **AAAAI National Allergy Bureau (NAB)** [44]: ~85 US stations using Burkard
  volumetric traps. **No public API** — formal data-release request required.
- **NASA Pollen / aerobiology research**: foundational only; no operational API.

## NC-specific pine pollen prediction (no API needed)

NC State Extension publishes a deterministic growing-degree-day (GDD) model for
pine pollen [42]:

- **Onset:** ≈300 GDD (Boyer 1978)
- **Peak:** ≈636 GDD (Baker & Langdon 1990)
- **Base temperature:** 55 °F
- **Accumulation start date:** February 1

This is implementable from any weather API providing daily max temperatures.
Predictive of the season *envelope* for SE-US pine pollen, not day-to-day grain
counts. No published uncertainty range — qualitative "approximately" only [42].

## Optical relevance vs allergen relevance

Pine pollen is **the visible yellow-film species** that coats outdoor surfaces
during NC spring [43]. It is **not the dominant allergen** — oak, birch, and
grass dominate the allergen burden [43]. This split matters for the app:

- An equipment-protection alert needs to weight pine pollen heavily, even when
  total pollen counts are moderate.
- An allergen-driven ranking (which is what most consumer apps optimize for)
  will under-weight the species that actually contaminates corrector plates.

## Forecast accuracy: a documented problem

Multiple peer-reviewed studies converge on poor consumer-app pollen forecast
accuracy:

- 2025 PMC study comparing AccuWeather and The Weather Channel apps to
  automated pollen counters [48]: AccuWeather concordance 7% for grass, 33%
  for ragweed, 56% for mold. The Weather Channel: 29% grass, 34% ragweed.
  **No statistically significant association** in Fisher exact tests [48].
- 2017 European 9-app validation [49]: best app 62.9% exact-hit rate; worst
  <40%. Authors call for mandatory quality control.
- 2024 Healio survey [105]: low accuracy of public pollen websites vs NAB
  predictions across 5 US cities.

The root causes [42, 44, 48]: sparse Hirst/Burkard manual counter networks,
3–9 day reporting lag, and model corrections that decay within hours of
assimilation. Fusing multiple poor forecasts (Google + Ambee + Tomorrow.io)
does not recover accuracy — it averages noise.

## Counter-perspective: pollen and astrophotography transparency

The atmospheric column-transparency impact of pollen is real but **strictly
daytime** [51]. Lidar studies (Noh et al. 2013) show pollen aloft can account
for 25–97% of aerosol optical depth during spring daytime peak emission, but
the column collapses after ~18:00 local time [51].

However, the pollen-settles-overnight assumption is species-dependent and
partially false [52]: ragweed nighttime ground-level concentrations exceed
daytime by >30%; birch day/night peaks are nearly equal. For pine specifically,
the heavy grain (settling velocity 2.1 cm/s [50]) does fall out overnight more
reliably than ragweed/birch.

**Two distinct risk vectors that consumer apps conflate:**

1. **Atmospheric column transparency loss** (daytime phenomenon, mostly
   irrelevant for night imaging sessions starting after astronomical twilight).
2. **Surface deposition / coating contamination** (cumulative during overnight
   sessions, the primary concern for NC SCT/refractor users). See
   [equipment-protection-thresholds.md](equipment-protection-thresholds.md).

## Gaps and limitations

- **No API distinguishes Pinus taeda from other Pinus.** All examined APIs
  treat pine as a single undifferentiated category. NC DEQ names predominant
  species in free-text but does not quantify them [41].
- **No quantitative pollen-to-AOD or pollen-to-extinction conversion** in any
  source found that maps "X grains/m³ → Y magnitudes of additional extinction
  in V/Ha/OIII." This is an open scientific gap (also flagged in
  [particulates-to-imaging-impact.md](particulates-to-imaging-impact.md)).
- **Tomorrow.io's actual species coverage and pricing** are behind a sales
  wall [40]. The app may be missing a better option without an enterprise
  trial.
- **BreezoMeter standalone API was retired** September 2023 and migrated into
  Google Maps Platform Environment APIs with different pricing [38]. Legacy
  BreezoMeter integrations break.
- **Pollen.com (IQVIA)** is the long-standing reference but has no documented
  public developer API; the third-party `pyiqvia` Python library scrapes it
  with no formal terms.
