# Astrophotography Planning Apps & the Gap Landscape (April 2026)

A citation-backed survey of existing astrophotography planning apps to inform a build / contribute / use-existing / skip decision for a planned new app. Conducted April 2026.

All factual claims are numbered and cite [`citations.md`](citations.md). Per-dimension detail lives in [`references/`](references/). Two independent verification agents audited this document — see [`audit/`](audit/).

## TL;DR

The honest answer is **don't build a generic astrophotography weather/planning app — the ecosystem already covers the basics well.** But there are two **specific, defensible gaps** worth filling, either as standalone product or (more cheaply) as a plugin to an existing OSS suite:

1. **Particulate-aware planning beyond wildfire smoke** — pollen, Saharan dust, urban PM2.5. *No app surfaces these today*; only Astrospheric covers wildfire smoke (US/Canada only) (Reference [06](references/06-particulate-integration.md)).
2. **Equipment-aware composite "go / no-go" score** — a single number that integrates seeing + transparency + cloud + targets + dew risk + the user's specific rig (focal length, sensor, narrowband vs broadband). The closest existing approach is StarCast (March 2026 launch) which integrates six atmospheric variables and target categories but no equipment specs (Reference [05](references/05-decision-aid-gap.md)).

The combination is differentiated. Either alone is differentiation; both is a niche worth defending.

The secondary bigger question — **is the market viable?** — answers cautiously yes-with-caveats. Astrophotography hobby is growing (telescope market ~7.8% CAGR per a 2020 paid report [191]; astrophotography camera market 8.9% CAGR per Verified Market Reports [192]) but indie astro-app revenue ceilings appear to top out around ~$200K ARR (est.) for planning-only tools — derived from Astrospheric's upper-bound ~$162K inference + Telescopius's ~$29K Patreon as the two highest indie planning-only data points (Reference [09](references/09-market-viability.md)). PhotoPills at ~$1M is the only demonstrable indie commercial success in the adjacent space, and it serves a much broader landscape-photography audience.

## Methodology summary

10 dimensions (see Reference files 01-10), each researched via parallel Discovery + Counter-Discovery sub-agents using WebSearch, with vendor-page WebFetch verification on the most cited pricing and feature claims. 216 sources catalogued in [`citations.md`](citations.md). Counter-perspective searches were folded into the same citation pool — no special tagging.

**Confidence is mixed across dimensions:** strongest on tool inventory and pricing (T2 vendor sources directly verified); weakest on market viability (forced to infer from third-party analytics, paid market reports, and inference). Full per-dimension confidence and limitations are in each reference file's "Gaps and limitations" section.

## Frame check

The user's question implicitly assumed three things, surfaced for transparency:

1. **The "build or contribute" frame.** This research adds a third possibility — *don't build at all because distribution and retention to a small hobbyist audience is the real bottleneck.* See Reference [09](references/09-market-viability.md) for evidence.
2. **The deep-sky imaging audience is the implicit subject.** Wide-field/Milky-Way photography (PhotoPills, TPE) has a different tool ecosystem and is largely orthogonal to this research's findings — see Reference [03](references/03-photo-planners.md).
3. **The North-American context dominates the candidate-citation list.** Most data sources surveyed (NWS, HRRR, RDPS, AirNow) and the leading dedicated weather app (Astrospheric, US/Canada-only) are CONUS-centric. A global tool faces a thinner data foundation. This is not made an explicit dimension but it's flagged as a structural constraint on addressable market.

## Landscape summary

### Decision format — what each tool actually presents

| Format | Tools | Verdict |
|---|---|---|
| **Raw data table, color-coded per cell, user synthesizes** | Astrospheric [27], Clear Outside [9], Clear Dark Sky [11][12], Good to Stargaze [15] | High info density; cognitive load real in driveway use |
| **Categorical traffic light per time block** | Scope Nights (3-tier) [13][14] | Coarse; limited inputs (no seeing/transparency from a meteorological model) |
| **Single composite percentage (limited inputs)** | Sky Tonight Stargazing Index [138][139] | Good UI; thin inputs (moon + cloud + Bortle + visibility window) |
| **Single composite 0-100 score with target-type modifier** | StarCast (LightCast suite) [136][137] | **Closest to a comprehensive composite found**; integrates cloud + moon + Bortle + humidity/visibility + seeing + dew-point. No equipment-aware modifier. New (March 2026) |
| **Per-target geometry score (not conditions)** | Telescopius visibility/season scores [38], Astrophotography Planner iOS [142] | Useful for target-vs-night, not weather-vs-night |

