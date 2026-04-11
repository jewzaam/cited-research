# Luau language vs standard Lua

This file covers Luau — the language Roblox scripts are actually written in.
Luau is a statically-typed, gradually-typed dialect of Lua 5.1 with a
bespoke compiler, VM, and standard library [4][5][6]. Roblox built it; they
released it as open source under the MIT license on 2021-11-03 [13][20],
and it has been adopted by at least a few non-Roblox game projects
including Remedy's *Alan Wake 2*, Digital Extremes' *Warframe*, and Giants
Software's *Farming Simulator 2025* [20].

See [citations](../citations.md) for source details.

## Relationship to Lua

Luau is based on Lua 5.1 [4]. It incorporates selected features from Lua
5.2, 5.3, and 5.4 but deliberately omits others [4]:

| Lua version | Incorporated into Luau | Not incorporated |
|---|---|---|
| 5.2 | Yieldable `pcall`/`xpcall`, `bit32` library, `__len` metamethod, string hex escapes (`\x`), `\z` escape, frontier patterns [4] | — |
| 5.3 | UTF-8 support, `\u` escapes, `string.pack`/`unpack`/`packsize`, floor division (`//`), `table.move` [4] | **Integer types, bitwise operators** — "rejected due to backwards compatibility and performance implications" [4] |
| 5.4 | New `math.random` implementation, `coroutine.close`, `__tostring` support in `print` [4] | — |

The integer-type omission is notable: Luau uses only Lua 5.1-style doubles
for numbers. `bit32` (from 5.2) handles bitwise ops in the absence of
native integer support [4].

## Type system

Luau's type system is a gradual, optional system designed for a
"heterogeneous developer community" [1]. It is documented across three
peer-reviewed papers from the Roblox team: HATRA 2021 [1], HATRA 2023 [2],
and a 2024 Programming journal paper [3] reporting telemetry from 340,000+
Roblox Studio sessions.

### Three type checking modes

Every Luau script can select one of three modes via a pragma on the first
line [7][8]:

| Pragma | Behavior |
|---|---|
| `--!nocheck` | Type checking completely disabled for the script [8] |
| `--!nonstrict` | Default mode. "All variables are assigned the type `any`" unless explicitly annotated [8] |
| `--!strict` | Full checking; "every value has a known type" [8] |

A workspace-wide default can be set via `Workspace.LuauTypeCheckMode` [8].
Type mismatches "are highlighted in the Script Editor and surfaced as
warnings in the Script Analysis window" [8].

### New type solver

Roblox is migrating to a new type solver. It entered beta on 2024-09-13
[18] and reached general release on 2025-11-20 [19], initially rolling
out to nocheck and nonstrict users with new Scripting workspace
properties for configuration [19]. HATRA 2023 [2] describes its key
design choices — semantic subtyping and type error suppression.

### Type annotation syntax

Type annotations use `:` for variable and parameter types and `::` for
type casts; `type` declares aliases and `export type` makes them importable
[7]. `typeof(expr)` is a compile-time query (it does not evaluate its
argument at runtime).

## Syntax extensions over Lua 5.1

The Luau syntax page [7] is the authoritative enumeration. The
incrementally-added features:

**Generalized iteration** [7][10]. `for k, v in t do` iterates tables
directly; the `__iter` metamethod (invoked once at loop startup) allows
custom containers to participate. This makes `pairs`/`ipairs` "mostly
obsolete" [10].

```lua
for k, v in {1, 2, 3} do print(k, v) end
```

**String interpolation** [7][11][14]. Backticks with `{...}` expressions.
Added February 2023 [14]. Desugars to `string.format` calls, with a new
`%*` token that calls `tostring` on arbitrary types [11].

```lua
print(`Hello {world}!`)
```

Restrictions: `{{` is explicitly rejected (to avoid escape ambiguity);
interpolated strings cannot be used as call arguments without parentheses;
no formatting specifier syntax [11].

**Compound assignments** [7][12]. Operators `+=`, `-=`, `*=`, `/=`, `//=`,
`%=`, `^=`, `..=` — note `//=` was added alongside floor division and is
not in the original RFC [12] but is listed in the current syntax page
[7]. These are statements, not expressions: `a = (b += 1)` is illegal [12].
They evaluate the LHS only once: `data[i].cost += 1` evaluates `data[i]`
just once [12].

**`continue` statement** [7]. Context-sensitive keyword (not reserved),
preserving backward compatibility with any Lua 5.1 code that used
`continue` as an identifier.

**If-then-else expressions** [7]. Ternary-like form that returns a value:

```lua
local x = if cond then a else b
```

**Number literals** [7]. Hex (`0xABC`), binary (`0b01010101`), and
underscore separators for readability (`1_048_576`).

