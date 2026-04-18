# Resource & Economy Optimization

Currencies, crafting materials, farming, hoarding vs. spending. See
[citations](../citations.md) for sources.

## Currency Overview

| Currency | Earn | Spend |
|---|---|---|
| Data Points | Analyzing Station (plants, Ignitium, salvage, biological samples); NOT ore | Recipe Station (recipe unlocks), Corporate Terminal (contract acceleration) |
| War Bonds | Corporation rewards (notably Griffits Blue), secret chests, fallen colonists | Weapons and weapon mods at Equipment Upgrade Station |

Sources: [10][11][20][26].

**Spending priority for Data Points is unambiguous in fetched sources:**
research (Recipe Station) first, contract acceleration second [10][11][20].

> "Datapoints are essential for unlocking various recipes and materials, so
> spending them on leveling can be a waste. Make sure to save them and use
> them in the Recipe Station instead." [20]

## Data Points Yield Table

| Source | DP Yield | Notes |
|---|---|---|
| Biological Sample (Goliath drop) | 5,000 [17] | Highest per-kill source documented |
| 5x Ignitium bundle | 2,000 [11] | Post-Rupture only; disintegrates |
| Broken Tech (Fallen Drones, colonist remains, ClayWood ruins) | 400–2,000 [11] | Quality-dependent |
| Glowcap (per piece) | 90 [10] | Underground caves, post-wave only; "didn't respawn after the wave" [21] |
| Rare plants (Purplants, Serpent Root, Star Tears) | 20+ [10] | Each |
| Common plants (Polifruit, Hydrobulb, Prickler) | 5 [10] | Each |
| Spider sacs | bonus (unspecified) [10] | |
| Artifacts (abandoned bases) | hundreds to thousands [10] | Highly variable |
| Meteor Hearts | — | **Do not analyze** [10][20]; needed for Base Cores and Pocket Base |
| Quartz ore | not analyzable [10] | |

### Goliath Farming (Counter-Discovery / Min-Max)

Goliath drops a 5,000 DP Biological Sample [17]. This is by far the highest
single-kill DP yield. Once the player has LMG or Assault Rifle and can reliably
separate the boss from its swarm (high ground recommended [17]), Goliath
farming dominates other DP sources.

## Post-Rupture Farming Window

The post-Rupture window is the **primary farming opportunity**, not a "wait
for calm" period [10][11][21][22]:

- **Ignitium** spawns only post-Rupture [11]; disintegrates quickly
- **Glowcap** only harvestable in underground caves post-wave [10]
- **Oxallop** only harvestable "between the barren times right after the wave
  and before the planet regenerates fully" [21]
- **Sulfur extractors** must be placed "just after a rupture" [22]

Practical routine: set OCL commissions before the Rupture, survive in shelter,
then emerge to farm Ignitium and cave Glowcap during the opening of the
post-Rupture window.

## Plant Rarity & Farming Locations

From [21]:

| Plant | Rarity | Primary Location |
|---|---|---|
| Polifruit | Common | "everywhere across Arcadia-7" with grass |
| Hydrobulb | Common | Near water; best spot "far right of the map just below the Forgotten Engine" |
| Prickler | Common | Red flower fields; NE of Orbital Lander, SE section, south of red lake |
| Grubbler | Common | Bent giant trees; SE and NE sections |
| Sulheart | Common (difficult) | Sulfur deposits (yellow map areas); respawn during regeneration only |
| Serpent Root | Uncommon | Barren map areas |
| Star Tear | Rare | On small rocks across planet |
| Purplant | Rare | Rocks under cliffs, shaded |
| Glowcap | Rare/Limited | Underground caves; post-wave window only |
| Oxallop | Rare/Limited | Water beds; narrow post-wave harvest window |
| Prism Herb | Rarest | SE pools; "rarest resource in the game" |

## Ore Progression

From [22]:

