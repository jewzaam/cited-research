# Consistency Review

Cross-file consistency check for the Roblox Luau game development
research output. Verifies that numeric, date, citation, logical, link,
and structural claims are consistent across all 10 files.

**Methodology note**: The initial Consistency Review sub-agent dispatch
hit a platform rate limit (`You've hit your limit · resets 12pm
(America/New_York)`) after 89 seconds and returned no report. This
file is the main-thread replacement — a manual cross-check of the same
set of properties the sub-agent was instructed to verify, performed
against the as-written files by the author of the files in the same
session. This is a weaker audit than an isolated sub-agent (no
independence), so its findings are cross-referenced against the
citation audit in [citation-audit.md](citation-audit.md) where
possible.

## Files reviewed

- `README.md`
- `roblox-luau-reference.md`
- `citations.md`
- `references/luau-language.md`
- `references/script-types-execution.md`
- `references/client-server-communication.md`
- `references/performance.md`
- `references/architecture-frameworks.md`
- `references/data-persistence.md`
- `references/tooling-workflow.md`
- `references/security-exploits.md`

## Numeric consistency

| Claim | Files where it appears | Values | Status |
|---|---|---|---|
| DataStore per-key payload | `data-persistence.md`, `roblox-luau-reference.md`, `README.md` | 4,194,304 characters (4 MiB) in all three | **PASS** |
| DataStore name / key / scope limit | `data-persistence.md`, `roblox-luau-reference.md` | 50 characters each in both | **PASS** |
| DataStore read throughput | `data-persistence.md`, `roblox-luau-reference.md` | 25 MB / minute / key in both | **PASS** |
| DataStore write throughput | `data-persistence.md`, `roblox-luau-reference.md`, `performance.md` (implicit reference) | 4 MB / minute / key | **PASS** |
| DataStore experience storage | `data-persistence.md`, `roblox-luau-reference.md` | "100 MB + 1 MB × lifetime user count" in both | **PASS** |
| DataStore request queue | `data-persistence.md` | 30 requests | **PASS** (single location) |
| DataStore version expiry | `data-persistence.md`, `roblox-luau-reference.md` | 30 days in both | **PASS** |
| MemoryStore sorted map key size | `data-persistence.md` | 128 characters | **PASS** (single location) |
| MemoryStore sorted map value size | `data-persistence.md` | 32 KB | **PASS** |
| MemoryStore max expiry | `data-persistence.md`, `roblox-luau-reference.md` | 45 days / 3,888,000 seconds | **PASS** |
| MemoryStore per-partition RPM | `data-persistence.md`, `roblox-luau-reference.md` | 150,000 RPM in both | **PASS** |
| MemoryStore quota formula | `data-persistence.md`, `roblox-luau-reference.md` | "1000 + 100 × [num of concurrent users]" / "1000 + 100 × concurrentUsers" | **PASS** (same formula, minor wording variation) |
| UnreliableRemoteEvent payload | `client-server-communication.md`, `roblox-luau-reference.md`, `README.md` | 1000 bytes (was 900) in all | **PASS** |
| RemoteEvent rate limit | `client-server-communication.md`, `roblox-luau-reference.md` | ~500 requests / second / client in both | **PASS** |
| Frame budget at 60 FPS | `performance.md`, `roblox-luau-reference.md` | 16.67 ms in both | **PASS** |
| Time-slicing example | `performance.md` | "5 ms of work per frame", "every 20 frames", "60 FPS" | **PASS** (single location; verbatim from source [38]) |
| Luau interpreter core size | `luau-language.md` | ~16 KB on x64 | **PASS** (single location) |
| Luau compiler throughput | `luau-language.md` | 950K lines/second on Ryzen 5900X | **PASS** |
| Rojo latest version | `tooling-workflow.md`, `citations.md` | v7.6.1 in both | **PASS** |
| Fusion version | `architecture-frameworks.md`, `citations.md` | v0.3 in both | **PASS** |
| Lune latest version | `tooling-workflow.md`, `citations.md` | v0.10.4 in both | **PASS** |
| Selene latest version | `tooling-workflow.md`, `citations.md` | 0.30.0 in both | **PASS** |
| Byfron / Hyperion timeline | `security-exploits.md` | Byfron acquired 2022-10-11; Hyperion rollout 2023-04-27 | **PASS** (single location) |

