# Fundamentals of video game design and development — and what drives game success

**Scope:** Indie and mobile games made by a solo developer or duo with agentic AI augmentation (Claude Code / Cursor / Copilot for code; image and audio generation tools for assets; LLMs for design exploration).

**Date:** 2026-05-10. Citation numbers reference [`citations.md`](citations.md). Reference files in [`references/`](references/) contain the per-dimension detail.

---

## Methodology

This document was produced under the [`cited-research`](../..) skill. Phase 1 dispatched 7 Discovery and 7 Counter-Discovery sub-agents in parallel (one of each per dimension), supplemented by multi-engine search via DuckDuckGo. The main thread WebFetched ~18 high-priority primary sources for direct verification. Phase 2 organized findings into [`citations.md`](citations.md) and seven reference files. Phase 3 synthesized the deliverable. Phase 4 (independent citation audit and consistency review) follows in [`audit/`](audit/).

The framing challenge surfaced in Phase 0:

1. "Success" was undefined in the original question. The deliverable distinguishes commercial subsistence, breakout success, and creative/critical success.
2. "Fundamentals" implies stability; the field is unusually volatile. The deliverable marks which fundamentals are durable and which are current market conditions.
3. Survivorship bias dominates this literature. The deliverable surfaces base rates and includes a dedicated failure-modes dimension.
4. Mobile and indie diverge structurally — F2P retention/ARPU vs. premium launch/discoverability — and are treated as related-but-distinct.

---

## TL;DR

For a solo developer or duo using AI augmentation in indie/mobile, the durable fundamentals split into three layers:

**Layer 1 — Craft fundamentals that AI does not change.** Game loops, meaningful decisions, game feel, "find the fun" prototyping, scope discipline. Iteration on these still requires human judgment ([1]–[10], [29]–[30]). AI changes the cost-per-feature, not the cost-per-decision.

**Layer 2 — Player engagement realities that the canonical literature mis-teaches.** SDT is a paradigm, not a validated theory ([11], [12]). Median mobile D28 retention is **~0.85%**, not the widely-cited "good benchmark" of D30 ≥ 10% [17]. Dark patterns are present in 89% of mobile games and structurally entangled with F2P [14]. Bartle's player types are taught but empirically displaced by Quantic Foundry's data [15], [16].

**Layer 3 — Commercial reality that "how to succeed" advice obscures.** The median Steam indie game grosses **$249** in 2025 [42]. **79% of 2024 Steam releases were classified "Limited"** by Valve [77]. **83% of mobile games fail within 3 years** [73]. Sponsored Twitch streams have **median ROI of -95%** [68]. Comparable-quality games show **500× revenue differences** attributable to chance [60]. The base rate of indie financial viability is **~0.5%**.

The honest summary: **most indie games fail, AI lowers the cost of features but not the cost of judgment, and the difference between hits and comparable flops is dominated by quality + luck + sustained marketing — not by following success patterns extracted from outliers.** Solo or duo with AI augmentation makes the cost curve more favorable but does not change which decisions matter.

---

## What changes for tiny teams with AI, and what doesn't

### What AI changes

- **Boilerplate and scaffolding code** is faster to produce, *if* the developer can evaluate the output. The METR randomized controlled trial [29] is the most rigorous data: experienced developers using Cursor + Claude on mature codebases took **19% longer with AI** despite predicting 24% speedup and self-reporting 20% speedup. Greenfield indie work may behave differently, but the structural finding (developers feel faster than they are) is plausible.
- **Asset iteration speed** for concept art, mood boards, placeholder visuals, and sound effects. AI is a starting point — production assets still require hand-finishing, style coherence enforcement, and integration work.
- **Marketing copy, social media drafts, narrative drafts, localization first drafts.** All require editing for tone and platform conventions.
- **The cost-per-feature for boilerplate-heavy work** drops materially. Practitioner reports (Tenjin, Alharthi [30]) describe specific cases like "2–3 hours of chess game logic in 2–3 minutes," but no controlled study confirms this scales to project-level outcomes.

### What AI does not change

