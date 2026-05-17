# MEF and IPluginManifest

Dimension covers: `[Export(typeof(IPluginManifest))]`, `[ImportingConstructor]`, `IPluginManifest` interface, `PluginBase`, lifecycle (Initialize/Teardown), part lifetime.

See [citations](../citations.md).

## Required MEF attributes

The plugin's main class must carry `[Export(typeof(IPluginManifest))]` [2], [27], [31]. Per [1]: "Mandatory to be exported once!" Exactly one class per plugin assembly exports this contract.

Any plugin XAML `ResourceDictionary` (Options, Mini, Dockable, *Settings) must also carry `[Export(typeof(ResourceDictionary))]` on the code-behind partial class so that `PluginLoader` can merge it into `Application.Current.Resources.MergedDictionaries` [5], [7].

Additional per-feature exports go on their respective implementation classes — not on the manifest class:
- `[Export(typeof(ISequenceItem))]` — sequencer instruction
- `[Export(typeof(ISequenceTrigger))]` — trigger
- `[Export(typeof(ISequenceCondition))]` — condition
- `[Export(typeof(ISequenceContainer))]` — instruction set
- `[Export(typeof(IDockableVM))]` — dockable imaging-tab panel
- `[Export(typeof(IPluggableBehavior))]` — IStarDetection / IStarAnnotator / IAutoFocusVMFactory swap-ins
- `[Export(typeof(IEquipmentProvider))]` — custom device drivers (implementation inherits `IEquipmentProvider<TDevice>`)

Source: [1].

## `[ImportingConstructor]` and injected services

The constructor on the exported plugin class (and on each sequence entity) is decorated `[ImportingConstructor]` [2], [27], [31]. Per MEF rules [53]: at most one `[ImportingConstructor]` per class.

Per [1], the full list of injectable interfaces a plugin entity may receive:

```
IProfileService                 ICameraMediator             ITelescopeMediator
IFocuserMediator                IFilterWheelMediator        IGuiderMediator
IRotatorMediator                IFlatDeviceMediator         IWeatherDataMediator
IDomeMediator                   ISwitchMediator             ISafetyMonitorMediator
IImagingMediator                IApplicationStatusMediator  INighttimeCalculator
IPlanetariumFactory             IImageHistoryVM             IDeepSkyObjectSearchVM
IImageSaveMediator              IApplicationMediator        IApplicationResourceDictionary
IFramingAssistantVM             IList<IDateTimeProvider>    IPlateSolverFactory
IWindowServiceFactory           IDomeFollower
IPluggableBehaviorSelector<IStarDetection>
IPluggableBehaviorSelector<IStarAnnotator>
IImageDataFactory               IMeridianFlipVMFactory      IAutoFocusVMFactory
IImageControlVM                 IImageStatisticsVM          IDomeSynchronization
ISequenceMediator               IOptionsVM                  IExposureDataFactory
```

Per [1], `ISequenceMediator` carries an important caveat: "**Must be initialized first before you can use it which is after all plugins are loaded!**" — plugins must not access it in `[ImportingConstructor]` body; defer until `Initialize()`.

The template plugin [2] injects three services: `IProfileService, IOptionsVM, IImageSaveMediator`. The InfluxDB exporter [27] injects 12 mediators. The ninaAPI plugin [31] injects 25+. There is no hard cap.

## PluginBase abstract class

`NINA.Plugin.PluginBase` [8] implements `IPluginManifest` [9] and auto-populates all manifest properties from assembly attributes (see [assembly-metadata](assembly-metadata.md)). Inheritance pattern (verified across template [2], InfluxDB exporter [27], ninaAPI [31], Ground Station [56]):

```csharp
[Export(typeof(IPluginManifest))]
public class MyPlugin : PluginBase, INotifyPropertyChanged {
    [ImportingConstructor]
    public MyPlugin(IProfileService profileService, /* other mediators */) {
        // store refs, subscribe to events, register consumers
    }

    public override Task Teardown() {
        // unsubscribe events, unregister consumers, dispose state
        return base.Teardown();
    }
}
```

