# Atmospheric Obstructions for Astrophotography

A planning-app-builder's guide to forecasting non-cloud atmospheric
obstructions (pollen, wildfire smoke, Saharan dust, general aerosols) and
deciding both whether the night is worth imaging and whether deploying
expensive optics is safe.

**Audience**: developers building astrophotography planning apps. Primary
geography: Southeast US (especially North Carolina). Global parity for v2.

**Methodology**: per the cited-research skill — every claim traces to a
URL visited in-session; two independent review agents audit the output;
where in-session re-verification was not possible, the source is flagged.

See [README.md](README.md) for the decision-aid summary;
[citations.md](citations.md) for the numbered source list; the
[references/](references/) directory for per-dimension deep-dives.

---

## The honest framing

The standard astrophotography weather forecast has a blind spot. Cloud
cover, seeing, and dew point are well covered by tools like Astrospheric
[58] and Clear Outside. Particulate atmospheric obstructions —
**pollen, wildfire smoke, Saharan dust, urban aerosols, volcanic
stratospheric haze** — are inconsistently surfaced.

For a NC astrophotographer, this matters. Pine pollen at 5,000+ grains/m³
can ruin a corrector plate with no rain in sight [76, 80]. Saharan dust
between mid-June and mid-August reduces transparency without registering
on any cloud forecast [66]. Western wildfire smoke transports across the
continent and persists when surface PM2.5 monitors say "Good."

Three biases that the planning app should resist:

1. **PM2.5 ≠ transparency.** Surface PM2.5 monitors measure what people
   breathe. Astrophotography cares about column AOD — what starlight
   passes through. The two correlate poorly across stations (R = 0.03–0.60
   in 19 China stations [11]) and **decouple completely above 1.3 km**
   (R² collapses from 0.29–0.54 below to 0.03–0.21 above) [16].
2. **Equipment protection is not the same question as data quality.** A
   night with mediocre transparency and high pollen is materially worse
   than a night with mediocre transparency and clean air, because the
   equipment-protection cost is real and asymmetric (cleaning risks
   scratching coatings).
3. **Source disagreement is information, not noise.** When AirNow and
   PurpleAir diverge by 3× on the same NC night, the right answer is
   often to surface the disagreement, not average it away [101, 104].

---

## Coverage and tradeoff matrix

For the SE US use case, here is what each major data source provides and
what it costs the developer to integrate. Quality tiers and license terms
abbreviated; full details in the per-dimension reference files.

### Pollen

| API | Coverage | Pine specificity | Free tier | Pros | Cons |
|---|---|---|---|---|---|
| **Google Pollen** [35] | 80 countries | Genus only (no Pinus species) | $200 monthly credit historically (verify [36]) | High-quality docs, Maps Platform integration, 1 km² | No subspecies; pricing cliff above free tier; [48] consumer apps low concordance with truth |
| **Ambee** [37] | 150+ countries (claimed) | Genus only | 100 records/day | Hourly resolution, 7-yr historical | Pricing opaque; vendor-self-reported "93%" accuracy unverified |
| **Tomorrow.io Premium** [40] | US + global | Behind sales wall | None | Possibly more granular | Documentation gated; no public docs |
| **NC State GDD model** [42] | NC pine specifically | **Yes — Pinus taeda season envelope** | Free (DIY) | Deterministic, peer-reviewed | Manual implementation; predicts season window only |

**Recommendation for NC**: Google Pollen API [35] for daily forecast +
NC State GDD model [42] for season-envelope context. Surface pine pollen
risk separately from total pollen risk for equipment-protection decisions.

### Wildfire smoke (column-integrated, the relevant variable)

| API | Coverage | Forecast | Cost | Notes |
|---|---|---|---|---|
| **HRRR-Smoke COLMD** [53] | CONUS + AK | 18 h std, 48 h ext | Free | Column-integrated mass density — matches transparency need |
| **NOAA HMS smoke polygons** [55] | North America | None (current state) | Free | Analyst-drawn from satellite, daily |
| **NASA FIRMS** [56] | Global | None (active fires) | Free, 5000 tx/10 min | Upstream input, not smoke transport |
| **CAMS Global Composition** [33] | Global | 5-day | Free, CDS API | ~40 km, useful for international v2 |
| **Astrospheric** [58] | (their app) | Per-app | Per-Astrospheric license | Already addresses column-vs-surface in their UI |

