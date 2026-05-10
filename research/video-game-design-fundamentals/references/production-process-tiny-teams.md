# Production process and scope management for tiny teams

What this dimension covers: pre-production, prototyping, vertical slice, scope discipline, methodology adapted for 1–2 person teams, where AI assistance changes production speed, why solo/small projects overrun. Source numbers refer to entries in [`../citations.md`](../citations.md).

## Timeline overruns of 2–3× are typical, not exceptional

Concrete documented postmortems with verified numbers:

| Project | Developer | Estimate vs. actual | Notes |
|---|---|---|---|
| The Last Humble Bee | Jacob Weersing [22] | 9 months → **27 months (3.0×)** | GameMaker; 10 min–2 hr/day; shipped Nov 2024 at $4.99 |
| Tower of Guns | Joseph Mirabello [23] | n/a → **3,850 hours / 600 days (~20 months)** | Solo FPS; 25% of time on marketing (983 hrs); efficiency 55–67% in early phases |
| Mark of the Ninja | Klei (Anderson, Cheng) [24] | n/a → **16 months** | Small team (~5–10 people); 4 months of unfocused early work wasted "art and animation"; 2-month focused pre-production established direction |
| Stardew Valley | Eric Barone [25] | n/a → **~5 years** | Solo; ~10 hrs/day, 7 days/week; originally titled "Sprout Valley"; 50M+ copies by Feb 2026 |
| Dwarf Fortress | Tarn Adams [26] | "decade" → **20+ years and counting** | Solo; ~711K lines of code; donation-funded for 16+ years; Steam release Dec 2022 |
| Caves of Qud | Freehold Games (2 people) [27] | n/a → **9 years in Steam Early Access** | Explicit "lifestyle over maximum profit" stance; 1.0 Dec 2024; OpenCritic 95% |

**Pattern:** 2–3× overruns are common for solo developers; 5–10× extensions exist for projects whose creators traded time for depth (Stardew Valley, Caves of Qud, Dwarf Fortress).

The figure circulating in indie communities — "average indie game takes 18 months" — does not have a verifiable primary source and traces to AI-aggregated industry-statistics sites. Treat as folklore. The verifiable distribution: simple-scope solo games ship in 1–6 months; medium-ambition solo projects run 1–3 years; large-ambition solo projects run 4+ years.

## Prototype vs. vertical slice — a distinction tiny teams routinely conflate

Per Rami Ismail [7]:

- **Prototype** = "should you make this?" Disposable, fast, cheap. Tests whether the core loop is fun before any production investment.
- **Vertical slice** = "can you make this?" 3–5 minutes of polished gameplay covering all core systems at near-shipping quality. Marks the end of pre-production.
- "Most indies mix up the purpose of the Prototype and the Vertical Slice and lose out on a lot of time and money."

The Mark of the Ninja postmortem [24] is the canonical small-team success: 4 months of unfocused work (in retrospect, partially-failed prototyping); 2-month focused pre-production summer 2011; bi-weekly Craigslist playtesting starting ~8 months in; shipped without significant overtime.

## Scope discipline — the cliche and its honest counter

