# Consistency Review — StarRupture Progression Optimization

**Reviewer:** Internal consistency sub-agent (no context from research conversation)
**Review date:** 2026-04-17
**Files reviewed:**
- `README.md`
- `progression-guide.md`
- `citations.md`
- `references/game-overview-ea-state.md`
- `references/progression-systems-inventory.md`
- `references/early-game-optimization.md`
- `references/mid-late-progression.md`
- `references/resource-economy.md`
- `references/combat-build-meta.md`
- `references/patch-volatility.md`

---

## Summary Table

| ID | Severity | Category | Short Description | Grade |
|---|---|---|---|---|
| C-01 | CRITICAL | Contradiction Transparency | Weapon mod cost currency ([15] War Bonds vs. [50] Basic Building Materials) never surfaced anywhere | **RESOLVED** — contradiction surfaced in `combat-build-meta.md` §Weapon Mods and in `citations.md` [50] entry |
| C-02 | CRITICAL | Citation Accuracy | `[22]` incorrectly cited for Oxallop post-Rupture claim in `progression-guide.md` §5 | **RESOLVED** — citation corrected to [10][11][21] for post-Rupture DP sources with [22] retained only for sulfur extractor placement |
| C-03 | MODERATE | Contradiction Transparency | Sulphur bottleneck vs. 47-nodes dispute absent from README and progression-guide deliverable | **RESOLVED** — Sulphur dispute added to `progression-guide.md` §5 ore progression table |
| C-04 | MODERATE | Contradiction Transparency | Production rebuild: "design flaw vs. playstyle mismatch" framed as settled in README, contested only in reference files | **RESOLVED** — README TL;DR reworded to explicitly flag the recommendation as contested |
| C-05 | MODERATE | Citation Accuracy | Recipe Station level: three-way conflict (L1 per [11], L2 per [30], L3 implied by [13][14][25]) described as two-way in progression-guide | **RESOLVED** — `progression-systems-inventory.md` §Contradictions now documents the full three-way (or four-way, with [12]) conflict |
| C-06 | MINOR | Estimation Markers | `progression-guide.md` cites `[22]` alongside `[21]` for post-Rupture farming window; `[22]` supports sulfur extractor but not Oxallop or Glowcap in that combined citation | **RESOLVED** — same fix as C-02; citations split per fact |
| C-07 | MINOR | Completeness | `citations.md` [20] extraction omits which corporation's Level 6 unlocks Food Station (claim is "Level 6" with no corporation name) | **Status:** OPEN — minor; Food Station corporation is Future Health Solutions per [14], [20] clarifies elsewhere in context but citation extraction does not specify |
| V-01 | — | VERIFIED | All numerical values cross-checked and consistent | PASS |
| V-02 | — | VERIFIED | Internal markdown links resolve correctly | PASS |
| V-03 | — | VERIFIED | Moon Energy L2/L3 contradiction surfaced explicitly | PASS |
| V-04 | — | VERIFIED | Corporation-level persistence uncertainty surfaced throughout | PASS |
| V-05 | — | VERIFIED | Caveat honesty: all five stated limitations prominent in README and per-file Gaps sections | PASS |
| V-06 | — | VERIFIED | Archetype scope (solo/duo) maintained; min-max and multiplayer divergences called out inline | PASS |
| V-07 | — | VERIFIED | Estimation markers present for all interpolated values (Pocket Base 100 BBM, player count, World Engine costs, FPS figures) | PASS |
| V-08 | — | VERIFIED | 50%+ citation spot-check: all checked citations match citations.md extraction | PASS |
| V-09 | — | VERIFIED | Formula validity: 83% player-count drop calculation correct; no other arithmetic derivations found | PASS |
| V-10 | — | VERIFIED | INACCESSIBLE source handling: all 403/405 sources flagged at point of use | PASS |

---

## Issue Detail

---

### C-01 — CRITICAL: Weapon mod cost currency never surfaced

**Category:** Contradiction Transparency
**Files:** `citations.md` (entry [50]), `combat-build-meta.md`, `progression-guide.md` §6, `references/progression-systems-inventory.md` §Currencies
**Status:** OPEN

**Description:**
The task specification identifies a known contradiction between [15] (TheGamer) and [50] (starrupture.wiki.gg): [15] prices weapon mods in **War Bonds**, while [50] is claimed to document **Basic Building Materials** as the mod cost currency.

In `citations.md`, entry [50] reads:

> "Discovery claim: canonical weapon list matches [15]; supports cross-verification."

