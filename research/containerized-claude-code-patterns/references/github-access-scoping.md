# Dimension 4 — GitHub access scoping for the Pod

**What this covers:** three patterns for giving a containerized Claude Code Pod the ability to push branches and open PRs against the user's own repos while keeping the user's work-org repos structurally unreachable. Patterns A (fine-grained PAT), B (second account with forks), and C (GitHub App, added in iter 1). Verdict on lowest-blast-radius pattern.

All facts cite [`citations.md`](../citations.md). Date of research: 2026-05-23.

---

## TL;DR

**The lowest-blast-radius pattern for an AI-sandbox Pod is Pattern C: a private GitHub App installed only on the user's personal repos** [20]. Installation tokens expire after exactly **1 hour** [20], can be further narrowed at mint-time via `repository_ids` [20], the credential format is rotated and stateless as of April 27 2026 [20], and commits/PRs appear as `app-name[bot]` (no contribution-graph noise, no human-impersonation risk). The private-key (PEM) blast radius is bounded to the explicitly installed repos — work-org repos are unreachable by design because a private App is only installable by the owner. Pattern A (fine-grained PAT) is convenient but carries a confirmed, unresolved silent-reset UI bug [22] that can promote routine maintenance into a privilege escalation. Pattern B (second account with forks) trades technical scoping for account-boundary scoping but sits in a GitHub ToS gray zone unless set up as a true machine account [23], and PR-from-fork ergonomics impose ongoing friction.

## 4.1 Pattern A — Fine-grained personal access token (single account)

### 4.1.1 Minimum permissions for push + open PR

Confirmed against the official GitHub docs [19]:

| Permission | Level | Why needed |
|---|---|---|
| Contents | Read and write | `git push` to non-default branches; read repo files |
| Pull requests | Read and write | Create / update PRs |
| Metadata | Read | Implicit dependency of Contents / PR; resolve repo IDs |

Endpoint mapping [19]:
- `PUT /repos/{owner}/{repo}/git/refs/{ref}` → Contents (write)
- `POST /repos/{owner}/{repo}/pulls` → Pull requests (write)
- `GET /repos/{owner}/{repo}` → Metadata (read)

### 4.1.2 Repo scoping and expiry

- Fine-grained PATs went GA on **March 18 2025** [21]
- Tokens can be restricted to "Only select repositories" — no documented hard cap on repo count per token; the published per-account limit is on number of tokens, not repos per token [21]
- Expiry is configurable from 1 to 366 days; org policies may enforce caps; "no expiration" is permitted only outside org-governed contexts [21]
- Unsupported scenarios at GA include: Packages and Checks APIs (no ghcr.io support), multi-org single-token, outside-collaborator access, Enterprise object APIs (SCIM, org creation), Internal repository access outside targeted orgs [21]

### 4.1.3 The silent-reset UI bug (#188472) — Pattern A's biggest problem

Confirmed against [22]: editing a fine-grained PAT through the GitHub web UI silently reverts the repository access setting to "All repositories" when the user saves, even if no scope change was intended. The form defaults to the unrestricted option rather than preserving the token's original scope.

Reproduction (per [22]):
1. Create fine-grained PAT scoped to one repo
2. Verify token works only on that repo
3. Navigate to edit the token (without changing scope)
4. Click "Update token"
5. Token now grants access to all the user's personal repos

**Implication for an AI-sandbox use case:** routine maintenance (extending expiry, adjusting permissions, rotating after a leak suspicion) is a silent privilege-escalation event. The third-party tool the operator forgot was bound to that PAT now sees every personal repo the account has access to — including any forks of work-org code. As of the iter-2 fetch the discussion is unresolved with no GitHub-staff response [22].

### 4.1.4 Blast radius if leaked

- If scoped correctly to selected repos: limited to those repos for the token's remaining lifetime
- If the UI bug above has fired: full read/write to all personal repos
- GitGuardian 2025 data: 96% of leaked GitHub tokens have write access; 28.65M secrets leaked on public GitHub in 2025 [33a]
- Leaked PAT remains usable until manually revoked or expired (no automatic invalidation)
- The token is the user's identity — commits and PR opens appear as the human user

### 4.1.5 Setup ergonomics

- Setup time: ~5 minutes
- Rotation: manual every ≤366 days (or shorter under org policy)
- One env var (`GITHUB_TOKEN` or `GH_TOKEN`) in a K8s Secret
- No bot-identity marker; commits credit the user on contribution graph

## 4.2 Pattern B — Second GitHub account holding forks only

### 4.2.1 ToS posture

GitHub Terms of Service [23] verbatim:

