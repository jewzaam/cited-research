# Citation Audit — C# NINA 3.x Plugin Coding Standards

Auditor: isolated citation-verification agent. No shared context with the research thread.
Audit date: 2026-05-17.
Method: each claim citing [N] is compared against the `Extracted:` field of citation [N] in `citations.md`. The `Extracted:` field is treated as ground truth for what the source says.

---

## Summary table

| Grade | Count | Notable items |
|---|---|---|
| VERIFIED | 46 | Most citations are well-supported |
| PARTIAL | 9 | [3], [6], [7], [17], [20], [38], [42], [53], [57] |
| INACCURATE | 2 | [16] (GUID matching claim overstated), [25] (4-place GUID claim partially attributed wrong) |
| UNCITED-CLAIM | 4 | See §UNCITED section |
| UNUSED | 0 | All 59 citations are referenced somewhere |

---

## Per-citation grades [1]–[59]

### [1] NINA Plugin Template — README

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §1: "The README explicitly recommends 'remove all PackageReferences…'" [1]
- `dotnet-nina-plugin.md` §1: "The plugin template's checked-in csproj [6] still targets .NET Framework 4.8 — treat it as historical; the README confirms the VS wizard produces a .NET 8 project [1]."
- `dotnet-nina-plugin.md` §1: "The VS post-build editor mangles `%localappdata%` tokens… [1]"
- `dotnet-nina-plugin.md` §3: "Sources: [1], [8]"
- `dotnet-nina-plugin.md` §3: defaults section referencing `MinimumApplicationVersion` default of `1.11.0.0`
- `dotnet-nina-plugin.md` §4: "per [1] it 'Must be initialized first before you can use it'"
- `dotnet-nina-plugin.md` §12.4: "Match the NINA.Plugin NuGet version compiled against [1]"
- `dotnet-nina-plugin.md` Appendix A: "Sources: [1] structure"
- `build-and-install.md`: plugin template README recommendation, .NET 8 wizard note, `%localappdata%` mangling
- `assembly-metadata.md`: required/recommended/optional split; `MinimumApplicationVersion` semantics
- `mef-manifest.md`: "Mandatory to be exported once!" quote; injectable interfaces list; `ISequenceMediator` caveat
- `wpf-options-ui.md`: `_Options`, `_Mini`, `_Dockable`, `_CameraSettings` postfixes listed
- `publishing.md`: manifest `MinimumApplicationVersion` matches NuGet version

**Claims vs. Extracted:** All claims trace directly to the Extracted field: the template README documents `AssemblyMetadata` keys, the injectable interface list (30+), DataTemplate naming, .NET 8 migration steps including `MinimumApplicationVersion` matching NuGet version, the `%localappdata%` token mangling workaround, and the wizard producing .NET 8 despite prompting for 4.8. The `ISequenceMediator` caveat ("Must be initialized first before you can use it which is after all plugins are loaded!") is quoted verbatim in the Extracted field.

---

### [2] NINA Plugin Template — `MyPlugin.cs`

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §3, §4, §7, §10.3, §12.2, cheat sheet
- `mef-manifest.md`: inheritance pattern, `[ImportingConstructor]`, `Teardown()` pattern
- `persisted-options.md`: `PluginOptionsAccessor` construction, `ProfileChanged` subscription
- `publishing.md`: four-place GUID — place #4 (PluginOptionsAccessor constructor)
- `assembly-metadata.md`: `PluginOptionsAccessor(profileService, Guid.Parse(this.Identifier))`

**Claims vs. Extracted:** `[Export(typeof(IPluginManifest))]`, `[ImportingConstructor]`, `PluginOptionsAccessor(profileService, Guid.Parse(this.Identifier))`, `BeforeImageSaved` / `BeforeFinalizeImageSaved` subscriptions, `ProfileChanged` subscription, `Teardown()` unsubscription, manual `INotifyPropertyChanged` with `[CallerMemberName]`, PluginBase populating manifest from AssemblyInfo — all directly in the Extracted field.

---

### [3] NINA Plugin Template — `Properties/AssemblyInfo.cs`

**Grade: PARTIAL**

**Used in:**
- `dotnet-nina-plugin.md` §3: "The template's checked-in `AssemblyInfo.cs` [3] contains zero `[AssemblyMetadata]` keys"
- `assembly-metadata.md`: "The template's checked-in `AssemblyInfo.cs` [3] contains ONLY standard CLR attributes — no `[AssemblyMetadata(...)]` keys."
- `publishing.md`: cited as source #1 of four GUID places — "[3], [28]" for `[assembly: Guid(...)]` in AssemblyInfo

**Claims vs. Extracted:** The "no `[AssemblyMetadata]` keys" claim is directly supported — the Extracted field lists all attributes present and none are `AssemblyMetadata`. The `[Guid]` attribute is confirmed in the Extracted field. However, the `publishing.md` cites [3] and [28] together as confirmation that `[assembly: Guid(...)]` is the assembly-level attribute. [3] confirms a Guid attribute exists in the template file; this is valid.

The PARTIAL grade is for one nuance: the reference file `assembly-metadata.md` says "The template's checked-in `AssemblyInfo.cs` [3] contains ONLY standard CLR attributes." The Extracted field for [3] ends with the explicit note "**No `[AssemblyMetadata(...)]` keys are present in the template's AssemblyInfo** — plugin authors must add them per [1]." This is fully consistent. No real overstep — but [3] is cited in `publishing.md` to establish that `[assembly: Guid]` is how place #1 works. The Extracted field for [3] does confirm `[assembly: Guid("78fc6455-c1ba-4dc5-a8d0-9f48aecd733d")]` is present, so that use is valid too.

Reconsidered: this is actually VERIFIED. The claims match. Upgrading to VERIFIED.

**Revised Grade: VERIFIED**

---

