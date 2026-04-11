# Citations

Master list of sources for the Roblox Luau game development research. Numbered
sequentially; cited throughout the reference files and the main deliverable as
`[N]`.

**Tier legend**

- **Tier 1** — Peer-reviewed papers, academic/institutional publications
- **Tier 2** — First-party primary sources: `create.roblox.com/docs`,
  `luau.org`, `rfcs.luau.org`, official GitHub repos, Roblox engineering /
  announcement posts
- **Tier 3** — Established secondary sources: DevForum staff and recognized
  community authors, personal blogs by framework maintainers
- **Tier 4** — Forums, wikis, social media — used sparingly

Recency note: citations without explicit publication dates marked "living
doc" are pages that are continuously updated; data was captured in April 2026.

---

## Luau language and runtime

**[1]** Brown, L., Friesen, A., Jeffrey, A. (2021). *Position Paper: Goals of
the Luau Type System*. HATRA 2021 (ACM SPLASH workshop).
<https://arxiv.org/abs/2109.11397>. **Tier 1.** Date: 2021-09-23. Supports:
Luau is a statically-typed language based on dynamically-typed Lua, with type
inference. "Due to Roblox's uniquely heterogeneous developer community, Luau
must operate in a somewhat different fashion than a traditional statically-
typed language."

**[2]** Brown, L., Friesen, A., Jeffrey, A. (2023). *Goals of the Luau Type
System, Two Years On*. HATRA 2023 (ACM SPLASH workshop).
<https://research.luau-lang.org/hatra23/hatra23.pdf>. **Tier 1.** Date:
2023-10-01. Supports: progress report on the Luau type system including
semantic subtyping and type error suppression.

**[3]** Brown, L., Friesen, A., Jeffrey, A. (2024). *Privacy-Respecting Type
Error Telemetry at Scale*. The Art, Science, and Engineering of Programming,
vol. 8, no. 3. <https://arxiv.org/abs/2403.02409>. **Tier 1.** Date:
2024-03-04. Supports: Luau's gradual type system minimizes false positive
errors; over 1.5 million telemetry records from 340,000+ Roblox Studio
sessions in Spring 2023.

**[4]** Luau. *Compatibility with Lua*. <https://luau.org/compatibility/>.
**Tier 2.** Living doc. Supports: "Luau is based on Lua 5.1, and as such
incorporates all features of 5.1, except for ones that had to be taken out
due to sandboxing limitations." The `io`, `os`, `package` and `debug`
libraries are removed or restricted. Lua 5.2+ features incorporated include
yieldable pcall/xpcall, bit32, `__len` metamethod, string hex escapes.
Integer types and bitwise operators are intentionally not incorporated.
`getfenv`/`setfenv` are retained "because of backwards compatibility
constraints".

**[5]** Luau. *Embedding a sandboxed Luau virtual machine*.
<https://luau.org/sandbox/>. **Tier 2.** Living doc. Supports: "All libraries
(`string`, `math`, etc.) are marked as readonly". "In Roblox we solve this by
creating a new global table for each script, that uses `__index` to point to
the builtin global table." External bytecode is explicitly rejected. "Ideally,
these [getfenv/setfenv] should be disabled as well, but unfortunately Roblox
community relies on these for various reasons."

**[6]** Luau. *How we make Luau fast*. <https://luau.org/performance/>.
**Tier 2.** Living doc. Supports: Luau is "noticeably faster than Lua 5.x
(including Lua 5.4)"; "On some workloads it can match the performance of
LuaJIT interpreter." Interpreter core is ~16 KB on x64. Tagged values are
16 bytes. Compiler throughput: "compiles 950K lines of Luau code in 1 second
on a single core of a desktop Ryzen 5900X CPU". `table.sort` ~4× faster than
Lua 5.x; paged sweeper GC 2-3× faster. Import optimization disabled by
`loadstring`/`getfenv`/`setfenv`.

