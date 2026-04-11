# Performance best practices

This file covers the performance primitives Roblox exposes (scheduling,
scripting hooks, profiling tools) and the documented anti-patterns to
avoid.

See [citations](../citations.md) for source details.

## Frame budget

At 60 FPS the frame budget is **16.67 milliseconds**, quoted verbatim from
the official design-for-performance docs [38]. Any single piece of
per-frame work that pushes into that budget pushes framerate down
proportionally. The documented worked example: "If a piece of code takes
100 ms to execute and you run it every frame, your experience can only
run at 10 FPS" [38].

The official first-line recommendation: **"Whenever possible, write
event-driven code rather than per-frame calculations"** [38]. Continuous
polling is the most common anti-pattern.

When per-frame work can't be avoided, the official time-slicing pattern
[38]: "you can perform 5 ms of work per frame, use `task.wait()`, and
have the completed calculation every 20 frames while still maintaining 60
FPS". Break large work into chunks and yield between chunks.

## RunService events and frame ordering

`RunService` exposes a set of events that fire at specific points in the
engine's per-frame loop [35]. The current official ordering:

```
PreRender → PreAnimation → PreSimulation → (physics simulation) → PostSimulation → Heartbeat
```

Event details from [35]:

| Event | When | Side | Status |
|---|---|---|---|
| `PreRender` | "Fires every frame, prior to the frame being rendered" | Client only | Current |
| `RenderStepped` | Same timing as `PreRender` | Client only | **Superseded by `PreRender`** [35] |
| `PreAnimation` | "Fires every frame, prior to the physics simulation but after rendering" | Both | Current |
| `PreSimulation` | "Fires every frame, prior to the physics simulation" | Both | Current |
| `Stepped` | Same timing as `PreSimulation` | Both | **Superseded by `PreSimulation`** [35] |
| `PostSimulation` | "Fires every frame, after the physics simulation has completed" | Both | Current |
| `Heartbeat` | Same timing as `PostSimulation` | Both | Current |

The "superseded" labels come directly from the reference page [35]. Both
pairs (`RenderStepped`/`PreRender`, `Stepped`/`PreSimulation`) fire at
identical times; the new names are recommended for new work.

**How to pick an event** [35]:
- Code that **writes** physics state (setting Velocity, CFrame on
  unanchored parts) should use `PreSimulation`.
- Code that **reads** physics state (reading Position, checking
  collisions) should use `PostSimulation`.
- Client-only visual code that must see the latest frame state should
  use `PreRender`.
- Code that doesn't care about physics ordering can use `Heartbeat`.

## The `task` library

Roblox's task scheduler lives in the `task` library [36]. It replaces the
legacy globals `spawn`, `wait`, `delay`, which are "less optimized and
configurable" per the original launch announcement [40].

| Function | Verbatim description [36] | Practical meaning |
|---|---|---|
| `task.spawn(f, ...)` | "Calls/resumes a function/coroutine immediately through the engine's scheduler" | Start a coroutine now, without waiting |
| `task.defer(f, ...)` | "Calls/resumes a function/coroutine at the end of the current resumption cycle" | Queue for after current tasks finish |
| `task.wait(n)` | "Yields the current thread without throttling" | Sleep `n` seconds, resume on next `Heartbeat` after |
| `task.delay(n, f, ...)` | "Schedules a function/coroutine to be called/resumed on the next Heartbeat after the given duration" | Fire-and-forget after `n` seconds |
| `task.synchronize()` | "Causes the following code to be run in serial" | Switch back to serial context (for parallel Luau) |
| `task.desynchronize()` | "Causes the following code to be run in parallel" | Switch to parallel context (for parallel Luau) |
| `task.cancel(thread)` | "Cancels a thread and closes it" | Kill a coroutine you started |

Legacy note: the `task.wait` page describes "the deprecated global wait()"
[36]. Any new code should use `task.wait` over `wait`. Legacy `wait`
throttled to roughly 30 fps; `task.wait` does not throttle [36].

**`task.spawn` vs `task.defer`**: spawn runs now, defer queues for end of
the current resumption cycle. Defer is safer when you want to avoid
re-entering your own code mid-execution. Spawn is safer when you need
guaranteed immediate execution.

## Parallel Luau

Parallel Luau is Roblox's multi-threaded execution model [37]. The
primitives are `Actor` instances and the `task.synchronize`/`task.desynchronize`
pair.

**Actor model** [37]:
- Actors are "units of execution isolation that distribute the load across
  multiple cores running simultaneously".
- Critically: "Scripts that are part of the same actor always execute
  sequentially with respect to each other". Within one Actor, parallelism
  does not happen — you need multiple Actors to get multi-core execution.

**Synchronization** [37]:
- `task.desynchronize()` switches the current coroutine into parallel
  (worker-thread) context.
- `task.synchronize()` switches back to serial (main-thread) context.
- Alternatively, `RBXScriptSignal:ConnectParallel()` schedules a callback
  to run in parallel on trigger.