### [4] NINA Plugin Template — `Options.xaml`

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` cheat sheet: "Options UI key `<AssemblyTitle>_Options`… [4][23][24]"
- `dotnet-nina-plugin.md` §6.1: "The template [4] uses `x:Key="$pluginname$_Options"`"
- `wpf-options-ui.md`: "The template [4] uses `x:Key="$pluginname$_Options"`"

**Claims vs. Extracted:** The Extracted field confirms: `<DataTemplate x:Key="$pluginname$_Options">`, comment "the key has to follow the naming convention of `<IPlugin.Name>_Options`", `[Export]` via code-behind. All claims match.

---

### [5] NINA Plugin Template — `Options.xaml.cs`

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §6.2: "`[Export(typeof(ResourceDictionary))]` partial class : ResourceDictionary" code snippet; "Source: [4], [5]"
- `dotnet-nina-plugin.md` cheat sheet: "[5]"
- `mef-manifest.md`: "[Export(typeof(ResourceDictionary))]" on code-behind partial class
- `wpf-options-ui.md`: code snippet for Options.xaml.cs

**Claims vs. Extracted:** The Extracted field shows exactly `[Export(typeof(ResourceDictionary))]` on the partial class declaration and `partial class Options : ResourceDictionary { public Options() { InitializeComponent(); } }`. All claims match.

---

### [6] NINA Plugin Template — `NINA.Plugin.Template.csproj`

**Grade: PARTIAL**

**Used in:**
- `dotnet-nina-plugin.md` §1: "The plugin template's checked-in csproj [6] still targets .NET Framework 4.8"
- `build-and-install.md`: "Plugin template repo csproj: `.NET Framework 4.8` (stale; wizard generates net8.0 anyway) [1], [6]"
- `build-and-install.md`: "The recommended pattern: reference `NINA.Plugin` with `<PrivateAssets>all</PrivateAssets>`… The template csproj [6] is too stale to demonstrate this"

**Claims vs. Extracted:** The `.NET Framework 4.8` target and the NINA NuGet 2.0.2.9001 references are confirmed. The note about being stale and the wizard generating .NET 8 comes from [1], not [6] itself. The Extracted field for [6] does note it is stale and the README [1] says the wizard generates .NET 8 — this is captured in the Extracted field: "Treat as historical reference." The deliverable correctly attributes the .NET 8 wizard behavior to [1].

One partial: `build-and-install.md` says the csproj "references NINA NuGets at 2.0.2.9001" — confirmed in Extracted. The claim that the template "does not demonstrate `PrivateAssets=all`" is an absence claim — consistent with the Extracted field, which does not mention `PrivateAssets`.

The PARTIAL is because the Extracted field says "Treat as historical reference" but some derived claims (e.g., "too stale to demonstrate PrivateAssets") are inferences rather than direct reads from the Extracted field. These are fair inferences from the stale content. Grade remains **PARTIAL** (borderline VERIFIED, downgraded for inference-based wording).

---

### [7] NINA — `PluginLoader.cs`

**Grade: PARTIAL**

**Used in:**
- `dotnet-nina-plugin.md` §2: "NINA's `AssemblyLoadContext` isolates plugins [7]"
- `dotnet-nina-plugin.md` §6.2: "`PluginLoader` merge the dictionary into `Application.Current.Resources.MergedDictionaries` [7]"
- `build-and-install.md`: exclusion list rationale — "the running NINA process loads them from its own folder, not the plugin folder [7]"
- `mef-manifest.md`: plugin discovery steps, fallback manifest, `ReflectionTypeLoadException`, ResourceDictionary merge
- `assembly-metadata.md`: malformed/missing behavior — synthesizes fallback `PluginManifest`, `ReflectionTypeLoadException` aggregation
- `wpf-options-ui.md`: "PluginLoader collects every `[Export(typeof(ResourceDictionary))]`… via MEF `[ImportMany]`"

**Claims vs. Extracted:** The Extracted field confirms: `AssemblyLoadContext` per plugin, two-phase catalog composition, `GuidAttribute`/`AssemblyCompanyAttribute`/`AssemblyFileVersionAttribute`/`AssemblyTitleAttribute` reads, fallback `PluginManifest`, `ReflectionTypeLoadException` aggregation, `Application.Current?.Resources.MergedDictionaries.Add(template)`.

PARTIAL: `wpf-options-ui.md` says PluginLoader uses "MEF `[ImportMany]`" to collect ResourceDictionary exports. The Extracted field says `foreach (var template in parts.DataTemplateImports) Application.Current?.Resources.MergedDictionaries.Add(template)` — the property is called `DataTemplateImports`, which implies `[ImportMany]`, but the Extracted field does not explicitly say `[ImportMany]`. The inference is reasonable but goes one step beyond what is in the Extracted field.

Also, `assembly-metadata.md` says PluginLoader "reads `GuidAttribute`, `AssemblyCompanyAttribute`, `AssemblyFileVersionAttribute`, `AssemblyTitleAttribute` via reflection" — confirmed in Extracted.

---

### [8] NINA — `PluginBase.cs`

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §3: default values for `Version` (`1.0.0.0`) and `MinimumApplicationVersion` (`1.11.0.0`); PluginBase does NOT implement IDisposable
- `dotnet-nina-plugin.md` §4: "PluginBase does NOT implement `IDisposable` [8]"
- `dotnet-nina-plugin.md` §6.1: `plugin.Name` from `[AssemblyTitle]` via PluginBase
- `dotnet-nina-plugin.md` §10.3: "PluginBase [8] does NOT extend `BaseINPC`"
- `assembly-metadata.md`: full attribute-to-property mapping table
- `mef-manifest.md`: PluginBase abstract class, `Initialize()` and `Teardown()` virtual methods
- `wpf-options-ui.md`, `publishing.md`: four-place GUID (place #2, auto-populated by PluginBase)

**Claims vs. Extracted:** The Extracted field is the most detailed of all citations, confirming every property mapping, the `1.11.0.0` default for `MinimumApplicationVersion`, the `1.0.0.0` default for `Version`, `Initialize()` and `Teardown()` as virtual async methods returning `Task.CompletedTask`, and the explicit note "**Does NOT implement `IDisposable`.**" All claims match directly.

---

### [9] NINA — `IPluginManifest.cs`

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §4: "`PluginBase` provides virtual async `Initialize()` and `Teardown()`… [8]. `IPluginManifest` interface… [9]"
- `mef-manifest.md`: "Methods: `Task Initialize()`, `Task Teardown()`" — are part of the interface contract, not just PluginBase
- `assembly-metadata.md`: `IPluginManifest` [9] properties list
- `mediators-and-devices.md`: "Every event subscription… must be reversed in `Teardown()` [9]"

**Claims vs. Extracted:** The Extracted field lists all properties (`Identifier`, `Name`, `License`, `LicenseURL`, `Author`, `Homepage`, `Repository`, `ChangelogURL`, `Tags`, `Version`, `MinimumApplicationVersion`, `Installer`, `Descriptions`) and methods (`Task Initialize()`, `Task Teardown()`). All claims match.

---

### [10] NINA — `Logger.cs`

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §2: "NINA does not ship log4net. The Logger uses Serilog [10][11]"
- `dotnet-nina-plugin.md` §9: Logger methods, Error overloads, CallerMemberName params, log file path, monthly rolling, 90-day retention, 1-second flush, output format
- `build-and-install.md`: "log4net — **not present** in NINA.Core — NINA migrated to Serilog [10], [11]"
- `logging.md`: backend is Serilog; full API surface; file path; retention; output template

**Claims vs. Extracted:** The Extracted field confirms backend is Serilog (not log4net), all five methods (`Error`, `Warning`, `Info`, `Debug`, `Trace`) plus `SetLogLevel`, `IsEnabled`, `CloseAndFlush`, all three `Error` overloads, `[CallerMemberName]`/`[CallerFilePath]`/`[CallerLineNumber]` on every method, file path pattern, monthly rolling, 90-day retention via `CoreUtil.DirectoryCleanup()`, shared mode disabled, 1-second flush, and the exact output template. All claims match.

---

### [11] NINA — `NINA.Core.csproj`

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §1: "For NINA 3.3+ targets… currently `net10.0-windows` on develop [11]"
- `dotnet-nina-plugin.md` §2: Serilog not log4net; NINA-shipped assemblies list
- `dotnet-nina-plugin.md` §6.5: "CommunityToolkit.Mvvm 8.4.0 ships with NINA [11]"
- `build-and-install.md`: exclusion list — CommunityToolkit.Mvvm, Newtonsoft.Json, Serilog etc.
- `logging.md`, `wpf-options-ui.md`, `async-threading-and-csharp-style.md`

**Claims vs. Extracted:** The Extracted field confirms `net10.0-windows` for develop, `Serilog.Sinks.Console 6.1.1`, `Serilog.Sinks.File 7.0.0`, `CommunityToolkit.Mvvm 8.4.0`, `Newtonsoft.Json 13.0.4`, `System.ComponentModel.Composition 10.0.2`, `OxyPlot.Core 2.2.0`, and all other listed transitive deps. All claims match.

---

### [12] NINA — `IImagingMediator.cs`

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §5.1: "`IImagingMediator` — `ImagePrepared` — NOT `ImageSaved` [12]"
- `dotnet-nina-plugin.md` §10.1: "CancellationToken as last parameter (or second-to-last when `IProgress<T>` follows [12])"
- `mediators-and-devices.md`: "IImagingMediator [12] does not expose an `ImageSaved` event. Its only event is `ImagePrepared`"
- `testing.md`: mocking example for `IImagingMediator.CaptureImage`

**Claims vs. Extracted:** The Extracted field explicitly states "**No `ImageSaved` event on this interface** — that lives on `IImageSaveMediator` [13]" and "Single event: `ImagePrepared`". The `CaptureImage` method signature (with `CancellationToken` parameter) is confirmed. All claims match.

---

### [13] NINA — `IImageSaveMediator.cs`

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §5.1: three events, `BeforeFinalizeImageSaved` FITS-header warning
- `dotnet-nina-plugin.md` §10.1: "`Func<..., Task>` events [13] must return `Task`"
- `mediators-and-devices.md`: three-event table with delegate types and timing
- `async-threading-and-csharp-style.md`: async event patterns

**Claims vs. Extracted:** The Extracted field confirms all three events: `BeforeImageSaved` (`Func<object, BeforeImageSavedEventArgs, Task>`), `BeforeFinalizeImageSaved` (`Func<object, BeforeFinalizeImageSavedEventArgs, Task>`), `ImageSaved` (`EventHandler<ImageSavedEventArgs>`). The source comment "Altering Image Meta Data will NOT be reflected in the written file" is in the Extracted field. All claims match.

---

### [14] NINA — `ITelescopeMediator.cs`

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §5.1: telescope events table
- `mediators-and-devices.md`: confirmed events list

**Claims vs. Extracted:** The Extracted field lists exactly `BeforeMeridianFlip`, `AfterMeridianFlip`, `Parked`, `Homed`, `Unparked`, `Slewed`. The claim in the deliverable lists these verbatim. Confirmed.

---

### [15] NINA — `IDeviceMediator.cs`

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §5.2: interface definition with `RegisterConsumer`, `RemoveConsumer` (not `Unregister`), `Broadcast`
- `mediators-and-devices.md`: generic interface definition

**Claims vs. Extracted:** The Extracted field confirms the generic `IDeviceMediator<THandler, TConsumer, TInfo>` with `RegisterConsumer(TConsumer)`, `RemoveConsumer(TConsumer)` (explicitly noting "note: `Remove`, not `Unregister`"), and `Broadcast(TInfo deviceInfo)`. All claims match.

---

### [16] NINA — `PluginSettingsTemplate.cs`

**Grade: INACCURATE (partially)**

**Used in:**
- `dotnet-nina-plugin.md` §7: typed accessors list; GUID extraction; profile scope
- `dotnet-nina-plugin.md` §12.2: four-place GUID — place #4 "The GUID passed to `new PluginOptionsAccessor(...)`" cited as [16], [2]
- `persisted-options.md`: full API surface; GUID extraction; enum/color serialization; profile scope
- `assembly-metadata.md`: `PluginOptionsAccessor.GetAssemblyGuid` returns null when missing or duplicated
- `publishing.md`: four-place GUID — place #4

**Claims vs. Extracted — general:** The Extracted field confirms all 16 primitive types including `GetValueSingle` (not `GetValueFloat`), `Color` stored as ARGB int, `Enum<T>` stored as string via `Enum.GetName`/`Enum.TryParse`, no internal locking, routing to `profileService.ActiveProfile.PluginSettings`. All accessor claims are verified.

**Inaccuracy flagged:** In `publishing.md`, the four-place GUID requirement is stated as:
> "4. The GUID passed to `new PluginOptionsAccessor(profileService, Guid.Parse(this.Identifier))` [16], [2]"

The Extracted field for [16] confirms the `PluginOptionsAccessor(IProfileService profileService, Guid pluginGuid)` constructor and `GetAssemblyGuid` helper. The *claim that this is a mandatory "must match" constraint* is supported. However, the same `publishing.md` section says "If any of these drift, NINA's plugin manager treats the plugin as unrelated to its prior installs — uninstalling the prior version will not update, and persisted options under the old GUID become orphaned." The Extracted field for [16] does not say anything about this behavioral consequence — that claim is an inference. The consequence for options (orphaned) is a reasonable inference from the implementation, but it is not stated in the Extracted field for [16]. This makes the behavioral consequence claim **PARTIAL** rather than strictly INACCURATE.

Reconsidering: the main claims about [16] (API surface, GUID extraction, profile scoping) are all verified. The one overreach is the behavioral consequence of GUID drift — an inference not in the Extracted field. The grade should be **PARTIAL** for [16] rather than INACCURATE.

**Revised Grade: PARTIAL**

Evidence: `Extracted:` for [16] confirms the constructor signature and `GetAssemblyGuid` behavior but does not state the consequences of GUID drift claimed in `publishing.md`.

---

### [17] NINA — `PluginSettingsTemplate.tt`

**Grade: PARTIAL**

**Used in:**
- `persisted-options.md`: "Source-of-truth T4 template generating [16]; confirms CLS type names drive method naming."
- `assembly-metadata.md`: not directly cited but provides backing for [16]

**Claims vs. Extracted:** The deliverable and reference files use [17] only to corroborate [16]'s CLS type naming convention. The Extracted field says "Source-of-truth T4 template generating [16]; confirms CLS type names drive method naming." This is accurate and the citation is used correctly.

However, [17] is cited in `persisted-options.md` primarily as a cross-reference to [16] — it does not directly appear in the deliverable's main body. The claim made (CLS type names drive method naming) is supported by the Extracted field. Grade: **VERIFIED** — reconsidering, this is fine.

**Revised Grade: VERIFIED**

---

### [18] NINA — `Profile.cs`

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §7.2: "Profile files: `%LOCALAPPDATA%\NINA\Profiles\<profile-guid>.profile`, serialized via `DataContractSerializer` [18]. `Profile.Save()` uses a journal → backup → final three-file write"
- `persisted-options.md`: profile file path; `DataContractSerializer`; journal/backup/final write pattern

**Claims vs. Extracted:** The Extracted field confirms `[Serializable]`, `[DataContract]`, `DataContractSerializer`, profile file path `Path.Combine(SpecialFolder.LocalApplicationData, "NINA", "Profiles", $"{Id}.profile")`, and `Save()` uses "journal → backup → final three-file write for crash safety." All claims match.

---

### [19] NINA — `IProfileService.cs`

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §7.3: "`IProfileService.ProfileChanged` [19]"
- `persisted-options.md`: `ProfileChanged` event, `ActiveProfile` property

**Claims vs. Extracted:** The Extracted field confirms `IProfile ActiveProfile { get; }`, `event EventHandler ProfileChanged`, and "Plugins must subscribe to `ProfileChanged` to re-raise property changed events when the active profile switches." All claims match.

---

### [20] NINA — `CoreUtil.cs`

**Grade: PARTIAL**

**Used in:**
- `dotnet-nina-plugin.md` §8: "fixed user-configurable port with fallback via `CoreUtil.GetNearestAvailablePort(port)` [20], [32]"
- `dotnet-nina-plugin.md` §9: "90-day retention [10][20]"
- `persisted-options.md`: profile file path based on `APPLICATIONTEMPPATH` [20]
- `logging.md`: log file path constructed from `APPLICATIONTEMPPATH`
- `embedded-http.md`: port selection via `CoreUtil.GetNearestAvailablePort(int port)`

**Claims vs. Extracted:** The Extracted field confirms `APPLICATIONTEMPPATH = Path.Combine(Environment.SpecialFolder.LocalApplicationData, "NINA")`, `DirectoryCleanup()` for 90-day retention, and `GetNearestAvailablePort(int port)` helper.

PARTIAL: `persisted-options.md` derives the profile path from `CoreUtil.APPLICATIONTEMPPATH` [20], but the Extracted field for [20] gives `Path.Combine(SpecialFolder.LocalApplicationData, "NINA")` as `APPLICATIONTEMPPATH`, while `Profile.cs` [18] gives the full profile path. The deliverable's §7.2 cites [18] for the profile path — correct. The `persisted-options.md` uses [20] to establish `APPLICATIONTEMPPATH` as a building block — valid but indirect. Also, `logging.md` cites [20] for the log path, which is consistent since the log path uses `APPLICATIONTEMPPATH`. No real inaccuracy, but some of the derivation steps are indirect. Grade remains **PARTIAL** due to the indirect derivation.

---

### [21] NINA — `BaseINPC.cs`

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §10.3: MVVM hierarchy showing `BaseINPC` extends `ObservableObject`
- `wpf-options-ui.md`: MVVM base class hierarchy
- `mef-manifest.md`: "Plugins that want the `RaisePropertyChanged()` helper either… derive a separate ViewModel from `BaseINPC` [21]"
- `persisted-options.md`: "AstroPhysicsToolsOptions [29] uses `RaiseAllPropertiesChanged()` (a `BaseINPC` helper)"

**Claims vs. Extracted:** The Extracted field confirms `public abstract class BaseINPC : CommunityToolkit.Mvvm.ComponentModel.ObservableObject` and the `RaisePropertyChanged([CallerMemberName])` helper. All claims match.

---

### [22] NINA — `RelayCommand.cs`

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §6.5: "NINA.Core.Utility.RelayCommand is `[Obsolete]` [22]"
- `dotnet-nina-plugin.md` "Do not" list item #2
- `wpf-options-ui.md`: "[22]. The MVVMLight… is also legacy"

**Claims vs. Extracted:** The Extracted field confirms `[Obsolete("Use CommunityToolkit.Mvvm.Input.RelayCommand instead...")]` and mentions the MVVMLight GalaSoft `NINA.WPF.Base.Utility.MVVMLight.RelayCommand` also exists but is superseded. All claims match.

---

### [23] NINA — `PluginOptionsDataTemplateSelector.cs`

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` cheat sheet and §6.1: "NINA renders the plugin's options panel by resolving `Application.Current.Resources[plugin.Name + "_Options"]` [23]"
- `wpf-options-ui.md`: keyed lookup implementation detail

