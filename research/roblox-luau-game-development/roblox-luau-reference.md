# Roblox Luau: Technical Reference and Decision Framework

A citation-backed reference for developers writing Luau code on the
Roblox platform. Part 1 describes the platform model. Part 2 surveys
patterns and framework choices with trade-off tables. Part 3 catalogs
pitfalls and limitations.

Every factual claim has an inline `[N]` citation pointing to
[citations.md](citations.md). Dimension-specific details live in
[references/](references/) — this document is the synthesizing overview
with decision-aid tables.

---

## Part 1 — Platform model

### 1.1 The language: Luau, not Lua

Roblox's scripting language is **Luau**, a statically-typed, gradually-
typed dialect of Lua 5.1 with a bespoke VM, compiler, and standard
library [4][5][6]. Luau was open-sourced under MIT on 2021-11-03 [13]
and has been adopted by non-Roblox projects including Remedy's *Alan
Wake 2* and Digital Extremes' *Warframe* [20].

Key relationships to stock Lua [4]:

- Based on Lua 5.1, with selective incorporation of 5.2-5.4 features
- **Integer types and bitwise operators from Lua 5.3 are not
  incorporated** — use `bit32` for bitwise work
- `io`, `os`, `package`, `debug` libraries removed or stripped for
  sandboxing

The three type checking modes — `--!nocheck`, `--!nonstrict`,
`--!strict` — are selected by pragma on the first line [8]. Nonstrict is
default; all variables get `any` unless explicitly annotated [8]. A new
type solver went GA on 2025-11-20 [19] and is rolling out to all users.

Luau adds real syntax extensions over Lua 5.1 [7]:

- Generalized iteration: `for k, v in t do` without `pairs`/`ipairs` [10]
- Backtick string interpolation: `` `Hello {name}` `` [11][14]
- Compound assignments: `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `^=`, `..=`
  [7][12]
- `continue` statement (context-sensitive keyword) [7]
- If-then-else expressions (`local x = if cond then a else b`) [7]
- Type annotations and aliases (`: Type`, `::`, `type`, `export type`) [7]
- Floor division `//`, `//=`, `__idiv` metamethod [7]
- Number literals with `_` separators: `1_048_576` [7]

Full treatment in [references/luau-language.md](references/luau-language.md).

### 1.2 Execution model

Code runs in one of three script types [21]:

- **`Script`** — runs on server or client depending on `RunContext` [21]
- **`LocalScript`** — legacy client-only [21]
- **`ModuleScript`** — library code, runs only on `require()` [22]

`RunContext` values: `Legacy` (default, server-only), `Server`, `Client`,
`Plugin` [21][24][26]. Introduced 2022-08-24 [26]. Modern Roblox code
prefers `Script` with `RunContext = Client` over `LocalScript`.

The placement rules matter. A `Script` with Legacy RunContext "is run in
a new thread when its Enabled property is true and the Script object is
a descendant of the Workspace or ServerScriptService" [23]. ModuleScripts
"run once and only once per Luau environment and return the exact same
value for subsequent calls to `require()`" [22] — and critically, the
server and each client have **independent Luau environments**, so the
same module required from both sides runs twice with per-VM state [22].

Full treatment in [references/script-types-execution.md](references/script-types-execution.md).

### 1.3 The client-server boundary

Roblox enforces a strict replication filter (historically called
FilteringEnabled, now Experience Filtering) that blocks automatic
client-to-server state changes [99][100]. Cross-boundary communication
uses four instance types [27][28][29][31]:

| Instance | Direction | Yields? | Reliable? | Ordered? |
|---|---|---|---|---|
| `RemoteEvent` [27] | Both | No | Yes | Yes |
| `RemoteFunction` [28] | Both | Yes (waits for return) | Yes | Yes |
| `UnreliableRemoteEvent` [29] | Both | No | **No** | **No** |
| `BindableEvent` / `BindableFunction` [31] | Same VM only | Varies | — | — |

`UnreliableRemoteEvent` was introduced 2023-11-29 [32]; its payload is
capped at **1000 bytes** (raised from 900 on 2025-03-12) [29][32].
Messages exceeding the cap are silently dropped [29].

`RemoteEvent` has a per-client rate limit of ~500 requests/second, shared
across all RemoteEvents of the same type [27]. Server-side validation
and rate limiting are mandatory because the client is untrusted (see §3).

