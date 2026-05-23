# Browser TTY tools — comparison rubric

## Dimension scope

Compare four realistic open-source candidates for "WebSocket-backed shell exposed via a containerized daemon," reachable from a browser over a Tailscale tailnet:

- **ttyd** (tsl0922) — https://github.com/tsl0922/ttyd
- **gotty** (sorenisanerd fork) — https://github.com/sorenisanerd/gotty (the original yudai/gotty is archived; the live fork is the one profiled)
- **wetty** (butlerx) — https://github.com/butlerx/wetty
- **code-server** (coder) — https://github.com/coder/code-server (terminal focus, not full IDE)

Source numbers refer to [`citations.md`](../citations.md).

## ttyd

### Project health

- Last release: **v1.7.7 (2024-03-30)** [9].
- Prior releases concentrated late March 2024 (1.7.7, 1.7.6, 1.7.5) after a five-month gap from 1.7.4 (October 2023) [9].
- Languages: 56% C, 26.4% TypeScript [8].
- Last commit visible on landing page: 2024-03-30 [8].
- Maintainer signal: moderate — no release in ~26 months as of 2026-05-23 (release was 2024-03-30), but discovery-iteration evidence shows post-1.7.7 commits and dependency bumps; the project is not abandoned but is in maintenance-only mode.

### Authentication options out of the box

| Method | Flag/mechanism | Source |
|---|---|---|
| HTTP Basic | `-c, --credential username:password` | [8] |
| Auth header from upstream proxy | `-H, --auth-header` (expects `X-WEBAUTH-USER`) | [8, 10] |
| OIDC native | **Not supported** — must be terminated upstream | [8, 10] |

The auth-header mode trusts any request with a non-empty `X-WEBAUTH-USER`. The wiki is explicit: "you should always start ttyd on a unix domain socket" when using this mode [10]. Examples are provided for both Apache (`RequestHeader set X-WEBAUTH-USER`) and nginx (`proxy_set_header X-WEBAUTH-USER $remote_user;`) [10]. This is the natural integration point for an oauth2-proxy or Pomerium sidecar.

The plaintext `-c user:pass` flag is visible in `ps aux` (and, by extension, in any container-inspection command that exposes the running process arguments), which is a known footgun in shared-tenancy environments [13].

### Session isolation

- `-o, --once` exits after first client disconnects [8].
- `-m, --max-clients N` caps concurrent clients [8].
- No documented "share one shell across all tabs" mode by default — the README and flags suggest each WebSocket connection drives the configured command process. ttyd is more reliably used as a single-tenant gateway in front of a single shell. To share a session deliberately, wrap with tmux.

When two browsers open the same URL, both reach the same ttyd process. Behavior is implementation-defined; tmux is the explicit pattern for deliberate sharing.

### WebSocket behavior under proxy

ttyd works under Traefik v3 with no special middleware — Traefik supports WebSocket out of the box [29]. No special ingress annotations are required for single-pod deployments.

### Resource footprint

- Docker image size (`tsl0922/ttyd:alpine`): **6.9 MB compressed** [11]. This is the smallest image among the four candidates by an order of magnitude.
- Idle RAM: no precise number found in-session. Anecdotally low (single C binary + libwebsockets + tmux/bash if used). **Gap.**

### Bundled image + base OS

- Base OS: Alpine Linux [11].

### Historical security signal

- **NCC Group advisory (2017):** Pre-v1.3.1 unauthenticated RCE via `LWS_CALLBACK_RECEIVE`. Patched same day by upstream [12]. Old, fixed, but on the record.
- Credential plaintext exposure in CLI: still open as a feature request [13].

## gotty (sorenisanerd fork)

### Project health

- Original `yudai/gotty` is archived. The active fork is `sorenisanerd/gotty` [14].
- Latest release: **v1.7.2 (2026-05-17)** [15].
- Recent burst of releases (v1.7.0, v1.7.1, v1.7.2 all within 4 days in May 2026) following a ~11-month gap from v1.6.0 (2025-08-03) and ~11-month earlier release v1.5.0 (2024-09-01) [15].
- License: MIT [14].

Fork-of-archived-project is a real maintenance risk, but the 2026 release cadence demonstrates the fork is active.

### Authentication options out of the box

