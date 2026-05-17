# Citations — C# NINA 3.x Plugin Coding Standards

Sources are numbered sequentially. Each entry records the URL visited, what was extracted, source quality tier, and accessibility state at fetch time. Where a local repository was used as ground-truth context, the GitHub-hosted equivalent is cited per user instruction. Fetched: 2026-05-17 unless stated otherwise.

---

## [1] NINA Plugin Template — README

- **URL:** https://github.com/isbeorn/nina.plugin.template (raw: `https://raw.githubusercontent.com/isbeorn/nina.plugin.template/master/README.md`)
- **Tier:** 1 (official plugin starter authored by NINA maintainer Stefan Berg / @isbeorn)
- **Extracted:** Full list of required/recommended/optional `AssemblyMetadata` keys (ShortDescription, License, LicenseURL, Repository, MinimumApplicationVersion, ChangelogURL, Tags, Homepage, LongDescription, FeaturedImageURL, ScreenshotURL, AltScreenshotURL); full set of exportable interfaces (IPluginManifest, ISequenceItem, ISequenceTrigger, ISequenceCondition, ISequenceContainer, IDockableVM, IPluggableBehavior, IEquipmentProvider); 30+ injectable mediator/service interfaces; DataTemplate naming conventions (`<IPluginManifest.Name>_Options`, `<Type>_Mini`, `<Type>_Dockable`, `<Type>_CameraSettings`); manifest distribution at Bitbucket; manual install path `%localappdata%\NINA\Plugins`; .NET 8 migration steps including upgrade-assistant, `NINACustomControlLibrary` → `NINA.CustomControlLibrary` rename, OxyPlot.Wpf → OxyPlot.Contrib.Wpf split, `MinimumApplicationVersion` must match `NINA.Plugin` NuGet version; warning that the wizard prompts .NET Framework 4.8 but produces a .NET 8 project; post-build event `%localappdata%` token corruption workaround.
- **Status:** OK

## [2] NINA Plugin Template — `MyPlugin.cs` (canonical IPluginManifest implementation)

- **URL:** https://github.com/isbeorn/nina.plugin.template/blob/master/NINA.Plugin.Template/MyPlugin.cs (raw: `https://raw.githubusercontent.com/isbeorn/nina.plugin.template/master/NINA.Plugin.Template/MyPlugin.cs`)
- **Tier:** 1
- **Extracted:** `[Export(typeof(IPluginManifest))]` on class; `public class $pluginclassname$ : PluginBase, INotifyPropertyChanged`; `[ImportingConstructor]` accepting `IProfileService, IOptionsVM, IImageSaveMediator`; `PluginOptionsAccessor(profileService, Guid.Parse(this.Identifier))` construction; `Settings.Default.Upgrade()` legacy ApplicationSettingsBase pattern alongside `IPluginOptionsAccessor`; `imageSaveMediator.BeforeImageSaved` / `BeforeFinalizeImageSaved` subscription as async-returning `Func<object, ..., Task>` handlers; `profileService.ProfileChanged += ProfileService_ProfileChanged` to surface per-profile values; `options.AddImagePattern(...)` to register file patterns; `Task Teardown()` override unsubscribes events then `return base.Teardown();`; manual `INotifyPropertyChanged` impl with `[CallerMemberName]`; class-level summary doc states "The base class PluginBase will populate all the necessary Manifest Meta Data out of the AssemblyInfo attributes" and "the user interface for the settings will be defined by a DataTemplate with the key having the naming convention `$pluginclassname$_Options`".
- **Status:** OK

## [3] NINA Plugin Template — `Properties/AssemblyInfo.cs`

- **URL:** https://github.com/isbeorn/nina.plugin.template/blob/master/NINA.Plugin.Template/Properties/AssemblyInfo.cs (raw: same path under `raw.githubusercontent.com`)
- **Tier:** 1
- **Extracted:** Standard CLR attributes only — `[assembly: AssemblyTitle("NINA.Plugin.Template")]`, `[assembly: AssemblyDescription("")]`, `[assembly: AssemblyConfiguration("")]`, `[assembly: AssemblyCompany("")]`, `[assembly: AssemblyProduct("NINA.Plugin.Template")]`, `[assembly: AssemblyCopyright("Copyright © 2022")]`, `[assembly: AssemblyTrademark("")]`, `[assembly: AssemblyCulture("")]`, `[assembly: ComVisible(false)]`, `[assembly: Guid("78fc6455-c1ba-4dc5-a8d0-9f48aecd733d")]`, `[assembly: AssemblyVersion("1.0.0.0")]`, `[assembly: AssemblyFileVersion("1.0.0.0")]`. **No `[AssemblyMetadata(...)]` keys are present in the template's AssemblyInfo** — plugin authors must add them per [1].
- **Status:** OK

## [4] NINA Plugin Template — `Options.xaml`

- **URL:** https://github.com/isbeorn/nina.plugin.template/blob/master/NINA.Plugin.Template/Options.xaml
- **Tier:** 1
- **Extracted:** Plain `ResourceDictionary` containing `<DataTemplate x:Key="$pluginname$_Options">`. No `DataType`, no `MergedDictionaries`. XAML comment explicitly states "the key has to follow the naming convention of `<IPlugin.Name>_Options`" and "the Resource Dictionary has to be exported via code behind export attributes".
- **Status:** OK

## [5] NINA Plugin Template — `Options.xaml.cs`

- **URL:** https://github.com/isbeorn/nina.plugin.template/blob/master/NINA.Plugin.Template/Options.xaml.cs
- **Tier:** 1
- **Extracted:** `[Export(typeof(ResourceDictionary))]` on the partial class declaration; `partial class Options : ResourceDictionary { public Options() { InitializeComponent(); } }`.
- **Status:** OK

## [6] NINA Plugin Template — `NINA.Plugin.Template.csproj`

