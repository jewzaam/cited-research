# Failure modes — indie and mobile

What this dimension covers: the base rates and structural patterns of commercial failure, anti-patterns in design and production, and the survivorship-bias problem that distorts most "how to succeed" advice. Source numbers refer to entries in [`../citations.md`](../citations.md).

This is the dimension that the user's original question did not ask. It is included because studying only successful games is the field's most common methodological flaw. The honest base rate on Steam is dismal; the mobile picture is worse.

## Steam base rates

| Metric | Value | Source |
|---|---|---|
| 2024 Steam releases classified "Limited" by Valve | **~79% (14,951 reported)** | Kotaku/SteamDB [77] |
| 2025 Steam releases earning fewer than 10 reviews | **~50%** | Multiple sources |
| 2025 Steam releases with zero reviews | **~10%** (~2,100 games) | Per Discovery agent / SteamDB |
| Median Steam indie gross revenue (2025) | **$249** | Ziva [42] |
| Indie releases (2024) achieving financial viability | **~0.5%** | Shahrabi [60] |
| Top 8.33% of qualifying games (200+ reviews, 90%+) capture | **80% of revenue** | Shahrabi [60] |

The "Limited" classification is the most useful failure proxy: Valve withholds full community features from games that fail undisclosed sales/engagement thresholds. The figure has worsened from 66% in 2020 → 72% in 2022 → 79% in 2024.

The 2019-cohort median of $1,136 lifetime gross [74] vs. the 2025 cohort median of $249 [42] reflects the denominator effect: total annual releases roughly doubled from 2020 to 2025 with no proportional expansion of buyer attention.

## Mobile base rates

SuperScale survey of 500 UK/US mobile developers (Atomik Research, Nov 2023) [73]:

- **83% of mobile games fail to survive beyond 3 years.**
- **43% are cancelled before launch.**
- 76% reach peak revenue in year one; only 4% peak in year two.
- 38% of developers neglect regular content updates.

Mobile retention base rates [17]: median D28 is **~0.85% across all games** (GameAnalytics reports D28, not D30). Top-25% achieves only ~3% at D28. Practitioner "good benchmark" of D30 ≥ 10% represents top-decile or better, not median.

Caveat: SuperScale is a live-ops vendor with commercial interest in framing post-launch failure as recoverable. The 83% / 3-year framing serves their pitch. The directional finding is consistent with mobile retention data and consolidation patterns.

## Documented individual failure cases

From Dan Bruno's failure postmortem compilation [75] and other sources:

| Game | Developer | Outcome |
|---|---|---|
| Super Win the Game | Kyle Pittman | ~900 first month — "complete and total failure" |
| Airscape | Daniel West | ~150 lifetime — PR costs exceeded projected revenue |
| Trials of Azra | 2-person team | ~200 first month — $100 marketing budget |
| Drunk Shotgun [76] | Alexey Strelkov | **$4,006 dev cost, $35.57 revenue.** CPI $0.41, LTV $0.02, CAC $120. Facebook/Instagram rejected ads for "guns, violence, blood and alcohol references." |
| The Wreck [83] | The Pixel Hunt | RPS "Bestest Best", ~20K wishlists, **~1,000 sold at launch.** "Press coverage doesn't magically convert people." |
| (Various per Bruno [75]) | n=many | Sub-1K-unit launches dominate the bucket of "shipped but not sustainable" |

These are *not* worst-case failures — they are *medium failures*: developers who shipped, had enough audience to publish a postmortem, and chose to do so. Catastrophic failures (cancelled mid-development; studios that folded before launch; first-time devs who never published) are structurally absent from the postmortem corpus.

## The survivorship bias problem

This is the dimension's most important methodological point.

**Tyler Haddad's argument [78]:** Failed devs are silent. They have no audience, no reputational incentive to document failure, and often no willingness. Success narratives circulate; failure narratives mostly do not. Indie dev culture extracts "lessons" from outliers and generalizes them as best practices.

**Khabibrakhmanov's GDC 2014 talk "Everybody Lies: Survivorship Bias" [79]** documents the structural pattern: industry data collection skews toward satisfied users; dissatisfied users disengage silently. Frameworks built on visible success produce flawed strategic guidance.

**Paul Kilduff-Taylor's "10 secrets to indie game success (and why they do not exist)" [80]:** Marketing tactics that worked briefly become obsolete within months. Even experienced studios (Mojang, Boss Key) cannot reliably replicate their own successes. The takeaway: most "patterns" extracted from successes are post-hoc storytelling, not transferable causation.

**Cliff Harris (Positech Games) [81]:** "The default position for an indie game developer is pretty much poverty." Even 36 years of coding experience and a profitable back catalog do not reliably generate press for a new release. This is a credentialed practitioner counter to "make games you love and they will come."

**Shahrabi's 2024 luck-dominance argument [60]:** comparable-quality games show 500× revenue differences attributable to factors outside developer control — algorithmic placement timing, incidental coverage, release-window collisions with AAA, a Sony executive happening to like the game. Quality is a necessary filter; outcome dispersion among quality-filtered games is dominated by chance.

## Anti-patterns identified across postmortems

Synthesized from postmortem analysis (Game Developer compilations, Cliff Harris [82]):

**Design anti-patterns:**
- Late content integration — narrative or systems retrofitted into existing implementations.
- Generic tool-building — building engine features instead of game features.
- Polish phase compression — running out of time at the end and shipping unbalanced.
- Choosing oversaturated genres without genre expertise (Cliff Harris cites 2D puzzle platformers [82]).