**Claims vs. Extracted:** The Extracted field confirms `Application.Current.Resources[plugin.Name + DataTemplatePostfix.Options]` where `plugin.Name` is `IPluginManifest.Name`. All claims match.

---

### [24] NINA — `DataTemplatePostfix.cs`

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` cheat sheet and §6.1: `DataTemplatePostfix.Options = "_Options"` [24]
- `wpf-options-ui.md`: constants `_Options`, `_Mini`, `_Dockable`, device-settings postfixes

**Claims vs. Extracted:** The Extracted field confirms `public const string Options = "_Options"` plus `_Mini`, `_Dockable`, device-settings postfixes referenced by [1]. All claims match.

---

### [25] NINA Plugin Manifest Repository — README

**Grade: PARTIAL**

**Used in:**
- `dotnet-nina-plugin.md` §12, §12.1–§12.8 throughout; cheat sheet; "Do not" list
- `publishing.md`: throughout

**Claims vs. Extracted — high-stakes: `Installer.ChecksumType` enum:**
The deliverable's §12.1 states `"ChecksumType": "SHA256"` and the `publishing.md` table says `Installer.ChecksumType` is `enum "MD5" | "SHA1" | "SHA256"`. The Extracted field confirms exactly `Installer.ChecksumType (enum "MD5" | "SHA1" | "SHA256")`. **VERIFIED** for this specific check.

**Claims vs. Extracted — four-place GUID:**
The deliverable's §12.2 states "The same GUID lives in four places." The Extracted field says `Identifier (GUID, constant across versions)` as a required field — confirming the manifest must have it and it must be constant, but the Extracted field for [25] does not itself enumerate all four places. The four-place constraint is assembled across citations [2], [3], [8], [16], [25]. The claim attributed to [25] is only that the manifest `Identifier` must match — which is supported. The broader "four places" framing requires citations beyond [25].

**Claims vs. Extracted — licensing:**
"Closed source plugins will not be accepted" — confirmed. Acceptable licenses MIT, BSD-3-Clause, MPL-2.0 — confirmed.

**Claims vs. Extracted — folder structure:**
`manifests\<first-letter><plugin-name>\<nina-version>\<plugin-version>\manifest.json` — confirmed in Extracted field.

**Claims vs. Extracted — `Channel` field:**
`"Channel": "Beta"` for beta channel — confirmed in Extracted field.

**PARTIAL reason:** The Extracted field mentions `CreateManifest.ps1` parameters including `-beta` (designate as Beta channel release), but the deliverable's §12.6 states "Users opt-in via NINA Options > General > Plugin Repositories with URL `https://nighttime-imaging.eu/wp-json/nina/v1/beta`" — this URL is in the Extracted field. However, the Extracted field's wording is "Beta opt-in URL `https://nighttime-imaging.eu/wp-json/nina/v1/beta`" — which is consistent. Not an issue.

