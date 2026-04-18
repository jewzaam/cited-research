# Progression Systems Inventory

What actually gates progress. See [citations](../citations.md) for sources.

## 1. Character Skills

StarRupture uses **three independent skill tracks**, not a single character level [9]:

| Skill | Earned By | Current EA Cap | Planned 1.0 Cap |
|---|---|---|---|
| Combat | Eliminating Vermin, surviving base raids | 45 | 100 |
| Survival | Collecting plants, mining meteorites/Ignitium, surviving Rupture Waves | 45 | 100 |
| Movement | Moving, exploring, running, climbing, sliding, jumping | 45 | 100 |

Source: [9].

### LEM Augment Slots

The progression reward for skill levels is LEM Augment Slot unlocks. Slots
unlock at levels **10, 25 (20 for Combat), 40 (35 for Combat), 65, 85, and 100** [9].

- **Current EA (cap 45):** 3 augment slots per skill → 9 total
- **Planned 1.0 (cap 100):** 6 augment slots per skill → 18 total

LEMs stack additively — multiple identical LEMs combine their bonuses
(e.g., multiple max-shield LEMs increase total shield capacity cumulatively) [31].

### Respec & Classes

No respec mechanism for LEM slots was documented in fetched sources. Character
selection at spawn is **cosmetic only**; per [13], "These characters bring
different dialogues to each situation" but share all blueprints/abilities.
Character can be swapped any time at a Regeneration Chamber (default in ship,
or craftable with 100 Basic Building Materials) [13].

## 2. Tech Tree

The game has a discrete tech tree unlocked by spending Data Points [28].
Discovery agents documented 19+ nodes including basic tools, smelting, wind
power, map access, a Vehicle Technology branch (Rover, Transport Vehicle,
Vehicle Bay), and later quantum/teleportation systems. Nodes chain by
prerequisite. Source [28] is the wiki tools site; the page was referenced by
Discovery but not fetched in the main thread — specific DP costs and node
prerequisites are not verified here.

## 3. Corporations (Faction / Reputation Analog)

**Five corporations**, each with its own reputation level and unlock rewards [14]:

| Corporation | Focus | Level Cap |
|---|---|---|
| Future Health Solutions | Character and habitat upgrades | 11 |
| Selenian Corporation | Factory structures and ore production | 11 |
| Griffits Blue Corporation | Combat and base defense | 11 |
| Moon Energy Corporation | Power generation and exploration tools | 11 |
| Clever Robotics | Storage and item transfer infrastructure | 13 |

Source: [14]. Four cap at 11; Clever Robotics uniquely caps at 13.

### How Corporation Leveling Works

Two methods [14][11][29]:

- **Export materials via Orbital Cargo Launcher (OCL):** The sustainable method
  — produce items the corporation wants and ship them via the Orbital Cargo
  Launcher. Requires production infrastructure. [14][29]
- **Spend Data Points directly:** The Corporate Terminal lets you spend Data
  Points to accelerate contracts. Described as "also need[ed]...to unlock
  different recipes" — doing this is a documented progression trap; see
  [Economy](resource-economy.md). [14][20]

### Key Corporation-Level Unlocks

Drawn from [13][14][18][22][23][24][25][26][29][30]. **Update 1 (April 9, 2026)
reset all corporation levels to Level 1** and converted prior progress to Data
Points (per Counter-Discovery agent sourcing Patchbot [2] plus community forums
at [42]) — the unlock map itself appears unchanged from these sources, but any
character's progression state was reset.

Early (Level 1–3):
- Moon Energy L3 — Map (Fog of War removal) [13][14][25]
- Selenian L2 — Fabricator [14][25][29]
- Griffits Blue L2 — UPP-7 Reaper Pistol [13][14][15]
- Clever Robotics L2 — Personal Storage (18 slots) [14][24][25]
- Selenian L3 — +8 character inventory slots [24]
- Future Health Solutions L3 — Regeneration Chamber, Medtool [14]
- Griffits Blue L3 — Grenades [15]
- Clever Robotics L3 — Storage Depot (400 units) [24]

Mid (Level 4–6):
- Griffits Blue L4 — Equipment Upgrade Station (weapon mods) [26]
- Selenian L6 — Helium-3 Extractor [22][23]
- Future Health Solutions L6 — Food Station [20][29]

Late (Level 7–11):
- Future Health Solutions L7 — character inventory upgrade [24]
- Griffits Blue L8 — character inventory upgrade [24]
- Selenian L8 — Mega Press (mass-produces Nuzzles, Valves, Pumps) [18]
- Clever Robotics L8 — Storage Depot upgrade (1,600 units) [24]
- Clever Robotics L9 — Personal Storage upgrade (42 slots) [24]
- Selenian L9 — Sulfur Extractor [22]
- Moon Energy L11 — character inventory upgrade [24]

Endgame (Clever Robotics specific):
- Clever Robotics L12 — Multistorage (2,500 units) [24]
- Clever Robotics L13 — Expandable Storage (1,600 per expansion) [24]

### Corporation-Level Persistence Across Saves

