# Development tooling and workflow

This file covers the tools experienced Roblox teams use outside of Studio
itself: filesystem-based editing, linting, formatting, testing, package
management, and CI/CD.

See [citations](../citations.md) for source details.

## Studio-based workflow

**Roblox Studio** is the built-in IDE. Relevant features for Luau
development:

- **Script Editor with Luau analysis.** Integrates type checking with
  `--!strict` warnings and surfaces results in the Script Analysis window
  [89]. Highlights deprecated API usage and potential type errors in
  real time.
- **Team Create** [88]. "The real-time multi-user editing mode for
  collaborative development." Allows multiple editors in a single place
  file simultaneously.
- **Built-in debugger.** Breakpoints, conditional breakpoints, variable
  inspection, expression evaluation — standard debugger features
  integrated into the Script Editor.

The Studio-only workflow is perfectly viable for small projects. For
anything more than a couple of developers or a couple of scripts, teams
typically move to a filesystem-backed workflow.

## Rojo: filesystem ↔ Studio sync

[github.com/rojo-rbx/rojo][74] (License: Mozilla Public License 2.0).
Latest stable v7.6.1 released 2025-11-07 [74].

Rojo is the tool that makes professional editor and VCS workflows
possible for Roblox [74]: "a tool designed to enable Roblox developers
to use professional-grade software engineering tools." It lets you:

- Work on scripts and models from the filesystem in VS Code (or any
  editor) [74]
- Version-control with Git [74]
- Stream `rbxmx` and `rbxm` models into Studio in real time [74]
- Deploy to roblox.com from the command line [74]

### Project format

The `default.project.json` file describes the tree of Roblox instances
Rojo should sync [75]. Each node has a `$className` and may have `$path`
(pointing to a filesystem location) or `$properties` [75]. The tree
mirrors the Studio Explorer hierarchy (Workspace, ServerScriptService,
etc.).

From v7.6.1 onward, the project file format supports JSON comments and
trailing commas via `.jsonc` extension [76].

### Syncback

The upcoming v7.7.0 release adds a **`rojo syncback`** command that does
the reverse operation: converting an existing `.rbxl` place file back to
a filesystem-tracked Rojo project [76]. This solves a long-standing
problem of bringing legacy place-file projects into Git-based
workflows. Controlled by a `syncbackRules` field in the project file
[76]. The networking layer is also rewritten from long-polling to
WebSockets in v7.7 [76].

## Editor tooling

**luau-lsp** ([github.com/JohnnyMorganz/luau-lsp][77], MIT) is the
dominant Luau language server. Last push 2025-09-20 [77]. Features
[77]:

- Diagnostics including type errors
- Autocomplete, hover, signature help, go-to-definition, find references
- Document and workspace symbols
- Rename, code actions, inlay hints
- Moonwave-style documentation comments (`---` or `--[=[ ]=]`)
- Semantic tokens

Critical for Roblox-specific work: "By default, the latest Roblox type
definitions and documentation are preloaded out of the box" [77]. This
means autocomplete works on Roblox APIs (`Instance`, `RemoteEvent`,
etc.) without any manual type definition setup.

Installed via the VS Code marketplace or OpenVSX for other editors [77].

## Linting and formatting

**StyLua** ([github.com/JohnnyMorganz/StyLua][78], MPL-2.0) is a
deterministic code formatter that "mainly follows the Roblox Lua Style
Guide, with a few deviations" [78]. Supports Lua 5.1-5.4, LuaJIT, Luau,
and CfxLua [78]. Operates Prettier-style: parses and reprints from
scratch, erasing any existing formatting.

**selene** ([github.com/Kampfkarren/selene][79], MPL-2.0) is "a
blazing-fast modern Lua linter written in Rust" [79]. Supports Luau and
has a built-in `roblox` standard library configuration for Roblox-
specific globals [80]. Version 0.30.0 (2026-01-22) includes the most
recent Luau parser updates [79].

## Package management

**Wally** ([github.com/UpliftGames/wally][81], MPL-2.0) is "a package
manager for Roblox inspired by Cargo (Rust) and npm (JavaScript)" [81].
Uses a `wally.toml` dependency manifest and a two-part registry
(package index repo + API) [81]. The official registry lives at
[github.com/upliftgames/wally-index][81].

Dependency categories in `wally.toml` [81]:

- `[dependencies]` — runtime dependencies (shared between server and
  client)
- `[server-dependencies]` — server-only
- `[dev-dependencies]` — testing and development tools

## Testing

Two testing frameworks are widely used, with a recent stewardship shift.

### TestEZ — archived

**Repo**: [github.com/Roblox/testez][82]
**Status**: **Archived on 2024-09-14.** Repo is read-only [82].
**License**: Apache 2.0 [82]

