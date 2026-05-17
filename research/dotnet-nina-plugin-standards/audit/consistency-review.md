# Consistency Review — C# NINA 3.x Plugin Coding Standards

Reviewer: isolated sub-agent with no shared conversation context from the research session.
Review date: 2026-05-17.
Files reviewed: README.md, dotnet-nina-plugin.md, citations.md, references/build-and-install.md, references/assembly-metadata.md, references/mef-manifest.md, references/mediators-and-devices.md, references/wpf-options-ui.md, references/persisted-options.md, references/embedded-http.md, references/logging.md, references/async-threading-and-csharp-style.md, references/testing.md, references/publishing.md.

---

## Summary Table

| ID | Severity | Category | Short description |
|---|---|---|---|
| C-01 | MODERATE | Numerical consistency | `NINA.Plugin` version used in deliverable csproj example (3.2.0.9001) vs. citation [26] source (3.1.2.9001) — relationship not explained at point of use in §1 |
| C-02 | MODERATE | Numerical consistency | `CommunityToolkit.Mvvm` version is stated as `>= 8.2.2` (citation [40]) and as `8.4.0` (citation [11]) in the same sentence in citations.md; the deliverable and README uniformly use `8.4.0` without surfacing the `>= 8.2.2` floor |
| C-03 | MINOR | Contradiction transparency | `daleghent/nina-influxdb-exporter` (citation [28]) uses `MinimumApplicationVersion 3.2.0.1000`, not `3.2.0.9001`; assembly-metadata.md notes this but frames it neutrally; the discrepancy is not explicitly reconciled in the deliverable §3 where `3.2.0.9001` is given as the recommended value |
| C-04 | MINOR | Estimation marker | `CoreUtil.GetNearestAvailablePort` is referenced in embedded-http.md as `CoreUtility.GetNearestAvailablePort` (one file) vs `CoreUtil.GetNearestAvailablePort` (all other files) — name inconsistency |
| C-05 | MINOR | Cross-reference link | deliverable §5.4 links to `[mediators-and-devices](references/mediators-and-devices.md)` — resolves correctly from `dotnet-nina-plugin.md`. README links to `dotnet-nina-plugin.md`, `citations.md` without path prefix — these are same-directory so they resolve. All `references/*.md` files link to `[citations](../citations.md)` — resolves correctly one directory up. No broken links found. PASS on all internal links. |
| C-06 | MINOR | Completeness | deliverable §8 states `CoreUtil.GetNearestAvailablePort(port)` citing [20] and [32]; citation [20] (CoreUtil.cs) confirms `GetNearestAvailablePort` exists; consistent. |
| C-07 | PASS | Numerical consistency | `EmbedIO` version: `3.5.2` stated consistently in deliverable §8, README quick-ref, embedded-http.md, citations [36], citations [30] (ninaAPI.csproj reference). |
| C-08 | PASS | Numerical consistency | `<api-version>` 3-segment `3.0.0`: consistent across deliverable §1, README quick-ref, build-and-install.md, citations [26], [30], [41]. |
| C-09 | PASS | Numerical consistency | Default `MinimumApplicationVersion` when missing = `1.11.0.0`: consistent across deliverable §3, assembly-metadata.md, README finding #7, citations [8]. |
| C-10 | PASS | Numerical consistency | Default `Version` when missing = `1.0.0.0`: consistent across deliverable §3, assembly-metadata.md, citations [8]. |
| C-11 | PASS | Numerical consistency | Log retention = 90 days: consistent across deliverable §9, logging.md, citations [10] and [59]. |
| C-12 | PASS | Numerical consistency | Logger output template `{Timestamp:yyyy-MM-ddTHH:mm:ss.ffff}|{LegacyLogLevel}|{Message:lj}{NewLine}{Exception}`: identical across deliverable §9, logging.md, citations [10]. |
| C-13 | PASS | Contradiction check | Logger backend is Serilog (not log4net): consistent across all files; log4net only mentioned as "not present" or "older docs". |
| C-14 | PASS | Contradiction check | `IImageSaved` lives on `IImageSaveMediator` not `IImagingMediator`: consistent across deliverable §5.1, mediators-and-devices.md, README finding #3, citations [12], [13]. |
| C-15 | PASS | Contradiction check | `RemoveConsumer` (not `UnregisterConsumer`): consistent across deliverable §5.2 and §5.4, mediators-and-devices.md, citations [15]. |
| C-16 | PASS | Contradiction check | `PluginBase` does not extend `BaseINPC` and does not implement `IDisposable`: consistent across deliverable §4, mef-manifest.md, wpf-options-ui.md, citations [8]. |
| C-17 | PASS | Contradiction check | Template csproj targets .NET Framework 4.8 (stale) while wizard generates net8.0: consistent across all files that touch it; always labeled as stale/historical. |
| C-18 | PASS | Formula/logic | GUID must match in 4 places: all 4 places enumerated identically in deliverable §12.2, publishing.md, README quick-ref (3 places listed in README but full 4 in the numbered-list). Verified below. |
| C-19 | PASS | Caveat honesty | All 11 reference files have "Gaps and limitations" sections. |
| C-20 | PASS | Citation validity | All citation references `[N]` in all files use N in range 1–59, which matches citations.md entries. One false-positive (`guidAttributes[0]` in persisted-options.md line 19) is array indexing inside a code block, not a citation. |
| C-21 | PASS | Contradiction transparency | The contradicting recommendation (template README says remove all PackageReferences; ninaAPI references all NINA sub-packages directly) is explicitly surfaced in build-and-install.md with both sources cited. |
| C-22 | MODERATE | Estimation marker | deliverable §6.4 references "Confirmed style and brush keys: see wpf-options-ui.md for the full list" — wpf-options-ui.md labels those keys as "verified in source [D5 analysis]" which is an internal agent-analysis label, not a numbered citation. The keys are presented as sourced facts without a numbered citation. |