**[7]** Luau. *Luau syntax by example*. <https://luau.org/syntax/>.
**Tier 2.** Living doc. Supports: full list of Luau syntax extensions over
Lua 5.1 — generalized iteration, string interpolation, continue, compound
assignments (`+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `^=`, `..=`), type
annotations (`:`, `::`, `type`, `export type`), if-then-else expressions,
floor division (`//`, `//=`), number literals (`0x`, `0b`, `_` separators),
string escapes (`\x`, `\u`, `\z`).

**[8]** Roblox. *Type checking*. create.roblox.com.
<https://create.roblox.com/docs/luau/type-checking>. **Tier 2.** Living doc.
Supports: three type checking pragmas — `--!nocheck`, `--!nonstrict`,
`--!strict`. In nonstrict mode "all variables are assigned the type `any`"
by default. Workspace-wide default configured via `Workspace.LuauTypeCheckMode`.
Type mismatches are "highlighted in the Script Editor and surfaced as
warnings in the Script Analysis window."

**[9]** Roblox. *Native code generation*. create.roblox.com.
<https://create.roblox.com/docs/luau/native-code-gen>. **Tier 2.** Living
doc. Supports: script-level `--!native` comment or function-level `@native`
attribute enables native compilation. "server-side scripts" only. De-optimization
triggers: "Use of deprecated getfenv()/setfenv() calls", "Use of various
Luau built-in functions like math.asin() with non-numeric arguments",
"Passing improperly typed parameters to typed functions". Costs: compilation
time increases server startup; extra memory for compiled code; experience-wide
cap on total natively compiled code.

**[10]** Luau. *Generalized iteration* (RFC).
<https://rfcs.luau.org/generalized-iteration.html>. **Tier 2.** Supports:
`for k, v in obj do` syntax; `__iter` metamethod invoked once at loop
startup; "mostly rendering pairs/ipairs obsolete".

**[11]** Luau. *String interpolation* (RFC).
<https://rfcs.luau.org/syntax-string-interpolation.html>. **Tier 2.**
Supports: backtick syntax `` `Hello {world}` ``; desugars to `string.format`
with new `%*` token for `tostring`; `{{` rejected to avoid ambiguity;
interpolated strings cannot be used in calls without parentheses; status:
implemented.

**[12]** Luau. *Compound assignment using op= syntax* (RFC).
<https://rfcs.luau.org/syntax-compound-assignment.html>. **Tier 2.**
Supports: operators `+=`, `-=`, `*=`, `/=`, `%=`, `^=`, `..=` (the original
RFC; `//=` added later with floor division per [7]); "these are assignment
statements, not expressions".

**[13]** Luau. *Luau Goes Open-Source* (news post).
<https://luau.org/news/2021-11-03-luau-goes-open-source/>. **Tier 2.** Date:
2021-11-03. Supports: Luau released as open source under MIT license with
VM, compiler, type checker, and linter on GitHub.

**[14]** Luau. *String Interpolation* (news post).
<https://luau.org/news/2023-02-02-luau-string-interpolation/>. **Tier 2.**
Date: 2023-02-02. Supports: string interpolation added February 2023.

**[15]** Luau. *Luau Recap for 2025: Runtime* (news post).
<https://luau.org/news/2025-12-19-luau-recap-runtime-2025/>. **Tier 2.** Date:
2025-12-19. Supports: 2025 native codegen improvements — Android support,
vector operation native lowering, integer CPU instructions, load-store
propagation.

**[16]** Luau. *Luau Recap: October 2023* (news post).
<https://luau.org/2023/11/01/luau-recap-october-2023.html>. **Tier 2.** Date:
2023-11-01. Supports: native code generation in Studio Beta with `--!native`
comment annotation; open-source CLI via `--codegen` flag.

**[17]** Roblox DevForum (staff announcement). *Luau Native Code Generation
Preview [Studio Beta]*.
<https://devforum.roblox.com/t/luau-native-code-generation-preview-studio-beta/2572587>.
**Tier 2.** Date: 2023-08-31. Supports: `--!native` beta release in Studio,
initial limitations.

**[18]** Roblox DevForum (staff announcement). *New Type Solver [Beta]*.
<https://devforum.roblox.com/t/new-type-solver-beta/3155804>. **Tier 2.**
Date: 2024-09-13. Supports: new type solver introduced as a beta feature.

**[19]** Roblox DevForum (staff announcement). *[General Release] Luau's New
Type Solver*.
<https://devforum.roblox.com/t/general-release-luaus-new-type-solver/4084991>.
**Tier 2.** Date: 2025-11-20. Supports: new type solver general release to
nocheck and nonstrict mode with new Scripting workspace properties to
configure default typechecking mode.

**[20]** Wikipedia. *Luau (programming language)*.
<https://en.wikipedia.org/wiki/Luau_(programming_language)>. **Tier 3.**
Living doc. Supports: Luau deployed on Roblox 2019-08-27; open-sourced
2021-11-03; adopted by Remedy Entertainment (Alan Wake 2), Digital Extremes
(Warframe), Giants Software (Farming Simulator 2025).

## Script types and execution model

**[21]** Roblox. *Script types and locations*. create.roblox.com.
<https://create.roblox.com/docs/scripting/locations>. **Tier 2.** Living doc.
Supports: three script types — Script, LocalScript, ModuleScript. RunContext
values Legacy/Server/Client/Plugin. Legacy RunContext requires Script in
Workspace or ServerScriptService to run. Client RunContext allows Script in
ReplicatedStorage, StarterCharacterScripts, StarterPlayerScripts.

**[22]** Roblox. *ModuleScript*. create.roblox.com API reference.
<https://create.roblox.com/docs/reference/engine/classes/ModuleScript>.
**Tier 2.** Living doc. Supports: "ModuleScripts run once and only once per
Luau environment and return the exact same value for subsequent calls to
require()"; "ModuleScripts must return exactly one value"; "return values
from ModuleScripts are independent with regards to Scripts and LocalScripts";
"Using require() on a ModuleScript in a LocalScript will run the code on
the client, even if a Script did so already on the server."

**[23]** Roblox. *Script*. create.roblox.com API reference.
<https://create.roblox.com/docs/reference/engine/classes/Script>. **Tier 2.**
Living doc. Supports: "A script's code is run in a new thread when its
Enabled property is true and the Script object is a descendant of the
Workspace or ServerScriptService." (Legacy behavior.)

**[24]** Roblox. *RunContext* (enum). create.roblox.com API reference.
<https://create.roblox.com/docs/reference/engine/enums/RunContext>. **Tier 2.**
Living doc. Supports: enum values Legacy, Server, Client, Plugin.

**[25]** Roblox. *BaseScript.RunContext*. create.roblox.com API reference.
<https://create.roblox.com/docs/reference/engine/classes/BaseScript#RunContext>.
**Tier 2.** Living doc. Supports: RunContext is a property of BaseScript
(inherited by Script) that controls where the script runs.

**[26]** Roblox DevForum (staff announcement). *[Live] Script RunContext*.
<https://devforum.roblox.com/t/live-script-runcontext/1938784>. **Tier 2.**
Date: 2022-08-24. Supports: RunContext feature launched with Legacy/Server/
Client values; Plugin value added later.

## Client-server communication

**[27]** Roblox. *RemoteEvent*. create.roblox.com API reference.
<https://create.roblox.com/docs/reference/engine/classes/RemoteEvent>.
**Tier 2.** Living doc. Supports: "Scripts firing a RemoteEvent do not
yield." Rate limit "approximately 500 requests per second, per client" which
is "shared among all remote events of the same type." Methods: FireServer,
FireClient(player), FireAllClients. Events: OnServerEvent (Player as first
arg), OnClientEvent.

**[28]** Roblox. *RemoteFunction*. create.roblox.com API reference.
<https://create.roblox.com/docs/reference/engine/classes/RemoteFunction>.
**Tier 2.** Living doc. Supports: "Scripts invoking a RemoteFunction yield
until they receive a response from the recipient." Deadlock warnings: "If
the client throws an error, the server throws the error too"; "If the
client disconnects while it's being invoked, InvokeClient() throws an
error"; "If the client doesn't return a value, the server yields forever."
"If the result is not needed, it is recommended that you use a RemoteEvent
instead."

**[29]** Roblox. *UnreliableRemoteEvent*. create.roblox.com API reference.
<https://create.roblox.com/docs/reference/engine/classes/UnreliableRemoteEvent>.
**Tier 2.** Living doc. Supports: "asynchronous, unordered and unreliable,
one-way communication across the client-server boundary". Payload limit
"1000 bytes". "Events with payloads larger than 1000 bytes are dropped.
When this happens in Studio, a log message in the Output window indicates
the number of bytes the event went over."

**[30]** Roblox. *Remote events and callbacks* (scripting guide).
<https://create.roblox.com/docs/scripting/events/remote>. **Tier 2.** Living
doc. Supports: overview of RemoteEvent vs RemoteFunction vs UnreliableRemoteEvent
with placement guidance (ReplicatedStorage).

**[31]** Roblox. *Bindable events and callbacks*.
<https://create.roblox.com/docs/scripting/events/bindable>. **Tier 2.**
Living doc. Supports: BindableEvent and BindableFunction are same-context
(not networked); table arguments are copied.

**[32]** Roblox DevForum (staff announcement). *Introducing
UnreliableRemoteEvents*.
<https://devforum.roblox.com/t/introducing-unreliableremoteevents/2724155>.
**Tier 2.** Date: 2023-11-29; updated 2025-03-12. Supports: original payload
limit 900 bytes, raised to 1000 bytes on 2025-03-12. Recommended use cases:
"particle effects, sound bites, and events that impact visuals but are not
crucial for game state". "There is no ordering guarantee between
UnreliableRemoteEvents and anything else." Events "may be dropped to
prioritize bandwidth or CPU usage in addition to any loss that occurs over
the network".

**[33]** Roblox DevForum community tutorial. *In-Depth Information about
Roblox's RemoteEvents, Instance Replication, and Physics Replication (w/
sources!)*.
<https://devforum.roblox.com/t/in-depth-information-about-robloxs-remoteevents-instance-replication-and-physics-replication-w-sources/1847340>.
**Tier 3.** Updated 2023-08-21. Supports: RemoteEvents are reliable and
ordered (TCP-like); physics replication via network ownership.

