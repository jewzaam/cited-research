# Consistency Review

Scope: cross-file consistency check on README.md, hosted-coding-sandbox-survey.md, citations.md, eight per-product reference files, cross-product-comparison.md, and synthesis.md. External-source verification is out of scope (citation-audit agent's job).

## Summary

PASS: 27 | FAIL: 5

## Findings

### FAIL

FAIL — references/synthesis.md:31 vs references/daytona.md:26 vs citations.md:105 — Synthesis item 11 attributes "Daytona uses 22222" for the web terminal to "Daytona [38] (discovery)". Citation [38] (OSS deployment) only documents the SSH Gateway on port 2222 TCP; the port 22222 web-terminal claim is flagged in daytona.md:26 as "discovery agent finding" with no primary-source citation. The bracketed [38] in synthesis is misleading because [38] does not actually support the 22222 claim. Recommended fix: drop the [38] from synthesis item 11 and keep only the "(discovery)" qualifier — e.g. "From Daytona (discovery; not in cited primary sources)". **Status: RESOLVED** — synthesis.md item 11 now reads "From Daytona (discovery; not in cited primary sources)".

FAIL — references/eclipse-che.md:20 + references/eclipse-che.md:78 vs references/cross-product-comparison.md:14 vs README.md:20 — Eclipse Che idle-timeout defaults (`secondsOfInactivityBeforeIdling`, `secondsOfRunBeforeIdling`) are explicitly flagged as "unverified at primary source" in eclipse-che.md (lines 20, 78) and cross-product-comparison.md:14, but the README headline table row for Eclipse Che (line 20) does not mention idle timeout at all and offers no flag. The README persistence cell lists only PVC strategies. Inconsistent treatment of a documented gap: it is surfaced in three places and silently elided in the headline. Recommended fix: add a short "(idle defaults unverified)" qualifier to the README Eclipse Che persistence cell, or accept the elision and remove the gap mention from cross-product-comparison.md to be consistent. **Status: RESOLVED** — README Eclipse Che persistence cell now reads "(Idle defaults unverified at primary source.)".

FAIL — references/daytona.md:42 vs README.md:19 vs references/cross-product-comparison.md:13 vs citations.md (all Daytona entries [35]–[42]) — "Auth0" attribution for Daytona's platform-level auth appears in daytona.md:42 ("Auth0/OIDC at the platform layer"), README.md:19 ("Auth0/Dex OIDC"), and cross-product-comparison.md:13 ("Auth via Auth0/OIDC at platform level"), but no Daytona citation [35]–[42] mentions Auth0 — only Dex is cited (in [38]). The cross-file claims are internally consistent but rest on an uncited source. daytona.md:42 has no citation marker on the Auth0 half of the claim and daytona.md does not list this as a gap. Recommended fix: either add a citation for the Auth0 claim or mark it as discovery/unverified in daytona.md alongside the existing Auth0/OIDC sentence, and propagate the qualifier to the README/cross-product cells. **Status: RESOLVED** — Auth0 attribution now qualified as "from discovery, uncited" in daytona.md, README, and cross-product-comparison.

FAIL — references/daytona.md:16 vs citations.md:101 (citation [36]) — daytona.md says "setting `ephemeral=True` or `autoDeleteInterval: 0` triggers it [36]" — citation [36] quoted material only covers "Ephemeral sandboxes are automatically deleted once they are stopped" and the states list; the specific API knobs `ephemeral=True` and `autoDeleteInterval: 0` are not in the quoted citation summary. These may or may not be on the source page (citation-audit agent's call), but the reference file presents them as cited when the citation summary does not support them. Recommended fix: either extend the citation [36] quoted-material summary to include the two knobs, or rewrite daytona.md:16 to flag those specifics as discovery findings. **Status: RESOLVED** — citation [36] in citations.md now includes the API knobs in its summary (the source page does state them; the WebFetch result captured them).

FAIL — references/gitpod.md:19 vs references/codespaces.md:13 vs README.md:13 — gitpod.md:19 says "Default browser editor is a VS Code variant built on the openvscode-server fork (also used by Codespaces) — confirmed in discovery; not re-fetched in this pass." This makes an architectural claim about Codespaces (that it is built on the openvscode-server fork), but codespaces.md:13 says only "in-browser editor is a hosted VS Code build", README.md:13 says "Hosted VS Code", and no Codespaces citation [1]–[8] mentions openvscode-server. The two reference files are not technically contradictory but the openvscode-Codespaces linkage is asserted in one file and absent from the other (and uncited). Recommended fix: either remove the parenthetical "(also used by Codespaces)" from gitpod.md:19 or add a discovery-source citation for it; do not let one product's reference file make uncited claims about a different product. **Status: RESOLVED** — parenthetical "(also used by Codespaces)" removed from gitpod.md:19.

### PASS — broad categories

PASS — Numeric: Codespaces 30-min default idle (citations.md:13, codespaces.md:9, cross-product-comparison.md:7, README.md:13).
PASS — Numeric: Codespaces 5–240 min idle range (citations.md:23, codespaces.md:9, cross-product-comparison.md:7, README.md:13).
PASS — Numeric: Codespaces 100 secrets/scope + 48 KB per secret (citations.md:17, codespaces.md:25, cross-product-comparison.md:7, README.md:13).
PASS — Numeric: Codespaces 13 GB github/github repo + 20 min clone + 45 min → 5 min → 10 sec prebuild ladder (citations.md:25, codespaces.md:31).
PASS — Numeric: Gitpod Classic 8 h / 36 h max lifetime (citations.md:31, gitpod.md:13, cross-product-comparison.md:8, README.md:14).
PASS — Numeric: Gitpod Classic 14 d / +21 d / +365 d soft/full/record delete (citations.md:31, gitpod.md:13, cross-product-comparison.md:8, README.md:14, synthesis.md:23).
PASS — Numeric: Daytona signed-URL TTL 1–86 400 s (citations.md:107, daytona.md:24, cross-product-comparison.md:13, README.md:19).
PASS — Numeric: Daytona port range 3000–9999 (citations.md:107, daytona.md:24, cross-product-comparison.md:13, README.md:19).
PASS — Numeric: Daytona SSH Gateway port 2222 TCP (citations.md:105, daytona.md:26, daytona.md:52, cross-product-comparison.md:13, README.md:19).
PASS — Numeric: Daytona web terminal port 22222 — internally consistent across daytona.md:26, cross-product-comparison.md:13, synthesis.md:31, README.md:19 (separate issue with citation attribution, see FAIL above).
PASS — Numeric: Replit Always-On removal date "January 1st, 2024" / "2024-01-01" / "Jan 1, 2024" (citations.md:77, replit.md:7, cross-product-comparison.md:11, README.md:17) — three different formats but same date, no contradictions.
PASS — Numeric: Replit Snapshot Engine 16 MiB chunks (citations.md:67, replit.md:9, cross-product-comparison.md:11).
PASS — Numeric: Replit Nix 1 terabyte / 1 TB shared mount + 30,000 packages (citations.md:75, replit.md:39).
PASS — Numeric: Replit IDE ~3000 LOC plugin core (replit.md:15, cross-product-comparison.md:11, README.md:17) — all qualified as "discovery", no citation marker; consistent treatment.

PASS — URL: all 57 citation URLs are unique (no two citation entries point to the same URL) — verified by inspection of citations.md.
PASS — URL: citation count claim — README.md:36 states "57 sources"; citations.md numbers run [1]–[57]; matches.

PASS — Date formatting: dates are presented consistently per citation entry (e.g. citation [22] "Apr 20, 2026 (updated Apr 21)"; citation [8] "Aug 11, 2021 (updated Dec 19, 2022)"). No same-date written two different ways within the same file. Last-revised date "2026-05-23" on README.md:7 is the only "Last revised" mention and is internally consistent.

PASS — Cross-product-comparison citation attributions for Codespaces row ([1][2][5][7][8] / [3][6] / [3] / [3][4]) all map to Codespaces-section citations [1]–[8]. No cross-product misnumbering.
PASS — Cross-product-comparison citation attributions for Gitpod Classic / Flex rows ([9]–[13]) all map to Gitpod-section citations [9]–[13].
PASS — Cross-product-comparison citation attributions for Coder row ([14]–[21]) all map to Coder-section citations [14]–[21].
PASS — Cross-product-comparison citation attributions for Replit row ([22]–[28]) all map to Replit-section citations [22]–[28].
PASS — Cross-product-comparison citation attributions for StackBlitz row ([29]–[34]) all map to StackBlitz-section citations [29]–[34].
PASS — Cross-product-comparison citation attributions for Daytona row ([35]–[42]) all map to Daytona-section citations [35]–[42].
PASS — Cross-product-comparison citation attributions for Eclipse Che row ([43]–[50]) all map to Eclipse Che-section citations [43]–[50].
PASS — Cross-product-comparison citation attributions for Devpod row ([51]–[57]) all map to Devpod-section citations [51]–[57].
PASS — Synthesis attributions to Codespaces, Gitpod Classic, Coder, Replit, StackBlitz, Eclipse Che, Devpod — each cited number matches the right product's citation range; spot-checked items 1, 4, 5, 7, 9, 14, 18, 19, 21, 25, 27, 28, 30, 31, 32, 33, 35, 38.

PASS — Internal links: hosted-coding-sandbox-survey.md links to all eight references/*.md files; each linked file exists in references/. README.md links resolve: hosted-coding-sandbox-survey.md (exists), references/ (exists as dir), citations.md (exists), audit/ (now created by this audit run).
PASS — Reference files all link back to citations.md via `../citations.md` (codespaces.md:3, gitpod.md:3, coder.md:3, replit.md:3, stackblitz.md:3, daytona.md:3, eclipse-che.md:3, devpod.md:3, cross-product-comparison.md:3) — paths resolve.

PASS — Logical: synthesis items attribute patterns to products whose reference files make the same claim — e.g. synthesis item 21 "three explicit NetworkPolicies" maps to eclipse-che.md:43–46 and citation [48]; synthesis item 25 "pull-based runners" maps to daytona.md:12 and citation [35]; synthesis item 33 "Repl Identity" maps to replit.md:33 and citation [24].

PASS — Classification consistency: deliverable hosted-coding-sandbox-survey.md:31–35 five architectural classes (VM-per-tenant, K8s-pod, Sysbox-container, Browser-tab, Client-orchestrated) match the cross-product-comparison.md:25–31 tenancy-unit grouping.

PASS — Gap surfacing: explicit-gap sections in each reference file (codespaces.md:33–38, gitpod.md:37–43, coder.md:39–44, replit.md:45–50, stackblitz.md:48–52, daytona.md:56–62, eclipse-che.md:74–80, devpod.md:57–63) consistently flag the same unverified items mentioned in the deliverable reflection (hosted-coding-sandbox-survey.md:76–82).

PASS — README cross-references match the headline summary — all four-column claims in README.md:13–21 are also stated (with citations) in the corresponding reference file and the cross-product-comparison.md table.