TestEZ is the long-standing Roblox BDD framework with `describe`/`it`/
`expect` syntax, modeled on RSpec and Mocha [82]. Used by Roblox's own
core scripts, Studio plugins, and libraries like Roact. Still runs fine
for existing codebases but will not receive updates.

### Jest-Lua — active

**Repo**: [github.com/jsdotlua/jest-lua][83]
**License**: MIT [83]

Jest-Lua is the jsdotlua community port of Roblox's internal
`jest-roblox`, aligned to JavaScript Jest v27.4.7 [83]. Installed via
Wally (`JestGlobals = "jsdotlua/jest-globals@3.10.0"`) [83].

**Key constraint**: "Jest Lua can currently only run inside of Roblox"
[83]. This means CLI test runs require `run-in-roblox` [85] to launch
Studio headlessly, execute the suite, and pipe results back. Jest-Lua
cannot yet run in Lune [84] or any other standalone Luau runtime, so
pure-CLI CI requires the `run-in-roblox` wrapper.

Battle-tested status per the README [83]: Roblox internally uses
Jest-Lua for "testing applications, core scripts, Studio plugins, and
libraries like Roact Navigation".

### Decision: TestEZ vs Jest-Lua

| Scenario | Recommended |
|---|---|
| New project, no legacy tests | **Jest-Lua** (actively maintained) |
| Existing TestEZ suite, working fine | Keep TestEZ; migrate only when touching tests |
| Need Jest parity / snapshot testing / mocking | Jest-Lua (feature-parity with JS Jest) |

## Standalone runtimes

**Lune** ([github.com/lune-org/lune][84], MPL-2.0) is "a standalone Luau
runtime ... built in Rust" [84]. Latest v0.10.4 released 2025-10-14 [84].
It provides:

- Fully async filesystem, networking, and stdio APIs [84]
- "A familiar runtime environment for Roblox developers, with an
  included 1-to-1 task scheduler port" [84]
- An "optional built-in library for manipulating Roblox place & model
  files, and their instances" [84]

Lune is the best option for headless Luau code that doesn't need the
Roblox engine — build scripts, asset pipelines, CLI utilities, and
anything else that benefits from running outside of Studio. It is **not**
a Roblox engine replacement: code that touches Roblox APIs (Instances,
services, etc.) still needs to run in Studio or via the Engine Open
Cloud API [87].

## CI/CD

### run-in-roblox

**Repo**: [github.com/rojo-rbx/run-in-roblox][85]

The CI bridge: launches Studio headlessly, runs a script, and pipes
stdout/stderr back to the terminal [85]. It is how teams run TestEZ or
Jest-Lua suites from GitHub Actions or similar.

### Open Cloud Engine API for Luau execution

Announced in staff Beta [87]: "Your tools are able to headlessly run
Luau scripts in a Roblox place, within the Roblox engine, via Open
Cloud" [87]. Concurrency capped at "two concurrent requests per
universe" [87].

### Official Roblox CI/CD demo

[github.com/Roblox/place-ci-cd-demo][86] is Roblox's own demonstration
of a production-shaped pipeline:

1. Build an `.rbxl` file from a Rojo project [86]
2. Upload to Roblox via Open Cloud [86]
3. Execute Luau headlessly via the Engine Open Cloud API [86]

The CI/CD steps are implemented in `.github/workflows/cicd.yml` [86].
This is the canonical reference for "how do I actually wire this up".

## Typical modern stack

A modern Roblox project stack looks roughly like:

```
Filesystem layout    →  Rojo project.json
  |
  |
  V
VS Code + luau-lsp   →  type checking, autocomplete, docs
  |
  |
  V
StyLua + selene      →  format on save, lint on save
  |
  |
  V
Git for version control
  |
  |
  V
Jest-Lua test suites →  run-in-roblox in CI
  |
  |
  V
Wally for deps       →  wally.toml manifest
  |
  |
  V
GitHub Actions + place-ci-cd-demo pipeline
  |
  |
  V
Open Cloud publish to Roblox
```

## Gaps and limitations

- **Exact latest release dates for Wally, luau-lsp, and selene** were
  partially captured (some reported "last push" dates, others
  unspecified).
- **run-in-roblox maintenance status** is uncertain — the repo exists
  but no recent-commit date was captured. It may be superseded by
  Open Cloud Luau Execution for new CI pipelines.
- **Open Cloud Luau Execution API GA date** was not confirmed. The
  announcement [87] is from the Beta period.
- **TestEZ's formal deprecation messaging** was not captured beyond the
  2024-09-14 archive date; Roblox has not published a formal
  "use Jest-Lua instead" statement.