**[34]** boyned (community author). *A reliable case for unreliable packets*.
<https://blog.boyned.com/articles/a-reliable-case-for-unreliable-packets/>.
**Tier 3.** Pre-2023. Supports: standard Roblox remote events are ordered
and reliable, which creates bandwidth cost for frequent updates like mouse
positions — the argument for an unreliable channel that influenced
UnreliableRemoteEvent.

## Performance and scheduling

**[35]** Roblox. *RunService*. create.roblox.com API reference.
<https://create.roblox.com/docs/reference/engine/classes/RunService>.
**Tier 2.** Living doc. Supports: frame event ordering PreRender →
PreAnimation → PreSimulation → (physics) → PostSimulation → Heartbeat.
PreRender and RenderStepped are both client-only with identical timing;
"This event has been superseded by PreRender which should be used for new
work." PreSimulation and Stepped similarly — PreSimulation supersedes
Stepped.

**[36]** Roblox. *task library*. create.roblox.com API reference.
<https://create.roblox.com/docs/reference/engine/libraries/task>. **Tier 2.**
Living doc. Supports: task.spawn "Calls/resumes a function/coroutine
immediately through the engine's scheduler"; task.defer "Calls/resumes a
function/coroutine at the end of the current resumption cycle"; task.wait
"Yields the current thread without throttling"; task.delay "Schedules a
function/coroutine to be called/resumed on the next Heartbeat after the
given duration"; task.synchronize, task.desynchronize, task.cancel. Legacy
`spawn`/`wait`/`delay` are described as "the deprecated global wait()".

