# Assembly Metadata — AssemblyInfo keys read by PluginLoader

Dimension covers: which `[assembly: ...]` and `[AssemblyMetadata(...)]` attributes NINA's `PluginLoader` reads, format constraints, defaults, and behaviour when malformed.

See [citations](../citations.md).

## Attributes consumed by PluginBase / PluginLoader

`PluginBase` [8] auto-populates `IPluginManifest` [9] properties from these assembly attributes via reflection:

| `IPluginManifest` property | Source attribute / `AssemblyMetadata` key | Required? | Default if missing |
|---|---|---|---|
| `Identifier` (string GUID) | `[Guid(...)]` (`GuidAttribute`) | **Yes** | none — plugin fails to load identity check [7] |
| `Name` | `[AssemblyTitle(...)]` (`AssemblyTitleAttribute`) | **Yes** | none |
| `Version` (IPluginVersion) | `[AssemblyFileVersion(...)]` (`AssemblyFileVersionAttribute`) | **Yes** | `1.0.0.0` per `PluginBase` [8] |
| `Author` | `[AssemblyCompany(...)]` (`AssemblyCompanyAttribute`) | Recommended | empty string [8] |
| `License` | `[AssemblyMetadata("License", ...)]` | Recommended | empty string |
| `LicenseURL` | `[AssemblyMetadata("LicenseURL", ...)]` | Recommended | empty string |
| `Homepage` | `[AssemblyMetadata("Homepage", ...)]` | Optional | empty string |
| `Repository` | `[AssemblyMetadata("Repository", ...)]` | Recommended | empty string |
| `ChangelogURL` | `[AssemblyMetadata("ChangelogURL", ...)]` | Optional | empty string |
| `Tags` (string[]) | `[AssemblyMetadata("Tags", "a, b, c")]` | Optional | empty array (split on comma) [8] |
| `MinimumApplicationVersion` (IPluginVersion) | `[AssemblyMetadata("MinimumApplicationVersion", "Major.Minor.Patch.Build")]` | **Recommended** | **`1.11.0.0`** per `PluginBase` [8] |
| `Descriptions.ShortDescription` | `[AssemblyDescription(...)]` (`AssemblyDescriptionAttribute`) | **Required** per [1] | empty string |
| `Descriptions.LongDescription` | `[AssemblyMetadata("LongDescription", ...)]` | Optional | empty |
| `Descriptions.FeaturedImageURL` | `[AssemblyMetadata("FeaturedImageURL", ...)]` | Optional | empty |
| `Descriptions.ScreenshotURL` | `[AssemblyMetadata("ScreenshotURL", ...)]` | Optional | empty |
| `Descriptions.AltScreenshotURL` | `[AssemblyMetadata("AltScreenshotURL", ...)]` | Optional | empty |

Sources for required/recommended/optional split: README [1] and `PluginBase.cs` [8].

## Key behaviour: `MinimumApplicationVersion`

Per [1]: this field describes the **minimum NINA build the plugin is compatible with**. "If multiple versions of a plugin are available, the plugin manager inside the application will serve the plugin manifest with the highest version that is compatible with the currently running application using the minimum application version."

Per [1] migration steps for porting to .NET 8 / NINA 3.x: "Change the AssemblyMetaData for `MinimumApplicationVersion` to the NINA.Plugin package version." So if you reference `NINA.Plugin 3.2.0.9001`, the corresponding `MinimumApplicationVersion` is `3.2.0.9001`. The `nina-influxdb-exporter` AssemblyInfo [28] uses `3.2.0.1000` — pinning to the 3.2 stable API floor.

Important distinction: `MinimumApplicationVersion` is **not** the same as the `<api-version>` install-path subfolder, which remains `3.0.0` (see [build-and-install](build-and-install.md)).

## Format constraints

- `AssemblyVersion` and `AssemblyFileVersion` follow `Major.Minor.Patch.Build` per [1] and template [3]. CLR `AssemblyVersion` enforces 16-bit-unsigned per segment (max 65535). The "9001" build segment fits comfortably.
- `Guid` must be a valid 128-bit GUID parsable by `Guid.Parse(...)` — the template `MyPlugin.cs` calls `Guid.Parse(this.Identifier)` [2].
- `MinimumApplicationVersion` metadata value uses the same 4-segment string format as `AssemblyVersion` [28]; it is parsed into the `IPluginVersion` structured object.
- `Tags` is a comma-separated string at the attribute layer; `PluginBase` splits into `string[]` [8].

## Malformed / missing behaviour

`PluginLoader.cs` [7] reads `GuidAttribute`, `AssemblyCompanyAttribute`, `AssemblyFileVersionAttribute`, `AssemblyTitleAttribute` via reflection. On failure paths, it synthesizes a fallback `PluginManifest` populated from whatever metadata was successfully read and registers the plugin with a `false` completion status. Non-plugin DLLs are silently skipped with trace-level logging. `ReflectionTypeLoadException` aggregates `LoaderExceptions` into a single error.

`PluginOptionsAccessor.GetAssemblyGuid` [16] returns `null` when the assembly has no `GuidAttribute` **or more than one**. Real-world plugins (e.g. `AstroPhysicsToolsOptions` [29]) explicitly check and throw `Exception("GUID was not found in assembly metadata")` rather than continuing with a null identity.

Net effect:
- Missing `[Guid]`: plugin fails to load (cannot construct `PluginOptionsAccessor`); identity tracking impossible.
- Missing `[AssemblyTitle]`: `Name` is null, DataTemplate Options key becomes `_Options` (no match), options panel renders empty.
- Missing `[AssemblyFileVersion]`: `Version` defaults to `1.0.0.0` per `PluginBase` [8].
- Missing `[AssemblyMetadata("MinimumApplicationVersion")]`: defaults to `1.11.0.0` [8] — i.e., effectively no minimum, but the manifest publisher will fail validation against [25] which lists it as required.

## Template AssemblyInfo is not exhaustive

The template's checked-in `AssemblyInfo.cs` [3] contains ONLY standard CLR attributes — no `[AssemblyMetadata(...)]` keys. Plugin authors must add the recommended set themselves. The README [1] is the canonical list of what to add. The `nina-influxdb-exporter` AssemblyInfo [28] is a realistic example.

## GUID matching with manifest.json

The `[Guid]` attribute must match the `Identifier` field in the published `manifest.json` exactly [25]. The GUID is the install/uninstall identity and must remain constant across all version updates of the plugin [25].

## Gaps and limitations

- The exact branching in `PluginLoader.cs` when a single attribute is malformed (e.g., `AssemblyFileVersion` is "1.0" not "1.0.0.0") vs. when several are missing was not captured at line-level detail. Behaviour described is from agent summaries of [7].
- Whether `[AssemblyConfiguration]` is read at all by NINA is not confirmed by any source — the template includes it [3] but no source code reference reads it.
