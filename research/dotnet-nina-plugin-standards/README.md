# NINA 3.x Plugin Coding Standards — Research

Citation-backed coding-standards research for **C# NINA 3.x plugins** targeting the public plugin SDK (`NINA.Plugin` NuGet, source at `https://github.com/isbeorn/nina`). Output deliverable is [`dotnet-nina-plugin.md`](dotnet-nina-plugin.md), intended to be copied into `~/source/standards/` and used to audit `~/source/nina-prometheus-exporter`.

Every claim in the deliverable traces to a numbered source in [`citations.md`](citations.md). Two isolated review agents (citation audit + consistency review) audit the output post-write.

## Quick answer

A correct NINA 3.x plugin (synthesized across all dimensions; sources cited in the deliverable):

```
[net8.0-windows class library, x64, UseWPF=true]
NuGet: NINA.Plugin <matching-version> with PrivateAssets=all
Install path: %LOCALAPPDATA%\NINA\Plugins\3.0.0\<AssemblyTitle>\     ← 3-segment, not 4
[Export(typeof(IPluginManifest))] class : PluginBase, INotifyPropertyChanged
[ImportingConstructor] takes only the mediators you need
AssemblyInfo: [Guid], [AssemblyTitle], [AssemblyVersion], [AssemblyFileVersion],
              [AssemblyDescription], [AssemblyCompany],
              [AssemblyMetadata("License","MPL-2.0")],
              [AssemblyMetadata("MinimumApplicationVersion","3.2.0.9001")],
              + Repository / LicenseURL / Homepage / Tags / images
Options UI: Options.xaml = <DataTemplate x:Key="<AssemblyTitle>_Options">
            Options.xaml.cs = [Export(typeof(ResourceDictionary))] partial class
            DataContext is the plugin instance itself
Persisted settings: new PluginOptionsAccessor(profileService, Guid.Parse(this.Identifier))
RelayCommand: CommunityToolkit.Mvvm.Input.RelayCommand (NINA's own is [Obsolete])
HTTP server: EmbedIO 3.5.2 with HttpListenerMode.EmbedIO (NO http.sys, NO admin)
Logging: NINA.Core.Utility.Logger (static, Serilog backend, NOT log4net)
Teardown(): unsubscribe every += and call RemoveConsumer for every RegisterConsumer
Publishing: PR manifest.json to bitbucket.org/Isbeorn/nina.plugin.manifests
            GUID must match across [Guid] + IPluginManifest.Identifier + manifest.Identifier
            SHA-256 over installer; recompiling invalidates
```

## Highest-leverage findings

These are the items that surprised the research most often and are most likely to bite an auditor:

