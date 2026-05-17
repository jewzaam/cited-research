# C# NINA 3.x Plugin Coding Standards

> Citation-backed conventions for building, packaging, and publishing a NINA 3.x plugin in C# on .NET 8. All claims trace to a numbered source in [citations](citations.md).

## Scope and assumptions

- Target application: NINA (Nighttime Imaging 'N' Astronomy) version **3.x** on Windows.
- Plugin SDK source: `https://github.com/isbeorn/nina` (develop branch tracked); SDK distributed via NuGet package `NINA.Plugin` (current stable `3.2.0.9001` [39]; develop is `3.3.0.x-nightly` targeting `net10.0-windows` [11]).
- Plugin runtime: .NET 8 Windows (WPF), x64.
- This document audits *idiomatic conventions and pitfalls*, not the full plugin SDK API surface. It pairs with the in-repo [plugin template](https://github.com/isbeorn/nina.plugin.template) [1] which is the canonical starting point.

## Quick-reference cheat sheet

| Aspect | Standard |
|---|---|
| TFM | `net8.0-windows` (NINA 3.2 stable) [26][30] |
| Platform | x64 [42] |
| UseWPF | `true` when XAML is present [26] |
| NuGet | `NINA.Plugin <matching-version>` only; rely on transitive deps [1][26] |
| `MinimumApplicationVersion` value | Matches `NINA.Plugin` NuGet version [1][28] |
| Install root | `%LOCALAPPDATA%\NINA\Plugins\<api-version>\<title>\` [26][41] |
| `<api-version>` segment | **3-part**, currently `3.0.0` for all NINA 3.x [41] |
| Plugin class | `[Export(typeof(IPluginManifest))] : PluginBase` [2][8] |
| Constructor | `[ImportingConstructor]` once per class [2][53] |
| Persisted options | `new PluginOptionsAccessor(profileService, Guid.Parse(this.Identifier))` [2][16] |
| Options UI key | `<AssemblyTitle>_Options` (auto-resolved via `IPluginManifest.Name`) [4][23][24] |
| ResourceDictionary code-behind | `[Export(typeof(ResourceDictionary))] partial class : ResourceDictionary` [5] |
| RelayCommand | `CommunityToolkit.Mvvm.Input.RelayCommand` (NINA's own is `[Obsolete]`) [22] |
| Logger backend | Serilog (NOT log4net); static `NINA.Core.Utility.Logger` [10][11] |
| Embedded HTTP | `EmbedIO 3.5.2` with `HttpListenerMode.EmbedIO` (managed sockets, no http.sys ACL pain) [32][33][34][37] |
| Cleanup | Override `Task Teardown()` and unsubscribe / unregister; `base.Teardown()` at end [2][9] |
| Publishing | PR to `bitbucket.org/Isbeorn/nina.plugin.manifests`; `manifest.json` per schema [25] |
| Hash | SHA-256 over installer file; recomputed if DLL changes [25] |

---

## 1. Project layout and csproj

Standard csproj for a NINA 3.2 plugin (synthesized from [26][30], matches all surveyed real plugins):

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net8.0-windows</TargetFramework>
    <Platforms>x64</Platforms>
    <PlatformTarget>x64</PlatformTarget>
    <OutputType>Library</OutputType>
    <UseWPF>true</UseWPF>
    <CopyLocalLockFileAssemblies>true</CopyLocalLockFileAssemblies>
    <LangVersion>latest</LangVersion>
  </PropertyGroup>

  <ItemGroup>
    <!-- NINA.Plugin version: match the NINA target.
         3.2.0.9001 for NINA 3.2 stable [30]; 3.1.2.9001 for plugins still on 3.1 [26] -->
    <PackageReference Include="NINA.Plugin" Version="3.2.0.9001">
      <PrivateAssets>all</PrivateAssets>
    </PackageReference>
    <!-- third-party PackageReferences here -->
  </ItemGroup>

  <Target Name="DeployToNinaPlugins" AfterTargets="Build">
    <PropertyGroup>
      <PluginDir>$(LocalAppData)\NINA\Plugins\3.0.0\$(AssemblyTitle)\</PluginDir>
    </PropertyGroup>
    <MakeDir Directories="$(PluginDir)" Condition="!Exists('$(PluginDir)')" />
    <Copy SourceFiles="$(TargetPath)" DestinationFolder="$(PluginDir)" />
    <!-- copy third-party DLLs the plugin brings — NOT NINA's own -->
  </Target>
</Project>
```

Rationale:
- `net8.0-windows` matches the running NINA 3.2 host [26][30]. For NINA 3.3+ targets, bump to whatever `NINA.Plugin` ships — currently `net10.0-windows` on develop [11].
- The README explicitly recommends "remove all PackageReferences from the csproj file. Dotnet core handles them much better and far less direct dependencies have to be specified" [1] — reference `NINA.Plugin` only and rely on transitive resolution.
- `PrivateAssets=all` prevents NINA's own DLLs being published into the plugin output (they are already shipped with NINA — see §2 below).
- The install path's `<api-version>` subfolder is **3-segment** `3.0.0`, NOT the 4-segment `3.0.0.9001` package version [41]. All surveyed NINA 3.x plugins use `\NINA\Plugins\3.0.0\` regardless of the running NINA build [26][30].
- The plugin template's checked-in csproj [6] still targets .NET Framework 4.8 — treat it as historical; the README confirms the VS wizard produces a .NET 8 project [1].
- The VS post-build editor mangles `%localappdata%` tokens to `%25localappdata%25`; either author the `<Target>` in XML directly (as above) or edit them back after the wizard touches them [1].

## 2. Do NOT bundle these assemblies

NINA's `AssemblyLoadContext` isolates plugins [7], but the plugin still resolves shared types through its own context first. Bundling an assembly NINA already ships causes either:
- A second copy loaded into the plugin context, breaking cross-context type identity, OR
- A version mismatch surfacing as `TypeLoadException` / `MissingMethodException`.

NINA-shipped assemblies (per [11], [39], [40]) — do not copy any of these into the plugin folder:

```
NINA.Astrometry, NINA.Core, NINA.Equipment, NINA.Image,
NINA.PlateSolving, NINA.Profile, NINA.Sequencer, NINA.WPF.Base,
NINA.CustomControlLibrary,
CommunityToolkit.Mvvm (currently 8.4.0 on develop; floor >=8.2.2 per NINA.Core), Newtonsoft.Json,
Serilog, Serilog.Sinks.File, Serilog.Sinks.Console,
System.ComponentModel.Composition, OxyPlot.Core,
SQLite (SourceGear.sqlite3 / System.Data.SQLite),
gRPC, Google.Protobuf, Accord.Math
```

**Important historical correction**: NINA does **not** ship log4net. The Logger uses Serilog [10][11]. Older docs and forum posts mentioning log4net for NINA logging are out of date.

For each third-party package the plugin pulls, add to the csproj's `DeployToNinaPlugins` target an explicit `<Copy>` of that DLL — the InfluxDB exporter [26] is the canonical example, copying its seven InfluxDB-related DLLs and nothing else.

## 3. AssemblyInfo.cs — the manifest source of truth

`PluginBase` [8] reads the following attributes from your `Properties/AssemblyInfo.cs` to populate `IPluginManifest`:

| Status | Attribute | Maps to |
|---|---|---|
| **Required** | `[Guid("...")]` | `Identifier` |
| **Required** | `[AssemblyTitle("...")]` | `Name` (also drives DataTemplate key, install folder, manifest Name) |
| **Required** | `[AssemblyVersion("M.m.p.b")]` | (CLR identity) |
| **Required** | `[AssemblyFileVersion("M.m.p.b")]` | `Version` |
| **Required** | `[AssemblyMetadata("ShortDescription", "...")]` (effectively, per [1]) | `Descriptions.ShortDescription` (via `AssemblyDescription` per [8] — see gap below) |
| Recommended | `[AssemblyCompany("...")]` | `Author` |
| Recommended | `[AssemblyMetadata("License", "MPL-2.0")]` | `License` |
| Recommended | `[AssemblyMetadata("LicenseURL", "...")]` | `LicenseURL` |
| Recommended | `[AssemblyMetadata("Repository", "...")]` | `Repository` |
| Recommended | `[AssemblyMetadata("MinimumApplicationVersion", "3.2.0.9001")]` | `MinimumApplicationVersion` |
| Optional | `[AssemblyMetadata("Homepage", "...")]` | `Homepage` |
| Optional | `[AssemblyMetadata("ChangelogURL", "...")]` | `ChangelogURL` |
| Optional | `[AssemblyMetadata("Tags", "a, b, c")]` | `Tags` (string[], split on comma) |
| Optional | `[AssemblyMetadata("LongDescription", "...")]` | `Descriptions.LongDescription` |
| Optional | `[AssemblyMetadata("FeaturedImageURL", "...")]` | `Descriptions.FeaturedImageURL` |
| Optional | `[AssemblyMetadata("ScreenshotURL", "...")]` | `Descriptions.ScreenshotURL` |
| Optional | `[AssemblyMetadata("AltScreenshotURL", "...")]` | `Descriptions.AltScreenshotURL` |

Sources: [1], [8]. README [1] calls `ShortDescription` Required and lists everything else under Recommended or Optional. `PluginBase` [8] reads `ShortDescription` from `AssemblyDescriptionAttribute` (the standard CLR attribute) — there is a minor naming inconsistency between the README's `[AssemblyMetadata(ShortDescription)]` framing and PluginBase's actual `AssemblyDescription`-attribute read. The `nina-influxdb-exporter` AssemblyInfo [28] uses `[AssemblyTitle]` to carry the short description ("Exports metrics to an InfluxDB 2.x or InfluxDB Cloud 2 instance") — so the field also serves dual purpose in some plugins. **Recommended**: set both `[AssemblyDescription]` and a substantive `[AssemblyTitle]`; keep them consistent.

Version-format constraints:
- `AssemblyVersion` segments are 16-bit unsigned (0–65535) per CLR.
- `MinimumApplicationVersion` metadata value uses the same 4-segment string format and is parsed into an `IPluginVersion` object [9].
- Defaults when missing: `Version` → `"1.0.0.0"`, `MinimumApplicationVersion` → `"1.11.0.0"` per `PluginBase` [8]. Both defaults are accepted by `PluginLoader` but will fail manifest-repo validation [25].

What happens when malformed:
- Missing `[Guid]`: `PluginOptionsAccessor.GetAssemblyGuid` returns `null` [16]; plugin cannot persist options. `PluginLoader` synthesizes a fallback manifest [7] but identity tracking is broken.
- Malformed version (e.g., `"1.0"` not `"1.0.0.0"`): not directly verified in source. Treat as a hard error and always use 4 segments.

The template's checked-in `AssemblyInfo.cs` [3] contains zero `[AssemblyMetadata]` keys — plugin authors add them. The `nina-influxdb-exporter` AssemblyInfo [28] is a realistic complete example.

## 4. The main plugin class — MEF wiring

Pattern verified across [2], [27], [31], [56]:

```csharp
[Export(typeof(IPluginManifest))]
public class MyPlugin : PluginBase, INotifyPropertyChanged {
    private readonly IProfileService profileService;
    private readonly IImageSaveMediator imageSaveMediator;
    private readonly IPluginOptionsAccessor pluginSettings;

    [ImportingConstructor]
    public MyPlugin(IProfileService profileService,
                    IImageSaveMediator imageSaveMediator) {
        this.profileService = profileService;
        this.imageSaveMediator = imageSaveMediator;
        this.pluginSettings = new PluginOptionsAccessor(
            profileService, Guid.Parse(this.Identifier));

        profileService.ProfileChanged += OnProfileChanged;
        imageSaveMediator.BeforeImageSaved += OnBeforeImageSaved;
    }

    public override async Task Teardown() {
        profileService.ProfileChanged -= OnProfileChanged;
        imageSaveMediator.BeforeImageSaved -= OnBeforeImageSaved;
        await base.Teardown();
    }

    private void OnProfileChanged(object sender, EventArgs e) {
        RaisePropertyChanged(nameof(SomeProfileSpecificProperty));
    }

    private async Task OnBeforeImageSaved(object sender, BeforeImageSavedEventArgs e) {
        // mutate FITS headers here
    }

    public event PropertyChangedEventHandler PropertyChanged;
    protected void RaisePropertyChanged([CallerMemberName] string name = null)
        => PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(name));
}
```

Rules:
- **One** `[Export(typeof(IPluginManifest))]` per plugin assembly [1].
- **One** `[ImportingConstructor]` per class [53]. The default MEF `CreationPolicy` is `Shared` (singleton per container) [53] and the plugin manager relies on this — do not declare `[PartCreationPolicy(NonShared)]` on the manifest class.
- Inject only what you need. The injectable interfaces list is in [1] and [mef-manifest](references/mef-manifest.md); it includes every `I*Mediator`, factories, and several VM types.
- **Do not** access `ISequenceMediator` in the constructor body — per [1] it "Must be initialized first before you can use it which is after all plugins are loaded." Defer to `Initialize()`.
- `PluginBase` provides virtual async `Initialize()` and `Teardown()` returning `Task.CompletedTask` [8]. Override one or both as needed. `PluginBase` does NOT implement `IDisposable` [8] — `Teardown()` is the only cleanup hook.

## 5. Mediators and device consumers

Two interaction patterns:

### 5.1 Event subscription

For discrete actions. Per [12], [13], [14]:

| Mediator | Notable events |
|---|---|
| `IImagingMediator` | `ImagePrepared(ImagePreparedEventArgs)` — **NOT `ImageSaved`** [12] |
| `IImageSaveMediator` | `BeforeImageSaved(Func<obj, BeforeImageSavedEventArgs, Task>)`, `BeforeFinalizeImageSaved(Func<obj, BeforeFinalizeImageSavedEventArgs, Task>)`, `ImageSaved(EventHandler<ImageSavedEventArgs>)` [13] |
| `ITelescopeMediator` | `BeforeMeridianFlip`, `AfterMeridianFlip`, `Parked`, `Homed`, `Unparked`, `Slewed` [14] |
| Other device mediators | Similar per-action event pattern [57] |

**The `Func<..., Task>` events on `IImageSaveMediator` are async**: the publisher awaits the returned task. Implement these as `async Task` methods. The fire-and-forget `EventHandler<ImageSavedEventArgs>` (`ImageSaved`) is the case where `async void` is the only delegate-compatible option — always wrap such handler bodies in `try / catch { Logger.Error(ex); }` because unhandled exceptions can crash NINA via the UI `SynchronizationContext` [48].

Per [13], on `BeforeFinalizeImageSaved`: "Altering Image Meta Data will NOT be reflected in the written file." Use `BeforeImageSaved` (not `BeforeFinalize…`) to mutate FITS headers.

### 5.2 Device-consumer registration

For streaming device-state polls. Per [15]:

```csharp
public interface IDeviceMediator<THandler, TConsumer, TInfo>
    where THandler : IDeviceVM<TInfo>
    where TConsumer : IDeviceConsumer<TInfo>
{
    void RegisterConsumer(TConsumer consumer);
    void RemoveConsumer(TConsumer consumer);  // Remove, not Unregister
    void Broadcast(TInfo deviceInfo);
}
```

Implementation pattern:

```csharp
public class MyPlugin : PluginBase, ITelescopeConsumer { // ITelescopeConsumer : IDeviceConsumer<TelescopeInfo>
    [ImportingConstructor]
    public MyPlugin(ITelescopeMediator telescopeMediator) {
        this.telescopeMediator = telescopeMediator;
        telescopeMediator.RegisterConsumer(this);
    }
    public void UpdateDeviceInfo(TelescopeInfo info) { /* called on hardware poll thread */ }
    public override Task Teardown() {
        telescopeMediator.RemoveConsumer(this);
        return base.Teardown();
    }
}
```

### 5.3 Thread semantics

Mediator events and `UpdateDeviceInfo` callbacks fire on background threads in the general case. Plugins that touch UI-bound properties must marshal:

```csharp
await Application.Current.Dispatcher.InvokeAsync(() => SomeProperty = newValue);
```

Per [48]: use `Dispatcher.InvokeAsync` (TAP-integrated), not `Dispatcher.BeginInvoke` (legacy, no async integration).

### 5.4 Cleanup discipline

Every `+= handler` requires a paired `-= handler` in `Teardown()`. Every `RegisterConsumer(this)` requires a paired `RemoveConsumer(this)`. Anonymous lambdas cannot be unsubscribed (no equal-delegate-instance match) — always use a named method or store the delegate in a field. See [mediators-and-devices](references/mediators-and-devices.md).

## 6. Options UI (WPF)

### 6.1 The DataTemplate key

NINA renders the plugin's options panel by resolving `Application.Current.Resources[plugin.Name + "_Options"]` [23]. `plugin.Name` is `IPluginManifest.Name` (auto-populated from `[AssemblyTitle]` via `PluginBase` [8]). Constant: `DataTemplatePostfix.Options = "_Options"` [24].

So with `[assembly: AssemblyTitle("MyPlugin")]`, the DataTemplate must be keyed `x:Key="MyPlugin_Options"`.

### 6.2 The wiring

`Options.xaml`:

```xml
<ResourceDictionary
    x:Class="MyPlugin.Options"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
    <DataTemplate x:Key="MyPlugin_Options">
        <StackPanel DataContext="{Binding}" Orientation="Vertical">
            <!-- bindings against the plugin class properties -->
        </StackPanel>
    </DataTemplate>
</ResourceDictionary>
```

`Options.xaml.cs`:

```csharp
using System.ComponentModel.Composition;
using System.Windows;

namespace MyPlugin {
    [Export(typeof(ResourceDictionary))]
    partial class Options : ResourceDictionary {
        public Options() { InitializeComponent(); }
    }
}
```

Source: [4], [5]. The `[Export(typeof(ResourceDictionary))]` attribute is what makes `PluginLoader` merge the dictionary into `Application.Current.Resources.MergedDictionaries` [7]. Forgetting it is the #1 cause of an empty options pane.

DataContext inside the template is the `IPluginManifest` instance itself (your `PluginBase` subclass) [23].

### 6.3 Other DataTemplate postfixes

Per [1], [24]:

| Postfix | Key form | Purpose |
|---|---|---|
| `_Options` | `<IPluginManifest.Name>_Options` | Plugin global options panel |
| `_Mini` | `<FullyQualifiedTypeName>_Mini` | Compact sequencer item view |
| `_Dockable` | `<FullyQualifiedTypeName>_Dockable` | Dockable imaging-tab panel |
| `_<DeviceType>Settings` | `<FullyQualifiedTypeName>_CameraSettings`, etc. | Custom device-driver settings |

### 6.4 Themed styles

NINA's themed brushes and styles are merged into `Application.Current.Resources` at app startup [7]. Reference via `{StaticResource ...}` without merging anything in the plugin dictionary. Confirmed style and brush keys: see [wpf-options-ui](references/wpf-options-ui.md) for the full list.

There is NO `BorderedTextBlock` style. Wrap a `TextBlock` (with the `StandardTextBlock` style) in a `Border`.

### 6.5 RelayCommand

`NINA.Core.Utility.RelayCommand` is `[Obsolete]` [22]. Use `CommunityToolkit.Mvvm.Input.RelayCommand` and `AsyncRelayCommand` directly — `CommunityToolkit.Mvvm 8.4.0` ships with NINA [11], so:

```xml
<PackageReference Include="CommunityToolkit.Mvvm" Version="8.4.0">
  <ExcludeAssets>runtime</ExcludeAssets>
</PackageReference>
```

`ExcludeAssets=runtime` keeps compile-time references but suppresses publishing the DLL (which NINA already ships).

## 7. Persisted options — IPluginOptionsAccessor

Construct in the plugin constructor:

```csharp
this.pluginSettings = new PluginOptionsAccessor(profileService, Guid.Parse(this.Identifier));
```

Source: [2], [16]. The GUID **must** match `[assembly: Guid(...)]`. Defensive form (handles missing/duplicate attribute):

```csharp
var guid = PluginOptionsAccessor.GetAssemblyGuid(typeof(MyOptions))
    ?? throw new Exception("GUID was not found in assembly metadata");
this.pluginSettings = new PluginOptionsAccessor(profileService, guid);
```

Source: [29].

### 7.1 Typed accessors

Per [16], typed pairs `GetValueT(string name, T defaultValue)` / `SetValueT(string name, T value)` for:

`Boolean, Byte, SByte, Char, Decimal, Double, Single, Int32, UInt32, Int64, UInt64, Int16, UInt16, String, DateTime, Guid, Color, Enum<T>`

Naming follows CLS type names: `GetValueSingle`, not `GetValueFloat`. Color is stored as ARGB int [16]. Enums are stored as strings via `Enum.GetName` and parsed via `Enum.TryParse<T>` — renaming an enum member silently breaks deserialization for existing profiles.

### 7.2 Profile scope

All settings are **per-profile**. Backed by `profileService.ActiveProfile.PluginSettings`, an in-memory `Dictionary<Guid, IDictionary<string, object>>` namespaced by plugin GUID [16]. Two plugins with the same setting name do not collide (different GUIDs).

Profile files: `%LOCALAPPDATA%\NINA\Profiles\<profile-guid>.profile`, serialized via `DataContractSerializer` [18]. `Profile.Save()` uses a journal → backup → final three-file write for crash safety.

### 7.3 Profile-change handling

Subscribe to `IProfileService.ProfileChanged` [19] and re-raise property-changed notifications when the active profile switches; otherwise the UI shows stale values from the previous profile:

```csharp
profileService.ProfileChanged += (s, e) => RaisePropertyChanged(nameof(MySetting));
```

Unsubscribe in `Teardown()`.

### 7.4 Convention: use `nameof()` for keys

Per [29]:

```csharp
public bool EnableX {
    get => pluginSettings.GetValueBoolean(nameof(EnableX), defaultValue: true);
    set { pluginSettings.SetValueBoolean(nameof(EnableX), value); RaisePropertyChanged(); }
}
```

No magic strings, refactor-safe.

## 8. Embedded HTTP servers

Plugins that expose HTTP endpoints (REST APIs, Prometheus metrics, local UI servers) **must use EmbedIO with `HttpListenerMode.EmbedIO`** to avoid the http.sys URL-ACL admin requirement [37].

Canonical pattern (synthesized from [32], [33]):

```csharp
private CancellationTokenSource serverToken;
private Thread serverThread;

public void StartServer() {
    serverToken = new CancellationTokenSource();
    serverThread = new Thread(() => {
        using var server = new WebServer(o => o
            .WithUrlPrefix($"http://*:{Port}")
            .WithMode(HttpListenerMode.EmbedIO));
        server.WithWebApi("/api", m => m.WithController<MyController>());
        server.RunAsync(serverToken.Token).Wait();
    }) { Name = "MyPlugin HTTP", IsBackground = true };
    serverThread.Start();
}

public void StopServer() => serverToken?.Cancel();
```

Why this pattern:
- `HttpListenerMode.EmbedIO` bypasses http.sys by binding raw managed TCP sockets [35]. No admin, no `netsh urlacl`, no firewall warning at startup (only at first external connection).
- Dedicated named `Thread` gives debugger visibility; `IsBackground = true` lets it die at process exit.
- `serverToken.Cancel()` is registered on the listener and unblocks `.Wait()` cleanly.

NuGet: `EmbedIO 3.5.2` [36], targets `.NETStandard 2.0`, no version conflicts with NINA.

Port selection: fixed user-configurable port with fallback via `CoreUtil.GetNearestAvailablePort(port)` [20], [32]. Expose `Port` (configured) and `CachedPort` (actually bound) properties so the user can see which port was used when the configured one was taken.

Do not use `HttpListenerMode.Microsoft` — that path requires elevation or `netsh http add urlacl` to bind any prefix other than `http://localhost:port/` [37].

## 9. Logging

**Backend is Serilog**, not log4net [10][11]. Use `NINA.Core.Utility.Logger` as a static class.

```csharp
Logger.Info("Server started on port " + port);
Logger.Warning("Configured port unavailable; bound " + cachedPort);
try { ... } catch (Exception ex) { Logger.Error(ex, "Server failed to start"); }

if (Logger.IsEnabled(LogLevelEnum.Trace)) {
    Logger.Trace($"State dump: {ExpensiveDump()}");
}
```

Per [10]:
- Methods: `Error`, `Warning`, `Info`, `Debug`, `Trace`, `SetLogLevel(LogLevelEnum)`, `IsEnabled(LogLevelEnum)`, `CloseAndFlush()`.
- `Error` overloads: `(Exception)`, `(Exception, string)`, `(string)`. The Exception-taking overload preserves stack trace.
- Every method has `[CallerMemberName]`, `[CallerFilePath]`, `[CallerLineNumber]` optional params — no need to pass them.
- Log file: `%LOCALAPPDATA%\NINA\Logs\<timestamp>-<version>.<processId>-.log`, monthly rolling, 90-day retention [10][20], 1-second flush.
- Output line format: `{Timestamp:yyyy-MM-ddTHH:mm:ss.ffff}|{LegacyLogLevel}|{Message:lj}{NewLine}{Exception}` [10].

Level discipline:
- `Trace` — high-frequency hot-path; off by default; gate with `IsEnabled`.
- `Debug` — internal state useful during bug reproduction.
- `Info` — lifecycle events (server started, settings loaded).
- `Warning` — recoverable anomaly.
- `Error` — operation failed; always include the exception.

NINA does NOT auto-prefix the plugin name. Heavy-logging plugins maintain their own separate log file in `%LOCALAPPDATA%\NINA\<PluginName>\Logs\` (e.g., `tcpalmer/nina-scheduler` uses `TS-` prefix [59]) — pattern, not framework.

Do not log credentials, API keys, tokens, or PII. Log files persist 90 days and are shared during support.

## 10. Async, threading, .NET 8 style

### 10.1 Async patterns

- Use `async Task` for ordinary methods.
- `async void` only for top-level event handlers subscribed to `EventHandler` / `EventHandler<T>` events. **Always** wrap the body in `try/catch` logging via `Logger.Error(ex)` — unhandled exceptions from `async void` propagate to the UI `SynchronizationContext` and can crash NINA [48].
- Handlers subscribed to `Func<..., Task>` events ([13]) must return `Task` — those are awaited by the publisher.
- `await Application.Current.Dispatcher.InvokeAsync(() => …)` for UI marshalling. Never `Dispatcher.BeginInvoke` in modern code [48].
- `CancellationToken` as the last parameter (or second-to-last when `IProgress<T>` follows [12]). Propagate through every call, including `Task.Run(action, ct)` [54].

### 10.2 .NET 8 language features

| Feature | Use in NINA plugin |
|---|---|
| `<Nullable>enable</Nullable>` | Project-wide on; `#nullable disable` per-file in XAML code-behind / `IValueConverter` files where WPF noise is excessive [49] |
| File-scoped namespaces (C# 10) | Use — `namespace Foo.Bar;` [50] |
| Primary constructors (C# 12) | Works in principle; combine with `[method: ImportingConstructor]` [51]; not observed in any real NINA plugin yet — prefer explicit constructor to match ecosystem precedent |
| `record` types | Immutable DTOs only. NOT for mutable VM properties (no `INotifyPropertyChanged`) |
| `record struct` | Hot-path value objects |
| `using` declarations | Prefer for single-disposable scopes [55] |
| `ObservableObject` + `[ObservableProperty]` (CommunityToolkit) | Encouraged for plugin VMs. Class must be `partial` [43] |
| Top-level statements | N/A (plugin is a class library) |

### 10.3 MVVM base classes

```
INotifyPropertyChanged (System)
  └─ CommunityToolkit.Mvvm.ComponentModel.ObservableObject [44]
       └─ NINA.Core.Utility.BaseINPC (abstract) [21]
```

`PluginBase` [8] does NOT extend `BaseINPC` — the template implements `INotifyPropertyChanged` manually [2]. Three viable options:

1. Implement INPC manually with `[CallerMemberName]` (template style).
2. Use a separate ViewModel inheriting `BaseINPC` (NINA helpers like `RaiseAllPropertiesChanged`).
3. Use `ObservableObject` directly with `[ObservableProperty]` source generator.

## 11. Testing

The plugin ecosystem has no published testing convention — surveyed plugins do not contain test projects. NINA core itself uses **NUnit + FluentAssertions** [42]. Recommendation for new plugin tests:

- Test framework: xUnit (broader tooling) or NUnit (matches NINA core)
- Mocking: Moq (interfaces in NINA are pure — `IImagingMediator`, `ITelescopeMediator`, `IPluginOptionsAccessor` all mock cleanly)
- Assertions: FluentAssertions
- WPF/STA helper: `Xunit.StaFact` (`[WpfFact]`, `[StaFact]`) [46] when tests touch `Dispatcher`

Test project TFM options [47]:

1. `net8.0-windows10.0.22621.0` (matches plugin; can reference plugin assembly directly; pinned to avoid NUnit `net8.0-windows`+`win-x64` issue).
2. `net8.0` (pure .NET; CANNOT reference `net8.0-windows` plugin directly — extract pure logic into a separate `net8.0` library both plugin and tests reference).

`[ObservableProperty]`-generated properties are not `virtual` [43] — Moq cannot proxy them on concrete classes. To test, instantiate the real VM, subscribe to `PropertyChanged`, assert. INPC events fire synchronously without a Dispatcher [43].

For `internal` plugin types reachable in tests:

```xml
<ItemGroup>
  <InternalsVisibleTo Include="MyPlugin.Tests" />
</ItemGroup>
```

Unsigned plugin assemblies (the NINA norm) need only the name [45].

## 12. Publishing

PR target: `bitbucket.org/Isbeorn/nina.plugin.manifests` (mirrored on GitHub) [25].

### 12.1 Schema (selected required fields)

```json
{
  "Name": "MyPlugin",
  "Identifier": "78fc6455-c1ba-4dc5-a8d0-9f48aecd733d",
  "Author": "Your Name",
  "License": "MPL-2.0",
  "LicenseURL": "https://www.mozilla.org/en-US/MPL/2.0/",
  "Repository": "https://github.com/you/myplugin",
  "Version": { "Major": 1, "Minor": 0, "Patch": 0, "Build": 0 },
  "MinimumApplicationVersion": { "Major": 3, "Minor": 2, "Patch": 0, "Build": 9001 },
  "Installer": {
    "URL": "https://github.com/you/myplugin/releases/download/v1.0.0/MyPlugin.zip",
    "Type": "ARCHIVE",
    "Checksum": "abc123...",
    "ChecksumType": "SHA256"
  },
  "Descriptions": {
    "ShortDescription": "..."
  }
}
```

Full schema in [publishing](references/publishing.md). Optional fields: `ChangelogURL`, `Tags`, `Homepage`, `LongDescription`, `FeaturedImageURL`, `ScreenshotURL`, `AltScreenshotURL`, `Channel ("Beta")`.

### 12.2 GUID matching

The same GUID lives in four places, and they must agree exactly:

1. `[assembly: Guid("...")]` in AssemblyInfo
2. `IPluginManifest.Identifier` (auto-derived from #1 via PluginBase)
3. `manifest.json` `"Identifier"`
4. The GUID passed to `new PluginOptionsAccessor(...)`

The GUID must never change across versions [25] — it is the install/uninstall identity.

### 12.3 SHA-256 over installer

The checksum is computed over the file referenced by `Installer.URL`:
- `Installer.Type = "DLL"` → hash of the .dll
- `Installer.Type = "ARCHIVE"` → hash of the .zip

Recompiling after manifest creation invalidates the checksum [25]. In CI, the build → hash → manifest must be one transactional workflow.

### 12.4 MinimumApplicationVersion

Match the `NINA.Plugin` NuGet version compiled against [1]. Compiled against `NINA.Plugin 3.2.0.9001` → manifest declares `MinimumApplicationVersion = {3,2,0,9001}`.

### 12.5 Folder structure

```
manifests\<first-letter><plugin-name>\<nina-version>\<plugin-version>\manifest.json
```

Example: `manifests\PPixInsightTools\3.x\1.0.0\manifest.json`. `<nina-version>` can be omitted if a single version is supported.

### 12.6 Channels

`"Channel": "Beta"` → published to beta channel. Users opt-in via NINA Options > General > Plugin Repositories with URL `https://nighttime-imaging.eu/wp-json/nina/v1/beta`. Omit `Channel` for stable. No Nightly or Alpha channels in the manifest layer.

### 12.7 Validation before PR

```bash
winget install nodejs
npm install
node gather.js
```

Manifest must validate cleanly against `manifest.schema.json` before PR.

### 12.8 Recommended automation

Use the official GitHub Actions template (`./tools/github-action.yml` in the manifest repo [25]) wired to fire on version-tag push. It builds → hashes → generates manifest → opens the PR in one workflow, eliminating the recompile-invalidates-hash trap [25].

---

## "Do not" / pitfall cross-cuts

1. **Do not** bundle NINA-shipped assemblies in the plugin output folder ([§2](#2-do-not-bundle-these-assemblies)).
2. **Do not** use the obsolete `NINA.Core.Utility.RelayCommand` — use `CommunityToolkit.Mvvm.Input.RelayCommand` ([§6.5](#65-relaycommand)).
3. **Do not** subscribe with anonymous lambdas (cannot unsubscribe) — named methods only ([§5.4](#54-cleanup-discipline)).
4. **Do not** leave `async void` handler bodies unwrapped — wrap in `try/catch` ([§10.1](#101-async-patterns)).
5. **Do not** look for `ImageSaved` on `IImagingMediator` — it lives on `IImageSaveMediator` ([§5.1](#51-event-subscription)).
6. **Do not** mutate FITS headers in `BeforeFinalizeImageSaved` — they won't be reflected ([§5.1](#51-event-subscription)).
7. **Do not** access `ISequenceMediator` in `[ImportingConstructor]` body — defer to `Initialize()` ([§4](#4-the-main-plugin-class-mef-wiring)).
8. **Do not** use `HttpListenerMode.Microsoft` — requires admin / netsh ([§8](#8-embedded-http-servers)).
9. **Do not** introduce a parallel logging framework — go through `NINA.Core.Utility.Logger` ([§9](#9-logging)).
10. **Do not** change the plugin GUID across versions — breaks install identity ([§12.2](#122-guid-matching)).
11. **Do not** recompile after manifest generation — invalidates SHA-256 ([§12.3](#123-sha-256-over-installer)).
12. **Do not** use `Dispatcher.BeginInvoke` — use `Dispatcher.InvokeAsync` ([§10.1](#101-async-patterns)).
13. **Do not** rename enum members exposed via `GetValueEnum<T>` — silently breaks deserialization ([§7.1](#71-typed-accessors)).
14. **Do not** trust the install-folder `<api-version>` to be 4-segment — it is 3-segment `3.0.0` ([§1](#1-project-layout-and-csproj)).

---

## Appendix A — Canonical AssemblyInfo template

```csharp
using System.Reflection;
using System.Runtime.InteropServices;

[assembly: AssemblyTitle("MyPlugin")]
[assembly: AssemblyDescription("Short one-line description (shows in plugin manager)")]
[assembly: AssemblyCompany("Your Name")]
[assembly: AssemblyProduct("MyPlugin")]
[assembly: AssemblyCopyright("Copyright © 2026")]
[assembly: ComVisible(false)]
[assembly: Guid("00000000-0000-0000-0000-000000000000")]   // do not change after release
[assembly: AssemblyVersion("1.0.0.0")]
[assembly: AssemblyFileVersion("1.0.0.0")]

[assembly: AssemblyMetadata("License", "MPL-2.0")]
[assembly: AssemblyMetadata("LicenseURL", "https://www.mozilla.org/en-US/MPL/2.0/")]
[assembly: AssemblyMetadata("Repository", "https://github.com/you/myplugin")]
[assembly: AssemblyMetadata("Homepage", "https://github.com/you/myplugin")]
[assembly: AssemblyMetadata("ChangelogURL", "https://github.com/you/myplugin/releases")]
[assembly: AssemblyMetadata("MinimumApplicationVersion", "3.2.0.9001")]
[assembly: AssemblyMetadata("Tags", "imaging, automation")]
[assembly: AssemblyMetadata("LongDescription", "Longer multi-paragraph description.")]
[assembly: AssemblyMetadata("FeaturedImageURL", "https://example.com/featured.png")]
[assembly: AssemblyMetadata("ScreenshotURL", "https://example.com/screenshot.png")]
```

Sources: [1] structure, [28] live example.

## Appendix B — Source coverage table

| Dimension | Confidence | Primary sources |
|---|---|---|
| Build & install | High | [1][6][7][26][30][39][41] |
| Assembly metadata | High | [1][2][3][7][8][9][28] |
| MEF & manifest | High | [1][2][7][8][9][27][31][53] |
| Mediators & devices | Medium-High | [12][13][14][15][27][56][57] (per-thread-of-event semantics inferred) |
| WPF options UI | High | [1][2][4][5][7][22][23][24][43][44] |
| Persisted options | High | [2][16][17][18][19][20][29] |
| Embedded HTTP | High | [30][32][33][34][35][36][37] |
| Logging | High | [10][11][20][58][59] |
| Async & .NET 8 style | Medium-High | [11][43][48][49][50][51][52][54][55] |
| Testing | Medium (extrapolated — no real plugin test projects found) | [42][43][45][46][47] |
| Publishing | High | [25][28] |

---

*Standards revision date: 2026-05-17. This document supersedes any prior NINA plugin guidance and is the basis for upcoming audit of `nina-prometheus-exporter`.*
