"""Persist fetched source content to the cited-research data dir for the audit phase."""
import os
from pathlib import Path

DATA_DIR = Path.home() / ".local" / "share" / "cited-research-data" / "video-game-design-fundamentals"
DATA_DIR.mkdir(parents=True, exist_ok=True)

SOURCES = {
    "stardew-valley.md": """# Fetched: https://en.wikipedia.org/wiki/Stardew_Valley
# Date: 2026-05-10
# Status: OK

## Sales and Success
- By February 2026, the game had sold over 50 million copies (26 million on PC, 7.9 million on Nintendo Switch)
- Became one of the best-selling video games ever made

## Development Timeline
- Originally titled "Sprout Valley"
- Took approximately 5 years to develop
- Released for Windows on February 26, 2016

## Critical Reception
- Metacritic by platform: PC 89, Xbox One 89, Switch 87, PS4 86, iOS 88
- OpenCritic: 99 percent recommend (75 reviews)
- IGN raised score to 10/10 after the 1.6 update (July 2024)

## Developer Background
Eric Barone (ConcernedApe) created the game solo, handling all pixel art, music, sound effects. Graduated from University of Washington Tacoma in 2011.

## Inspiration
Designed as a modern, fan-made alternative to later Harvest Moon titles.
""",

    "wishlist-conversion.md": """# Fetched: https://newsletter.gamediscover.co/p/the-state-of-steam-wishlist-conversions
# Date: 2026-05-10
# Status: OK

## Median Conversion Rates
- Games with greater than 25k wishlists: 0.15x median conversion
- Games priced over 10 dollars: 0.10x median conversion
- Overall baseline: approximately 0.11x to 0.17x

## Key Variables
- Lower-priced titles convert better than premium-priced
- Adult/NSFW games and co-op titles showed outsized conversion (6 to 539x expected)
- Time on storefront: top performers averaged 214 days pre-launch, underperformers averaged 411 days

## Study Parameters
Period: September 2024 through mid-September 2025
Source: GameDiscoverCo Pro subscriber data (paywalled)

## Review correlation
Top converters averaged 91 percent positive reviews. Underperformers averaged 67 percent (Mixed rating).
""",

    "vampire-survivors.md": """# Fetched: https://en.wikipedia.org/wiki/Vampire_Survivors
# Date: 2026-05-10
# Status: OK

## Launch and Initial Reception
- Released for macOS and Windows on October 20, 2022
- Early access began December 2021
- Reached over 30,000 concurrent players by late January 2022, later surpassing 70,000

## Creator Background
Luca Galante developed the game while unemployed, drawing inspiration from his gambling industry background and the Castlevania series. He spent approximately 1100 pounds on initial assets.

## Critical Recognition
- Metacritic scores: PC 87/100, Xbox Series X 95/100, iOS 91/100
- Won two BAFTA awards (2023): Best Game and Game Design
- Nominated for five BAFTA categories total
- Also won at Golden Joystick Awards (Breakthrough Award) and DICE Awards (Action Game of the Year)

## Commercial Success
By August 2024, creator Galante was estimated to have accumulated 40 million pounds, making him among the UK wealthiest game developers.

## Notable Achievement
The game is considered a pioneer of the bullet heaven genre.
""",

    "hades.md": """# Fetched: https://en.wikipedia.org/wiki/Hades_(video_game)
# Date: 2026-05-10
# Status: OK

## Release Timeline
- Early Access launched December 6, 2018 on Epic Games Store
- Full release: September 17, 2020 (macOS, Nintendo Switch, Windows)
- Console ports (PS4/PS5, Xbox One/Series X|S): August 13, 2021
- iOS release via Netflix Games: March 19, 2024

## Critical Reception
Metacritic scores remained consistent across platforms at 93/100. OpenCritic indicated 99 percent recommend status. Universal acclaim per aggregators.

## Commercial Success
During its nearly two-year early access period, the title sold 700,000 copies. Following official launch, an additional 300,000 units sold within three days, bringing lifetime total to over one million.

## Awards Recognition
Game of the Year honors from BAFTA Games Awards, DICE Awards, and Game Developers Choice Awards. First video game recipient of the Hugo Award.

## Developer Context
Supergiant Games operated as a small team of about 20 employees. The studio had previously released Bastion, Transistor, and Pyre.
""",

    "among-us.md": """# Fetched: https://en.wikipedia.org/wiki/Among_Us
# Date: 2026-05-10
# Status: OK

## Original Launch Date
The game released on June 15, 2018 for iOS and Android, with a Windows/Steam launch following on November 16, 2018.

## Viral Momentum Timeline
Twitch streamer Sodapoppin first popularized the game on Twitch in July 2020, with other major content creators like xQc, Pokimane, and Shroud following suit. Surge gained traction by mid-2020, driven initially by creators in South Korea and Brazil.

## Peak Concurrent Players
The game reached 1.5 million concurrent players by September 2020, then peaked at 3.8 million in late September.

## Total Downloads
By September 2020, the game exceeded 100 million downloads. By November 2020, SuperData Research estimated roughly 500 million players worldwide.

## 2020 Mobile Revenue Share
The free-to-play mobile version accounted for 97 percent of players but the buy-to-play PC version generated 64 percent of the game gross revenue.

## Developer Team Context
Innersloth is identified as the developer/publisher. The core creative team included Marcus Bromander (designer/composer), Forest Willard (programmer), and Amy Liu (artist).
""",

    "balatro.md": """# Fetched: https://www.gamedeveloper.com/business/balatro-sells-5-million-copies-after-end-of-year-spike
# Date: 2026-05-10
# Status: OK

## Total Sales Figure
Balatro has sold 5 million copies as of January 2025, following a significant end-of-year spike.

## Timeline to Milestones
- February 2024: Initial launch across PC, PlayStation 4/5, Xbox One/Series X|S, and Nintendo Switch
- First three days: 250,000 copies sold
- Mid-December 2024: 3.5 million units sold
- January 2025: 5 million copies sold

## Game Awards Impact
LocalThunk specifically credited interest from the game nomination in various categories at the 2024 Game Awards. The game won Best Indie, Best Mobile, and Best Debut Indie at the event.

## Publisher
PlayStack published the title.

## Note
Article does not provide platform-specific sales breakdown or profitability timeline within hours. The 1 million dollar in 8 hours figure was not in this article.
""",

    "metr-2025.md": """# Fetched: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
# Date: 2026-05-10
# Status: OK

## Study Design
Randomized controlled trial (RCT) with 16 experienced developers from large open-source repositories. Developers were randomly assigned issues (246 total, averaging 2 hours each) to complete either with or without AI tool access. Developers recorded screens and self-reported implementation times. Compensation: 150 dollars per hour.

## Sample Size and Slowdown
- 16 developers participating
- 246 total issues completed
- 19 percent slowdown when using AI tools

## Developer Predictions vs Actual Results
- Developers expected AI to speed them up by 24 percent before the study
- After experiencing the slowdown, they still believed AI had sped them up by 20 percent
- Actual result: AI made them 19 percent slower

## Key Quote
When developers are allowed to use AI tools, they take 19 percent longer to complete issues, a significant slowdown that goes against developer beliefs and expert forecasts.

## Limitations Acknowledged
- Only 16 developers (potential sampling bias)
- Cursor Pro usage averaged about 50 hours
- Represents experienced open-source developers only
- Tasks from high-quality codebases with strict quality standards

## Study Dates
Published July 10, 2025. Follow-up data on late-2025 AI tools published February 2026.
""",

    "kellogg-twitch.md": """# Fetched: https://insight.kellogg.northwestern.edu/article/video-game-companies-are-spending-big-on-sponsored-streams
# Date: 2026-05-10
# Status: OK

## ROI Metrics
- Median return on investment for sponsored streams: negative 95 percent
- Organic streams increased players by approximately 3 percent
- Sponsored streams showed even smaller effects than organic streams

## Research Methodology and Scope
- Sample size: Top 60,000 streamers on Twitch
- Time period: May to December 2021 (5 months)
- Data collection: Every 10 minutes when streamers went live
- Sources: Steam (player counts), Comscore (sales data)

## Cost Estimates
- Average approximate hourly earnings for streamers: about 144 dollars per hour
- Historical reference: 2019 report cited top-tier streamers receiving up to 50,000 dollars per hour from major publishers

## Performance by Game Type
The research identified two exceptions where sponsored streams showed positive returns:
1. Lesser-known games from small developers
2. Games with high critical ratings

Morozov notes that most games showed deeply negative returns, describing typical cases as a really really bad deal.
""",

    "valve-100k.md": """# Fetched: https://www.gamedeveloper.com/business/valve-says-5-836-titles-earned-over-100-000-on-steam-in-2025
# Date: 2026-05-10
# Status: OK

## Key Metrics
5,863 games earned over 100,000 dollars on Steam in 2025, according to Valve GDC 2026 presentation. Up from approximately 3,000 titles achieving this threshold in 2020.

## Tom Giardino quote
Dramatically more games are finding success on the PC storefront. Comparable expansion across higher revenue tiers, with consistent growth trends at 500,000 and 1 million thresholds.

## Platform Performance
- Peak concurrent users: 42 million
- In-game concurrent users: 13.9 million (double the 2020 figure)

## Note
Article does not provide: exact total 2025 releases, breakdown between new titles vs back-catalog, or Carless estimate. The 5,863 figure includes all historical games still earning, not just 2025 releases.
""",

    "niknejad-dark-patterns.md": """# Fetched: https://arxiv.org/html/2412.05039v1
# Date: 2026-05-10
# Status: OK

## Study Overview
Researchers from the University of Bremen analyzed 1,496 mobile games from the community-driven website darkpatterns.games to quantify manipulative design practices.

## Key Findings

Dark Pattern Prevalence:
- Over 85,000 instances of dark patterns were identified across the sample
- Only 10.76 percent of games showed zero reported dark patterns
- Dark games averaged significantly higher dark pattern counts than healthy games

Business Model Correlation:
- 96.8 percent of dark games used free-to-play models versus 53 percent of healthy games
- 93.6 percent of dark games included in-app purchases compared to 54 percent of healthy games
- 52.4 percent of dark games contained advertisements versus 37.3 percent of healthy games

## Dark Pattern Categories
Four manipulation types: Temporal (forcing time investments), Monetary (hidden costs and purchase pressure), Social (exploiting peer relationships), Psychological (cognitive biases and false illusions).

## Research Context
Published at ACM MUM 2024 (International Conference on Mobile and Ubiquitous Multimedia).
""",

    "mobile-failure-83.md": """# Fetched: https://mobilesyrup.com/2023/11/23/mobile-games-failure-rate-report/
# Date: 2026-05-10
# Status: OK

According to a SuperScale report conducted by Atomik Research surveying 500 game developers across the UK and US, the mobile gaming industry faces significant challenges:

Key Findings:
- 83 percent of mobile games fail to survive beyond three years
- 43 percent are cancelled before launch
- 76 percent reach peak revenue in their first year
- Only 4 percent hit peak revenue in year two
- 38 percent of developers neglect regular content updates

Notable casualties include Nintendo Dr Mario World and Dragalia Lost, plus Niantic Harry Potter Wizards Unite.

Two-thirds of studios have conducted layoffs or budget cuts. Only 5 percent continue supporting games after seven years, yet 78 percent of developers still prefer working on mobile titles despite the grim outlook.

The mobile gaming industry remains lucrative, projected at 90 billion USD annually, but success requires sustained engagement.
""",

    "tom-francis-scope.md": """# Fetched: https://www.gamedeveloper.com/design/scope-creep-a-useful-treacherous-tool-says-i-heat-signature-i-dev
# Date: 2026-05-10
# Status: OK

## His Core Philosophy
Francis stated: Scope creep is a bad, dirty term, yet it has also been my fundamental development technique. He argued that without allowing his projects to expand beyond initial plans, he would have remained an amateur hobbyist rather than a successful game developer.

## The Heat Signature Experience
Heat Signature development took approximately two years longer than originally scheduled. Unlike Gunpoint, where prototyping revealed the game core mechanic organically, Heat Signature required building nearly the entire game to test whether the concept worked, making scope management significantly more challenging.

## His Four Rules for Healthy Scope Creep
1. Choose a game idea that is quick to prototype
2. Prototype the important parts
3. Decide which should be the core
4. Creep as far as you like in that direction

## The Prototyping Imperative
Until you make something you don't know anything. He advocates for hands-on testing to determine what genuinely works.

GDC 2018 talk reference.
""",

    "sag-aftra-strike.md": """# Fetched: https://en.wikipedia.org/wiki/2024-2025_SAG-AFTRA_video_game_strike
# Date: 2026-05-10
# Status: OK

## Dates and Duration
- Start: July 26, 2024
- End: July 9, 2025 (ratification date)
- Total: 11 months, 1 week, 6 days

## Primary Reason
The strike centered on artificial intelligence protections. Workers demanded safeguards against companies using AI to replicate performer voices and likenesses without informed consent or fair compensation.

## Settlement Details
- Tentative agreement: June 9, 2025
- Strike suspended: June 11, 2025
- Ratification: July 9, 2025 with 95.04 percent member approval

## Key Terms Achieved
- Consent and disclosure requirements for AI digital replica use
- Ability for performers to suspend consent during strikes
- Annual wage increases over three years
- Increased compensation for union games
- Revenue-sharing arrangements with AI companies like Ethovox

## Scope
Approximately 2,600 voice actors and motion capture artists were affected.
""",

    "karhulahti-vitality.md": """# Fetched: https://pmc.ncbi.nlm.nih.gov/articles/PMC11162526/
# Date: 2026-05-10
# Status: OK

## Publication Details
- Author: Veli-Matti Karhulahti
- Journal: Open Research Europe
- Year: 2024

## Construct Validity Problem
Karhulahti argues that identifying addictive game design features lacks construct validity because it is tautological. Quote: it is unclear whether addictive behaviour should equally apply to someone being distracted by checking their smartphone regularly and another person playing a massive multiplayer online game for decades.

## The Vitality Structures Framework
Rather than searching for universal addictive elements, Karhulahti proposes vitality structures.

Three dimensions:
1. Chronotope (experienced spacetime): micro, meso, macro
2. Meta-spatial: close to self, distanced (avatar), far (objects)
3. Meta-temporal: past, present, future orientations

## Three Proposed Vitality Structures
- CLIMB: The sensation of upward progress through exerted effort. Hypothesizes links to ADHD and autism spectrum presentations.
- FINAL STRETCH: Feeling a nearly-completed goal within reach. Suggests connections to obsessive-compulsive patterns.
- ALERT: Immediate awareness of accessible information. Potentially linked to anxiety disorders.

## Methodological Approach
110 Finnish treatment-seekers, supplemented by author own 600-3,000 hours playing League of Legends, Clash Royale, and Soulsborne titles. Explicitly evidence-based hypotheses requiring empirical validation.
""",

    "gdc-2025-state.md": """# Fetched: https://gdconf.com/article/gdc-2025-state-of-the-game-industry-devs-weigh-in-on-layoffs-ai-and-more/
# Date: 2026-05-10
# Status: OK

## Survey Scope
The 2025 State of the Game Industry report surveyed over 3,000 game developers and industry professionals (with plus or minus 2 percent margin of error), conducted in partnership with Omdia and Game Developer.

## Generative AI Usage and Sentiment
- 36 percent of developers personally use generative AI tools
- 30 percent believe the technology negatively impacts the industry (up 12 percent from prior year)
- Usage by role: Business/Finance leads at 51 percent, Production/Leadership at 41 percent, Community/Marketing at 39 percent

## Self-Funding
More than half (56 percent) of respondents have put their own money into funding the creation of their game, with 89 percent reporting this approach achieved at least moderate success.
""",

    "humble-bee.md": """# Fetched: https://www.gamedeveloper.com/business/the-last-humble-bee-postmortem-staying-sane-in-solo-development
# Date: 2026-05-10
# Status: OK

## Developer
Jacob Weersing

## Game
The Last Humble Bee (Steam release: November 21, 2024)

## Development Timeline
- Original estimate: 9 months
- Actual duration: 27 months (2 years, 3 months)
- Daily commitment: 10 minutes to 2 hours per day

## Technical Approach
Weersing used GameMaker and GML (C-based language). Plans to transition to Unity for future 3D projects.

## Key Lessons
On expectations: Weersing references Scott Cawthon journey, noting the developer created approximately 70 games before achieving breakthrough success with Five Nights at Freddy.

## Results
The game accumulated about 3,000 wishlists at launch and is priced at 4.99 dollars.
""",

    "ziva-revenue.md": """# Fetched: https://ziva.sh/blogs/indie-game-revenue
# Date: 2026-05-10
# Status: OK

## Median Earnings
- Gross revenue: 249 dollars
- Net (after Valve 30 percent cut): 174 dollars

## Revenue Distribution (2025)
- 66 percent of games earned under 1,000 dollars
- 90 percent earned under 50,000 dollars
- 0.5 percent exceeded 1 million dollars in revenue

## Average Revenue by Experience Level
- First game (debut): 120,000 dollars gross
- Third game: 209,000 dollars gross

## Data Sources
The analysis draws from VG Insights, Alinea Analytics, GameDiscoverCo, Valve GDC 2026 announcements, SteamDB records.

## Context
According to the article, nearly 19,000 games launched on Steam in 2025. Indie games generated 4.4 billion dollars collectively (about 25 percent of Steam total). The median developer earnings fall well below sustainable income levels for multi-person teams.
""",

    "zukowski-2024.md": """# Fetched: https://howtomarketagame.com/2025/01/15/what-the-hell-happened-in-2024/
# Date: 2026-05-10
# Status: OK

## Success Rate Decline
Despite 445 games reaching 1,000+ reviews (up 25 percent), the overall success percentage actually dropped. The percentage of ALL games succeeding went down by 0.12 percent as total releases jumped 31 percent year-over-year. This represents a shift from 2.56 percent success rate in 2023 to 2.44 percent in 2024.

## Growth Drivers
The author attributes the 25 percent increase in successful titles to: enhanced developer knowledge of Steam mechanics, expanded daily deal slots, new demo notification tools for wishlists, algorithm changes favoring mid-tier games.

## Genre Stability
Genres remain remarkably stable. Horror dominates the number 1 position for the third consecutive year.

## Success Rates by Genre (Professional Tier, 700+ followers)
- Farming: 52.63 percent
- Open World Survival Craft: 40.35 percent
- Idle games: 22.99 percent
- 2D platformers and point-and-click adventures: about 2-3 percent

## TikTok Marketing Absence
The article contains no discussion of TikTok as a marketing channel for indie games.
""",

    "stack-overflow-2025.md": """# Fetched: https://stackoverflow.co/company/press/archive/stack-overflow-2025-developer-survey/
# Date: 2026-05-10
# Status: OK

## Trust Metrics
- 46 percent of developers distrust AI tool accuracy (up from 31 percent in 2024)
- 84 percent use or plan to use AI tools in development (up from 76 percent in 2024)

## Top AI-Related Frustration
45 percent cite debugging AI-generated code as time-consuming.

## Additional Findings
- 75.3 percent would not trust AI answers if it handled most coding tasks
- 61.7 percent have ethical/security concerns about AI-generated code
- Only 31 percent currently use AI agents (though 69 percent of those report productivity gains)
- 64 percent do not perceive AI as a job threat (slight decline from 68 percent in 2024)
- 77 percent do not practice vibe coding professionally
- Claude Code adoption stands at 10 percent among developers

## Learning
44 percent of developers use AI tools to learn coding, while 68 percent still prefer technical documentation.
""",

    "mda-framework.md": """# Fetched: https://users.cs.northwestern.edu/~hunicke/MDA.pdf
# Date: 2026-05-10
# Status: OK

## Full Citation
Hunicke, R., LeBlanc, M., Zubek, R. (2004). MDA: A Formal Approach to Game Design and Game Research. Proceedings of the AAAI Workshop on Challenges in Game AI.

## Core Components
- Mechanics: rule systems and systems underlying gameplay (designer directly controls)
- Dynamics: emerge from mechanics during actual play (behavioral interactions)
- Aesthetics: emotional responses players experience (desired effects on the player)

## Eight Aesthetic Categories
1. Sensation: Pleasure from sensory stimulus
2. Fantasy: Immersion in alternative realities
3. Narrative: Engagement through storytelling
4. Challenge: Satisfaction from overcoming obstacles
5. Fellowship: Social connection with other players
6. Discovery: Joy of exploration and learning
7. Expression: Self-representation and creativity
8. Submission: Relaxation through engaging escapism

## Key Conceptual Inversion
Designers craft mechanics, while players experience aesthetics. Dynamics function as the interpretive bridge between designer intent and player experience.

## Historical Context
Developed through GDC workshops spanning 2001-2004.
""",

    "drunk-shotgun.md": """# Fetched: https://www.gamedeveloper.com/business/how-i-wasted-4k-and-half-a-year-of-my-life-to-develop-a-game-that-earned-only-30
# Date: 2026-05-10
# Status: OK

## Developer and Game
Developer: Alexey Strelkov
Game: Drunk Shotgun (top-down mobile shooter)
Platform: iOS and Android

## Financial Summary
Total Development Cost: 4,006 dollars
- Art: 3,220 dollars
- Unity Plus subscription: 342 dollars
- Licensed music: 180 dollars
- Ad campaigns: 254 dollars
- Sound effects: 10 dollars

Total Revenue: 35.57 dollars
- In-game ads: 18.94 dollars
- Subscriptions: 16.63 dollars

Net Loss: about 3,970 dollars

## User Acquisition Metrics
- Cost Per Install (CPI): 0.41 dollars
- Lifetime Value (LTV): 0.02 dollars
- Cost to Acquire Paying User (CAC): 120 dollars

## Time Investment
Approximately 55 work days from October 2019 prototype through June 2020 v1.1.0 release (developed part-time while employed as CTO).

## Marketing Rejection
Facebook and Instagram rejected ad campaigns due to guns, violence, blood and alcohol references. The developer eventually changed blood color from red to yellow for Google Play approval.
""",

    "tower-of-guns.md": """# Fetched: https://www.gamedeveloper.com/business/how-long-does-it-take-to-make-an-indie-game-
# Date: 2026-05-10
# Status: OK

## Developer
Joseph Mirabello

## Game
Tower of Guns (randomized indie FPS)

## Development Timeline
600 days

## Total Tracked Hours
3,850 hours and 5 minutes

## Marketing Investment
Approximately 25 percent of total development time (983 hours 24 minutes)

## Efficiency Rates by Year
- 2012: 55-67 percent efficiency
- 2013: Slightly improved but still suboptimal
- 2014: Best efficiency period, coinciding with peak marketing focus

## Lessons
- Expect reduced efficiency when wearing multiple development roles
- Combat demotivation proactively as a solo developer
- Budget approximately 25 percent of project time for marketing activities
""",

    "dwarf-fortress.md": """# Fetched: https://stackoverflow.blog/2021/12/31/700000-lines-of-code-20-years-and-one-developer-how-dwarf-fortress-is-built/
# Date: 2026-05-10
# Status: OK

## Timeline and Scale
Tarn Adams has been developing Dwarf Fortress since 2002, initially part-time for four years, then full-time from 2006 onward. The codebase has grown to approximately 711,000 lines of code written entirely by one developer.

## Funding Model
The game operated on a donation-based system for years. Adams developed a commercial version with pixel graphics and improved UI for Steam release.

## Development Philosophy
Adams emphasizes the challenges: It is easy to forget stuff. Searching for semicolon, which is a loose method but close enough, we are up to 711,000 lines, so it is just not possible to keep it all in my head now.

He notes working independently avoids bureaucratic obstacles: I do not have any team-oriented or bureaucratic hurdles to jump through when I want to make an alteration.

## Technical Stack
The game combines C and C++, OpenGL, SDL, and FMOD.
""",

    "caves-of-qud.md": """# Fetched: https://www.gamesradar.com/games/roguelike/legendary-roguelike-rpgs-9-years-in-steam-early-access-was-possible-as-devs-wanted-a-positive-lifestyle-and-great-game-rather-than-maximum-profit/
# Date: 2026-05-10
# Status: OK (truncated)

## Developers
Freehold Games (Jason Grinblat and Brian Bucklew)

## Early Access Duration
9 years on Steam

## Development Philosophy
The developers prioritized a positive lifestyle and great game, rather than maximum profit.

## Critical Reception
OpenCritic score of 95 percent.
""",
}

for fname, content in SOURCES.items():
    fpath = DATA_DIR / fname
    fpath.write_text(content, encoding="utf-8")
    print(f"Wrote {fpath}")

print(f"\nTotal: {len(SOURCES)} files written to {DATA_DIR}")
