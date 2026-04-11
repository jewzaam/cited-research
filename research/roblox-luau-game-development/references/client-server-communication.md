# Client-server communication

Roblox enforces a strict client/server split. Most state mutations do not
replicate across the boundary automatically — code that needs to talk
across it uses a specific set of instance types (the "remote" family).
This file covers what each remote type does and when to pick each one.

See [citations](../citations.md) for source details.

## FilteringEnabled / Experience Filtering

Roblox's replication filter — historically known as FilteringEnabled, now
Experience Filtering — means the server does not automatically accept
changes made by clients [99][100]. Before it was enforced (2018-07-25 per
[100]), clients could modify the server's world directly. After enforcement,
that path is gone — cross-boundary state changes require an explicit remote
call.

"When a LocalScript modifies an object in the game, the change will be
made on the client but will not replicate to the server" [99].

The implication: any server-side state the client wants to affect
(currency, inventory, positions of authoritatively-owned parts) must go
through a remote call that the server validates and performs itself. This
is why the security model (see `security-exploits.md`) turns every remote
call into a trust boundary.

## The remote instance family

Four types, with different semantics [27][28][29][30][31]:

| Instance | Direction | Yields? | Reliable? | Ordered? | Networked? |
|---|---|---|---|---|---|
| `RemoteEvent` [27] | Both | No | Yes | Yes | Yes |
| `RemoteFunction` [28] | Both | Yes (caller yields for return value) | Yes | Yes | Yes |
| `UnreliableRemoteEvent` [29] | Both | No | **No** | **No** | Yes |
| `BindableEvent` / `BindableFunction` [31] | Same-side only | Varies | — | — | **No** |

"Networked?" distinguishes the first three (cross-boundary) from Bindables
(same VM only).

### `RemoteEvent`

One-way fire-and-forget across the client-server boundary. "Scripts firing
a RemoteEvent do not yield" [27].

API [27]:
- `FireServer(args)` — client → server
- `FireClient(player, args)` — server → a specific client
- `FireAllClients(args)` — server → every connected client
- `OnServerEvent` — listen on server; first argument is the firing `Player`
- `OnClientEvent` — listen on client

Delivery guarantees: reliable and ordered (per the in-depth community
networking writeup [33]) — Roblox sends RemoteEvents over a reliable,
in-order channel, equivalent to TCP-style semantics.

Rate limit: "approximately 500 requests per second, per client" [27], and
this limit is "shared among all remote events of the same type" [27]. A
client spamming many different `RemoteEvent` instances shares the same
budget. Server-side rate limiting is still required because exploiters can
saturate this budget intentionally (see `security-exploits.md`).

### `RemoteFunction`

Synchronous two-way call. "Scripts invoking a RemoteFunction yield until
they receive a response from the recipient" [28].

API [28]:
- `InvokeServer(args)` — client → server; client yields, server returns
- `InvokeClient(player, args)` — server → client; **server yields**
- `OnServerInvoke` — server callback, must return a value
- `OnClientInvoke` — client callback

Documented deadlock hazards when the server invokes a client [28]:

1. "If the client throws an error, the server throws the error too."
2. "If the client disconnects while it's being invoked, `InvokeClient()`
   throws an error."
3. **"If the client doesn't return a value, the server yields forever."**

Roblox's own recommendation, verbatim: "If the result is not needed, it is
recommended that you use a RemoteEvent instead, since its call is
asynchronous and doesn't need to wait for a response to continue execution"
[28]. In practice: **never use `InvokeClient` unless you have no other
option.** Most server→client calls should be `FireClient` instead.

### `UnreliableRemoteEvent`

Introduced in a staff announcement on 2023-11-29 [32]; its docs page is
the canonical reference [29]. "Asynchronous, unordered and unreliable,
one-way communication across the client-server boundary" [29].

Key differences from `RemoteEvent` [29][32]:

- **No ordering guarantee.** "There is no ordering guarantee between
  UnreliableRemoteEvents and anything else" [32].