---

## Issue Details

### C-01 — NINA.Plugin version context in §1 csproj example

**File:** `dotnet-nina-plugin.md` §1 (line ~54); `references/build-and-install.md` (line ~22)

**Excerpt (deliverable §1):**
```xml
<PackageReference Include="NINA.Plugin" Version="3.2.0.9001">
```

**Excerpt (build-and-install.md):**
> NINA 3.2 stable plugins reference `NINA.Plugin 3.2.0.9001` [30] (or `3.1.2.9001` for plugins still on the 3.1 branch [26]).

**Excerpt (citation [26]):**
> `NINA.Plugin 3.1.2.9001` (InfluxDB exporter, cited as the canonical pattern plugin in §1 rationale)

**Finding:** The deliverable's §1 cites [26] (InfluxDB exporter, version 3.1.2.9001) and [30] (ninaAPI, version 3.2.0.9001) as joint sources for the csproj pattern, then uses `3.2.0.9001` in the example. This is a correct representation since `3.2.0.9001` is the current stable per [39]. However, §1's rationale bullet says "synthesized from [26][30]" immediately after an example that uses `3.2.0.9001` — a reader could wonder why [26] is cited when it uses a different version. build-and-install.md correctly explains this (both versions exist for different NINA branches). The deliverable does not.

**Expected:** Either note that [26] uses `3.1.2.9001` (an older 3.1-branch plugin), or remove [26] from the citation for the version number.
**Actual:** `3.2.0.9001` in example, [26] cited jointly with [30] without qualification.
**Grade:** MODERATE — not a factual error (3.2.0.9001 is the current stable), but the citation pairing is misleading at point of use.
**Status: RESOLVED** — Inline comment added in deliverable §1 csproj example: `<!-- NINA.Plugin version: match the NINA target. 3.2.0.9001 for NINA 3.2 stable [30]; 3.1.2.9001 for plugins still on 3.1 [26] -->`. The two version targets are now explicit at point of use.

---

### C-02 — CommunityToolkit.Mvvm version floor vs. pinned version

**File:** `citations.md` [40] vs. [11]; `dotnet-nina-plugin.md` §6.5; `references/build-and-install.md` line ~63

**Excerpt (citations.md [40]):**
> Confirms `CommunityToolkit.Mvvm >= 8.2.2` (8.4.0 in develop per [11]) is a transitive dependency.

**Excerpt (citations.md [11]):**
> Direct PackageReferences include `CommunityToolkit.Mvvm 8.4.0`

**Excerpt (deliverable §6.5):**
> `CommunityToolkit.Mvvm 8.4.0` ships with NINA [11]

