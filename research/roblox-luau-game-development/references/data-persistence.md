# Data persistence

Roblox provides two first-party persistence systems: `DataStoreService`
(durable per-player save data) and `MemoryStoreService` (short-lived
cross-server shared state). Community middleware — ProfileService and its
successor ProfileStore — wraps DataStoreService to handle session locking
and common failure modes.

See [citations](../citations.md) for source details.

## DataStoreService limits

All numbers here come from the first-party error-codes-and-limits page
[62] except where explicitly marked as community-compiled.

### Hard limits

| Limit | Value | Source |
|---|---|---|
| Per-key payload size | **4,194,304 characters** (= 4 MiB) [62] | [62] |
| Data store name | 50 characters | [62] |
| Key name | 50 characters | [62] |
| Scope | 50 characters | [62] |
| Request queue length (before throttle) | 30 requests | [62] |

Note the payload is documented in **characters**, not bytes. With UTF-8
data this is effectively 4 MiB for ASCII-only content but less for
non-ASCII.

### Throughput (per key, per minute)

| Operation | Limit | Source |
|---|---|---|
| Read | 25 MB / minute / key | [62] |
| Write | 4 MB / minute / key | [62] |

Throughput accounting rounds each request up to the next kilobyte [62].
Exceeding these limits triggers `KeyThrottled` errors (vs
`DatastoreThrottled` for whole-datastore throttling).

### Request budgets

The engine-side DataStore rate limit uses the formula [63]:

```
rateLimit = baseLimit + (perPlayerLimit × numPlayers)
```

The official `GetRequestBudgetForRequestType` page [63] documents the
**formula structure** and shows parameter constraint ranges `[0, 60]`
and `[0, 40]` for various request types, but it does **not** enumerate
the default base/per-player values for each operation.

The values commonly cited in the community, from a well-known DevForum
post [71]:

| Operation | Per-server budget (requests/min) |
|---|---|
| `GetAsync` | 60 + numPlayers × 10 [71] |
| `SetAsync` / `UpdateAsync` / `RemoveAsync` / `SetIncrementAsync` | 60 + numPlayers × 10 [71] |
| `GetSortedAsync` (OrderedDataStore) | 5 + numPlayers × 2 [71] |

Experience-wide (game-wide) budgets from the same community source [71]:

| Operation category | Experience budget (requests/min) |
|---|---|
| Read | 250 + concurrentUsers × 40 [71] |
| Write | 250 + concurrentUsers × 20 [71] |
| List | 10 + concurrentUsers × 2 [71] |
| Remove | 100 + concurrentUsers × 40 [71] |

**Quality note**: Treat these as indicative. The official formula in [63]
exposes the rate-limit model but not the per-operation defaults; the
authoritative way to get the current budget is to actually call
`GetRequestBudgetForRequestType` at runtime. Roblox could change these
defaults without updating the community post.

### Experience-wide storage cap

The verbatim formula from [62]: **"Total latest version storage limit =
100 MB + 1 MB × lifetime user count"**. A lifetime user is any user who
has joined the experience at least once. The limit is currently enforced.

### Version history

From the `RemoveVersionAsync` page [64]:

- Versions **expire after 30 days** — except the current version, which
  never expires [64].
- `ListVersionsAsync` enumerates versions for a key with optional
  timestamp filtering [64].
- `RemoveVersionAsync` **permanently** deletes a version and creates no
  tombstone. This differs from `RemoveAsync`, which deletes the current
  version and writes a tombstone [64].

## MemoryStoreService

MemoryStoreService is the short-lived counterpart — cross-server shared
state that lives in memory, not durable storage.

### Sorted map / queue / hash map limits

From [65]:

| Limit | Value |
|---|---|
| Key size | 128 characters |
| Value size | 32 KB |
| Sort key size | 128 characters |
| Max item expiry | 3,888,000 seconds (= 45 days) |

### Throughput

Per-partition limits [66]: "each sorted map or queue is assigned a single
partition" and "in the very best case, a sorted map and a queue are
limited to 150,000 RPM". Hot keys can exceed a single partition's
throughput — use multiple sorted maps or shard your key space for
higher-throughput workloads.