**Forecast skill caveat** [59]: 12 operational smoke models all
underpredicted AOD during the Williams Flats fire (NMB −87.4% to −4.3%;
spatial r ≤ 0.50). Camp Fire HRRR-Smoke evaluation showed up to **70%
PM2.5 underprediction** during smoke-on-smoke satellite blindness [61].
**Display forecast uncertainty rather than a single deterministic
number.**

**Nighttime gap**: GOES visible-band smoke detection requires solar or
lunar illumination [60]. At night, smoke is "not present at all in the
infrared imagery" unless extraordinarily thick. **HRRR-Smoke updates
slow at night.**

### Saharan dust

| Source | Type | Cadence | Cost | Notes |
|---|---|---|---|---|
| **CAMS dust AOD** [68] | Forecast | Twice daily, 5 day, ~40 km | Free, CC-BY | Variable `composition_duaod550`; the practical primary source |
| **CAMS via Open-Meteo** [45] | Wrapped CAMS | Free no-key | Free non-commercial | Easier integration; reduced resolution |
| **NOAA AOML SAL hub** [66] | Visualization | Real-time imagery | Free | Best for "is the SAL active?" UI cue |
| **AERONET** [73] | Ground truth | ~15 min, station-level | Free | Sparse stations; nearest in MD/VA/FL for NC users |
| **Barcelona DRC MONARCH** [70] | Forecast (regional) | 72 h, restricted | Public data >2 days old; NRT institutional only | Embargo blocks hobbyist app use |
| **NRL ICAP-MME** [72] | Multi-model | 6-hr to 120-hr | Visualization free; programmatic unclear | 9-model ensemble |

**Window**: SE-US dust transport is tightly seasonal (mid-June through
mid-August peak; outbreaks every 3–5 days in season) [66]. Off-season,
the dust pipeline can be turned off in the app's UI.

**Surface vs column caveat** [3, 66]: SAL base sits ~1 mi above surface and
the layer is 2–2.5 mi thick; 20% of dust outbreaks reach observatory
altitudes [3]. CAMS dust AOD forecasts column loading; ground-based
observers may see it as visible sky reddening before any surface PM2.5
increase.

### General aerosols / PM2.5 (for surface AQ, not transparency)

| API | Type | Free tier | Commercial use | Notes |
|---|---|---|---|---|
| **AirNow** [23] | Regulatory | Free public | Yes | 2,500+ US/CA/MX stations; primary for North America |
| **EPA AQS** [27] | Regulatory archive | Free | Yes | **6+ month lag** — historical only |
| **OpenAQ v3** [26] | Aggregator | Free X-API-Key | Yes | Pass-through, no QA/QC at ingestion |
| **PurpleAir** [28] | Low-cost dense | Points-based | Yes | Apply Barkjohn correction [18]; **5–6× low in dust** [19] |
| **WAQI (aqicn.org)** [29] | Regulatory aggregate | Free token | **NO** ("personal/non-commercial only") | License blocker |
| **IQAir** [30] | Mixed | Free (AQI only) | Paid for raw PM2.5 | Default ToS personal-use only |
| **Sensor.Community** [31] | Low-cost open | Free | Yes (open) | Sparse in US; no correction at source |
| **EEA** [32] | EU regulatory | Free | Yes | EU only |
| **CAMS PM2.5** [33] | Model | Free CDS API | Yes (CC-BY) | ~40 km too coarse for urban |

**For commercial app**: AirNow + EPA-corrected PurpleAir + CAMS for global.
Avoid WAQI and IQAir as primaries due to license terms.

### Equipment protection

No API directly answers "is it safe to deploy." Indirect inputs:

- Pollen count (Google Pollen [35] / Ambee [37]) with **pine** as named
  contributor — trigger equipment-protection alert at >1,500 grains/m³.
- Saharan dust (CAMS [68]) during SE-US June–August window — silica
  abrasion risk advisory.
- NC State GDD model [42] for SE-US users — surfaces "we are in pine
  pollen window."

Vendor positions on pollen damage span from "with proper care, normally
this will not degrade image quality" (Astro-Physics [78]) to "very
aggressive ethereal oils which can indeed penetrate into the coating
layers" (Baader [80]). The widely-quoted "5–7 minute corrector
contamination window" [76] traces to one Tier 3 source (Arkansas Sky
Observatories) with no measurement methodology, and the page returned
403 in our re-fetch — **treat with caution**.