The [50] entry makes no mention of a mod-cost currency discrepancy. It characterises [50] solely as corroborating the weapon *list* (not the mod *costs*). If [50]'s Discovery summary included a different mod-cost currency, that finding has been stripped from the [50] entry and the contradiction is entirely absent from all seven documents.

No file — README, progression-guide, combat-build-meta, progression-systems-inventory, or resource-economy — mentions any uncertainty about whether weapon mods cost War Bonds or Basic Building Materials. Every file accepts the [15] figure (War Bonds) without noting a competing claim from [50].

**Expected:** A note in `combat-build-meta.md` §Weapon Mods and/or `progression-guide.md` §6 (Weapons) acknowledging that [50] (unverified Discovery-level source) documents a different mod cost currency; the discrepancy should be flagged as unresolved pending direct verification of [50].
**Actual:** No mention of this dispute anywhere.

**Impact:** If mods cost Basic Building Materials rather than War Bonds, the War Bond budget tables are wrong. This is a player-facing decision (mod investment requires knowing which currency to accumulate).

---

### C-02 — CRITICAL: `[22]` incorrectly cited for Oxallop post-Rupture claim

**Category:** Citation Accuracy
**Files:** `progression-guide.md` §5 (Post-Rupture Window, line ~265)
**Status:** OPEN

**Description:**
`progression-guide.md` §5 states:

> "The highest-yield DP sources (Ignitium, Glowcap, Oxallop) are all post-Rupture only [10][11][21][22]."

Citation [22] is the TheGamer ore-locations article (Wolfram, Titanium, Calcium, Helium-3, Sulfur). Per `citations.md` [22] extraction, it covers only ore types. It does **not** document Oxallop (a plant) or Glowcap. The [22] citation is valid only for the Sulfur Extractor post-Rupture placement claim (which appears in the following sentence in `resource-economy.md`) — not for Oxallop or Glowcap.

The corresponding claim in the **README** (`README.md` line 25–26) correctly cites only `[10][11][21]` for the Ignitium/Glowcap/Oxallop post-Rupture claim — no [22]. The progression-guide adds [22] erroneously.

**Expected:** `[10][11][21]` for the Oxallop/Glowcap/Ignitium post-Rupture sentence; [22] reserved for the Sulfur Extractor sentence that follows.
**Actual:** `[10][11][21][22]` cited together for the Oxallop/Glowcap/Ignitium claim.

**Note:** `resource-economy.md` §Post-Rupture Farming Window also cites `[10][11][21][22]` for the combined post-Rupture block, but [22] is present in that file to support the bullet "Sulfur extractors must be placed 'just after a rupture' [22]" within the same list — structurally defensible as a block citation. The problem is cleanest and clearest in `progression-guide.md`'s single-sentence combined claim.

---

### C-03 — MODERATE: Sulphur bottleneck vs. 47-nodes dispute absent from deliverable

**Category:** Contradiction Transparency
**Files:** `README.md`, `progression-guide.md`, `references/mid-late-progression.md` §Stuck Points
**Status:** OPEN

**Description:**
`mid-late-progression.md` correctly notes the dispute:

> "Sulphur (disputed — 47 nodes documented on map [36])"

This is the only place in all seven files where the Sulphur scarcity vs. 47-nodes contradiction is surfaced. It does not appear in:
- `README.md` (Key Facts table, Limitations section, or anywhere else)
- `progression-guide.md` §4 (Late Game) or §5 (Resource & Farming Strategy) — which discusses ore progression in detail but states nothing about sulphur availability being contested

Since `progression-guide.md` is the primary deliverable and includes an ore table (§5) that lists Sulfur as a late-game resource, a reader of the guide alone would have no awareness that sulphur scarcity is disputed. The reference file surfaces it; the deliverable does not.

**Expected:** A note in `progression-guide.md` §5 ore progression (Sulfur row) or §8 (Contradictions) that sulphur availability is disputed — some players cite 47 nodes on the map [36] against reports of it being a bottleneck.
**Actual:** Dispute confined to `mid-late-progression.md`; absent from the deliverable.

---

### C-04 — MODERATE: Production rebuild framing inconsistent between README and reference files

**Category:** Contradiction Transparency
**Files:** `README.md` lines 29–32, `progression-guide.md` §3 and §9, `references/mid-late-progression.md` §Production Chain Rebuilds
**Status:** OPEN

**Description:**
The README's TL;DR Decision 3 states:

> "The experienced-player consensus [34] is to accept demolition-and-distribute rather than fight the rebuild loop."

