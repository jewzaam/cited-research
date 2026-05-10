# Commercial success drivers — indie and mobile

What this dimension covers: discoverability, wishlists and conversion, marketing channels, monetization models, platform dynamics, base rates, and survivorship. Source numbers refer to entries in [`../citations.md`](../citations.md).

## The Steam revenue distribution is steeply power-law

The clearest published 2025 numbers (Ziva synthesis of VG Insights, Alinea Analytics, GameDiscoverCo, and Valve GDC 2026 [42]):

| Metric | Value |
|---|---|
| Median Steam indie gross revenue (2025) | **$249** (~$174 net after Valve's 30% cut) |
| Games earning under $1,000 lifetime | **66%** |
| Games earning under $50,000 lifetime | **90%** |
| Games earning over $1M lifetime | **0.5%** |
| Debut game average gross | $120,000 |
| Third-game average gross | $209,000 |

Older data point as a check: Zukowski's 2019-cohort analysis [74] found median lifetime gross ~$1,136. The 2025 figure is much lower because the denominator (number of games released annually) has grown faster than total spend on indie games.

Valve's GDC 2026 disclosure [43]: **5,863 games earned $100,000+ on Steam in 2025**, up from ~3,000 in 2020. This is a record. Context: ~150,000 games on Steam total; ~20,000 released in 2025; only ~1,700 of the 5,863 were *new 2025 titles* (Carless estimate). After Valve's 30% cut and taxes, $100K gross ≈ $50K net — insufficient for a multi-person team.

Industry critic response (Kotaku [59 — see also citations.md additional]): "more games are making money on Steam" framing is misleading. Only ~4% of all Steam games clear $100K lifetime; ~100K games earn effectively nothing.

VG Insights 2024 segmentation [44]: indie segment breaks into triple-i 53% / small teams 20% / middle market 19% / hobbyists 8%. Indie share of Steam revenue: 48% in 2024 (inflated by Black Myth: Wukong classification), settling to **25% of Steam's $17.7B total in 2025** [45].

## Wishlist conversion — variance is enormous

GameDiscoverCo / Simon Carless [46] (Sept 2024 – Sept 2025):

| Wishlist tier / condition | Median first-week conversion |
|---|---|
| Games with 25K+ wishlists | **0.15×** |
| Games priced > $10 | **0.10×** |
| Top converters (e.g., Peak) | up to **29.29×** |
| Underperformers | well under 0.10× |

The variance is the headline. A game with 100K wishlists could convert to 10K first-week sales (median) or 290K (top of the distribution). Two predictive variables:

- **Review score:** top converters averaged 91% positive in week 1; underperformers averaged 67%.
- **Time on storefront:** top performers averaged 214 days pre-launch vs. 411 days for underperformers — long pre-launch periods can hurt by accumulating cold (stale) wishlists.

## Steam Next Fest — the most data-rich festival channel

Zukowski's February 2026 Next Fest survey [47] (n=182 dev responses):

| Pre-fest wishlists | Median wishlists gained during SNF |
|---|---|
| 0–999 | 322 |
| 1,000–10,000 | 1,006 |
| 10,000–100,000 | 5,215 |
| 100,000+ | 12,882 |

**Median demo-to-wishlist conversion: 16.33%.** Pre-fest wishlist count is the dominant predictor of SNF gain (Spearman r = 0.825) — meaning the rich get richer; SNF amplifies existing momentum more than it creates new momentum from cold starts.

Approximate thresholds: **7,000 wishlists ≈ Popular Upcoming threshold ≈ Gold tier SNF cutoff.** 100K+ wishlists target for popup featuring. 30–50K wishlists target for $250K+ revenue tier.

## The 2024–2025 indie market shift

Zukowski's 2024 retrospective [48]:

- 25% more games reached 1,000+ reviews in absolute terms.
- 31% more total releases — so the **success rate fell from 2.56% in 2023 to 2.44% in 2024.**
- Genre stability: horror #1 for the third consecutive year. Farming subgenre 52.63% success rate at the 700+ follower tier; 2D platformers 2–3%.
- TikTok absent as a working marketing channel for Steam.

## Long tail — typically modest, occasionally massive

GameDiscoverCo long-tail data [49] (~100 dev survey):

| Time period | Multiplier of Week 1 revenue (median) |
|---|---|
| Year 1 | **4×** |
| Year 5 | **8.77×** |
| Year 5, Early Access games | **20.34×** |

But the median understates the tail's potential. The "stegosaurus tail" pattern [50] — viral spike events months or years post-launch — produces extreme outliers:

| Game | First-year vs. first-week ratio |
|---|---|
| Lethal Company | 507× |
| Class of '09 | 106× |
| Pizza Tower | 22.5× |
| Median 2023 cohort | 2.64× |

Long tails are typically modest; cultural-spike long tails are extreme. The honest median multiplier is 2–4× Week 1 in Year 1.

## Mobile is bigger but more concentrated

Sensor Tower 2025 data [51], [52]:

- **Mobile game IAP revenue: $82B in 2024 (+4% YoY); $81B in 2025 (flat).**
- 49B downloads in 2024 (-7% YoY).
- **Top 1% of publishers generate 90%+ of store revenue.**
- Hybridcasual IAP +37% YoY in 2024.

Top mobile publishers by revenue [56], [57]:

| Publisher | H1 2024 | Full-year 2024 |
|---|---|---|
| Tencent | $3.2B | $6.2B |
| Scopely | $931M | $1.96B |
| NetEase | $912M | $1.67B |

**Tencent alone earns ~3× the second-place publisher and ~100× a credible indie breakout.** This is the structural reality for indie mobile: the market has consolidated around franchise incumbents, not new entrants.

## ARPU by genre — the unit economics

Appodeal mobile casual benchmarks 2025 [53] (US Android, 10,000+ games, June 2024–Jan 2025):

| Genre | ARPU (lifetime, ad-revenue) |
|---|---|
| Hypercasual | **$0.86** |
| Match | $2.99 |
| Party | $4.90 |
| Luck Battle | $12.23 |
| Merge 3 | **$14.83** |

Admiral Media 2025 [54]: hypercasual Android CPI $0.25–$0.80; iOS $0.50–$1.50. Midcore RPG Android CPI $2.50–$6.00; iOS $4.00–$12.00. **Breakeven requires LTV ≈ 3× CAC** in standard mobile economics; for hypercasual, that means ARPU $0.86 vs CPI $0.50 leaves almost no margin without retention extension.

## Whales — the F2P revenue is a long-tail-of-payers problem

Swrve 2015 data [55], structurally consistent with newer Unity 2025 data:

- **2.3% of F2P players spent any money.**
- **Top 10% of payers = 64% of revenue.**
- **Under 0.25% of all players drove the majority of IAP.**

The newer Unity 2025 figure: top 5% of payers ≈ 50–65% of IAP. The shape persists across a decade.

This is the structural pivot point for mobile commercial success: the model survives on whale concentration. Designing for whales aligns with the dark-pattern findings in [14] — F2P optimizes for the top of the spending distribution, which produces the dark-pattern density at the bottom.

The peer-reviewed **Zendle et al. 2022 [58]** classifies 35 distinct manipulation techniques across 8 domains in F2P design — pay-to-skip, currency manipulation, pay-for-quality-of-life, etc. — and frames them as exploitation of psychological vulnerabilities.

## Steam algorithm — known unknowns

Erik Johnson's foundational 2018 piece in Game Developer [59] documents Steam's algorithmic opacity. The October 2018 algorithm change reduced traffic to games not meeting an undisclosed daily revenue threshold; developers experienced unexplained traffic drops they could only observe, not explain. Subsequent practitioner work (Zukowski, Carless) has narrowed the picture but the algorithm remains a black box. Practitioner consensus: **revenue drives algorithmic visibility, not wishlists or reviews per se** — wishlists feed Popular Upcoming and Discovery Queue, but the broader recommendation surfaces are revenue-momentum-weighted.

## Marketing — what actually works

The honest practitioner picture as of 2025–2026:

- **Steam page optimization is the highest-ROI marketing surface.** Capsule, screenshots, GIFs, trailer, tags, demo. Cheap and fully under the dev's control.
- **Streamer/YouTuber discovery** is high-variance. The Kellogg study [68] found median sponsored-stream ROI of -95%, but lesser-known indies are one of two exceptions where sponsored streams produce positive returns.
- **TikTok organic reach declined sharply in early 2025.** Devlogs that earned 800K views in 2024 now average 300–800. Paid TikTok wishlist conversion runs under 1% at $500–$2,000 spend.
- **Steam Next Fest** is the highest-leverage festival event for SNF-eligible projects, but only amplifies existing wishlist momentum [47].
- **Press coverage doesn't reliably convert.** *The Wreck* [83] received Rock Paper Shotgun "Bestest Best," accumulated ~20,000 wishlists, and **sold ~1,000 copies at launch.** Florent Maurin: "press coverage doesn't magically convert people."

## Shahrabi's luck-dominance argument (2024)

Shahriar Shahrabi's Medium analysis [60] of ~12,000 2024 indie Steam releases:

- After filtering for quality (200+ reviews, 90%+ positive), 108 games remained.
- **Top 8.33% of those 108 captured 80% of revenue.**
- ~0.5% of all 12,000 indie releases achieved financial viability.
- Comparable-quality games show 500× revenue differences attributable to factors outside developer control (algorithmic placement timing, incidental coverage, release window).

Caveat: revenue estimates use a 50× review-count multiplier, an industry approximation rather than confirmed sales data.

## What this means for a 1–2 person team

- **The base case is the median: $249 gross / $174 net.** Plan financially as if your game will earn this. Anything above is upside.
- **Quality threshold matters more than wishlist count.** A 91% positive review rate at launch is a stronger predictor of conversion than wishlist count alone [46].
- **7K wishlists is the floor for organic discovery.** Below this, Steam algorithmic surfaces are essentially closed.
- **Mobile F2P unit economics are punishing for indies.** Without franchise scale or whale acquisition pipelines, the math rarely works. **Premium mobile** ($3–10 paid) avoids the whale dependency but caps revenue per user.
- **TikTok and other social channels** are unreliable. Steam page + Next Fest + targeted creator outreach is the highest-confidence playbook in 2026.
- **Long tail is real but typically modest.** Plan around Year 1 revenue ≈ 4× Week 1, not Lethal Company's 507×.

## Gaps and limitations

- **The 5,863 / $100K Valve figure** [43] does not break out new-2025 vs back-catalog earnings; the new-2025 estimate of ~1,700 is Carless's, not Valve's.
- **The Ziva $249 median** synthesizes multiple sources; full methodology audit not publicly available.
- **No clean data** on indie marketing-spend ROI as a function of total budget — the relationship between marketing dollars and outcome is observational, not experimental.
- **Mobile failure rate of 83% within 3 years** [73] comes from a SuperScale-commissioned survey of 500 devs — Atomik Research methodology, but vendor incentive caveat.
- **"Wishlist quality matters more than count"** is a real GameDiscoverCo finding but no controlled study isolates the variable; the GameDiscoverCo data is observational.
- **App Store Editors' Choice impact** is widely cited but the most-quoted "1,747% download boost" figure is from Apptopia and predates iOS 15+ algorithm changes; current data not located in this run.
