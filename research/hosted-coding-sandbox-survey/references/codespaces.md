# GitHub Codespaces

Dimension: how Codespaces solves session persistence, browser access UX, multi-tenant isolation, and credential injection. Sources in [citations.md](../citations.md).

## Session persistence

Each codespace is a Linux container running inside a dedicated VM. A shallow clone of the source repository (full history backfilled during post-create) lands in `/workspaces` on the VM, mounted into the dev container. Changes inside `/workspaces` "are preserved when you stop and start the codespace, and when you rebuild the container" [1]. Changes outside `/workspaces` "are preserved when you stop and start your codespace, but are not preserved when you rebuild the container" [1] — the home directory survives idle stop but is wiped by a `Rebuild Container` action.

Idle behaviour is conservative. Default timeout is 30 minutes [2][7], user-configurable to 5–240 minutes [7], with an org policy cap that overrides higher user settings [7]. "Activity" resets the timer on typing/mouse input OR terminal I/O — input or output [7] — so a long-running build or test that prints to stdout keeps the codespace alive without a human at the keyboard. Stopped codespaces are deleted after 30 days of further inactivity by default [2]. The terminal scrollback survives stop, but the visible terminal contents do not [2].

## Browser access UX

The browser client connects over a "TLS encrypted tunnel provided by the GitHub Codespaces service" [3], and "Only the creator of a codespace can connect to a codespace" [3]. The in-browser editor is a hosted VS Code build.

Port forwarding is a first-class concern. When the in-container process prints `http://localhost:PORT` or `http://127.0.0.1:PORT` to the terminal, the port is auto-forwarded to a generated subdomain `https://CODESPACENAME-PORT.app.github.dev` [6]. Forwarded ports default to HTTP on the in-container side, with HTTPS available as an override [6]. Visibility per port is Private (default), Organization, or Public [6]; only the public mode bypasses auth entirely.

## Multi-tenant isolation

GitHub's strongest claim: "Each codespace is hosted on its own newly-built virtual machine (VM). Two codespaces are never co-located on the same VM" [3]. Restarts re-land the codespace on a fresh VM with current patches [3]. Network isolation is at the virtual-network layer: "Each codespace has its own isolated virtual network. We use firewalls to block incoming connections from the internet and to prevent codespaces from communicating with each other on internal networks" [3]. This is VM-level tenancy, not container-on-shared-host.

## Credential injection

`GITHUB_TOKEN` is minted fresh on every codespace create or restart with an automatic expiry [3]. Its scope follows the user's repo permissions — read-only access yields a fork-write token after auto-fork, write access yields read/write on the source repo, and multi-repo authorizations are explicit [3]. The token remains stable for the duration of a single codespace session and rotates on stop/restart [6].

User secrets are stored encrypted (specific algorithm not surfaced on the user-secrets page [4]) and "exported as an environment variable into the user's terminal session" [4]. Limits: 100 secrets per scope, 48 KB per secret [4]. Scoping is hierarchical (user / repo / org) with repo-level secrets taking precedence over org-level on name collision [4].

## Prebuilds — pool model

Prebuilds split create-time work in two: a GitHub Actions workflow runs `onCreateCommand` and `updateContentCommand` against a temporary codespace, snapshots the container, and stores it; a user-create downloads the snapshot to a fresh VM and runs `postCreateCommand` — which deliberately does not run during prebuild [5]. Concurrency is "one workflow run at a time for a given prebuild configuration"; on multiple pushes, intermediate runs are cancelled and only the last queued run completes [5].

GitHub's own engineering team published the impact numbers: the `github/github` repo is "almost 13 GB on disk" and "cloning the repository takes 20 minutes"; cold codespace create went from 45 minutes → 5 minutes (after shallow-clone + Docker caching) → 10 seconds with prebuilds [8]. The model is a pool, not on-demand: "pools of codespaces, fully cloned and bootstrapped, waiting to be connected with a developer who wants to get to work" [8]. Date matters — this engineering post is from Aug 2021, updated Dec 2022; the pool-pattern claim is durable but exact numbers may have drifted.

## Gaps

- Hypervisor / sandbox tech (Hyper-V, Firecracker, plain Azure VMs?) not publicly documented [3].
- Secret encryption algorithm not stated on the user-secrets doc [4]; libsodium-sealed-box pattern is plausible (used elsewhere by GitHub) but not verified at primary source in this pass.
- 3-hour auth cookie behaviour for private forwarded ports reported by the discovery agent but NOT confirmed on the port-forwarding doc [6]; treat as unverified.
- Exact `GITHUB_TOKEN` TTL beyond "automatic expiry" not stated [3].
