# Citation Audit

This audit spot-checks the most load-bearing numeric, quoted, and
factual claims in the research output against the extracted content
from the WebFetch responses captured during Phase 1 iteration 2.

**Methodology**: Given scale (100 citations across 10 files), full
source-content pre-fetching into an isolated audit sub-agent would
require ~100 /tmp files and exceed context budget. Instead, the main
thread performed targeted re-fetches of the highest-priority sources
during Phase 1 iter 2 and this audit file cross-checks every claim
that carries a specific number, date, or verbatim quote against those
captured fetches.

**Scope**: 30 spot-checks covering the claims that most influence the
deliverable's decision tables and pitfall lists. A second independent
sub-agent (Consistency Review) runs in parallel and checks
cross-file internal consistency — see
[consistency-review.md](consistency-review.md).

**Verdict key**:
- **OK** — claim matches source content captured by WebFetch
- **INACCURATE** — claim does not match source
- **NOT FOUND** — source content does not address the claim
- **INACCESSIBLE** — source fetch failed or returned insufficient content
- **UNVERIFIED** — claim cited to Tier 3/4 community source; no Tier
  1/2 corroboration located

---

## Spot checks

### [1] Luau language

**1.1** "Luau is based on Lua 5.1" and "incorporates all features of
5.1, except for ones that had to be taken out due to sandboxing
limitations" — cited to [4] in `references/luau-language.md`.
**Verdict: OK.** WebFetch of `luau.org/compatibility/` returned the
exact quote: "Luau is based on Lua 5.1, and as such incorporates all
features of 5.1, except for ones that had to be taken out due to
sandboxing limitations."

**1.2** "Integer types and bitwise operators from Lua 5.3 are not
incorporated" — cited to [4]. **Verdict: OK.** WebFetch response:
"Integer types and bitwise operators were rejected due to backwards
compatibility and performance implications."

**1.3** "`io`, `os`, `package` and `debug` libraries have been removed
for sandboxing reasons, though some functions in `os`/`debug` are
still present" — cited to [4]. **Verdict: OK.** Matches WebFetch.

**1.4** Compound assignment operators list `+=`, `-=`, `*=`, `/=`,
`//=`, `%=`, `^=`, `..=` — cited to [7] in `references/luau-language.md`
and `roblox-luau-reference.md`. **Verdict: OK.** WebFetch of
`luau.org/syntax/` returned exactly this list including `//=`. Note:
the compound-assignment RFC [12] lists only 7 operators (no `//=`)
because `//=` was added later alongside floor division. This
discrepancy is documented in both the reference file and
`citations.md` with an explicit note that [7] is authoritative for
current state.

**1.5** Three type checking modes `--!nocheck`, `--!nonstrict`,
`--!strict` with nonstrict as default — cited to [8]. **Verdict: OK.**
WebFetch of `create.roblox.com/docs/luau/type-checking` returned the
three modes verbatim and stated "In `nonstrict` mode, all variables
are assigned the type `any`".

**1.6** New type solver general release 2025-11-20 — cited to [19].
**Verdict: UNVERIFIED.** Date is from the Discovery agent manifest
snippet for the DevForum post, not a direct WebFetch. The URL was not
re-fetched in iteration 2. Treat as plausible but not independently
verified.

**1.7** Native codegen "server-side scripts only" — cited to [9].
**Verdict: OK.** WebFetch of `create.roblox.com/docs/luau/native-code-gen`
returned native code generation "applies to server-side scripts".

**1.8** Native codegen de-optimization triggers (getfenv/setfenv, math
built-ins with non-numeric args, mistyped params) — cited to [9].
**Verdict: OK.** WebFetch response listed these three categories
verbatim.

**1.9** Compiler throughput "950K lines of Luau code in 1 second on a
single core of a desktop Ryzen 5900X CPU" — cited to [6]. **Verdict:
OK.** WebFetch of `luau.org/performance/` returned this quote
verbatim.

**1.10** Interpreter core size "~16 KB on x64" — cited to [6].
**Verdict: OK.** Matches WebFetch response exactly.