- **Whether a mechanic is fun.** Alharthi 2025 [30]: "AI recognizes patterns and predicts likely outputs, but it doesn't grasp the cascading effects of a single tweak on balance, readability, or emotional tone." Fun-finding remains the bottleneck.
- **Scope discipline.** AI lowers the cost of implementing features, which makes it easier to scope-creep. Tom Francis's [8] distinction — creep *toward the discovered core* vs. *away from it* — becomes more important, not less.
- **Discoverability and marketing.** No AI tool solves the Steam algorithm or wishlist-building problem. Press coverage doesn't reliably convert (The Wreck [83]: 20K wishlists, RPS Bestest Best, ~1,000 sales at launch).
- **Community trust.** Players are sensitive to undisclosed AI use; the GDC 2026 follow-up survey shows **52% of game industry professionals believe gen AI has a negative impact** [34]. Frontier removed AI portraits from *Jurassic World Evolution 3* after wishlist deletions [41].
- **Legal exposure.** Andersen v. Stability AI [39], the SAG-AFTRA settlement [37], and Steam's evolving disclosure policy [38] all create real compliance surface that did not exist 18 months prior.

---

## The seven dimensions, synthesized

### 1. Core design fundamentals

Five frameworks dominate practitioner discourse: MDA [1], Sid Meier's "interesting decisions" [2], Swink's game feel [3], Koster's theory of fun [5], Schell's lenses [6]. They are not mutually exclusive. None has been empirically validated as predictive of commercial outcomes; all are useful as language and diagnostic tools.

The most generalizable concrete finding: **additive polish ("juice") disproportionately improves perceived game feel without changing the underlying simulation.** Demonstrated live by Jonasson & Purho [9] and Nijman [10]. The "sleep" frame-pause technique (~0.2s on enemy hit) is invisible but perceptually load-bearing.

The clearest practical distinction tiny teams routinely conflate: **prototype** ("should you make this?", disposable) vs. **vertical slice** ("can you make this?", production-quality, near-shipping) per Rami Ismail [7]. Treating them as the same wastes polish on prototypes that should die.

The contested counter-finding: orthodox fundamentals are not universal. Game feel is genre-specific [4]. Walking simulators succeed without core loops. Dark Souls violates UX orthodoxy. Tom Francis's [8] practitioner inversion — "scope creep is a bad, dirty term, yet it's also been my fundamental development technique" — names a real failure mode of pre-planned design discipline.

[Full dimension: `references/core-design-fundamentals.md`](references/core-design-fundamentals.md)

### 2. Player psychology and engagement

Self-Determination Theory (autonomy, competence, relatedness) [11] is the dominant framework. Tyack & Mekler 2024 [12] reviewed 259 SDT-using HCI games papers and found 54.83% used it descriptively only; only 6 papers contested any tenet. **SDT functions as an unquestioned paradigm, not a validated theory** in games research. Designing around SDT is defensible; *claiming evidence* on SDT grounds is not.

Flow theory has 24 distinct operationalizations across 42 studies [20] — the construct has no stable empirical identity. Bartle's player types [15] are taught but empirically displaced by Quantic Foundry's 12-motivation, 6-cluster model derived from 1.75M+ players [16].

The **mobile retention reality is far worse than commonly cited benchmarks suggest.** Median D1 ~15%, median D7 3.42–3.94%, **median D28 ~0.85%** per GameAnalytics 2025 [17]. The widely-cited "good" benchmarks of D1 ≥ 45% / D7 ≥ 20% / D30 ≥ 10% describe top-quartile performance, not industry average.

Genre matters dramatically: Match games sustain D30 retention ~5× better than hyper-casual [18].

The dark-pattern finding is the most empirically grounded result in the dimension: **only 10.76% of analyzed mobile games had zero reported dark patterns** [14]. **96.8% of "dark" games used F2P** vs. 53% of "healthy" games. F2P monetization and dark patterns are structurally entangled in current practice.

[Full dimension: `references/player-psychology-engagement.md`](references/player-psychology-engagement.md)

### 3. Production process for tiny teams

**2–3× timeline overruns are typical for solo developers**, not exceptional. The Last Humble Bee shipped 9-months-estimate / 27-months-actual [22]. Tower of Guns took 3,850 hours over 600 days, with marketing consuming 25% of total time [23]. Mark of the Ninja shipped at 16 months total — a small-studio success — but 4 of those months were unfocused work [24].