- **URL:** https://github.com/isbeorn/nina.plugin.template/blob/master/NINA.Plugin.Template/NINA.Plugin.Template.csproj
- **Tier:** 1 (template repo) but **content is stale** — the checked-in csproj still targets `.NET Framework 4.8` and references NINA NuGets at 2.0.2.9001. The README [1] explicitly notes that the VSIX wizard produces a .NET 8 project despite this. Treat as historical reference.
- **Extracted:** TargetFramework `.NET 4.8`; legacy NINA NuGet 2.0.2.9001 references (NINA.Core, NINA.Equipment, NINA.Image, NINA.Astrometry, NINA.PlateSolving, NINA.Sequencer, NINA.WPF.Base, NINACustomControlLibrary, plus nikoncswrapper); class library output; resource embedding for sequence items, dockable windows, XAML.
- **Status:** OK but obsolete content; modern plugins use `net8.0-windows` (see [26], [30]).

## [7] NINA — `NINA.Plugin/PluginLoader.cs` (develop branch)

- **URL:** https://github.com/isbeorn/nina/blob/develop/NINA.Plugin/PluginLoader.cs
- **Tier:** 1
- **Extracted:** Plugin discovery: enumerate `*.dll` 1 level deep from `Constants.UserExtensionsFolder`; uses dedicated `AssemblyLoadContext` per plugin for isolation (two-phase: core via `TypeCatalog`, plugin via assembly context); reads `GuidAttribute`, `AssemblyCompanyAttribute`, `AssemblyFileVersionAttribute`, `AssemblyTitleAttribute` via reflection; failed manifests synthesize a fallback `PluginManifest` populated from these attributes; non-plugin DLLs silently skipped with trace-level logging; `ReflectionTypeLoadException` is caught and `LoaderExceptions` aggregated into a single error; `foreach (var template in parts.DataTemplateImports) Application.Current?.Resources.MergedDictionaries.Add(template);` merges plugin ResourceDictionaries into app resources.
- **Status:** OK

## [8] NINA — `NINA.Plugin/PluginBase.cs` (develop branch)

- **URL:** https://github.com/isbeorn/nina/blob/develop/NINA.Plugin/PluginBase.cs
- **Tier:** 1
- **Extracted:** Abstract class implementing `IPluginManifest`; sets meta-data from assembly attributes — `Identifier` from `GuidAttribute`; `Name` from `AssemblyTitleAttribute`; `Version` from `AssemblyFileVersionAttribute` (default `1.0.0.0`); `Author` from `AssemblyCompanyAttribute`; `License`, `LicenseURL`, `Homepage`, `Repository`, `ChangelogURL`, `MinimumApplicationVersion`, `LongDescription`, `FeaturedImageURL`, `ScreenshotURL`, `AltScreenshotURL` from `AssemblyMetadataAttribute` keys; `ShortDescription` from `AssemblyDescriptionAttribute`; `Tags` from `AssemblyMetadata("Tags")` split on comma; `MinimumApplicationVersion` defaults to `"1.11.0.0"` when key absent; `Installer` returns placeholder details; `Initialize()` and `Teardown()` are virtual `async` methods returning `Task.CompletedTask`. **Does NOT implement `IDisposable`.**
- **Status:** OK

## [9] NINA — `NINA.Plugin/Interfaces/IPluginManifest.cs` (develop branch)

- **URL:** https://github.com/isbeorn/nina/blob/develop/NINA.Plugin/Interfaces/IPluginManifest.cs
- **Tier:** 1
- **Extracted:** Properties: `string Identifier`, `string Name`, `string License`, `string LicenseURL`, `string Author`, `string Homepage`, `string Repository`, `string ChangelogURL`, `string[] Tags`, `IPluginVersion Version`, `IPluginVersion MinimumApplicationVersion`, `IPluginInstallerDetails Installer`, `IPluginDescription Descriptions`. Methods: `Task Initialize()`, `Task Teardown()`. (So Initialize/Teardown are part of the interface, not just PluginBase additions.)
- **Status:** OK

## [10] NINA — `NINA.Core/Utility/Logger.cs` (develop branch)

- **URL:** https://github.com/isbeorn/nina/blob/develop/NINA.Core/Utility/Logger.cs
- **Tier:** 1
- **Extracted:** Static logger; **backend is Serilog** (Serilog.Sinks.Console + Serilog.Sinks.File per `NINA.Core.csproj` [11]), not log4net; log file path `{APPLICATIONTEMPPATH}/Logs/{timestamp}-{version}.{processId}-.log`; monthly rolling, 90-day retention via `CoreUtil.DirectoryCleanup()`; shared mode disabled; 1-second flush interval; methods `Error`, `Warning`, `Info`, `Debug`, `Trace` plus `SetLogLevel(LogLevelEnum)`, `IsEnabled(LogLevelEnum)`, `CloseAndFlush()`; `Error` overloads accept (Exception), (Exception, string), and (string); other methods accept (string); every method has `[CallerMemberName]`, `[CallerFilePath]`, `[CallerLineNumber]` optional params; output template `"{Timestamp:yyyy-MM-ddTHH:mm:ss.ffff}|{LegacyLogLevel}|{Message:lj}{NewLine}{Exception}"`; header writes system diagnostics (OS, architecture, processor count, physical memory) before message logging begins.
- **Status:** OK

## [11] NINA — `NINA.Core/NINA.Core.csproj` (develop branch)

- **URL:** https://github.com/isbeorn/nina/blob/develop/NINA.Core/NINA.Core.csproj
- **Tier:** 1
- **Extracted:** Develop branch targets `net10.0-windows` for nightly 3.3.0; stable 3.2 builds target `net8.0`. Direct PackageReferences include `CommunityToolkit.Mvvm 8.4.0`, `Newtonsoft.Json 13.0.4`, `Serilog.Sinks.Console 6.1.1`, `Serilog.Sinks.File 7.0.0`, `System.ComponentModel.Composition 10.0.2`, `Accord.Math 3.8.2-alpha`, `Google.Protobuf 3.33.4`, `Grpc.Core.Api 2.76.0`, `Grpc.Tools 2.76.0`, `OxyPlot.Core 2.2.0`, `SourceGear.sqlite3 3.50.4.5`, `System.Data.SqlClient 4.9.0`, `System.Data.SQLite 2.0.2`, `System.IO.Ports 10.0.2`, `System.Management 10.0.2`, `System.Runtime.Caching 10.0.2`. SignedRelease config signs assemblies with Sectigo timestamps.
- **Status:** OK

