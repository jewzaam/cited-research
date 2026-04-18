# Patch Volatility & Guide Freshness

What has changed, what's likely to change, and how to judge if a guide is
stale. This dimension exists to make the deliverable honest about its shelf life.

Research snapshot date: **2026-04-17**. Game version: **Hotfix 0.2.1** (released
April 16, 2026 per [2]).

See [citations](../citations.md) for sources.

## Chronological Patch Timeline

From [2][4][32]:

| Version | Date (approx) | Type | Key Changes |
|---|---|---|---|
| 0.1.0 | 2026-01-06 | EA Launch | Initial public release |
| 0.1.1 | 2026-01-09 | Hotfix | Subtitle/font scaling, Japanese font, launch crash on some configs |
| 0.1.2 | 2026-01-16 (approx) | Hotfix | Audiolog subtitles, Chinese font scaling, inventory-crash fix. **Initially released without official Steam announcement**, community discovered via SteamDB and 542.8MB download prompt |
| 0.1.3 | Late Jan / early Feb 2026 | Technical Hotfix | Disabled PTB save loading (intentionally save-breaking); UI text readability |
| Update 1 PTB | ~2026-03-25 | PTB release | 0.2.0 feature rollout for testing |
| Update 1 PTB Hotfix 1 | early April 2026 | PTB balance | Build-cost adjustments (Power Generators, Zipline, Drone Rails, Teleport); energy consumption/cooling for v.2 buildings; Scanner unlock moved to Recipe Station; recipe rebalances (Nanofibre, Pressure Tank, Condenser, Superconductor) |
| **Update 1 (0.2.0)** | **2026-04-09** | Major content | Map expansion, Powerium + Goethite, Zipline, Development Station, v.2 buildings, 40+ new items, Vulpir/Coralion/Skylisk wildlife |
| **Hotfix 0.2.1** | **2026-04-16** | Stability | Rail junction deconstruction crash fix, Fire Wave co-op stability |

Dates for Update 1 and Hotfix 0.2.1 are confirmed by [2] and [4]. Earlier hotfix
dates are approximate, sourced from [2]'s "N weeks ago" phrasing relative to the
research date.

## What Changed in Update 1 (April 9, 2026)

### New Content

- **Map expansion** with unlockable zones and new points of interest [4]
- **New resources:** Powerium, Goethite [2][4]
- **New traversal:** Zipline system [4]
- **Development Station** (habitat building) — unlock mechanism for v.2 buildings [4]
- **v.2 buildings:** Compounder v.2, Fabricator v.2, Furnace v.2, Ore Excavator
  v.2, Orbital Cargo Launcher v.2, Constructorizer v.2 [4]
- **New buildings:** Oil Extractor, Laser Drill, Refinery, Pyro Forge, Facturer,
  Chemical Generator, Radial Rail Connector, Recycler [4]
- **"40+ new items and recipes"** [4]
- **Three new wildlife:** Vulpir, Coralion, Skylisk [4]

### Mechanics Reworks (Progression-Significant)

Per [2] and Counter-Discovery agent summaries of inaccessible official patch
notes [3]:

- **Corporation levels reset to Level 1**, with prior progress converted to
  Data Points (Counter-Discovery summary from [42]; flagged unverified but
  strong signal from community threads)
- **Scanner blueprint:** unlock path moved from world-exploration to Recipe
  Station [2]
- **Pressure Tank blueprint:** unlock path moved from Forgotten Engine dungeon
  to Recipe Station [32]
- **Quartz Building Material deprecated** as a build currency (Counter-
  Discovery summary; unverified at primary-source level) — existing stock
  can be recycled to Quartz Ore via the Recycler
- **Teleporter unlock:** alternate path added via corporation-level achievement
  (Counter-Discovery summary of gamingpromax.com)

### Recipe Changes (from PTB Hotfix 1, shipped in 0.2.0)

Per Counter-Discovery sourcing from [2]:

- **Nanofibre:** Wolfram Wire added as third component (net cost increase)
- **Pressure Tank:** Titanium Housing removed (net cost reduction)
- **Condenser:** Synthetic Resin removed (net cost reduction)
- **Superconductor:** Ceramics replaced by Synthetic Resin (upstream chain change)

These specific recipe changes are mentioned in Counter-Discovery summaries and
in the PTB Hotfix 1 context [2]. They were not directly recovered from a
fetched primary-source patch note.