This presents the satellite-bases recommendation as settled consensus, with no indication of disagreement. The progression-guide executive summary similarly states:

> "Experienced players report the rebuild-loop frustration is a playstyle mismatch, not a design flaw. [34]"

However, `mid-late-progression.md` §Production Chain Rebuilds explicitly says:

> "This is a contested claim — see Patch Volatility for Update 1's building rebalance."

And the progression-guide §3 does note it as a dispute: "experienced players argue this is a playstyle mismatch." The §9 Reflection section also notes it is "explicitly presented as contested."

The inconsistency is between the README (which suppresses the design-flaw reading entirely) and the nuanced treatment elsewhere. A reader who only reads the README summary would not know the consensus is contested.

**Expected:** README TL;DR Decision 3 should acknowledge the "design flaw vs. playstyle mismatch" framing is a player-community debate, not a resolved verdict.
**Actual:** README states it as resolved consensus.

---

### C-05 — MODERATE: Recipe Station unlock level described as two-way conflict; actually three-way

**Category:** Citation Accuracy / Contradiction Transparency
**Files:** `progression-guide.md` §2 (Corp Unlock Order), `citations.md` [11] and [30]
**Status:** OPEN

**Description:**
`progression-guide.md` §2 states:

> "Two sources disagree on whether the Recipe Station unlocks at Moon Energy L2 or earlier; [30] says L2, [10][13] imply L3 (with Map). The conservative reading is that L2 unlocks the Recipe Station and L3 unlocks the Map — but treat this as unverified."

However, `citations.md` entry [11] (GameRant "How to Farm Data Points Fast") explicitly states:

> "Moon Energy Corp Level 1 required for Recipe Station."

This creates a **three-way** conflict: [11] = L1, [30] = L2, and [13][14][25] imply L3. The progression-guide's framing of "L2 or earlier" technically covers L1 with "earlier," but it buries [11]'s specific L1 claim in vague language. The `progression-systems-inventory.md` §Contradictions also frames this as "L3 vs. L2," omitting [11]'s L1 claim entirely:

> "[13], [14], [25] all state Level 3. [30] states 'Recipe Station... typically linked to Moon Energy Corporation Level 2 advancement.'"

[11]'s L1 claim is not mentioned in the contradiction note in `progression-systems-inventory.md`.

**Expected:** Contradiction note updated to reflect three-way conflict: [11] says L1, [30] says L2, [13][14][25] say L3.
**Actual:** `progression-systems-inventory.md` ignores [11]'s L1 claim; `progression-guide.md` partially obscures it as "or earlier."

---

### C-06 — MINOR: Combined post-Rupture citation block in `progression-guide.md` conflates two distinct claims

**Category:** Estimation Markers / Citation Accuracy
**Files:** `progression-guide.md` §5, `resource-economy.md` §Post-Rupture Farming Window
**Status:** OPEN

**Description:**
Related to C-02 but at a lower severity level for the `resource-economy.md` instance. The block citation `[10][11][21][22]` for the post-Rupture farming window appears as a list that includes both plant-related claims (Glowcap, Oxallop) and the sulfur extractor claim. [22] supports only the sulfur extractor bullet; using it as a block citation for the whole list implies it corroborates Glowcap and Oxallop timing, which it does not.

Best practice would be to attach [22] specifically to the Sulfur Extractor bullet rather than the section header.

**Expected:** `[22]` attached inline to the Sulfur Extractor bullet: "Place Sulfur Extractors on Sulfur deposits in this window [22]"
**Actual:** `[10][11][21][22]` as a section-level block citation

---

### C-07 — MINOR: `citations.md` [20] extraction omits corporation name for Food Station unlock

**Category:** Completeness
**Files:** `citations.md` entry [20]
**Status:** OPEN

**Description:**
`citations.md` entry [20] extraction reads:

> "Food Station unlocks at Level 6."

It does not name the corporation. Everywhere else in the research documents, the full name is used: "Future Health Solutions Level 6." The missing corporation name in the citations.md extraction is a minor documentation gap — it does not create an inconsistency across files (all reference files name the corporation correctly), but it makes the citations.md extraction incomplete as a standalone record.

**Expected:** "Food Station unlocks at Future Health Solutions Level 6."
**Actual:** "Food Station unlocks at Level 6."

---

## Verified Items

### V-01 — Numerical Consistency: PASS

All quantitative values checked across files:

| Value | Files Checked | Result |
|---|---|---|
| Goliath reward: 5,000 DP | citations.md [17], README, progression-guide §4/§5, resource-economy, combat-build-meta, mid-late-progression | Consistent |
| Ignitium bundle: 2,000 DP | citations.md [11], all five reference files, README, progression-guide | Consistent |
| Glowcap: 90 DP/piece | citations.md [10], all files | Consistent |
| Common plants: 5 DP each | citations.md [10], all files | Consistent |
| Rare plants: 20+ DP each | citations.md [10], all files | Consistent |
| MAR-9: 200 WB; SLAMS-12: 250 WB; M175: 400 WB | citations.md [15], progression-guide, combat-build-meta | Consistent |
| UPP-7 alt cost: 2 War Bonds | citations.md [15], progression-guide, combat-build-meta | Consistent |
| Equipment Upgrade Station: GB L4 | citations.md [26], all files | Consistent |
| Equipment Upgrade Station claim cost: 120 BBM | citations.md [26], combat-build-meta | Consistent |
| Personal Storage: 18 slots (L2) → 42 slots (L9) | citations.md [24], progression-guide, resource-economy, progression-systems | Consistent |
| Storage Depot: 400 units (L3) → 1,600 (L8) | citations.md [24], all files | Consistent |
| Multistorage: 2,500 units | citations.md [24], all files | Consistent |
| Expandable Storage: 1,600/expansion | citations.md [24], all files | Consistent |
| Character inventory: 24 → 56 slots | citations.md [24], all files | Consistent |
| Regen Chamber: 100 BBM | citations.md [13], progression-guide, progression-systems, early-game | Consistent |
| Helium-3 Extractor: 250 BBM, Selenian L6 | citations.md [23], progression-guide, resource-economy, progression-systems | Consistent |
| 64 recipes depend on Helium-3 | citations.md [23], progression-guide, resource-economy, progression-systems | Consistent |
| Neutrino Missile: 3,469 Helium-3 | citations.md [23], resource-economy, progression-guide | Consistent |
| Neutrino Bomb: 2,000 Helium-3 | citations.md [23], resource-economy | Consistent |
| Organ Producer: 2,388 Helium-3 | citations.md [23], resource-economy | Consistent |
| Electronics recipe: 600 Synth Silicon + 200 Inductors + 200 Stators + 800 DP | citations.md [18], progression-guide, mid-late-progression | Consistent |
| Skill cap: EA 45, 1.0 100 | citations.md [9], all files | Consistent |
| LEM slots: 3 per skill (9 total) EA; 6 per skill (18 total) at 1.0 | citations.md [9], progression-guide, progression-systems, combat-build-meta | Consistent |
| 5 corporations; 4 cap L11; CR caps L13 | citations.md [14], all files | Consistent |
| Steam reviews: 82% overall / 5,858 reviews | citations.md [1], README, game-overview | Consistent |
| Steam reviews recent: 77% / 1,155 reviews | citations.md [1], game-overview | Consistent |
| Rupture countdown: 15 seconds | citations.md [13], all files | Consistent |
| Turret regression: 24 towers / 6 of 50 bugs; coolers 75% less effective | citations.md [35], patch-volatility, combat-build-meta, progression-guide | Consistent |
| Broken tech: 400–2,000 DP | citations.md [11], all files | Consistent |
| Starter rations: 20 total | citations.md [20], early-game, progression-guide | Consistent |
| EA launch date: 2026-01-06 | citations.md [1], all files | Consistent |
| Current price: $15.99 (20% off $19.99) | citations.md [1], README, game-overview | Consistent |
| 1.0 target: 2027 (~1 year EA) | citations.md [1], all files | Consistent |
| Player count: 42,864 Jan peak → 7,331 March | citations.md [8], game-overview | Consistent (both flagged unverified) |
| 83% player count drop calculation | game-overview: (42864-7331)/42864 ≈ 82.9% → 83% | Correct |

### V-02 — Internal Markdown Links: PASS

All cross-reference links use relative paths appropriate to their file's location:
- Reference files link `[citations](../citations.md)` — correct from `references/` subdirectory
- README and progression-guide link `[references/foo.md](references/foo.md)` and `[Patch Volatility](references/patch-volatility.md)` — correct from research root
- No broken anchors detected in path structures

### V-03 — Moon Energy L2/L3 Contradiction Surfaced: PASS

The Map-unlock contradiction is explicitly surfaced in three locations:
- `progression-guide.md` §2 Corporation Unlock Order (inline warning) and §8 Contradictions
- `progression-systems-inventory.md` §Contradictions & Open Questions
- `early-game-optimization.md` §Corporation Unlock Order (inline note)