| Ore | Phase | Gate | Notes |
|---|---|---|---|
| Wolfram | Early | None (tutorial) | North, northeast of spawn; far north |
| Titanium | Early | None (tutorial) | Gray circles on map; smaller veins than Wolfram |
| Calcium | Early/Mid | None (ground-minable); Excavator for large veins | "last ore you'll be able to mine with the Excavator" |
| Helium-3 | Mid | Selenian L6 | Purple geysers; 64 recipes depend on it [23] |
| Sulfur | Late | Selenian L9 | Yellow map areas; post-Rupture placement required |

### Helium-3 Demand

Per [23]: 64 recipes require Helium-3. Highest demands:

- Neutrino Missile: **3,469 Helium-3** [23]
- Neutrino Bomb: 2,000 Helium-3 [23]
- Organ Producer: 2,388 Helium-3 [23]

Implication: stockpile Helium-3 as soon as the extractor unlocks at Selenian
L6, even though early uses are limited.

## Inventory & Storage

From [24]:

- Character inventory: 24 → 56 slots across multiple corporation unlocks
  (Selenian L3, Future Health Solutions L7, Griffits Blue L8, Moon Energy L11)
- Personal Storage (Clever Robotics): 18 slots at L2 → 42 slots at L9
- Storage Depot (Clever Robotics): 400 units at L3 → 1,600 units at L8
- Multistorage (Clever Robotics L12): 2,500 units of different items
- Expandable Storage (Clever Robotics L13): 1,600 units per expansion

## Do-Not / Do Rules

Consolidated from [10][20][31]:

**Do not:**

- Analyze Meteor Hearts (preserve for Base Cores) [10][20]
- Drop items on the ground as stockpile (Rupture cycles wipe them) [31]
- Spend Data Points on corporation leveling before exhausting Recipe Station
  unlocks [20]
- Build circular routing in rails/conveyors (pull-based logistics creates
  infinite loops that jam chains) [31]
- Assume all identical-looking resource nodes yield the same output — hidden
  quality tiers cause 2x to 4x+ output variance; verify extractor output
  before scaling [31]

**Do:**

- Always set a Commission on an OCL before leaving base [12]
- Split 6,400-point commissions across multiple OCLs to parallelize [20]
- Stockpile Helium-3 once Selenian L6 unlocks the Extractor [23]
- Save Ignitium farming for the post-Rupture window [11]

## Vendor / Trade

No in-game NPC vendor was confirmed in any fetched source. The economy runs
through Analysis Station (resource → DP), Recipe Station (DP → recipes),
Corporate Terminal (contracts), and OCL (materials → corp reputation). Third-
party player-trading platforms sometimes reference War Bonds, but this is
outside the game's official economy.

## Update-1 Economy Changes (Stale-Advice Flags)

Per [2][4][32] and Counter-Discovery summaries:

- **Quartz Building Material deprecated as a build currency.** Discovery agent
  summary: all Quartz spent on buildings now returned to inventory as Quartz
  Ore; existing Quartz Building Materials can be recycled (without loss) into
  Quartz Ore via the Recycler.
- **Recipe changes in Update 1 / PTB Hotfix 1:**
  - Nanofibre: Wolfram Wire added as third component (cost increase)
  - Pressure Tank: Titanium Housing removed (cost reduction)
  - Condenser: Synthetic Resin removed (cost reduction)
  - Superconductor: Ceramics replaced by Synthetic Resin (upstream change)
- **Scanner blueprint:** unlock moved from world-find to Recipe Station [2][32]
- **Pressure Tank blueprint:** unlock moved from Forgotten Engine dungeon to
  Recipe Station [32]
- **Power Generator, Zipline, Drone Rails, Teleport build costs** adjusted in
  PTB Hotfix 1 [2]
- **Energy consumption and Base Core cooling** adjusted for v.2 buildings [2]

See [Patch Volatility](patch-volatility.md) for full detail.

## Gaps & Limitations

- Ignitium's post-Rupture despawn timer (commonly cited as ~1 hour in-game
  time) came from a Discovery snippet; not verified in a fetched source.
- Sulfur's specific late-game recipe dependencies were not enumerated in
  fetched sources.
- No drop-rate percentages were recovered; community spreadsheets (if they
  exist) were not indexed.