**Conclusion:** the comprehensive composite-score gap is **real but narrower than the user's intuition assumed.** StarCast substantially closes the atmospheric-conditions gap. The remaining true gaps are equipment-aware modification and particulate integration.

### Particulate integration — gap fully confirmed

| Particulate | Astrospheric | Clear Dark Sky | All others |
|---|---|---|---|
| Wildfire smoke | YES (column-integrated PM2.5, 6h refresh) [4][5] | PARTIAL (smoke row from FireSmoke.ca, vendor-warned not well-calibrated) [11][155] | NO |
| AOD / aerosol | YES (jet stream + AOD overlay) [147] | NO | NO (Meteoblue API has AOD550; consumer page unconfirmed) |
| Saharan dust | NO (subsumed in generic smoke/PM2.5) | NO | NO ([154][158]) |
| Pollen | **NO** | NO | **NO across all apps** ([150][153]) |
| Urban PM2.5 | Implicit only (vendor warns not for AQI use) [4] | NO | NO |

Astrospheric is alone in the category and covers wildfire smoke only. The pollen + dust + AQI integration is **the strongest greenfield gap surfaced** in this research.

### Existing tool gravity

Three competitive moats indie new entrants must navigate:

1. **Free-tier dominance.** Clear Outside is free, retailer-backed [9]. NINA, KStars, Stellarium, Cartes du Ciel are free OSS. Telescopius is free + Patreon. **An indie new app cannot compete on price** — it has to differentiate on capability.
2. **Astrospheric's data depth.** $29.99/yr Pro tier surfaces ensemble cloud (RDPS+GFS+NBM+NAM), Allan-Rahill seeing, RAP-derived smoke, jet stream, dew point, AOD overlays [1][4][27]. Hard to match without a multi-year data-pipeline investment.
3. **Telescopius's planning workflow.** Equipment-aware target filtering, FOV simulation, mosaic planning, CSV export to NINA/SGP/Voyager/ASIAIR [38][42]. The de facto target-selection tool for hobbyist deep-sky imagers.

### Build-on-top vs contribute-to-existing

The OSS surface is contributable:

- **NINA** — MPL 2.0; plugin SDK with manifest registry; closed-source plugins rejected [102][108][109]. Plugin scope is broad. Highest-leverage *contribution* target if the goal is to add a decision-aid score to a Windows-imaging audience.
- **KStars / Ekos** — GPL-2.0+; full D-Bus surface [76][77][78]. Cross-platform reach. Higher governance friction (KDE) but feasible.
- **Stellarium** — GPL-2.0+; HTTP RemoteControl API + ECMAScript scripting [49][50]. Broad reach, lower AP-specificity.

The closed-but-API-accessible surface enables *companion* products:

- **Astrospheric REST API** — Pro-tier-gated; 100 credits/day; cloud-cover call costs 5 credits [8]. Dependency on vendor's pricing/terms. US+Canada coverage hard limit.
- **Voyager Application Server API** — JSON-RPC over TCP/WebSocket [116]. Companion-app development; not core extension.
- **Underlying weather APIs** — NWS (US-only, free, no key), MET Norway (CC-BY-4.0, global), ECMWF Open Data (CC-BY-4.0, global), 7Timer (free, no key, **non-commercial only**), Open-Meteo (AGPL-3.0 self-host or free non-commercial hosted), Meteoblue (5K calls/yr free, paid commercial) [164][165][167][18][169][22]. **A "thin decision layer over directly-usable data providers" is technically feasible.**

## The build / contribute / skip framework

### Build new

Make sense **only if all three are true:**

1. The differentiation is the particulate integration + equipment-aware score combination (Refs [05](references/05-decision-aid-gap.md) and [06](references/06-particulate-integration.md)) — i.e., the new niche, not a generic competitor.
2. The 5-year horizon is acceptable. Top-end revenue is **~$50K/yr in years 1-3 (est.), hard ceiling around ~$200K ARR (est.; sum of inferred Astrospheric ~$162K upper + Telescopius ~$29K)** (Ref [09](references/09-market-viability.md)). PhotoPills's ~$1M is achievable only with a much broader photographer-audience pivot.
3. There's a YouTube-reviewer distribution plan from day one (AstroBackyard especially [197][198]). App Store organic discovery is essentially dead for niche apps without paid acquisition [194].