The conventional advice — "scope is the indie killer" — is supported by case evidence (Weersing's 3× overrun, every postmortem citing scope as a contributor) but has a credentialed counter-position:

- **Tom Francis [8]** (*Gunpoint*, *Heat Signature*): "Scope creep is a bad, dirty term, yet it's also been my fundamental development technique. If I'd stuck to my original plan on those games, I wouldn't be here today: I'd just be someone with a slightly boring, unfinished hobby project. All of the good things in those games came from ideas that I found along the way." Heat Signature shipped roughly 2 years late; the lateness was load-bearing for the game's quality.
- His four rules: (1) pick an idea that's quick to prototype, (2) prototype the important parts, (3) decide which is the core, (4) creep as far as you like in *that direction*.

Both positions are right at different scales: undisciplined scope creep destroys projects that don't ship; disciplined scope creep produced the games we celebrate. The framework that distinguishes them is whether the scope expansion is *toward the discovered core* or *away from it*.

## Methodology — sprints over Waterfall

Sophie Smart (Blossom Arcade) at London Games Festival 2026 [28] argues for Scrum-style sprints (1–4 weeks, always-playable product) over Waterfall for indie teams. Quote: "Your scope document is not your plan. That is just a list of tasks." The sprint approach maintains a constantly-playable product, which is the only reliable way to keep "find the fun" iteration alive.

Heart Machine's *Hyper Light Drifter* used gaming events (PAX, MineCon) as informal milestones — externally-imposed playable-build deadlines. The game shipped March 2016 against an originally-targeted 2014 release; the delay was driven by health challenges, not methodology.

## Where AI changes the production curve

The honest summary: **AI changes the cost-per-feature for some tasks, not the cost-per-decision for any task.**

Where AI helps in production:

- **Boilerplate and scaffolding code:** plausibly faster, though see [29] on net effect.
- **Asset iteration speed:** faster mood boards, faster placeholder art, faster sound effect variants.
- **Marketing copy generation:** faster Steam page descriptions, social media variants, localization first drafts.
- **Dialogue and narrative drafting:** faster first drafts of barks, item descriptions, NPC chatter.

Where AI does not help — and may hurt:

- **METR's randomized controlled trial [29]** (n=16 experienced open-source developers, 246 issues): developers using Cursor Pro + Claude 3.5/3.7 Sonnet **took 19% longer** with AI than without. Pre-study they predicted 24% speedup; post-study they still believed they were 20% faster. Caveat: study limited to mature OSS codebases with experienced devs; greenfield indie work may behave differently. The study itself flags this limitation.
- **Stack Overflow 2025 survey [31]:** 46% of developers distrust AI accuracy (up from 31% in 2024). 45% cite debugging AI-generated code as time-consuming. 84% use or plan to use AI tools (up from 76% in 2024) — adoption is rising even as trust is falling.
- **GDC 2025 State of the Industry [32]:** 36% of developers personally use generative AI; 30% believe it negatively impacts the industry (up 12 pts year-over-year).
- **Alharthi's peer-reviewed survey [30]:** 75%+ of game design professionals say AI accelerates task completion, but 60%+ are worried about reduced originality. AI cannot reason about how a single mechanic tweak propagates through balance, readability, and emotional tone — those remain the human's job.

## What this means for a 1–2 person team with AI augmentation

- **Plan for 2–3× your initial estimate.** This holds with or without AI, because the bottleneck is design judgment, not feature implementation speed.
- **Use the prototype/vertical-slice distinction explicitly.** Tiny teams blur them constantly; the cost is wasted polish on prototypes that should have died.
- **Treat scope creep nonbinary.** Creep toward the discovered fun (Tom Francis's rule 4); cut anything else aggressively. AI lowers the cost of feature implementation, which makes scope discipline *more* important, not less — every unnecessary feature implemented quickly still has to be balanced, integrated, and maintained.
- **Sprint-based, always-playable methodology** is consensus practitioner advice. The cost of ignoring it is losing "find the fun" iteration to refactor periods.
- **Treat the METR finding as a serious data point.** Even if greenfield game work behaves better than mature OSS work, the structural pattern — developers feel faster than they are with AI — is plausible. Track your own time, not your perception.

## Gaps and limitations

- **No controlled comparison** of AI-augmented vs. non-augmented solo game-dev timelines exists. All productivity claims are self-reports or anecdotes.
- **The "average indie dev time" figures** circulating in community discussions do not have verifiable primary sources.
- **The METR study's generalizability to game development specifically** is limited. The study covered open-source maintenance, not greenfield game implementation. Game work involves more art-asset and balance iteration than typical OSS.
- **No empirical study has tested whether the prototype/vertical-slice distinction actually correlates with shipping or commercial outcomes** — it is consensus practitioner advice, not validated practice.
- **Postmortem culture has structural survivorship bias** — devs who don't ship don't write postmortems, so the timeline data understates failure rates.
