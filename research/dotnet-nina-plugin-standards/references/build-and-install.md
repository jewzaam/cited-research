# Build and Install — csproj, post-build, install path

Dimension covers: TargetFramework, platform, UseWPF, NuGet `NINA.Plugin` reference shape, post-build install script, install path under `%LOCALAPPDATA%\NINA\Plugins\<api-version>\<title>\`, dependency conflict avoidance.

See [citations](../citations.md).

## Target framework

| Aspect | Value | Source |
|---|---|---|
| TFM for NINA 3.2 stable plugins | `net8.0-windows` | [26], [30] |
| TFM for NINA 3.3 nightly (develop) | `net10.0-windows` | [11] |
| OutputType | `Library` | [26], [30] |
| UseWPF | `true` (when plugin defines XAML) | [26] |
| Platform | x64 (NINA itself built `-p:PlatformTarget=x64`) | [42] |
| Plugin template repo csproj | `.NET Framework 4.8` (stale; wizard generates net8.0 anyway) | [1], [6] |

Per [1]: "The wizard may prompt you to choose .NET Framework 4.8 instead of .NET 8. You can safely ignore this suggestion and select .NET Framework 4.8. Despite this, the project will still be created as a .NET 8 project, as this is a current limitation of the extension."

## NINA.Plugin NuGet reference

NINA 3.2 stable plugins reference `NINA.Plugin 3.2.0.9001` [30] (or `3.1.2.9001` for plugins still on the 3.1 branch [26]). The plugin template README explicitly states: "It is recommended to remove all PackageReferences from the csproj file. Dotnet core handles them much better and far less direct dependencies have to be specified" [1] — meaning a plugin should pull only `NINA.Plugin` (plus genuinely third-party packages) and rely on transitive resolution for the NINA sub-packages.

In practice this recommendation is not uniformly followed: `ninaAPI.csproj` [30] references every NINA sub-package directly alongside `NINA.Plugin`. The InfluxDB exporter csproj [26] follows the recommendation and only references `NINA.Plugin` + the third-party `InfluxDB.Client`. The exporter pattern is the better convention because it tracks NINA's evolving package boundaries.

The "9001" build segment in `NINA.Plugin 3.2.0.9001` designates stable. Nightly NuGet packages use `1xxx` build numbers (e.g., `3.2.0.1067-nightly`), beta `2xxx`, RC `3xxx` [39].

## Install path

`%LOCALAPPDATA%\NINA\Plugins\<api-version>\<plugin-title>\` [26], [30], [41].

The `<api-version>` segment is **three-part** (`Major.Minor.Revision`, e.g., `3.0.0`), **not** four-part. Per the official NINA 3.0.0.9001 release notes [41]: "plugin folder in `%localappdata%\NINA\Plugins` now contains a subfolder with the Major.Minor.Revision version of the application." Both `nina-influxdb-exporter` and `ninaAPI` post-build into `%localappdata%\NINA\Plugins\3.0.0\` [26], [30] — even though the running NINA build is e.g. 3.2.0.9001, the `<api-version>` folder remains pinned to `3.0.0` (the API revision floor for NINA 3.x plugins).

`<plugin-title>` matches `AssemblyTitle` and the manifest `Name` [25].

## Post-build install pattern

InfluxDB exporter [26] post-build target:
1. Creates `%localappdata%\NINA\Plugins\3.0.0\` if absent
2. Copies compiled assembly
3. Copies the seven third-party DLLs the plugin brings (InfluxDB client libs, JSON, reactive extensions, CSV, time, REST client)
4. Does **not** copy NINA's own assemblies — those are shipped with NINA

ninaAPI [30] uses `xcopy` with preservation flags to copy assembly to `%localappdata%\NINA\Plugins\3.0.0\Advanced API\`.

The plugin template README [1] notes that the VS post-build editor mangles `%localappdata%` tokens into `%25localappdata%25` and that they must be edited back to the original form by hand.

## Which DLLs not to copy

Anything reachable transitively through `NINA.Plugin` is shipped with NINA and must **not** be redistributed in the plugin bin directory, since the running NINA process loads them from its own folder, not the plugin folder [7]. The exclusion list inferred from [11], [39], [40]:

| Assembly | Reason | Source |
|---|---|---|
| NINA.Astrometry | NINA.Plugin transitive | [39] |
| NINA.Core | NINA.Plugin transitive | [39] |
| NINA.Equipment | NINA.Plugin transitive | [39] |
| NINA.Image | NINA.Plugin transitive | [39] |
| NINA.PlateSolving | NINA.Plugin transitive | [39] |
| NINA.Profile | NINA.Plugin transitive | [39] |
| NINA.Sequencer | NINA.Plugin transitive | [39] |
| NINA.WPF.Base | NINA.Plugin transitive | [39] |
| NINA.CustomControlLibrary | NINA.WPF.Base transitive | [39] |
| CommunityToolkit.Mvvm | NINA.Core transitive (>= 8.2.2, currently 8.4.0) | [11], [40] |
| Newtonsoft.Json | NINA.Core transitive | [11] |
| Serilog.Sinks.Console / Serilog.Sinks.File | NINA.Core transitive | [11] |
| System.ComponentModel.Composition | NINA.Core transitive | [11] |
| OxyPlot.Core | NINA.Core transitive | [11] |
| log4net | **not present** in NINA.Core — NINA migrated to Serilog | [10], [11] |

The recommended pattern: reference `NINA.Plugin` with `<PrivateAssets>all</PrivateAssets>` or `<ExcludeAssets>runtime</ExcludeAssets>` on the PackageReference to keep compile-time references but suppress runtime publishing. The template csproj [6] is too stale to demonstrate this; the InfluxDB exporter [26] works around it via the explicit post-build copy list.

Duplicate-assembly conflict is a real failure mode: if a plugin ships its own newer `Newtonsoft.Json` alongside NINA's, the plugin's `AssemblyLoadContext` [7] will load its bundled copy while other NINA code holds the older one. Symptoms: `TypeLoadException` or `MissingMethodException`. Mitigation: never bundle the NINA-shipped list above; if a newer version is required, escalate to the NINA project before relying on it.

## Gaps and limitations

- The exact MSBuild syntax of the canonical post-build target was not directly captured at character level — the agent summaries describe behaviour but did not quote the XML. Authors should crib from `daleghent/nina-influxdb-exporter/InfluxDB Exporter.csproj` [26] directly.
- The `<api-version>` value behaviour as NINA's API contract bumps (e.g., when a NINA 3.x release decides to roll the api-version forward) is not documented in the sources we found; plugins currently all use `3.0.0`.
- Whether `<Nullable>enable</Nullable>` is on or off in `nina.plugin.template`'s modern wizard output is unconfirmed — the checked-in 4.8 csproj does not enable it.