**Hard constraint** [37]: "You can't use `require()` in a desynchronized
parallel phase. Require scripts you want to use first in a serial
context." All module loading must happen in serial code before crossing
into parallel.

**Cross-actor data** [37]:
- `SharedTable` is "a table-like data structure accessible from scripts
  running under multiple actors"; enables atomic updates without copying.
- The Actor Messaging API (introduced in V2 on 2023-05-31 per [41]):
  `Actor:SendMessage(topic, ...)`, `Actor:BindToMessage(topic, cb)`
  (serial), `Actor:BindToMessageParallel(topic, cb)` (parallel).

Parallel Luau V1 was released 2022 [42]; V2 (with Actor Messaging and
SharedTable) followed on 2023-05-31 [41].

## Native code generation

Covered in detail in [luau-language.md](luau-language.md), but the
performance-relevant summary: `--!native` or `@native` enables a JIT
compilation to machine code [9][17]. Server-side only [9]. Best for
"scripts that perform a lot of computation directly inside Luau" [9] —
particularly math-heavy code on tables and buffers. Deoptimization
triggers include getfenv/setfenv use, mistyped parameters, and calling
built-ins with unexpected types [9]. Always measure rather than
blanket-enable [9].

## Instance creation: the parent-last rule

The canonical Roblox performance PSA, dated 2016-10-31 [39], still applies:
**set all properties before assigning `Parent`**.

The mechanism [39]: "Once an object is attached to game, a lot of internal
Roblox systems start listening to property changes... queueing changes
for replication, updating physics contact state". An unparented instance
can have its properties set cheaply; a parented instance triggers a chain
of listener updates on each property write.

**Do not** use `Instance.new("Part", workspace)` with the parent argument
— the parent is set first, then subsequent property assignments trigger
replication and physics churn [39].

Correct sequence [39]:

```lua
local p = Instance.new("Part")
p.Size = Vector3.new(4, 1, 2)
p.Material = Enum.Material.Metal
p.CFrame = target
p.Parent = workspace  -- last!
```

Then connect signals after parenting. The author of the original post
floated adding a Script Analysis warning for the parent-argument form,
which the Script Editor now surfaces as an undefined-behavior-style hint
in some versions [89].

## Instance pooling

For hot-path allocation — bullets, particles, spawned enemies — pooling
beats per-use `Instance.new`/`:Destroy()` [44][45]. The community standard
threshold: "up to 100 [instances] being fine to create without pooling"
[45]; beyond that, pool.

Roblox's own core scripts include an `ObjectPool.lua` implementation [46]
that can serve as a reference — a plain Luau module that tracks free and
in-use instances and rents/returns them.

## Profiling

Two built-in tools [43]:

- **MicroProfiler** — the per-frame render time visualization. Opened
  with **Ctrl+Alt+F6** [43]. Vertical orange bars represent each frame;
  bar height is frame duration. Click a bar to drill into its label
  tree.
- **`debug.profilebegin(label)` / `debug.profileend()`** [43] — create
  labeled spans that show up in the MicroProfiler timeline. Wrap the
  code you want to measure:

  ```lua
  debug.profilebegin("EnemyUpdate")
  updateAllEnemies()
  debug.profileend()
  ```

  Yielding inside a span ends the label early.

The Script Profiler (complementary to MicroProfiler) provides per-function
CPU timing and is available in Studio; it's the tool of choice for
identifying which functions consume the most time overall, as opposed to
which frames are slow.

## Documented anti-patterns

Summary list from [38]:

- **Continuous per-frame polling** when an event could drive the work.
- **Caching the result of a method each time you call it**, rather than
  storing and reusing: "Don't call the same method every time you need a
  value. Call the method once, store the value, and then overwrite it
  later as necessary" [38].
- **Forgetting to `Disconnect()` signal connections.** "Use the
  `RBXScriptConnection:Disconnect()` method to stop functions from being
  called unnecessarily the next time an event fires" [38].
- **Storing everything in ReplicatedStorage**, which forces the client to
  load it all [38].

Plus from elsewhere:

- **Instance.new parent argument** — property writes on a parented
  instance are expensive [39].
- **Legacy `spawn`/`wait`/`delay`** — throttled and less optimized than
  `task` library equivalents [36][40].
- **Frequent parallel ↔ serial transitions** via
  `task.synchronize`/`task.desynchronize` within a hot loop — the sync
  overhead eats the parallelism benefit (DevForum discussion referenced
  but not fetched in this pass).

## Gaps and limitations

- **Exact performance numbers for native codegen speedup** (e.g., "1.5×–
  2.5× for compute-heavy code") were not located from a first-party
  source. Roblox's guidance is "measure your own code".
- **Exact bandwidth overhead of `debug.profilebegin`/`profileend`** in
  hot paths is not documented.
- **`--!native` client availability as of 2026** was not verified; [9]
  says server-side only.
- **Whether `PreAnimation` fires between rendering and PreSimulation on
  all platforms** (the current ordering per [35]) — ordering bugs have
  been reported historically.
