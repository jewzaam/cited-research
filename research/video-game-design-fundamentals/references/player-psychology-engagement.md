# Player psychology and engagement

What this dimension covers: motivation theory applied to games, retention metrics, what produces sustained play vs. churn, the engagement-vs-exploitation boundary. Source numbers refer to entries in [`../citations.md`](../citations.md).

## Self-Determination Theory (SDT) is the dominant framework — and the most-cited

SDT proposes that intrinsic motivation depends on satisfying three basic psychological needs:

| Need | Definition (in games) |
|---|---|
| **Autonomy** | Player actions feel self-chosen, not coerced. |
| **Competence** | Player feedback confirms skill growth and goal achievement. |
| **Relatedness** | Player feels connected to or significant to others. |

The foundational paper is **Ryan, Rigby, & Przybylski 2006** [11]. Studies 1–3 (lab) found in-game autonomy and competence predict enjoyment and pre/post well-being changes. Study 4 (multiplayer survey) confirmed all three needs independently predict enjoyment and intent to continue play. Operationalized via the **Player Experience of Need Satisfaction (PENS)** scale — 21-item, 7-point Likert, five subscales (autonomy, competence, relatedness, presence/immersion, intuitive controls).

## SDT critique — the framework is unquestioned, not validated

A 2024 ACM paper by **Tyack & Mekler** [12] reviewed N=259 HCI games papers using SDT. Findings:

- **54.83%** of papers used SDT only descriptively (citing it without testing it).
- Only **6 papers across the entire corpus** ever contested any SDT tenet.
- The PENS scale's validation commitments are largely unfulfilled in published literature.
- Core constructs are routinely miscoded — autonomy conflated with quantity of choices; competence conflated with superiority over opponents; relatedness studied almost only in multiplayer contexts.

This is not a replication failure of SDT itself but a critique of how games research applies it. The field uses SDT as an unquestioned paradigm.

## Flow theory — present but operationally incoherent

Csikszentmihalyi's flow concept (challenge matched to skill, clear goals, immediate feedback, altered time perception) maps intuitively to games. Jenova Chen's MFA thesis at USC (2006) is the canonical games application, leading to *Flow* (2007, thatgamecompany).

But **Abuhamdeh's 2020 review** [20] of 42 flow studies identified **24 distinct operationalizations**. **17 of 42** studies excluded enjoyment despite Csikszentmihalyi defining it as central. The construct has no stable empirical identity in games research — meaning when one paper says "flow predicts X" and another says "flow does not predict Y," the reader cannot easily compare them because the underlying measurement is different.

## Player typologies — Bartle is taught, Quantic Foundry is empirical

Richard Bartle's 1996 MUD-derived taxonomy [15] (Achievers, Explorers, Socializers, Killers) is still the most-taught player typology. Empirical critiques are well-documented:

- Nick Yee's factor-analytic work (~3,200 MMO players) found Bartle's Explorer type fractures into two uncorrelated factors (Discovery vs. Mechanics). The four types are not mutually exclusive as Bartle claimed.
- The widely-cited 80%/10%/10%/1% distribution (Socializers/Achievers/Explorers/Killers) appears on industry sites without a primary source — it is not from Bartle himself.

**Quantic Foundry's Gamer Motivation Model** [16], derived from 140K+ gamers (later 1.75M+), produces 12 motivations across 6 clusters: Action, Social, Mastery, Achievement, Creativity, Immersion. It is the empirically grounded successor — but commercial and unindependent of its developer, so academic uptake is limited.

## Mobile retention benchmarks — what the actual numbers look like

The widely-cited "good benchmark" of D1 ≥ 45%, D7 ≥ 20%, D30 ≥ 10% is **aspirational top-quartile or best-in-class performance, not industry average.**

Actual median figures (GameAnalytics 2025 [17], 11,600 apps, 1.48B MAU):

| Metric | Top 25% | Median | Bottom 25% |
|---|---|---|---|
| D1 | 26.48–27.69% | ~15% | 10–11.5% |
| D7 | 7–8% | 3.42–3.94% | ~1.5% |
| D28 | ~3%+ | ~0.85% | very low |

