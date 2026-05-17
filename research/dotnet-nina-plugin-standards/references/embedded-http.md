# Embedded HTTP Servers — EmbedIO and the http.sys ACL workaround

Dimension covers: why default `HttpListener` (http.sys) fails for non-elevated plugins, the EmbedIO `HttpListenerMode.EmbedIO` managed-socket workaround, server lifecycle, port selection, threading, firewall.

See [citations](../citations.md).

## The http.sys problem

`System.Net.HttpListener` is a thin managed wrapper over Windows' `http.sys` kernel-mode driver. http.sys maintains a global URL-namespace registry. Any non-elevated process that tries to bind a new namespace gets `System.Net.HttpListenerException (5): Access is denied` [37]. The only exemption is `http://localhost:PORT/` — wildcards (`http://+:PORT/`, `http://*:PORT/`) always require admin or a pre-registered `netsh http add urlacl url=http://+:PORT/ user=DOMAIN\user` entry [37], [38].

NINA runs as a normal user-space app, so plugins cannot rely on http.sys without imposing a `netsh` step on every user — which is unacceptable for a click-to-install plugin.

## EmbedIO's managed-socket alternative

EmbedIO's `WebServer` factory switches on the `HttpListenerMode` enum [34]:

- `HttpListenerMode.Microsoft` → wraps `System.Net.HttpListener` (http.sys path; inherits the ACL pain)
- Anything else (including `HttpListenerMode.EmbedIO`) → instantiates `EmbedIO.Net.HttpListener`, which uses `EndPointManager` / `EndPointListener` to open raw managed sockets [35]:

```csharp
new Socket(SocketType.Stream, ProtocolType.Tcp)
   .Bind(IPEndPoint)
   .Listen(500);
```

No http.sys interaction, no URL ACL, no netsh, no admin requirement for ports above 1023. HTTP request parsing and response generation happen in managed C# code (derived from Mono's reimplementation of `HttpListener`).

## Canonical NINA plugin pattern

Verified across ninaAPI's `API.cs` [32] and Touch-N-Stars' `TouchNStarsServer.cs` [33]. The minimal idiom:

```csharp
private CancellationTokenSource apiToken;
private Thread apiThread;

public void Start() {
    apiToken = new CancellationTokenSource();
    apiThread = new Thread(APITask) { Name = "API Thread", IsBackground = true };
    apiThread.Start();
}

private void APITask() {
    using var server = new WebServer(o => o
        .WithUrlPrefix($"http://*:{Port}")
        .WithMode(HttpListenerMode.EmbedIO));
    server.WithLocalSessionManager()
          .WithWebApi("/api", m => m.WithController<MyController>());
    server.RunAsync(apiToken.Token).Wait();
}

public void Stop() => apiToken.Cancel();
```

Why a dedicated `Thread` and `.Wait()` rather than `Task.Run`?
- The thread receives a meaningful name (`"API Thread"`) visible in debuggers.
- The blocking call sits on a thread you own, not a thread-pool thread that could be needed elsewhere.
- `Cancel()` propagates into the EmbedIO listener and unblocks `.Wait()` cleanly.

## NuGet package

| Aspect | Value | Source |
|---|---|---|
| Package ID | `EmbedIO` (NOT `Unosquare.EmbedIO`, which was v2.x) | [36] |
| Stable version | `3.5.2` (published 2022-10-31) | [36] |
| Target framework | `.NETStandard 2.0` | [36] |
| Compatible with NINA plugin TFM | `net8.0-windows` ✓ | [30] |
| Used by | ninaAPI, Touch-N-Stars, others | [30], [33] |

Note: `EmbedIO 3.5.2` is .NETStandard 2.0, so it is not a Windows-only dependency — it will load fine in NINA's process and does not pin to any specific Windows API surface.

## URL prefix patterns

| Prefix | Microsoft mode (http.sys) | EmbedIO mode (raw sockets) |
|---|---|---|
| `http://localhost:port` | Works without admin | Works |
| `http://127.0.0.1:port` | Works without admin (localhost exemption) | Works |
| `http://+:port` | Requires admin or netsh urlacl | Works (binds IPAddress.Any) |
| `http://*:port` | Requires admin or netsh urlacl | Works (binds IPAddress.Any + IPv6Any) but see caveat |

EmbedIO has an open issue (labeled wontfix) [63] noting that with `HttpListenerMode.EmbedIO`, the wildcard prefix `http://*:port` does not always correctly route to every IPv4 address — some configurations require explicit prefix enumeration. Despite this, the established NINA pattern uses `http://*:{port}` because it works in the common case and the workaround (enumerating explicit interface addresses) is rarely worth the complexity.

## Port selection

NINA plugins use a **fixed user-configurable port with automatic fallback to the nearest free port** via `CoreUtil.GetNearestAvailablePort(int port)` [20], [32]. Ephemeral (port 0) binding is not the pattern, partly because EmbedIO explicitly rejects `port=0` in its `CheckUri` validation.

| Plugin | Default port |
|---|---|
| ninaAPI (Advanced API) | 1888 |
| Touch-N-Stars web UI | 5000 (separate process, not the in-NINA API) |

Both plugins expose `Port` and `CachedPort` properties on their main class so the user can configure a port and see what was actually bound (when the configured port was taken).

## Lifecycle integration

Server start happens in the plugin's `Initialize()` (or constructor for simple cases — ninaAPI [31] starts in constructor conditionally on `APIEnabled`). Server stop happens in `Teardown()`:

```csharp
public override Task Teardown() {
    Server?.Stop();
    API.StopWatchers();
    // remove temp files, dispose comm channels
    return base.Teardown();
}
```

`Server?.Stop()` translates to `apiToken.Cancel()` plus `apiThread.Join()` (or just letting the `IsBackground` thread die at process exit).

## Firewall

A managed TCP socket bound to `0.0.0.0` triggers Windows Defender Firewall's "allow this app to communicate on the network" prompt on first external connection. Bound to localhost only (`http://localhost:port` or `http://127.0.0.1:port`), no firewall prompt. No NINA plugin we inspected automates `netsh advfirewall` rule creation; the user is expected to grant the firewall prompt manually.

## Why not Kestrel / TcpListener?

- **Kestrel** (ASP.NET Core) — managed and no http.sys dependency, but very heavy. Brings transitive deps (`Microsoft.Extensions.*`) that conflict with whatever versions NINA pins, especially since NINA's `AssemblyLoadContext` [7] does not unify them.
- **Raw TcpListener** — viable but requires hand-rolling HTTP parsing. Not used in any inspected plugin.
- **HttpListenerMode.Microsoft** — same ACL pain as raw http.sys.
- **HttpListenerMode.EmbedIO** — single ~1 MB DLL, .NETStandard 2.0, no conflicts, no admin, full HTTP/WebSocket/static-files/WebApi out of the box. This is the de-facto NINA plugin choice.

## Gaps and limitations

- The EmbedIO `http://*:port` wildcard issue (issue #459 in their tracker) is labeled wontfix; we did not measure how often it bites in practice for NINA plugins.
- `GetNearestAvailablePort` source behaviour (linear probe? OS port enumeration?) not directly fetched.
- HTTPS / TLS termination inside the plugin (`Options.Certificate` parameter to EmbedIO's HttpListener constructor [34]) — not investigated; no NINA plugin found uses HTTPS in-process.