| Method | Flag/mechanism | Source |
|---|---|---|
| HTTP Basic | `-c user:pass` (credentials sent in plaintext on every request without TLS) | [14] |
| TLS server cert | `-t` + `-tls-crt` / `-tls-key` | [14] |
| TLS client cert | `--tls-ca-crt` (requires all clients to present a signed cert) | [14] |
| Random URL token | `-r` with `--random-url-length` (default 8) | [14] |
| Header pass-through | `--pass-headers` converts HTTP headers to env vars | [14] |
| Write permission gate | `-w` (read-only by default; "BE CAREFUL") | [14] |

OIDC is not native; like ttyd, terminate upstream. The TLS client cert option is unique among the four candidates and is a strong primitive when paired with cert-manager.

### Session isolation

> "GoTTY starts a new process with the given command when a new client connects to the server." [14]

**Each client gets its own process by default.** This is the most isolation-friendly default of the four candidates. For deliberate sharing, the README explicitly recommends tmux or GNU Screen [14].

### WebSocket behavior under proxy

Same as ttyd — works under Traefik v3 out of the box [29]. No special annotations.

### Resource footprint

- Go binary, expected baseline low. No specific idle-RAM benchmark in-session. **Gap.**
- No official Docker image published by sorenisanerd as part of release flow; community Alpine images report ~19 MB compressed (discovery-agent snippet, not directly verified). **Gap.**

### Base OS

Community Docker images are Alpine-based (discovery-agent finding from non-official images). **Gap on official image.**

## wetty

### Project health

- Last release: **v2.7.0 (2023-09-16)** [16].
- Default port: 3000 [16].
- License: MIT [16].
- Snyk classifies the npm package as having limited maintenance signal; no recent npm publish in >12 months [17].

### Authentication options out of the box

wetty is fundamentally an SSH bridge in the browser, so its "authentication" is **SSH-based by design** [16]:

| Method | Flag/mechanism | Source |
|---|---|---|
| SSH password | Default | [16] |
| SSH public key | `--ssh-auth publickey` | [16] |
| SSH key file (passwordless) | `--ssh-key` (documented as "password-less and insecure!") | [16] |
| Force SSH when running as root | `--force-ssh` | [16] |
| Custom SSH config | `--ssh-config` | [16] |

This is structurally different from ttyd/gotty — wetty does not host the shell itself; it proxies an SSH session. Authentication is whatever the backend `sshd` enforces. For pod-internal shells this means each sandbox Pod runs an `sshd` and wetty connects to it (typically via `localhost`).

### Session isolation

Each browser connection establishes an independent SSH login. Two browsers at the same URL each get their own SSH session (architectural inference from SSH semantics, not from explicit wetty README text — the README does not document multi-client behavior).

### Resource footprint

- Node.js process; expected baseline 50–100 MB. No wetty-specific idle benchmark found in-session. **Gap.**
- Docker image: `wettyoss/wetty` exists; size not verified in-session (Dockerfile fetch returned 404 for `main` and `dev` branches). Discovery-agent snippet reported ~105 MB. **Gap.**

### Base OS

Not verified in-session. Likely Debian or Node-base from the official Docker image. **Gap.**

### Historical security signal

- **Authentication-token exfiltration in the Glitch wetty embedding** [18]. The wh0 writeup documents an attack where a malicious project member on Glitch could replace the WeTTY server with one that served a page exposing the persistent auth token via the URL — i.e., a token-in-URL / content-injection attack rather than a WebSocket-protocol-level Origin-validation flaw. Glitch's fix was platform-side (short-lived tokens, separating client serving from project containers) rather than an upstream wetty patch. This is one data point that upstream wetty was not the primary patch surface.

The disqualification of wetty for this use case rests less on this specific historic incident and more on the combination of (a) v2.7.0 from 2023-09-16 as the last release [16], (b) Snyk's "limited maintenance signal / inactive" classification [17], and (c) the SSH-bridge architecture imposing an `sshd` inside every sandbox Pod, which adds operational surface without proportional benefit for a homelab scenario.

## code-server

### Project health

- Latest release: **v4.121.0 (2026-05-20)** [19, 20].
- Release cadence: approximately weekly, aligned to upstream VS Code [20].
- License: MIT [19].
- Maintained by Coder, Inc.

### Authentication options out of the box

| Method | Flag/mechanism | Source |
|---|---|---|
| Password | Default, with rate limiting (2/min, 12/hr) | [22] |
| Disabled | `auth: none` in config file | [22] |
| OIDC native | **Not supported** — external reverse proxy required | [22] |
| Documented integrations | Pomerium, oauth2-proxy, Cloudflare Access | [22] |

Coder is explicit: "Never expose code-server directly to the internet without some form of authentication and encryption" [22].

### Session isolation