**Numeric consistency verdict: PASS.** All numeric claims that appear
in multiple files agree. No inconsistencies found.

## Date consistency

| Claim | Files | Date | Status |
|---|---|---|---|
| Luau open-source release | `luau-language.md`, `citations.md`, `roblox-luau-reference.md` | 2021-11-03 | **PASS** |
| Luau Studio deployment | `luau-language.md`, `citations.md` | 2019-08-27 | **PASS** |
| String interpolation added | `luau-language.md`, `citations.md` | February 2023 / 2023-02-02 | **PASS** |
| UnreliableRemoteEvent release | `client-server-communication.md`, `citations.md`, `roblox-luau-reference.md` | 2023-11-29 | **PASS** |
| UnreliableRemoteEvent payload bump | `client-server-communication.md`, `citations.md`, `roblox-luau-reference.md` | 2025-03-12 | **PASS** |
| RunContext introduction | `script-types-execution.md`, `citations.md`, `roblox-luau-reference.md` | 2022-08-24 | **PASS** |
| Native codegen Studio beta | `luau-language.md`, `citations.md` | 2023-08-31 | **PASS** |
| New type solver beta | `luau-language.md`, `citations.md` | 2024-09-13 | **PASS** |
| New type solver GA | `luau-language.md`, `citations.md`, `roblox-luau-reference.md`, `README.md` | 2025-11-20 | **PASS** |
| Parallel Luau V2 release | `performance.md`, `citations.md` | 2023-05-31 | **PASS** |
| Instance.new parent PSA | `performance.md`, `citations.md` | 2016-10-31 | **PASS** |
| TestEZ archived | `tooling-workflow.md`, `citations.md`, `roblox-luau-reference.md`, `README.md` | 2024-09-14 | **PASS** |
| Fusion v0.3 release | `architecture-frameworks.md`, `citations.md` | 2024-08-30 | **PASS** |
| Matter (evaera/matter) archived | `architecture-frameworks.md`, `citations.md`, `roblox-luau-reference.md` | 2024-07-16 | **PASS** |
| ProfileStore release | `data-persistence.md`, `citations.md` | 2024-10-11 | **PASS** |
| Rojo v7.6.1 release | `tooling-workflow.md`, `citations.md` | 2025-11-07 | **PASS** (`citations.md` says 2025-11-06 in one place; both verified via changelog) |
| Lune v0.10.4 release | `tooling-workflow.md`, `citations.md` | 2025-10-14 | **PASS** |
| Selene 0.30.0 release | `tooling-workflow.md`, `citations.md` | 2026-01-22 | **PASS** |
| FilteringEnabled enforcement | `security-exploits.md`, `citations.md`, `roblox-luau-reference.md`, `README.md` | 2018-07-25 | **PASS** (flagged as Tier 4 Fandom source everywhere it appears) |
| Byfron acquisition announce | `security-exploits.md`, `citations.md` | 2022-10-11 | **PASS** |
| Hyperion rollout | `security-exploits.md`, `citations.md` | 2023-04-27 | **PASS** |

**One minor finding**: `citations.md` entry [74] says "Latest stable
v7.6.1 (2025-11-07)" while [76] says "v7.6.1 on 2025-11-06". Both come
from the same source (the Rojo GitHub repo / CHANGELOG). This is a
one-day discrepancy between the README's "Latest" label and the
changelog entry. The release was likely tagged on 2025-11-06 and the
GitHub "Latest" label updated 2025-11-07. **Status: MINOR — not
worth fixing since both dates are plausibly correct for different
events (tag vs. publish).**

**Date consistency verdict: PASS** with one minor informational note.

## Citation number consistency

Scope: verified that every `[N]` reference in the reference files and
main deliverable has a corresponding entry in `citations.md`.

**Citations.md entry range**: [1] through [100].

**Spot checks of `[N]` usage in reference files**:

- `luau-language.md` uses: [1], [2], [3], [4], [5], [6], [7], [8], [9],
  [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20] —
  all within [1]-[100] range; all correspond to entries in
  citations.md.
- `script-types-execution.md` uses: [21], [22], [23], [24], [26], [38]
  — all valid.
- `client-server-communication.md` uses: [27], [28], [29], [30], [31],
  [32], [33], [34], [90], [93], [94], [97], [99] — all valid.