> One person or legal entity may maintain no more than one free Account (if you choose to control a machine account as well, that's fine, but it can only be used for running a machine).

> A machine account is an Account set up by an individual human who accepts the Terms on behalf of the Account, provides a valid email address, and is responsible for its actions.

> A machine account is used exclusively for performing automated tasks.

> You may maintain no more than one free machine account in addition to your free Personal Account.

Implication: a "second personal account holding forks for an AI sandbox" is permitted **only if** used exclusively for automation. The moment the operator uses it interactively (browses, comments, edits a profile bio), it ceases to qualify as a machine account and risks suspension under the "one personal account" rule [23]. GitHub abuse detection is automated and can suspend without warning.

### 4.2.2 Isolation mechanism

Work-org repos live on the primary account; the second account has no access to them by definition. Cross-account fork-PR workflow is the standard fork-PR pattern.

| Property | Behavior |
|---|---|
| Reachability to work repos | Structurally none. The second account simply lacks access. |
| Token scoping | Doesn't matter — even a wide-scope PAT on Account B can only see Account B's repos |
| Cross-org fork | Works (push to fork → open PR to upstream) |

### 4.2.3 Ergonomic costs

- **PR-from-fork friction**: upstream maintainer (= primary account) must approve GitHub Actions runs the first time the fork account submits a PR (security gate added ~2021). For AI-generated PRs this means every novel PR needs manual click-through unless the fork account is added as a collaborator — which defeats the isolation purpose.
- **Contribution graph fragmentation**: commits from Account B don't credit Account A. For developers who care about contribution streaks, this is a real cost. For automation-only use, it's a feature (clearly distinguishes human vs bot work).
- **Double identity maintenance**: separate SSH key, email, PAT, and rotation cadence.
- **Billing seat cost**: in GitHub Enterprise / paid orgs, a machine user account consumes a billable seat. For a personal free account this is moot.

### 4.2.4 Blast radius if leaked

- Bounded to Account B's repos (forks of primary's personal repos + anything else the operator stored there)
- Forks contain a copy of the primary's personal-repo code — if sensitive, the code itself is at risk via the fork
- Work-org repos remain unreachable by design

## 4.3 Pattern C — GitHub App (installation tokens, per-repo install)

### 4.3.1 Token characteristics

The single most operationally important fact from the official docs [20]:

> The installation access token will expire after 1 hour.

Compare to PAT's 1–366 day lifetime [21]. The blast-radius window per token is two to three orders of magnitude smaller.

- JWT (used to mint installation tokens) is signed with RS256; JWT max lifetime is 10 minutes (not in the [20] excerpt but standard GitHub App practice)
- Per-token scoping: `repositories` or `repository_ids` body parameter on the token-creation API, limit 500 repos per request [20]
- Token format: stateless `ghs_APPID_JWT` rolling out April 27 2026 (replaces previously-40-char tokens) [20]
- Cannot be refreshed; must be re-minted on expiry. Octokit SDKs handle automatic re-minting

### 4.3.2 Minimum permissions

Same as Pattern A (per [19] semantics): Contents (write) + Pull requests (write) + Metadata (read). No additional permissions required for the push-branch + open-PR use case.

### 4.3.3 Repo scoping (per-installation + per-token)

GitHub Apps have two scoping layers:

1. **Installation scope** (set at install time): the owner selects "Only select repositories" and picks specific repos. Permanent until the owner changes it.
2. **Token scope** (set at token-mint time): the `repository_ids` parameter further narrows which repos within the installation a given token can access [20].

For an AI-sandbox use case: register a **private** App under the user's personal account (visibility: "Only on this account"). It cannot be installed on work orgs because work-org admins can't see it. Install it only on the user's personal repos. Mint tokens scoped to one repo at a time per session.

### 4.3.4 Blast radius if PEM private key leaks

| Window | Capability |
|---|---|
| 0–1 hour after leak (an attacker mints a token) | Read/write on installed repos for ≤1 hour per minted token |
| 1+ hours after leak (operator rotates PEM) | Existing tokens valid for their remaining minute; no new tokens can be minted |
| Work-org repos | Unreachable — App is private to personal account, not installed on work orgs |

Compare to PAT: leaked PAT is valid for up to 366 days until manually revoked. The PEM is a longer-lived secret than the installation token, but **storing it in K8s Secret + revoking via App regeneration** is a clean operational pattern, and the leaked-credential window is the 1-hour token life, not the PEM lifetime.

Anti-pattern flag: storing the PEM in GitHub Secrets is documented as a poor choice (no expiry, full-app permissions, any workflow with secret access inherits full App power). For a Pod, the K8s Secret + ESO + Reloader pattern documented in [`api-key-injection.md`](api-key-injection.md) §3.2.3 is the appropriate equivalent.

### 4.3.5 Identity and contribution graph

- Commits/PRs appear as `app-name[bot]` — clearly identifiable as automation
- GitHub automatically excludes `[bot]`-suffixed accounts from contributor statistics and contribution graph
- Reviewers see a bot author, not a human — disambiguates AI work from human work cleanly

### 4.3.6 Setup ergonomics

- Setup time: ~10–15 minutes (App registration, key generation, install)
- Rotation: automatic for installation tokens (Octokit re-mints); PEM rotation only on leak
- Token minting flow: JWT (signed with PEM, ≤10 min validity) → POST `/app/installations/{install_id}/access_tokens` → 1-hour installation token
- More moving parts than a PAT, but **net less ongoing maintenance** once set up

## 4.4 Cross-pattern comparison