### Build Cost Changes (PTB Hotfix 1)

Per [2]:

- Power Generators, Ziplines, Drone Rails, Teleport: build costs adjusted
  (specific numbers not recovered)
- Energy consumption and Base Core cooling rebalanced for v.2 buildings

## What Changed in Hotfix 0.2.1 (April 16, 2026)

Per [2][5]:

- Fixed crash when deconstructing Rail junctions
- Improved co-op stability during Fire Wave events
- Improved stability when deconstructing buildings

No progression-relevant balance changes confirmed in this hotfix — it is a
stability pass responding to regressions introduced by Update 1 itself.

## Documented Regressions & Community Complaints Post-Update 1

From [35]:

- **Turret targeting regression:** "24 gun towers in a 3-layered defense... the
  guns might kill 6 of the 50 bugs that come running at them now"
- **Base cooler nerf:** "The base coolers were also made 75% less effective"
- Player framing: regression, not balance pass; no developer response

Per Counter-Discovery on [42] (unverified direct fetch):

- One player reported 0 crashes in 28.7 hours pre-patch → 15 crashes in 25
  minutes post-hotfix
- Character banter/dialogue feature silently removed in an early hotfix with
  no patch-note entry

## Guide-Freshness Rules

Based on patch history:

1. **Any guide dated before April 9, 2026** may be stale on: Scanner acquisition
   (world-find → Recipe Station), Pressure Tank acquisition (dungeon →
   Recipe Station), Quartz Building Material usage, corporation level state
   (reset), recipe ingredient counts (Nanofibre, Pressure Tank, Condenser,
   Superconductor), turret effectiveness, cooler effectiveness.

2. **Any guide that doesn't mention the Development Station** is missing the
   v.2 building unlock mechanism [4].

3. **YouTube guides titled "Before Update 1"** are explicitly stale on the
   author's acknowledgment.

4. **Wiki pages last updated before April 2026** (e.g., starrupture.wiki.gg's
   Quartz Building Material page, last updated Jan 12 per Discovery) reflect
   pre-Update-1 state and should be cross-checked with patch notes.

## Developer Communication Pattern

A recurring theme in Counter-Discovery [48]: Creepy Jar has been inconsistent
about releasing patch notes contemporaneously with builds. Hotfix 0.1.2 (a
542.8MB download) had no official Steam announcement initially; players
discovered it via SteamDB [2]. Community complaints about developer-communication
use phrases like "extremely unprofessional" and "dishonest" regarding
"very, very soon" messaging without dates. Update 1 was contemporaneous with
a formal patch-note post (though the page itself was JS-gated at fetch time).

## Expected Volatility Going Forward

Given a stated ~1-year EA (launch Jan 2026 → 1.0 target 2027 [1]), and the
current cadence (Update 1 was the first major content update, ~3 months
post-launch), additional major updates are likely before 1.0. Planned 1.0
features per [4] and Discovery summaries of the roadmap post [7] include:

- Frost Wave (new hazard type, parallel to Rupture)
- Additional biome
- "Definitive endgame" (story conclusion, final objectives)
- Achievements (not in EA per [4])
- Expanded character skill caps (45 → 100) [9]

Any guide — including this one — should be re-verified against patch notes
after the next major update.

## What This Means for Readers of This Research

The current snapshot (2026-04-17, Hotfix 0.2.1) is:

- **8 days after** a major content + balance update (Update 1)
- **1 day after** a stability hotfix (0.2.1)

Therefore:

- Recipe-ingredient advice here should hold at least until the next content
  patch
- Corporation-level unlocks appear unchanged by Update 1 (only player progress
  was reset); the unlock table in [Progression Systems](progression-systems-inventory.md)
  is current
- Combat-tuning advice is least stable — Update 1's turret/cooler changes
  suggest the base-defense loop is actively being reworked, and a follow-up
  rebalance is plausible

## Gaps & Limitations

- **Official Steam patch-note pages [3][5][7] were inaccessible (JS-gated).**
  All specific patch content is routed through [2] (Patchbot aggregator) and
  [4] (press coverage). A direct quote of the official patch notes was not
  achievable during this research window.
- The **Massively Overpowered player-count article [8]** (42,864 → 7,331)
  would corroborate retention impact of the content-drought window, but was
  INACCESSIBLE.
- Exact build-cost deltas (e.g., "Power Generator was 40 BBM, now 30") are
  not recovered.
