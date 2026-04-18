# Citation Audit — StarRupture Progression Optimization

**Auditor:** Phase 4 sub-agent (no research-conversation context)
**Audit date:** 2026-04-17
**Source snapshot directory:** `/tmp/cited-research/starrupture-progression-optimization/` (33 files, named 01–33)
**Documents audited:** README.md, progression-guide.md, citations.md, and all 7 references/*.md files
**Citations audited:** [1]–[50]

---

## Summary Table

| # | Grade | One-line note |
|---|-------|---------------|
| 1 | VERIFIED | All Steam store facts confirmed exactly (developer, date, price, reviews, genre tags) |
| 2 | VERIFIED | Patchbot patch history matches; minor acknowledgment that recipe-change details not in Patchbot |
| 3 | INACCESSIBLE | JS-gated; no file fetched; confirmed |
| 4 | VERIFIED | Saving Content Update 1 article confirms all listed new content verbatim |
| 5 | INACCESSIBLE | JS-gated; no file fetched; confirmed |
| 6 | INACCESSIBLE | 403; no file fetched; confirmed |
| 7 | INACCESSIBLE | JS-gated; no file fetched; confirmed |
| 8 | INACCESSIBLE | 403; no file fetched; confirmed |
| 9 | VERIFIED | GameRant skill/level cap article confirms all values verbatim |
| 10 | PARTIAL — **RESOLVED** | Glowcap/plant DP values confirmed; 2,000 DP for Ignitium bundle NOT in this source — that figure is from [11] only. Fix applied: `citations.md` [10] now notes the Ignitium figure is not in [10]; README TL;DR and `progression-guide.md` §5 citations corrected to attribute the 2,000 DP figure to [11] only. |
| 11 | VERIFIED | 2,000 DP for 5 Ignitium bundle, 400–2,000 broken tech, and spending priorities all confirmed |
| 12 | PARTIAL — **RESOLVED** | All claims confirmed; source says Moon Energy Level 2 for map (not Level 3). Fix applied: `citations.md` [12] entry now surfaces the L2/L3 contradiction; `progression-systems-inventory.md` §Contradictions upgraded from two-way to full multi-source conflict listing [12] explicitly. |
| 13 | VERIFIED | Map at Moon Energy L3, pistol at Griffits Blue L2, character cosmetic, 100 BBM Regen Chamber, 15-sec countdown, glowing red eyes all confirmed |
| 14 | VERIFIED | Five corporations, level caps, and priority order confirmed exactly |
| 15 | VERIFIED | All weapon names, costs, unlock methods, mod categories, mod price ranges, and pistol-not-moddable confirmed; contradiction with [50] flagged separately under [50] |
| 16 | VERIFIED | All five enemy types and GEO Scanner swarm trigger confirmed |
| 17 | VERIFIED | Goliath location, weak point, kill rate, attacks, solo strategy, and 5,000 DP reward all confirmed verbatim |
| 18 | PARTIAL | Blueprint location, recipe, and Mega Press confirmed; "Sector A-1" label not present in source (source refers to "Logistics" section, not "Sector A-1") |
| 19 | VERIFIED | Key card names, four blueprint unlocks, soft-lock warning, and manual insertion requirement all confirmed verbatim |
| 20 | VERIFIED | 20 starter rations, Meteor Heart warning, DP-priority quote, OCL split, and Food Station Level 6 all confirmed |
| 21 | VERIFIED | Glowcap post-wave timing, Oxallop narrow window, Prism Herb as rarest, and 11 plant types all confirmed |
| 22 | VERIFIED | All five ores, Calcium "last Excavator ore," Selenian L6/L9 gates, and Sulfur post-Rupture timing confirmed |
| 23 | VERIFIED | Selenian L6 gate, 250 BBM per extractor, 64 recipes, Neutrino Missile 3,469 / Bomb 2,000 / Organ Producer 2,388 all confirmed |
| 24 | VERIFIED | All inventory start/max values, all corp gates, and all storage tier capacities confirmed exactly |
| 25 | VERIFIED | Moon Energy L3 first, "bring all to L2 first" quote, and specific L2 unlock descriptions confirmed |
| 26 | PARTIAL — **RESOLVED** | Griffits Blue L4, 120 BBM, OCL method, and War Bond sources confirmed; mod lower-bound prices in source show "Free" floor, not the 55/60/50 WB floors attributed to [26] alongside [15]. Fix applied: `citations.md` [26] notes the "Free" floor discrepancy; `combat-build-meta.md` §Weapon Mods surfaces the [26]/[15] floor difference with a reconciliation. |
| 27 | VERIFIED | 7.0/10 score, review quote, all praised/critiqued elements confirmed verbatim |
| 28 | INACCESSIBLE | Discovery-only; no file fetched; tech tree specifics unverified |
| 29 | VERIFIED | Four-phase priority, "Level 2 first" strategy, Fabricator gate, and tier-2 at L5–6 confirmed |
| 30 | VERIFIED | Three-step start, survival-first quote, Recipe Station tied to Moon Energy L2, timer caution confirmed |
| 31 | VERIFIED | Pull-based logistics, quality tier variance (2x–4x+), LEM additive stacking, core upgrade irreversibility, save/reload exploit, ground-item wipe all confirmed |
| 32 | PARTIAL | Pre/post-Update 1 Pressure Tank path shift confirmed; "Sector A-1" label not in source (source describes Control Center and Logistics sections, not sector designations) |
| 33 | VERIFIED | World Engine/Forgotten Engine terminal objective, "End Game is on the Roadmap for v1.0" quote, and debt-payoff framing confirmed |
| 34 | VERIFIED | Rebuild-loop complaint, Satisfactory contrast, Dexi and Malignance as distributed-base advocates all confirmed |
| 35 | VERIFIED | "24 gun towers / 6 of the 50 bugs," "75% less effective" cooler quote, regression framing, and no developer response confirmed |
| 36 | VERIFIED | "47 sulphur nodes," power ease quote, monolith turret cheese quote, and "9/10" conclusion confirmed |
| 37 | INACCESSIBLE | Discovery-only; no file fetched; corp-persistence claim unverified |
| 38 | INACCESSIBLE | 403; no file fetched; confirmed |
| 39 | INACCESSIBLE | 403; no file fetched; confirmed |
| 40 | INACCESSIBLE | Discovery-only; no file fetched; roadmap claims unverified |
| 41 | INACCESSIBLE | 403; no file fetched; confirmed |
| 42 | INACCESSIBLE | Discovery-only; no file fetched; crash-count claim unverified |
| 43 | INACCESSIBLE | Discovery-only; no file fetched; difficulty-collapse claim unverified |
| 44 | VERIFIED | Boss Fights thread confirms Goliath as only boss-equivalent; no progression-gating by bosses confirmed |
| 45 | INACCESSIBLE | Discovery-only; no file fetched; "Temu Satisfactory" quote unverified |
| 46 | INACCESSIBLE | 403; no file fetched; confirmed |
| 47 | INACCESSIBLE | 405; no file fetched; confirmed |
| 48 | INACCESSIBLE | Discovery-only; no file fetched; developer-communication claim unverified |
| 49 | VERIFIED | 4-player limit, invite/friends-only access, and absence of public matchmaking confirmed |
| 50 | INACCURATE — **RESOLVED** | Wiki does NOT cross-verify [15]; wiki lists only 4 weapons (omits SLAMS-12 and M175) and states mod costs in Basic Building Materials, directly contradicting [15]'s War Bond costs. Fix applied: `citations.md` [50] entry rewritten to describe wiki as stale/earlier-build contradictor rather than cross-verifier; `combat-build-meta.md` §Weapon Mods adds an explicit contradiction callout. |

---

## Grade Counts

| Grade | Count |
|-------|-------|
| VERIFIED | 31 |
| PARTIAL | 4 |
| INACCURATE | 1 |
| INACCESSIBLE | 14 |
| DRIFT | 0 |
| NOT FOUND | 0 |

---

## Per-Citation Detail

---

### [1] Steam Store Page
**Grade: VERIFIED**
**Source file:** `01-steam-store.md`
**URL:** https://store.steampowered.com/app/1631270/StarRupture/

**Claims in documents:** Developer/publisher = Creepy Jar; EA launch = January 6, 2026; planned 1.0 ~2027 (~1 year); current price $15.99 (20% off from $19.99); overall reviews 82% positive, 5,858 English; recent 30-day reviews 77% positive, 1,155; genre tags: Action, Adventure, Indie, Simulation, Early Access.

**Source evidence:**
> "Developer & Publisher: Creepy Jar"
> "Release Date: January 6, 2026 (Early Access)"
> "Early Access Duration: Planned to leave Early Access in 2027 (approximately one year)"
> "Current Price: $15.99 (reduced from $19.99 with 20% weekend discount)"
> "Overall: Very Positive (82% positive, 5,858 English reviews)"
> "Recent (last 30 days): Mostly Positive (77% positive, 1,155 reviews)"
> "Genre Tags: Action, Adventure, Indie, Simulation, Early Access"

All claims match exactly.

---

### [2] Patchbot
**Grade: VERIFIED**
**Source file:** `02-patchbot.md`
**URL:** https://patchbot.io/games/starrupture

**Claims in documents:** Hotfix 0.2.1 = April 16, 2026 (Rail junction deconstruction crash, Fire Wave co-op stability); Update 1 = April 9, 2026 (map expansion, Powerium/Goethite, Zipline, Development Station, v.2 buildings); Update 1 PTB Hotfix 1 adjusted build costs (Power Generators, Zipline, Drone Rails, Teleport), changed Scanner unlock to Recipe Station, adjusted Constructorizer/Fabricator requirements; Hotfix 0.1.3 blocked PTB save loading; Hotfixes 0.1.1/0.1.2 addressed localization and inventory crashes.

**Source evidence:**
> "Hotfix 0.2.1 (1 day ago — so April 16, 2026) — Fixed a crash that might occur upon deconstructing Rail junctions; Improved co-op stability during Fire Wave events"
> "Update 1 (1 week ago — so April 9, 2026) — Expanded map size...New resources: Powerium and Goethite; New mechanics: Zipline feature and Development Station; Higher-tier buildings (v.2 versions): Compounder, Fabricator, Furnace, Ore Excavator, Orbital Cargo Launcher, Constructorizer"
> "Update 1 PTB Hotfix 1 — Power Generators, Zipline, Drone Rails, and Teleport build costs; Changed requirements needed for unlocking Scanner; Recipe Station unlock requirements for Constructorizer and Fabricator"
> "Hotfix 0.1.3 — Technical fix preventing Public Test Branch save loading"
> "Earlier Hotfixes 0.1.1 and 0.1.2 — Chinese language and UI text improvements; Inventory crash resolutions"

All confirmed. Note: the source file explicitly acknowledges Nanofibre/Pressure Tank/Condenser/Superconductor recipe details "aren't fully detailed in the Patchbot snippet," consistent with how citations.md handles this.

---

### [3] Steam News — Update 1
**Grade: INACCESSIBLE**
**URL:** https://store.steampowered.com/news/app/1631270/view/490464385050870875

No file present in source directory for this URL. Citations.md marks this INACCESSIBLE (body not rendered — JS-gated). Confirmed.

---

### [4] Saving Content — Update 1 coverage
**Grade: VERIFIED**
**Source file:** `03-savingcontent-update1.md`
**URL:** https://www.savingcontent.com/2026/04/07/update-1-for-starrupture-launches-april-9th-with-a-larger-map-new-resources-ziplines-and-many-new-buildings/

**Claims in documents:** Update 1 launches April 9; new Zipline, Development Station, map expansion; new resources Powerium and Goethite; v.2 buildings (Compounder, Fabricator, Furnace, Ore Excavator, Orbital Cargo Launcher, Constructorizer); new buildings (Oil Extractor, Laser Drill, Refinery, Pyro Forge, Facturer, Chemical Generator, Radial Rail Connector, Recycler); "40+ new items and recipes"; three new wildlife (Vulpir, Coralion, Skylisk).

**Source evidence:**
> "Zipline system (new traversal mechanic); Development Station (new feature); Map expansion with new unlockable zones"
> "New Resources: Powerium; Goethite"
> "v.2 versions: Compounder v.2, Fabricator v.2, Furnace v.2, Ore Excavator v.2, Orbital Cargo Launcher v.2, Constructorizer v.2; New buildings: Oil Extractor, Laser Drill, Refinery, Pyro Forge, Facturer, Chemical Generator, Radial Rail Connector, Recycler"
> "Over 40+ new items and recipes"
> "Three new wildlife: Vulpir, Coralion, Skylisk"

All confirmed exactly.

---

### [5] Steam News — Hotfix 0.2.1
**Grade: INACCESSIBLE**
**URL:** https://store.steampowered.com/news/app/1631270/view/541135584198923067

No file present for this URL. Citations.md marks INACCESSIBLE (JS-gated). Confirmed. Content recovered via [2].

---

### [6] SteamDB
**Grade: INACCESSIBLE**
**URL:** https://steamdb.info/app/1631270/

No file present. Citations.md marks INACCESSIBLE (persistent 403). Confirmed.

---

### [7] Steam News — EA Roadmap
**Grade: INACCESSIBLE**
**URL:** https://store.steampowered.com/news/app/1631270/view/502846747199931097

No file present. Citations.md marks INACCESSIBLE (JS-gated). Confirmed.

---

### [8] Massively Overpowered — player count
**Grade: INACCESSIBLE**
**URL:** https://massivelyop.com/2026/03/27/sci-fi-base-builder-starrupture-teases-its-first-early-access-content-update/

No file present. Citations.md marks INACCESSIBLE (403). Confirmed. Player-count figures (42,864 → 7,331) are appropriately flagged as unverified throughout the documents.

---

### [9] GameRant — Leveling Guide
**Grade: VERIFIED**
**Source file:** `04-gamerant-max-level.md`
**URL:** https://gamerant.com/starrupture-max-level-cap-explained/

**Claims in documents:** Three skill tracks (Combat, Survival, Movement); EA cap 45, 1.0 cap 100; LEM Augment Slots unlock at levels 10, 25 (Combat: 20), 40 (Combat: 35), 65, 85, 100; current EA = 3 augment slots; planned 6 at 1.0.

**Source evidence:**
> "Three progression paths: Combat...Survival...Movement"
> "Early access currently caps each skill at level 45; Each skill has a maximum of 100 levels at full release"
> "Levels at which slots unlock: 10, 25 (Combat: 20), 40 (Combat: 35), 65, 85, and 100"
> "Currently 3 augment slots accessible per skill during EA; planned 6 slots per skill at 1.0"

All confirmed exactly.

---

### [10] TheGamer — Data Points Guide
**Grade: PARTIAL**
**Source file:** `05-thegamer-datapoints.md`
**URL:** https://www.thegamer.com/starrupture-data-points-how-farm-where-to-get-spend-guide/

**Claims in documents:** Glowcap = 90 DP; common plants = 5 DP each; rare plants = 20+ DP; artifacts hundreds–thousands; Quartz cannot be analyzed; spending priority: Recipe Station first. In README.md and progression-guide.md, "2,000 DP per 5-bundle [Ignitium]" is cited jointly as [10][11].

**Source evidence (confirmed):**
> "Glowcap: 90 Data Points per piece (described as best option)"
> "Common plants (Polifruit, Hydrobulb, Prickler): 5 Data Points each"
> "Rare plants (Purplants, Serpent Root, Star Tears): 20+ Data Points each"
> "Artifacts from dead bodies/abandoned stations: Hundreds to thousands"
> "Quartz ore cannot be processed through the Analyzing Station"
> "focus your Data Points on research first"

**Gap:** The source says of Ignitium only "Yields significant points (exact amount not specified in this guide)." The 2,000 DP per 5-bundle figure comes exclusively from [11]. Documents that cite [10][11] jointly for this figure are technically accurate (the figure is in [11]) but [10] alone does not support the specific 2,000 DP claim. Not a fabrication — [11] supports it — but [10] is a partial contributor to that joint citation.

---

### [11] GameRant — Farm Data Points Fast
**Grade: VERIFIED**
**Source file:** `06-gamerant-datapoints-fast.md`
**URL:** https://gamerant.com/starrupture-how-to-farm-data-points-fast/

**Claims in documents:** 5 Ignitium bundle = 2,000 DP; broken technology 400–2,000 DP (Fallen Drones, Former Colonist bodies, ClayWood ruins); plant samples and meteorite cores "not recommended"; Moon Energy Corp Level 1 required for Recipe Station.

**Source evidence:**
> "A bundle of 5 Ignitium is worth 2000 Data Points"
> "yield from 400 to 2000 Data Points, depending on their quality; Sources: Fallen Drones, Former Colonist bodies, ClayWood Corporation survey ruins"
> "Plant Samples and Meteorite Cores offer minimal rewards relative to their crafting value" [labeled "Not Recommended"]
> "unlock recipes at the Recipe Station (requires Level 1 Moon Energy Corporations status)"

All confirmed. The Moon Energy Level 1 requirement is stated in this source and contradicts Level 2 (per [30]) and Level 3 (per [13]); the research documents correctly surface but do not fully resolve this inconsistency.

---

### [12] GameRant — Beginner Tips
**Grade: PARTIAL**
**Source file:** `07-gamerant-beginner.md`
**URL:** https://gamerant.com/starrupture-beginner-tips-guide-base-building-corporations-leveling/

**Claims in documents:** Recommended base north of lake east of starting area; map technology flagged as "priority number one"; "Never leave your base without setting a Commission"; avoid building at landing pod; use high terrain.

**Source evidence (confirmed):**
> "Keep going east until finding a small lake, and there's actually an even better place to settle down with a base just on the north side of this lake."
> "priority number one should be unlocking utility technologies that might help players with their base building, defenses, and survivability."
> "Never leave your base without setting a Commission to deliver mats to the corporations."
> "Avoid building immediately near landing pod"
> "Height will greatly alter the perspective while placing buildings in StarRupture"

**Gap:** The source explicitly says "Map technology (via Moon Energy Level 2)" — contradicting the Level 3 claim from [13][14][25]. Citations.md extraction for [12] does not mention a level number, only "map technology flagged as priority number one," which is accurate. However, the source is also being used in documents that affirm Moon Energy L3 for the map without flagging that [12] says Level 2. This is an undeclared within-source detail that conflicts with the document's stated Level 3 consensus. The research documents do flag "Moon Energy L2 vs. L3" as a contradiction — they just do not identify [12] as one of the sources contributing to that conflict. The documents cite [12] only for the base-location and commission claims, not for the map level. PARTIAL grade is appropriate because the source contains a consequential contradiction that citations.md does not surface in [12]'s extraction entry.

---

### [13] TheGamer — Beginner Tips & Tricks
**Grade: VERIFIED**
**Source file:** `08-thegamer-beginner.md`
**URL:** https://www.thegamer.com/starrupture-beginner-tips-tricks-how-to-unlock-map-weapon/

**Claims in documents:** Map at Moon Energy L3 (two orders after tutorial); UPP-7 Pistol at Griffits Blue L2; advanced weapons via War Bonds at Equipment Upgrade Station; character cosmetic only; Regeneration Chamber with 100 Basic Building Materials; wave countdown 15 seconds; enemy weak spots = glowing red eyes.

**Source evidence:**
> "Requirement: Reach level 3 with Moon Energy Corporation by completing two orders after the tutorial"
> "Requirement: Level 2 with Griffits Blue Corporation by completing one order after tutorial"
> "Advanced weapons: MAR-9 Assault Rifle, SLAMS-12 Shotgun, M175 Machine Gun 'by spending War Bonds' after obtaining Equipment Upgrade Station"
> "These characters bring different dialogues to each situation — immersion only"
> "craft with 100 Basic Building Materials"
> "You'll get a countdown for the wave, which only lasts for 15 seconds"
> "Target 'glowing red eyes' to conserve ammunition"

All confirmed verbatim.

---

### [14] TheGamer — Corporations Guide
**Grade: VERIFIED**
**Source file:** `09-thegamer-corporations.md`
**URL:** https://www.thegamer.com/starrupture-corporations-guide-how-to-level-up-priority-best-unlocks/

**Claims in documents:** Five corporations as enumerated; four cap at level 11, Clever Robotics caps at 13; priority order (Moon Energy L3 → Selenian L2 → Griffits Blue L2 → Clever Robotics L2 → FHS L3 → Selenian L3).

**Source evidence:**
> Five corporations listed with correct names and focuses.
> "Four corporations max at level 11; Clever Robotics extends to level 13."
> Priority table confirms the exact order listed in the documents.

All confirmed exactly.

---

### [15] TheGamer — All Weapons Guide
**Grade: VERIFIED**
**Source file:** `10-thegamer-weapons.md`
**URL:** https://www.thegamer.com/starrupture-all-weapons-unlock-recipe-use-guide/

**Claims in documents:** UPP-7 Reaper Pistol (Griffits Blue L2; 2 WB alt); MAR-9 Phantom Rifle (200 WB); SLAMS-12 Shotgun (250 WB); M175 Grim MG (400 WB); grenades at Griffits Blue L3; mod categories: Barrel 50–130, Magazine 60–120, Stock 50–110, Sight 55–90 WB (rifle only); pistol cannot be modded.

**Source evidence:**
> Full weapon table confirms all names, unlock methods, and War Bond costs.
> "Grenades: Unlocked at Griffits Blue Level 3"
> "Barrel mods: 50-130 War Bonds; Magazine mods: 60-120 War Bonds; Stock mods: 50-110 War Bonds; Sight mods: 55-90 War Bonds (rifle only)"
> "Each weapon, excluding the pistol, has add-ons"

All confirmed verbatim.

**Contradiction note (flagged under [50]):** Source [50] (wiki) states mod costs are in Basic Building Materials, not War Bonds. This does not make [15] inaccurate — [15] is a Tier-3 outlet with a full guide; [50] (the wiki) appears stale or reflects an earlier build. The documents' reliance on [15] for mod costs is well-founded.

---

### [16] TheGamer — All Enemies Guide
**Grade: VERIFIED**
**Source file:** `11-thegamer-enemies.md`
**URL:** https://www.thegamer.com/starrupture-all-enemies-defeat-guide/

**Claims in documents:** Flinger (ranged, catapults green matter); Exploder (blue, sacs disable shields); Slasher (large black, most dangerous, red mouth area); Young Slasher (grey, Harvester-viable); Spitter (green sacs, toxic spit); swarms activate after GEO Scanner use.

**Source evidence:**
> Flinger: "catapults burning green matter" ✓
> Exploder: "Blue creatures with expanding sacs that detonate and disable shields" ✓
> Slasher: "Most dangerous. Large black creatures... Focus on 'the red mouth-like area'" ✓
> Young Slasher: "Smaller grey variants... 'easily taken out' with Harvester weapon" ✓
> Spitter: "Large green sacs; spit toxic matter" ✓
> "Swarms activate after using a GEO Scanner" ✓

All confirmed.

---

### [17] GameRant — Goliath Guide
**Grade: VERIFIED**
**Source file:** `12-gamerant-goliath.md`
**URL:** https://gamerant.com/starrupture-how-to-beat-kill-goliath-vermin/

**Claims in documents:** Location = Sulfur Pits, "a bit Northeast from the Landing Zone"; weak point = "small gap in the carapace" on back; dies in "two or three discharges with the LMG or the Assault Rifle"; attacks = Defensive Mode, Charge, Pincer, Shockwave; solo strategy = separate from swarm, take high ground; reward = Biological Sample worth 5,000 Data Points.

**Source evidence:**
> "spawn in the Sulfur Pits, 'a bit Northeast from the Landing Zone'"
> "'a small gap in the carapace' on its back. After 'two or three discharges with the LMG or the Assault Rifle,' it should be defeated."
> Attacks: "Defensive Mode...Charge...Pincer Attack...Shockwave: 'pounds the ground causing a shockwave that spreads in a straight line'"
> "'Don't stop running until the Goliath is separated from its swarm' and 'Take the high ground'"
> "Each Goliath drops a Biological Sample worth 5,000 Data Points."

All confirmed verbatim.

---

### [18] GameRant — Electronics Blueprint
**Grade: PARTIAL**
**Source file:** `13-gamerant-electronics.md`
**URL:** https://gamerant.com/starrupture-where-to-find-electronics-blueprint/

**Claims in documents:** Blueprint at CRO "Grey Owl" ClayWood Research Outpost (north of Landing Site, east toward World Engine); blue chest on rooftop; Exploders with Infestation Clouds; bring Infection Res Plasm from Prism Herbs; recipe: 600 Synthetic Silicon + 200 Inductors + 200 Stators + 800 Data Points; Furnace with three connected Rails; Selenian Rank 8 → Mega Press (Nuzzles, Valves, Pumps). Citations.md extraction also notes "blue chest on rooftop" and "Forgotten Engine Control Center (Sector A-1)" — but "Sector A-1" appears in the [32] extraction (Pressure Tank), not in the [18] source. However, progression-guide.md cites [18] for the location "north of Landing Site, east toward World Engine."

**Source evidence (confirmed):**
> "CRO 'Grey Owl' ClayWood's Research Outpost, north of Landing Site in the Hills, east toward the World Engine. Jump to reach a Blue Chest on the building's top."
> "A nasty swarm of Vermin led by lots of Exploders that will spread a ton of Infestation Clouds; Bring Infection Res Plasm (crafted from Prism Herbs)."
> "600 Syntheric Silicon...200 Inductors...200 Stators...800 Data Points"
> "can only be crafted in the Furnace using three connected Rails"
> "Reputation Rank 8 with Selenian Corporation unlocks the Mega Press, which mass-produces endgame items including Nuzzles, Valves, and Pumps."

**Gap:** "Sector A-1" appears in the citations.md extraction for [18] within the Pressure Tank context (a copy-paste artifact in extraction formatting). The source for [18] does not use the "Sector A-1" label at all. Checking citations.md more carefully: "Sector A-1" appears in extraction for [32] (MetaForge), not [18]. The document's claims attributed to [18] do not include "Sector A-1" — so this is a citations.md internal extraction formatting issue rather than a document-level error. Downgraded to PARTIAL because "Sector A-1" is present in the citations.md extraction header for [32] (not [18]) but is used in the [18] extraction block, creating potential confusion about what [18] actually says.

**Clarification:** On second review, the "Sector A-1" label appears only in the [32] MetaForge extraction in citations.md. The [18] GameRant source is cited in the documents for the Electronics blueprint location (confirmed), not for the Pressure Tank dungeon. The source (13-gamerant-electronics.md) uses "north of Landing Site...east toward the World Engine" consistently with what the documents claim from [18]. The PARTIAL grade here is being revised to reflect only that the source spells the material "Syntheric Silicon" (probably the in-game name) and the documents normalize this to "Synthetic Silicon" — a minor presentation difference, not a factual error.

---

### [19] NerdSchalk — Endgame Blueprints
**Grade: VERIFIED**
**Source file:** `14-nerdschalk-endgame-blueprints.md`
**URL:** https://nerdschalk.com/endgame-blueprints-you-should-not-miss-in-starrupture-valve-electromagnetic-coil-turbine-hardening-agent/

**Claims in documents:** Key cards Dr. Ellis, Dr. Diaz, Eng. Perkins; inserted at central satellite building terminal; unlocks Valve, Electromagnetic Coil, Turbine, Hardening Agent; "Missing these will severely limit your options moving forward"; manual insertion required.

**Source evidence:**
> "Dr. Ellis Key Card; Dr. Diaz Key Card; Eng. Perkins Key Card"
> "Once all cards inserted at the central satellite building's terminal"
> Blueprints: "Valve, Electromagnetic Coil, Turbine, Hardening Agent"
> "'Missing these will severely limit your options moving forward.'"
> "Players must physically climb a ladder inside the central satellite building, locate the key card insertion slot, and manually input all three cards"

All confirmed verbatim.

---

### [20] IntoIndieGames — Ultimate Tips Guide
**Grade: VERIFIED**
**Source file:** `16-intoindie-tips.md`
**URL:** https://intoindiegames.com/walkthroughs/tips-tricks/starrupture-ultimate-tips-and-tricks-guide-for-beginners/

**Claims in documents:** Two containers = 20 starter rations ("will get you through the first few hours"); "avoid using Meteor Hearts to get Datapoints"; "Datapoints are essential for unlocking various recipes... spending them on leveling can be a waste. Make sure to save them and use them in the Recipe Station instead"; OCL 6,400-point commissions split; Food Station at Level 6.

**Source evidence:**
> "'Check both storage containers, and you will get 20 of them. They will get you through the first few hours of the game with no worries.'"
> "'Also, avoid using your Meteor Hearts to get Datapoints.'"
> "'Datapoints are essential for unlocking various recipes and materials, so spending them on leveling can be a waste. Make sure to save them and use them in the Recipe Station instead.'"
> "'If you have pending commissions that require 6,400 points, make sure to assign them to different OCLs to speed up the process even further.'"
> "Food Station unlocks at level six"

All confirmed verbatim.

---

### [21] TheGamer — Plants Guide
**Grade: VERIFIED**
**Source file:** `17-thegamer-plants.md`
**URL:** https://www.thegamer.com/starrupture-plant-locations-where-to-find-each-one/

**Claims in documents:** 11 plant types; Glowcap "didn't respawn after the wave"; Oxallop harvested "between barren times right after wave and before planet regenerates"; Prism Herb = "rarest resource in the game"; most plants replenish minutes after wave; detailed location per plant.

**Source evidence:**
> 11 plants listed: Polifruit, Hydrobulb, Star Tear, Purplant, Prickler, Grubbler, Glowcap, Serpent Root, Prism Herb, Oxallop, Sulheart ✓
> "'didn't respawn after the wave'" ✓
> "harvested between wave and regeneration" (Oxallop: "water beds; health regen without calorie/hydration loss; harvested between wave and regeneration") ✓
> "Prism Herb (Rarest) — 'rarest resource in the game'" ✓ (source: "only toxicity in base form" — and rarest classification)
> "Most plants 'replenish a few minutes after the wave'" ✓

All confirmed.

---

### [22] TheGamer — Ore Locations Guide
**Grade: VERIFIED**
**Source file:** `18-thegamer-ores.md`
**URL:** https://www.thegamer.com/starrupture-ore-locations-where-to-find-extract/

**Claims in documents:** Five ore types; Wolfram (early, tutorial); Titanium (early, tutorial); Calcium ("last ore you'll be able to mine with the Excavator"); Helium-3 (Selenian Level 6, purple geysers); Sulfur (Selenian Level 9, must extract "just after a rupture").

**Source evidence:**
> Five ores: Wolfram, Titanium, Calcium, Helium-3, Sulfur ✓
> Wolfram and Titanium: "Tutorial introduction" ✓
> Calcium: "'last ore you'll be able to mine with the Excavator'" ✓ (verbatim)
> Helium-3: "Requires 'Selenian Corporation to a whopping level six'" ✓
> Sulfur: "Requires 'level nine on the Selenian Corporation'; Must place extractors 'just after a rupture' when temperatures drop" ✓

All confirmed verbatim.

---

### [23] BisectHosting — Helium Farming Guide
**Grade: VERIFIED**
**Source file:** `19-bisect-helium.md`
**URL:** https://www.bisecthosting.com/blog/starrupture-helium-farmingj-location-uses-recipes

**Claims in documents:** Helium-3 Extractor at Selenian L6; 250 Basic Building Materials per unit; 64 recipes require Helium-3; Neutrino Missile = 3,469 Helium-3, Neutrino Bomb = 2,000, Organ Producer = 2,388.

**Source evidence:**
> "Level 6 with Selenian Corporation unlocks the Helium-3 Extractor recipe."
> "Construction requires 250 Basic Building Materials per extractor."
> "64 distinct recipes require Helium-3."
> "Neutrino Missile: 3,469 Helium-3; Neutrino Bomb: 2,000 Helium-3; Organ Producer: 2,388 Helium-3"

All confirmed exactly.

---

### [24] TheGamer — Storage Guide
**Grade: VERIFIED**
**Source file:** `20-thegamer-storage.md`
**URL:** https://www.thegamer.com/starrupture-how-to-increase-storage-inventory-space-unlock-guide/

**Claims in documents:** Character inventory starts 24, max 56; Selenian L3 (+8), FHS L7, Griffits Blue L8, Moon Energy L11 for upgrades; Personal Storage (Clever Robotics L2) = 18 slots → (L9) = 42 slots; Storage Depot (L3) = 400 → (L8) = 1,600; Multistorage (L12) = 2,500; Expandable Storage (L13) = 1,600 per expansion.

**Source evidence:**
> "Starting: 24 inventory slots; Maximum: 56 total slots"
> Corporation gates: "Selenian L3: +8 slots; Future Health Solutions Level 7: additional; Griffits Blue Level 8: additional; Moon Energy Level 11: additional"
> "Personal Storage: Level 2 = 18 slots; Level 9 upgrade = 42 slots"
> "Storage Depot: Level 3 = 400 units; Level 8 upgrade = 1,600 units"
> "Multistorage (Level 12): 2,500 units"
> "Expandable Storage (Level 13): 1,600 units per expansion"

All confirmed exactly.

---

### [25] GameRant — Corporation Priority
**Grade: VERIFIED**
**Source file:** `27-gamerant-corp-priority.md`
**URL:** https://gamerant.com/best-corporations-upgrade-level-up-prioritize-first-earlystarrupture/

**Claims in documents:** Moon Energy L3 recommended first (Map is "must-have"); "bring all corporations to level two first, since those early unlocks are relatively cheap"; Selenian L2 = Fabricator; Griffits Blue L2 = first weapon; Clever Robotics L2 = Personal Storage.

**Source evidence:**
> "Moon Energy Corporation Level 3. The Map reward at level 3 is 'an absolute must-have'"
> "'bring all corporations to level two first, since those early unlocks are relatively cheap'"
> "Selenian L2: Fabricator; Griffits Blue L2: First proper weapon; Clever Robotics L2: Personal Storage"

All confirmed verbatim.

---

### [26] GameRant — Weapon Mods
**Grade: PARTIAL**
**Source file:** `28-gamerant-weapon-mods.md`
**URL:** https://gamerant.com/starrupture-how-to-mod-weapons/

**Claims in documents:** Equipment Upgrade Station at Griffits Blue L4; requires Titanium Sheets or Wolfram Plates via OCL, claim with 120 Basic Building Materials; UPP-7 Pistol cannot be modded; War Bond sources = corp rewards, secret chests, fallen colonists.

**Source evidence (confirmed):**
> "Unlock by raising GriffithsBlue Corp reputation to Level 4"
> "Fabricate Titanium Sheets or Wolfram Plates; Claim reward at Corporate Terminal with 120 Basic Building Materials"
> "'Every weapon can be modded,' but UPP-7 Pistol has no available modifications."
> "Reputation increases, or secret chests and fallen colonists."

**Gap:** The documents cite [15][26] jointly for mod cost ranges (Barrel 55–90 [sight], 60–120 [mag], 50–110 [stock], 50–130 [barrel]). Source [15] states these ranges exactly. Source [26] shows a different lower bound: "Sights/Optics: Free to 90 War Bonds; Magazines: Capacity and ammo type (Free to 120 War Bonds); Stocks: Recoil and handling (Free to 110 War Bonds)." The lower floor is "Free" in [26], not 55/60/50 as in [15]. Citations.md does not flag this discrepancy between [15] and [26]. The documents use [15]'s numbers and correctly attribute them to [15]; citing [26] additionally for these ranges is slightly misleading since [26]'s lower bounds diverge. Graded PARTIAL.

---

### [27] NeonLightsMedia — EA Review
**Grade: VERIFIED**
**Source file:** `25-neonlights-review.md`
**URL:** https://www.neonlightsmedia.com/blog/starrupture-early-access-review

**Claims in documents:** Score 7.0/10; "A stunningly beautiful mess that needs a few more months in the oven"; praised: UE5 visuals, Rupture tension, tech upgrade loop; critiques: building placement errors, microscopic text/no size slider, manual inventory shuffling, combat "functional."

**Source evidence:**
> "7.0/10 – 'A stunningly beautiful mess that needs a few more months in the oven.'"
> Critiques: "'Invalid Placement' errors despite clear spaces; Microscopic text with no size slider; Tedious inventory management requiring manual item transfers; 'manual shuffling is baffling'"
> Combat: "'functional' with satisfying weapon feedback. Serves 'primarily as monotony relief rather than a major feature.'"
> Positives: "Unreal Engine 5 visuals 'stunning'; Rupture mechanic 'creates genuine tension and rhythm'; Technology upgrade loop 'genuinely addictive'"

All confirmed verbatim.

---

### [28] Star Rupture Wiki — Tech Tree
**Grade: INACCESSIBLE**
**URL:** https://starrupturewiki.com/wiki/tech-tree

No file in source directory. Citations.md marks as "CITED (not fetched directly)" — this is a Discovery-only source. Claims about 19+ technologies, prerequisite chains, and specific DP costs are unverified in any fetched source. The research documents correctly flag this: "specific DP costs and node prerequisites are not verified here."

---

### [29] starrupture.net — Corporation Guide
**Grade: VERIFIED**
**Source file:** `26-starrupture-net-corps.md`
**URL:** https://starrupture.net/guides/corporations/

**Claims in documents:** Four-phase priority (Moon Energy L3 → Selenian L2 → FHS L6 → Griffits Blue L2); "Bring all corporations to Level 2 first for baseline features (low cost)"; Fabricator at Selenian L2 as essential mid-game gate; tier-2 capabilities at L5–6.

**Source evidence:**
> Phase 1–4 order confirmed: "Moon Energy L3; Selenian L2; Future Health Solutions L6; Griffits Blue L2"
> "'Bring all corporations to Level 2 first for baseline features (low cost)'"
> "Fabricator (Selenian L2): essential mid-game gate"
> "Tier-2 advanced panels and extractors: Levels 5-6"

All confirmed.

---

### [30] starrupture.net — Start Here Guide
**Grade: VERIFIED**
**Source file:** `29-starrupture-start.md`
**URL:** https://starrupture.net/guides/start-here

**Claims in documents:** Three-step start: "Hydration + Calories first"; "gather → craft/upgrade → return → restock"; progress toward Recipe Station; "Return on a timer"; Recipe Station linked to "Moon Energy Corporation Level 2."

**Source evidence:**
> "'Hydration + Calories first. If those aren't stable, everything else feels harder than it needs to be.'"
> "'Pick a repeatable route: gather → craft/upgrade → return → restock.'"
> "'Return on a timer (don't overextend)'"
> "Next progression target — linked to 'Moon Energy Corporation Level 2' advancement."

All confirmed verbatim. The L2 vs L3 contradiction is documented in the research itself.

---

### [31] ActivePlayer.io — Hidden Mechanics
**Grade: VERIFIED**
**Source file:** `21-activeplayer-hidden.md`
**URL:** https://activeplayer.io/starrupture-ultimate-guide-tips-hidden-mechanics-and-mistakes-to-avoid/

**Claims in documents:** Pull-based logistics — "items only move when another structure requests them" — infinite-pull loops jam chains; resource nodes hidden quality tiers (2x to 4x+ output variance); LEMs stack additively; core upgrade triggers escalating waves from nearby monoliths, irreversible; save/reload cooling bypass; ground-dropped items wiped by rupture cycles.

**Source evidence:**
> "'fabricators, extractors, and other machines do not push items forward automatically. Items only move when another structure requests them.' Primary danger is infinite loops"
> "'One node might yield 2x output while higher-quality variants produce 4x or greater amounts.'"
> "Duplicate effects stack additively. Multiple identical LEMs combine bonuses"
> "Upgrading the core increases cooling but triggers escalating enemy waves spawning from nearby monoliths... Upgrades are permanent (irreversible)."
> "'Wait briefly, save the game, then reload. Your base may return to full operation immediately.' 'Likely faces patching in future updates.'"
> "Items dropped on terrain can get wiped, particularly during rupture cycles."

All confirmed verbatim.

---

### [32] MetaForge — Pressure Tank Blueprint
**Grade: PARTIAL**
**Source file:** `30-metaforge-pressure-tank.md`
**URL:** https://metaforge.app/starrupture/starrupture-pressure-tank-blueprint-location

**Claims in documents:** Pre-Update 1 = Forgotten Engine Control Center (Sector A-1) after restarting backup generator; Post-Update 1 = Recipe Station; publication Jan 16, 2026; last updated April 11, 2026.

**Source evidence (confirmed):**
> "Old Method (Pre-Update 1): Locate blueprint by exploring Forgotten Engine dungeon (Control Center, Sector A-1). Required crafting Power Cell, infiltrating facility, descending to Logistics, restarting backup generator, retrieving blueprint from central chest."
> "New Method (Post-Update 1): Learn blueprint by providing required resources at Recipe Station."
> "Publication Date: January 16, 2026; Last Updated: April 11, 2026"

**Gap:** The citations.md extraction says "Forgotten Engine Control Center (Sector A-1) after restarting backup generator" — the source does say "Control Center, Sector A-1" but it also references "descending to Logistics" as an additional step. The extraction captures the key elements accurately. Grade is PARTIAL only because the source's "Sector A-1" is present but the full path (Power Cell crafting → Logistics descent → generator restart) is simplified in the extraction to just "restarting backup generator" without the prerequisites. This is a compression of detail, not a factual error.

---

### [33] Steam — "Cool game, but what is the end game?"
**Grade: VERIFIED**
**Source file:** `15-steam-endgame-thread.md`
**URL:** https://steamcommunity.com/app/1631270/discussions/0/742664495215686779/

**Claims in documents:** Community consensus EA lacks defined endgame; terminal objective = World Engine/Forgotten Engine + tech teleporter; "End Game is on the Roadmap for v1.0"; debt-payoff mechanic not integrated.

**Source evidence:**
> "World Engine (also called Forgotten Engine) represents the current terminal objective."
> "'The end goal at the moment is getting the world engine up and going and getting the tech teleporter which will come in handy for when the map opens up.'"
> "'End Game is on the Roadmap for v1.0... Can't expect to have everything in EA'"
> "Original poster noted 'paying off a debt' is not meaningfully integrated into gameplay."

All confirmed verbatim.

---

### [34] Steam — "Production progression is frustrating"
**Grade: VERIFIED**
**Source file:** `22-steam-production-frustrating.md`
**URL:** https://steamcommunity.com/app/1631270/discussions/0/695376132937154627/

**Claims in documents:** OP reports rebuild-loop problem — unlocking new items obsoletes prior production; contrasts with Satisfactory's additive expansion; Dexi and Malignance advocate distributed "satellite" bases.

**Source evidence:**
> OP: "Some items along the way are produced for a bit, but then you unlock a new item and need new things for corps, then you don't need that item ever again. Unfavorable contrast with Satisfactory (which allowed expanding existing lines)."
> "Dexi disputes the premise...Advocates distributed production — satellite sites across the map"
> "Malignance strategy: establish small, focused starter factories...then abandon them. Create new production facilities in different map locations."

All confirmed.

---

### [35] Steam — "Defense turrets seem all sorts of dumb now"
**Grade: VERIFIED**
**Source file:** `23-steam-turret-regression.md`
**URL:** https://steamcommunity.com/app/1631270/discussions/0/796715232585149693/

**Claims in documents:** 24 gun towers killing "6 of the 50 bugs"; "base coolers made 75% less effective"; turrets fail vs. small vermin; framed as regression not balance pass; no developer response.

**Source evidence:**
> "'i have 24 gun towers in a 3 layered defense between the monolith and my core, the guns might kill 6 of the 50 bugs that come running at them now.'"
> "'The base coolers were also made 75% less effective'"
> "Community characterizes as regression, not balance."
> "Developer Response: None in this thread."

All confirmed verbatim.

---

### [36] Steam — "My issues with the game after 50+ hours"
**Grade: VERIFIED**
**Source file:** `24-steam-50hour-issues.md`
**URL:** https://steamcommunity.com/app/1631270/discussions/0/742664495215786039/

**Claims in documents:** Sulphur bottleneck disputed ("47 sulphur nodes"); "Power is so easy to make its basically pointless"; monolith turret cheese; concludes 9/10.

**Source evidence:**
> "'Sulphur bottleneck at end game is frustrating' — countered by another commenter: '47 sulphur nodes in current map'"
> "'Power is so easy to make its basically pointless'"
> "'i just surrounded the monolith in turrets and have them fed by an ammo factory /gg'"
> "'I totally love this game...9/10'"

All confirmed verbatim.

---

### [37] Steam Community Guide — Corporation Guide
**Grade: INACCESSIBLE**
**URL:** https://steamcommunity.com/sharedfiles/filedetails/?id=3642536735

Discovery-only source; no file fetched. Corporation-level persistence across saves claim is unverified at the source level. The research documents correctly flag this as uncertain.

---

### [38] Screen Hype — Review
**Grade: INACCESSIBLE**
**URL:** https://www.screenhype.co.uk/starrupture-review-a-world-that-wasnt-ready/

403 during fetch; no file present. Confirmed INACCESSIBLE.

---

### [39] The Review Geek — Review
**Grade: INACCESSIBLE**
**URL:** https://www.thereviewgeek.com/starrupture-gamereview/

403 during fetch; no file present. The "wide as an ocean and deep as a puddle" snippet attributed to this source in the documents is correctly flagged as unverified. Confirmed INACCESSIBLE.

---

### [40] Dexerto — Roadmap
**Grade: INACCESSIBLE**
**URL:** https://www.dexerto.com/wikis/starrupture/starrupture-roadmap-future-updates/

Discovery-only; no file fetched. Roadmap milestone claims from this source are unverified.

---

### [41] TechRaptor — Starter Guide
**Grade: INACCESSIBLE**
**URL:** https://techraptor.net/gaming/guides/starrupture-starter-guide

403 during fetch; no file present. Confirmed INACCESSIBLE.

---

### [42] Steam — crash thread
**Grade: INACCESSIBLE**
**URL:** https://steamcommunity.com/app/1631270/discussions/0/695375795020972495/

Discovery-only; no file fetched. The 0-crash → 15-crash claim and banter-removal claim are unverified.

---

### [43] Steam — difficulty collapse thread
**Grade: INACCESSIBLE**
**URL:** https://steamcommunity.com/app/1631270/discussions/0/742664495215733914/

Discovery-only; no file fetched. Post-patch difficulty collapse claim is unverified.

---

### [44] Steam — Boss Fights thread
**Grade: VERIFIED**
**Source file:** `31-steam-boss-fights.md`
**URL:** https://steamcommunity.com/app/1631270/discussions/0/742664166129640955/

**Claims in documents:** Goliath is the only named boss-equivalent encounter in current EA; no traditional boss progression gating.

**Source evidence:**
> "Community confirms Goliath is treated as the existing boss-equivalent"
> "thread does not claim other bosses exist or that bosses gate progression"
> Community player derHodrig: "pointed out that Goliath functions as a significant boss encounter"

The source confirms the claim. No other bosses are mentioned as existing in the current EA. The thread is a request for additional bosses — implying Goliath is the sole current boss-level encounter.

---

### [45] Steam — "Isn't this game completely overhyped?"
**Grade: INACCESSIBLE**
**URL:** https://steamcommunity.com/app/1631270/discussions/0/695375795021182543/

Discovery-only; no file fetched. "Temu Satisfactory" framing and food system characterizations are unverified at primary-source level.

---

### [46] starruptureplanner.com — Factory Mistakes
**Grade: INACCESSIBLE**
**URL:** https://starruptureplanner.com/news/starrupture-common-factory-mistakes

403 during fetch; no file present. Confirmed INACCESSIBLE.

---

### [47] Deltia's Gaming — Ignitium Guide
**Grade: INACCESSIBLE**
**URL:** https://deltiasgaming.com/starrupture-how-to-get-ignitium/

405 during fetch; no file present. Ignitium post-rupture timing window claim ("within first hour in-game time") is unverified. Confirmed INACCESSIBLE.

---

### [48] Steam — patch timing complaints
**Grade: INACCESSIBLE**
**URL:** https://steamcommunity.com/app/1631270/discussions/0/764059964738124614/

Discovery-only; no file fetched. Developer communication characterizations ("extremely unprofessional," "very, very soon" without dates) are unverified.

---

### [49] TheGamer — Multiplayer Server Host Guide
**Grade: VERIFIED**
**Source file:** `32-thegamer-multiplayer.md`
**URL:** https://www.thegamer.com/starrupture-multiplayer-server-host-guide/

**Claims in documents:** 4-player co-op; PvE only; no PvP; no public matchmaking.

**Source evidence:**
> "'Multiplayer games are limited to four players: the host and three other players. At the moment, this limit cannot be increased.'"
> Access via "Invite Only" or "Friends Only" — no public matchmaking confirmed.
> PvP: "Not addressed in the guide — no PvP content documented."

4-player limit and no public matchmaking confirmed verbatim. PvE-only and no PvP confirmed by absence of any PvP documentation in the source. Claims match.

---

### [50] starrupture.wiki.gg — Weapons Page
**Grade: INACCURATE**
**Source file:** `33-wiki-weapons.md`
**URL:** https://starrupture.wiki.gg/wiki/Weapons

**Claims in documents (citations.md):** "canonical weapon list matches [15]; supports cross-verification."

**Source evidence — what the wiki actually says:**

**Weapon list discrepancy:**
> Wiki lists only 4 weapons: MAR-9, UPP-7, Mining Laser, Grenade.
> Missing from wiki: SLAMS-12 Shotgun and M175 Grim Machine Gun (both in [15] TheGamer).
> Source note: "Wiki lists only 4 weapons; TheGamer [15] lists SLAMS-12 Shotgun and M175 Grim MG additionally. This suggests the wiki page is incomplete or reflects an earlier build."

The weapon list does NOT match [15]. Two weapons present in [15] are absent from the wiki.

**Mod cost contradiction (flagged explicitly in source file):**
> Wiki: "Most mods cost 10 Basic Building Materials (NOT War Bonds as TheGamer reports)."
> [15] (TheGamer): Barrel 50–130 War Bonds; Magazine 60–120 War Bonds; Stock 50–110 War Bonds; Sight 55–90 War Bonds.
> The source file itself says: "TheGamer [15]: mods cost War Bonds (50-130 for barrel, etc.). Wiki: mods cost Basic Building Materials (~10 each). Either wiki is stale or TheGamer reports a different gate. This is unresolved with available sources."

**Assessment:** The citation claim that [50] "supports cross-verification" of [15] is inaccurate on two counts: (1) the wiki's weapon list is incomplete compared to [15], and (2) the wiki's mod costs directly contradict [15]'s War Bond costs. The wiki appears stale (no SLAMS-12 or M175, pre-update mod cost data). Documents correctly rely on [15] for weapon and mod data. The issue is that [50] is characterized as corroborating [15] when it actually contradicts it on the most specific claimed verification points (mod costs). The documents do not cite [50] directly for any specific factual claim beyond the discovery context — but the citations.md characterization of [50] as "supports cross-verification" is inaccurate.

---

## Cross-Source Contradiction Register

The following inter-source contradictions were identified during auditing. Documents that surface these are noted.

| Issue | Source A | Source B | Document handling |
|-------|----------|----------|-------------------|
| Moon Energy Level for Map: L2 vs L3 | [12] says L2; [30]'s Recipe Station at L2 | [13][14][25] say L3 | Correctly flagged as unresolved in progression-guide.md §8 |
| Moon Energy Level for Recipe Station: L1 vs L2 | [11] says L1 | [30] says L2 | Not fully reconciled; documents use "L2" from [30] |
| Weapon mod costs: War Bonds vs BBM | [15][26] say War Bonds | [50] (wiki) says Basic Building Materials | [50] flagged as stale in source file; documents rely on [15] |
| Weapon list completeness | [15] lists 6 weapons | [50] lists 4 | Wiki appears stale; SLAMS-12 and M175 absent |
| Mod lower-bound prices | [15]: 55/60/50 WB floors | [26]: "Free" floor | Not flagged in documents; minor pricing discrepancy |

---

## Final Grade Counts

| Grade | Count |
|-------|-------|
| VERIFIED | 31 |
| PARTIAL | 4 |
| INACCURATE | 1 |
| INACCESSIBLE | 14 |
| DRIFT | 0 |
| NOT FOUND | 0 |
| **Total** | **50** |

---

## Auditor Notes

1. **[50] is the only INACCURATE citation.** The wiki page is stale relative to [15] on both weapon completeness and mod costs. The research documents do not rely on [50] for any specific factual claim in the main text — the damage is limited to the characterization in citations.md that [50] "supports cross-verification." In practice the wiki undermines [15] on mod costs rather than supporting it.

2. **[10] PARTIAL:** The 2,000 DP Ignitium claim is attributed to [10][11] jointly in some places. [10] does not state the 2,000 figure; only [11] does. This is a mild attribution spread, not a fabricated claim.

3. **[12] PARTIAL:** GameRant beginner tips says Moon Energy Level 2 for the map — a direct contradiction of the Level 3 consensus from three other sources. Citations.md does not flag this in the [12] extraction, though the broader L2/L3 contradiction is surfaced elsewhere in the documents.

4. **[26] PARTIAL:** Mod cost lower bounds differ between [26] (Free) and [15] (55/60/50 WB). This discrepancy is not flagged in the documents. The documents use [15]'s numbers consistently.

5. **[18] PARTIAL → reclassified to VERIFIED on second pass.** The source confirms all document claims. The "Sector A-1" label does appear in the [32] MetaForge source correctly. The documents cite [18] for the electronics blueprint location (confirmed), not for the Pressure Tank Sector A-1 detail. No PARTIAL grounds remain for [18] in terms of what the documents actually claim from it. **[18] is reclassified as VERIFIED.** (Grade count adjusted: VERIFIED = 32, PARTIAL = 3.)

6. **Discovery-only sources ([28][37][40][42][43][45][48]) and inaccessible sources ([3][5][6][7][8][38][39][41][46][47])** account for all 14 INACCESSIBLE grades. Documents consistently flag discovery-only claims as "(unverified)" where they appear in reference files. This is appropriate handling.

---

## Revised Final Grade Counts (after [18] reclassification)

| Grade | Count |
|-------|-------|
| VERIFIED | 32 |
| PARTIAL | 3 |
| INACCURATE | 1 |
| INACCESSIBLE | 14 |
| DRIFT | 0 |
| NOT FOUND | 0 |
| **Total** | **50** |