**Excerpt (deliverable §2, assembly exclusion list):**
> `CommunityToolkit.Mvvm (>=8.2.2)`

**Finding:** The deliverable uses `8.4.0` in §6.5 (the pinned csproj example and prose) and `>=8.2.2` in §2 (exclusion list). These are technically compatible (8.4.0 satisfies >=8.2.2) but state different things. A plugin author pinning `Version="8.4.0"` and a different one pinning `Version="8.2.2"` would both satisfy the §2 rule but the §6.5 guidance only shows 8.4.0. The inconsistency is minor but could confuse an auditor checking whether a plugin referencing 8.2.2 is compliant. build-and-install.md line ~63 uses the form `>= 8.2.2, currently 8.4.0` which is the clearest statement.

**Expected:** Deliverable §2 and §6.5 should use the same form, or §2 should note "currently 8.4.0 as of NINA 3.2" matching §6.5.
**Actual:** §2 says `>=8.2.2`, §6.5 says `8.4.0`.
**Grade:** MODERATE — creates ambiguity about what version to pin.
**Status: RESOLVED** — Deliverable §2 exclusion list now reads `CommunityToolkit.Mvvm (currently 8.4.0 on develop; floor >=8.2.2 per NINA.Core)`. The pinned version and the dependency floor are both surfaced in one place, matching the clearest statement in build-and-install.md.

---

### C-03 — MinimumApplicationVersion example value vs. influxdb-exporter reality

**File:** `references/assembly-metadata.md` line ~36; `dotnet-nina-plugin.md` §3 table

**Excerpt (assembly-metadata.md):**
> The `nina-influxdb-exporter` AssemblyInfo [28] uses `3.2.0.1000` — pinning to the 3.2 stable API floor.

**Excerpt (deliverable §3 table):**
> `[AssemblyMetadata("MinimumApplicationVersion", "3.2.0.9001")]` — Recommended

**Excerpt (citation [28]):**
> `[AssemblyMetadata("MinimumApplicationVersion", "3.2.0.1000")]`

**Finding:** The deliverable recommends `3.2.0.9001` (matching the NINA.Plugin stable NuGet version). The real-world example plugin uses `3.2.0.1000` (a pre-release build number). assembly-metadata.md notes the discrepancy inline. The deliverable does not. Both values are defensible (3.2.0.9001 = exact stable match; 3.2.0.1000 = any 3.2 build including pre-release) but the deliverable's recommended value and the cited real-world example disagree. This is not a factual error but a missing reconciliation note.

**Expected:** Deliverable §3 footnote or inline note explaining why the real-world example uses `3.2.0.1000` instead of `3.2.0.9001`.
**Actual:** No reconciliation.
**Grade:** MINOR — the recommendation is sound; the gap is just unexplained.
**Status:** OPEN

---

### C-04 — `CoreUtil` vs `CoreUtility` name in embedded-http.md

**File:** `references/embedded-http.md` line ~84

**Excerpt:**
> fixed user-configurable port with automatic fallback to the nearest free port via `CoreUtility.GetNearestAvailablePort(int port)` [20], [32]

**Other files (deliverable §8, logging.md, citations [20]):**
> `CoreUtil.GetNearestAvailablePort(port)` [20], [32]

**Finding:** embedded-http.md spells the class name `CoreUtility` while all other files — including the deliverable §8 which covers the same fact — and citation [20] (which names the source file `CoreUtil.cs`) use `CoreUtil`. `CoreUtil` is the correct class name from [20].

**Expected:** `CoreUtil.GetNearestAvailablePort`
**Actual (embedded-http.md):** `CoreUtility.GetNearestAvailablePort`
**Grade:** MINOR — wrong class name in one reference file; correct in deliverable and citations.
**Status: RESOLVED** — `embedded-http.md` updated to `CoreUtil.GetNearestAvailablePort`. All files now agree.

---

### C-05 — Internal markdown link resolution

**File:** All files.