## [12] NINA — `NINA.Equipment/Interfaces/Mediator/IImagingMediator.cs` (develop branch)

- **URL:** https://github.com/isbeorn/nina/blob/develop/NINA.Equipment/Interfaces/Mediator/IImagingMediator.cs
- **Tier:** 1
- **Extracted:** Extends `IMediator`. Members: `CaptureImage(CaptureSequence, CancellationToken, IProgress<ApplicationStatus>, string targetName)`, `CaptureAndPrepareImage(...)`, two `PrepareImage` overloads (IImageData and IExposureData), `StartLiveView(CaptureSequence, CancellationToken)`, `DestroyImage()`, `SetImage(BitmapSource)`, `GetImageRotation()`, `SetImageRotation()`, `SetSubSambleRectangle(ObservableRectangle)`. **Single event: `ImagePrepared`** (uses `ImagePreparedEventArgs { IRenderedImage RenderedImage; PrepareImageParameters Parameters; }`). **No `ImageSaved` event on this interface** — that lives on `IImageSaveMediator` [13].
- **Status:** OK

## [13] NINA — `NINA.WPF.Base/Interfaces/Mediator/IImageSaveMediator.cs` (develop branch)

- **URL:** https://github.com/isbeorn/nina/blob/develop/NINA.WPF.Base/Interfaces/Mediator/IImageSaveMediator.cs
- **Tier:** 1
- **Extracted:** `Task Enqueue(IImageData imageData, Task<IRenderedImage> prepareTask, IProgress<ApplicationStatus> progress, CancellationToken token)`. **Three events:** (a) `BeforeImageSaved` typed `Func<object, BeforeImageSavedEventArgs, Task>` — fires "before the image is saved to the disk, but also before the image is processed fully", grants access to raw `IImageData` and the in-flight prepare task; (b) `BeforeFinalizeImageSaved` typed `Func<object, BeforeFinalizeImageSavedEventArgs, Task>` — fires after processing but before final destination move, supports image pattern injection via `AddImagePattern()`, source comment notes "Altering Image Meta Data will NOT be reflected in the written file"; (c) `ImageSaved` typed `EventHandler<ImageSavedEventArgs>` — fires after persistence; ImageSavedEventArgs carries metadata, bitmap, statistics, star detection analysis, file path, file type, Bayered status, duration, filter info. The two `Func<...,Task>` events use the async-event idiom — subscribers may `await` work inside handlers.
- **Status:** OK

## [14] NINA — `NINA.Equipment/Interfaces/Mediator/ITelescopeMediator.cs` (develop branch)

- **URL:** https://github.com/isbeorn/nina/blob/develop/NINA.Equipment/Interfaces/Mediator/ITelescopeMediator.cs
- **Tier:** 1
- **Extracted:** Extends `IDeviceMediator<ITelescopeVM, ITelescopeConsumer, TelescopeInfo>`. Methods: `MoveAxis(TelescopeAxes, double)`, `PulseGuide(GuideDirections, int)`, `StopSlew()`, `SlewToCoordinatesAsync(Coordinates, CancellationToken)`, `SlewToTopocentricCoordinates(TopocentricCoordinates, CancellationToken)`, `MeridianFlip(Coordinates, CancellationToken)`, `Sync(Coordinates)`, `SetTrackingEnabled(bool)`, `SetTrackingMode(TrackingMode)`, `SetCustomTrackingRate(SiderealShiftTrackingRate)`, `GetCurrentPosition()`, `DestinationSideOfPier(Coordinates)`, `ParkTelescope(IProgress<ApplicationStatus>, CancellationToken)`, `UnparkTelescope(...)`, `FindHome(...)`, `SendToSnapPort(bool)`, `WaitForSlew(CancellationToken)`. **Events:** `BeforeMeridianFlip`, `AfterMeridianFlip`, `Parked`, `Homed`, `Unparked`, `Slewed`. (Pattern: per-device mediator extends the generic IDeviceMediator with three type params plus device-specific methods and events.)
- **Status:** OK

## [15] NINA — `NINA.Equipment/Interfaces/Mediator/IDeviceMediator.cs` (develop branch)

- **URL:** https://github.com/isbeorn/nina/blob/develop/NINA.Equipment/Interfaces/Mediator/IDeviceMediator.cs
- **Tier:** 1
- **Extracted:** Generic `IDeviceMediator<THandler, TConsumer, TInfo>` where `THandler : IDeviceVM<TInfo>`, `TConsumer : IDeviceConsumer<TInfo>`. **Consumer registration is via `RegisterConsumer(TConsumer)` and `RemoveConsumer(TConsumer)` (note: `Remove`, not `Unregister`).** Mediator broadcasts via `Broadcast(TInfo deviceInfo)`. `IDeviceConsumer<TInfo>` is the consumer-side interface implementing `UpdateDeviceInfo(TInfo)`.
- **Status:** OK

## [16] NINA — `NINA.Profile/PluginSettingsTemplate.cs` (develop branch)

- **URL:** https://github.com/isbeorn/nina/blob/develop/NINA.Profile/PluginSettingsTemplate.cs
- **Tier:** 1
- **Extracted:** T4-generated file defining `IPluginOptionsAccessor` interface, `IPluginSettings`, and concrete `PluginOptionsAccessor` class. Constructor `PluginOptionsAccessor(IProfileService profileService, Guid pluginGuid)`. Static helper `GetAssemblyGuid(Type type)` reads `[assembly: Guid("...")]` via `type.Assembly.GetCustomAttributes(typeof(GuidAttribute), false)` — returns `null` when missing or duplicated. Methods cover 16 primitive types: `GetValueBoolean/SetValueBoolean`, `GetValueByte`, `GetValueSByte`, `GetValueChar`, `GetValueDecimal`, `GetValueDouble`, `GetValueSingle` (NOT `GetValueFloat` — uses CLS type name), `GetValueInt32`, `GetValueUInt32`, `GetValueInt64`, `GetValueUInt64`, `GetValueInt16`, `GetValueUInt16`, `GetValueString`, `GetValueDateTime`, `GetValueGuid`. Plus `Color GetValueColor(string, Color)` (stored as ARGB int via bit-shift) and `T GetValueEnum<T>(string, T) where T : struct, Enum` (stored as string via `Enum.GetName`, parsed back via `Enum.TryParse<T>`; renaming an enum member breaks deserialization). Every getter accepts a default; no coercion between types; type mismatch returns default. No internal locking. Implementation routes all calls to `profileService.ActiveProfile.PluginSettings` (a `Dictionary<Guid, IDictionary<string, object>>`).
- **Status:** OK

