# Persisted Options — IPluginOptionsAccessor

Dimension covers: `IPluginOptionsAccessor` API surface, GUID extraction, profile scoping, profile-change handling, defaults, enum/color serialization.

See [citations](../citations.md).

## Construction

```csharp
public PluginOptionsAccessor(IProfileService profileService, Guid pluginGuid)
```

The `pluginGuid` is extracted via the static helper [16]:

```csharp
public static Guid? GetAssemblyGuid(Type type) {
    var guidAttributes = type.Assembly.GetCustomAttributes(typeof(GuidAttribute), false);
    if (guidAttributes == null || guidAttributes.Length != 1) { return null; }
    return Guid.Parse(((GuidAttribute)guidAttributes[0]).Value);
}
```

Returns `null` if the assembly has no `[Guid]` attribute OR more than one. Real-world plugins explicitly check and throw — [29]:

```csharp
var guid = PluginOptionsAccessor.GetAssemblyGuid(typeof(MyOptionsClass));
if (guid == null) throw new Exception("GUID was not found in assembly metadata");
this.optionsAccessor = new PluginOptionsAccessor(profileService, guid.Value);
```

The template [2] uses the simpler form `new PluginOptionsAccessor(profileService, Guid.Parse(this.Identifier))`, treating `IPluginManifest.Identifier` (which `PluginBase` already populated from `[Guid]` [8]) as the canonical source.

## API surface — typed getter/setter pairs

`IPluginOptionsAccessor` exposes typed methods for **16 primitive types** plus `Color` and generic enum support [16]:

| Method base | Backing type | Notes |
|---|---|---|
| `Boolean` | `bool` | |
| `Byte` | `byte` | |
| `SByte` | `sbyte` | |
| `Char` | `char` | |
| `Decimal` | `decimal` | |
| `Double` | `double` | |
| `Single` | `float` | **Method name uses CLS type — `GetValueSingle`, not `GetValueFloat`** |
| `Int32` | `int` | |
| `UInt32` | `uint` | |
| `Int64` | `long` | |
| `UInt64` | `ulong` | |
| `Int16` | `short` | |
| `UInt16` | `ushort` | |
| `String` | `string` | |
| `DateTime` | `DateTime` | |
| `Guid` | `Guid` | |
| `Color` | `System.Windows.Media.Color` | Stored as ARGB int via bit-shift [16] |
| `Enum<T>` | `T : struct, Enum` | Stored as string via `Enum.GetName`; parsed back via `Enum.TryParse<T>` [16] |

Signatures follow the pattern `T GetValueT(string name, T defaultValue)` and `void SetValueT(string name, T value)`. Defaults are returned when the key is missing **or** when the stored value's type does not match the requested type (no coercion). Source: [16].

## Profile scoping

Plugin options are **always per-profile** [16], [18]. Every getter/setter delegates to `profileService.ActiveProfile.PluginSettings`, an in-memory `Dictionary<Guid, IDictionary<string, object>>` where the outer key is the plugin GUID (namespacing by plugin) and the inner key is the user-supplied setting name. Two plugins using the same string key (e.g. `"Enabled"`) do not collide because their plugin GUIDs differ.

There is no documented global (non-profile) plugin option store. Plugins that need cross-profile settings have to fall back to `Settings.Default` (`ApplicationSettingsBase`) — the template [2] uses both: `Settings.Default.DefaultNotificationMessage` for global, `pluginSettings.GetValueString(...)` for per-profile.

## Storage backing

The active profile's `PluginSettings` is `[DataMember]` of `Profile` [18], serialized as XML by `DataContractSerializer`. Profile files live at:

```
%LOCALAPPDATA%\NINA\Profiles\<profile-guid>.profile
```

derived from `Environment.SpecialFolder.LocalApplicationData + "NINA" + "Profiles"` per `CoreUtil.APPLICATIONTEMPPATH` [20].

`Profile.Save()` uses a journal → backup → final three-file write pattern for crash safety [18].

## Save semantics

`SetValue*` updates the in-memory `pluginStorage` dictionary and raises `INotifyPropertyChanged` to mark the profile dirty [16]. The actual disk flush happens when the profile service decides to save (e.g., profile switch, application exit). Plugins do **not** call `Save()` explicitly per set.

## Enum serialization caveat

Enums are stored as strings via `Enum.GetName(typeof(T), value)` and parsed via `Enum.TryParse<T>(stringValue, out T result)` [16]. Consequences:

- Renaming an enum member after a plugin release breaks deserialization of stored values for users on older profiles — they will fall back to `defaultValue` silently.
- `[Flags]` enums with combined values may not round-trip cleanly through `Enum.GetName` (it returns the name of a single member, not a composed name); use a string-typed field if `[Flags]` semantics matter.

## Profile-change handling

When the active profile switches, `IProfileService.ProfileChanged` fires [19]. Plugins must subscribe and notify any bound properties to re-read from the new profile [29]:

```csharp
profileService.ProfileChanged += (s, e) => RaiseAllPropertiesChanged();
```

Without this, the UI shows stale values from the previous profile (even though `GetValue*` calls correctly read from `ActiveProfile.PluginSettings`).

The template [2] does this granularly per-property:

```csharp
private void ProfileService_ProfileChanged(object sender, EventArgs e) {
    RaisePropertyChanged(nameof(ProfileSpecificNotificationMessage));
}
```

`AstroPhysicsToolsOptions` [29] uses `RaiseAllPropertiesChanged()` (a `BaseINPC` helper) for bulk re-read.

## Recommended idioms

1. Inject `IProfileService` via `[ImportingConstructor]`.
2. Construct `PluginOptionsAccessor` in the constructor body using `Guid.Parse(this.Identifier)` (template style [2]) or the explicit `GetAssemblyGuid` check (defensive style [29]).
3. Use `nameof(PropertyName)` as the setting key — no magic strings [29].
4. Subscribe to `ProfileChanged` and re-raise property changes; unsubscribe in `Teardown()`.
5. Provide a sensible default in every `GetValue*` call — never assume a key exists.
6. Avoid `[Flags]` enums backed by `GetValueEnum<T>`.

## Thread safety

No explicit synchronization in `PluginSettingsTemplate.cs` [16] (no `lock`, no `Concurrent*` collections). Concurrent access from background tasks while the UI is also reading is unsafe; if a plugin updates options from a non-UI thread it must marshal back through the UI dispatcher or hold its own lock.

## Gaps and limitations

- The exact trigger points for `Profile.Save()` on disk (every set vs. timed flush vs. on profile switch) are documented as profile-service-driven [16] but not enumerated in fetched source.
- Whether `PluginOptionsAccessor` caches any value or always reads through to `ActiveProfile.PluginSettings` — the implementation appears non-caching but the source was not read line-by-line.
- No mechanism documented for migrating per-profile settings across plugin GUID changes (i.e., once published, the GUID must not change).
