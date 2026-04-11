# Script types and execution contexts

This file covers how Luau code actually runs inside a Roblox experience —
what kinds of scripts exist, where they must live to execute, and how the
server and client each see them.

See [citations](../citations.md) for source details.

## Three script types

Roblox has exactly three script object types [21]:

| Type | Role |
|---|---|
| `Script` | Runs either on server or client, depending on `RunContext` [21] |
| `LocalScript` | Runs only on the client; no `RunContext` property [21] |
| `ModuleScript` | Library code; runs only when another script calls `require()` on it [22] |

`LocalScript` is a legacy client-only type; modern Roblox code uses
`Script` with `RunContext = Client` instead of `LocalScript` [21]. Both
forms are still fully supported.

## RunContext

`RunContext` is a property on `BaseScript` (inherited by `Script`) that
controls which VM the script runs in [24][25][26]. Introduced in 2022-08-24
[26]; the `Plugin` value was added as a later update [26].

| RunContext | Runs where |
|---|---|
| `Legacy` | Default. Script runs server-side only when parented to Workspace or ServerScriptService [21][23] |
| `Server` | Server-side; can also run from ReplicatedStorage (though not recommended, as the script would replicate to clients) [21] |
| `Client` | Client-side; runs in ReplicatedStorage, StarterCharacterScripts, or StarterPlayerScripts [21] |
| `Plugin` | Plugin scripts only [26] |

Legacy is the default when you create a new Script [21]. The explicit
behavior: "A script's code is run in a new thread when its Enabled property
is true and the Script object is a descendant of the Workspace or
ServerScriptService" [23]. That rule — active only when both `Enabled`
and parented to a valid container — applies to all RunContext values.

## Container placement rules

Where a script lives determines whether it runs at all and which side it
runs on [21]:

| Container | Replicated to client? | Typical use |
|---|---|---|
| `ServerScriptService` | **No** — server only | Server-side `Script` with Legacy/Server RunContext |
| `ServerStorage` | **No** — server only | Server-only `ModuleScript` libraries, server data |
| `ReplicatedStorage` | **Yes** — both sides | Shared `ModuleScript`; remote event instances; Client-RunContext `Script` |
| `ReplicatedFirst` | Yes; runs before the default loading screen | Custom loading screen `LocalScript` |
| `StarterPlayerScripts` | Copied into each player's `PlayerScripts` on join; persists for the session | Client `LocalScript` or Client-RunContext `Script` |
| `StarterCharacterScripts` | Copied into each player's character on every spawn (including respawn) | Client scripts that need to re-run on respawn |
| `StarterGui` | Copied into player's PlayerGui | Client UI scripts |
| `StarterPack` | Copied into player's Backpack | Client scripts attached to tools |
| `Workspace` | Yes (replicated) | Legacy pattern — works but mixes concerns |

**Anti-pattern from the official performance guidance:** "Don't store
everything in ReplicatedStorage. The client loads everything that is in
this container. Instead, use ServerStorage for anything the client does
not need access to" [38].

## `LocalScript` lifecycle quirks

One documented gotcha on `LocalScript`: "LocalScripts cloned from
StarterGui or StarterPack into a player's PlayerGui or Backpack run before
the old character model is replaced, so `Player.Character` may refer to
the old model whose `Parent` property is nil" [21]. Code that assumes a
valid character at startup needs to defensively wait.

## `ModuleScript` semantics

`ModuleScript` execution is triggered by `require()` — it does not run on
its own [22]. The essential rules [22]:

1. **Return value requirement.** "ModuleScripts must return exactly one
   value" [22]. Typically a table of functions.
2. **Per-environment caching.** "ModuleScripts run once and only once per
   Luau environment and return the exact same value for subsequent calls
   to `require()`" [22]. The first `require` triggers execution; every
   subsequent `require` returns the cached result without re-running the
   module's code.
3. **Server/client isolation.** "Return values from ModuleScripts are
   independent with regards to Scripts and LocalScripts" [22]. The same
   `ModuleScript` in `ReplicatedStorage` runs **twice** if required from
   both sides — once in the server VM, once in each client VM — and
   each side gets its own return value. Mutations to the module's state
   on the client do not propagate to the server.
4. **Chain activation.** "If a ModuleScript requires another ModuleScript,
   a Script or LocalScript must require the first ModuleScript in the
   chain for any of them to run" [22]. A standalone `require` chain does
   not execute until something in a running `Script`/`LocalScript`
   pulls it in.

The per-VM isolation has a specific consequence: "Using `require()` on a
ModuleScript in a LocalScript will run the code on the client, even if a
Script did so already on the server" [22]. State inside a module is
**per-VM**, not global.

## Server/client boundary summary

Putting the above together, the replication and execution model is:

```
Server VM                        Client VM(s)
───────────                      ────────────
ServerScriptService ─ run        StarterPlayerScripts → PlayerScripts ─ run
ServerStorage       ─ store      StarterCharacterScripts → Character ─ run per-spawn
                                 ReplicatedFirst  ─ run before load screen

ReplicatedStorage ──────────────── ReplicatedStorage  (shared, replicated)
Workspace ──────────────────────── Workspace          (replicated, physics)
```

Scripts placed on the server side do not replicate; scripts placed in
replicated containers are visible to both sides. The choice of which VM
actually executes a given Script is a combination of container placement,
script type, and `RunContext` [21].

## Gaps and limitations

- **Exact content of `create.roblox.com/docs/projects/client-server`**
  (the replication matrix) was not fetched verbatim in this research
  pass; the matrix in this file is synthesized from the individual
  container reference pages and the scripting/locations page [21].
- **Whether `ServerStorage` is documented with the phrase "not
  replicated"**: Discovery sources confirm the behavior but the exact
  wording from the reference page was not extracted.
- **Exact LocalScript activation rule (the parallel to the Script
  `Enabled` + descendant rule)** is not quoted verbatim here; the `Script`
  page [23] covers the server side cleanly.