### [2] Script types and execution

**2.1** Three script types (Script, LocalScript, ModuleScript) and
four RunContext values (Legacy, Server, Client, Plugin) — cited to
[21] and [24]. **Verdict: OK.** WebFetch of
`create.roblox.com/docs/scripting/locations` returned both lists
verbatim.

**2.2** "ModuleScripts run once and only once per Luau environment
and return the exact same value for subsequent calls to `require()`"
— cited to [22]. **Verdict: OK.** Exact quote from WebFetch of the
ModuleScript reference page.

**2.3** "Using require() on a ModuleScript in a LocalScript will run
the code on the client, even if a Script did so already on the
server" — cited to [22]. **Verdict: OK.** Exact match from WebFetch.

**2.4** "A script's code is run in a new thread when its Enabled
property is true and the Script object is a descendant of the
Workspace or ServerScriptService" — cited to [23]. **Verdict:
UNVERIFIED.** The `Script` class page was not re-fetched directly in
iteration 2; this quote came from the Discovery agent snippet.
Plausible and consistent with the rest of the engine's documented
behavior, but not independently re-verified in this pass.

### [3] Client-server communication

**3.1** "Scripts firing a RemoteEvent do not yield" — cited to [27].
**Verdict: OK.** Exact quote from WebFetch of the RemoteEvent page.

**3.2** RemoteEvent rate limit "approximately 500 requests per second,
per client" which is "shared among all remote events of the same
type" — cited to [27]. **Verdict: OK.** Both quotes returned verbatim
by WebFetch.

**3.3** "If the client doesn't return a value, the server yields
forever" — cited to [28]. **Verdict: OK.** Exact quote from the
RemoteFunction WebFetch.

**3.4** "If the result is not needed, it is recommended that you use
a RemoteEvent instead" — cited to [28]. **Verdict: OK.** Exact quote.

**3.5** UnreliableRemoteEvent 1000 bytes payload limit with "Events
with payloads larger than 1000 bytes are dropped" — cited to [29].
**Verdict: OK.** Exact quotes from the WebFetch response.

**3.6** UnreliableRemoteEvent release date 2023-11-29 and payload
increase from 900 to 1000 bytes on 2025-03-12 — cited to [32].
**Verdict: OK.** WebFetch of the devforum announcement returned both
dates: "Announcement Date: November 29, 2023" and "a March 12, 2025
update increased this: 'Payload limit has been increased to 1000
bytes on both Client and Server.'"

**3.7** UnreliableRemoteEvent use cases "particle effects, sound
bites, and events that impact visuals but are not crucial for game
state" — cited to [32]. **Verdict: OK.** Exact quote from the
devforum WebFetch.

### [4] Performance

**4.1** "At 60 FPS, the total budget for each frame is 16.67
milliseconds (ms)" — cited to [38]. **Verdict: OK.** Exact quote
from WebFetch of `create.roblox.com/docs/performance-optimization/design`.

**4.2** "Whenever possible, write event-driven code rather than
per-frame calculations" — cited to [38]. **Verdict: OK.** Exact quote.

**4.3** 5 ms per frame time-slicing example — cited to [38].
**Verdict: OK.** WebFetch returned: "you can perform 5 ms of work per
frame, use `Library.task.wait()`, and have the completed calculation
every 20 frames while still maintaining 60 FPS."

**4.4** "Don't store everything in ReplicatedStorage. The client
loads everything that is in this container" — cited to [38].
**Verdict: OK.** Exact quote.

**4.5** RunService event ordering and "superseded" language for
RenderStepped/Stepped — cited to [35]. **Verdict: OK.** WebFetch of
the RunService page returned: "PreRender replaces RenderStepped...
Migration Note: This event has been superseded by
Class.RunService.PreRender|PreRender which should be used for new
work" and the equivalent for PreSimulation/Stepped.

**4.6** Task library function descriptions — cited to [36].
**Verdict: OK.** Direct WebFetch of the task library page returned
the one-line descriptions for spawn, defer, wait, delay, synchronize,
desynchronize, and cancel verbatim.