The overall PARTIAL is because publishing.md's behavioral consequence claim about GUID drift ("NINA's plugin manager treats the plugin as unrelated to its prior installs") is not in the Extracted field for [25], which only says `Identifier` must be constant. The behavioral consequence is a reasonable inference but goes beyond the source.

---

### [26] daleghent — `nina-influxdb-exporter/InfluxDB Exporter.csproj`

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §1: `net8.0-windows`, post-build to `3.0.0` subfolder, InfluxDB exporter as canonical example
- `build-and-install.md`: TFM, install path, post-build steps

**Claims vs. Extracted — high-stakes: 3-segment `api-version`:**
The deliverable claims the `<api-version>` is three-segment (`3.0.0`). The Extracted field confirms "creates `%localappdata%\NINA\Plugins\3.0.0\`" and "Confirms the per-`<api-version>` folder is named with **three segments** (`3.0.0`), not four (`3.0.0.9001`)." **VERIFIED.**

All other claims (TargetFramework `net8.0-windows`, OutputType Library, UseWPF, `NINA.Plugin 3.1.2.9001`, post-build copying seven supporting DLLs) are confirmed in the Extracted field.

---

### [27] daleghent — `nina-influxdb-exporter/InfluxDbExporter.cs`

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §4: verified across [2], [27], [31], [56]
- `mef-manifest.md`: 12 injected mediators; `Initialize()` starts background work; `Teardown()` cleanup pattern

**Claims vs. Extracted:** The Extracted field confirms `PluginBase` inheritance, `[Export(typeof(IPluginManifest))]`, `[ImportingConstructor]` with 12 mediators, background `Task.Run` in Initialize, `Teardown()` signals cancellation and disposes. All claims match.

---

### [28] daleghent — `nina-influxdb-exporter/Properties/AssemblyInfo.cs`

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §3: "The `nina-influxdb-exporter` AssemblyInfo [28] is a realistic complete example"
- `dotnet-nina-plugin.md` Appendix A: "Sources: [1] structure, [28] live example"
- `assembly-metadata.md`: `MinimumApplicationVersion` format (4-segment), realistic example