### Request quota

Experience-wide quota from the staff announcement [67]: **"1000 + 100 ×
[num of concurrent users] request units per minute"** — note "request
units", not simple request counts. Different MemoryStore operations
consume different numbers of units.

## ProfileService → ProfileStore

The community-standard DataStore wrapper is ProfileService
([github.com/MadStudioRoblox/ProfileService][68]), maintained by loleris.
Its README now carries this explicit header [68]:

> **"FOR NEW PROJECTS - USE ProfileStore"**
>
> "This project is no longer supported - it's been stable for a long
> while and migration to ProfileStore is possible for most projects."

**License**: Apache 2.0 [68].

**What it does**: handles session locking (prevents two Roblox servers
from saving the same player's data simultaneously), auto-saving at
periodic intervals, and a reconcile pattern to merge new schema fields
into existing saved data. Without this abstraction, DataStoreService
is easy to misuse in ways that cause data loss.

### ProfileStore

**Repo**: [github.com/MadStudioRoblox/ProfileStore][69]
**Released**: 2024-10-11 [69]
**License**: Apache 2.0 [69]

ProfileStore is the successor to ProfileService [69]. It is "a Roblox
DataStore wrapper that streamlines auto-saving, session locking and a few
other features" [69] and is packaged as a single ModuleScript [69].
Backwards-compatible with ProfileService, so existing keys load
correctly in ProfileStore.

Key ProfileStore API from its docs [70]:

| Method | Purpose |
|---|---|
| `:StartSessionAsync(userID, ...)` | Opens a session for a user (acquires the session lock) |
| `Profile:Reconcile(template)` | "Fills in missing (nil) [string_key] = [value] pairs to the Profile.Data structure from the template argument" — schema migration support |
| `Profile:EndSession()` | Releases the session lock |

Session locking is the critical feature: it detects when another server
holds a lock on the same key and waits (or fails cleanly) rather than
overwriting.

### Decision: ProfileService vs ProfileStore vs raw DataStore

| Option | When to use |
|---|---|
| Raw DataStoreService | Prototyping; one-off non-critical state; cases where the player data is a trivial scalar |
| **ProfileStore** | **Default for new projects.** Any significant per-player save data |
| ProfileService | Existing codebases already using it; migration planning is straightforward but not mandatory |
| Suphi's DataStore | Alternative session-locking implementation; less widely adopted |

The reason to never use raw DataStoreService for significant save data is
the combination of [72][73]:

- **`BindToClose` is unreliable** — "BindToClose functions don't
  consistently work and often lead to data-loss" [72]. Servers can
  exceed the shutdown deadline before the callback completes.
- **Multi-key atomicity is impossible** — "currently impossible to
  safely update two data store keys simultaneously as a Roblox
  developer" [73]. This blocks safe implementations of trading systems
  and any cross-player currency transfer.

ProfileStore's session-lock + auto-save model mitigates (but does not
eliminate) the first; nothing mitigates the second short of designing
your data model around single-key updates.

## Gaps and limitations

- **Authoritative per-operation request budgets** are not enumerated
  on [63]; only the formula structure is. The indicative numbers in
  [71] are community-compiled and should be verified at runtime with
  `GetRequestBudgetForRequestType` for the target experience.
- **The exact `BindToClose` shutdown deadline** (how many seconds before
  Roblox forces termination) was not located in first-party docs.
- **When the experience-wide storage cap (`100 MB + 1 MB × lifetime
  users`) was rolled out or whether it's backstopped by any grace
  period** is not documented in the located sources.
- **Historical DataStore payload limit increase** — [18 history context
  from Discovery] notes a "DataStore Data Limit Increase" DevForum
  announcement that increased the per-key cap to 4 MB at some point,
  but the previous limit value and the date of the change were not
  captured in this pass.
- **ProfileStore `Reconcile` depth behavior** — whether it deep-merges
  nested tables or only fills top-level nil keys — is not extracted
  from [70].
- **MemoryStore hash map limits** (distinct from sorted map limits)
  were not captured from a first-party source.
