# Architecture patterns and frameworks

This file catalogs the module-organization patterns and third-party
frameworks that experienced Roblox teams use, along with current
maintenance status for each.

See [citations](../citations.md) for source details.

## Raw ModuleScript patterns

Before reaching for a framework, the default is plain `ModuleScript`s. The
official creator docs include a page on common patterns [61]:

- **Singleton / namespace module.** Return a table of functions; callers
  `require` once per VM and get the cached instance [22][61].
- **Factory module.** Return a function that constructs new objects with
  per-instance state.
- **Metatable-based OOP.** Return a "class" table whose `__index` points
  to itself; `new()` constructors set a metatable.

The per-VM caching rules from [22] — "ModuleScripts run once and only
once per Luau environment" — make the singleton pattern the natural
default for per-VM shared state. The server-client independence rule
("using require on a ModuleScript in a LocalScript will run the code on
the client, even if a Script did so already on the server") means any
module placed in `ReplicatedStorage` and required from both sides runs
**twice** — once per VM — with independent state.

## Frameworks currently in wide use

Four main frameworks + one TypeScript ecosystem, with their canonical
repos and current status.

### Knit — archived but battle-tested

**Repo:** [github.com/Sleitnick/Knit][47]
**License:** MIT [47]
**Status:** **Archived.** "Knit has been archived and will no longer
receive updates" [47].

Knit is Stephen Leitnick's services/controllers framework: a
`KnitService` on the server exposes a `.Client` table, which Knit
automatically wires up to RemoteFunction/RemoteEvent infrastructure
[47][48]. On the client, `KnitController`s consume services via a
generated client-side proxy. The framework abstracts remote plumbing so
developers write business logic, not serialization glue.

The author's own summary from Medium [49]: "Knit serves as the backbone
of many Roblox games, contributing to millions of dollars of revenue
every year." Even after archiving, Leitnick has described it on the
DevForum as still reliable [50]: "Knit is a battle-tested framework that
has stood strong and scaled well, with games with literally hundreds of
thousands of concurrent players utilizing Knit without a hitch."

**When to use:** existing Knit codebases; teams that value the
service/controller split and don't need active maintenance. **When to
avoid:** net-new projects where long-term framework support matters.

### Fusion — active reactive UI

**Repo:** [github.com/dphfox/Fusion][51]
**License:** MIT [51]
**Version:** 0.3 (released 2024-08-30) [51]
**Author:** Daniel P. H. Fox (dphfox / Elttob)

Fusion is "a portable Luau companion library for simpler, more descriptive
code" [51]. It provides reactive state objects and declarative UI
construction — a different paradigm from React-style component trees. v0.3
introduced scope-based memory management and contextual value sharing [51].

Docs for v0.2 live at [elttob.uk/Fusion/0.2/][52]; v0.3 docs exist but
were not verified in this research pass.

**When to use:** UI-heavy games where the code is mostly reactive state
derivation; teams preferring Fusion's scope-based approach over React's
component model.

### React-Lua — active React 17 port

**Repo:** [github.com/jsdotlua/react-lua][57]
**License:** unspecified from extracted content
**Status:** actively maintained

`jsdotlua/react-lua` is the community fork of Roblox's internal
`react-lua`, stated as aiming to be "the Roblox and global Lua community
go-to for React in Lua" [57]. It translates ReactJS 17.x into Lua [57],
including hooks, functional components, and the full reconciler.

Roblox's own `Roblox/react-luau` repo [58] is a read-only mirror — "not
open for community contribution" and "not published to any public package
registry" [58]. For any team outside Roblox, the `jsdotlua` fork is the
only practical choice.

**When to use:** teams with React experience; large UIs where component
composition is preferred over reactive state graphs.

### Matter — active ECS

**Repo:** [github.com/matter-ecs/matter][53]
**License:** MIT [53]
**Lineage:** Originally `evaera/matter` [55], archived 2024-07-16 and
migrated to the `matter-ecs` organization [53][55]

"Matter is a modern ECS library for Roblox" [53]. The Why-ECS docs page
makes Matter's design argument explicit [54]: "Behavior in ECS is
declarative — systems run every frame and declare what the state of the
world should be right now. This makes code self-healing and more
resilient to game-breaking bugs than in an event-driven model."

Matter's stewardship transition (2024-07) is a notable risk signal for
teams evaluating it: the change was a voluntary maintainer handoff, not
an abandonment. Migration from the old `evaera/matter` Wally scope to
`matter-ecs/matter` is mechanical.

**When to use:** simulation-heavy games (hundreds of interacting
entities); teams already comfortable with ECS from Bevy or Unity DOTS.
**When to avoid:** small projects where the ECS setup cost outweighs the
benefits.

### Roact — legacy

**Repo:** [github.com/Roblox/roact][56]
**Status:** Legacy; official tutorials marked "(Deprecated)"

Roact was Roblox's earlier React-inspired UI library [56]. It is no
longer the recommended path; teams using Roact should plan migration to
react-lua [57].

## TypeScript ecosystem: roblox-ts + Flamework

**roblox-ts** [59] is a TypeScript-to-Luau compiler. Repo has ~948 stars
as of December 2024, growing to ~1.2k by mid-2025 [59]. The
`roblox-ts.com/docs/` entry point positions it as "great for managing
large scale projects, with static types and intellisense allowing
developers to understand their code more deeply".

**Flamework** [60] is the roblox-ts equivalent of Knit — "an extensible
game framework" requiring TypeScript, with "built-in dependency
injection". A DevForum tutorial frames the decision plainly: "Switching
into Roblox TS means switching from Knit and switching to Flamework".

**When to use:** teams with strong TypeScript experience, tolerating the
additional compile step for type safety beyond Luau's gradual system;
large codebases where dependency injection and tsconfig-style tooling
pay off. **When to avoid:** small teams; teams that want to stay within
the Luau ecosystem's direct tooling.

## Decision framework

The choice between frameworks depends primarily on what problem you're
solving:

| Need | Recommended |
|---|---|
| Networking abstraction, service/controller layout | Knit [47] (legacy) or Flamework [60] (TS) |
| Declarative reactive UI, Luau-native | Fusion [51] |
| React-style UI, component model | React-Lua (jsdotlua fork) [57] |
| Simulation-heavy game logic | Matter ECS [53][54] |
| Just organize code, nothing fancy | Raw ModuleScripts + official patterns [61] |
| Large codebase, strong typing, TS tooling | roblox-ts + Flamework [59][60] |

**Key risk**: Knit is archived [47]. For new projects choosing a
networking framework, the options are (a) accept the archive risk and use
Knit anyway, (b) build your own thin service/controller wrapper on top
of raw ModuleScripts and remotes, or (c) move to roblox-ts + Flamework.
There is no first-party Roblox replacement.

A useful cross-framework comparison gist by sloont [source: Discovery
Agent, `gist.github.com/sloont/f7e58b931fc19fdec16c9aee94050ce2`]
observes that "no framework combines all three features" of structured
server/client splits, networking ergonomics, and change detection with
automatic delta replication. Teams that want all three typically
compose two frameworks (e.g., Knit for networking + Matter for
simulation).

## Gaps and limitations

- **Exact commit recency** for Fusion, roblox-ts, and react-lua was not
  verified in this pass; all were reported as "actively maintained" but
  dates weren't extracted.
- **Star counts** for Knit, Fusion, and Matter are not cited here — the
  github READMEs do not expose that count in the extracted content.
- **Fusion v0.3 API details** (the specific reactive primitives — State,
  Computed, Observer, Values, etc.) were not fetched in this pass.
- **TestEZ/Jest-Lua are covered in `tooling-workflow.md`**, not here,
  since they're testing tools rather than architecture frameworks.
- **Nevermore** (Quenty's framework) was mentioned in the Discovery
  cross-framework gist but not researched directly here.