**Claims vs. Extracted:** The Extracted field confirms `[AssemblyMetadata("MinimumApplicationVersion", "3.2.0.1000")]` (note: uses `3.2.0.1000` not `3.2.0.9001` — the deliverable correctly notes it "pins to the 3.2 stable API floor"). All listed attributes are in the Extracted field. All claims match.

---

### [29] daleghent — `nina-astro-physics-tools/AstroPhysicsToolsOptions.cs`

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §7: defensive `GetAssemblyGuid` form; `nameof()` for keys
- `persisted-options.md`: `GetAssemblyGuid` check with explicit throw; `nameof(PropertyName)` pattern; `RaiseAllPropertiesChanged()`

**Claims vs. Extracted:** The Extracted field confirms `PluginOptionsAccessor.GetAssemblyGuid(typeof(AstroPhysicsToolsOptions))` with null-check and throw, `ProfileChanged` subscription calling `RaiseAllPropertiesChanged()`, and `nameof(PropertyName)` as the setting key. All claims match.

---

### [30] christian-photo — `ninaAPI/ninaAPI.csproj`

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §1: `net8.0-windows`, `xcopy` to `3.0.0\Advanced API\`, ninaAPI as example
- `build-and-install.md`: TFM, install path, `xcopy` pattern; note that ninaAPI directly references all NINA sub-packages (against the recommendation)

**Claims vs. Extracted:** The Extracted field confirms `net8.0-windows`, `NINA.Plugin 3.2.0.9001`, `EmbedIO 3.5.2`, post-build `xcopy` to `%localappdata%\NINA\Plugins\3.0.0\Advanced API\`, and notes this plugin explicitly references all NINA assemblies directly. All claims match.

---

### [31] christian-photo — `ninaAPI/AdvancedAPI.cs`

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §4: "Pattern verified across [2], [27], [31], [56]"
- `mef-manifest.md`: 25+ injected mediators; static `NINAControls` aggregator; `Teardown()` cleanup

**Claims vs. Extracted:** The Extracted field confirms `PluginBase` inheritance, `[Export(typeof(IPluginManifest))]`, `[ImportingConstructor]` with 25+ mediators, `NINAControls` aggregator, and `Teardown()` pattern. All claims match.

---

### [32] christian-photo — `ninaAPI/WebService/API.cs`

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §8: canonical EmbedIO pattern with dedicated thread, `serverToken.Cancel()` stop
- `embedded-http.md`: `http://*:{Port}` prefix, `HttpListenerMode.EmbedIO`, named thread, `RunAsync().Wait()`

**Claims vs. Extracted:** The Extracted field confirms `new WebServer(o => o.WithUrlPrefix($"http://*:{Port}").WithMode(HttpListenerMode.EmbedIO))`, dedicated named `Thread("API Thread")`, `apiToken.Cancel()` unblocks `.Wait()`. All claims match.

---

### [33] Touch-N-Stars — `TouchNStarsServer.cs`

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §8: "Canonical pattern… synthesized from [32], [33]"
- `embedded-http.md`: confirms EmbedIO+named-thread pattern across plugins

**Claims vs. Extracted:** The Extracted field confirms same pattern as [32]: `http://*:{port}`, `HttpListenerMode.EmbedIO`, named thread, `RunAsync().Wait()`, `Cancel()` stop. The claim that "this confirms EmbedIO+named-thread pattern is the de-facto idiom across NINA plugins" is supported.

---

### [34] EmbedIO — `WebServer.cs`

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §8: "`HttpListenerMode.EmbedIO` bypasses http.sys by binding raw managed TCP sockets [35]" — note this specific claim cites [35] not [34]
- `embedded-http.md`: factory method switches on `HttpListenerMode`; `Microsoft` vs `EmbedIO` path

**Claims vs. Extracted:** The Extracted field confirms the factory method switch: `Microsoft` → `new SystemHttpListener(new System.Net.HttpListener())`, anything else → `new EmbedIO.Net.HttpListener(...)`. The `ProcessRequestsAsync` loop on `cancellationToken.IsCancellationRequested` is also confirmed. All claims match.

---

### [35] EmbedIO — `EndPointListener.cs`

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §8: "`HttpListenerMode.EmbedIO` bypasses http.sys by binding raw managed TCP sockets [35]"
- `embedded-http.md`: raw socket implementation details

**Claims vs. Extracted:** The Extracted field confirms `new Socket(SocketType.Stream, ProtocolType.Tcp)`, `Bind(IPEndPoint)`, `Listen(500)`, and explicitly states "no http.sys, no URL ACL, no netsh, no admin requirement for ports >1023." All claims match.

---

### [36] EmbedIO NuGet Gallery

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §8: "NuGet: `EmbedIO 3.5.2` [36], targets `.NETStandard 2.0`"
- `embedded-http.md`: package ID `EmbedIO` (not `Unosquare.EmbedIO`), version `3.5.2`, `.NETStandard 2.0`

**Claims vs. Extracted:** The Extracted field confirms package ID `EmbedIO`, version `3.5.2` (published 2022-10-31), `.NETStandard 2.0`. All claims match.

---

### [37] Microsoft Learn — HttpListenerException Access denied

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §8: "Do not use `HttpListenerMode.Microsoft` — that path requires elevation or `netsh http add urlacl`"
- `embedded-http.md`: the http.sys problem; `http://localhost:PORT/` exemption; wildcards require admin

**Claims vs. Extracted:** The Extracted field confirms `HttpListenerException (5): Access is denied` without admin or pre-existing urlacl, `http://localhost:PORT/` exemption, and wildcards (`http://+:PORT/` or `http://*:PORT/`) always require admin or urlacl. All claims match.

---

### [38] Grapevine docs — netsh urlacl syntax

**Grade: PARTIAL**

**Used in:**
- `embedded-http.md`: "`netsh http add urlacl url=http://+:1234/ user=DOMAIN\user` command syntax [37], [38]"

**Claims vs. Extracted:** The claim in `embedded-http.md` is: "Any non-elevated process that tries to bind a new namespace gets `System.Net.HttpListenerException (5): Access is denied` [37]. The only exemption is `http://localhost:PORT/` — wildcards… always require admin or a pre-registered `netsh http add urlacl url=http://+:PORT/ user=DOMAIN\user` entry [37], [38]."

[38] is cited alongside [37] for the `netsh` command. The Extracted field for [38] confirms the `netsh http add urlacl url=http://+:1234/ user=DOMAIN\user` syntax and "exact match" requirement. The command syntax claim is supported. However, the broader context of requiring admin vs urlacl comes primarily from [37]; [38] adds only the command syntax. The citation is accurate for what it's used for.

The PARTIAL is because [38] is Tier 3 (Grapevine legacy docs) and the deliverable uses it primarily to confirm a `netsh` command syntax — valid but [38]'s narrow scope means any claims broader than that syntax are not from [38].

---

### [39] NuGet Gallery — `NINA.Plugin`

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §1: "current stable `3.2.0.9001` [39]"
- `build-and-install.md`: "9001" designates stable; transitive NINA sub-packages
- `assembly-metadata.md`: exclusion list items as "NINA.Plugin transitive"

**Claims vs. Extracted:** The Extracted field confirms `3.2.0.9001` as current stable, "9001" = stable build designation, `net8.0` (Windows), transitive dependencies bringing all NINA sub-assemblies at matching version. All claims match.

---

### [40] NuGet Gallery — `NINA.Core`

**Grade: VERIFIED**

**Used in:**
- `build-and-install.md`: "`CommunityToolkit.Mvvm` ships with NINA at runtime and must NOT be copied into the plugin output folder"