Note that `PluginBase` does **not** implement `IDisposable` [8] — cleanup is via the `Teardown()` override only.

`PluginBase` does **not** extend `BaseINPC` (verified by the template implementing `INotifyPropertyChanged` manually with `[CallerMemberName]` [2]). Plugins that want the `RaisePropertyChanged()` helper either implement INPC inline like the template, derive a separate ViewModel from `BaseINPC` [21], or directly inherit `CommunityToolkit.Mvvm.ComponentModel.ObservableObject` [44].

## IPluginManifest interface

Per [9]: properties `Identifier`, `Name`, `License`, `LicenseURL`, `Author`, `Homepage`, `Repository`, `ChangelogURL`, `Tags` (string[]), `Version` (IPluginVersion), `MinimumApplicationVersion` (IPluginVersion), `Installer` (IPluginInstallerDetails), `Descriptions` (IPluginDescription). Methods: `Task Initialize()`, `Task Teardown()`.

So `Initialize` and `Teardown` are part of the **interface contract**, not just helpers on the base class. `PluginBase` [8] provides virtual `async Task` implementations that return `Task.CompletedTask`; plugins override one or both.

`Version` and `MinimumApplicationVersion` are structured `IPluginVersion` objects exposing `Major/Minor/Patch/Build` — same shape used in the manifest.json [25].

## Part lifetime

MEF default `CreationPolicy` is `Shared` (singleton per container) when no `[PartCreationPolicy]` is specified [53]. None of the inspected NINA plugin classes [2], [27], [31] declare an explicit part-creation policy — they rely on the default. Effect: a single instance of the manifest class lives for the lifetime of the NINA process, and that same instance is the DataContext of the Options DataTemplate (see [wpf-options-ui](wpf-options-ui.md)).

Sequencer entities (`ISequenceItem`, `ISequenceTrigger`, etc.) need new instances per drag-into-sequence operation; whether they declare `NonShared` policy explicitly or rely on factory-style construction internally was not directly verified in the sources fetched.

## Plugin discovery and loading

Per `PluginLoader.cs` [7]:
1. Enumerate `*.dll` 1 level deep from `Constants.UserExtensionsFolder` (the `%LOCALAPPDATA%\NINA\Plugins\<api-version>\` tree).
2. For each candidate, create a dedicated `AssemblyLoadContext` for plugin isolation.
3. Compose two MEF catalogs: (a) core — sequencer types and equipment SDKs via `TypeCatalog`; (b) plugin — assembly's MEF parts.
4. Merge each plugin's exported `ResourceDictionary` into `Application.Current.Resources.MergedDictionaries`.
5. Non-plugin DLLs are silently skipped with trace-level logging.
6. `ReflectionTypeLoadException` is caught, `LoaderExceptions` aggregated into one error; failed plugins register with completion=false.
7. When manifest construction fails, the loader synthesizes a fallback `PluginManifest` from raw assembly attributes (`Guid`, `AssemblyCompany`, `AssemblyFileVersion`, `AssemblyTitle`).

The `AssemblyLoadContext` isolation [7] is the reason a plugin can bring its own newer third-party DLL without crashing NINA — but it also means types from the plugin context are not assignment-compatible with types from NINA's default context unless they come from a shared reference assembly.

## Gaps and limitations

- Whether a single class can carry both `[Export(typeof(IPluginManifest))]` and `[Export(typeof(IDockableVM))]` is technically legal under MEF rules but not idiomatic in NINA plugins; all observed plugins keep them on separate classes.
- The order of `IPluginManifest.Initialize()` calls relative to equipment device initialization was not directly verified — `ISequenceMediator` caveat in [1] is the closest constraint we have ("after all plugins are loaded").