**[37]** Roblox. *Parallel Luau*.
<https://create.roblox.com/docs/scripting/multithreading>. **Tier 2.**
Living doc. Supports: Actors are "units of execution isolation that
distribute the load across multiple cores". "Scripts that are part of the
same actor always execute sequentially with respect to each other" —
multiple actors required for parallelism. `task.desynchronize()` suspends
execution for parallel, `task.synchronize()` switches back. "You can't use
`require()` in a desynchronized parallel phase." SharedTable enables safe
atomic updates across actors. Actor:SendMessage and
BindToMessage/BindToMessageParallel for cross-actor communication.

**[38]** Roblox. *Design for performance*.
<https://create.roblox.com/docs/performance-optimization/design>. **Tier 2.**
Living doc. Supports: "At 60 FPS, the total budget for each frame is 16.67
milliseconds (ms)." "Whenever possible, write event-driven code rather than
per-frame calculations." "Don't store everything in ReplicatedStorage. The
client loads everything that is in this container. Instead, use
ServerStorage for anything the client does not need access to." Time-
slicing example: "you can perform 5 ms of work per frame, use task.wait(),
and have the completed calculation every 20 frames while still maintaining
60 FPS."

**[39]** Roblox DevForum (staff / senior community) PSA. *Don't use
Instance.new() with parent argument*.
<https://devforum.roblox.com/t/psa-dont-use-instancenew-with-parent-argument/30296>.
**Tier 2 (staff-adjacent).** Date: 2016-10-31. Supports: "Once an object is
attached to game, a lot of internal Roblox systems start listening to
property changes... queueing changes for replication, updating physics
contact state". Optimal sequence: create instance → assign properties →
assign Parent → connect signals.

**[40]** Roblox DevForum (staff announcement). *Task Library - Now Available!*.
<https://devforum.roblox.com/t/task-library-now-available/1387845>. **Tier 2.**
Date: ~2021. Supports: task library rationale as replacement for less
optimized `spawn()`/`delay()`/`wait()`.

**[41]** Roblox DevForum (staff announcement). *Parallel Luau [Version 2
Release]*.
<https://devforum.roblox.com/t/parallel-luau-version-2-release/2399970>.
**Tier 2.** Date: 2023-05-31. Supports: Parallel Luau V2 introduced the
Actor Messaging API and SharedTable.

**[42]** Roblox DevForum (staff announcement). *Full Release of Parallel
Luau V1*.
<https://devforum.roblox.com/t/full-release-of-parallel-luau-v1/1836187>.
**Tier 2.** Date: 2022. Supports: V1 full release with Actor model and
task.synchronize/desynchronize.

**[43]** Roblox. *MicroProfiler*.
<https://create.roblox.com/docs/performance-optimization/microprofiler>.
**Tier 2.** Living doc. Supports: MicroProfiler shows per-frame render time
as vertical bars; opened via Ctrl+Alt+F6. `debug.profilebegin(label)` and
`debug.profileend()` create labeled spans.

**[44]** Roblox DevForum community tutorial. *Instance Pooling*.
<https://devforum.roblox.com/t/instance-pooling/1148403>. **Tier 3.** Supports:
instance pooling recycles objects to avoid repeated `Instance.new` /
`:Destroy()` calls in hot paths.

**[45]** Roblox DevForum community tutorial. *Part Pooling - Increase
performance with many parts*.
<https://devforum.roblox.com/t/part-pooling-increase-performance-with-many-parts/518433>.
**Tier 3.** Supports: "up to 100 [instances] being fine to create without
pooling"; pool beyond that threshold.

**[46]** GitHub. *Roblox/Core-Scripts ObjectPool.lua*.
<https://github.com/Roblox/Core-Scripts/blob/master/CoreScriptsRoot/Modules/Common/ObjectPool.lua>.
**Tier 2.** Living doc. Supports: Roblox's own Core-Scripts use an object
pool implementation for internal efficiency.

## Architecture patterns and frameworks

**[47]** GitHub. *Sleitnick/Knit*. <https://github.com/Sleitnick/Knit>.
**Tier 2.** Supports: Knit is "a lightweight framework for Roblox that
simplifies communication between core parts of your game and seamlessly
bridges the gap between the server and the client." "Knit has been archived
and will no longer receive updates." Services (server) expose `.Client`
methods that auto-create RemoteFunction infrastructure; Controllers
(client) consume services. License: MIT.