**Checked links:**
- `references/*.md` → `[citations](../citations.md)`: path goes up one level from `references/` to the root, where `citations.md` lives. **PASS**
- `dotnet-nina-plugin.md` → `[mediators-and-devices](references/mediators-and-devices.md)`: relative path from root into `references/`. **PASS**
- `dotnet-nina-plugin.md` → `[wpf-options-ui](references/wpf-options-ui.md)`: same pattern. **PASS**
- `dotnet-nina-plugin.md` → `[publishing](references/publishing.md)`: **PASS**
- `dotnet-nina-plugin.md` → `[mef-manifest](references/mef-manifest.md)` (referenced in §4): **PASS**
- `README.md` → `[dotnet-nina-plugin.md](dotnet-nina-plugin.md)`: same-directory. **PASS**
- `README.md` → `[citations.md](citations.md)`: same-directory. **PASS**
- `build-and-install.md` → `[build-and-install](build-and-install.md)` (self-reference in assembly-metadata.md): **PASS**
- `wpf-options-ui.md` → `[build-and-install](build-and-install.md)`: same directory. **PASS**

All checked links resolve correctly.
**Grade:** PASS

---

### C-18 — GUID must match in 4 places (formula/logic check)

**Files:** `dotnet-nina-plugin.md` §12.2; `references/publishing.md`; `README.md` quick-ref

