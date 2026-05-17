# Publishing — Manifest Repository, Schema, and Submission

Dimension covers: Bitbucket / GitHub manifest repo, `manifest.json` schema, SHA-256 over installer, GUID match, MinimumApplicationVersion, channels, submission workflow.

See [citations](../citations.md).

## Canonical manifest repository

Per [25]: the central manifest repo is `bitbucket.org/Isbeorn/nina.plugin.manifests` (also mirrored to `github.com/isbeorn/nina.plugin.manifests` — both contain the same README). Pull requests target Bitbucket.

The bitbucket-pipelines.yml automation path requires a paid Bitbucket plan because Bitbucket free-tier dropped the Downloads section; the GitHub Actions path (`tools/github-action.yml`) is free and is now the canonical method [25].

## Submission workflow

Six steps per [25]:

1. Satisfy prerequisites (open-source license)
2. Develop the plugin
3. Generate a manifest file
4. Validate the manifest against the JSON schema
5. Submit a pull request to the repository
6. Await review and merge

## Licensing requirement

Per [25]:

> "Closed source plugins will not be accepted for the manifest repository and no support in any form will be given by the community."

Acceptable licenses include MIT, BSD-3-Clause, MPL-2.0. The plugin source must be open; the plugin may interface with proprietary services or commercial backends, but the plugin code itself must be open-source.

## Manifest generation methods

| Method | When to use |
|---|---|
| **GitHub Actions** (`./tools/github-action.yml`) [25] | Recommended. Triggers automatically on version-tag push. Free. |
| **Bitbucket Pipelines** (`./tools/bitbucket-pipelines.yml`) [25] | Only for plugins hosted on a paid Bitbucket workspace |
| **`CreateManifest.ps1`** (PowerShell 7) [25] | Manual local generation |

`CreateManifest.ps1` parameters:
- `-file` (required): path to compiled plugin DLL
- `-installerUrl`: download URL the plugin manager will fetch
- `-createArchive`: bundle the DLL plus deps into a zip
- `-archiveName`: custom zip filename
- `-uploadToBitbucket`: direct upload (paid Bitbucket only)
- `-beta`: designate as Beta channel release

Critical warning per [25]:

> "Make sure that your DLL will not be recompiled or changed after the manifest is created, as the checksum will change each time!"

The implication: in CI, the build → checksum → manifest steps must be a single workflow; rebuild after manifest invalidates the SHA-256.

## Manifest JSON schema

Per [25], the schema definition is in `manifest.schema.json` in the manifest repo.

### Required fields

| Field | Type | Source / constraint |
|---|---|---|
| `Name` | string | Must match `IPluginManifest.Name` (i.e. `[AssemblyTitle]`). Also used as install-folder name. |
| `Identifier` | GUID string | Must match `[assembly: Guid(...)]` in plugin and `IPluginManifest.Identifier`. **Constant across all versions** [25] |
| `Author` | string | From `[AssemblyCompany]` |
| `License` | string | SPDX-like short name (e.g. `"MPL-2.0"`) |
| `LicenseURL` | URL | |
| `Repository` | URL | Plugin source code |
| `Version` | object `{Major, Minor, Patch, Build}` | Each segment is an integer |
| `MinimumApplicationVersion` | object `{Major, Minor, Patch, Build}` | Same shape as Version. Minimum NINA build required. |
| `Installer.URL` | URL | Download URL (the installer file) |
| `Installer.Type` | enum `"DLL"` \| `"ARCHIVE"` | Single DLL or zip bundle |
| `Installer.Checksum` | hex string | Hash of the installer file |
| `Installer.ChecksumType` | enum `"MD5"` \| `"SHA1"` \| `"SHA256"` | Hash algorithm — **`SHA256` is the modern default** |
| `Descriptions.ShortDescription` | string | From `[AssemblyDescription]` |

### Optional fields