Full treatment in [references/client-server-communication.md](references/client-server-communication.md).

### 1.4 Scheduling primitives

The frame budget at 60 FPS is **16.67 ms** [38]. Per-frame work must
either stay well under this or be sliced across frames with
`task.wait()` [38].

The `RunService` events (current official names) [35]:

```
PreRender (client only) -> PreAnimation -> PreSimulation -> (physics) -> PostSimulation -> Heartbeat
```

`RenderStepped` and `Stepped` are the older names, now officially
"superseded by" `PreRender` and `PreSimulation` respectively [35].

Code that writes physics state (Velocity, CFrame) uses `PreSimulation`;
code that reads physics state uses `PostSimulation` [35]. Client visual
code uses `PreRender`.

The `task` library [36] replaces legacy `spawn`/`wait`/`delay` — more
optimized, not throttled, and tied into the new scheduler:

| Call | Meaning |
|---|---|
| `task.spawn(f)` | Resume now |
| `task.defer(f)` | Resume at end of current resumption cycle |
| `task.wait(n)` | Yield for n seconds, resume on next Heartbeat |
| `task.delay(n, f)` | Fire-and-forget after n seconds |
| `task.cancel(thread)` | Kill a coroutine |

Parallel Luau (via `Actor`, `task.synchronize`/`task.desynchronize`,
`SharedTable`) [37][41][42] enables multi-core execution. Scripts in the
same Actor still run serially relative to each other — multiple Actors
are required for parallelism [37]. Parallel code can't call `require()`
[37].

Full treatment in [references/performance.md](references/performance.md).

### 1.5 Data persistence primitives

Two first-party systems:

**`DataStoreService`** — durable per-player save data with strict limits
[62]:

- Per-key payload: **4,194,304 characters** (4 MiB)
- Data store / key name / scope: 50 characters each
- Throughput: 25 MB/min read, 4 MB/min write (per key)
- Experience-wide storage: **100 MB + 1 MB × lifetime users**
- Versions expire after 30 days [64]

Request budgets follow `baseLimit + perPlayerLimit × numPlayers` [63].
Exact defaults per operation are not enumerated on the official docs;
community-compiled values exist [71] but should be verified at runtime
with `GetRequestBudgetForRequestType`.

**`MemoryStoreService`** — cross-server shared state with per-partition
limits of 150,000 RPM in the best case [66]. Experience-wide quota
`1000 + 100 × concurrentUsers` request units per minute [67]. Max item
expiry 45 days [65].

`DataStoreService` raw is not safe for significant save data because
**multi-key atomicity is impossible** [73] and **`BindToClose` is
unreliable** [72]. The community standard wrapper is **ProfileStore**
[69] (successor to ProfileService [68]), which handles session locking,
auto-saving, and schema reconciliation.

Full treatment in [references/data-persistence.md](references/data-persistence.md).

---

## Part 2 — Patterns and decisions

### 2.1 When to use which remote

```
Need a return value?
- Yes (and it's client -> server) -> RemoteFunction [28]
- Yes (and it's server -> client) -> DON'T. Use RemoteEvent + callback. [28]
- No
  - Critical for game state?
    - Yes -> RemoteEvent [27]
    - No  -> UnreliableRemoteEvent [29] (if payload <= 1000 bytes)
  - Same-VM only -> BindableEvent / BindableFunction [31]
```

The "never server -> client with RemoteFunction" rule comes directly
from Roblox's own docs [28]: "If the client doesn't return a value, the
server yields forever", plus errors on client-side exceptions and
disconnects. Use `RemoteEvent:FireClient` and have the client send back
a separate `RemoteEvent` if you need a response.

### 2.2 When to use which RunService event

Current names (the `PreX` names) [35]:

| Event | Purpose |
|---|---|
| `PreRender` (client only) | Visual code that must see the latest state |
| `PreAnimation` | Before physics, after rendering |
| `PreSimulation` | Write physics state (Velocity, CFrame) |
| `PostSimulation` | Read physics state after it's resolved |
| `Heartbeat` | Generic per-frame work without physics ordering concerns |

Legacy names (`RenderStepped`, `Stepped`) still work but are superseded
[35]. New code should use the `PreX`/`PostX` names.

### 2.3 When to use which task function