| Dimension | Pattern A — fine-grained PAT | Pattern B — second account fork | Pattern C — GitHub App |
|---|---|---|---|
| Minimum permissions | Contents+PR write [19] | Contents+PR write (Account B token) | Contents+PR write [20] |
| Credential lifetime | Up to 366 days [21] | Up to 366 days [21] (Account B PAT) | **1 hour** (installation token) [20] |
| Work-repo isolation | By repo scoping (token-level) — **fragile per UI bug [22]** | By account boundary — structural, unconditional | By App installation scope — structural |
| Blast radius if leaked | All scoped repos for ≤366 days; UI bug expands to all personal repos | Account B repos (forks) for ≤366 days; work repos unreachable | Only installed repos, ≤1 hour per token |
| Rotation burden | Manual every ≤366 days; UI bug requires care | Manual every ≤366 days × N accounts | Automatic for tokens (Octokit); PEM rotation rare |
| ToS compliance | Fully compliant | Compliant only if used exclusively as machine account [23] | Fully compliant |
| Ergonomic cost | Low (single env var) + silent-reset bug risk | Medium (dual-account mgmt, fork PRs, no graph credit) | Medium-high upfront (App registration, PEM storage) |
| Contribution graph | Commits credit primary user | No credit on primary; account B graph fragmented | Excluded from graph (`[bot]` identity) |
| PR identity | Primary user | Second / fork account (reviewer confusion) | `app-name[bot]` (unambiguous) |
| Setup time | ~5 min | ~20 min + ongoing dual-account upkeep | ~10–15 min upfront, minimal ongoing |
| Per-repo token narrowing at mint time | No | No | Yes (`repository_ids` per token) [20] |

## 4.5 Verdict — lowest blast radius for "AI in a container that can leak its credential"

**Pattern C (GitHub App) wins on structural grounds.** Three reasons:

1. **Token lifetime is two to three orders of magnitude shorter** (1 hour vs up to 366 days [20] vs [21]). A leaked installation token grants ≤1 hour of damage; a leaked PEM requires active minting to cause harm, and rotating the PEM immediately invalidates all future tokens.
2. **Work-repo isolation is structural, not configurational.** A private App is unreachable on work orgs by design — no token scope mistake can grant access to work repos, because the App isn't installed there. Compare to Pattern A's UI-bug risk [22], where a routine PAT edit can silently grant access to every personal repo (including any work-related forks).
3. **Identity is clearly bot.** `app-name[bot]` commits and PRs are unambiguous, reviewers know they're looking at automation, and the contribution graph is unaffected — no human-impersonation risk and no graph pollution.

**Pattern B is structurally close on isolation** (account boundary is unconditional), but the ToS gray zone [23] + PR-from-fork CI-approval friction + double-identity maintenance make it strictly worse ergonomically than Pattern C for the same isolation property.

**Pattern A is the easiest to set up** and fine for a low-stakes sandbox where the operator is confident they will never edit the PAT after creation. The silent-reset bug [22] makes it an active risk for any sandbox that exists long enough to need maintenance.

### 4.5.1 Recommended setup for the Pod

1. Register a **private** GitHub App under the user's personal account ("Only on this account" visibility)
2. Permissions: Contents=write, Pull requests=write, Metadata=read [19]
3. Install on the user's personal repos only, choosing "Only select repositories" at install time
4. Generate the App's private key (PEM); store as a K8s Secret using the file-mount pattern documented in [`api-key-injection.md`](api-key-injection.md) §3.2.2
5. In the Pod's entrypoint, use Octokit (or a small custom script) to mint a 1-hour installation token at the start of each session, scoped via `repository_ids` to only the repo being worked on this session [20]
6. Pass the token to `gh` / `git` via the standard `GITHUB_TOKEN` env var
7. Rotate the PEM only on suspected compromise; tokens rotate themselves

## 4.6 Gaps and limitations

- **Hard cap on "selected repositories" per fine-grained PAT**: not documented in official sources; the published account-level limit is on number of tokens (50), not repos per token [19], [21]. Practical limit appears to be the UI dropdown's usability rather than a hard API cap.
- **GitHub Apps + scoped-token complexity limits**: counter-discovery surfaced an unverified report of `Too many repositories for installation` errors when scoping to many repos. Not directly verified in iter 2.
- **PAT-reset bug current status**: as of the iter-2 fetch of [22], unresolved. May have been silently patched between research date and any future deployment — re-verify before deployment.
- **GitHub Apps as a multi-tenant pattern**: the App framework is designed for distribution to many orgs; using it for a single-user personal sandbox is supported but uncommon, and most tooling examples assume the GitHub Marketplace publication path (which is not needed for a private App).
- **OIDC / Workload Identity Federation alternative**: GitHub also supports OIDC federation as a credential-free path (e.g., from GitHub Actions to cloud providers). For Pod-to-GitHub auth, this is the inverse direction and does not currently apply — the Pod is the consumer, not the producer.
- **Stateless `ghs_APPID_JWT` format rollout** [20]: April 27 2026 staged rollout. Any third-party tooling that validates token length == 40 chars will break. Verify your scripts handle variable-length tokens.