PlaneWave [81] explicitly excludes pollen damage from warranty.
Celestron's exclusion is broader [82] but covers it. **There is no
standard astronomical-equipment insurance product for contamination
damage** as of this research.

### Volcanic / stratospheric

| Source | Use case | Cost | Notes |
|---|---|---|---|
| **GloSSAC** [98] | Long-term SAOD baseline | Free | 1979–Dec 2024 canonical record |
| **SAGE III/ISS** [Dim9 Disc.] | Stratospheric extinction profile | Free | ±70° latitude only |
| **TROPOMI SO₂** [99] | NRT volcanic SO₂ | Free | Operational DOAS noisy; COBRA algorithm 4× better |
| **Smithsonian GVP weekly** [Dim9 Disc.] | Eruption summaries | Free | Weekly narrative; WFS GeoJSON |
| **USGS HANS** [97] | US volcano alert level | Free | JSON API, no SLA |
| **London VAAC QVA API** [96] | Aviation-quality ash forecast | Free with reg. | Only VAAC with REST API; aviation-focused |
| **IVHHN Vog Dashboard** [94] | Hawaii surface SO₂/PM2.5 | Free | Web dashboard only, no API |
| **VMAP Hawaii** [95] | Hawaii vog forecast | Free | WRF + NAM NEST; no API |

**Most of the time, this dimension is "off" for the app.** Run as a
background advisory layer; surface only when GloSSAC anomaly exceeds
~0.02 SAOD above background or after a confirmed VEI ≥ 5 eruption.
Stellar photometric SAOD detection floor is ±0.017 [91] — events below
~0.02 SAOD are at the noise.

---

## The PM2.5 → magnitude conversion (don't use a single number)

The chain `PM2.5 → AOD → magnitude loss` accumulates two large
uncertainties. See
[references/particulates-to-imaging-impact.md](references/particulates-to-imaging-impact.md)
for the full decomposition.

### The physics is simple

```
Δm (mag/airmass) = 1.086 × τ
```

where τ is the optical depth. AOD scales between bands via the Ångström
exponent [5]:

```
AOD(λ) = AOD(λ₀) × (λ/λ₀)^(−α)
```

Typical α: 0–0.5 for coarse-mode (dust, pollen); 1.5–2.5 for fine-mode
(urban, smoke).

For a fine-mode aerosol with α = 1.5 and AOD(550 nm) = 0.20, applying
AOD(λ) = AOD(550) × (λ/550)^(−1.5) and Δm = 1.086 × AOD (all values est.):

| Band | Wavelength | AOD (est.) | Δm at zenith (mag, est.) |
|---|---|---|---|
| OIII | 500 nm | 0.231 | 0.25 |
| V | 550 nm | 0.200 | 0.22 |
| Ha | 656 nm | 0.154 | 0.17 |

**OIII suffers more than Ha during fine-mode events.** Under coarse-mode
(dust, pollen), all bands see roughly equal extinction.

### The PM2.5 → AOD bridge is unreliable

- Daily PM2.5/AOD R = 0.03–0.60 across 19 stations in China [11].
- η = PM2.5 per unit AOD spans 7.8 µg/m³ (Hawaii) to 504 µg/m³ (Mongolia)
  globally [17] — a 65× range.
- Above 1.3 km altitude the PM2.5–AOD relationship breaks (R² 0.03–0.21)
  [16].
- 58% of aerosol scale-height measurements place mass above 1.35 km
  [16] — surface PM2.5 misses most of it.

### Observatory baselines anchor expectations

| Site | Elevation | V-band median (mag/airmass) | Source |
|---|---|---|---|
| Cerro Paranal | 2,635 m | ~0.15–0.16 (with α = −1.38 [1]) | Patat 2011 [1] |
| Mauna Kea | 4,205 m | V ≈ 0.11, B ≈ 0.19 (DRIFT — band values not re-verified [2]) | Buton 2013 [2] |
| ORM (La Palma) | 2,396 m | 0.130 [3] | IAC [3] |

A SE-US sea-level user under typical summer conditions sees ~2–3× this
extinction, with the additional component being mostly aerosol and water
vapor.

### The recommended display

Don't show the user a single "PM2.5 health number" as a transparency
proxy. Instead:

1. **Primary number**: column AOD at 550 nm (from AERONET nearest station
   [73] or CAMS gridded forecast [33]).
2. **Per-band Δm**: V-band for broadband planning; Ha and OIII for
   narrowband planning, with the Ångström-exponent assumption noted.