A Steam Community guide [37] reports that corporation levels persist across
saves, meaning a second playthrough retains unlocks from the first. Whether
this is intended design or an oversight is not addressed in any fetched source.
Treat this as a strategic option for second runs but flag as uncertain.

## 4. Currencies

**Two documented currencies** [10][11][20][26]:

| Currency | Primary Sources | Primary Spends |
|---|---|---|
| Data Points | Analyzing Station (plants, Ignitium, salvage tech, biological samples); NOT from ore | Recipe Station (recipe unlocks), Corporate Terminal (contract acceleration) |
| War Bonds | Corporation level rewards (notably Griffits Blue), secret chests, fallen colonists | Weapons (UPP-7 free unlock, MAR-9 200, SLAMS-12 250, M175 400), weapon mods (50–130 per mod), Equipment Upgrade Station |

Data Points are the rarer and more progression-critical of the two [11][20].
No third (premium/hard) currency was documented in any fetched source.
War Bonds are sometimes referenced in third-party player-trading contexts, but
no in-game NPC vendor was confirmed in fetched sources.

## 5. Crafting Stations

**Tier chain** (derived from [18][22][23] plus Discovery manifests):

1. **Smelter** — raw ore → ingots/bars (Titanium, Wolfram, Calcium) [22]
2. **Fabricator** (Selenian L2) — secondary processing: Sheets, Plates, Beams,
   Rods, Wires, Rotors, Tubes [25][29]
3. **Furnace** — high-temperature advanced materials (Glass requires Helium-3;
   Wolfram Powder, Calcium Powder, Inductors, Electronics) [18][23]
4. **Recipe Station** — unlocks new blueprints for Data Points + materials [10][20]
5. **Analyzing Station** — converts resources into Data Points [10][11]
6. **Orbital Cargo Launcher (OCL)** — ships production to corporations [12][14]

Advanced and Update-1-added stations: **Mega Press** (Selenian L8), **Recycler**,
**Development Station** (habitat, enables v.2 building unlocks), **Oil Extractor**,
**Laser Drill**, **Refinery**, **Pyro Forge**, **Facturer**, **Chemical
Generator**, **Radial Rail Connector** [4].

## 6. Recipe-Unlock Paths

Two paths [10][20]:

- **Recipe Station** — the primary mechanic. Spend Data Points plus raw
  materials to unlock a recipe permanently.
- **Blueprints found in the world** — Blue Chests at Abandoned Settlements and
  specific POIs (e.g., Electronics at "Grey Owl" ClayWood Research Outpost [18];
  Satellite POI key-card chain unlocks Valve, Electromagnetic Coil, Turbine,
  Hardening Agent [19]).

**Update 1 shifted some blueprints** from world-exploration to Recipe Station
acquisition — specifically **Scanner** (per [2]) and **Pressure Tank** (per [32]).
Old guides describing dungeon exploration for these are stale. See
[Patch Volatility](patch-volatility.md).

## 7. Story / Quest Gating

Minimal. A story exists (broadly framed as "stop the star from exploding" per
Discovery agent snippet; not verified in a fetched source) but progression is
gated primarily by corporation levels, blueprint acquisition, and Rupture
cycle timing — not story quest completion. Current terminal objective per
community consensus [33] is activating the World Engine / Forgotten Engine
and unlocking the tech teleporter.

## 8. Building-Tier Progression

Introduced by Update 1 (April 9, 2026) [4]:

- **v.2 tier buildings:** Compounder v.2, Fabricator v.2, Furnace v.2, Ore
  Excavator v.2, Orbital Cargo Launcher v.2, Constructorizer v.2
- **Development Station** (habitat) is the new gating mechanism for v.2
  unlocks

Pre-Update 1 guides that do not reference the Development Station are
incomplete for v.2 progression. See [Patch Volatility](patch-volatility.md).

## Contradictions & Open Questions

- **Moon Energy Level 2 vs. Level 3 for Map unlock:** Three-way contradiction
  in fetched sources:
  - [13], [14], [25] state **Level 3** unlocks the Map
  - [12] states **Level 2** unlocks the Map (direct contradiction)
  - [30] states the Recipe Station is "typically linked to Moon Energy
    Corporation Level 2"
  - [11] states Recipe Station requires **Level 1** Moon Energy

  The most likely reconciliation is that Moon Energy L1 or L2 unlocks the
  Recipe Station and L3 unlocks the Map — but no single fetched source states
  both cleanly. [12]'s Level-2-for-Map claim is the outlier against three
  other sources and should be treated as likely in error. The Recipe Station
  level itself (L1 vs. L2) is unresolved in available sources. Flag when citing.
- **Corporation L8 inventory unlock for Griffits Blue** (per [24]) is listed
  separately from the Equipment Upgrade Station at L4 (per [26]) — these are
  distinct unlocks at different levels within the same corporation.
- **Corporation-level persistence across saves** [37] — intended or bug? No
  developer statement found.
- **Tech tree specifics** — specific DP costs and prerequisite chains for the
  19+ tech nodes were not fetched in the main thread; [28] would resolve but
  was not read directly.
