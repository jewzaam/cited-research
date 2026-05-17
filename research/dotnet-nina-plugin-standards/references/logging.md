# Logging — NINA.Core.Utility.Logger

Dimension covers: static Logger API, levels, file path, retention, output format, caller-context attribution, what *not* to log.

See [citations](../citations.md).

## Backend: Serilog, not log4net

NINA migrated to Serilog. `NINA.Core.csproj` [11] lists `Serilog.Sinks.Console 6.1.1` and `Serilog.Sinks.File 7.0.0` as direct PackageReferences. There is **no** log4net dependency. Older documentation and forum guidance that mention log4net is out of date.

`NINA.Core.Utility.Logger` [10] wraps Serilog statically. Plugins call into it as a static class — no instance creation, no DI injection.

## Static API surface

Per [10]:

```csharp
public static class Logger {
    public static void Error(Exception ex,
                             [CallerMemberName] string memberName = "",
                             [CallerFilePath] string sourceFilePath = "",
                             [CallerLineNumber] int sourceLineNumber = 0);

    public static void Error(Exception ex, string customMessage,
                             [CallerMemberName] ..., [CallerFilePath] ..., [CallerLineNumber] ...);

    public static void Error(string message,
                             [CallerMemberName] ..., [CallerFilePath] ..., [CallerLineNumber] ...);

    public static void Warning(string message,
                               [CallerMemberName] ..., [CallerFilePath] ..., [CallerLineNumber] ...);

    public static void Info(string message,
                            [CallerMemberName] ..., [CallerFilePath] ..., [CallerLineNumber] ...);

    public static void Debug(string message,
                             [CallerMemberName] ..., [CallerFilePath] ..., [CallerLineNumber] ...);

    public static void Trace(string message,
                             [CallerMemberName] ..., [CallerFilePath] ..., [CallerLineNumber] ...);

    public static void SetLogLevel(LogLevelEnum logLevel);
    public static bool IsEnabled(LogLevelEnum level);
    public static void CloseAndFlush();
}
```

Calls log-only; `Logger.Error` does not re-throw [10].

Every method has `[CallerMemberName] / [CallerFilePath] / [CallerLineNumber]` so callers do not pass method or file info explicitly — the compiler injects it. Example:

```csharp
try {
    DoWork();
} catch (Exception ex) {
    Logger.Error(ex);   // automatically logs the calling method + file + line
}
```

## Levels

Five levels, configurable globally in NINA's Options > Log Level UI [59]:

| Level | When to use in a plugin |
|---|---|
| `Trace` | High-frequency hot-path diagnostics. Off by default; only on for active debugging. |
| `Debug` | Step-by-step plugin internal state useful when reproducing a bug. |
| `Info` | Significant plugin lifecycle events (server started on port X, settings loaded, image processed). One or two lines per user-visible action. |
| `Warning` | Recoverable anomaly (configured server port was taken, falling back to nearest free). |
| `Error` | Operation failed; include the exception object. |

Per [10], `IsEnabled(LogLevelEnum)` lets callers cheaply guard expensive log message construction:

```csharp
if (Logger.IsEnabled(LogLevelEnum.Trace)) {
    Logger.Trace($"Allocated buffer: {ExpensiveDump()}");
}
```

## File location and rotation

Path constructed from `APPLICATIONTEMPPATH = Path.Combine(SpecialFolder.LocalApplicationData, "NINA")` [20], then:

```
%LOCALAPPDATA%\NINA\Logs\<timestamp>-<version>.<processId>-.log
```

Per [10]:
- Monthly rolling interval with file-size limits
- 90-day retention via `CoreUtil.DirectoryCleanup()` [20]
- Shared mode disabled, buffering disabled
- 1-second flush-to-disk interval
- File header records OS, architecture, processor count, physical memory

## Output template

Per [10]:

```
{Timestamp:yyyy-MM-ddTHH:mm:ss.ffff}|{LegacyLogLevel}|{Message:lj}{NewLine}{Exception}
```

So a log line looks like:

```
2026-05-17T19:08:42.1234|INFO|[MyPlugin.Initialize:42] Server starting on port 1888
```

Per [58], external NINA-log-report tools parse this format with `Timestamp|Level|...` regex.

## Plugin-name tagging

NINA does **not** automatically prefix plugin name into log lines. The `[CallerFilePath]` attribute provides the absolute source file path, which transitively identifies the plugin in most builds — but a stable plugin-name prefix is not part of the format.

Plugins that produce significant log volume (e.g. `tcpalmer/nina-scheduler`) maintain their **own separate log file** in `%localappdata%\NINA\<PluginName>\Logs\` with a short prefix like `TS-` per log line [59]. This is implemented by the plugin itself; it is not a NINA framework feature. For most plugins, writing through `NINA.Core.Utility.Logger` and letting `[CallerFilePath]` provide context is enough.

## Conventions for a NINA plugin

1. Static-class calls: `Logger.Info("Server started on port " + port);` — no instance or DI.
2. Errors carry the exception object: `Logger.Error(ex, "Failed to start server")` not just `Logger.Error("Failed: " + ex.Message)`. The Exception-typed overload [10] gives Serilog the stack trace.
3. No format-string interpolation problems — these are `string` params, not Serilog message templates, so `$"..."` interpolation is fine.
4. Guard `Trace` calls in tight loops with `IsEnabled` [10].
5. Do not log credentials, API keys, tokens, or PII — log files persist 90 days [10] and are commonly shared during support requests.
6. Do not introduce a separate logging framework (Serilog directly, NLog, log4net) — that creates duplicate sinks and confuses NINA's `IsEnabled`/level-control surface. Always go through `NINA.Core.Utility.Logger`.

## Gaps and limitations

- The exact monthly rolling pattern (`%LOCALAPPDATA%\NINA\Logs\<timestamp>-<version>.<processId>-.log` is one file per process start? or rolls to a new file each month?) is described from agent summary of [10]; the precise Serilog `WriteTo.File(...)` configuration was not quoted at character level.
- Whether `LogLevelEnum` values map 1:1 to Serilog's `LogEventLevel` (Verbose / Debug / Information / Warning / Error / Fatal) or use a NINA-specific mapping is the contract of `SetLogLevel` but the precise mapping was not extracted.