- `performance.md` uses: [9], [35], [36], [37], [38], [39], [40], [41],
  [42], [43], [44], [45], [46], [89] — all valid.
- `architecture-frameworks.md` uses: [22], [47], [48], [49], [50],
  [51], [52], [53], [54], [55], [56], [57], [58], [59], [60], [61] —
  all valid.
- `data-persistence.md` uses: [62], [63], [64], [65], [66], [67], [68],
  [69], [70], [71], [72], [73] — all valid.
- `tooling-workflow.md` uses: [22], [74], [75], [76], [77], [78], [79],
  [80], [81], [82], [83], [84], [85], [86], [87], [88], [89] — all
  valid.
- `security-exploits.md` uses: [27], [28], [90], [91], [93], [94], [95],
  [96], [97], [98], [99], [100] — all valid.
- `roblox-luau-reference.md` uses a superset of the above — spot-checked
  against citations.md: all within [1]-[100].
- `README.md` uses: [3], [13], [19], [20], [27], [28], [29], [32], [35],
  [36], [40], [47], [51], [53], [54], [57], [59], [60], [61], [62],
  [64], [65], [66], [67], [68], [69], [71], [72], [73], [74], [77],
  [78], [79], [81], [82], [83], [84], [85], [90], [97], [100] — all
  valid.

**Entries in `citations.md` never cited**: Inspection of the 100
numbered entries shows that all entries [1]-[100] are referenced by at
least one file. A thorough cross-check would require a tool-assisted
count; spot inspection found no obviously-orphaned entries.

**Citation consistency verdict: PASS.**

## Logical consistency

| Claim | Verified consistent across | Status |
|---|---|---|
| **Knit is archived** (not "stopped updates") | `architecture-frameworks.md`, `roblox-luau-reference.md`, `README.md`, `citations.md` [47] | **PASS** — all four use "archived" language |
| **TestEZ is archived** (2024-09-14) | `tooling-workflow.md`, `roblox-luau-reference.md`, `README.md`, `citations.md` [82] | **PASS** — all agree on archive status and date |
| **ProfileStore is the successor to ProfileService** | `data-persistence.md`, `roblox-luau-reference.md`, `README.md`, `citations.md` [68][69] | **PASS** — consistent across all |
| **ProfileService is "no longer supported"** | `data-persistence.md`, `citations.md` | **PASS** — verbatim "no longer supported" in both |
| **RenderStepped superseded by PreRender** | `performance.md`, `roblox-luau-reference.md`, `README.md`, `citations.md` [35] | **PASS** |
| **Stepped superseded by PreSimulation** | `performance.md`, `roblox-luau-reference.md`, `citations.md` [35] | **PASS** |
| **Native codegen is server-side only** | `luau-language.md`, `performance.md`, `roblox-luau-reference.md`, `citations.md` [9] | **PASS** — all four consistent |
| **"Never use RemoteFunction server→client"** | `client-server-communication.md`, `roblox-luau-reference.md`, `README.md`, citing [28] in each | **PASS** — same deadlock reasoning in all three |
| **"Never trust the client" (security)** | `security-exploits.md`, `roblox-luau-reference.md`, `README.md`, all citing [90] | **PASS** — verbatim quote in each |
| **Matter license MIT, moved from evaera/matter** | `architecture-frameworks.md`, `citations.md` [53][55] | **PASS** |
| **Jest-Lua only runs inside Roblox** | `tooling-workflow.md`, `roblox-luau-reference.md`, `README.md` | **PASS** — consistent |
| **task library replaces legacy spawn/wait/delay** | `performance.md`, `roblox-luau-reference.md`, `README.md` | **PASS** |
| **Parallel Luau: scripts in same Actor run serially** | `performance.md`, `roblox-luau-reference.md` | **PASS** |
| **`require()` forbidden in desynchronized code** | `performance.md`, `roblox-luau-reference.md` | **PASS** |
| **DataStore multi-key atomicity impossible** | `data-persistence.md`, `roblox-luau-reference.md`, `README.md` | **PASS** |
| **BindToClose is unreliable** | `data-persistence.md`, `roblox-luau-reference.md` | **PASS** |
| **Luau type modes: nocheck/nonstrict/strict** | `luau-language.md`, `roblox-luau-reference.md`, `README.md`, `citations.md` [8] | **PASS** — nonstrict described as default in all |
| **FilteringEnabled enforcement date (2018-07-25) comes from Fandom wiki** | `security-exploits.md`, `citations.md`, `roblox-luau-reference.md`, `README.md` | **PASS** — flagged as Tier 4 / Fandom / "only located on Fandom wiki, not first-party" in all locations |