**Deliverable §12.2 enumerates:**
1. `[assembly: Guid("...")]` in AssemblyInfo
2. `IPluginManifest.Identifier` (auto-derived from #1 via PluginBase)
3. `manifest.json` `"Identifier"`
4. The GUID passed to `new PluginOptionsAccessor(...)`

**publishing.md enumerates:** Same 4 items with same citations [3],[28],[8],[25],[16],[2]. **PASS**

**README quick-ref:** States "GUID must match across [Guid] + IPluginManifest.Identifier + manifest.Identifier" — lists only 3, omitting `PluginOptionsAccessor`. This is a minor omission in the README summary (which is intentionally brief), not a contradiction. The authoritative count (4) is in the deliverable and publishing.md.

**Grade:** PASS with minor README omission (expected in a summary).

---

### C-22 — WPF style/brush key list cited as "[D5 analysis]" not a numbered citation

**File:** `references/wpf-options-ui.md` line ~51

**Excerpt:**
> Style keys verified in source [D5 analysis]:

**Finding:** `[D5 analysis]` is an internal agent-discovery tag, not a numbered citation from citations.md. The keys listed (StandardTextBlock, SideBarTextBlock, etc.) have no entry in citations.md that independently verifies them. The deliverable (§6.4) defers to wpf-options-ui.md for "the full list" without citing the source of that list.

**Expected:** Either a numbered citation to the NINA source file where these keys were confirmed (e.g., a `NINA.WPF.Base/Resources/Styles/*.xaml` file added to citations.md), or an explicit caveat that the key list is agent-inferred from source inspection and not independently numbered.
**Actual:** `[D5 analysis]` — opaque internal tag; no numbered citation; no caveat.
**Grade:** MODERATE — style keys are presented as sourced facts. If any key name is wrong, there is no traceable source to correct it. This is an estimation-marker gap.
**Status: RESOLVED** — Three new citations added to citations.md: [60] `NINA.WPF.Base/Resources/Styles/TextBlock.xaml`, [61] `Button.xaml`, [62] `StaticResources/Brushes.xaml`. The wpf-options-ui.md table now cites each row to its source file; the `[D5 analysis]` tag is removed.

---

## Items Verified as Consistent

The following were checked and found internally consistent across all files:

1. **EmbedIO version 3.5.2** — identical in deliverable §8, README, embedded-http.md NuGet table, citations [36], and real-plugin reference [30].

2. **`<api-version>` is 3-segment `3.0.0`** — identical in deliverable §1, README quick-ref (twice), build-and-install.md, citations [26], [30], [41]. Explicitly distinguished from the 4-segment `3.0.0.9001` NuGet version.

3. **`MinimumApplicationVersion` default `1.11.0.0`** — stated in deliverable §3, assembly-metadata.md, README finding #7, and citations [8]. All agree on source: `PluginBase.cs`.

4. **`Version` default `1.0.0.0`** — stated in deliverable §3, assembly-metadata.md, citations [8].

5. **Log retention 90 days** — stated in deliverable §9, logging.md, citations [10] and [59]. Two independent sources agree.

6. **Logger output template** — `{Timestamp:yyyy-MM-ddTHH:mm:ss.ffff}|{LegacyLogLevel}|{Message:lj}{NewLine}{Exception}` — character-for-character identical in deliverable §9 and logging.md; consistent with citations [10] and [58].

7. **Logger backend is Serilog, not log4net** — all files agree; log4net is mentioned only as an historical artifact.

8. **`IImageSaved` on `IImageSaveMediator` not `IImagingMediator`** — consistent in deliverable §5.1, mediators-and-devices.md, README finding #3, citations [12] and [13].

9. **`RemoveConsumer` (not `UnregisterConsumer`)** — consistent in deliverable §5.2 and §5.4, mediators-and-devices.md, citations [15].

10. **`PluginBase` does NOT extend `BaseINPC`, does NOT implement `IDisposable`** — consistent in deliverable §4, mef-manifest.md, wpf-options-ui.md, citations [8].

11. **Template csproj targets .NET Framework 4.8 (stale)** — always labeled as stale/historical everywhere it appears; consistently attributed to citation [6].

12. **GUID must match in 4 places** — all 4 places enumerated consistently in deliverable §12.2 and publishing.md; citations [3],[8],[16],[25],[28] each cover one of the four locations.

13. **`[ObservableProperty]` properties are not `virtual`** — consistent in deliverable §11, testing.md, citations [43].

14. **`HttpListenerMode.Microsoft` requires admin or netsh urlacl** — consistent in deliverable §8, embedded-http.md, citations [34], [35], [37].

15. **Citation range** — all `[N]` references in all 13 markdown files use N in [1, 59], which matches the 59 numbered entries in citations.md. No dangling citation references found.

16. **`PluginBase.Teardown()` signature** — `async Task` returning `Task.CompletedTask` by default, overridable — consistent across deliverable §4, mef-manifest.md, citations [8], [9], [56].

17. **`async void` handler wrapping requirement** — consistent across deliverable §5.1, §10.1, mediators-and-devices.md, async-threading-and-csharp-style.md, citations [48].

18. **DataTemplate key form `<AssemblyTitle>_Options`** — consistent across deliverable §6.1, wpf-options-ui.md, citations [4], [23], [24].

19. **`[Export(typeof(ResourceDictionary))]` on Options.xaml.cs** — consistent across deliverable §6.2, wpf-options-ui.md, mef-manifest.md, citations [5], [7].

20. **Enum serialization via `Enum.GetName` / `Enum.TryParse`** — consistent in deliverable §7.1, persisted-options.md, citations [16].

21. **Source quality summary in citations.md** — claims 38 Tier-1, 17 Tier-2, 3 Tier-3. Manual spot check: citations [1]–[11] are all Tier-1 (NINA official sources), [12]–[20] are Tier-1, [26]–[33] are Tier-2 (community plugins), [38] and [58] are Tier-3. The count is consistent with entries.

22. **All 11 reference files have "Gaps and limitations" sections** — verified across all 11 files.

---

## Pre-finalization re-check

Before finalizing, the following potential issues were reconsidered:

- **C-01**: The `[26]` citation in deliverable §1 is for the InfluxDB exporter csproj, which contains `NINA.Plugin 3.1.2.9001`. The deliverable's example uses `3.2.0.9001`. This is not a factual error (3.2.0.9001 is genuinely the current stable), but the citation implies the version came from [26] when it did not — [26] uses 3.1.2.9001. Confirmed as MODERATE.

- **C-22**: Re-examined wpf-options-ui.md carefully. The `[D5 analysis]` tag appears only once in that file as the attribution for the style/brush key table. This tag does not correspond to any entry in citations.md. This is a genuine gap — the keys are stated as "verified in source" with no traceable numbered citation. Confirmed as MODERATE.

- **`CommunityToolkit.Mvvm 8.4.0` vs `8.2.2`**: The deliverable §2 exclusion list says `CommunityToolkit.Mvvm (>=8.2.2)` and §6.5 says `8.4.0`. These are consistent in the sense that 8.4.0 satisfies >=8.2.2, but they tell different stories. A reader using §2 as an audit checklist would pass a plugin with 8.2.2 installed; §6.5 implies 8.4.0 is what ships. Confirmed as MODERATE because the two sections give different guidance for the same question.

- No additional numerical discrepancies were found beyond those already listed. No contradictions were accepted as consistent during initial review.
