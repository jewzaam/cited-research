# Combat, Build & Loadout Meta

What combat optimization looks like in current EA. See [citations](../citations.md) for sources.

## Combat's Role in Progression

Combat in StarRupture is **not the primary progression vector**. Per NeonLights
Media review [27], combat is "functional" with "satisfying weapon feedback"
but serves "primarily as monotony relief rather than a major feature." Counter-
Discovery surfaced multiple Steam threads characterizing combat as "shallow,"
"clunky," or "boring" (e.g., [45] calls the game "Temu Satisfactory"). This
dimension is therefore scoped to the essential combat decisions that affect
progression, not a speedrunner-grade meta.

## Weapons

From [15]:

| Weapon | Unlock | Cost | Role |
|---|---|---|---|
| UPP-7 Reaper Pistol | Griffits Blue L2 contract | 2 War Bonds (alt) | Starter; semi-auto; mid-range |
| MAR-9 Phantom Assault Rifle | Equipment Upgrade Station | 200 War Bonds | Mid-range standard |
| SLAMS-12 Shotgun | Equipment Upgrade Station | 250 War Bonds | Close quarters; high recoil |
| M175 Grim Machine Gun | Equipment Upgrade Station | 400 War Bonds | Rapid-fire; long to mid-range |
| Grenades | Griffits Blue L3 contract | — | Area damage |
| Harvester Tool | — | — | Defensive utility against small Slashers, Exploders [15] |

The UPP-7 Pistol **cannot be modded** [26]. The other three weapons accept
modifications.

Equipment Upgrade Station requires **Griffits Blue Level 4** [26]. To reach
it: build production infrastructure (Supply Line, Smelter, Fabricator),
fabricate Titanium Sheets or Wolfram Plates, ship via OCL to earn reputation,
then claim the Station reward at the Corporate Terminal with 120 Basic
Building Materials [26].

### Weapon Mods

Four slot categories per [15][26]:

- **Barrel:** 50–130 War Bonds — range, damage, fire rate
- **Magazine:** 60–120 War Bonds — capacity, ammo type
- **Stock:** 50–110 War Bonds — recoil, handling
- **Sight / Optics:** 55–90 War Bonds (rifle only) — aiming

War Bond sources: corporation-level rewards (notably Griffits Blue), secret
chests, fallen colonists [26].

**Contradiction with the starrupture.wiki.gg Weapons page [50]:** the wiki
prices MAR-9 mods in **Basic Building Materials** (~10 BBM each), not War
Bonds, and lists only four weapons total (MAR-9, UPP-7, Mining Laser, Grenade)
rather than the six documented in [15]. The wiki page appears stale or to
reflect an earlier playtest build — [15] and [26] agree on War Bond pricing
and the full roster (UPP-7, MAR-9, SLAMS-12, M175, grenades, Harvester). This
research treats [15] and [26] as current; [50] is flagged in citations.md as
INACCURATE for cross-verification purposes. If Creepy Jar has shifted mod
pricing between currencies in a later patch, [15] may also become stale.

Additional minor discrepancy: [26] lists the mod cost floor as "Free" for
Sights, Magazines, and Stocks, while [15] reports 50–55 War Bond floors.
"Free" likely refers to baseline default equipment while priced mods are
paid upgrades.

### Ammunition

Crafted at Basic Item Printer [15]:

- Pistol: Basic Building Material
- Standard (rifle): Material + Wolfram Powder
- Shotgun: Material + Calcium Powder
- Heavy (MG): Material + Titanium Rod

## Enemies (Vermin)

From [16]:

| Enemy | Description | Counter |
|---|---|---|
| Flinger | Ranged; catapults burning green matter | Pistol, close the distance |
| Exploder | Blue creatures; sacs detonate to disable shields | Shoot sac from distance |
| Slasher | Large black; most dangerous; aggressive | Sustained pistol fire; weak point = red mouth area |
| Young Slasher | Small grey variants | Harvester Tool (ammo-efficient) |
| Spitter | Large green sacs; toxic spit | Pistol or Harvester; dodge sac |