Scope and creative-depth tradeoffs produce 5–10× extensions when intentional: Stardew Valley [25] (~5 years solo, 50M+ copies); Dwarf Fortress [26] (20+ years and counting since 2002, ~711K LoC); Caves of Qud [27] (9 years in Steam Early Access, "lifestyle over maximum profit").

Methodology consensus: **Scrum-style sprints (1–4 weeks, always-playable product) outperform Waterfall** for indie teams per Sophie Smart [28] and Rami Ismail's milestone framework. The cost of ignoring this: losing "find the fun" iteration to refactor periods.

The "average indie dev time is 18 months" figure circulating in community discussions does not have a verifiable primary source — likely AI-aggregated folklore. Use case data (above) instead of folklore averages.

[Full dimension: `references/production-process-tiny-teams.md`](references/production-process-tiny-teams.md)

### 4. Disciplines and AI augmentation

A solo developer must personally cover programming, art, audio, design, narrative, QA, marketing, community, business/legal, and production. **AI adoption is real but contested:** 36% of game developers personally use generative AI per GDC 2025 [32]; 90% report "AI in workflows" per Google Cloud's broader-definition survey [33]; 84% of general developers per Stack Overflow 2025 [31]. **Sentiment is moving against AI even as adoption rises** — 30% believe gen AI harms the industry per GDC 2025, up 12 points YoY; 52% per the GDC 2026 follow-up [34].

**Where AI takes meaningful load (with caveats):** boilerplate code, asset concepting and mood boards, background/ambient audio (with paid commercial-license tools), marketing copy first drafts, localization first drafts.

**Where AI does not help — and may hurt:** mechanic balance and fun-finding; narrative cohesion across long arcs; style coherence across asset sets ("gameslop"); curation requires sophisticated taste novice developers may lack; debugging AI-generated code in custom systems.

**Real exposure:** Steam disclosure policy [38] (~8,000 disclosed games by mid-2025), Andersen v. Stability AI ongoing [39], SAG-AFTRA settlement at 95.04% ratification with consent/disclosure requirements for digital replicas [37], copyright unprotectability for AI-only works in the US.

**Player rejection is documented and commercially material.** Frontier Developments removed AI portraits from *Jurassic World Evolution 3* pre-launch after wishlist deletions [41].

[Full dimension: `references/disciplines-solo-duo-with-ai.md`](references/disciplines-solo-duo-with-ai.md)

### 5. Commercial success — indie and mobile

The Steam revenue distribution is steeply power-law:

| Metric | 2025 value |
|---|---|
| Median indie gross | **$249** ($174 net) [42] |
| Games earning under $1K | **66%** [42] |
| Games earning under $50K | **90%** [42] |
| Games earning over $1M | **0.5%** [42] |
| Games earning $100K+ in 2025 | **5,863** total ([43]; ~1,700 are new 2025 titles per Carless estimate) |

**The 7,000-wishlist threshold ≈ Popular Upcoming threshold ≈ Gold-tier Steam Next Fest cutoff.** Below this, organic Steam discovery is essentially closed. Wishlist conversion variance is enormous: median 0.15× for games with 25K+ wishlists [46]; top performers (Peak) reach 29.29×. Quality (91% positive vs 67%) and time-on-storefront (214 vs 411 days) predict the variance.

Mobile is bigger but more concentrated: $82B IAP in 2024 [51], but **top 1% of publishers generate 90%+ of store revenue** [52]. Tencent alone earned $6.2B in 2024 — over 3× the second-place publisher, ~100× a credible indie breakout [57]. F2P unit economics depend on whales: **2.3% of F2P players spend money; top 10% of payers ≈ 64% of revenue** [55].

ARPU by mobile genre [53]: hypercasual $0.86, match $2.99, merge-3 $14.83. Most genres need 3× LTV/CAC for breakeven; for hypercasual, this is structurally hard.

Steam algorithm consensus: **revenue drives algorithmic visibility**, not wishlists or reviews directly [59]. Wishlists feed Popular Upcoming and Discovery Queue; broader recommendation surfaces are revenue-momentum-weighted.

[Full dimension: `references/commercial-success-indie-mobile.md`](references/commercial-success-indie-mobile.md)

### 6. Critical and cultural success