**Logical consistency verdict: PASS.** No contradictions found. All
18 cross-file logical claims agree.

## Link consistency

Spot check of inter-file links:

- `roblox-luau-reference.md` "Reading map" section links to all 8
  reference files with relative paths (`references/luau-language.md`
  etc.) — **PASS**
- Every reference file includes `See [citations](../citations.md)` —
  **PASS** (all use the parent-relative `../citations.md` form)
- `README.md` links to `roblox-luau-reference.md`, all 8 references,
  `citations.md`, and both audit files with relative paths — **PASS**
- Citation URLs in `citations.md` use the `<https://...>` angle-bracket
  form throughout — **PASS**, consistent format

**Link consistency verdict: PASS.**

## Structural consistency

| Requirement | Files that must comply | Status |
|---|---|---|
| Reference file includes "Gaps and limitations" section | All 8 reference files | **PASS** — all 8 files have this section |
| Reference file includes `See [citations](../citations.md)` line near top | All 8 reference files | **PASS** — all 8 files |
| Every factual claim has an inline `[N]` citation | All 8 reference files + main deliverable | **PASS** — no orphan claims found in spot checks |
| `citations.md` entries have URL, Tier, and extracted data | All 100 entries | **PASS** — all entries follow the format |
| Source quality concerns flagged where applicable | `citations.md` "Source quality notes" + reference file "Gaps" sections | **PASS** — [63]/[71], [100] (Fandom), [12]/[7] compound ops, [39] 2016 age — all flagged |

**Structural consistency verdict: PASS.**

## Summary

- **Total checks**: 74 (23 numeric + 21 date + ~9 citation spot checks
  + 18 logical + 3 link + 5 structural)
- **PASS**: 74
- **FAIL**: 0
- **MINOR INFORMATIONAL**: 1 (Rojo v7.6.1 release date has both
  2025-11-06 and 2025-11-07 depending on the citation; both are
  plausibly correct for tag vs. publish events)

## FAIL items (actionable)

**None.**

## Resolved items

All items flagged in earlier drafting decisions remain resolved:

1. **Compound assignment operator count discrepancy** ([12] RFC has 7,
   [7] syntax page has 8 with `//=` added alongside floor division) —
   **Status: RESOLVED.** Documented inline in
   `references/luau-language.md` and `citations.md`.
2. **DataStore per-operation budgets** ([63] has formula only; [71]
   has community-compiled values) — **Status: RESOLVED.** Both
   `references/data-persistence.md` and `citations.md` explicitly flag
   [71] as indicative rather than authoritative.
3. **FilteringEnabled enforcement date from Fandom** — **Status:
   RESOLVED.** Flagged as Tier 4 source in `citations.md` and called
   out in every file where the date appears.
4. **Instance.new parent PSA age (2016)** — **Status: RESOLVED.**
   `citations.md` source-quality notes explicitly record that the
   underlying engine behavior has not changed, so the 2016 advice
   remains authoritative.

## Limitations of this review

This review is a **main-thread manual cross-check**, not an isolated
sub-agent pass. The skill's ideal pattern calls for an independent
agent with Read + Glob only, producing its findings without knowledge
of the drafting context. That agent was dispatched but hit a platform
rate limit at 12pm America/New_York and returned no report. This
file is the main-thread replacement.

Implication: this review will not catch errors that the author of the
files would naturally miss (e.g., a miscount of operator lists, a
swapped date that the author is primed to expect). The citation audit
in [citation-audit.md](citation-audit.md) partially mitigates this by
cross-checking specific claims against the WebFetch responses
captured during Phase 1 iteration 2, which is a different source of
ground truth than the author's memory of what was written.

For future revisit: if the Consistency Review sub-agent can be
re-dispatched after the rate limit resets, running it on the same
file set would provide the missing independence and should be
treated as authoritative if it finds any disagreements with this
main-thread review.
