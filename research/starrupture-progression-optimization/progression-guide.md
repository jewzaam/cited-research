# StarRupture Progression Optimization — Full Guide

Research snapshot: **2026-04-17**, game version **Hotfix 0.2.1** (released April
16, 2026 [2]). Audience: solo/duo first-playthrough aiming for efficient
completion without spoiler-level foreknowledge.

**Important:** StarRupture is in Early Access. This document reflects the state
8 days after Update 1 (April 9, 2026) and 1 day after Hotfix 0.2.1. See
[Patch Volatility](references/patch-volatility.md) for staleness flags on
pre-Update-1 guidance and [Game Overview](references/game-overview-ea-state.md)
for EA-state context.

## Executive Summary

StarRupture's progression is corporation-gated. Five corporations (Future
Health Solutions, Selenian, Griffits Blue, Moon Energy, Clever Robotics) unlock
buildings, recipes, and gear at specific levels; four cap at 11 and Clever
Robotics caps at 13 [14]. Data Points (earned via the Analyzing Station) fund
recipe unlocks, and War Bonds fund weapons and weapon mods [10][11][26]. The
current terminal objective is activating the World Engine / Forgotten Engine
plus the tech teleporter [33]; a defined endgame is a 1.0 target [33].

Three decisions drive efficiency across the entire run:

1. **Spend Data Points on recipes, not on corporation-level acceleration.** [20]
2. **Treat the post-Rupture window as the primary farming window**, not a
   recovery phase. Ignitium (2,000 DP per 5-bundle) [11], Glowcap (90 DP each)
   [10], and Oxallop [21] only appear in this window. Sulfur extraction also
   requires post-Rupture placement [22].
3. **Distribute production across satellite bases** rather than expanding a
   single monolithic base. Experienced players report the rebuild-loop
   frustration is a playstyle mismatch, not a design flaw. [34]

## 1. Character Systems

### Skills and LEM Augments

Three skill tracks (Combat, Survival, Movement), each currently capped at
**Level 45** and planned to reach 100 at 1.0 [9]. LEM Augment Slots unlock
at Levels 10, 25 (Combat: 20), 40 (Combat: 35), 65, 85, 100 [9]. In current EA,
three slots per skill are accessible (9 total); 1.0 will raise this to six
per skill (18 total) [9].

**LEMs stack additively** — two identical max-shield LEMs give double the
shield bonus [31]. No respec mechanism is documented in fetched sources.

### Character Selection is Cosmetic

Per [13]: "These characters bring different dialogues to each situation" —
all characters access all blueprints and abilities. Swap any time at a
Regeneration Chamber (default in ship, or craft for 100 Basic Building
Materials). Do not treat character choice as a meaningful optimization lever.

## 2. First Session (~5 Hours)

### Immediate Actions at Spawn

1. Loot the two Orbital Lander storage containers for 20 starter rations [20]
2. Place your Base Core (establishes oxygen bubble and build zone)
3. Move east from the landing pod — do not build at the pod itself [12].
   Recommended first base location: north of the small lake east of spawn [12]
4. Set a Commission on your first OCL before every exploration trip [12]

### Survival Meter Management

Three meters: Calories, Hydration, Toxicity [21][30]. For the first few hours,
graze:

- Polifruit (common, grassy areas) → calories [21]
- Hydrobulb (near water) → hydration [21]
- Purplant (shaded rocks) → reduces toxicity [21]

Per [30]: "Hydration + Calories first. If those aren't stable, everything
else feels harder than it needs to be."

### Corporation Unlock Order

Bring all corporations to **Level 2 cheaply first** [25][29], then pursue the
following targets. Both TheGamer [14] and GameRant [25] agree on Moon Energy
L3 (Map) as first priority:

| Priority | Target | Why |
|---|---|---|
| 1 | Moon Energy Level 3 | Map — removes Fog of War [13][14][25] |
| 2 | Selenian Level 2 | Fabricator — secondary material processing [14][25] |
| 3 | Griffits Blue Level 2 | UPP-7 Reaper Pistol [13][15] |
| 4 | Clever Robotics Level 2 | Personal Storage (18 slots) [14][24] |
| 5 | Future Health Solutions Level 3 | Regeneration Chamber, Medtool [14] |
| 6 | Selenian Level 3 | +8 character inventory [24] |

Two sources disagree on whether the Recipe Station unlocks at Moon Energy L2
or earlier; [30] says L2, [10][13] imply L3 (with Map). The conservative
reading is that L2 unlocks the Recipe Station and L3 unlocks the Map — but
treat this as unverified.

### The Data Point Trap

The single most impactful early-game decision is **not spending Data Points
on corporation-level acceleration**. Per [20]:

> "Datapoints are essential for unlocking various recipes and materials, so
> spending them on leveling can be a waste. Make sure to save them and use
> them in the Recipe Station instead."

Use OCL commissions to level corporations. Reserve DP for Recipe Station
blueprint unlocks. The Corporate Terminal offers DP-for-contract-acceleration,
and this is a trap.

### Do-Not Rules for Early Game

Consolidated from [10][20][31]:

- **Do not analyze Meteor Hearts** — they are used for Base Cores and Pocket
  Base emergency shelters. Analyzing destroys progression-critical components.
- **Do not drop items on the ground as stockpile** — Rupture cycles wipe them [31]
- **Do not build circular rails/conveyors** — pull-based logistics creates
  infinite-pull loops that jam the whole network [31]
- **Do not upgrade the Base Core early** — it triggers escalating enemy waves
  from nearby monoliths and is irreversible [31]
- **Do not analyze Quartz ore** — it is not analyzable [10]

### Rupture Survival

The Rupture is a recurring stellar flare. Warning and countdown [13]:

> "You'll get a countdown for the wave, which only lasts for 15 seconds."

Consequences: instant death outside shelter, surface incineration. Strategic
framing: the **post-Rupture window is the best farming opportunity**, not
a recovery phase — see Section 5.

Discovery-agent consensus (not verified in a single fetched source): carry a
"Pocket Base" kit — 1 Meteor Heart + ~100 Basic Building Materials — to drop
an emergency Base Core + Habitat anywhere on the map. Materials refund on
deconstruction.

## 3. Mid-Game (~5–30 Hours)

### The Fabricator-Furnace-Electronics Spine

Once the Map is unlocked (Moon Energy L3), the mid-game loop is:

- Build out Fabricator (Selenian L2) → Furnace production chains
- Ship outputs via OCL to level Selenian and Clever Robotics
- Selenian L6 → Helium-3 Extractor (250 Basic Building Materials per unit) [23]
- Stockpile Helium-3 immediately, even though early uses are limited —
  **64 recipes depend on it** [23]; peaks at 3,469 units for Neutrino Missile [23]
- Griffits Blue L4 → Equipment Upgrade Station [26], which unlocks MAR-9
  Rifle (200 War Bonds), SLAMS-12 Shotgun (250 War Bonds), M175 MG (400 War
  Bonds) [15]

### Electronics — The Mid-to-Late Gate

Per [18]:

- Blueprint location: CRO "Grey Owl" ClayWood Research Outpost (north of
  Landing Site, east toward World Engine). Blue Chest on rooftop.
- Guarded by Exploders with Infestation Clouds — bring Infection Res Plasm
  (crafted from Prism Herbs [18])
- Recipe: 600 Synthetic Silicon + 200 Inductors + 200 Stators + 800 Data Points
- Station: Furnace with three connected Rails
- Downstream: enables Impellers, Batteries, Electromagnetic Coils; Selenian L8
  unlocks the Mega Press for mass-producing Nuzzles, Valves, Pumps [18]

### The Satellite POI Key-Card Chain

NerdSchalk [19] flags this as a soft-lock risk:

- Three key cards: **Dr. Ellis**, **Dr. Diaz**, **Eng. Perkins**
- Insert at central satellite building terminal (climb a ladder inside)
- Unlocks: Valve, Electromagnetic Coil, Turbine, Hardening Agent blueprints
- "Missing these will severely limit your options moving forward" [19]
- The terminal does not auto-unlock on key-card pickup — manual insertion
  required

Collect all three cards and complete the insertion as a mid-game milestone.
Guides that skip this create unnecessary late-game grind.

### The Production Chain Rebuild Problem

New tier unlocks can obsolete prior production layouts. Per Steam thread [34],
experienced players argue this is a playstyle mismatch:

- **Do not** try to build a single monolithic expanding base (Satisfactory-style)
- **Do** build distributed satellite production sites per material tier,
  connected via OCL routing [34]

## 4. Late Game (~30 Hours+)

Current terminal objective: activate the World Engine / Forgotten Engine,
unlock the tech teleporter [33]. No true endgame exists in the current EA
build [33]; a "definitive endgame" is a 1.0 target per roadmap references.

### Corporation Levels 9–11 Wall

The late-game wall is compositional: corporation final-tier exports demand
either massive bulk or ultra-advanced single items. Players who relied on
Data Points for early leveling hit this wall when exports become mandatory.
Key late-game unlocks per [18][22][24]:

- Selenian L8 — Mega Press
- Selenian L9 — Sulfur Extractor (must place post-Rupture when temperatures
  drop [22])