**Claims vs. Extracted:** The Extracted field confirms `CommunityToolkit.Mvvm >= 8.2.2` (8.4.0 in develop) is a transitive dependency of NINA.Core and must not be copied. All claims match.

---

### [41] NINA 3.0.0.9001 RELEASE_NOTES

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §1: "`<api-version>` subfolder is **3-segment** `3.0.0`, NOT the 4-segment `3.0.0.9001` package version [41]"
- `build-and-install.md`: "plugin folder in `%localappdata%\NINA\Plugins` now contains a subfolder with the Major.Minor.Revision version"
- `dotnet-nina-plugin.md` cheat sheet: "`<api-version>` segment — 3-part, currently `3.0.0` for all NINA 3.x [41]"

**Claims vs. Extracted — high-stakes: 3-segment `api-version`:**
The Extracted field states: "plugin folder in `%localappdata%\NINA\Plugins` now contains a subfolder with the Major.Minor.Revision version of the application" — confirming three-part. **VERIFIED.**

---

### [42] NINA CONTRIBUTING.md

**Grade: PARTIAL**

**Used in:**
- `dotnet-nina-plugin.md` §11: "NINA core itself uses **NUnit + FluentAssertions** [42]"
- `dotnet-nina-plugin.md` cheat sheet: "Platform: x64 [42]"
- `build-and-install.md`: "Platform x64 (NINA itself built `-p:PlatformTarget=x64`) [42]"
- `testing.md`: NUnit convention from CONTRIBUTING.md; test run command

**Claims vs. Extracted:** The Extracted field confirms NUnit + FluentAssertions and the test run command `dotnet test ... -p:PlatformTarget=x64`. The x64 platform claim is supported by the `-p:PlatformTarget=x64` flag in the test command — this is a reasonable inference that NINA is built x64, though the Extracted field is about the test command specifically, not the build target for NINA's main assembly.

PARTIAL: The x64 platform claim for plugins (`dotnet-nina-plugin.md` cheat sheet: "Platform: x64 [42]") uses [42] as the source. The Extracted field for [42] shows the test command runs with `PlatformTarget=x64` — this establishes NINA runs x64, from which the plugin must also target x64. The inference is sound but indirect; the Extracted field does not directly say "plugins must target x64."

---

### [43] CommunityToolkit.Mvvm — `[ObservableProperty]` docs

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §10.2, §11: "not `virtual`, so Moq cannot proxy them on concrete classes"; class must be `partial`
- `wpf-options-ui.md`, `testing.md`, `async-threading-and-csharp-style.md`

**Claims vs. Extracted:** The Extracted field confirms generated properties are `public` with standard getter/setter — not `virtual`; requires class to be `partial`; C# 12+ supports partial property syntax. All claims match.

---

### [44] CommunityToolkit.Mvvm — ObservableObject docs

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §10.3: MVVM hierarchy `ObservableObject [44]`
- `wpf-options-ui.md`: MVVM hierarchy; BaseINPC derives from ObservableObject

**Claims vs. Extracted:** The Extracted field confirms `ObservableObject` is the base class for `INotifyPropertyChanged` types, and that `BaseINPC` derives from this. All claims match.

---

### [45] Microsoft Learn — InternalsVisibleToAttribute

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §11: `<InternalsVisibleTo Include="MyPlugin.Tests" />`; unsigned assemblies need only the name
- `testing.md`: SDK-style csproj pattern; unsigned plugin assemblies

**Claims vs. Extracted:** The Extracted field confirms the SDK-style csproj pattern `<InternalsVisibleTo Include="MyPlugin.Tests" />` inside `<ItemGroup>`, and that unsigned assemblies need name-only. All claims match.

---

### [46] Xunit.StaFact

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §11: "`Xunit.StaFact` (`[WpfFact]`, `[StaFact]`) [46]"
- `testing.md`: `[WpfFact]`, `[StaFact]`, `[UIFact]`; required for WPF types in tests

**Claims vs. Extracted:** The Extracted field confirms `[WpfFact]`, `[StaFact]`, cross-platform `[UIFact]`; required for tests touching `Dispatcher.CurrentDispatcher` or `ObservableCollection<T>`. All claims match.

---

### [47] NUnit issue #4565

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §11: "pinned to avoid NUnit `net8.0-windows`+`win-x64` issue"
- `testing.md`: known incompatibility; workaround pin to `net8.0-windows10.0.22621.0`

**Claims vs. Extracted:** The Extracted field confirms the known incompatibility between `net8.0-windows` + `win-x64` RID, and the workaround to pin to `net8.0-windows10.0.22621.0`. All claims match.

---

### [48] Rick Strahl — Async and Async-Void Event Handling in WPF

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §5.1, §10.1: `async void` must wrap in `try/catch`; `Dispatcher.InvokeAsync` not `BeginInvoke`; unhandled exceptions crash via `SynchronizationContext`
- `mediators-and-devices.md`, `async-threading-and-csharp-style.md`

**Claims vs. Extracted:** The Extracted field confirms: wrapping in `await Dispatcher.InvokeAsync(...)` resolves hang issues; `async void` acceptable only for top-level delegate-typed handlers; unhandled exceptions propagate to UI `SynchronizationContext` and crash unless global handler is wired; best practice: wrap in `try/catch` with `Logger.Error(ex)`. All claims match.

---

### [49] dotnet/wpf issue #2885 — Nullable annotations

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §10.2: "`<Nullable>enable</Nullable>` Project-wide on; `#nullable disable` per-file in XAML code-behind / `IValueConverter` files [49]"
- `async-threading-and-csharp-style.md`: WPF lacks nullable annotations; warnings in XAML code-behind

**Claims vs. Extracted:** The Extracted field confirms WPF APIs lack `#nullable` annotations as of .NET 8, producing warnings in XAML code-behind, IValueConverter, ICommand parameters. Pragmatic recommendation: enable project-wide but `#nullable disable` per-file where WPF boilerplate creates noise. All claims match.

---

### [50] C# 10 spec — File-scoped namespaces

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §10.2: "File-scoped namespaces (C# 10) — Use — `namespace Foo.Bar;` [50]"
- `async-threading-and-csharp-style.md`: constraints on file-scoped namespaces

**Claims vs. Extracted:** The Extracted field confirms: exactly one file-scoped namespace per file, cannot mix with block-scoped, `using` directives precede the namespace declaration. All claims match.

---

### [51] C# 12 spec — Primary constructors

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §10.2: "Works in principle; combine with `[method: ImportingConstructor]` [51]"
- `async-threading-and-csharp-style.md`: `[method: ImportingConstructor]`; per-parameter `[Import]` not supported

**Claims vs. Extracted:** The Extracted field confirms primary-constructor parameters scope across the class body; `method:` target for synthesized constructor attributes; per-parameter `[Import(...)]` not supported — explicit constructor required for per-parameter MEF customization. All claims match.

---

### [52] Microsoft Learn — Primary constructor tutorial

**Grade: VERIFIED**

**Used in:**
- `async-threading-and-csharp-style.md`: confirms `[method: AttributeName]` syntax

**Claims vs. Extracted:** The Extracted field confirms `[method: AttributeName]` syntax for attributing the synthesized constructor. Used correctly as corroboration.

---

### [53] MEF Attributed Programming Model

**Grade: PARTIAL**

**Used in:**
- `dotnet-nina-plugin.md` §4: "`[ImportingConstructor]` once per class [53]"; "default MEF `CreationPolicy` is `Shared` (singleton per container) [53]"
- `mef-manifest.md`: "Per MEF rules [53]: at most one `[ImportingConstructor]` per class"; part lifetime `CreationPolicy.Shared`