Review scores correlate with sales but explain a small fraction of variance. Bracket-correlation [70]: Metacritic 90+ averages ~800K copies, 80–89 ~250K. Practitioner counter [71]: two-thirds of 90+ games sell under 2M; *CoD: Finest Hour* (76) sold 4M+. Academic ML synthesis [72]: Metacritic correlates positively but has lower feature importance than Steam metrics.

For Steam specifically, **review tier labels are the impulse-purchase signal.** "Overwhelmingly Positive" (≥95% from 500+ reviews) drives the strongest conversion; "Mostly/Very Positive" (≥80%) is the psychological purchase threshold.

**Sponsored Twitch streams have median ROI of -95%** per Kellogg/Northwestern peer-reviewed research [68]. Organic streams produce ~3% player gain and outperform sponsored streams (the source notes "sponsored streams showed even smaller effects than organic streams"; the precise multiplier is not given in the source). Two exceptions where sponsored streams produce positive returns: lesser-known indies and critically acclaimed titles — exactly the indie-breakout overlap.

The five most-discussed cultural breakouts (Among Us, Vampire Survivors, Balatro, Stardew Valley, Hades) share: low entry friction (price, accessibility), replayability that produces recurring content-creation value, streamer/content-creator compatibility, sustained post-launch updates, and developer authenticity signals. Long tail medians are modest: Year 1 ≈ 4× Week 1; Year 5 ≈ 8.77× Week 1; Early Access games reach 20.34× by Year 5 [49]. "Stegosaurus tail" outliers (Lethal Company 507×, Pizza Tower 22.5×) are the exceptions [50].

[Full dimension: `references/critical-cultural-success.md`](references/critical-cultural-success.md)

### 7. Failure modes — the dimension the question didn't ask

**The honest base rates:**

- **79% of 2024 Steam releases classified "Limited"** [77] (worsened from 66% in 2020).
- **~50% of 2025 Steam releases earned fewer than 10 reviews.**
- **Median lifetime gross: $249** [42].
- **~0.5% of 2024 indie releases achieved financial viability** [60].
- **83% of mobile games fail within 3 years** [73] (caveat: SuperScale-commissioned).
- **Median mobile D28 retention: ~0.85%** [17].

**Structural patterns:**

- **Survivorship bias dominates "how to succeed" advice** [78]–[80]. Failed devs are silent. Marketing tactics that worked briefly become obsolete. Even experienced studios cannot reliably replicate their own successes.
- **Luck dominates skill among quality-filtered games.** Comparable-quality 2024 indies showed **500× revenue differences** attributable to factors outside developer control [60].
- **Press coverage doesn't reliably convert** — *The Wreck* [83]: RPS "Bestest Best", 20K wishlists, ~1,000 launch-week sales.
- **Even correct pre-launch behavior can be negated by platform failure** — Planet Centauri's wishlist email bug eliminated 130K subscribers' notifications, producing ~581 launch-week sales (secondary-attested).

**Anti-patterns** (Cliff Harris [82], postmortem synthesis): oversaturated genre choices without genre expertise; engine/tool switching mid-project; marketing as afterthought; insufficient post-launch support. AI-augmentation-specific anti-patterns (emerging): undisclosed AI use, stylistically incoherent AI assets ("gameslop"), AI voices without performer consent.

[Full dimension: `references/failure-modes-indie-mobile.md`](references/failure-modes-indie-mobile.md)

---

## What actually drives game success — the cross-dimensional synthesis

Putting the seven dimensions together:

### 1. Quality is necessary, not sufficient

Across [70], [72], [60], [46], [49]: review scores correlate with sales but explain a small fraction of variance. The best-converting Steam games have ≥91% positive reviews [46]. Quality is the entry filter. Among quality-filtered games, outcome dispersion is dominated by other variables.

### 2. Discoverability is the gate, and the gate is narrow

The median Steam game has too few wishlists to access organic algorithmic surfaces. The 7,000-wishlist threshold for Popular Upcoming is binary in practical effect. Below it, the algorithm is closed; above it, conversion variance is wide [46], [47]. Marketing that builds wishlists is not optional; it is the precondition.

### 3. The breakout pattern is replayability + accessibility + streamer-compatibility + sustained updates

