# Volcanic and stratospheric haze events

**Dimension scope:** programmatic data sources for volcanic SO₂ injection,
stratospheric aerosol loading, and pyroCb (pyrocumulonimbus) smoke injection
into the lower stratosphere — long-tail but real for global users, with
multi-year persistence after major events.

See [citations.md](../citations.md) for full source details.

## When does this dimension matter

Stratospheric aerosol effects on amateur astrophotography are episodic and
threshold-bound. Per Stothers 2001 [91]: stellar photometric uncertainty for
SAOD is ±0.017 — events with global SAOD below ~0.02 are at or below the
detection floor of the very technique used to measure them via starlight.

**Practically**: only **VEI ≥ 5–6 eruptions** produce globally averaged
SAOD large enough to matter. Pinatubo (1991) reached 0.10–0.15 globally
[86]; Hunga Tonga (2022) was the largest perturbation since Pinatubo but
hemispherically asymmetric (SH-concentrated) [from Dim9 Counter, citing
Nature Comms ESS 2025].

**Most of the time, this dimension is "off" for the app** — but when active,
it persists for 1–3 years.

## Hunga Tonga (January 2022) as the recent canonical case

Hunga Tonga–Hunga Haʻapai injected ~0.4–0.5 Tg SO₂ (35–50× less than Pinatubo)
but **~146 Tg of water vapor** (+5% global stratospheric H₂O) [87]. Water
vapor accelerated aerosol formation 3× faster than typical [88]; particles
were ~2× larger than typical volcanic [90].

Direct astronomical evidence: ESO Messenger 190 (Mar 2023) [89] reports
VLT/Paranal twilight calibration showed sky brightness changes that persisted
>12 months — sky had not returned to pre-eruption state one year later. **This
citation is INACCESSIBLE in our re-fetch (PDF parse failed, archive page 403)
— relying on Dim9 Discovery agent extraction.**

Counter-perspective [from Dim9 Counter]: Hunga Tonga's effect was largely
confined to the Southern Hemisphere; Northern Hemisphere observers were
minimally affected. Globally averaged SAOD ~2× the 2015 Calbuco event but
still 5–10× smaller than Pinatubo's peak.

## Pinatubo (June 1991) as the calibration anchor

Per the USGS Self et al. chapter [86, verified]:

- SO₂ injection: ~17 Mt (TOMS 20 ± 6 Mt; other estimates 13.5–17 Mt).
- Globally averaged stratospheric AOD: **0.1–0.15 for 2 years**.
- Peak local: **0.4** in late 1992.
- 3-year persistence above background.
- Visual effects in Hawaii late 1991–early 1993: "unusual colored sunrises
  and sunsets, crepuscular rays, and a hazy, whitish appearance of the sun."

**No quantitative astronomical magnitude data** in the USGS chapter.
Calculated implication (est.):

- Global avg AOD 0.12 → +0.13 mag/airmass V-band at zenith.
- Local peak AOD 0.4 → +0.43 mag/airmass at zenith; +0.86 at airmass 2.

This is the upper bound of what amateur astrophotographers experienced from
a major eruption and informs the upper anchor of the app's stratospheric
severity scale.

## Pyrocumulonimbus (pyroCb) smoke into the stratosphere

Distinct from tropospheric wildfire smoke, pyroCb events inject smoke into
the lower stratosphere where it persists for months. Per Dim9 Discovery
extraction:

- Australian Black Summer pyroCb super-outbreak (Dec 2019–Jan 2020): ~1 Tg
  smoke into stratosphere — largest pyroCb stratospheric injection on record
  [npj Climate Atmos Sci 2021, citation in Dim9 Discovery].
- 2017 British Columbia pyroCb: ~0.3 Tg; persisted 8–10 months in lower
  stratosphere with ~178-day e-folding time [ACP 2021, citation in Dim9
  Discovery].
- pyroCb account for **10–25% of present-day lower-stratospheric black
  carbon and organic aerosol** [Science (Fromm et al.), citation in Dim9
  Discovery].

**For astrophotography**: pyroCb smoke increases sky absorption (black
carbon component) without producing the characteristic volcanic twilight
purple/red enhancement. Rare but real source of multi-month transparency
degradation.

## Data product matrix

| Product | Type | Coverage | Resolution | Access | Cost |
|---|---|---|---|---|---|
| **Sentinel-5P TROPOMI SO₂** [99] | Satellite L2 swath | Global | 13 × 24 km nadir, daily | Copernicus Data Space (OData/OpenSearch) + AWS Open Data S3 | Free |
| **OMI/Aura OMSO2** [from Dim9 Discovery] | Satellite L2/L3 | Global | 13 × 24 km, since Oct 2004 | NASA GES DISC, Earthdata Login | Free |
| **SAGE III/ISS** [from Dim9 Discovery] | Stratospheric aerosol extinction | ±70° latitude (ISS orbit) | Multi-wavelength (449–1021 nm), occultation | NASA ASDC | Free |
| **CALIPSO L3 stratospheric APro** [from Dim9 Discovery] | Lidar archive | Global | 532 nm backscatter, monthly | NASA ASDC | Free; mission ended Aug 2023 |
| **GloSSAC v2.23** [98] | Merged climatology | Global | 10° lat bins, 8.5–39.5 km | NASA ASDC | Free; canonical 1979–Dec 2024 record |
| **CAMS** [33] | Forecast (assimilates GOME-2 + TROPOMI SO₂) | Global | 5-day, ~40 km | CDS API | Free, CC-BY |
| **NOAA HYSPLIT volcanic ash** [from Dim9 Discovery] | Trajectory/dispersion | Global | Variable | READY Web API (250 calls/day with key) | Free |
| **USGS HANS volcano API** [97] | Alert level + color code | US volcanoes | Per-volcano | JSON REST | Free, no SLA |
| **Smithsonian GVP weekly** [from Dim9 Discovery] | Eruption summaries | Global | Weekly narrative | WFS GeoJSON / Excel / Google Earth KML | Free |
| **London VAAC QVA API** [96] | Quantitative volcanic ash forecast | Global (London VAAC sector) | Gridded across 12 altitude slices | Met Office QVA API | Free with registration |
| **Other VAACs (8 of 9)** | Aviation advisories (text/PDF) | Per-region | None standard | Web pages | Free; text only |
| **IVHHN Vog Dashboard** [94] | Real-time SO₂ + PM2.5 | Hawaii stations | 15-min SO₂, hourly PM2.5 | Web dashboard | Free; no documented REST API |
| **VMAP Hawaii** [95] | Vog forecast | HI statewide / Big Island | 3 km / 1 km, WRF + NAM NEST | Web dashboard | Free; no API |