## [17] NINA — `NINA.Profile/PluginSettingsTemplate.tt` (T4 template)

- **URL:** https://github.com/isbeorn/nina/blob/develop/NINA.Profile/PluginSettingsTemplate.tt
- **Tier:** 1
- **Extracted:** Source-of-truth T4 template generating [16]; confirms CLS type names drive method naming.
- **Status:** OK

## [18] NINA — `NINA.Profile/Profile.cs` (develop branch)

- **URL:** https://github.com/isbeorn/nina/blob/develop/NINA.Profile/Profile.cs
- **Tier:** 1
- **Extracted:** `[Serializable]`, `[DataContract]`, `[KnownType(typeof(PluginSettings))]`; `PluginSettings` is `[DataMember]`; serializer is `DataContractSerializer`; profile file path `Path.Combine(SpecialFolder.LocalApplicationData, "NINA", "Profiles", $"{Id}.profile")`; `Save()` uses journal → backup → final three-file write for crash safety.
- **Status:** OK

## [19] NINA — `NINA.Profile/Interfaces/IProfileService.cs` (develop branch)

- **URL:** https://github.com/isbeorn/nina/blob/develop/NINA.Profile/Interfaces/IProfileService.cs
- **Tier:** 1
- **Extracted:** `IProfile ActiveProfile { get; }`, `event EventHandler ProfileChanged`, profile lifecycle methods. Plugins must subscribe to `ProfileChanged` to re-raise property changed events when the active profile switches.
- **Status:** OK

## [20] NINA — `NINA.Core/Utility/CoreUtil.cs` (develop branch)

- **URL:** https://github.com/isbeorn/nina/blob/develop/NINA.Core/Utility/CoreUtil.cs
- **Tier:** 1
- **Extracted:** `APPLICATIONTEMPPATH = Path.Combine(Environment.SpecialFolder.LocalApplicationData, "NINA")`; `DirectoryCleanup()` implements 90-day retention used by Logger [10]; `GetNearestAvailablePort(int port)` helper referenced by embedded HTTP servers [31][32][33].
- **Status:** OK

## [21] NINA — `NINA.Core/Utility/BaseINPC.cs` (develop branch)

- **URL:** https://github.com/isbeorn/nina/blob/develop/NINA.Core/Utility/BaseINPC.cs
- **Tier:** 1
- **Extracted:** `public abstract class BaseINPC : CommunityToolkit.Mvvm.ComponentModel.ObservableObject` — extends the CommunityToolkit base. Adds `RaisePropertyChanged([CallerMemberName])` helper and collection-change helpers.
- **Status:** OK

## [22] NINA — `NINA.Core/Utility/RelayCommand.cs` (develop branch)

- **URL:** https://github.com/isbeorn/nina/blob/develop/NINA.Core/Utility/RelayCommand.cs
- **Tier:** 1
- **Extracted:** Class is decorated `[Obsolete("Use CommunityToolkit.Mvvm.Input.RelayCommand instead...")]`. The MVVMLight GalaSoft `NINA.WPF.Base.Utility.MVVMLight.RelayCommand` also exists but is superseded. New plugin code must use `CommunityToolkit.Mvvm.Input.RelayCommand` and `AsyncRelayCommand`.
- **Status:** OK

## [23] NINA — `NINA/ViewModel/Plugins/PluginOptionsDataTemplateSelector.cs` (develop branch)

- **URL:** https://github.com/isbeorn/nina/blob/develop/NINA/ViewModel/Plugins/PluginOptionsDataTemplateSelector.cs
- **Tier:** 1
- **Extracted:** `SelectTemplate(object item, ...)` does keyed lookup `Application.Current.Resources[plugin.Name + DataTemplatePostfix.Options]` where `plugin.Name` is `IPluginManifest.Name`. No file scanning; the ResourceDictionary must have been imported by MEF (see [7]).
- **Status:** OK

## [24] NINA — `NINA.WPF.Base/Utility/DataTemplatePostfix.cs` (develop branch)

- **URL:** https://github.com/isbeorn/nina/blob/develop/NINA.WPF.Base/Utility/DataTemplatePostfix.cs
- **Tier:** 1
- **Extracted:** Constant `public const string Options = "_Options";` (plus `_Mini`, `_Dockable`, device-settings postfixes referenced by [1]).
- **Status:** OK

## [25] NINA Plugin Manifest Repository — README