**[48]** Sleitnick, S. *Knit documentation*.
<https://sleitnick.github.io/Knit/docs/intro/>. **Tier 2.** Living doc.
Supports: "Services and controllers are the core of Knit."

**[49]** Sleitnick, S. *Knit, its history, and how to build it better*.
Medium post. <https://medium.com/@sleitnick/knit-its-history-and-how-to-build-it-better-3100da97b36>.
**Tier 2.** Date: 2022-08-16. Supports: "Knit serves as the backbone of many
Roblox games, contributing to millions of dollars of revenue every year";
author retrospective on framework strengths and limitations.

**[50]** Roblox DevForum. *Is using Knit framework still good?* (reply by
Sleitnick).
<https://devforum.roblox.com/t/is-using-knit-framework-still-good/2893430/3>.
**Tier 3.** Supports: "Knit is a battle-tested framework that has stood
strong and scaled well, with games with literally hundreds of thousands of
concurrent players utilizing Knit without a hitch" — from the original
author, after archiving.

**[51]** GitHub. *dphfox/Fusion*. <https://github.com/dphfox/Fusion>.
**Tier 2.** Supports: "Fusion is a portable Luau companion library for
simpler, more descriptive code"; version 0.3 released 2024-08-30. License:
MIT.

**[52]** Elttob. *Fusion documentation (v0.2)*.
<https://elttob.uk/Fusion/0.2/>. **Tier 2.** Supports: declarative reactive
UI with state graph model.

**[53]** GitHub. *matter-ecs/matter*. <https://github.com/matter-ecs/matter>.
**Tier 2.** Supports: "Matter is a modern ECS library for Roblox." Migrated
from evaera/matter (archived 2024-07-16) to the matter-ecs organization.
License: MIT.

**[54]** Matter. *Why ECS*.
<https://matter-ecs.github.io/matter/docs/WhyECS/>. **Tier 2.** Supports:
"Behavior in ECS is declarative - systems run every frame and declare what
the state of the world should be right now. This makes code self-healing
and more resilient to game-breaking bugs than in an event-driven model."

**[55]** GitHub. *evaera/matter* (archived).
<https://github.com/evaera/matter>. **Tier 2.** Archived 2024-07-16.
Supports: original Matter repo, now read-only.

**[56]** GitHub. *Roblox/roact*. <https://github.com/Roblox/roact>.
**Tier 2.** Legacy/deprecated. Supports: Roact is Roblox's React-inspired
UI library, marked as legacy; newer work uses react-lua.

**[57]** GitHub. *jsdotlua/react-lua*.
<https://github.com/jsdotlua/react-lua>. **Tier 2.** Supports: community-
maintained fork with the intention of being "the Roblox and global Lua
community go-to for React in Lua". Translates ReactJS 17.x into Lua.

**[58]** GitHub. *Roblox/react-luau*.
<https://github.com/Roblox/react-luau>. **Tier 2.** Supports: Roblox's
internal React 17 port, read-only mirror, not open for community
contribution and not published to any registry.

**[59]** GitHub. *roblox-ts/roblox-ts*.
<https://github.com/roblox-ts/roblox-ts>. **Tier 2.** Supports: "A
TypeScript-to-Luau Compiler for Roblox"; ~948 stars as of December 2024
growing to ~1.2k by mid-2025.

**[60]** GitHub. *rbxts-flamework/core*.
<https://github.com/rbxts-flamework/core>. **Tier 2.** Supports: "Flamework
is an extensible game framework. It requires typescript and offers many
useful features … built-in dependency injection" — the roblox-ts ecosystem
equivalent of Knit.

**[61]** Roblox. *ModuleScript Patterns*.
<https://create.roblox.com/docs/scripting/scripts/modulescript-patterns>.
**Tier 2.** Living doc. Supports: official guidance on idiomatic module
patterns (singletons, factories, metatable-based OOP).

## Data persistence

**[62]** Roblox. *Data store error codes and limits*.
<https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits>.
**Tier 2.** Living doc. Supports: **per-key data limit 4,194,304 characters**
(= 4 MiB). Data store name, key name, and scope each limited to 50
characters. Per-key throughput: 25 MB per minute read, 4 MB per minute
write. Throttling errors when request queues exceed 30 requests.
Experience-wide storage limit formula: "Total latest version storage limit
= 100 MB + 1 MB * lifetime user count".

**[63]** Roblox. *DataStoreService:GetRequestBudgetForRequestType*.
<https://create.roblox.com/docs/reference/engine/classes/DataStoreService/GetRequestBudgetForRequestType>.
**Tier 2.** Living doc. Supports: the rate limit formula structure is
`rateLimit = baseLimit + (perPlayerLimit * numPlayers)` with constraint
tables `[0, 60]` and `[0, 40]` for different request types. Exact default
per-operation budgets are not enumerated on this page — see [71] for
community-compiled enumeration.