By genre (Mistplay/AppsFlyer Q3 2022 [18]):

| Genre | D1 | D7 | D30 |
|---|---|---|---|
| Match | 32.65% | 13.98% | 7.15% |
| Puzzle | 31.85% | 12.18% | 5.35% |
| RPG | 30.54% | ~8% | 3.48% |
| Hyper-casual | 29.31% | 5.90% | 1.38% |
| Shooting | 28.54% | 6.45% | 1.79% |
| Strategy | 25.30% | n/a | n/a |

**Match games sustain D30 retention ~5× better than hyper-casual.** iOS top-25% D1 is 31–33% vs Android 25–27%. Both medians declined from 2023 levels — attributed to record game releases in 2024 increasing competition. Solsten [19] frames the milestones qualitatively: D1 = "finding the fun," D7 = "feeling progression and social hooks," D30 = "sunk cost and commitment."

## Engagement vs. addiction vs. compulsion — a contested ethical line

**Niknejad et al. 2024 (ACM MUM)** [14] is the strongest empirical mapping of dark patterns in mobile games:

- N=1,496 mobile games analyzed via the community database darkpatterns.games.
- **85,000+ dark pattern instances identified.**
- **Only 10.76% of games had zero reported dark patterns.**
- 96.8% of "dark" games used F2P vs. 53% of "healthy" games.
- 93.6% IAP in dark games vs. 54% in healthy.
- Four pattern categories: Temporal (grinding, daily logins), Monetary (loot boxes, hidden costs), Social (peer pressure, viral loops), Psychological (cognitive bias exploitation).

The dark-pattern density correlates so strongly with F2P monetization that the two are structurally entangled, not optional design choices. This matters because most mobile success literature presents F2P + dark patterns as the success path.

**Karhulahti 2024** [13] argues "addictive" lacks construct validity as a design descriptor: "it is unclear whether 'addictive behaviour' should equally apply to someone being distracted by checking their smartphone regularly … and another person playing a massive multiplayer online game for decades." He proposes **vitality structures** instead — phenomenological dimensional constructs:

- **CLIMB** (felt upward progress) — hypothesized links to ADHD/ASD presentations.
- **FINAL STRETCH** (achievable goal nearly in reach) — hypothesized links to OCD.
- **ALERT** (attention spike from accessible information) — hypothesized links to anxiety.

Karhulahti is explicit that these are "evidence-based hypotheses" requiring validation, not validated constructs.

**Celia Hodent** [21] (former Epic UX Director) distinguishes engagement, excessive gaming, problematic gaming, and addictive gaming (DSM-5 IGD). Her estimate: only 0.3–1% of the global player base qualifies for clinical gaming disorder.

## What this means for solo/duo indie and mobile

- **D30 retention ~3% is the base case for mobile.** Practitioners citing the 40/20/10 benchmarks are describing top-quartile performance. A new mobile indie game hitting 5% D30 is doing well. Hitting 10% D30 puts it in genre-leading territory.
- **F2P monetization comes packaged with manipulative pattern density.** Choosing F2P is partly choosing into a design space where competition forces toward dark patterns. The 10.76% of games without reported dark patterns may underrepresent the available premium-only design space.
- **SDT remains the practical scaffold for thinking about motivation** — but practitioners should recognize they are using a paradigm, not a validated theory. Designing for autonomy/competence/relatedness is defensible; *claiming evidence* for specific design decisions on SDT grounds is not.

## Gaps and limitations

- **No indie-specific retention benchmarks** exist. All published retention data conflates studio sizes. A solo dev cannot easily benchmark against peers.
- **PENS scale validation** has unresolved issues (competence and intuitive controls load as one factor in some studies).
- **The "5% retention improvement = 95% profit increase" figure** widely cited in mobile gaming originates from Bain & Company's 1990s service-business research, not gaming. Use with skepticism.
- **Karhulahti's vitality structures** are theoretical; no validation studies have been published as of the research date.
- **Solo mobile play** has limited SDT research — the relatedness need is structurally absent in single-player contexts and the framework's adjustment for this is underspecified.