**Claims vs. Extracted:** The Extracted field confirms "`[ImportingConstructor]` may appear at most once per class" and "Default `[Export]` creation policy is `CreationPolicy.Shared` (singleton per container) unless explicit `[PartCreationPolicy]` overrides."

PARTIAL: The deliverable says "the default MEF `CreationPolicy` is `Shared` (singleton per container) [53] and the plugin manager relies on this — do not declare `[PartCreationPolicy(NonShared)]` on the manifest class." The italicized guidance ("plugin manager relies on this") is not in the Extracted field — it's an inference. The Extracted field establishes the default but does not say "NINA's plugin manager relies on this." The claim is reasonable but goes beyond the source for the specific NINA-context statement.

---

### [54] Microsoft Premier Developer — CancellationToken patterns

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §10.1: `CancellationToken` as last parameter; propagate through every call
- `async-threading-and-csharp-style.md`: `CancellationToken` last; explicit `ThrowIfCancellationRequested` only at boundaries

**Claims vs. Extracted:** The Extracted field confirms `CancellationToken` as the last parameter of every async method (unless followed by `IProgress<T>`); inner calls propagate `OperationCanceledException` naturally; explicit `ThrowIfCancellationRequested()` only at boundaries where no inner async call exists. All claims match.

---

### [55] C# spec — `using` declarations

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §10.2: "Prefer for single-disposable scopes [55]"
- `async-threading-and-csharp-style.md`: `using var x = ...;` disposes at end of scope

**Claims vs. Extracted:** The Extracted field confirms `using var x = ...;` disposes at end of enclosing scope; `using (...) { }` block scopes; both compile to `try/finally`. All claims match.

---

### [56] daleghent — `nina-ground-station/GroundStation.cs`

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §4: "Pattern verified across [2], [27], [31], [56]"
- `mef-manifest.md`: lifecycle hook signature confirmation

**Claims vs. Extracted:** The Extracted field confirms `PluginBase` subclass with `async Task Initialize()` / `async Task Teardown()` overrides, subscribing to events in Initialize and unsubscribing in Teardown. All claims match.

---

### [57] daleghent — NINA fork RELEASE_NOTES

**Grade: PARTIAL**

**Used in:**
- `dotnet-nina-plugin.md` §5.1: "Other device mediators follow similar per-action event pattern [57]"
- `mediators-and-devices.md`: quote "Device mediators have been enhanced with numerous new events"

**Claims vs. Extracted:** The Extracted field contains: "Device mediators have been enhanced with numerous new events that subscribers can monitor following an action performed by the device (e.g., mount slewing, cover opening, etc.)." This is cited in `mediators-and-devices.md` correctly as the source.

PARTIAL: The deliverable's §5.1 cites [57] for "Other device mediators follow similar per-action event pattern" — the Extracted field is a historical release note that confirms the introduction of per-action events in 3.x, not a source that enumerates which mediators have which events. Using it as a pointer to "other device mediators have similar events" is a reasonable inference but goes slightly beyond "historical confirmation of per-action events introduced in NINA 3.x" stated in the Extracted field.

---

### [58] photon1503 — NINA-Log-Report regex

**Grade: VERIFIED**

**Used in:**
- `logging.md`: "Python parser regex confirms log line format `Timestamp|Level|...`"; default log path
- `dotnet-nina-plugin.md` §9 indirectly (logging format confirmed by [10], [58] is in logging.md only)

**Claims vs. Extracted:** The Extracted field confirms "Python parser regex confirms log line format `Timestamp|Level|...` matching the Serilog template in [10]" and default log path `%localappdata%/NINA/Logs`. Used correctly as corroboration of [10]'s format string.

---

### [59] tcpalmer — Target Scheduler Technical Details

**Grade: VERIFIED**

**Used in:**
- `dotnet-nina-plugin.md` §9: "e.g., `tcpalmer/nina-scheduler` uses `TS-` prefix [59]"
- `logging.md`: 90-day retention; separate plugin log file pattern

**Claims vs. Extracted:** The Extracted field confirms "Like the main NINA logs … will also be purged after 90 days" and documents the pattern of a separate plugin log file in `%localappdata%\NINA\<PluginName>\Logs\` with a custom prefix (`TS-`). All claims match.

---

## High-stakes claim verification

### 1. `<api-version>` install subfolder is 3-segment (`3.0.0`), not 4-segment

**Sources cited: [41] and [26]/[30]**

- [41] Extracted: "plugin folder in `%localappdata%\NINA\Plugins` now contains a subfolder with the Major.Minor.Revision version of the application" — **3-segment confirmed.**
- [26] Extracted: "creates `%localappdata%\NINA\Plugins\3.0.0\`" and explicitly notes three segments not four. **Confirmed.**
- [30] Extracted: "xcopy's assembly to `%localappdata%\NINA\Plugins\3.0.0\Advanced API\`." **Confirmed.**

**Verdict: VERIFIED.**

---

### 2. Logger backend is Serilog, not log4net

**Sources cited: [10] and [11]**

- [10] Extracted: "**backend is Serilog** (Serilog.Sinks.Console + Serilog.Sinks.File per `NINA.Core.csproj` [11]), not log4net." **Confirmed.**
- [11] Extracted: Lists `Serilog.Sinks.Console 6.1.1` and `Serilog.Sinks.File 7.0.0`; no log4net. **Confirmed.**

**Verdict: VERIFIED.**

---

### 3. `ImageSaved` event lives on `IImageSaveMediator`, not `IImagingMediator`

**Sources cited: [12] and [13]**

- [12] Extracted: "**Single event: `ImagePrepared`**… **No `ImageSaved` event on this interface** — that lives on `IImageSaveMediator` [13]." **Confirmed.**
- [13] Extracted: Confirms `ImageSaved` typed `EventHandler<ImageSavedEventArgs>` on `IImageSaveMediator`. **Confirmed.**

**Verdict: VERIFIED.**

---

### 4. `NINA.Core.Utility.RelayCommand` is `[Obsolete]`

**Source cited: [22]**

- [22] Extracted: "Class is decorated `[Obsolete("Use CommunityToolkit.Mvvm.Input.RelayCommand instead...")]`." **Confirmed.**

**Verdict: VERIFIED.**

---

### 5. `PluginBase` does not implement `IDisposable`

**Source cited: [8]**

- [8] Extracted: "**Does NOT implement `IDisposable`.**" **Confirmed.**

**Verdict: VERIFIED.**

---

### 6. The plugin GUID must match in four places

**Sources cited: [2], [16], [25], [3]**

The deliverable's §12.2 lists four places:
1. `[assembly: Guid("...")]` in AssemblyInfo — supported by [3] (Extracted: shows `[assembly: Guid(...)]`) and [28] (real example). **Verified.**
2. `IPluginManifest.Identifier` (auto-derived via PluginBase) — supported by [8] (Extracted: `Identifier` from `GuidAttribute`). **Verified.**
3. `manifest.json` `Identifier` — supported by [25] (Extracted: `Identifier (GUID, constant across versions)` as required field). **Verified.**
4. The GUID passed to `new PluginOptionsAccessor(...)` — supported by [2] (Extracted: `PluginOptionsAccessor(profileService, Guid.Parse(this.Identifier))`) and [16] (Extracted: constructor takes `Guid pluginGuid`). **Verified.**

The deliverable's `publishing.md` cites the four places as `[3], [28]` / `[8]` / `[25]` / `[16], [2]`. The `dotnet-nina-plugin.md` §12.2 does not re-cite all four — it states the constraint without repeating all individual citations (acceptable given they are in the reference file).

**Verdict: VERIFIED** across the cited sources, with the observation that place #2 relies on [8], which is not explicitly cited in §12.2's four-place list (only implied by "auto-derived from #1 via PluginBase").

---

### 7. Plugin template csproj targets .NET Framework 4.8

**Sources cited: [6] and [1]**

- [6] Extracted: "TargetFramework `.NET 4.8`." **Confirmed.**
- [1] Extracted: "warning that the wizard prompts .NET Framework 4.8 but produces a .NET 8 project." **Confirmed.**

**Verdict: VERIFIED.**

---

### 8. Default `MinimumApplicationVersion` is `1.11.0.0`

**Source cited: [8]**

- [8] Extracted: "`MinimumApplicationVersion` defaults to `"1.11.0.0"` when key absent." **Confirmed.**

The deliverable's §3 states "Defaults when missing: `Version` → `"1.0.0.0"`, `MinimumApplicationVersion` → `"1.11.0.0"` per `PluginBase` [8]."

**Verdict: VERIFIED.**

---

### 9. Manifest `Installer.ChecksumType` enum is `MD5|SHA1|SHA256`

**Source cited: [25]**

- [25] Extracted: "`Installer.ChecksumType` (enum `MD5` | `SHA1` | `SHA256`)." **Confirmed.**

**Verdict: VERIFIED.**

---

## UNCITED-CLAIM items

The following factual claims appear in the deliverable or reference files without inline citation. They may be valid — but per the audit mandate, claims without attribution should be flagged.

### UC-1: `PluginBase` does not extend `BaseINPC`

**Location:** `dotnet-nina-plugin.md` §10.3: "`PluginBase` [8] does NOT extend `BaseINPC` — the template implements `INotifyPropertyChanged` manually [2]."

**Assessment:** The citation to [8] is present in the same sentence, but the claim that PluginBase does not extend BaseINPC is inferred by comparing [8]'s Extracted field (which says it implements `IPluginManifest` and lists what it sets from assembly attributes but does not mention `BaseINPC`) against [21] (which defines `BaseINPC`). The Extracted field for [8] does not explicitly say "does NOT extend BaseINPC." The inference is confirmed by [2] (template implements INPC manually), but neither [8] nor [2] explicitly states "PluginBase does not extend BaseINPC." This is a **reasonable verified inference** rather than a direct quote — minor gap, not a significant concern.

### UC-2: `BeforeFinalizeImageSaved` fires "after processing but before final destination move"

**Location:** `dotnet-nina-plugin.md` §5.1 timing column for `BeforeFinalizeImageSaved`.

**Assessment:** The Extracted field for [13] states `BeforeFinalizeImageSaved` fires "after processing but before final destination move" — so this IS cited (by [13]). Not actually an uncited claim. **Cleared.**

### UC-3: EmbedIO's `http://*:port` wildcard "does not always correctly route to every IPv4 address"

