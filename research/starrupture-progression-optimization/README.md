# StarRupture Progression Optimization

A citation-backed research document on efficient progression in StarRupture
(Creepy Jar, 2026, Early Access on Steam). Research snapshot **2026-04-17**,
game version **Hotfix 0.2.1** (released April 16, 2026).

**Audience:** solo/duo first-playthrough aiming for efficient completion.
Min-max and multiplayer divergences are called out only where they materially
change a recommendation.

**Warning:** StarRupture is in Early Access. Progression mechanics changed
meaningfully in Update 1 (April 9, 2026) — guides written before that date
are stale on Scanner/Pressure Tank acquisition, corporation level state,
several recipe ingredients, and base defense tuning. See
[patch volatility](references/patch-volatility.md) for staleness flags.

## TL;DR — Three Decisions That Dominate the Run

1. **Spend Data Points on recipes, not on corporation leveling.** Per
   IntoIndieGames [20]: "Datapoints are essential for unlocking various
   recipes... spending them on leveling can be a waste." Use OCL commissions
   to level corporations; reserve DP for the Recipe Station.

2. **Treat post-Rupture as farming time, not recovery time.** Ignitium
   (2,000 DP per 5-bundle) [11], Glowcap (90 DP each) [10], and Oxallop [21]
   only appear post-Rupture. Pre-stage OCL commissions, shelter through the
   15-second countdown, then farm.

3. **Build distributed satellite bases, not a single expanding megabase.**
   Recipe cycling obsoletes prior production. This recommendation is contested
   — the original complaint [34] frames it as a design flaw, while experienced
   players in the same thread argue it is a playstyle mismatch. Distributed
   satellite production is the community workaround that has the most
   experienced-player backing [34], but readers who value single-base
   expansion should be aware this reflects a divergence from the in-game
   progression loop, not a designer-endorsed strategy.

## Key Facts at a Glance

| Fact | Value | Source |
|---|---|---|
| Developer | Creepy Jar | [1] |
| EA launch date | 2026-01-06 | [1] |
| Steam review score (overall) | 82% positive, 5,858 reviews | [1] |
| Current price | $15.99 (20% off from $19.99) | [1] |
| Current version | 0.2.1 (released 2026-04-16) | [2] |
| Planned 1.0 window | 2027 (~1 year EA) | [1] |
| Skill tracks / cap | Combat, Survival, Movement / 45 EA, 100 1.0 | [9] |
| Corporations | 5 (four cap L11, Clever Robotics caps L13) | [14] |
| Currencies | Data Points, War Bonds | [10][26] |
| Terminal objective (current EA) | World Engine / Forgotten Engine + teleporter | [33] |
| Highest DP source | Goliath Biological Sample (5,000 DP) | [17] |

## Priority Corporation Unlocks (First Session)

| Priority | Target | Why |
|---|---|---|
| 1 | Moon Energy Level 3 | Map — Fog of War removal [13][14][25] |
| 2 | Selenian Level 2 | Fabricator [14][25] |
| 3 | Griffits Blue Level 2 | UPP-7 Reaper Pistol [13][15] |
| 4 | Clever Robotics Level 2 | Personal Storage (18 slots) [14][24] |
| 5 | Future Health Solutions Level 3 | Regeneration Chamber, Medtool [14] |
| 6 | Selenian Level 3 | +8 character inventory [24] |

Bring all corporations to Level 2 cheaply first [25][29] before pushing any
single corporation to Level 3.

## Decision Framework

1. **Is it your first 5 hours?** See [Early-Game Optimization](references/early-game-optimization.md).
   Loot the Lander, set a Commission before exploring, forage Polifruit and
   Hydrobulb, drive toward Moon Energy L3 for the Map.

2. **Are you hitting the mid-game (~5–30 hours)?** See
   [Mid-to-Late Progression](references/mid-late-progression.md). Unlock the
   Equipment Upgrade Station at Griffits Blue L4; push Selenian to L6 for
   the Helium-3 Extractor; find the Electronics blueprint at CRO "Grey Owl"
   ClayWood Research Outpost; complete the Satellite POI key-card chain
   (Ellis + Diaz + Perkins) to avoid soft-locking.

3. **Are you at the late-game wall (30+ hours)?** See
   [Mid-to-Late Progression](references/mid-late-progression.md). Goliath
   farming (5,000 DP per kill) is the dominant DP source. Corporation levels
   9–11 shift from DP acceleration to export-based progression. Expect a
   content ceiling — "definitive endgame" is a 1.0 target.

4. **Are you reading a pre-April-9, 2026 guide?** See
   [Patch Volatility](references/patch-volatility.md) for what's stale.
   Specifically: Scanner and Pressure Tank acquisition paths, Quartz Building
   Material usage, corporation level state, Nanofibre/Pressure Tank/
   Condenser/Superconductor recipes, turret and cooler effectiveness.

## Files in This Research Directory

- [`progression-guide.md`](progression-guide.md) — the full deliverable
- [`citations.md`](citations.md) — all sources, numbered 1–50
- [`references/game-overview-ea-state.md`](references/game-overview-ea-state.md)
- [`references/progression-systems-inventory.md`](references/progression-systems-inventory.md)
- [`references/early-game-optimization.md`](references/early-game-optimization.md)
- [`references/mid-late-progression.md`](references/mid-late-progression.md)
- [`references/resource-economy.md`](references/resource-economy.md)
- [`references/combat-build-meta.md`](references/combat-build-meta.md)
- [`references/patch-volatility.md`](references/patch-volatility.md)
- [`audit/citation-audit.md`](audit/citation-audit.md) — Phase 4 sub-agent
  output verifying every cited claim
- [`audit/consistency-review.md`](audit/consistency-review.md) — Phase 4
  sub-agent output verifying cross-file consistency

## Limitations

- Official Steam patch-note pages were JS-gated and could not be directly
  fetched; Update 1 / Hotfix 0.2.1 specifics route through Patchbot [2]
  and secondary press [4]
- Multi-engine search augmentation did not run due to a package-rename
  issue — single-engine (WebSearch) bias is not structurally reduced
- Several high-signal sources (Massively OP player-count article, Screen
  Hype review, The Review Geek review, TechRaptor starter guide, Deltia's
  Ignitium guide) returned persistent 403/405 errors and are noted INACCESSIBLE
- No Reddit results surfaced — community edge-case discussion is a gap
- Single fetched external critic review (n=1)

## Audience Note on Min-Max and Multiplayer

This research is scoped to **solo/duo first-playthrough**. Where optimization
advice differs for min-max speedrunners or multiplayer groups, the divergence
is called out inline in the relevant section. The document does not contain
a dedicated min-max chapter or multiplayer chapter.