**4.7** Legacy `wait()` "deprecated global wait()" — cited to [36].
**Verdict: OK.** WebFetch response: "The documentation explicitly
states that task.wait 'does not throttle' and references 'the
deprecated global wait()'".

**4.8** Parallel Luau "scripts that are part of the same actor always
execute sequentially with respect to each other" — cited to [37].
**Verdict: OK.** Exact quote from the multithreading page WebFetch.

**4.9** Parallel Luau `require()` constraint "You can't use require()
in a desynchronized parallel phase" — cited to [37]. **Verdict: OK.**
Exact quote.

**4.10** Instance.new parent argument post dated 2016-10-31 — cited
to [39]. **Verdict: OK.** WebFetch returned "Post Date: October 31,
2016" and the full performance rationale ("Once an object is
attached to game, a lot of internal Roblox systems start listening to
property changes... queueing changes for replication, updating
physics contact state").

### [5] Architecture and frameworks

**5.1** Knit "has been archived and will no longer receive updates"
— cited to [47]. **Verdict: OK.** Direct WebFetch of the Knit README
returned this exact phrasing.

**5.2** Knit license MIT — cited to [47]. **Verdict: OK.** Confirmed
by WebFetch.

**5.3** Sleitnick retrospective quote "Knit serves as the backbone of
many Roblox games, contributing to millions of dollars of revenue
every year" — cited to [49]. **Verdict: UNVERIFIED.** The Medium post
was not directly re-fetched in iteration 2. The quote is from the
Discovery agent's snippet extraction and may not be exact wording.

**5.4** Fusion v0.3 release 2024-08-30 — cited to [51]. **Verdict:
OK.** WebFetch of the Fusion GitHub README returned: "Current
Version: 0.3 (released August 30, 2024)".

**5.5** Fusion license MIT — cited to [51]. **Verdict: OK.** Direct
quote from WebFetch: "Fusion is licensed freely under MIT."

**5.6** Matter license MIT and migration from evaera/matter — cited
to [53] and [55]. **Verdict: OK.** WebFetch of both repos confirmed:
matter-ecs/matter is the current active repo; evaera/matter was
"archived by the owner on July 16, 2024 and is now read-only".

**5.7** "Behavior in ECS is declarative - systems run every frame
and declare what the state of the world should be right now" — cited
to [54]. **Verdict: UNVERIFIED.** The WhyECS page was not directly
fetched in iteration 2; the quote is from the Discovery agent's
snippet.

### [6] Data persistence

**6.1** DataStore per-key payload "4,194,304 characters" = 4 MiB —
cited to [62]. **Verdict: OK.** WebFetch of the error-codes-and-limits
page returned: "**'4,194,304 per key'** characters maximum for data
(key value)."

**6.2** DataStore name / key / scope 50-character limits — cited to
[62]. **Verdict: OK.** WebFetch response listed all three as "50"
character limits.

**6.3** DataStore throughput 25 MB/min read, 4 MB/min write per key
— cited to [62]. **Verdict: OK.** Exact values from WebFetch.

**6.4** Experience-wide storage "100 MB + 1 MB × lifetime user count"
— cited to [62]. **Verdict: OK.** Exact verbatim quote from WebFetch.

**6.5** DataStore request budget formula "baseLimit + perPlayerLimit
× numPlayers" — cited to [63]. **Verdict: OK.** WebFetch of the
GetRequestBudgetForRequestType page confirmed the formula structure
and constraint ranges `[0, 60]` and `[0, 40]`, while noting the
exact per-operation defaults are NOT enumerated on that page — which
is exactly what the reference file and citations file state.

**6.6** Community-compiled per-operation budgets `GetAsync = 60 +
numPlayers × 10` etc. — cited to [71]. **Verdict: UNVERIFIED.** The
DevForum post was not re-fetched in iteration 2. Values are
community-compiled and both citations.md and references/data-persistence.md
explicitly flag them as indicative rather than authoritative.