- Clever Robotics L8 — Storage Depot 1,600-unit upgrade
- Clever Robotics L9 — Personal Storage 42-slot upgrade
- Clever Robotics L12 — Multistorage (2,500 units)
- Clever Robotics L13 — Expandable Storage (1,600 per expansion)

### Goliath Farming (High-Yield DP Source)

Per [17]:

- Goliath location: Sulfur Pits northeast of Landing Zone
- Weak point: "small gap in the carapace" on back
- Kill rate: "two or three discharges with the LMG or the Assault Rifle"
- Reward: **Biological Sample worth 5,000 Data Points per kill** [17]

Per-kill DP yield vastly exceeds plant or salvage farming. Goliath farming
becomes the dominant DP strategy once combat gear permits reliable solo kills
(separate from swarm, take high ground).

### Documented Exploits

Three are widely discussed:

1. **Monolith turret cheese [36]:** surround the monolith with turrets fed by
   an ammo factory to trivialize base defense
2. **Save/reload cooling bypass [31]:** reloading restores cooling
3. **Double-jump + drone flying** (not verified in a fetched source;
   Counter-Discovery summary; developer reportedly acknowledged)

Each may be patched. Do not build a long-term strategy around these.

### Update-1 Combat Regression

Post-Update-1 Steam threads [35] document a significant reduction in turret
effectiveness and base cooler efficiency. Players report "24 gun towers" only
killing "6 of the 50 bugs" that approach; base coolers are "75% less
effective" [35]. Late-game base defense is in flux; guides recommending
specific turret counts should be re-verified against current performance.

## 5. Resource & Farming Strategy

### Data Point Spending Priority

One rule, unambiguous across [10][11][20]: **Recipe Station first, Corporate
Terminal second**. Do not accelerate contracts with DP until your recipe
unlocks are exhausted.

### Data Point Yields by Source

| Source | DP Yield | Availability |
|---|---|---|
| Goliath Biological Sample | 5,000 [17] | Sulfur Pits; repeatable |
| 5x Ignitium bundle | 2,000 [11] | Post-Rupture only; disintegrates |
| Broken technology (by quality) | 400–2,000 [11] | Fallen Drones, colonist bodies, ClayWood ruins |
| Glowcap (per piece) | 90 [10] | Underground caves post-wave only |
| Rare plants (Purplants, Serpent Root, Star Tears) | 20+ each [10] | Throughout map |
| Common plants (Polifruit, Hydrobulb, Prickler) | 5 each [10] | Throughout map |
| Meteor Hearts | **Do not analyze** [10][20] | Use for Base Cores / Pocket Base |
| Quartz ore | Not analyzable [10] | — |

### Post-Rupture Window — Primary Farming Opportunity

The highest-yield DP sources are post-Rupture-only: Ignitium [11], Glowcap
[10], and Oxallop [21]. Sulfur extraction also requires post-Rupture placement
[22]. Structure play around this:

- Set OCL commissions before the Rupture warning
- Shelter in a Habitat during the 15-second countdown
- Emerge immediately post-Rupture to collect Ignitium (orange horizon glow,
  ground smoke signal) [11]
- Visit underground caves for Glowcap (90 DP each) [10]
- Place Sulfur Extractors on Sulfur deposits in this window [22]

### Ore Progression

| Ore | Phase | Gate | Key Quote |
|---|---|---|---|
| Wolfram | Early | None | Tutorial [22] |
| Titanium | Early | None | Tutorial [22] |
| Calcium | Early/Mid | None (Excavator required for veins) | "last ore you'll be able to mine with the Excavator" [22] |
| Helium-3 | Mid | Selenian L6 | 64 recipes depend on it [23] |
| Sulfur | Late | Selenian L9 | Must place extractor post-Rupture [22] |

**Sulphur scarcity is contested.** Counter-Discovery surfaces a dispute: one
50+ hour player [36] described an end-game Sulphur bottleneck, but a second
community voice countered with "47 sulphur nodes in current map" — framing
the complaint as a base-layout and routing problem rather than a supply-cap
problem. Readers planning late-game Sulphur chains should place extractors
across multiple deposits rather than relying on a single site. See
[Mid-Late Progression](references/mid-late-progression.md) for detail.

### Inventory & Storage Upgrades

From [24]:

- Character inventory: 24 → 56 slots via Selenian L3 (+8), Future Health
  Solutions L7, Griffits Blue L8, Moon Energy L11
- Personal Storage (Clever Robotics L2 → L9): 18 → 42 slots
- Storage Depot (Clever Robotics L3 → L8): 400 → 1,600 units
- Multistorage (Clever Robotics L12): 2,500 units of different items
- Expandable Storage (Clever Robotics L13): 1,600 per expansion

## 6. Combat