| Field | Type | Purpose |
|---|---|---|
| `ChangelogURL` | URL | |
| `Tags` | string array | Searchable tags |
| `Homepage` | URL | |
| `Descriptions.LongDescription` | string | |
| `Descriptions.FeaturedImageURL` | URL | Logo shown in plugin manager |
| `Descriptions.ScreenshotURL` | URL | |
| `Descriptions.AltScreenshotURL` | URL | |
| `Channel` | string | Set to `"Beta"` for beta channel; omit for stable |

## Hash target

The hash is computed over the **installer file** referenced by `Installer.URL` — meaning:
- `Installer.Type = "DLL"` → hash of the .dll
- `Installer.Type = "ARCHIVE"` → hash of the .zip

Recompiling the DLL after manifest creation invalidates the checksum and the plugin manager will refuse the install [25]. The `CreateManifest.ps1` flow automates this; CI workflows must do `build → hash → manifest` as a single transactional unit.

## GUID matching contract

The same GUID must appear in **all four places**:

1. `[assembly: Guid("...")]` in `AssemblyInfo.cs` [3], [28]
2. `IPluginManifest.Identifier` (auto-populated from #1 via `PluginBase` [8])
3. `manifest.json` `Identifier` field [25]
4. The GUID passed to `new PluginOptionsAccessor(profileService, Guid.Parse(this.Identifier))` [16], [2]

If any of these drift, NINA's plugin manager treats the plugin as unrelated to its prior installs — uninstalling the prior version will not update, and persisted options under the old GUID become orphaned.

The GUID must **never change** across plugin versions [25].

## MinimumApplicationVersion semantics

Per [25] and [1]:
- The plugin manager lists all manifest versions of a plugin whose `MinimumApplicationVersion` is ≤ the running NINA build.
- It serves the **highest** such version.
- A plugin author can publish multiple versions targeting different NINA branches by submitting multiple manifests at different `<nina-version>` subfolders (see Folder structure below).

The manifest's `MinimumApplicationVersion` should match the `[AssemblyMetadata("MinimumApplicationVersion", ...)]` attribute in the plugin, which in turn matches the `NINA.Plugin` NuGet version the plugin was compiled against [1]. So a plugin compiled against `NINA.Plugin 3.2.0.9001` declares `MinimumApplicationVersion = "3.2.0.9001"`.

## Folder structure for submission

Per [25]:

```
manifests\<first-letter><plugin-name>\<nina-version>\<plugin-version>\manifest.json
```

Example: `manifests\PPixInsightTools\3.x\1.0.0\manifest.json`.

If only one NINA version is supported, the `<nina-version>` folder can be omitted.

## Channels

Two channels per [25]: stable (default) and Beta. To publish a beta version, add `"Channel": "Beta"` to the manifest. Users opt-in via NINA's Options > General > Plugin Repositories with URL `https://nighttime-imaging.eu/wp-json/nina/v1/beta`.

There is no `Nightly` or `Alpha` channel in the plugin manifest layer. NINA application nightlies are separate from plugin channels.

## Validation before PR

Per [25]:

```bash
winget install nodejs
npm install
node gather.js
```

`gather.js` collects all manifests, validates each against the JSON schema, and reports failures. Your manifest must validate cleanly before PR submission.

## InstallerURL hosting

Per [25] and observed real plugins:
- Bitbucket Downloads no longer available on free plans
- GitHub Releases is the de facto host: `https://github.com/<user>/<repo>/releases/download/<tag>/<file>.zip`
- Any HTTPS URL pointing to the bundled artifact works

## Versioning monotonicity

The plugin manager picks the highest manifest version that is `MinimumApplicationVersion`-compatible [25]. Manifests must increment monotonically; there is no documented downgrade mechanism.

## Gaps and limitations

- The full schema (`manifest.schema.json`) was not fetched directly — the field list above is from the README description. The schema may have additional optional fields not enumerated.
- Whether the `Tags` field is `string[]` (per README description) or another shape (e.g. comma-string at this layer) was not confirmed from the schema file itself.
- The exact `<nina-version>` subfolder naming convention (`3.x` wildcard vs `3.0` exact) is described as flexible in [25]; community practice not surveyed.