The integrated terminal in code-server lives inside a VS Code instance. **A single code-server process is single-user by design**: two browsers at the same URL share the same VS Code session — they see the same open files, the same terminal processes, the same workspace state.

For 12 concurrent operators, this means 12 separate code-server pods, not one. Coder's own positioning is that for multi-user deployments, code-server is **the wrong tool** — their recommendation is Coder v2 (a different, heavier product with workspace lifecycle management) [22 referencing Coder marketing context; the Coder docs explicitly recommend a proxy for any production deployment].

### WebSocket behavior under proxy

Works under Traefik v3 out of the box [29]. The 2025 CVE (below) is a proxy-related but not a WebSocket-protocol issue.

### Resource footprint

- Minimum stated: **1 GB RAM, 2 vCPUs** [19].
- Docker image compressed size: **265.68 MB linux/amd64**, **265.08 MB linux/arm64** [25].
- Image tag: `latest` = `4.121.0`. Base OS: Debian [25]. Architectures: linux/amd64, linux/arm64 [25].
- This is the largest image and the heaviest per-instance memory floor of the four candidates.

### Historical security signal

- **CVE-2025-47269 (GHSA-p483-wpfp-42cj):** CVSS 8.3. Title: "Session cookie can be extracted by having user visit specially crafted proxy URL." Affected versions: <4.99.4. Fixed: ≥4.99.4. Description: the `/proxy/` subpath did not validate port, so a crafted URL relayed requests (with session cookie) to an attacker-controlled domain. Published 2025-05-09 by the Coder team [21].

This is the most recent named CVE among the four candidates, and it was responsibly disclosed by the vendor with a patch. The class of bug (URL parsing) is one that recurs in this category of software.

### Helm chart

- In-tree at `coder/code-server/ci/helm-chart/values.yaml` [23]. Defaults: persistence on, 10 Gi ReadWriteOnce, no ingress, image pulled from `codercom/code-server:4.121.0` [23].
- Install docs only briefly reference Helm; community charts also exist [24].

## Cross-cutting risks (all four tools)

**Cross-Site WebSocket Hijacking (CSWSH)** applies to all four. OWASP documents that browsers include cookies in the WebSocket handshake, making any tool that relies solely on cookies for authentication vulnerable to a CSWSH attack from a concurrently open malicious origin unless the server validates the `Origin` header or uses a per-handshake CSRF token [33]. This is the structural threat model that operators must address at the ingress and auth layer, not a per-tool quirk.

## Comparison table

| Project | Last release | Last release date | Authn out-of-box | Session per tab (default) | Proxy-friendly (Traefik v3) | Idle RAM | Image size | Base OS |
|---|---|---|---|---|---|---|---|---|
| ttyd | v1.7.7 [9] | 2024-03-30 [9] | Basic, auth-header [8, 10] | Implementation-defined; tmux for sharing | Yes [29] | Gap | 6.9 MB compressed (Alpine) [11] | Alpine [11] |
| gotty (sorenisanerd) | v1.7.2 [15] | 2026-05-17 [15] | Basic, TLS server, TLS client cert, random URL, pass-headers [14] | **Yes — new process per connection** [14] | Yes [29] | Gap | ~19 MB compressed (community Alpine) | Alpine (community images) |
| wetty | v2.7.0 [16] | 2023-09-16 [16] | SSH-based (delegates to backend `sshd`) [16] | Yes (each connection = SSH login) | Yes [29] | Gap | Gap (~105 MB per discovery) | Gap (likely Debian) |
| code-server | v4.121.0 [20] | 2026-05-20 [20] | Password, none, oauth2-proxy/Pomerium/Cloudflare Access [22] | **No — single VS Code session shared** | Yes [29] | ≥1 GB stated min [19] | 265.68 MB compressed (linux/amd64) [25] | Debian [25] |

## Gaps and Limitations

- Idle RAM benchmarks are missing for all four tools. None of the official READMEs publish baseline-memory data and community reports are too scattered to cite.
- gotty's official image base OS could not be confirmed; the fork does not appear to publish an official Docker image, only via community builds.
- wetty's Dockerfile could not be fetched (404 on `main` branch path); base OS is inferred from the `wettyoss/wetty` Docker Hub image, which was not exhaustively inspected in-session.
- The OpenClaw and OpenShell CVE-related counter-signal was not folded into this comparison, since those projects do not compete in this category.
- ttyd's exact "two browsers, same URL" behavior depends on the running command and whether `tmux` is wrapping it; the README does not document the default behavior precisely.
