# Roblox Luau game development

Citation-backed reference for writing Luau code on the Roblox platform.
Covers the language, execution model, client-server boundary, scheduling
and performance, architecture frameworks, data persistence, development
tooling, and security. Every factual claim has an inline `[N]` citation
pointing to [citations.md](citations.md).

## The shortest possible summary

Roblox runs **Luau**, not Lua. It's a statically-typed, gradually-typed
dialect of Lua 5.1 with a bespoke VM and sandbox. The type system has
three modes (`--!nocheck` / `--!nonstrict` / `--!strict`) and a new type
solver hit GA on 2025-11-20 [19]. The open-source Luau runtime [13] has
been adopted by games like *Alan Wake 2* and *Warframe* [20].

Every game runs in two VMs: one server and one per-client. Code crosses
the boundary only through `RemoteEvent` / `RemoteFunction` /
`UnreliableRemoteEvent`, and the server must treat every argument from
the client as hostile. The platform enforces this: **"Assume every
piece of data sent from the client has been manipulated, fabricated, or
sent with malicious intent"** [90].

For anything non-trivial, teams use filesystem-based tooling (Rojo +
VS Code + luau-lsp + StyLua + selene + Wally) rather than editing
inside Studio directly. Tests run via Jest-Lua (TestEZ is archived
[82]) bridged through `run-in-roblox` in CI.

Save data goes through **ProfileStore** [69] (the actively-maintained
successor to ProfileService [68]) rather than raw `DataStoreService`,
because the raw API has data-loss pitfalls around `BindToClose` [72]
and no multi-key atomicity [73].

## The core decision tables

### Pick a remote type

| You need... | Use |
|---|---|
| Client → server request/response | `RemoteFunction` [28] |
| Server → client call | **Never `RemoteFunction`**; use `RemoteEvent:FireClient` [28] |
| Ordered, reliable event either direction | `RemoteEvent` [27] |
| High-frequency ephemeral updates (particles, SFX triggers) | `UnreliableRemoteEvent` — max 1000 bytes [29][32] |
| Same-VM signaling (server ↔ server or client ↔ client) | `BindableEvent` / `BindableFunction` [31] |

### Pick a RunService event

| You need... | Use |
|---|---|
| Write physics state (Velocity, CFrame) | `PreSimulation` [35] |
| Read physics state | `PostSimulation` [35] |
| Client visual code that needs latest state | `PreRender` (client only) [35] |
| Generic per-frame work | `Heartbeat` [35] |

`RenderStepped` and `Stepped` are older names now superseded [35] but
still work.

### Pick a persistence backend

| Your data is... | Use |
|---|---|
| Per-player save data (inventory, progression, currency) | **ProfileStore** [69] |
| Cross-server shared state (matchmaking, global leaderboards) | `MemoryStoreService` [65][66] |
| Version-history-tracked critical data | DataStore versioning (30-day expiry) [64] |
| Multi-key atomic transactions (trading) | **Not possible** — redesign around single keys [73] |

### Pick an architecture framework

| You need... | Use | Risk |
|---|---|---|
| Server/client service layer | Knit [47] | **Archived** — still stable, no updates |
| Reactive UI, Luau-native | Fusion v0.3+ [51] | Active |
| Reactive UI, React-style | React-Lua (jsdotlua fork) [57] | Active |
| Simulation-heavy ECS | Matter [53][54] | Active; stewardship moved 2024-07 |
| TypeScript ecosystem | roblox-ts + Flamework [59][60] | Active |
| Nothing fancy | Plain ModuleScripts + official patterns [61] | N/A |

## The 5-step quick-start

1. **Install tooling.** VS Code + [luau-lsp][77] + [StyLua][78] +
   [selene][79] + [Rojo][74] + [Wally][81] + [Lune][84]. Everything
   except Lune is free and cross-platform.

2. **Initialize a Rojo project.** Define `default.project.json` with
   your Studio tree [75]. Point it at a `src/` folder full of `.luau`
   files. Track that folder in Git.

3. **Pick `--!strict` for new code.** The new type solver minimizes
   false positives [3][19]. Strict mode in 2026 is far less noisy
   than it was in 2022.

4. **Use `task.spawn`/`task.defer`/`task.wait`, not `spawn`/`wait`/
   `delay`.** The legacy globals are deprecated [36][40]. Use
   `RunService:PreSimulation` / `PostSimulation` rather than
   `Stepped` / `Heartbeat` for new code [35].

5. **Validate every remote call on the server.** Type-check arguments,
   range-check numbers, scope-check instance references, rate-limit
   per player. Community baseline [97]: kick at >5 fires/sec. Assume
   the client is an adversary [90].

## The full reference

Read [roblox-luau-reference.md](roblox-luau-reference.md) for the
complete reference + decision framework (Parts 1, 2, 3 covering
platform model, patterns, and pitfalls).

Dimension-specific deep dives:

- **[Luau language](references/luau-language.md)** — types, syntax,
  sandbox, native codegen
- **[Script types & execution](references/script-types-execution.md)** —
  Script / LocalScript / ModuleScript; RunContext; container placement
- **[Client-server communication](references/client-server-communication.md)** —
  RemoteEvent / RemoteFunction / UnreliableRemoteEvent / BindableEvent
- **[Performance](references/performance.md)** — frame budget, task
  library, RunService events, Parallel Luau, profiling
- **[Architecture & frameworks](references/architecture-frameworks.md)** —
  Knit, Fusion, Matter, React-Lua, roblox-ts, plain modules
- **[Data persistence](references/data-persistence.md)** — DataStore
  limits, MemoryStore, ProfileStore session locking
- **[Tooling & workflow](references/tooling-workflow.md)** — Rojo,
  luau-lsp, StyLua, selene, Wally, TestEZ/Jest-Lua, Lune, CI/CD
- **[Security & exploits](references/security-exploits.md)** — trust
  model, attacker capabilities, validation patterns

All citations: **[citations.md](citations.md)**.

Verification reports (two independent audit passes):

- [audit/citation-audit.md](audit/citation-audit.md)
- [audit/consistency-review.md](audit/consistency-review.md)

## Scope and limits

**Not covered**: teaching Luau from scratch; exhaustive API enumeration
(cite the official API reference for that); game design, art, audio, or
monetization; comparing Roblox to other game engines.

**Source recency**: Roblox/Luau is a fast-moving platform. Fetches
in this research were captured in April 2026. For performance, tooling,
and framework claims, prefer the cited source's own current version. The
foundational execution-model and language facts are stable across
years.

**Known gaps** (documented in each reference file's "Gaps and
limitations" section):

- Exact per-operation default DataStore request budgets (community-
  compiled values only [71])
- UnreliableRemoteEvent transport-layer details
- Exact performance speedup from `--!native` for compute-heavy code
- FilteringEnabled enforcement date (2018-07-25) was only located on
  Fandom wiki [100], not a first-party source