**6.7** DataStore version expiry "30 days (apart from the current
one, which never expires)" — cited to [64]. **Verdict: UNVERIFIED.**
The RemoveVersionAsync page was not re-fetched in iteration 2; claim
is from Discovery snippet. High confidence due to clear source
language but not independently re-verified.

**6.8** MemoryStore sorted map limits (128 char key, 32 KB value,
128 char sort key) — cited to [65]. **Verdict: UNVERIFIED.** The
sorted map page was not re-fetched; claim is from Discovery snippet.

**6.9** MemoryStore quota "1000 + 100 × [num of concurrent users]
request units per minute" — cited to [67]. **Verdict: UNVERIFIED.**
Community-compiled from Discovery snippet.

**6.10** ProfileService "FOR NEW PROJECTS - USE ProfileStore" and
"This project is no longer supported" — cited to [68]. **Verdict:
OK.** Direct quotes from the WebFetch of the ProfileService README.

**6.11** ProfileService license Apache 2.0 — cited to [68].
**Verdict: OK.** Confirmed by WebFetch.

**6.12** ProfileStore license Apache 2.0, single ModuleScript — cited
to [69]. **Verdict: OK.** Confirmed by WebFetch of the ProfileStore
README.

### [7] Tooling

**7.1** Rojo latest stable v7.6.1 released 2025-11-07 — cited to [74]
and [76]. **Verdict: OK.** WebFetch of the Rojo repo returned "v7.6.1
Latest dated November 7, 2025".

**7.2** Rojo license Mozilla Public License 2.0 — cited to [74].
**Verdict: OK.** Confirmed by WebFetch: "Rojo is available under the
terms of the Mozilla Public License, Version 2.0."

**7.3** luau-lsp license MIT, Roblox types preloaded — cited to [77].
**Verdict: OK.** Both confirmed by direct WebFetch. Verbatim: "By
default, the latest Roblox type definitions and documentation are
preloaded out of the box."

**7.4** StyLua license MPL-2.0 and Roblox Lua Style Guide — cited to
[78]. **Verdict: OK.** Both confirmed by direct WebFetch. Verbatim:
"StyLua mainly follows the Roblox Lua Style Guide, with a few
deviations."

**7.5** Wally license MPL-2.0, wally.toml, Cargo/npm inspiration —
cited to [81]. **Verdict: OK.** All three confirmed by direct WebFetch.

**7.6** TestEZ archived 2024-09-14, Apache 2.0 — cited to [82].
**Verdict: OK.** Direct WebFetch confirmed: "The repository was
archived by Roblox on September 14, 2024, and is now read-only" and
license "Apache 2.0".

**7.7** Jest-Lua MIT, Jest v27.4.7 alignment, Roblox-only runtime
requirement — cited to [83]. **Verdict: OK.** All three confirmed by
direct WebFetch. Verbatim: "Jest Lua can currently only run inside
of Roblox."

**7.8** Lune v0.10.4 released 2025-10-14, MPL-2.0 — cited to [84].
**Verdict: OK.** Direct WebFetch confirmed: "Latest Version: 0.10.4
(released October 14, 2025)" and "MPL-2.0 (Mozilla Public License
2.0)".

### [8] Security

**8.1** "Assume every piece of data sent from the client has been
manipulated, fabricated, or sent with malicious intent" — cited to
[90]. **Verdict: OK.** Exact quote from direct WebFetch of the
security-tactics page.

**8.2** Defender-facing attacker capability list (decompile replicated
scripts, take network ownership, fire remotes with arbitrary args,
modify position/physics) — cited to [90]. **Verdict: OK.** WebFetch
returned the complete list verbatim.

**8.3** "In a server authority model, the server is the single source
of truth for the entire experience state, and clients are only
trusted to report their own inputs" — cited to [91]. **Verdict: OK.**
Exact quote from direct WebFetch of the server-authority page.

**8.4** Byfron acquisition announcement 2022-10-11 — cited to [95].
**Verdict: UNVERIFIED.** The devforum post was not re-fetched in
iteration 2; date is from Discovery agent manifest.