**[64]** Roblox. *DataStore:RemoveVersionAsync*.
<https://create.roblox.com/docs/reference/engine/classes/DataStore/RemoveVersionAsync>.
**Tier 2.** Living doc. Supports: "permanently deletes the specified
version of a key"; "unlike GlobalDataStore:RemoveAsync(), this function
does not create a 'tombstone' version"; "versions expire after 30 days
(apart from the current one, which never expires)".

**[65]** Roblox. *Memory store sorted map*.
<https://create.roblox.com/docs/cloud-services/memory-stores/sorted-map>.
**Tier 2.** Living doc. Supports: key size limit 128 characters, value
size limit 32 KB, sort key size limit 128 characters; max item expiry
3,888,000 seconds (45 days).

**[66]** Roblox. *MemoryStore per-partition limits*.
<https://create.roblox.com/docs/cloud-services/memory-stores/per-partition-limits>.
**Tier 2.** Living doc. Supports: each sorted map or queue resides on a
single partition; "in the very best case, a sorted map and a queue are
limited to 150,000 RPM".

**[67]** Roblox DevForum (staff announcement). *Memory Stores Service Quota
[Update]*.
<https://devforum.roblox.com/t/memory-stores-service-quota-update/2062296>.
**Tier 2.** Supports: MemoryStoreService request quota
"1000 + 100 × [num of concurrent users]" request units per minute per
experience.

**[68]** GitHub. *MadStudioRoblox/ProfileService*.
<https://github.com/MadStudioRoblox/ProfileService>. **Tier 2.** Supports:
"FOR NEW PROJECTS - USE ProfileStore". "This project is no longer supported
- it's been stable for a long while and migration to ProfileStore is
possible for most projects." Session locking prevents multiple servers
from editing the same profile simultaneously. License: Apache 2.0.

**[69]** GitHub. *MadStudioRoblox/ProfileStore*.
<https://github.com/MadStudioRoblox/ProfileStore>. **Tier 2.** Released
2024-10-11. Supports: "a Roblox DataStore wrapper that streamlines
auto-saving, session locking and a few other features"; successor to
ProfileService; backwards-compatible (existing keys load). Single
ModuleScript codebase. License: Apache 2.0.

**[70]** ProfileStore documentation. *API*.
<https://madstudioroblox.github.io/ProfileStore/api/>. **Tier 2.** Supports:
`Profile:Reconcile()` fills nil keys from a template (schema migration
support); `:StartSessionAsync()` opens a session with lock acquisition.

**[71]** Roblox DevForum community resource. *Details on DataStoreService
for Advanced Developers*.
<https://devforum.roblox.com/t/details-on-datastoreservice-for-advanced-developers/175804>.
**Tier 3.** Supports: per-server request budget formulas commonly cited as
`GetAsync = 60 + numPlayers × 10` per minute; `Set/Update/Remove =
60 + numPlayers × 10` per minute. Experience-wide: Read =
`250 + concurrentUsers × 40`; Write = `250 + concurrentUsers × 20`.
**Quality note:** these are community-compiled values; the authoritative
official source is [63], which exposes the formula structure but not the
per-operation defaults. Treat numbers as indicative rather than
authoritative.

**[72]** Roblox DevForum. *BindToClose & Data Loss Risk*.
<https://devforum.roblox.com/t/bindtoclose-data-loss-risk/135693>.
**Tier 3.** Supports: "BindToClose functions don't consistently work and
often lead to data-loss"; servers may exceed shutdown deadline before the
callback completes.

**[73]** Roblox DevForum. *Dependent UpdateAsyncs aka DataStore failure
atomicity*.
<https://devforum.roblox.com/t/dependent-updateasyncs-aka-datastore-failure-atomicity/386157>.
**Tier 3.** Supports: multi-key DataStore updates cannot be made atomic,
which prevents safe implementation of in-game trading systems.

## Development tooling

**[74]** GitHub. *rojo-rbx/rojo*. <https://github.com/rojo-rbx/rojo>.
**Tier 2.** Latest stable v7.6.1 (2025-11-07). Supports: "Rojo is a tool
designed to enable Roblox developers to use professional-grade software
engineering tools"; file-system ↔ Studio sync, `rbxmx`/`rbxm` model
streaming, CLI deployment. License: Mozilla Public License 2.0.

**[75]** Rojo. *Project Format*. <https://rojo.space/docs/6.x/project-format/>.
**Tier 2.** Living doc. Supports: `default.project.json` structure with
`tree` field, `$className`, `$path`, `$properties` keys.

**[76]** GitHub. *rojo-rbx/rojo CHANGELOG*.
<https://github.com/rojo-rbx/rojo/blob/master/CHANGELOG.md>. **Tier 2.**
Supports: v7.6.1 on 2025-11-06 changelog entries. v7.7.0-rc.1 adds `rojo
syncback` command (reverse place → filesystem sync) and rewrites networking
to WebSockets.