| Need | Call | Why |
|---|---|---|
| Run a coroutine now | `task.spawn(f)` [36] | Immediate resumption |
| Run after current code finishes | `task.defer(f)` [36] | Avoids re-entry |
| Sleep N seconds and continue | `task.wait(n)` [36] | No throttling, precise timing |
| Fire-and-forget after delay | `task.delay(n, f)` [36] | Single-shot timer |
| Never: legacy `wait(n)` | Replaced by `task.wait` [36] | Throttled, less precise |

### 2.4 When to use which typing mode

| Context | Recommended mode | Why |
|---|---|---|
| Learning / prototyping | `--!nonstrict` (default) | Forgiving; still surfaces explicit annotations |
| Library / shared module | **`--!strict`** | Prevents API drift; callers get proper autocomplete |
| Performance-critical / `--!native` code | **`--!strict`** + explicit annotations on function parameters | Mistyped params trigger native deoptimization [9] |
| Legacy code you don't own | `--!nocheck` | Avoids noise from code you can't change |

The cost-benefit flipped with the new type solver GA in late 2025 [19]:
strict mode is now far less noisy than it was. The 2024 telemetry paper
[3] — 340,000+ Studio sessions — is explicit that the Luau type system
is tuned to minimize false positives, specifically to keep beginners
from being scared off strict mode.

### 2.5 When to use which architecture framework

| Need | Option | Maintenance risk |
|---|---|---|
| Server/client service layer | **Knit** [47] (archived but stable) or roll-your-own on raw modules | High (archived) |
| TypeScript ecosystem equivalent | Flamework on roblox-ts [59][60] | Active |
| Reactive UI (Luau-native) | **Fusion v0.3+** [51] | Active |
| Reactive UI (React-style) | **React-Lua (jsdotlua fork)** [57] | Active |
| Simulation-heavy game logic | **Matter ECS** [53][54] | Active; stewardship moved 2024-07 |
| Nothing fancy, just organize code | Plain ModuleScripts + official patterns [61] | N/A |

**The Knit problem.** Knit is archived [47]. For new projects, the
choices are: use it anyway (stable, battle-tested, zero new features),
build a thin service/controller layer on plain modules, or move to the
TypeScript ecosystem with Flamework [60]. There is no first-party
Roblox framework filling this niche.

### 2.6 When to use which data persistence option

| Scenario | Recommended | Why |
|---|---|---|
| One-off trivial state (leaderboards, server picks) | Raw `DataStoreService` | Overhead not worth it |
| Per-player save data (inventory, progression, currency) | **ProfileStore** [69] | Session locking prevents duplication; schema reconcile |
| Existing ProfileService codebase | Keep ProfileService [68]; migrate lazily | Backwards-compatible with ProfileStore |
| Cross-server shared state (matchmaking, leaderboards) | `MemoryStoreService` [65][66] | Purpose-built for this |
| Multi-key atomic updates (trading systems) | **None safe** — design around single-key updates [73] | Roblox doesn't expose transactions |

### 2.7 When to use which test framework

| Scenario | Recommended |
|---|---|
| New project | **Jest-Lua** [83] (active) |
| Legacy TestEZ suite | Stay; TestEZ is archived [82] but still works |
| Need CLI/CI integration | Both require `run-in-roblox` [85] or similar |

### 2.8 When to use `--!native`

[9] is unambiguous: measure before enabling. Rules of thumb:

- **Enable on**: server-side scripts doing heavy math on tables or
  `buffer` types; tight inner loops with typed parameters
- **Don't enable on**: scripts that call Roblox APIs often; scripts
  with `getfenv`/`setfenv`; client scripts (currently unavailable
  anyway per [9])
- **Strict typing is a prerequisite**: mistyped parameters trigger
  deoptimization that can make native code *slower* than interpreted
  [9]

---

## Part 3 — Pitfalls and limitations

### 3.1 Performance anti-patterns

All from official sources:

- **Per-frame polling** when an event could drive the work [38]. The
  first-line recommendation in Roblox's own docs: "Whenever possible,
  write event-driven code rather than per-frame calculations".
- **`Instance.new("Part", parent)`** — using the parent argument [39].
  Once parented, every property write triggers replication and physics
  contact recalculation. Set properties first, assign Parent last.
- **Legacy `spawn`/`wait`/`delay`** [36][40]. Throttled to ~30 FPS,
  less optimized than `task` equivalents.