**Production anti-patterns:**
- Engine/tool switching mid-project — "almost all indies chop and change … this is utter madness" (Harris [82]).
- Treating marketing as optional — "tweeting a WIP screenshot once a week is not a marketing plan" (Harris [82]).
- Insufficient post-launch support (Harris [82] recommends 12 months / 40+ patches; 5% of mobile devs continue support past 7 years [73]).

**Mobile-specific anti-patterns:**
- Relying on F2P + IAP without the franchise scale to acquire whales.
- Predatory monetization driving player trust collapse (top 5% spenders = 50–65% of IAP per Unity 2025 / Swrve 2015 [55]).
- Showing ads too frequently — immediate uninstalls.
- Pivoting to F2P after premium failure too late (LawBreakers / Boss Key Productions cited as the canonical case in the Counter-Discovery pool).

**AI-augmentation-specific anti-patterns (emerging 2024–2026):**
- Undisclosed AI use → review bombs and refund campaigns even when scores are unaffected (Frontier Developments / *Jurassic World Evolution 3* [41]).
- AI assets without coherence pipelines → "gameslop" — visually mismatched asset sets that break immersion.
- Voice cloning without performer consent → SAG-AFTRA strike precedent [37] establishes legal exposure.

## Scope creep — real but contested as the dominant cause

The conventional indie wisdom is "scope creep is the killer." Multiple postmortems support this (Weersing's 9→27 months [22]; the *Untitled Paper RPG* 9-year cancellation surfaced in the Discovery pool).

The contested view is from **Tom Francis [8]:** scope creep is the *fundamental development technique* for projects whose creative core is not pre-existing in the design document. The failure mode in Francis's framing is not scope expansion per se — it is scope expansion *away from the discovered core* (rule 4: creep "in that direction").

Both views are supported by case evidence. The synthesis: undisciplined scope creep destroys projects that don't ship; disciplined scope creep produced *Gunpoint*, *Heat Signature*, and most loved indies. The diagnostic question is not "did the project expand?" but "did the expansion converge toward a discovered core, or away from one?"

## Platform-failure modes — when the system itself fails the developer

The clearest documented case: **Planet Centauri (Permadeath, 2024).** Per multiple secondary sources:

- ~10 years in Early Access, accumulated ~130,000 wishlists.
- At 1.0 launch, Steam's wishlist notification system had a bug (affecting fewer than 100 releases since 2015) and never emailed the wishlist subscribers.
- Result: ~581 units sold in the first 5 days.
- Nine months passed before Valve acknowledged the bug in writing. Valve offered a Daily Deal slot as compensation; by then the developer's financial position made continued support infeasible.

(Caveat: the PC Gamer article URL did not return readable content during this research run; details are from secondary attestation. Marked as **secondary-attested, unverified at audit** in [`../citations.md`](../citations.md).)

The lesson: even correct pre-launch behavior (long EA, large wishlist) can be negated by platform infrastructure failure. Steam algorithm changes (Erik Johnson's 2018 Game Developer piece [59]) similarly demonstrate that opaque platform decisions can destroy a project mid-cycle.

## What this means for a 1–2 person team

- **Plan for failure as the base case.** Median Steam indie revenue is $249. The 80%+ of games that earn near-zero are not statistical anomalies — they are the modal outcome.
- **Ship something small first.** First-game average gross is $120K, third-game $209K [42] — there is a real experience effect, but only if you survive long enough to make a second and third game.
- **Survivorship bias contaminates almost all "how to succeed" advice.** Treat practitioner playbooks as approximations of patterns visible in successes, not as reliable causal recipes.
- **Marketing is not optional and starts before development is finished.** Wishlist building requires ~12+ months of pre-launch attention; the median Steam indie that doesn't market loses access to algorithmic surfaces entirely.
- **F2P mobile is structurally unviable for tiny teams** without franchise scale or whale acquisition pipelines. Premium mobile or premium PC are the more honest paths, even at lower revenue ceilings.
- **AI use creates new failure modes.** Disclose AI assets per Steam policy [38]. Use AI tools with explicitly licensed training data where possible. The downside risk of undisclosed AI use is now larger than the upside from speed.

## Gaps and limitations

- **The "85% of indie games fail" figure** circulating in indie communities has no definitive primary source. The structural data (79% Limited, $249 median) is consistent with a failure rate above 80% by any financial-viability definition, but the specific 85% number should not be cited as a discrete fact.
- **The "70% of indies cite scope as the killer" figure** traces to an unlinked Gamasutra reference and is not verifiable. Use the case-evidence pattern (Weersing 3×, etc.) instead.
- **The Planet Centauri 130K wishlists / 581 units / Valve acknowledgment timeline** is documented in multiple secondary outlets but the PC Gamer primary URL did not resolve cleanly during this research. Marked as secondary-attested.
- **Failure-attribution data is structurally biased toward shipped, communicative developers.** The true distribution of failure modes (especially for never-shipped projects) is empirically unknowable from the available literature.
- **Mobile failure causes** are difficult to disentangle. UA cost, product quality, and store policy all contribute simultaneously; controlled separation does not exist publicly.
- **No academic meta-study** of indie failure modes was located. Available academic postmortem analyses (Washburn et al. 2016, ICSE; Petrillo & Pimenta 2009) analyze shipped games only, embedding survivorship bias in the corpus.
