# WPF Options UI

Dimension covers: DataTemplate `<IPluginManifest.Name>_Options` convention, ResourceDictionary export, NINA-themed styles, RelayCommand choice, MVVM base classes.

See [citations](../citations.md).

## DataTemplate naming convention

NINA renders the per-plugin Options panel by looking up `Application.Current.Resources[plugin.Name + "_Options"]` where `plugin.Name` is `IPluginManifest.Name` and `"_Options"` is the `DataTemplatePostfix.Options` constant [23], [24].

`plugin.Name` is auto-populated from `[AssemblyTitle]` via `PluginBase` [8]. So the practical rule is:

> Set `[assembly: AssemblyTitle("MyPlugin")]` in `AssemblyInfo.cs`, then make the DataTemplate `x:Key="MyPlugin_Options"`.

The template [4] uses `x:Key="$pluginname$_Options"` (the VSIX wizard substitutes `$pluginname$` with the chosen plugin name).

There is no `DataType` on the DataTemplate — keyed lookup is sufficient. There is no need to declare `MergedDictionaries` in the plugin's own ResourceDictionary — see below.

Additional DataTemplate postfixes documented in [1] (constants live in `NINA.WPF.Base.Utility.DataTemplatePostfix` [24]):

| Postfix | Key form | Purpose |
|---|---|---|
| `_Options` | `<IPluginManifest.Name>_Options` | Plugin global options panel |
| `_Mini` | `<FullyQualifiedSequenceItemTypeName>_Mini` | Compact view in imaging-tab sequencer |
| `_Dockable` | `<FullyQualifiedDockableVMTypeName>_Dockable` | Dockable imaging-tab panel |
| `_CameraSettings` (et al.) | `<FullyQualifiedDeviceTypeName>_<DeviceType>Settings` | Custom device-driver settings pane |

## ResourceDictionary export — the wiring step

`Options.xaml.cs` (the partial code-behind) [5]:

```csharp
[Export(typeof(ResourceDictionary))]
partial class Options : ResourceDictionary {
    public Options() { InitializeComponent(); }
}
```

PluginLoader collects every `[Export(typeof(ResourceDictionary))]` from the plugin assembly via MEF `[ImportMany]` and merges each into `Application.Current.Resources.MergedDictionaries` [7]. Forgetting the `[Export]` attribute is the most common cause of an empty Options panel — keyed lookup [23] finds nothing because the dictionary was never merged.

## DataContext of the Options DataTemplate

`PluginsView.xaml` (in NINA) sets the DataContext to the `IPluginManifest` instance itself, then uses `ContentControl Content="{Binding}"` with `ContentTemplateSelector="{StaticResource PluginOptionsDataTemplateSelector}"` [23].

Effect: inside the DataTemplate, `{Binding SomeProperty}` binds against the plugin's `PluginBase` subclass instance. The template [2] exposes `DefaultNotificationMessage` (backed by `Settings.Default`) and `ProfileSpecificNotificationMessage` (backed by `IPluginOptionsAccessor`) via public properties; the XAML [4] binds them with `{Binding ...}` directly.

## NINA-themed styles

NINA ships theme resources under `NINA.WPF.Base/Resources/Styles/` and brushes under `NINA.WPF.Base/Resources/StaticResources/`. These are merged into `Application.Current.Resources` at NINA startup, before any plugin loads — so plugins reference them via `{StaticResource ...}` without merging anything themselves.

Style keys verified in source:

| Resource | Type | Key | Source |
|---|---|---|---|
| Standard TextBlock | Style | `StandardTextBlock` | [60] |
| Sidebar TextBlock | Style | `SideBarTextBlock` | [60] |
| Tab Item TextBlock | Style | `TabItemTextBox` | [60] |
| Mouseover TextBlock | Style | `TextBlockWithMouseOver` | [60] |
| Window Button TextBlock | Style | `WindowButtonTextBlock` | [60] |
| Standard Button | Style | `StandardButton` | [61] |
| Background Button | Style | `BackgroundButton` | [61] |
| Primary brush | Brush | `PrimaryBrush` | [62] |
| Secondary brush | Brush | `SecondaryBrush` | [62] |
| Border brush | Brush | `BorderBrush` | [62] |
| Button background | Brush | `ButtonBackgroundBrush` | [62] |
| Button background selected | Brush | `ButtonBackgroundSelectedBrush` | [62] |
| Button foreground | Brush | `ButtonForegroundBrush` | [62] |
| Button foreground disabled | Brush | `ButtonForegroundDisabledBrush` | [62] |
| Background | Brush | `BackgroundBrush` | [62] |
| Secondary background | Brush | `SecondaryBackgroundBrush` | [62] |
| Tertiary background | Brush | `TertiaryBackgroundBrush` | [62] |
| Notification warning | Brush | `NotificationWarningBrush` | [62] |
| Notification error | Brush | `NotificationErrorBrush` | [62] |

Note: there is **no** `BorderedTextBlock` style — that term is sometimes assumed but does not exist in NINA's resources [60]. The correct approach is a `Border` wrapping a `TextBlock` styled with `StandardTextBlock`.

Brushes are dynamically resolved through `{StaticResource ProfileService}` so they respond to NINA's profile-driven theme.

## RelayCommand and MVVM base classes

NINA's own `NINA.Core.Utility.RelayCommand` is marked `[Obsolete("Use CommunityToolkit.Mvvm.Input.RelayCommand instead...")]` [22]. The MVVMLight `NINA.WPF.Base.Utility.MVVMLight.RelayCommand` is also legacy. **Plugins should use `CommunityToolkit.Mvvm.Input.RelayCommand` and `AsyncRelayCommand`** directly.

`CommunityToolkit.Mvvm 8.4.0` is a direct PackageReference of `NINA.Core` [11], so it ships with NINA at runtime — plugins do **not** copy the DLL into their bin folder (see [build-and-install](build-and-install.md)). Plugins should reference the package as a `<PackageReference Include="CommunityToolkit.Mvvm" Version="8.4.0" ExcludeAssets="runtime" />` so the compiler sees the types but no DLL is published.

MVVM base class hierarchy:

```
INotifyPropertyChanged                       (System)
   └─ ObservableObject                       (CommunityToolkit.Mvvm) [44]
        └─ BaseINPC                          (NINA.Core.Utility, abstract) [21]
```

`PluginBase` [8] does **not** derive from `BaseINPC` — observed by the template [2] implementing `INotifyPropertyChanged` manually. Options:

| Pattern | When to use |
|---|---|
| Implement `INotifyPropertyChanged` on the plugin class manually with `[CallerMemberName]` helper | What the template does [2]. Avoids extra NINA.Core type coupling. |
| Add a separate ViewModel inheriting `BaseINPC` and bind through it | If options UI grows complex and you want NINA's helpers |
| Use `CommunityToolkit.Mvvm.ComponentModel.ObservableObject` directly + `[ObservableProperty]` source generator | Cleanest .NET 8 idiom; requires `partial class` |

The `[ObservableProperty]` source generator [43] requires the containing class be `partial`. NINA itself uses this style (BaseINPC extends ObservableObject [21]).

## Common errors

1. Missing `[Export(typeof(ResourceDictionary))]` on `Options.xaml.cs` → empty options panel.
2. DataTemplate key not matching `AssemblyTitle` exactly (case, spacing, underscore) → empty options panel.
3. Adding `DataType="{x:Type local:MyPluginClass}"` instead of `x:Key="MyPluginClass_Options"` → keyed lookup misses; template never selected.
4. Merging NINA's resource dictionaries into the plugin's own dictionary → duplicate-key exceptions at app startup.
5. Referencing `NINA.Core.Utility.RelayCommand` (the obsolete one) → compiler warning; switch to `CommunityToolkit.Mvvm.Input.RelayCommand`.

## Gaps and limitations

- The complete list of `NINA.WPF.Base.Utility.DataTemplatePostfix` constants was not exhaustively fetched; only `Options`, `Mini`, `Dockable`, and `*Settings` were confirmed.
- Whether NINA explicitly guarantees all standard styles/brushes are merged before plugin load is implicit in the load sequence [7] but not stated as a contractual API.