Native iOS + Android is required (Ref [10](references/10-mobile-vs-desktop.md)). PWA/TWA architecture is a quality penalty (see Telescopius and Ouranos rating gaps). Offline-friendly design is a moat.

### Contribute to existing

**The lowest-effort path to the same impact** is a plugin or extension to an OSS suite:

- **NINA "Decision Score" plugin** that consumes the existing Weather driver + Safety Monitor signals, adds particulate inputs (AirNow + a pollen API + a dust source), and outputs a composite go/no-go score per night — published to NINA's plugin registry [108][109]. Reach: Windows imagers (large addressable audience).
- **KStars/Ekos enhancement** that integrates a multi-factor score into the Scheduler's constraint logic [75][77]. Cross-platform, smaller user base, higher contribution-friction.
- **Stellarium plugin** that surfaces a planning panel pulling weather/particulate signals from external APIs [49][50]. Broad reach, lower AP-specificity.

Any of these costs months, not years, and the audience already exists.

### Use a paid tier and move on

For a US/Canada-based imager whose most pressing real complaint is wildfire smoke or transparency:

- **Astrospheric Pro at $29.99/yr** [2] is the highest-quality data product in the category and already integrates wildfire smoke into transparency [4][6][27].
- **Telescopius (free)** for target selection and FOV/mosaic planning [38].
- **Sky Tonight or Stellarium Mobile Plus** for casual driveway-use and a built-in red night mode [138][52][200].

Total annual cost: $30. The *missing* particulate signals (pollen, Saharan dust, urban PM2.5) and the *missing* equipment-aware composite score are the only things this stack doesn't deliver — which loops back to the differentiation hooks for the new product.

### Don't build at all

A real option, supported by Ref [09](references/09-market-viability.md):

- App Store organic discovery has structurally collapsed for niche apps [194].
- Free-tool gravity (Clear Outside, OSS suites) sets the price floor at $0.
- Top-end indie planning-app revenue is ~$200K ARR (est.; sum of Astrospheric upper inference + Telescopius Patreon); PhotoPills ~$1M is not the relevant precedent.
- Subscription retention for low-frequency hobbyist apps is below average-app benchmark of 44.1% annual [189].

If the goal is income, build for a different audience. If the goal is solving the personal pain (NC pine pollen seasons), the contribute-or-side-project paths cost less and serve the goal equally well.

## Reflection

After assembling the draft above and before writing the README, one final pass:

- The decision-aid gap (Ref [05](references/05-decision-aid-gap.md)) was almost certainly stated with more confidence in the topic spec than the evidence supports. StarCast's March 2026 launch is the clearest example of the gap narrowing during the time the user has been considering the build. *This is a moving target* — a new entrant could discover it has been beaten to market while still in development.
- The particulate gap (Ref [06](references/06-particulate-integration.md)) is the most durable. No tool plans pollen integration; no tool plans Saharan dust as a separate signal. This is a defensible niche on its own.
- Market-viability inference (Ref [09](references/09-market-viability.md)) leans heavily on third-party analytics (MWM, AppBrain, Crunchbase) and paid market reports. Treat the absolute numbers as directional. The *trend* (sustained hobby growth, indie revenue ceiling around six figures) is consistent across all sources.
- Counter-evidence was integrated honestly: StarCast was found via the discovery agents themselves, not pushed back by a separate counter-search (most counter-discovery agents hit usage limits before producing output). The discovery agents' counter-evidence absorption was sufficient given the broad framing of their queries.

## Source quality and recency

- Pricing data: all primary tools verified against vendor pages April 2026.
- Feature claims for Astrospheric, NINA, SkySafari 8, SGP, StarCast, Stellarium Mobile Plus: vendor pages directly fetched and quoted.
- Market-size and revenue figures: third-party estimates flagged in Ref [09](references/09-market-viability.md).
- Forum/community signals: T4 sources cited explicitly; treat as anecdotal-but-directional.