- **URL:** https://github.com/isbeorn/nina.plugin.manifests/blob/master/README.md (Bitbucket mirror at https://bitbucket.org/Isbeorn/nina.plugin.manifests is the canonical PR target — Bitbucket free-tier no longer supports downloads section)
- **Tier:** 1
- **Extracted:** Submission workflow (six steps: prerequisites, develop, generate, validate, PR, await review). Licensing: must be open source (MIT, BSD-3-Clause, MPL-2.0); closed source rejected. Manifest generation methods: GitHub Actions (`./tools/github-action.yml` triggers on tag push, requires "Read and write permissions"), Bitbucket Pipelines (paid plan only), or `CreateManifest.ps1` (PowerShell 7) parameters `-file`, `-installerUrl`, `-createArchive`, `-archiveName`, `-uploadToBitbucket`, `-beta`. Critical warning: "Make sure that your DLL will not be recompiled or changed after the manifest is created, as the checksum will change each time!" **Manifest schema required fields:** `Name`, `Identifier` (GUID, constant across versions), `Author`, `License`, `LicenseURL`, `Repository`, `Version` (object `{Major,Minor,Patch,Build}`), `MinimumApplicationVersion` (same object shape), `Installer.URL`, `Installer.Type` (enum `DLL` or `ARCHIVE`), `Installer.Checksum`, `Installer.ChecksumType` (enum `MD5` | `SHA1` | `SHA256`), `Descriptions.ShortDescription`. **Optional:** `ChangelogURL`, `Tags` (array of strings), `Homepage`, `Descriptions.LongDescription`, `Descriptions.FeaturedImageURL`, `Descriptions.ScreenshotURL`, `Descriptions.AltScreenshotURL`, `Channel` (set to `"Beta"` for beta channel; omit for stable). Folder structure: `manifests\<first-letter><plugin-name>\<nina-version>\<plugin-version>\manifest.json`. Validation: `npm install` then `node gather.js`. Beta opt-in URL `https://nighttime-imaging.eu/wp-json/nina/v1/beta`.
- **Status:** OK

## [26] daleghent — `nina-influxdb-exporter/InfluxDB Exporter.csproj`

- **URL:** https://github.com/daleghent/nina-influxdb-exporter/blob/main/InfluxDB%20Exporter.csproj
- **Tier:** 2 (established community plugin by NINA contributor)
- **Extracted:** TargetFramework `net8.0-windows`; OutputType class library; UseWPF enabled. PackageReferences: `InfluxDB.Client 4.18.0`, `NINA.Plugin 3.1.2.9001`. **No direct references to NINA.Core / NINA.Equipment / etc.** — those come transitively through NINA.Plugin. **Post-build target** creates `%localappdata%\NINA\Plugins\3.0.0\` (3-segment subfolder) if absent and copies compiled assembly plus seven supporting DLLs (InfluxDB client libraries, JSON, reactive extensions, CSV, time, REST client). Confirms the per-`<api-version>` folder is named with **three segments** (`3.0.0`), not four (`3.0.0.9001`).
- **Status:** OK

## [27] daleghent — `nina-influxdb-exporter/InfluxDbExporter.cs`

- **URL:** https://github.com/daleghent/nina-influxdb-exporter/blob/main/InfluxDbExporter.cs
- **Tier:** 2
- **Extracted:** Inherits `PluginBase`; `[Export(typeof(IPluginManifest))]`. `[ImportingConstructor]` accepts 12 mediator dependencies: camera, image save, filter wheel, flat device, guider, dome, rotator, telescope, safety monitor, weather data, focuser, switch. Lazy `??=` init pattern for stream collectors. `Initialize()` performs auth check and starts background `MiscData.Run()` via `Task.Run` with a `CancellationToken`. `Teardown()` signals cancellation, deregisters handlers, disposes data stream objects, calls `base.Teardown()`. Maintains 13 public properties for per-equipment stream collectors.
- **Status:** OK

## [28] daleghent — `nina-influxdb-exporter/Properties/AssemblyInfo.cs`

- **URL:** https://github.com/daleghent/nina-influxdb-exporter/blob/main/Properties/AssemblyInfo.cs
- **Tier:** 2
- **Extracted:** `[Guid("3f820a89-a858-47f2-a56d-4e2b296f2364")]`, `[AssemblyVersion("1.1.0.900")]`, `[AssemblyTitle(...)]` short description in title, `[AssemblyCompany("Dale Ghent")]`, `[AssemblyCopyright("2022-2025")]`, `[AssemblyMetadata("License", "MPL-2.0")]`, `[AssemblyMetadata("MinimumApplicationVersion", "3.2.0.1000")]` (note: matches NINA.Plugin NuGet version, **not** the install-subfolder `3.0.0`), `[AssemblyMetadata("Repository", "https://github.com/daleghent/nina-influxdb-exporter")]`, `[AssemblyMetadata("Homepage", "https://daleghent.com/influxdb-exporter")]`, `[AssemblyMetadata("ChangelogURL", "...")]`, `[AssemblyMetadata("Tags", "influx, influxdb")]`, `[AssemblyMetadata("FeaturedImageURL", "https://daleghent.github.io/nina-plugins/assets/images/influxdb-logo.png")]`.
- **Status:** OK

## [29] daleghent — `nina-astro-physics-tools/AstroPhysicsToolsOptions.cs`

- **URL:** https://github.com/daleghent/nina-astro-physics-tools/blob/main/AstroPhysicsToolsOptions.cs
- **Tier:** 2
- **Extracted:** Canonical real-world `IPluginOptionsAccessor` consumer. Constructor calls `PluginOptionsAccessor.GetAssemblyGuid(typeof(AstroPhysicsToolsOptions))` and throws `Exception("GUID was not found in assembly metadata")` if null. Subscribes to `profileService.ProfileChanged` and calls `RaiseAllPropertiesChanged()` on change to re-read all settings for the new active profile. Uses `nameof(PropertyName)` as the setting key in `GetValueBoolean(nameof(X), defaultValue)` / `SetValueBoolean(nameof(X), value)` to avoid magic strings.
- **Status:** OK

## [30] christian-photo — `ninaAPI/ninaAPI.csproj`

- **URL:** https://github.com/christian-photo/ninaAPI/blob/main/ninaAPI/ninaAPI.csproj
- **Tier:** 2
- **Extracted:** TargetFramework `net8.0-windows`. PackageReferences (Windows build) include NINA suite at 3.2.0.9001 (Astrometry, Core, CustomControlLibrary, Equipment, Image, MGEN, PlateSolving, Profile, Sequencer, WPF.Base), `NINA.Plugin 3.2.0.9001`, `Dirkster.AvalonDock 4.60.0`, `NINA.WpfToolkit 3.5.3`, `System.Windows.Interactivity.WPF 2.0.20525`, `Microsoft.Windows.Compatibility 6.0.1`, `EmbedIO 3.5.2`, `System.Data.DataSetExtensions 4.5.0`. Conditional Linux build (`net10.0`) uses local ProjectReferences excluding XAML pages. **Post-build target xcopy's assembly to `%localappdata%\NINA\Plugins\3.0.0\Advanced API\`.** Note: this plugin explicitly references all NINA assemblies directly, contrary to the template README [1] recommendation to remove all PackageReferences and rely on `NINA.Plugin` transitively.
- **Status:** OK

## [31] christian-photo — `ninaAPI/AdvancedAPI.cs`

- **URL:** https://github.com/christian-photo/ninaAPI/blob/main/ninaAPI/AdvancedAPI.cs
- **Tier:** 2
- **Extracted:** Inherits `PluginBase` and implements `INotifyPropertyChanged` manually; `[Export(typeof(IPluginManifest))]`. `[ImportingConstructor]` accepts 25+ mediators (camera, telescope, focuser, etc.) and stuffs them into a static `NINAControls` aggregator object. Server lifecycle: conditional `API` server start in `Initialize`, `API.StartWatchers()`. `Teardown()` calls `Server?.Stop()`, `API.StopWatchers()`, disposes communicator, removes temp thumbnail/image files with retry. Properties: `Port`, `APIEnabled`, `CachedPort`, `PortVisibility`.
- **Status:** OK

## [32] christian-photo — `ninaAPI/WebService/API.cs`

- **URL:** https://github.com/christian-photo/ninaAPI/blob/main/ninaAPI/WebService/API.cs
- **Tier:** 2
- **Extracted:** `new WebServer(o => o.WithUrlPrefix($"http://*:{Port}").WithMode(HttpListenerMode.EmbedIO))`. Dedicated named `Thread("API Thread")` runs `APITask()` which creates a `CancellationTokenSource` and calls `server.RunAsync(apiToken.Token).Wait()` (blocks dedicated thread for server lifetime; calling thread not blocked). Stop is `apiToken.Cancel()` which propagates to listener and unblocks `.Wait()`.
- **Status:** OK

## [33] Touch-N-Stars — `TouchNStarsServer.cs`

- **URL:** https://github.com/Touch-N-Stars/N.I.N.A-Plugin-for-Touch-N-Stars/blob/main/Touch-N-Stars/Server/TouchNStarsServer.cs
- **Tier:** 2
- **Extracted:** Same pattern as [32]: `http://*:{port}` prefix, `HttpListenerMode.EmbedIO`, named thread runs `RunAsync().Wait()`, `Cancel()` stops. Confirms EmbedIO+named-thread pattern is the de-facto idiom across NINA plugins.
- **Status:** OK