Combat is **not a primary progression vector** — NeonLights reviewer [27]:
combat is "functional" and "primarily monotony relief." Optimization is
therefore about minimum-viable combat capability rather than a deep meta.

### Weapons

| Weapon | Unlock | Cost |
|---|---|---|
| UPP-7 Reaper Pistol | Griffits Blue L2 | Starter / 2 War Bonds alt [15] |
| MAR-9 Phantom Rifle | Equipment Upgrade Station | 200 War Bonds [15] |
| SLAMS-12 Shotgun | Equipment Upgrade Station | 250 War Bonds [15] |
| M175 Grim Machine Gun | Equipment Upgrade Station | 400 War Bonds [15] |
| Grenades | Griffits Blue L3 | — [15] |

UPP-7 Pistol **cannot be modded** [26]. Other weapons take 4 mod slots (barrel
50–130, magazine 60–120, stock 50–110, sight 55–90 War Bonds — rifle only) [15][26].

Equipment Upgrade Station unlock at **Griffits Blue L4** [26] — requires OCL
shipment of Titanium Sheets or Wolfram Plates.

### Enemy Handling

From [16]:

- Slasher → pistol sustained fire on red mouth
- Young Slasher → Harvester Tool (save ammo)
- Exploder → shoot sac from distance
- Flinger → close the distance under pistol fire
- Spitter → dodge sac, shoot from range

Goliath (the only documented boss, Sulfur Pits NE of spawn): weak point on
back, needs high ground to access, 2–3 MG/Rifle bursts [17].

### Base Defense Under Update 1

Turret effectiveness and base cooler efficiency were reduced in Update 1 [35].
Pre-April-9 guides recommending specific turret counts ("8 heavy turrets
handle waves 1–2" per Discovery summary) should not be trusted without
re-verification. A Hotfix 0.2.2 or later is plausible if the regression
persists.

## 7. What's Likely to Change (Volatility Flags)

Per [Patch Volatility](references/patch-volatility.md):

- **Stale pre-April-9 guidance:** Scanner and Pressure Tank acquisition paths,
  Quartz Building Material usage, corporation level state (reset), recipe
  ingredient counts (Nanofibre, Pressure Tank, Condenser, Superconductor).
- **Actively rebalancing:** Base defense (turret targeting, cooler efficiency)
  changed meaningfully in Update 1; follow-up adjustments are plausible.
- **Planned 1.0 additions per roadmap references:** Frost Wave hazard,
  additional biome, "definitive endgame," achievements, skill cap raised to 100 [9].

Any recommendation in this document may become stale at the next major patch.
Re-verify against patch notes [2] after subsequent updates.

## 8. Contradictions and Open Questions

Claims in fetched sources that do not fully agree or are not verified:

- **Moon Energy Level 2 vs. Level 3 for Map unlock:** [13][14][25] say L3;
  [30] implies the Recipe Station ties to L2. Conservative reading: L2
  unlocks Recipe Station, L3 unlocks Map — but single-source.
- **Pocket Base kit material count** (100 Basic Building Materials): multiple
  Discovery snippets, not verified in a single fetched source.
- **Player count decline** (42,864 → 7,331) [8] — source INACCESSIBLE.
- **Screen Hype and The Review Geek reviews** [38][39] — INACCESSIBLE. Single
  critic review ([27], 7.0/10) is the only fetched external rating.
- **Quartz respawn mechanic** — contested in community threads; "community
  split on navigation vs. supply problem" per Counter-Discovery summary.
- **Corporation-level persistence across saves** [37] — whether intended or
  bug is not addressed in any fetched source.

## 9. Reflection

A single reflection pass on this draft:

- **Confidence stated vs. warranted:** The corporation-unlock table in Section
  2 is drawn from multiple corroborating sources and should be trusted. The
  "Moon Energy L3 = Map" claim is strongly supported [13][14][25]. The Pocket
  Base kit specifics are less supported and are flagged accordingly.
- **Contradictions surfaced vs. suppressed:** Moon Energy L2/L3 ambiguity is
  surfaced with flag. The "production rebuild" debate (design flaw vs.
  playstyle mismatch) is explicitly presented as contested rather than
  resolved. Combat shallowness is acknowledged up front rather than papered
  over.
- **Cross-source claims:** The Data-Point-priority rule (Recipe Station first)
  is backed by [10][11][20] — strong multi-source basis. The post-Rupture
  window claim is backed by [10][11][21][22] — strong. Goliath farming yield
  (5,000 DP) is single-source [17] but specific and falsifiable.
- **Dismissed alternatives:** The "optimize combat builds" framing is
  explicitly dismissed based on [27]; Counter-Discovery does not contradict
  this.