**[77]** GitHub. *JohnnyMorganz/luau-lsp*.
<https://github.com/JohnnyMorganz/luau-lsp>. **Tier 2.** Last push
2025-09-20. Supports: "An implementation of a language server for the Luau
programming language." Features: diagnostics, autocompletion, hover,
go-to-definition, Moonwave-style documentation comments, semantic tokens.
"By default, the latest Roblox type definitions and documentation are
preloaded out of the box." License: MIT.

**[78]** GitHub. *JohnnyMorganz/StyLua*.
<https://github.com/JohnnyMorganz/StyLua>. **Tier 2.** Supports: "A
deterministic code formatter for Lua 5.1, 5.2, 5.3, 5.4, LuaJIT, Luau and
CfxLua/FiveM Lua". "StyLua mainly follows the Roblox Lua Style Guide, with
a few deviations." License: Mozilla Public License 2.0.

**[79]** GitHub. *Kampfkarren/selene*. <https://github.com/Kampfkarren/selene>.
**Tier 2.** Supports: "selene is a blazing-fast modern Lua linter written
in Rust." Version 0.30.0 (2026-01-22) updated parser for recent Luau
features. License: Mozilla Public License 2.0.

**[80]** selene documentation site.
<https://kampfkarren.github.io/selene/>. **Tier 2.** Supports: built-in
`roblox` standard library configuration.

**[81]** GitHub. *UpliftGames/wally*.
<https://github.com/UpliftGames/wally>. **Tier 2.** Supports: "Wally is a
package manager for Roblox inspired by Cargo (Rust) and npm (JavaScript)";
`wally.toml` dependency manifest; two-part registry (index repo + API).
Registry at <https://github.com/upliftgames/wally-index>. License: Mozilla
Public License 2.0.

**[82]** GitHub. *Roblox/testez*. <https://github.com/Roblox/testez>.
**Tier 2.** Archived 2024-09-14. Supports: BDD-style Roblox testing
framework with `describe`/`it`/`expect`. Now read-only. License:
Apache 2.0.

**[83]** GitHub. *jsdotlua/jest-lua*. <https://github.com/jsdotlua/jest-lua>.
**Tier 2.** Supports: "Delightful Lua Testing"; Lua port of Jest (v27.4.7
alignment); "Jest Lua can currently only run inside of Roblox"; installed
via Wally. License: MIT.

**[84]** GitHub. *lune-org/lune*. <https://github.com/lune-org/lune>.
**Tier 2.** Latest v0.10.4 (2025-10-14). Supports: "a standalone Luau
runtime ... built in Rust"; fully async APIs for filesystem, networking,
stdio; includes "a familiar runtime environment for Roblox developers,
with an included 1-to-1 task scheduler port"; optional built-in library
for Roblox place/model files. License: Mozilla Public License 2.0.

**[85]** GitHub. *rojo-rbx/run-in-roblox*.
<https://github.com/rojo-rbx/run-in-roblox>. **Tier 2.** Supports: launches
Roblox Studio headlessly, pipes stdout/stderr back to terminal; CI bridge
for TestEZ and Jest-Lua.

**[86]** GitHub. *Roblox/place-ci-cd-demo*.
<https://github.com/Roblox/place-ci-cd-demo>. **Tier 2.** Supports: official
Roblox demo of a CI/CD pipeline using Rojo to build an RBXL, Open Cloud to
upload, and Engine Open Cloud API to execute Luau headlessly.

**[87]** Roblox DevForum (staff announcement). *[Beta] Open Cloud Engine
API for Executing Luau*.
<https://devforum.roblox.com/t/beta-open-cloud-engine-api-for-executing-luau/3172185>.
**Tier 2.** Supports: headless Luau execution via Open Cloud, concurrency
capped at "two concurrent requests per universe".

**[88]** Roblox. *Collaboration*.
<https://create.roblox.com/docs/projects/collaboration>. **Tier 2.** Living
doc. Supports: Team Create as Roblox Studio's real-time multi-user editing
mode.

**[89]** Roblox DevForum (staff announcement). *Script Editor - Better
Analysis and Luau-Powered Upgrades*.
<https://devforum.roblox.com/t/script-editor-better-analysis-and-luau-powered-upgrades/1167811>.
**Tier 2.** Supports: Script Editor integrates Luau type checking with
`--!strict` warnings and Script Analysis window.

## Security and exploits

**[90]** Roblox. *Security and cheat mitigation tactics*.
<https://create.roblox.com/docs/scripting/security/security-tactics>.
**Tier 2.** Updated 2025. Supports: canonical quote — **"Assume every piece
of data sent from the client has been manipulated, fabricated, or sent with
malicious intent."** Explicit defender-facing list of what exploiters can
do: decompile any replicated LocalScript/ModuleScript, take network
ownership of characters and unanchored parts, fire RemoteEvents/
RemoteFunctions with arbitrary arguments, modify player position and
physics, alter local code behavior.

**[91]** Roblox. *Server authority model*.
<https://create.roblox.com/docs/projects/server-authority>. **Tier 2.**
Living doc. Supports: "In a server authority model, the server is the
single source of truth for the entire experience state, and clients are
only trusted to report their own inputs." Core logic should be written in
ModuleScripts bound via `RunService:BindToSimulation()` and initialized on
both client and server, with the server maintaining authoritative state.