## [34] EmbedIO — `WebServer.cs` mode selection

- **URL:** https://github.com/unosquare/embedio/blob/master/src/EmbedIO/WebServer.cs
- **Tier:** 1
- **Extracted:** Factory method switches on `HttpListenerMode`: `Microsoft` → `new SystemHttpListener(new System.Net.HttpListener())` (wraps http.sys); any other value (including `EmbedIO`) → `new EmbedIO.Net.HttpListener(Options.Certificate)`. `ProcessRequestsAsync` loops `while (!cancellationToken.IsCancellationRequested && (Listener?.IsListening ?? false))`.
- **Status:** OK

## [35] EmbedIO — `EndPointListener.cs` raw socket impl

- **URL:** https://github.com/unosquare/embedio/blob/master/src/EmbedIO/Net/Internal/EndPointListener.cs
- **Tier:** 1
- **Extracted:** `new Socket(SocketType.Stream, ProtocolType.Tcp)`, `Bind(IPEndPoint)`, `Listen(500)`, accepts via `SocketAsyncEventArgs`. Confirms `HttpListenerMode.EmbedIO` is a fully managed TCP socket implementation — no http.sys, no URL ACL, no netsh, no admin requirement for ports >1023.
- **Status:** OK

## [36] EmbedIO NuGet Gallery

- **URL:** https://www.nuget.org/packages/EmbedIO/
- **Tier:** 1
- **Extracted:** Package ID `EmbedIO` (not `Unosquare.EmbedIO` which was v2.x). Latest stable `3.5.2` (published 2022-10-31). Targets `.NETStandard 2.0`. Author Unosquare. 2.8M total downloads. No separate package for managed-socket mode — bundled in single package.
- **Status:** OK

## [37] Microsoft Learn — HttpListenerException Access denied

- **URL:** https://learn.microsoft.com/en-us/answers/questions/2275519/system-net-httplistenerexception-(5)-access-is-den
- **Tier:** 1
- **Extracted:** `HttpListener.Start()` without admin or pre-existing `netsh http add urlacl` produces `System.Net.HttpListenerException (5): Access is denied`. Error code 5 is Win32 `ERROR_ACCESS_DENIED`. `http://localhost:PORT/` is exempted from the ACL check; wildcards (`http://+:PORT/` or `http://*:PORT/`) always require admin or pre-registered urlacl.
- **Status:** OK

## [38] Grapevine docs — netsh urlacl syntax

- **URL:** https://scottoffen.github.io/grapevine-legacy/en/using-httplistener.html
- **Tier:** 3
- **Extracted:** `netsh http add urlacl url=http://+:1234/ user=DOMAIN\user` command syntax; "exact match" requirement for the registered URL prefix vs. the listener's prefix.
- **Status:** OK

## [39] NuGet Gallery — `NINA.Plugin`

- **URL:** https://www.nuget.org/packages/NINA.Plugin/
- **Tier:** 1
- **Extracted:** Current stable version `3.2.0.9001`; "9001" build number designates stable, distinguishing from nightly (`1xxx`), beta (`2xxx`), RC (`3xxx`). Target `.NET 8.0` (Windows). Transitive dependencies bring `NINA.Astrometry`, `NINA.Core`, `NINA.Equipment`, `NINA.Image`, `NINA.PlateSolving`, `NINA.Profile`, `NINA.Sequencer`, `NINA.WPF.Base` (all at matching 3.2.0.9001). Newer prerelease versions exist for develop-branch nightlies.
- **Status:** OK

## [40] NuGet Gallery — `NINA.Core`