1. **NINA uses Serilog, NOT log4net.** Older docs and forum posts mention log4net. The Logger backend was switched and is now Serilog (verified in `NINA.Core.csproj` and `Logger.cs`).
2. **The `<api-version>` subfolder is 3-segment** (`3.0.0`), not 4-segment (`3.0.0.9001`). All NINA 3.x plugins install under `\NINA\Plugins\3.0.0\` regardless of the running NINA build.
3. **`ImageSaved` lives on `IImageSaveMediator`, not `IImagingMediator`.** Easy to confuse; subscribing to the wrong interface silently does nothing.
4. **`PluginBase` does NOT extend `BaseINPC` and does NOT implement `IDisposable`.** The template implements `INotifyPropertyChanged` manually; cleanup goes through the `Teardown()` override only.
5. **`NINA.Core.Utility.RelayCommand` is `[Obsolete]`.** Use `CommunityToolkit.Mvvm.Input.RelayCommand` (NINA ships `CommunityToolkit.Mvvm 8.4.0`).
6. **The plugin template's checked-in csproj still targets `.NET Framework 4.8`** but the README confirms the VS wizard generates a `net8.0-windows` project anyway. Treat the checked-in csproj as historical.
7. **Default `MinimumApplicationVersion` when missing is `1.11.0.0`** per `PluginBase` — accepted by `PluginLoader` but rejected by manifest-repo validation.
8. **GUID must match in 4 places** (`[Guid]`, `IPluginManifest.Identifier`, `manifest.json Identifier`, the `PluginOptionsAccessor` constructor argument) and must never change across versions.
9. **`HttpListenerMode.EmbedIO` is the only viable embedded-HTTP path for non-elevated NINA.** `HttpListenerMode.Microsoft` requires admin or `netsh http add urlacl`.
10. **`BeforeFinalizeImageSaved` cannot mutate FITS headers** — use `BeforeImageSaved` for that. The source's own comment says so.

## Decision framework for auditing a plugin

1. **Open the .csproj.** Confirm `net8.0-windows`, `x64`, `UseWPF=true`, `NINA.Plugin` reference only (no direct NINA.* sub-package refs unless the plugin has a specific reason). Confirm the post-build deploys to `\NINA\Plugins\3.0.0\<Title>\` and does NOT copy NINA-shipped DLLs.
2. **Open AssemblyInfo.cs.** Verify the required + recommended `[AssemblyMetadata(...)]` keys are present and `MinimumApplicationVersion` matches the `NINA.Plugin` NuGet version. Confirm `[Guid]` is set.
3. **Open the main plugin class.** Verify `[Export(typeof(IPluginManifest))]`, single `[ImportingConstructor]`, and that every `+=` in the constructor has a matching `-=` in `Teardown()`.
4. **If the plugin has options UI:** verify `Options.xaml.cs` has `[Export(typeof(ResourceDictionary))]` and that the DataTemplate key matches `<AssemblyTitle>_Options`.
5. **If the plugin persists settings:** verify it constructs `PluginOptionsAccessor` with the assembly GUID and subscribes to `IProfileService.ProfileChanged` (and unsubscribes in Teardown).
6. **If the plugin runs an HTTP server:** verify EmbedIO with `HttpListenerMode.EmbedIO`, on a dedicated named thread, with a CancellationToken stop pattern.
7. **Check logging:** all log calls go through `NINA.Core.Utility.Logger` (no `log4net`, no `Serilog` direct, no `Console.WriteLine`).
8. **Check publishing artifacts:** verify a `manifest.json` exists matching the published schema, with `Installer.ChecksumType = "SHA256"` and `Identifier` matching `[Guid]`.

## File layout

```
research/dotnet-nina-plugin-standards/
├── README.md                                ← this file
├── dotnet-nina-plugin.md                    ← full standards deliverable (copy to ~/source/standards/)
├── citations.md                             ← all sources, numbered
├── references/
│   ├── build-and-install.md
│   ├── assembly-metadata.md
│   ├── mef-manifest.md
│   ├── mediators-and-devices.md
│   ├── wpf-options-ui.md
│   ├── persisted-options.md
│   ├── embedded-http.md
│   ├── logging.md
│   ├── async-threading-and-csharp-style.md
│   ├── testing.md
│   └── publishing.md
└── audit/
    ├── citation-audit.md                    ← citation-vs-source verification
    └── consistency-review.md                ← cross-file numerical/logical checks
```

## Methodology notes

- 11 Discovery sub-agents (Sonnet, parallel) followed by main-thread WebFetch of source files.
- Counter-perspective handling: **Skip** (per user — technical/factual topic without meaningful counter-views).
- Local read-only repos under `~/source/nina*` informed hypotheses but the deliverable cites only GitHub-hosted equivalents (per user instruction).
- Two isolated review agents (Sonnet, no shared conversation context) audit the produced files post-write.

## Limitations

- The full `manifest.schema.json` was not fetched directly — schema field list is from the manifest repo README. Plugins generating manifests should run `node gather.js` for authoritative validation.
- Per-event thread origin for each NINA mediator is not source-verified; the deliverable applies a conservative "treat as background; marshal via Dispatcher.InvokeAsync" rule.
- No real NINA plugin test project was found in any surveyed repository; the testing dimension is the weakest, recommending xUnit/NUnit + Moq + FluentAssertions by extrapolation from NINA core's CONTRIBUTING.md.
- Primary-constructor + MEF + WPF combination is documented as legal in theory; not observed in any real NINA plugin.