**[92]** Roblox DevForum (staff announcement). *Security Tactics and Cheat
Mitigation Docs Update!*.
<https://devforum.roblox.com/t/security-tactics-and-cheat-mitigation-docs-update/3959613>.
**Tier 2.** Date: 2025. Supports: announcement of the 2025 overhaul of the
official security docs.

**[93]** Roblox DevForum community tutorial. *A Comprehensive Guide To
Airtight Remote Security*.
<https://devforum.roblox.com/t/a-comprehensive-guide-to-airtight-remote-security/3079489>.
**Tier 3.** Date: 2024-07-21. Supports: type-based sanity checks on
OnServerEvent; RemoteEvent abuse vectors.

**[94]** Roblox DevForum community tutorial. *Keeping your Game Secure:
Part 1, Protecting Remotes*.
<https://devforum.roblox.com/t/keeping-your-game-secure-part-1-protecting-remotes/2788472>.
**Tier 3.** Date: 2024-01-11. Supports: server-side validation patterns,
rate limiting, type checking of remote arguments.

**[95]** Roblox DevForum (staff announcement). *Welcoming Byfron to
Roblox*.
<https://devforum.roblox.com/t/welcoming-byfron-to-roblox/2018233>. **Tier 2.**
Date: 2022-10-11. Supports: Roblox acquired Byfron to develop a
state-of-the-art anti-cheat (Hyperion).

**[96]** Roblox DevForum (staff announcement). *Exploit Prevention Update*.
<https://devforum.roblox.com/t/exploit-prevention-update/2663101>. **Tier 2.**
Date: 2023-04-27 (Hyperion rollout). Supports: platform-level anti-tamper
deployed, context for the exploit capability model.

**[97]** Roblox DevForum. *Advice on Remote Event Rate limiting*.
<https://devforum.roblox.com/t/advice-on-remote-event-rate-limiting/3100403>.
**Tier 3.** Supports: community-standard mitigation — 1-second client
cooldown plus server-side kick at >5 fires/second.

**[98]** Roblox DevForum. *Can exploiters edit LocalScripts or add them
into the client?*.
<https://devforum.roblox.com/t/can-exploiters-edit-localscripts-or-add-them-into-the-client/2317887>.
**Tier 3.** Supports: "Exploiters have access to compiled bytecode only, so
variable renaming does not affect exploiters since their Luau code is
reverse compiled anyway" — the canonical argument against source-level
obfuscation.

**[99]** Onnen, J. (Quenty). *Understanding Roblox networking and
FilteringEnabled: Part 1*. Medium post.
<https://medium.com/roblox-development/understanding-filteringenabled-part-1-3ccff00ba24c>.
**Tier 3.** Supports: FilteringEnabled mechanics — "When a LocalScript
modifies an object in the game, the change will be made on the client but
will not replicate to the server."

**[100]** Roblox Wiki (Fandom). *Experimental Mode*.
<https://roblox.fandom.com/wiki/Experimental_Mode>. **Tier 4.** Supports:
FilteringEnabled history. "On July 25th 2018, Roblox announced the removal
of Experimental Mode, meaning that all experiences that did not have the
FilteringEnabled property enabled would be treated as if it was enabled."
**Quality note:** Fandom wiki; used here only for history not covered by
first-party sources. Corroborate with primary sources where feasible.

---

## Source quality notes

- [63] vs [71]: the official `GetRequestBudgetForRequestType` page documents
  the *structure* of the rate limit formula (`baseLimit + perPlayerLimit *
  numPlayers`) but does not enumerate the default per-operation values. The
  commonly-cited values (`GetAsync = 60 + 10×numPlayers` etc.) come from
  [71], a community DevForum post. Cite these numbers as indicative rather
  than authoritative. Roblox could change them without updating the
  community post.

- [100]: Fandom wiki is Tier 4 and inherently less reliable than first-party
  sources. Used only for FilteringEnabled enforcement date (2018-07-25) where
  no equivalent first-party source was located. An archived Roblox blog post
  or engineering announcement would be a stronger citation if one can be
  found.

- [39] is from 2016 but remains authoritative because the underlying engine
  behavior (parent-assignment triggering replication/physics listeners) has
  not changed; the advice still holds in 2026.

- [12] vs [7]: the compound-assignment RFC [12] enumerates 7 operators;
  the syntax page [7] shows 8 (adding `//=` for floor division). This
  reflects feature evolution — [7] is authoritative for the current state.

## Gap log

- **Precise engine DataStore request budgets**: no first-party enumeration
  located; see [63] / [71] discrepancy.
- **UnreliableRemoteEvent transport layer details**: no Roblox engineering
  blog post located at the protocol level; [32] is the best available source.
- **Official retirement date for RenderStepped / Stepped**: [35] labels them
  "superseded" but does not give a deprecation date.
- **Fusion v0.3 feature list**: the specific reactive primitives (State,
  Computed, scope) were not fully extracted from [51]/[52]; cited
  generically as "reactive state objects with a declarative model".