- **Not disconnecting signal connections** [38]. "Use `RBXScriptConnection:Disconnect()`
  to stop functions from being called unnecessarily".
- **Storing everything in `ReplicatedStorage`** [38]. "The client loads
  everything that is in this container. Instead, use `ServerStorage`
  for anything the client does not need access to".
- **Frequent `task.synchronize`/`task.desynchronize` in a hot loop**
  [37] — the synchronization overhead eats the parallelism benefit.

### 3.2 Data persistence failure modes

- **`BindToClose` is unreliable** [72]. Servers routinely exceed the
  shutdown deadline before the callback completes. Don't rely on it
  for final saves. Save periodically instead.
- **Multi-key atomicity is impossible** [73]. This prevents safe
  cross-player transactions (trading, gifting). Design data models
  around single-key updates per player.
- **DataStore write throughput is 4 MB/min per key** [62]. Hot keys
  saturate quickly; shard heavily used keys or batch writes.
- **Version history expires after 30 days** [64]. Not a backup system.

### 3.3 Security failure modes

- **Client-side obfuscation is ineffective** [98]. Exploiters work with
  bytecode, not source. Variable renaming and control-flow flattening
  do not slow a determined attacker.
- **Any replicated `LocalScript` or `ModuleScript` is fully visible**
  [90]. Don't put secrets in replicated containers. If it's on the
  client, assume it's public.
- **RemoteFunctions that invoke the client deadlock on silent
  clients** [28]. "If the client doesn't return a value, the server
  yields forever". Use `RemoteEvent:FireClient` and a callback remote
  instead.
- **Client-side argument validation is decorative** [90]. Anything
  important must be re-checked on the server. Type-check, range-check,
  scope-check, ownership-check — every argument, every call.
- **Platform anti-cheat (Hyperion)** [95][96] mitigates some exploits
  but does not replace server-side validation.

### 3.4 Language and runtime caveats

- **`getfenv`/`setfenv` disable optimizations** including import
  optimization [5][6]. Avoid in hot paths and in scripts you want to
  `--!native`-compile.
- **ModuleScripts run once per VM**, meaning a module required from
  both server and client runs twice with independent state [22]. Do
  not assume cross-boundary state sharing.
- **`require()` is forbidden in desynchronized parallel code** [37].
  All module loading must happen before crossing into parallel.

### 3.5 Tooling caveats

- **Rojo project files have a v6/v7 format split** — v7.7 introduces
  syncback [76], a feature that didn't exist in v6.
- **TestEZ is archived on 2024-09-14** [82]; Jest-Lua [83] is the
  actively-maintained alternative but **only runs inside Roblox** (via
  `run-in-roblox` for CI).
- **Knit is archived** [47]. Active ecosystem frameworks are Flamework
  (TypeScript only), Fusion (UI only), and Matter (ECS only). There
  is no active Luau-native services/controllers framework as of 2026.

### 3.6 Documented but unresolved gaps

Things this research could not pin down from first-party sources:

- **Exact per-operation default DataStore request budgets** ([63] shows
  the formula structure but not the defaults; [71] is community-
  compiled)
- **Exact historical DataStore payload limit before the 4 MB increase**
- **UnreliableRemoteEvent transport-layer implementation** (UDP? custom?)
- **Per-message reliable RemoteEvent byte limit**
- **FilteringEnabled enforcement date (2018-07-25)** — only located in
  Fandom wiki [100], not first-party
- **Native codegen client availability status as of 2026**
- **Exact performance speedup from `--!native`** for compute-heavy code

These are flagged in each reference file's "Gaps and limitations"
section as well.

---

## Reading map

- Full language details: [references/luau-language.md](references/luau-language.md)
- Script types and placement: [references/script-types-execution.md](references/script-types-execution.md)
- Client-server communication: [references/client-server-communication.md](references/client-server-communication.md)
- Performance and scheduling: [references/performance.md](references/performance.md)
- Architecture patterns and frameworks: [references/architecture-frameworks.md](references/architecture-frameworks.md)
- Data persistence: [references/data-persistence.md](references/data-persistence.md)
- Development tooling: [references/tooling-workflow.md](references/tooling-workflow.md)
- Security and exploits: [references/security-exploits.md](references/security-exploits.md)

All citations: [citations.md](citations.md)
Verification reports: [audit/citation-audit.md](audit/citation-audit.md),
[audit/consistency-review.md](audit/consistency-review.md)