Among Us, Vampire Survivors, Balatro, Stardew Valley, Hades all share these traits [61]–[67]. The roguelike skew in the breakouts is not coincidental — runs produce content-creator clipping moments by structure. Stardew Valley is the outlier: not roguelike, but matched the others on accessibility and sustained-update commitment.

### 4. Mobile success requires whale-acquisition infrastructure that tiny teams lack

The whale concentration [55] (top 10% of payers = 64% of revenue), publisher concentration [56], [57] (Tencent alone 6.2B), and dark-pattern density in F2P [14] (96.8% of "dark" games are F2P) point to the same structural conclusion: **F2P mobile is structurally unviable for tiny teams.** Premium mobile or premium PC are more honest paths.

### 5. The "make games you love and they'll come" advice is dangerous

Cliff Harris [81]: "the default position for an indie game developer is pretty much poverty." Shahrabi [60]: 0.5% of 2024 indie releases achieved financial viability. Survivorship bias [78], [79] makes success advice systematically misleading. Luck and timing dominate skill among quality-filtered games. Plan financially around the median outcome ($249 gross), not the marketed ones.

### 6. AI changes the cost curve, not the decision curve

AI helps with cost-per-feature for the 30% of work that is boilerplate, scaffolding, and asset placeholders. AI does not help with the 70% that is design judgment, balance, taste, fun-finding, or community. METR [29] is the most rigorous available data point against the "AI doubles productivity" claim. The honest framing: AI is a useful tool that requires the same discipline (small teams that historically shipped without AI mostly used the same disciplines).

### 7. Failure mode is the rule, not the exception

Plan for failure as the base case. ~80%+ failure rate by any financial-viability definition. Build the cheapest viable first project. First-game average gross is $120K, third-game $209K [42] — there is a real experience effect, but only if you survive to make a second and third game. Many do not.

---

## Reflection pass

Before finalizing, the synthesis above was checked for overstatement and suppressed contradiction:

- The Tom Francis scope-creep counter [8] is in tension with the conventional "scope is the killer" framing. The synthesis names this tension and frames the diagnostic question (toward or away from the discovered core) rather than picking a side.
- The METR finding [29] is generalized cautiously — the study itself notes generalizability limits to mature OSS contexts. The deliverable does not claim AI net-harms greenfield indie work; it cites the structural finding (developers feel faster than they are) as plausible.
- The "0.5% indie financial viability" figure [60] uses a 50× review-multiplier methodology, not confirmed sales data. The deliverable cites it but the gap notes flag the caveat.
- The "$1M in first 8 hours" figure for Balatro circulating elsewhere is not in the verified Game Developer source [64]; the deliverable does not make this specific claim.
- The Planet Centauri 130K-wishlists / 581-sales / Valve acknowledgment timeline is widely reported but the primary URL (PC Gamer) did not return readable content in this run; the deliverable marks it as secondary-attested.
- "Most games fail" is a strong claim. The deliverable supports it with: 79% Limited [77]; $249 median [42]; 0.5% financial viability [60]; 83% mobile failure [73]. Each has methodology caveats noted in the relevant reference file. The aggregate picture across four independent measures supports the headline.

---

## Open questions and honest gaps

- **No controlled comparison of AI-augmented vs. non-augmented solo dev outcomes** has been published. All productivity claims are self-reports, anecdotes, or general-software studies (METR) generalized to game work.
- **No clean indie-specific retention benchmarks** for mobile exist. All published retention data conflates studio sizes.
- **No quantified IGF / Day of the Devs commercial-impact data** was located.
- **Several primary URLs returned binary content, paywalls, or 404s** during the research run (SDT 2006 PDF, GamesRadar Planet Centauri, Springer DOI). Backups via secondary sources are noted in [`citations.md`](citations.md) where applicable.
- **The Ma et al. ML study on success drivers [72]** is paywalled — claims are drawn from search snippet, not full text.
- **Apple App Store algorithm changes (June 2025, October 2025)** are partially documented; ASO rankings have shifted but post-2025 cohort data is not yet available.
- **Player sentiment about AI in games is changing rapidly in both directions.** Current numbers (52% negative per GDC 2026) may not reflect the situation in 12 months.
- **The "indie mobile dev with AI" demographic is empirically under-studied.** This deliverable triangulates from broader datasets; a dedicated study would substantially refine its conclusions.