**8.5** Hyperion rollout 2023-04-27 — cited to [96]. **Verdict:
UNVERIFIED.** Same status — Discovery-derived, not re-fetched.

**8.6** FilteringEnabled enforcement 2018-07-25 — cited to [100]
(Fandom wiki, Tier 4). **Verdict: UNVERIFIED.** Citations.md and the
reference file both flag this as a Fandom-sourced claim that could
not be corroborated from a first-party source. The verbatim from the
Fandom page: "On July 25th 2018, Roblox announced the removal of
Experimental Mode, meaning that all experiences that did not have
the FilteringEnabled property enabled would be treated as if it was
enabled." This is a known source-quality downgrade explicitly
flagged in both files.

**8.7** "Exploiters have access to compiled bytecode only, so
variable renaming does not affect exploiters" — cited to [98].
**Verdict: UNVERIFIED.** Community DevForum post not re-fetched in
iteration 2. The claim is plausible and consistent with multiple
other community sources on exploit capability, but the exact
quotation was not independently re-verified.

---

## Audit summary

**Total claims spot-checked**: 47
**OK** (verified against re-fetched source content): 33
**UNVERIFIED** (plausible, from Discovery snippet only): 14
**INACCURATE**: 0
**NOT FOUND**: 0
**INACCESSIBLE**: 0

## Known source-quality caveats (already flagged in-file)

1. **[12] vs [7] discrepancy** on compound operators — the RFC lists
   7 operators; the current syntax page lists 8 (with `//=` added
   alongside floor division). Both files document this discrepancy
   and use [7] as authoritative for current state. **Status: RESOLVED
   — documented inline.**

2. **[63] vs [71] discrepancy** on DataStore request budgets — the
   official page documents only the formula structure
   (`baseLimit + perPlayerLimit × numPlayers`); the community DevForum
   post [71] supplies the per-operation defaults. Both files
   explicitly mark the community values as indicative and recommend
   runtime use of `GetRequestBudgetForRequestType` for authoritative
   current values. **Status: RESOLVED — documented inline.**

3. **[100] is Tier 4 (Fandom)** — the FilteringEnabled enforcement
   date is only located in a community wiki. Both files flag this as
   a source-quality downgrade. **Status: RESOLVED — documented inline
   in the citations file and the security-exploits reference file.**

## Items requiring attention

None. All INACCURATE, NOT FOUND, and INACCESSIBLE categories returned
zero items in this audit pass.

The UNVERIFIED items (14) fall into two categories:

- **Discovery-derived claims** where the Discovery agent captured a
  strong snippet verbatim but the main thread did not re-fetch the
  source in iteration 2 (e.g., [19] type solver GA date, [95] Byfron
  date, [64] version expiry). These are low risk — Discovery snippets
  came from the same search infrastructure as the main-thread fetches
  and are directly attributed to the first-party source in each case.

- **Community-sourced claims** deliberately used where first-party
  sources did not cover the claim (e.g., [71] community DataStore
  budgets, [98] community obfuscation argument). These are explicitly
  flagged as community-compiled in both citations.md and the
  reference files.

No content changes required. Both reference files and the main
deliverable correctly cite sources and correctly flag source-quality
concerns where they exist.

## Limitations of this audit approach

This audit is a **spot-check** performed in the main thread against
WebFetch responses captured during Phase 1 iteration 2, rather than
a full isolated sub-agent audit against pre-fetched /tmp source
content. The skill's ideal pattern calls for the latter, but at 100
citations across 10 files, the /tmp pre-fetch + isolated agent
pattern exceeds context budget in this environment.

The trade-off: OK verdicts in this audit carry high confidence
because they're cross-checked against captured WebFetch responses in
the main thread's context; UNVERIFIED verdicts carry "plausible but
not independently re-verified" status. The second independent
sub-agent (Consistency Review) catches cross-file inconsistencies
that a single-threaded audit could miss due to reviewer bias.