3. **Surface PM2.5**: shown as a separate "air quality" indicator for
   human comfort — not as a transparency proxy.
4. **Confidence**: surface forecast uncertainty (per [59], smoke
   forecast spatial r ≤ 0.50 — be honest).

---

## Source conflict resolution: the practical algorithm

When AirNow regulatory and corrected PurpleAir diverge by >50% at the
same time and place, the wrong answer is to silently pick one or
average them. The right answer depends on the active aerosol regime.

The Barkjohn 2021 EPA correction [18]:

```
PM2.5_corrected = 0.524 × PA_cf_1 − 0.0862 × RH + 5.75
```

works well for urban aerosol (slope 1.00) and smoke (slope 0.99), but
**underestimates dust by a factor of 5–6** (Keeler CA slope 5.6) [19].

Recommended logic (Option B from
[references/source-conflict-resolution.md](references/source-conflict-resolution.md)):

1. **AirNow regulatory station within 25 km** → use AirNow [23].
2. **Else EPA-corrected PurpleAir within 10 km** with A/B agreement →
   use median.
3. **Else OpenAQ aggregator** [26] (filter to government providers if
   possible).
4. **Else CAMS gridded reanalysis** [33] with low-resolution caveat
   surfaced to user.

**Aerosol-regime override**: if CAMS dust AOD [33] is elevated in the
region OR active wildfires within plume distance via FIRMS [56], treat
PurpleAir-derived numbers with skepticism and prefer AirNow regulatory.

When sources disagree by >50% even after this hierarchy, **show both
values with provenance** rather than fusing — let the user see the
uncertainty.

---

## What this research did not resolve

Honest gaps where the literature is thin:

1. **Pollen grains/m³ → V-band Δm conversion**: no paper found provides
   this. Pine pollen specifically lacks any quantitative astronomical
   extinction study.
2. **Pinatubo / Hunga Tonga in standard photometric magnitudes for
   amateur conditions**: discussed in observatory-tier literature
   (Paranal twilight calibration in ESO Messenger 190 [89] —
   **INACCESSIBLE in our re-fetch (PDF parse failure + 403 on archive
   page); claim rests on Phase 1 discovery-agent extraction only**).
3. **Narrowband (Ha vs OIII) differential extinction during smoke or
   dust events**: physics-correct calculations exist (Ångström exponent
   [5]) but not empirically validated for amateur conditions.
4. **Wildfire smoke deposition on telescope optics**: undocumented gap.
   Inferred to require solvent cleaning analogous to cigarette tar but
   no published guidance.
5. **The widely-quoted "5–7 minute corrector contamination window"**
   [76] traces to one Tier 3 source whose page returned 403 in our
   re-fetch. The claim is widely repeated but has no published
   measurement methodology.
6. **No standardized pollen API head-to-head accuracy comparison.**
   Independent accuracy data for consumer pollen apps is broadly poor
   [48], but no peer-reviewed test of Tomorrow.io vs Ambee vs Google
   Pollen exists.
7. **Insurance coverage for contamination damage**: no policy product
   confirmed.

---

## Phase 1 confidence and verification

This research was produced via the cited-research methodology with two
explicit confidence checkpoints:

- **Phase 1 sub-agents** (16 dispatched, 14 completed; 2 hit
  mid-task rate limits — Dim3 Dust Counter and Dim6 Equipment Counter)
  produced URL manifests and preliminary extraction across all 9
  dimensions. Confidence ranged 0.55–0.82 across dimensions.
- **In-session WebFetch verification** of 14 highest-priority Tier 1–2
  sources directly confirmed quantitative claims (Barkjohn equation
  [18], Jaffe 2023 5–6× dust factor [19], Patat 2011 Paranal extinction
  parameters [1], NC DEQ station details [41], Pinatubo USGS chapter
  [86], Williams Flats intercomparison [59], Google Pollen 80-country
  coverage [35], etc.). Several discovery-agent claims were corrected
  during this step (e.g., Barkjohn calibration is **39 sites in 16
  states**, not "70+ sites" as some secondary references state).
- **Phase 4 isolated verification agents** (citation audit + consistency
  review, run in separate sessions with no conversation context) audit
  the produced files. Their reports are in the [audit/](audit/)
  directory.

Citations marked **(verified)** in [citations.md](citations.md) are
in-session re-verified; **(unverified)** rest on Phase 1 extraction with
matching URLs that the audit agent reads against persisted snapshots.