- **URL:** https://www.nuget.org/packages/NINA.Core/
- **Tier:** 1
- **Extracted:** Confirms `CommunityToolkit.Mvvm >= 8.2.2` (8.4.0 in develop per [11]) is a transitive dependency. So `CommunityToolkit.Mvvm` ships with NINA at runtime and must NOT be copied into the plugin output folder.
- **Status:** OK

## [41] NINA 3.0.0.9001 RELEASE_NOTES

- **URL:** https://f002.backblazeb2.com/file/ninasetup/Releases/3.0.0.9001/RELEASE_NOTES.html
- **Tier:** 1 (official release artifact hosted on NINA's Backblaze)
- **Extracted:** "plugin folder in `%localappdata%\NINA\Plugins` now contains a subfolder with the Major.Minor.Revision version of the application" — confirms the install path's `<api-version>` segment is **three-part** (e.g., `3.0.0`), **not** four-part (`3.0.0.9001`).
- **Status:** OK

## [42] NINA CONTRIBUTING.md (develop branch)

- **URL:** https://github.com/isbeorn/nina/blob/develop/CONTRIBUTING.md
- **Tier:** 1
- **Extracted:** "The NINA project uses the NUnit unit-testing framework to write and run automated unit tests, and additionally uses Fluent Assertions to write easy to read assertions." Test run command: `dotnet test NINA.Test/NINA.Test.csproj --configuration Debug --no-build -p:PlatformTarget=x64`. NINA core itself uses NUnit + FluentAssertions; this is the application-level convention, not necessarily plugins.
- **Status:** OK

## [43] CommunityToolkit.Mvvm — `[ObservableProperty]` docs

- **URL:** https://learn.microsoft.com/en-us/dotnet/communitytoolkit/mvvm/generators/observableproperty
- **Tier:** 1
- **Extracted:** Generated properties are `public` with standard getter/setter — not `virtual`, so Moq cannot mock them on concrete types. Requires class to be `partial`. C# 12+ supports `partial` property syntax eliminating backing field. `OnPropertyNameChanged` and `OnPropertyNameChanging` partial method hooks available.
- **Status:** OK

## [44] CommunityToolkit.Mvvm — ObservableObject docs

- **URL:** https://learn.microsoft.com/en-us/dotnet/communitytoolkit/mvvm/observableobject
- **Tier:** 1
- **Extracted:** Base class for `INotifyPropertyChanged` types; required parent for `[ObservableProperty]` source generator. NINA's `BaseINPC` [21] derives from this.
- **Status:** OK

## [45] Microsoft Learn — InternalsVisibleToAttribute

- **URL:** https://learn.microsoft.com/en-us/dotnet/api/system.runtime.compilerservices.internalsvisibletoattribute
- **Tier:** 1
- **Extracted:** SDK-style csproj pattern: `<InternalsVisibleTo Include="MyPlugin.Tests" />` inside `<ItemGroup>`. Strong-named assemblies require full public key in the value. For unsigned plugin assemblies (the NINA norm), name-only is sufficient.
- **Status:** OK

## [46] Xunit.StaFact (AArnott)

- **URL:** https://github.com/AArnott/Xunit.StaFact
- **Tier:** 2
- **Extracted:** Provides `[WpfFact]`, `[StaFact]`, cross-platform `[UIFact]` to run tests on STA thread. Required when tests touch WPF types like `Dispatcher.CurrentDispatcher` or `ObservableCollection<T>` mutation.
- **Status:** OK

## [47] NUnit issue #4565 — net8.0-windows + win-x64

- **URL:** https://github.com/nunit/nunit/issues/4565
- **Tier:** 2
- **Extracted:** Known incompatibility between bare `net8.0-windows` + `win-x64` RID. Workaround: pin to `net8.0-windows10.0.22621.0` or extract non-UI logic into `net8.0`-targeting library.
- **Status:** OK

## [48] Rick Strahl — Async and Async-Void Event Handling in WPF (2022)

- **URL:** https://weblog.west-wind.com/posts/2022/Apr/22/Async-and-Async-Void-Event-Handling-in-WPF
- **Tier:** 2
- **Extracted:** Wrapping event handler body in `await Dispatcher.InvokeAsync(...)` resolves event hang-up issues. `async void` is acceptable only for top-level delegate-typed event handlers; unhandled exceptions propagate to UI `SynchronizationContext` and crash unless `Application.DispatcherUnhandledException` is wired up. Best practice: wrap async void handler body in try/catch with `Logger.Error(ex, ...)`.
- **Status:** OK

## [49] dotnet/wpf issue #2885 — Nullable annotations

- **URL:** https://github.com/dotnet/wpf/issues/2885
- **Tier:** 1
- **Extracted:** WPF framework APIs lack comprehensive `#nullable` annotations as of .NET 8. Enabling `<Nullable>enable</Nullable>` produces warnings against correct code in plugin XAML code-behind, IValueConverter implementations, ICommand parameters. Pragmatic recommendation: enable project-wide but `#nullable disable` per-file where WPF-binding boilerplate creates noise.
- **Status:** OK

## [50] C# 10 spec — File-scoped namespaces

- **URL:** https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/proposals/csharp-10.0/file-scoped-namespaces
- **Tier:** 1
- **Extracted:** Constraint: exactly one file-scoped namespace per file; cannot mix with block-scoped; `using` directives precede the namespace declaration. Default in .NET 6+ project templates via `csharp_style_namespace_declarations = file_scoped`.
- **Status:** OK

## [51] C# 12 spec — Primary constructors

- **URL:** https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/proposals/csharp-12.0/primary-constructors
- **Tier:** 1
- **Extracted:** Primary-constructor parameters scope across the entire class body. Attributes on the synthesized constructor use the `method:` target: `[method: ImportingConstructor]`. Per-parameter `[Import(...)]` attribute annotation in the parameter list is **not supported** — if per-parameter MEF customization is required, an explicit `[ImportingConstructor]` constructor is required.
- **Status:** OK

## [52] Microsoft Learn — Primary constructor tutorial

- **URL:** https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/tutorials/primary-constructors
- **Tier:** 1
- **Extracted:** Confirms `[method: AttributeName]` syntax for attributing the synthesized constructor method. WPF data binding inspects public properties, not constructors, so primary constructors have no impact on binding behavior.
- **Status:** OK

## [53] MEF Attributed Programming Model (Microsoft Learn)

- **URL:** https://learn.microsoft.com/en-us/dotnet/framework/mef/attributed-programming-model-overview-mef
- **Tier:** 1
- **Extracted:** `[ImportingConstructor]` may appear at most once per class. Default `[Export]` creation policy is `CreationPolicy.Shared` (singleton per container) unless explicit `[PartCreationPolicy]` overrides.
- **Status:** OK

## [54] Microsoft Premier Developer — CancellationToken patterns

- **URL:** https://devblogs.microsoft.com/premier-developer/recommended-patterns-for-cancellationtoken/
- **Tier:** 1
- **Extracted:** `CancellationToken` as the last parameter of every async method (unless followed by `IProgress<T>`). Inner async calls propagate `OperationCanceledException` naturally; explicit `ThrowIfCancellationRequested()` only at boundaries where no inner async call exists.
- **Status:** OK

## [55] C# spec — `using` declarations and statements

- **URL:** https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/using
- **Tier:** 1
- **Extracted:** `using var x = ...;` disposes at end of enclosing scope; `using (...) { }` block scopes disposal explicitly. Both compile to `try/finally` ensuring dispose on early return / exception.
- **Status:** OK

## [56] daleghent — `nina-ground-station/GroundStation.cs`

- **URL:** https://github.com/daleghent/nina-ground-station/blob/main/GroundStation.cs
- **Tier:** 2
- **Extracted:** `PluginBase` subclass; `async Task Initialize()` / `async Task Teardown()` overrides confirming the lifecycle hook signature. Subscribes to safety monitor, weather, dome mediator events in Initialize; unsubscribes in Teardown.
- **Status:** OK

## [57] daleghent — NINA fork RELEASE_NOTES (develop branch)

- **URL:** https://github.com/daleghent/nina/blob/develop/RELEASE_NOTES.md
- **Tier:** 2 (mirror of upstream releases)
- **Extracted:** "Device mediators have been enhanced with numerous new events that subscribers can monitor following an action performed by the device (e.g., mount slewing, cover opening, etc.)." — historical confirmation of per-action events introduced in NINA 3.x.
- **Status:** OK

## [58] photon1503 — NINA-Log-Report regex

- **URL:** https://github.com/photon1503/NINA-Log-Report
- **Tier:** 3
- **Extracted:** Python parser regex confirms log line format `Timestamp|Level|...` matching the Serilog template in [10]. Default log path `%localappdata%/NINA/Logs`.
- **Status:** OK

## [59] tcpalmer — Target Scheduler Technical Details

- **URL:** https://tcpalmer.github.io/nina-scheduler/technical-details.html
- **Tier:** 2
- **Extracted:** "set the log level (trace, debug, info, warning, error) similar to the main NINA log"; "Like the main NINA logs ... will also be purged after 90 days" (confirming 90-day retention applies to main log too). Documents plugin pattern of maintaining a separate plugin-specific log file in `%localappdata%\NINA\<PluginName>\Logs\` with a custom prefix (e.g., `TS-`).
- **Status:** OK

## [60] NINA — `NINA.WPF.Base/Resources/Styles/TextBlock.xaml` (develop branch)

- **URL:** https://github.com/isbeorn/nina/blob/develop/NINA.WPF.Base/Resources/Styles/TextBlock.xaml
- **Tier:** 1
- **Extracted:** Themed TextBlock style keys available to plugins via `{StaticResource ...}`: `StandardTextBlock`, `SideBarTextBlock`, `TabItemTextBox`, `TextBlockWithMouseOver`, `WindowButtonTextBlock`. There is no `BorderedTextBlock` style key in this file.
- **Status:** OK

## [61] NINA — `NINA.WPF.Base/Resources/Styles/Button.xaml` (develop branch)

- **URL:** https://github.com/isbeorn/nina/blob/develop/NINA.WPF.Base/Resources/Styles/Button.xaml
- **Tier:** 1
- **Extracted:** Themed Button style keys: `StandardButton`, `BackgroundButton` (and others).
- **Status:** OK

## [62] NINA — `NINA.WPF.Base/Resources/StaticResources/Brushes.xaml` (develop branch)

- **URL:** https://github.com/isbeorn/nina/blob/develop/NINA.WPF.Base/Resources/StaticResources/Brushes.xaml
- **Tier:** 1
- **Extracted:** Brush resource keys: `PrimaryBrush`, `SecondaryBrush`, `BorderBrush`, `ButtonBackgroundBrush`, `ButtonBackgroundSelectedBrush`, `ButtonForegroundBrush`, `ButtonForegroundDisabledBrush`, `BackgroundBrush`, `SecondaryBackgroundBrush`, `TertiaryBackgroundBrush`, `NotificationWarningBrush`, `NotificationErrorBrush`. Values bind dynamically through `{StaticResource ProfileService}` so they respond to NINA's profile-driven theme.
- **Status:** OK

## [63] EmbedIO issue #459 — wildcard binding bug

- **URL:** https://github.com/unosquare/embedio/issues/459
- **Tier:** 1
- **Extracted:** With `HttpListenerMode.EmbedIO`, the wildcard prefix `http://*:port` and `http://+:port` does not correctly route requests to every IPv4 address in some configurations. Workaround is to enumerate explicit prefixes. Labeled wontfix. Both ninaAPI [32] and Touch-N-Stars [33] use the wildcard pattern regardless, accepting the edge case.
- **Status:** OK

---

**Source quality summary:** 41 Tier-1, 17 Tier-2, 3 Tier-3, 0 Tier-4 (total 63 citations after audit-driven additions). The standards doc is grounded almost entirely in official NINA source code (develop branch of `isbeorn/nina`), the official plugin template, and the manifest repository README — with established community plugins providing real-world validation of idioms.