Per [16] comment: additional enemy types may exist beyond these five.

### Goliath (the only documented boss)

From [17]:

- **Location:** Sulfur Pits, "a bit Northeast from the Landing Zone"
- **Weak point:** "small gap in the carapace" on back
- **Kill rate:** "two or three discharges with the LMG or the Assault Rifle"
- **Attacks:** Defensive Mode (invulnerable to front fire), Charge, Pincer,
  Shockwave (straight-line ground pound)
- **Solo strategy:** "Don't stop running until the Goliath is separated from
  its swarm" + "Take the high ground"
- **Reward:** Biological Sample worth 5,000 Data Points per kill

## Base Defense

### Structures

Two turret tiers documented via Discovery (starrupture.tools):
- **Auto Turret (Tier 1)**
- **Defense Tower (Tier 2)**

Turrets are automated but require power and ammunition supply (not
self-resupplying). Placement meta from Discovery: elevated positions for
line-of-sight, face nearest Monolith (wave spawn source), bottleneck choke
approaches.

### Wave Mechanics

Per Discovery summaries and [31]:

- Wave strength scales with **Base Core level** (irreversibly increasing each
  upgrade) [31]
- Monoliths appear to be the spawn source; Counter-Discovery documents
  players exploiting this with the monolith-turret cheese [36]
- Enemies can selectively target power plants and disable turret grids
  (Counter-Discovery summary of [36])

### Base Defense Regression (Update 1, April 9, 2026)

Per [35]:

- 24 gun towers in a 3-layered defense killing "6 of the 50 bugs that come
  running at them now" post-Update 1
- Base coolers "made 75% less effective" [35]
- Turrets deprioritize small vermin, which then reach structures
- Community framing: regression, not balance pass

No developer response in the thread [35].

### No Walls (Contested)

One Discovery source (review) claimed no defensive walls or fences exist,
with terrain substituting. This was not verified in a fetched source and
appears in only one Discovery snippet. Treat as unconfirmed.

## Build Diversity

Combat "builds" in StarRupture are loadout choices, not character builds:

- Two active weapon slots
- LEM Augment Slots (shared across combat/survival/movement) — current EA
  caps at 3 per skill; see [Progression Systems](progression-systems-inventory.md) [9]
- No character classes, skill respec, or weapon-specialization trees
  documented in fetched sources
- Per [31], LEMs stack additively — multiple identical LEMs compound their
  effects (e.g., shield capacity)

Community "best loadout" consensus: MAR-9 Assault Rifle + grenades for
general purpose; SLAMS-12 Shotgun specifically for Slashers at close range.
M175 MG for sustained-fire scenarios and Goliath.

## PvE / PvP / Co-op

- PvE only; no PvP documented in fetched sources
- Co-op up to 4 players, host-tied shared world and progression [49]
- No public matchmaking — invite/direct join only [49]
- Solo fully supported

## Min-Max / Multiplayer Callouts

- **Min-max:** Goliath farming (5,000 DP per kill [17]) is the highest-yield
  combat investment. Requires MAR-9 or M175, ability to separate the boss from
  its swarm, and access to the Sulfur Pits NE of spawn.
- **Multiplayer:** No meaningful build divergence documented; party handles
  Goliath more safely (one distracts, others hit back weak point per [17]).

## Update-1 Combat Staleness Flags

- Pre-Update-1 turret-only defense guides may be wrong post-April 9 given the
  cooler/targeting changes [35]
- Base core upgrade advice from pre-Update-1 is unchanged mechanically but
  the consequence is now more punishing due to cooler nerfs [35]
- Enemy targeting behavior changed — pre-patch "turrets handle swarms" advice
  no longer holds at the reported rate [35]

## Gaps & Limitations

- Weapon damage numbers, DPS, headshot multipliers — none documented in
  fetched sources
- Full enemy roster may exceed the five documented types [16]
- No data on exact wave counts per Rupture cycle or how Core Level scales
  wave size numerically