**String escapes** [7]. `\xAB` (hex byte), `\u{ABC}` (Unicode codepoint),
`\z` (skip whitespace).

**Floor division** [7]. `//` operator, `//=` compound, and `__idiv`
metamethod — "an ergonomic alternative to `math.floor`".

## Sandboxing model

Luau sandboxes scripts at multiple layers [5]:

1. **Read-only globals.** "All libraries (`string`, `math`, etc.) are
   marked as readonly"; the global table and string metatable are also
   marked readonly [5]. This protection "prevents all writes, including
   assignments, `rawset`, and `setmetatable`" [5].
2. **Per-script global isolation.** "In Roblox we solve this by creating
   a new global table for each script, that uses `__index` to point to
   the builtin global table" [5]. Each script can write its own globals
   without polluting others.
3. **Standard library restrictions.** The `io`, `os`, `package`, and
   `debug` libraries are removed or stripped [4]. "Some functions in
   `os`/`debug` are still present" [4] — e.g., `os.clock`, `os.time`,
   `debug.traceback`, `debug.info`.
4. **External bytecode rejection.** "External bytecode should be
   encrypted/signed to prevent MITM attacks"; the VM explicitly assumes
   bytecode comes from the official compiler [5]. Roblox has not
   supported loading arbitrary external bytecode since 2012.

One unresolved tension: `getfenv`/`setfenv` remain present in Luau
"because of backwards compatibility constraints" [4]. The sandbox docs
explicitly flag this: "Ideally, these should be disabled as well, but
unfortunately Roblox community relies on these for various reasons" [5].
Their presence disables several compiler optimizations including import
optimization [6].

## Performance characteristics

The Luau VM is hand-optimized for interpretation speed [6]:

| Claim | Quote | Source |
|---|---|---|
| Interpreter speed vs Lua 5.x | "noticeably faster than Lua 5.x (including Lua 5.4)" | [6] |
| Interpreter speed vs LuaJIT | "On some workloads it can match the performance of LuaJIT interpreter" | [6] |
| Interpreter core size | "~16 KB on x64" (leaves half instruction cache available) | [6] |
| `table.sort` | "~4x speedup on average" vs Lua 5.x | [6] |
| Paged sweeper GC | "2-3× faster" than linked list sweeping | [6] |
| Tagged value size | 16 bytes per value (64-bit double + 64-bit pointer; no NaN tagging) | [6] |
| Compiler throughput | "compiles 950K lines of Luau code in 1 second on a single core of a desktop Ryzen 5900X CPU" | [6] |

### Native code generation

Luau has a native codegen JIT, enabled per-script with `--!native` or
per-function with `@native` [9][16][17]. Introduced as Studio beta
2023-08-31 [17]; received 2024-2025 improvements including Android
support and vector operation lowering [15].

Native codegen is **server-side only** for live games [9]. The compiler
specializes hot paths using type annotations [6], but several conditions
trigger deoptimization back to interpreted bytecode [9]:

- Use of deprecated `getfenv()`/`setfenv()`
- Luau built-ins called with unexpected types (e.g., `math.asin` on a
  non-numeric argument)
- Mismatched type annotations on parameters (which "may trigger
  unnecessary checks, resulting in slower code execution")

Costs documented [9]: compilation time adds to server startup; each
natively compiled script consumes extra memory; there is "a limit on the
total allowed amount of natively compiled code in an experience". When
the cap is hit, remaining code falls back to interpreted.

Official recommendation: "scripts that perform a lot of computation
directly inside Luau" benefit most — "particularly with mathematical
operations on tables and buffer types" [9]. Roblox advises measurement
rather than blanket enablement: "It's recommended that you measure the
time a script or a function takes with and without native compilation"
[9].

### Key optimizations and what disables them

From the performance page [6]:

| Optimization | Disabled by |
|---|---|
| Import optimization (resolving global chains like `math.max` at load time) | `loadstring`, `getfenv`, `setfenv` |
| Inline caching on table/global field access | Metatables on the accessed fields |
| Closure caching | Mutable upvalues |
| Function inlining / loop unrolling | Requires `-O2` compile flag; `getfenv`/`setfenv` disables |

## Gaps and limitations

- **Exact behavioral differences between old and new type solver in
  strict mode** are not enumerated in the sources located; [19] announces
  general release but does not catalog rule changes.
- **`--!native` client availability** is marked server-only in [9]; it
  is possible this has changed in 2026 but no source located says so.
- **Exact `--!strict` introduction date** is not pinned to a specific
  Luau version; the 2020-11-19 type checking release post [13 context]
  is the earliest reference but is not confirmed as the origin.
- **Verified performance numbers for native codegen speedups** (e.g.,
  claimed 1.5-2.5× for compute-heavy code) were not located from a
  first-party source and are omitted here.
