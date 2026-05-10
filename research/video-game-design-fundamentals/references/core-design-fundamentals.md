# Core design fundamentals

What this dimension covers: the durable, craft-level concepts that hold across project scales — game loops, mechanics, player agency, "game feel," meaningful decisions, prototyping the fun. The pieces that change least when team size and budget change.

Source numbers refer to entries in [`../citations.md`](../citations.md).

## The orthodox canon

Five frameworks dominate practitioner discourse on what game design *is*:

| Framework | Source | Core claim | Where it works |
|---|---|---|---|
| MDA (Mechanics → Dynamics → Aesthetics) | Hunicke, LeBlanc, Zubek 2004 [1] | Designers build mechanics; players experience aesthetics; dynamics are emergent runtime behavior in between. Eight aesthetic categories: Sensation, Fantasy, Narrative, Challenge, Fellowship, Discovery, Expression, Submission. | Action games, competitive games, formal analysis. |
| "Interesting decisions" | Sid Meier (GDC 1989, GDC 2012) [2] | "A game is a series of interesting decisions." Insignificant decisions take the same cognitive load as interesting ones but produce no satisfaction. Soren Johnson's complementary formula: fun = (meaningful decisions) ÷ (time played). | Strategy games, system-driven design, and most genres where choice is central. |
| Game feel | Steve Swink 2008 [3] | "Realtime control of virtual objects in a simulated space, with interactions emphasised by polish." Six components of virtual sensation. | Action, platforming, anything with real-time control. **Genre-specific** — confirmed by Pichlmair & Johansen's 2020 academic survey [4] which acknowledges the framework does not extend cleanly beyond action/platformer contexts. |
| Theory of fun | Raph Koster 2004 [5] | "Fun = learning." Pattern mastery drives engagement; cognitive chunking is the mechanism; games go boring when patterns are mastered, anxious when patterns are unrecognizable. | Mechanically rich games. **Excludes narrative as a mechanic** — Koster himself acknowledges this; practitioners (Frictional Games and others) have rebutted with shipped horror games where narrative *is* the mechanic. |
| Lenses | Jesse Schell (3rd ed. 2019) [6] | 100 perspective-shifting questions. Elemental Tetrad: Mechanics, Story, Aesthetics, Technology — all four equally weighted. | Diagnostic tool across all design phases. |

The frameworks are not mutually exclusive. Most working designers carry several and switch between them by problem.

## "Juice" / game feel — additive polish that disproportionately changes perceived quality

Two practitioner talks established the consensus that perceived game feel is largely additive polish on top of an unchanged underlying simulation:

- **Jonasson & Purho's "Juice It or Lose It" (GDC Europe 2012) [9]** demonstrated live that layering particles, screenshake, hit-pause, and sound on a bare Pong clone transformed the player experience without changing the underlying mechanic.
- **Jan Willem Nijman's "The Art of Screenshake" (INDIGO 2013) [10]** documented 30 specific techniques. The "sleep" frame-pause technique (~0.2s on enemy hit) is nearly invisible but perceptually load-bearing.

This is one of the most generalizable and verified findings in the dimension: small additive polish layers reliably and dramatically improve perceived game feel without redesigning the system underneath.

## Prototyping discipline

Rami Ismail [7] provides the cleanest distinction in the indie space:

- **Prototype** = "should you make this?" — disposable, fast, cheap. Tests whether the loop is fun.
- **Vertical slice** = "can you make this?" — production-quality, near-shipping content covering all systems. Marks the end of pre-production.
- "Most indies mix up the purpose of the Prototype and the Vertical Slice and lose out on a lot of time and money."

The distinction matters because the failure modes are different: a prototype proves the wrong thing if it's polished too early; a vertical slice misleads the team if it's treated as throwaway.

## Counter-perspective: the canon is not the territory

The canon is not consensus. The dimension's strongest counter-evidence:

- **MDA is architecturally limited.** Hunicke et al. assume a linear mechanics-to-experience pipeline that does not hold for narrative-driven or simulation games. Multiple Game Developer essays and a peer-reviewed MDPI paper document the framework's narrative blindness; proposed replacements (DDE, GFI) have not displaced it because the field tolerates a known-broken framework rather than adopting an unfamiliar one.
- **Game feel is genre-specific, not universal.** Pichlmair & Johansen's academic survey [4] explicitly says so. Liz England's review of Swink (separately documented in the discovery pool) makes the same point: turn-based, narrative, and puzzle games sit outside the framework's scope.
- **Successful games violate every "fundamental" at scale.** *Dark Souls* (27M+ copies across the trilogy) violated tutorial design and explicit feedback. Walking simulators *Firewatch* (2.5M copies) and *Gone Home* (700K) succeeded commercially with essentially no core gameplay loop. These are not edge cases — they are commercially significant counter-examples.
- **"Find the fun" prototyping has documented failures.** James Margaris (industry veteran) frames extended prototyping as "pseudo-scientific transposition of A/B testing" that prevents teams from holding a shared design vision; Spore is his named example. **Tom Francis [8]** offers the practitioner inversion: "Scope creep is a bad, dirty term, yet it's also been my fundamental development technique" — meaning the things players love about *Gunpoint* and *Heat Signature* came from unplanned expansion during prototyping, not from disciplined adherence to a pre-existing vision.

## What this means for solo and duo teams with AI augmentation

The fundamentals here are **the part AI does not change**:

- AI can generate a mechanic prototype faster, but cannot tell you whether the mechanic is fun. Alharthi (2025) [30]: "AI recognizes patterns and predicts likely outputs, but it doesn't grasp the cascading effects of a single tweak on balance, readability, or emotional tone."
- "Find the fun" iteration is unaltered by AI assistance. The cycle of prototyping, playing, observing, and revising remains the human's job because the evaluative judgment is the load-bearing step.
- Polish/juice is partially AI-assistable (asset generation, sound effect generation), but the *pacing* of polish — when to add screenshake, how long to make a hit-pause — requires direct play-testing.
- Scope discipline becomes more, not less, important. AI lowers the cost-per-feature, which makes scope creep easier and more tempting [8].

## Gaps and limitations

- **No empirical study** systematically compares orthodox-canon-following games to canon-violating games on commercial or critical outcomes. Both clusters succeed; both fail. The canon is taught as if validated.
- **Game feel** has no validated cross-genre measurement instrument. Practitioners use intuition and playtesting; academia has surveys [4] but not benchmarks.
- **The narrative-vs-mechanics debate** documented in Game Developer 2012 was never resolved. Both positions have shipped commercially successful games. The deliverable does not pick a side.
- **Solo/duo-specific design fundamentals** are not a distinct literature. Practitioner advice for solo devs largely re-applies team-scale frameworks. Whether some fundamentals matter more or less at this scale is empirically unaddressed.
