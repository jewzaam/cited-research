# Astrophotography Planning Apps & the Gap Landscape

Citation-backed survey of existing astrophotography planning apps as of April 2026, intended to inform a build / contribute / use-existing / skip decision before greenfield work.

**Full deliverable:** [analysis.md](analysis.md)
**Per-dimension detail:** [references/](references/)
**All sources:** [citations.md](citations.md)
**Verification:** [audit/](audit/)

## One-paragraph summary

The astrophotography weather + planning ecosystem already covers the basics well. **Don't build a generic competitor.** Two specific gaps are real and defensible: (1) particulate-aware planning beyond wildfire smoke — *no app today* surfaces pollen, Saharan dust, or urban PM2.5; only Astrospheric covers wildfire smoke and only in the US/Canada; and (2) an equipment-aware composite "go/no-go" score — the closest existing approach is StarCast (launched March 2026), which integrates six atmospheric variables and target categories but no user equipment specs. The market is real and growing (telescope market ~7.8% CAGR per a 2020 paid report; astrophotography-camera market 8.9% CAGR per Verified Market Reports) but indie revenue tops out around ~$200K ARR (est.) for planning-only tools — based on the inferred upper bound of Astrospheric (~$162K) plus Telescopius's Patreon (~$29K) as the highest indie planning-only data points; PhotoPills at ~$1M is the only adjacent commercial success and serves a much broader landscape-photographer audience.

## The decision matrix

| The differentiation is | Tool stack today | New product makes sense as |
|---|---|---|
| Particulate-aware (pollen + dust + AQI integration) | Nothing | **Standalone niche app OR a NINA/Ekos plugin** |
| Equipment-aware composite score | StarCast partial (no equipment) | **Plugin** (lower effort, similar reach) |
| Both combined | Nothing | **Defensible standalone niche** with 5-year horizon |
| Generic clear-sky forecast | Astrospheric / Clear Outside / 7Timer / Sky Tonight | **Don't build** — use existing |
| Generic target picker + FOV | Telescopius / Stellarium / SkySafari Pro | **Don't build** — use existing |
| Income > ~$200K/yr (est.) | n/a (no indie astro-only app reaches this; inference from Astrospheric + Telescopius data points) | **Pivot audience** or don't build |

## Quick decision framework

1. **What's the actual pain?** If it's wildfire smoke transparency in continental US/Canada, Astrospheric Pro at $29.99/yr already solves it [[2]](citations.md#)[[27]](citations.md#). If it's pollen in NC or dust in summer or chronic urban PM2.5, no tool today covers you — that's the niche.
2. **What's the time budget?** A NINA / KStars / Stellarium plugin costs months. A standalone app costs 1-3 years to MVP and ship to mobile.
3. **What's the income expectation?** Top-end indie planning-app ARR is ~$200K (est., derived from inferred Astrospheric upper bound + Telescopius Patreon). If the project is mostly for personal benefit, contribute or side-project. If it must pay a salary, plan for a 5-year horizon with realistic ceilings.
4. **What's the distribution plan?** AstroBackyard (Trevor Jones, 506K YouTube subscribers as of April 2025) is the dominant English-language reviewer. Cloudy Nights is the dominant forum (180K members). Without one or both, an indie app launches into silence — App Store organic discovery is structurally dead for niche apps.
5. **Mobile-first or don't ship.** Native iOS + Android (or excellent offline-friendly PWA). Red/night-vision mode is table stakes. Offline degradation must be graceful.

## Recommended path (this researcher's read)

**For the user described:** NC-based, deep-sky imaging, sensitive to pine pollen / smoke / dust gaps; existing FOSS-processing focus and contribution-friendly history.

The highest-leverage move is **a NINA plugin** that:
- Consumes the existing NINA Weather driver + Safety Monitor signals
- Adds AirNow (urban AQI / wildfire smoke), a pollen API (Tomorrow.io or IQVIA), and a Saharan-dust signal (NASA GEOS-FP or EUMETSAT)
- Outputs a composite per-target go/no-go score, equipment-aware via NINA's existing equipment profile
- Publishes to NINA's plugin manifest registry under MPL 2.0

This delivers the exact differentiation (particulate + equipment-aware) without competing on the parts (cloud forecasts, target catalogs) that existing tools already do well. Time-to-MVP is months not years. Audience already exists. License-compatible. And if the plugin works, it provides the validation needed to consider a standalone app later.

If the goal is purely "solve my own NC pollen problem," the same plugin scratches the itch and the work is small enough to actually ship.

If the goal is income, the data in [Reference 09](references/09-market-viability.md) does not support optimism for a standalone indie planning app — pivot the audience or don't build for income.

## What's in this directory

- [`analysis.md`](analysis.md) — Full deliverable with framing and synthesis
- [`citations.md`](citations.md) — 216 numbered sources
- [`references/`](references/) — Per-dimension detail (10 files)
  - [01-weather-tools.md](references/01-weather-tools.md)
  - [02-planning-tools.md](references/02-planning-tools.md)
  - [03-photo-planners.md](references/03-photo-planners.md)
  - [04-capture-software.md](references/04-capture-software.md)
  - [05-decision-aid-gap.md](references/05-decision-aid-gap.md)
  - [06-particulate-integration.md](references/06-particulate-integration.md)
  - [07-api-and-oss.md](references/07-api-and-oss.md)
  - [08-pricing.md](references/08-pricing.md)
  - [09-market-viability.md](references/09-market-viability.md)
  - [10-mobile-vs-desktop.md](references/10-mobile-vs-desktop.md)
- [`audit/`](audit/) — Independent verification reports
  - [citation-audit.md](audit/citation-audit.md)
  - [consistency-review.md](audit/consistency-review.md)