**Location:** `embedded-http.md`: "EmbedIO has an open issue [D7 finding] noting that with `HttpListenerMode.EmbedIO`, the wildcard prefix `http://*:port` does not always correctly route…"

**Assessment:** This is tagged "[D7 finding]" internally — it references a discovery-phase finding, not a numbered citation in `citations.md`. No citation [1]–[59] covers this claim. It is presented as a caveat in a reference file (not the main deliverable), so the risk is low — but it is an uncited claim in the reference material. **Flag: UNCITED-CLAIM in embedded-http.md.**
**Status: RESOLVED** — Citation [63] (EmbedIO issue #459 — wildcard binding bug, wontfix) added to citations.md; embedded-http.md updated to cite [63] in place of the internal `[D7 finding]` tag.

### UC-4: NINA-themed style keys (StandardTextBlock, SideBarTextBlock, etc.)

**Location:** `wpf-options-ui.md` table of style and brush keys citing "[D5 analysis]" — not a numbered citation.

**Assessment:** The style table references "[D5 analysis]" which is a discovery-phase finding, not a numbered citation [1]–[59]. None of the citations cover the NINA WPF theme resource keys directly. This is an uncited claim (relative to the numbered citation system) in the reference file. **Flag: UNCITED-CLAIM in wpf-options-ui.md.**
**Status: RESOLVED** — Three citations added to citations.md: [60] `NINA.WPF.Base/Resources/Styles/TextBlock.xaml`, [61] `NINA.WPF.Base/Resources/Styles/Button.xaml`, [62] `NINA.WPF.Base/Resources/StaticResources/Brushes.xaml`. The wpf-options-ui.md table now cites each row to its source XAML file; `[D5 analysis]` tag removed.

---

## UNUSED citations

All 59 citations [1]–[59] are referenced in at least one location across the deliverable or reference files. None are unused.

---

## Final tally

| Grade | Count |
|---|---|
| VERIFIED | 51 |
| PARTIAL | 7 ([6], [7], [16], [20], [25], [42], [53], [57], [38]) |
| INACCURATE | 0 |
| UNCITED-CLAIM | 2 (in reference files only; UC-3 and UC-4) |
| UNUSED | 0 |

> Note: [3] and [17] were initially flagged PARTIAL but revised to VERIFIED after re-examination. [16] was initially flagged INACCURATE but revised to PARTIAL. Final PARTIAL count is 8 ([6], [7], [16], [20], [25], [38], [42], [53], [57]).

---

## Summary of PARTIAL findings

| Citation | Issue |
|---|---|
| [6] | "Too stale to demonstrate `PrivateAssets`" is an inference from absence, not stated in Extracted |
| [7] | `[ImportMany]` attribution for ResourceDictionary collection is an inference; `DataTemplateImports` property name in Extracted implies it but does not say `[ImportMany]` |
| [16] | Behavioral consequence of GUID drift ("plugin manager treats as unrelated, options orphaned") is not in the Extracted field |
| [20] | Profile path derivation from `APPLICATIONTEMPPATH` is indirect (path is in [18]; [20] provides the base constant only) |
| [25] | Behavioral consequence of GUID drift not in Extracted; four-place GUID constraint is partially assembled across multiple citations |
| [38] | Tier-3 source; used only for `netsh` command syntax, which is confirmed; main http.sys access-denied reasoning comes from [37] |
| [42] | x64 platform requirement for plugins is inferred from the test command's `PlatformTarget=x64` flag; Extracted field is about running tests, not building plugins |
| [53] | "NINA's plugin manager relies on Shared creation policy" is an inference; the Extracted field only establishes the MEF default |
| [57] | Used to imply other device mediators have similar events — Extracted field only confirms introduction of events in 3.x historically |

---

## Notable observations

1. **Zero inaccuracies found.** No citation is used to support a claim that the source contradicts. The research thread was careful to align claims with what sources actually say.

2. **The high-stakes claims all verified.** The 3-segment `api-version`, Serilog backend, `ImageSaved` on `IImageSaveMediator`, `[Obsolete]` RelayCommand, `PluginBase` not implementing `IDisposable`, `1.11.0.0` default, `MD5|SHA1|SHA256` enum — all directly supported by the Extracted fields of their cited sources.

3. **PARTIAL cases are inference-quality**, not drift. Each PARTIAL involves a reasonable step of inference from the source rather than a mismatch. No PARTIAL approaches INACCURATE on reconsideration.

4. **Two uncited claims in reference files** use internal "[D5 analysis]" and "[D7 finding]" tags referencing discovery-phase findings that never received numbered citations. These are in `wpf-options-ui.md` (NINA style keys) and `embedded-http.md` (EmbedIO `http://*` wildcard caveat). Both are presented as observations/caveats, not central claims — risk level is low.
