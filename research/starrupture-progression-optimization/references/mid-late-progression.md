# Mid-to-Late Progression & Bottlenecks

Where players stall and how the community solves it. See [citations](../citations.md) for sources.

## Current Terminal Objective

Per community consensus on the Steam forums [33], the current terminal goal
in Early Access is **activating the World Engine (also referred to as Forgotten
Engine) and unlocking the tech teleporter**:

> "The end goal at the moment is getting the world engine up and going and
> getting the tech teleporter which will come in handy for when the map
> opens up." [33]

No formal "endgame" exists in the current EA build. A forum response
paraphrased as: "End Game is on the Roadmap for v1.0... Can't expect to have
everything in EA" [33].

## The Satellite POI Key-Card Chain (Critical Mid-to-Late Gate)

NerdSchalk [19] documents a gate that is easy to miss and can soft-lock
progression:

- Three key cards required — **Dr. Ellis**, **Dr. Diaz**, **Eng. Perkins**
- Inserted at a central satellite building terminal (climb a ladder inside)
- Unlocks four blueprints: **Valve**, **Electromagnetic Coil**, **Turbine**,
  **Hardening Agent**
- Quote: "Missing these will severely limit your options moving forward"

Per [19], the terminal does not auto-unlock on key-card collection — players
must manually insert all three and "thoroughly loot the room."

## Electronics — The Mid-to-Late Transition Gate

Electronics is the named chokepoint material for entering the late-game loop [18]:

- **Blueprint location:** CRO "Grey Owl" ClayWood's Research Outpost — north of
  Landing Site, east toward World Engine; Blue Chest on rooftop; guarded by
  Exploders with Infestation Clouds [18]
- **Countermeasure for the fight:** Infection Res Plasm crafted from Prism Herbs [18]
- **Crafting recipe:** 600 Synthetic Silicon + 200 Inductors + 200 Stators + 800
  Data Points [18] (note: source writes "Syntheric Silicon" — likely the in-game
  spelling is "Synthetic Silicon")
- **Crafting station:** Furnace with three connected Rails feeding inputs [18]
- **Downstream unlocks:** Impellers, Batteries, Electromagnetic Coils,
  transitions to Selenian Rank 8 which unlocks the **Mega Press** for
  mass-producing Nuzzles, Valves, Pumps [18]

## The Corporation Level 9–11 Wall

Per Counter-Discovery agent sourcing the Steam Community corp guide [37] and
50+ hour player thread [36]:

- Levels 9–11 mark a complexity spike: final exports demand either massive
  bulk quantities or ultra-advanced single items requiring full multi-tier
  production chains
- The Orbital Cargo Launcher becomes essential at this stage
- Players who relied on Data Points to level early corporations hit a hard
  wall when the cost transitions to export-based leveling [20]

## Key Late-Game Unlocks

- **Selenian L8** — Mega Press (endgame mass production) [18]
- **Selenian L9** — Sulfur Extractor (required for sulfur-based late recipes) [22]
- **Selenian L9** Sulfur's "corrosive air that will damage you" requires placing
  extractors "just after a rupture" [22]
- **Clever Robotics L8** — Storage Depot 1,600-unit upgrade [24]
- **Clever Robotics L9** — Personal Storage 42-slot upgrade [24]
- **Clever Robotics L12** — Multistorage (2,500 units) [24]
- **Clever Robotics L13** — Expandable Storage (1,600 per expansion) [24]

## Production Chain Rebuilds — The Structural Mid-Game Grind

A recurring complaint in Counter-Discovery [34][45]: unlocking new tiers
obsoletes prior production layouts, driving players to repeatedly demolish
and rebuild. Experienced players in [34] (Dexi, Malignance) argue this is a
playstyle mismatch rather than a design flaw:

- **Not recommended:** one monolithic base expanded in place (Satisfactory-style)
- **Recommended:** distributed "satellite" production sites per material tier,
  connected by OCL routing [34]

This is a contested claim — see [Patch Volatility](patch-volatility.md) for
Update 1's building rebalance. Update 1's v.2 buildings and Development Station
partially address this by introducing formal building upgrades rather than
replacement.

## Late-Game Performance Degradation

Per Counter-Discovery sourcing Steam threads, late-game factory scale causes
performance degradation:

> "FPS degrades to 8–13 on capable hardware during late-game production;
> players leave game running overnight to accumulate materials." — from
> Counter-Discovery agent summary of [Steam thread 832738775777145975]

This effectively functions as an additional progression wall: the game
becomes unplayable at certain scales regardless of mechanical progress. Source
specifics (Ryzen 7 5700X + RTX 5070Ti baseline, 8–13 FPS) came from
Counter-Discovery agent summarization and were not verified in a directly-fetched
thread.

## Documented Exploits and Cheese

Three patterns appear in fetched sources:

1. **Monolith turret cheese** [36]: surround the monolith with turrets fed by
   an ammo factory to trivialize base defense — "i just surrounded the
   monolith in turrets and have them fed by an ammo factory /gg"
2. **Save/reload cooling bypass** [31]: reloading restores cooling without
   waiting; described as "likely faces patching in future updates"
3. **Double-jump + drone flying exploit** (Counter-Discovery summary, not
   verified in a fetched source): allows bypassing map traversal; developer
   reportedly acknowledged, patch anticipated

Players generally frame these as unintended but accepted.

## Stuck Points Reported by the Community

Per Counter-Discovery agent summaries of Steam forum threads:

- ~15–20 hours: casual/exploration players hit a content wall
- ~50–70 hours: factory-focused players report content fatigue
- Specific material bottlenecks named: Sulphur (disputed — 47 nodes
  documented on map [36]), Quartz (contested; respawns in outlying caves at
  7–10 crystals each per cycle), Helium-3 (scarcity relieves once extractor
  unlocks at Selenian L6)

## Boss Content

Only one named boss-equivalent encounter: **Goliath**, found in the Sulfur
Pits northeast of the Landing Zone [17]:

- Weak point: "small gap in the carapace" on back, accessed via high ground [17]
- Dies in "two or three discharges with the LMG or the Assault Rifle" [17]
- Reward: Biological Sample worth **5,000 Data Points** per kill [17] — very
  high DP/time ratio vs. plant/salvage farming
- No evidence that Goliath kills gate other progression unlocks [44]

## Min-Max / Multiplayer Callouts

- **Multiplayer:** Late-game base defense is reported easier in co-op [49],
  but no fetched source documents specific role divergence. The monolith
  turret cheese [36] works solo or grouped.
- **Min-max:** Goliath farming (5,000 DP per kill) is the community-recommended
  sustainable DP source once combat capability is sufficient [17]. Experienced
  players running satellite bases [34] can bypass the Corp L9–11 wall faster
  than single-base players.

## Gaps & Limitations

- The World Engine activation cost (one Discovery snippet mentioned "400
  Electronics, 400 Chemicals, 1,000 Data Points") was not verified in a
  fetched source.
- Teleporter-unlock corporation level (post-Update-1 alternative path) is
  named by Discovery but specific level unconfirmed in fetched content.
- No developer statements were recovered on whether exploits (monolith cheese,
  cooling bypass) are patch targets.