## VAAC mandate vs astrophotography use

[from Dim9 Counter] VAACs are aviation-operational. Products express ash in
flight levels (FL), geographic polygons relevant to engine ingestion risk,
and dispersion forecasts for rerouting — **not** surface optical depth or
photometric extinction. Using raw VAAC text products as a transparency
signal generates noise (frequent low-altitude advisories for small eruptions
with no stratospheric component) with little useful signal for ground
observers.

The London VAAC QVA API [96] (launched July 2025) is the first VAAC with
gridded ash concentration data accessible via REST. Toulouse co-launched
QVA in November 2025 but no public REST API confirmed.

## Mauna Kea VOG (counter-finding worth noting)

[from Dim9 Counter, citing CFHT manual [93] and IVHHN [94]]: VOG ceiling
under trade-wind conditions caps at ~4,500 ft. **Mauna Kea summit at 13,796
ft is structurally above the VOG layer.** The CFHT documentation explicitly
states the trade inversion "isolates the upper atmosphere from lower moist
maritime air."

VOG only affects Mauna Kea telescopes during anomalous Kona wind events
(southerly flow that breaks the inversion).

For the app: a Hawaii-based user at coastal/mid-altitude is affected by VOG;
a user planning a remote session at Mauna Kea/Hualālai elevations is
typically not.

## Background stratospheric layer is not constant

[from Dim9 Counter, citing Solomon et al. 2011 [92]]: the background "Junge"
stratospheric aerosol layer is "persistently variable" even absent major
eruptions, driven by small volcanic degassing, pyroCb smoke injections, and
seasonal OCS oxidation. This variability (~0.005–0.02 SAOD) is at the same
scale as the signal from minor eruptions.

**Implication**: the "event-vs-baseline" framing breaks down for anything
short of a major eruption. What looks like an event signal may simply be
natural background variability. The app should not treat every TROPOMI SO₂
detection as an event.

## TROPOMI SO₂ data quality caveats

[from Dim9 Counter]: the standard operational DOAS SO₂ retrieval has elevated
noise vs the COBRA algorithm (factor-of-4 improvement). High solar zenith
angle pixels are flagged as potential false positives (flag value 4).
Detection limit ~8 kt/yr means many continuous-degassing volcanoes appear
as low-level "events" even when emissions are geologically routine.

**Interpreting raw TROPOMI SO₂ maps without column-altitude context** (is
this in the troposphere or stratosphere?) makes them unreliable for
stratospheric transparency prediction.

## Recommended app decision logic

This dimension should run as a **background advisory layer**, not a
per-night planning input most of the time:

1. **Quarterly check** of GloSSAC [98] / SAGE III [from Dim9 Discovery]
   anomalies vs baseline. If global SAOD > 0.02 above background, surface
   a "stratospheric haze active" advisory.
2. **Monitor Smithsonian GVP weekly reports** [from Dim9 Discovery] for new
   VEI ≥ 5 eruptions.
3. **For Hawaii-located users**: integrate IVHHN Vog Dashboard [94] and
   VMAP [95] for daily VOG conditions, with altitude-aware logic (Mauna
   Kea summit users mostly unaffected per [93]).
4. **For all users during active stratospheric events**: add a tooltip/info
   note on the main forecast indicating "expect ~0.05–0.15 mag/airmass
   additional extinction from background stratospheric haze" (calculated
   from current GloSSAC value, est.).

**Do not** integrate raw VAAC text or TROPOMI SO₂ maps as direct user
signals — they introduce more noise than signal for ground observers.

## Gaps and limitations

- **ESO Messenger 190 PDF was inaccessible** for in-session re-verification
  [89]. The most directly relevant astronomical evidence for Hunga Tonga
  (Paranal twilight calibration changes, sky-brightness recovery timeline)
  rests on Dim9 Discovery agent extraction only.
- **No peer-reviewed paper found** quantifying Pinatubo or Hunga Tonga's
  effect in standard photometric magnitudes (B/V/R band extinction increase)
  for amateur imaging conditions. Direct evidence is observatory-tier.
- **OMI operational status as of April 2026** is not confirmed in this
  research (Aura launched 2004, design life 6 years).
- **CALIPSO product availability**: discovery agent noted some products
  pulled from public access at AERIS/ICARE; current ASDC holdings not
  enumerated.
- **VMAP/IVHHN have no documented REST API** [94, 95] — programmatic
  Hawaii-VOG ingestion requires HTML scraping.
- **8 of 9 VAACs** lack documented REST APIs; programmatic access is text/PDF
  parsing only.