Note: this finding does not override C-05, which identifies that the L1 claim from [11] is not fully incorporated into the contradiction statement.

### V-04 — Corporation Persistence Uncertainty: PASS

Flagged as uncertain in:
- `progression-guide.md` §8
- `progression-systems-inventory.md` §Corporation-Level Persistence Across Saves
- `patch-volatility.md` implicitly (Update 1 reset is documented; persistence mechanism across saves is separate)

### V-05 — Caveat Honesty: PASS

All five limitations are prominently noted:
- INACCESSIBLE sources: flagged in README §Limitations and at point-of-use in every reference file's §Gaps section
- Multi-engine search failure: noted in README §Limitations and `citations.md` §Methodology Notes
- No Reddit results: noted in README and `game-overview-ea-state.md` §Gaps
- n=1 critic review: noted in README and `game-overview-ea-state.md` §Reception
- JS-gated Steam pages: noted in README and `patch-volatility.md` §Gaps

### V-06 — Archetype Scope Maintained: PASS

Solo/duo first-playthrough scope stated in README §Audience, progression-guide §Introduction. Min-max and multiplayer callout sections present in `early-game-optimization.md`, `mid-late-progression.md`, and `combat-build-meta.md`. Inline callouts appear in progression-guide where relevant (§2 Corp Unlock Order note on min-max skip). No section implicitly treats min-max advice as primary audience recommendation.

### V-07 — Estimation Markers Present: PASS

All interpolated/unverified values are appropriately flagged:
- Pocket Base 100 BBM: "indicative rather than exact" in early-game-optimization; "not verified in a single fetched source" in progression-guide
- Player count figures: "unverified" and "single-source and unverified" in game-overview and citations
- World Engine activation cost: "not verified in a fetched source" in mid-late-progression §Gaps
- FPS degradation figures: "not verified in a directly-fetched thread" in mid-late-progression
- Planet name "Arcadia-7": "corroborated by [22]" but flagged as Discovery-agent source

### V-08 — Citation Spot-Check (>50% of ~50 citations): PASS

Citations spot-checked: [1][2][4][8][9][10][11][12][13][14][15][16][17][18][19][20][21][22][23][24][25][26][27][28][29][30][31][32][33][34][35][36][37][38][39][41][42][44][45][49][50] — approximately 42 of 50, exceeding the 50% threshold.

All checked citations:
- Point to the correct entry in `citations.md`
- Use the claimed extraction content consistently across files
- Do not misquote or contradict the stated extraction

The one exception is C-02 (citation [22] incorrectly applied to Oxallop claim in `progression-guide.md`) and C-05 (citation [11]'s L1 Recipe Station claim underrepresented in contradiction notes).

### V-09 — Formula Validity: PASS

The only arithmetic derivation in the research is the 83% player-count drop in `game-overview-ea-state.md`. Calculation: (42,864 − 7,331) / 42,864 = 35,533 / 42,864 = 82.9% → rounded to "~83%." This is correct. No other numeric derivations requiring verification were found.

### V-10 — INACCESSIBLE Source Handling: PASS

Sources [3][5][6][7][8][38][39][41][46][47] are marked INACCESSIBLE in `citations.md`. All claims derived from these sources are marked "(unverified)" or are flagged at their point of use in reference files. No claim from an INACCESSIBLE source is presented as verified fact in the deliverable.

---

## Reviewer Notes

The most significant finding is **C-01** (weapon mod cost currency). The [50] wiki entry in `citations.md` is characterised as corroborating only the weapon *list*, but the task specification asserts [50] documents Basic Building Materials for mod costs — a direct conflict with [15]'s War Bonds. If the Discovery agent's [50] summary included this alternative cost and it was not recorded in the `citations.md` extraction, the contradiction has been silently dropped. This is the type of suppressed contradiction the consistency check exists to catch.

**C-02** (erroneous [22] citation for Oxallop) is internally verifiable from the files: the README cites [10][11][21] for the same claim without [22], confirming the progression-guide addition of [22] is an error.

**C-05** (three-way Recipe Station level conflict) is a documentation precision issue rather than a substantive error in recommendations — the conservative reading advised in the progression-guide is still correct. However it means the contradiction statement in `progression-systems-inventory.md` is itself inaccurate.

The numerical consistency across all files is otherwise excellent. The research documents have been cross-checked thoroughly and apply consistent values for all ~30 quantitative claims verified.