- **Packets may be dropped.** Events "may be dropped to prioritize
  bandwidth or CPU usage in addition to any loss that occurs over the
  network" [32].
- **Payload size cap.** The current limit is **1000 bytes**; events with
  larger payloads are dropped silently (or with a log warning in Studio)
  [29]. The original launch limit was 900 bytes; Roblox raised it to
  1000 bytes on 2025-03-12 [32].

Recommended use cases, verbatim from the announcement: "particle effects,
sound bites, and events that impact visuals but are not crucial for game
state" [32]. The underlying argument for having an unreliable channel at
all is bandwidth efficiency: ordered-and-reliable delivery imposes
overhead that's wasteful for per-frame position updates or similar
high-frequency, disposable data [34].

### `BindableEvent` / `BindableFunction`

Same-VM signaling only. These do **not** cross the client-server boundary
[31]. Use them to connect code within the server (or within a single
client) that would otherwise be tightly coupled.

One edge case: "Tables passed as arguments to bindable events are copied
— they will not be exactly equivalent to those provided when firing the
event" [31] (and the same applies to `BindableFunction`). Don't assume
reference identity on passed tables.

## Decision framework: which remote do I use?

```
Does the call need a return value back to the caller?
├── Yes → RemoteFunction (but only client → server; avoid server → client)
└── No → Does every packet matter for correctness?
         ├── Yes → RemoteEvent
         └── No  → UnreliableRemoteEvent (must fit in 1000 bytes per call)
```

Same-side coordination (server→server or client→client in the same VM)
uses BindableEvent/BindableFunction instead [31], never a remote.

## Argument serialization

RemoteEvents and RemoteFunctions serialize arguments over the network, so
their argument types are constrained. The official docs describe
"any type of Roblox object" and standard Lua types as supported [27], but
flag limitations the developer must "carefully explore". In practice,
functions, cyclic tables, userdata with non-serializable members, and
metatables are not transmissible. Numeric precision is preserved for
Lua doubles, but do not assume `Instance` references remain identical
across the boundary — the server's view of an instance and the client's
view are distinct handles.

## Server-side validation patterns

Because clients can (and will) send arbitrary arguments via `FireServer`
/ `InvokeServer`, the server must validate every remote call. Canonical
guidance [90][93][94]:

1. **Type check every argument.** Don't trust argument types to match
   what your function signature expects. Community libraries for
   declarative type validation on `OnServerEvent` handlers exist [93].
2. **Range check every number.** Damage values, currency deltas, position
   deltas — all must be bounded to what the game logic permits.
3. **Instance ownership checks.** If a client sends an `Instance`
   reference, verify it is an instance the client actually controls.
4. **Rate limit per-player.** Per the community standard [97], a
   reasonable baseline is: 1-second cooldown on the client plus server-
   side kick at >5 fires/second. Exact thresholds depend on the expected
   call rate.
5. **Action-scope checks.** Ensure the requested action is even valid
   right now — e.g., "can this player open this shop?", "is this player
   currently alive?".

The underlying principle, verbatim from Roblox's security docs [90]:
"Assume every piece of data sent from the client has been manipulated,
fabricated, or sent with malicious intent."

## Gaps and limitations

- **Exact per-message byte limit on reliable RemoteEvent** is not
  documented on the primary reference page [27]; community sources cite
  a ~50 kbps bandwidth cap but could not trace it to an authoritative
  source.
- **The "500 requests/second" rate limit** on [27] is stated as
  "approximately"; Roblox has not published the exact enforcement point
  or whether it has changed over time.
- **Physics replication / `BasePart:SetNetworkOwner`** is referenced
  throughout DevForum discussions and [33] but was not fetched as a
  first-party source in this research pass; it is a meaningful gap for a
  complete networking reference.
- **UnreliableRemoteEvent transport layer** (whether it's actually UDP,
  some custom RTT-aware scheme, or something else) is not documented at
  the engineering-blog level in any source located.
