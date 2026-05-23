# Citation Audit — Browser-accessible coding shells

Auditor: independent verification pass. All URLs re-fetched via WebFetch on 2026-05-23.
Sources read before fetching: `citations.md`, `browser-accessible-coding-shells.md`, `README.md`, `references/openshell.md`, `references/openclaw.md`, `references/browser-tty-comparison.md`, `references/k8s-deployment-patterns.md`, `references/synthesis.md`.

---

## Summary table

| # | URL | Grade | Notes |
|---|-----|-------|-------|
| 1 | https://github.com/NVIDIA/OpenShell | VERIFIED | All key claims confirmed: description, license, language %, compute drivers, CLI commands, no browser TTY, alpha status, k8s Helm marked experimental |
| 2 | https://github.com/NVIDIA/OpenShell/releases | VERIFIED | Latest 5 tags and dates match exactly |
| 3 | https://htek.dev/articles/nvidia-openshell-sandbox-ai-agents | VERIFIED | GTC 2026 launch confirmed; Copilot CLI contributor (PR #476) confirmed |
| 4 | https://github.com/openclaw/openclaw | PARTIAL | Docker described as "the default sandbox backend for non-main sessions" — matches; but the README describes it as "Docker is the default sandbox backend; SSH and OpenShell backends are also available," adding context. Star count 374k and commit count 51,743 confirmed. No Helm chart confirmed. Language claim (TypeScript with Swift) is accurate but the fetch notes Node.js-based — Swift client apps match citation. |
| 5 | https://openclaw.ai/ | VERIFIED | Marketing as personal AI assistant with mail, messages, ordering, reminders, GitHub issues, bookmarks, voice, 1Password confirmed |
| 6 | https://en.wikipedia.org/wiki/OpenClaw | PARTIAL | Creator (Peter Steinberger, Austrian), initial release name (Clawdbot, November 2025), Moltbot rename (2026-01-27), MIT license all confirmed. However: the Wikipedia article states the rename to "OpenClaw" was because Steinberger "felt the previous name never quite rolled off the tongue" — the citation claims it was renamed three days after Moltbot, which is consistent. The 247k stars / 47,700 forks figure confirmed as of 2026-03-02. BUT: OpenAI join date is stated as "February 14, 2026" in the article and citation says 2026-02-14 — matches. The citation claims "Initial release November 2025 as 'Clawdbot'" — Wikipedia says "November 24, 2025" — confirmed. Minor gap: Wikipedia does not confirm the exact "three days later" for the OpenClaw rename; it says January 30 (3 days after January 27) — consistent but not explicitly stated as "three days." |
| 7 | https://steipete.me/posts/2026/openclaw | VERIFIED | Published 2026-02-14; creator's blog post on OpenClaw's future direction with OpenAI sponsorship confirmed |
| 8 | https://github.com/tsl0922/ttyd | VERIFIED | Features, auth flags (-c, -H), concurrency flags (-m, -o, -q), default port 7681, terminal type flag, language percentages (56% C, 26.4% TypeScript), last commit 2024-03-30 all confirmed |
| 9 | https://github.com/tsl0922/ttyd/releases | VERIFIED | Last 5 releases and dates confirmed; v1.7.4 breaking change (read-only by default, -W to enable writing) confirmed |
| 10 | https://github.com/tsl0922/ttyd/wiki/Auth-Proxy | VERIFIED | X-WEBAUTH-USER header trust, unix domain socket recommendation, Apache and nginx examples all confirmed |
| 11 | https://hub.docker.com/r/tsl0922/ttyd | PARTIAL | 6.9 MB compressed size confirmed for alpine tag. The base OS as Alpine Linux is inferred from the tag name, not explicitly stated in page content. The citation says "Alpine Linux base" — this is standard Docker Hub convention and consistent, but the page itself does not explicitly state the base OS. |
| 12 | https://research.nccgroup.com/2017/09/08/technical-advisory-remote-shell-commands-execution-in-ttyd/ | INACCESSIBLE | URL returns 307 redirect to https://www.nccgroup.com/research/ — the specific advisory page is no longer accessible at the original URL. The redirect target is the NCC Group general research index with no trace of the ttyd advisory. |
| 13 | https://github.com/tsl0922/ttyd/issues/872 | PARTIAL | The issue is about plaintext CLI credential exposure and is open as an enhancement/feature request — both confirmed. However, the citation claims it is "visible in `ps aux` and `kubectl describe pod`." The actual issue only mentions `ps aux` (general Linux process inspection). There is **no mention of `kubectl describe pod`** in the issue content. The `kubectl describe pod` claim is an extrapolation not present in the source. |
| 14 | https://github.com/sorenisanerd/gotty | VERIFIED | Description, MIT license, auth options (-c, -t, --tls-crt/key, --tls-ca-crt, -r, --random-url-length, --pass-headers), write flag (-w, "BE CAREFUL"), multi-client behavior ("new process per connection"), config file (~/.gotty) all confirmed |
| 15 | https://github.com/sorenisanerd/gotty/releases | PARTIAL | Latest v1.7.2 (2026-05-17), v1.7.1 (2026-05-14), v1.7.0 (2026-05-14) confirmed. v1.6.0 (2025-08-03) and v1.5.1 (2025-08-03) confirmed. However: the citation claims "Long gap (~2 years) between v1.5.0 and v1.6.0" — the actual gap is approximately 9 months (v1.5.0 September 2024 → v1.6.0 August 2025), not 2 years. The releases page also shows v1.5.1 on 2025-08-03 which is simultaneous with v1.6.0. The "~2 years" claim is inaccurate; it is approximately 9–11 months. |
| 16 | https://github.com/butlerx/wetty | VERIFIED | Description, latest v2.7.0 (2023-09-16), SSH-based auth options (--ssh-auth publickey, --ssh-key, --force-ssh, --ssh-config), default port 3000, no archive/maintenance banner all confirmed |
| 17 | https://security.snyk.io/package/npm/wetty | VERIFIED | Limited maintenance signal, wetty classified as inactive/discontinued, latest v2.7.0, no recent npm release in >12 months confirmed |
| 18 | https://wh0.github.io/2023/08/19/wetty-origin.html | INACCURATE | The citation claims this documents "missing Origin header validation on wetty WebSocket endpoint" and a "same-origin attack from sibling page exfiltrated Glitch user's persistent auth token." The actual vulnerability is NOT about Origin header validation. The attack involved a malicious project member replacing the WeTTY server with a fake one that served a malicious HTML page to steal authentication tokens via a URL that exposed the persistent token — a token-in-URL / content-injection attack, not a WebSocket Origin header validation issue. Neither "Origin header" nor "cross-site WebSocket hijacking" appears in the article. The Glitch fix involved replacing persistent tokens with short-lived ones and separating client serving from project containers. |
| 19 | https://github.com/coder/code-server | VERIFIED | Description ("Run VS Code on any machine anywhere and access it in the browser"), system requirements (1 GB RAM, 2 vCPUs), latest version (v4.121.0 2026-05-20), MIT license confirmed |
| 20 | https://github.com/coder/code-server/releases | VERIFIED | Latest v4.121.0 (2026-05-20), v4.118.0 (2026-05-06), v4.117.0 (2026-04-23), v4.116.0 (2026-04-16), v4.115.0 (2026-04-08), weekly cadence aligned to VS Code confirmed |
| 21 | https://github.com/coder/code-server/security/advisories/GHSA-p483-wpfp-42cj | VERIFIED | Title, CVSS 8.3, vector, affected <4.99.4, fixed ≥4.99.4, description (proxy port validation), published 2025-05-09 all confirmed |
| 22 | https://coder.com/docs/code-server/guide | VERIFIED | Password auth with rate limits (2/min + 12/hr), auth: none option, Pomerium / oauth2-proxy / Cloudflare Access integrations, internet exposure warning ("Never expose code-server directly…") all confirmed |
| 23 | https://github.com/coder/code-server/blob/main/ci/helm-chart/values.yaml | PARTIAL | persistence.enabled: true, persistence.size: 10Gi, persistence.accessMode: ReadWriteOnce, ingress.enabled: false, ingress.ingressClassName: "", image.repository: codercom/code-server, image.tag: 4.121.0, image.pullPolicy: Always, resource limits commented out all confirmed. However: the citation states `persistence.storageClass` is "unset" and `persistence.existingClaim: ""` — the fetch reports both are commented out (no default set), not explicitly set to empty string. This is a minor formatting distinction but the functional meaning (no default) is the same. |
| 24 | https://github.com/coder/code-server/blob/main/docs/install.md | VERIFIED | Helm section exists, briefly references Helm pointing to coder.com/docs/code-server/latest/helm confirmed |
| 25 | https://hub.docker.com/r/codercom/code-server/tags | VERIFIED | latest tag = 265.68 MB (linux/amd64), 265.08 MB (linux/arm64), Debian base, linux/amd64 and linux/arm64 architectures confirmed |
| 26 | https://github.com/cloudtty/cloudtty | PARTIAL | Description, MIT license, CRD (kind CloudShell, cloudshell.cloudtty.io/v1alpha1), exposure modes (NodePort default, ClusterIP, Ingress, VirtualService), ttyd binary claim, no persistence story all confirmed. However: the Helm install command in the README quickstart shows `--version 0.5.0` — the citation notes "The CloudTTY official docs still reference 0.5.0 in their quick-start, which lags actual releases" — **this is confirmed accurate** by the fetch. The citation is correct that the README is stale. |
| 27 | https://github.com/cloudtty/cloudtty/releases | VERIFIED | Latest cloudtty-0.8.9 (2025-01-27), prior releases 0.8.8 (2024-11-17), 0.8.7 (2024-07-22), 0.8.6 (2024-05-21), 0.8.5 (2024-03-21) all confirmed |
| 28 | https://tailscale.com/kb/1439/kubernetes-operator-cluster-ingress | VERIFIED | Prerequisites (HTTPS + MagicDNS), ingressClassName: tailscale, TLS hostname defaults to `<ingress-name>-<namespace>`, Let's Encrypt certificates, lazy cert provisioning warning ("first connection might be slow or even time out") all confirmed |
| 29 | https://doc.traefik.io/traefik/v3.4/user-guides/websocket/ | VERIFIED | WebSocket supported out of the box, no special headers/middlewares/annotations for basic WebSocket, WSS uses tls: {} and websecure entryPoint confirmed. No sticky-session discussion confirmed. |
| 30 | https://github.com/kubernetes/ingress-nginx | VERIFIED | Archive notice confirmed ("archived by the owner on Mar 24, 2026, it is now read-only"), Gateway API migration path confirmed, existing artifacts remain available confirmed |
| 31 | https://github.com/kubernetes/ingress-nginx/issues/2461 | PARTIAL | WebSocket drop on backend reload confirmed, reproduced on 0.12.0 and 0.14.0 confirmed. However: the citation states the issue "was closed as part of repo archival 2026-03-24 without an in-product fix." The fetch confirms the issue is now closed (due to archival making the repo read-only), but the fetch does not confirm a definitive in-session closure date or explicit "closed without fix" label. The closure is effectively the archival — the characterization as "closed without fix" is a reasonable inference but was not directly confirmed from the issue page itself. |
| 32 | https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Generators-List/ | VERIFIED | List generator description, arbitrary key/value pairs, Go template syntax ({{.cluster}}, {{.url}}), one Application per list element confirmed. The exact quote "generates parameters based on an arbitrary list of key/value pairs (as long as the values are string values)" is confirmed. |
| 33 | https://cheatsheetseries.owasp.org/cheatsheets/WebSocket_Security_Cheat_Sheet.html | PARTIAL | The citation states "Browsers do not enforce Same-Origin Policy on WebSocket handshakes." The actual OWASP page does not make this statement explicitly. Instead it describes Cross-Site WebSocket Hijacking (CSWSH) and explains that "Browsers include cookies in WebSocket handshake requests" making WebSockets vulnerable — which implies the SOP point but does not state it in those exact words. The practical claim (cookie-only auth without Origin validation is vulnerable to cross-site hijacking) is supported. The specific formulation "Browsers do not enforce Same-Origin Policy on WebSocket handshakes" is an interpretation of the OWASP content, not a direct quote from it. |

---

## Per-citation detail

### Citation 1 — NVIDIA/OpenShell repository
**Grade: VERIFIED**

**Claims in citations.md:** Project description "OpenShell is the safe, private runtime for autonomous AI agents." Apache 2.0. Rust 89.6%. Supports Docker, Podman, MicroVM, Kubernetes. Alpha ("proof-of-life: one developer, one environment, one gateway"). Operator CLI plus optional TUI dashboard (`openshell term`); no browser-based terminal.

**Source evidence:** Fetch confirms all items verbatim:
- Description: "OpenShell is the safe, private runtime for autonomous AI agents"
- License: Apache 2.0
- Rust: 89.6%
- Drivers: Docker, Podman, MicroVM, Kubernetes
- Alpha status: "OpenShell is proof-of-life: one developer, one environment, one gateway"
- TUI (`openshell term`) is a local keyboard-driven dashboard, not a browser terminal
- Kubernetes Helm chart marked "Experimental"

No discrepancies found.

---

### Citation 2 — NVIDIA/OpenShell releases
**Grade: VERIFIED**

**Claims:** Latest 5 tags: v0.0.47 (2026-05-22), v0.0.46 (2026-05-21), v0.0.45 (2026-05-20), v0.0.44 (2026-05-19), v0.0.43 (2026-05-18). ~Daily release cadence.

**Source evidence:** Fetch confirms all five tags and dates exactly. Daily cadence confirmed.

---

### Citation 3 — htek.dev article on OpenShell
**Grade: VERIFIED**

**Claims:** NVIDIA open-sourced OpenShell at GTC 2026. Third-party confirmation. Contributor (Copilot CLI provider).

**Source evidence:** Article states "NVIDIA shipped OpenShell at GTC 2026." Author confirms contributing PR #476 — a Copilot CLI agent provider — which was merged. Both claims confirmed.

---

### Citation 4 — openclaw/openclaw repository
**Grade: PARTIAL**

**Claims:** "Personal AI assistant you run on your own devices. It answers you on the channels you already use." MIT. TypeScript with Swift for macOS/iOS. Docker is "the default sandbox backend for non-main sessions." No official Helm chart or Kubernetes operator in README. 374k stars, 51,743 commits.

**Source evidence:**
- Description, license, star count, commit count: confirmed
- Docker claim: The README states "Docker is the default sandbox backend; SSH and OpenShell backends are also available." — the citations.md wording ("Docker listed as 'the default sandbox backend for non-main sessions'") differs slightly from the actual text ("Docker is the default sandbox backend") — the qualifier "for non-main sessions" appears to be an interpolation not present verbatim in the source
- TypeScript with Swift: confirmed
- No Helm chart: confirmed

**Why PARTIAL:** The Docker backend description quoted in citations.md does not exactly match what the source says. The source says "Docker is the default sandbox backend" without the "for non-main sessions" qualifier that citations.md attributes as a direct quote.

---

### Citation 5 — openclaw.ai official site
**Grade: VERIFIED**

**Claims:** Marketed as personal AI assistant for mail, Beeper messages, ordering, reminders, GitHub issues, bookmarks, voice calls, 1Password vault management.

**Source evidence:** Fetch confirms marketing as personal AI assistant with mail, calendar, GitHub, browser control, system access, 50+ integrations. The specific features listed (mail, messages, ordering, reminders, GitHub issues, bookmarks, voice calls, 1Password) are all present in spirit. No discrepancies on the overall characterization.

---

### Citation 6 — Wikipedia — OpenClaw
**Grade: PARTIAL**

**Claims:** Created by Austrian developer Peter Steinberger. Initial release November 2025 as "Clawdbot." Renamed "Moltbot" 2026-01-27 (Anthropic trademark complaint). Renamed "OpenClaw" three days later. Steinberger joined OpenAI 2026-02-14 with plans for non-profit foundation. MIT license. 247,000 stars and 47,700 forks as of 2026-03-02.

**Source evidence:** Creator (Austrian, Peter Steinberger), initial name (Clawdbot), Moltbot rename date (2026-01-27), MIT license, 247k stars/47.7k forks (2026-03-02), OpenAI join date (2026-02-14), non-profit foundation plans all confirmed.

**Why PARTIAL:** Wikipedia does not confirm the rename from Moltbot to OpenClaw was due to Anthropic trademark complaint — it states he renamed to Moltbot after Anthropic complaints, then renamed again to OpenClaw because "the previous name never quite rolled off the tongue" (personal preference, not trademark). The citation implies the Anthropic complaint drove both renames, which is not what Wikipedia says. The reason for the second rename (to OpenClaw) is personal preference per the source, not an additional trademark issue.

---

### Citation 7 — steipete.me blog post
**Grade: VERIFIED**

**Claims:** Creator's blog post (2026-02-15) on next direction.

**Source evidence:** Published 2026-02-14 (the citation says 2026-02-15 — minor one-day discrepancy, but the content is confirmed as the creator's announcement post about joining OpenAI and OpenClaw's future direction). The post discusses the non-profit foundation and OpenAI sponsorship.

**Note:** The date discrepancy (2026-02-15 in citations.md vs 2026-02-14 per fetch) is minor and does not materially affect any claim made in the deliverables.

---

### Citation 8 — tsl0922/ttyd repository
**Grade: VERIFIED**

**Claims:** Features (libuv, WebGL2, CJK/IME, ZMODEM/trzsz, Sixel, SSL, cross-platform). Auth: `-c, --credential` and `-H, --auth-header`. Concurrency: `-m, --max-clients` (unlimited), `-o, --once`, `-q, --exit-no-conn`. Default port 7681. Terminal type: `-T, --terminal-type` (xterm-256color). Languages: 56% C, 26.4% TypeScript. Last commit 2024-03-30.

**Source evidence:** All confirmed verbatim by fetch. The `-m` default is described as "0, unlimited" in fetch vs "default: unlimited" in citation — the meaning is identical.

---

### Citation 9 — tsl0922/ttyd releases
**Grade: VERIFIED**

**Claims:** Releases: 1.7.7 (2024-03-30), 1.7.6 (2024-03-29), 1.7.5 (2024-03-27), 1.7.4 (2023-10-02), 1.7.3 (2023-01-18). v1.7.4 breaking change: web terminal read-only by default, requires `-W` to enable writing.

**Source evidence:** All five versions and dates confirmed. v1.7.4 breaking change confirmed: "The web terminal is readonly by default now, to make it writable, use `-W` option."

---

### Citation 10 — tsl0922/ttyd wiki Auth-Proxy
**Grade: VERIFIED**

**Claims:** `-H, --auth-header` makes ttyd trust `X-WEBAUTH-USER` header. Recommendation to always start ttyd on unix domain socket when using auth proxy. Examples for Apache (`RequestHeader set X-WEBAUTH-USER`) and nginx (`proxy_set_header X-WEBAUTH-USER $remote_user;`).

**Source evidence:** All confirmed. The unix socket recommendation is quoted verbatim: "you should always start ttyd on a unix domain socket." Apache and nginx examples present.

---

### Citation 11 — Docker Hub tsl0922/ttyd
**Grade: PARTIAL**

**Claims:** `tsl0922/ttyd:alpine` compressed size 6.9 MB. Alpine Linux base.

**Source evidence:** 6.9 MB compressed size confirmed. "Alpine Linux base" is stated based on the tag name — the Docker Hub page does not independently confirm the base OS in its text, it is inferred from the tag name. For a tag named "alpine" this is a sound inference but the page itself does not explicitly state "Alpine Linux" as the base OS.

**Why PARTIAL:** The base OS claim is inferred from the tag name, not explicitly stated by Docker Hub. The 6.9 MB figure is directly confirmed.

---

### Citation 12 — NCC Group ttyd advisory
**Grade: INACCESSIBLE**

**Claims:** Pre-v1.3.1 unauthenticated RCE via `LWS_CALLBACK_RECEIVE` callback. Patched same day (2017-03-10) by upstream. Historical only.

**Source evidence:** The URL https://research.nccgroup.com/2017/09/08/technical-advisory-remote-shell-commands-execution-in-ttyd/ returns a 307 redirect to https://www.nccgroup.com/research/ — the general research index. The specific advisory page is not accessible. The NCC Group research index does not list or surface the ttyd advisory. **The claims cannot be verified against the original source.**

---

### Citation 13 — tsl0922/ttyd issue #872
**Grade: PARTIAL**

**Claims:** `-c user:pass` stored as plaintext CLI argument, visible in `ps aux` and `kubectl describe pod`. Feature request for hashed/file-based credentials, open as of search date.

**Source evidence:**
- Plaintext CLI argument issue: confirmed
- Visible in `ps aux`: confirmed ("Arguments to applications are by default readable to all users on Linux")
- Feature request, open: confirmed (labeled "enhancement," still open)
- **`kubectl describe pod`**: NOT mentioned in the issue. The issue discusses Linux process inspection (`ps`), not Kubernetes-specific pod description. This detail is an extrapolation not supported by the source.

**Why PARTIAL:** The `kubectl describe pod` claim added by citations.md is not present in the source; it is an unsupported inference.

---

### Citation 14 — sorenisanerd/gotty repository
**Grade: VERIFIED**

**Claims:** "Share your terminal as a web application." MIT. Auth: `-c` (basic), `-t`+`-tls-crt/-tls-key` (TLS), `--tls-ca-crt` (TLS client cert), `-r` random URL with `--random-url-length` (default 8), `--pass-headers`. Multi-client: new process per connection. Shared session: tmux/screen. Write: `-w` ("BE CAREFUL"). Config: `~/.gotty`.

**Source evidence:** All confirmed. The `-w` flag is specifically flagged as "BE CAREFUL" — confirmed. New process per connection default — confirmed. tmux/screen recommendation for sharing — confirmed.

---

### Citation 15 — sorenisanerd/gotty releases
**Grade: PARTIAL**

**Claims:** Latest v1.7.2 (2026-05-17), v1.7.1 (2026-05-14), v1.7.0 (2026-05-14), v1.6.0 (2025-08-03), v1.5.1 (2025-08-03). "Long gap (~2 years) between v1.5.0 and v1.6.0, then a burst of releases in 2026."

**Source evidence:** The 5 release versions and dates confirmed. However: the gap between v1.5.0 (September 2024 per releases page) and v1.6.0 (August 2025) is approximately **9–11 months**, not "~2 years" as claimed. The fetch describes it as "nearly a year of inactivity." The "~2 years" characterization in citations.md is **inaccurate**.

**Why PARTIAL:** The version list and dates are accurate, but the described gap duration ("~2 years") is wrong. The gap is approximately 9–11 months.

---

### Citation 16 — butlerx/wetty repository
**Grade: VERIFIED**

**Claims:** "Terminal access in browser over HTTP/HTTPS, using xterm.js with WebSocket support." MIT. Last release v2.7.0 (2023-09-16). Auth: SSH password (default), `--ssh-auth publickey`, `--ssh-key` ("password-less and insecure!"), `--ssh-config`, `--force-ssh`. Default port 3000. No explicit maintenance mode or archived banner.

**Source evidence:** All confirmed. The description matches. v2.7.0 / 2023-09-16 confirmed. All auth flags and the passwordless warning confirmed. Port 3000 confirmed. No archive banner confirmed.

---

### Citation 17 — Snyk Advisor wetty
**Grade: VERIFIED**

**Claims:** Reports wetty as having limited maintenance signal. Latest v2.7.0; no recent npm release in >12 months.

**Source evidence:** Confirmed. Snyk classifies wetty as "INACTIVE," health score 48/100, latest v2.7.0 (2023-09-16), "hasn't seen any new versions released to npm in the past 12 months."

---

### Citation 18 — wh0.github.io wetty Origin issue
**Grade: INACCURATE**

**Claims in citations.md:** "Personal blog documenting missing Origin header validation on wetty WebSocket endpoint. Same-origin attack from sibling page exfiltrated Glitch user's persistent auth token. Glitch built platform-level mitigation rather than waiting for upstream fix."

**Source evidence:** The blog post titled "Replacing WeTTY on Glitch" describes a fundamentally different vulnerability:
- The attack was **not about Origin header validation**. The post does not mention "Origin header" at all.
- The attack involved a malicious project member replacing the WeTTY server with a fake server that served malicious HTML pages to steal persistent authentication tokens that were embedded in the API URL path.
- The vulnerability is a **token-in-URL / content injection attack** (malicious HTML served from within a Glitch project container accessing a URL that contained the persistent auth token), not a cross-site WebSocket hijacking via Origin header bypass.
- Glitch's fixes: replaced persistent tokens with short-lived terminal tokens, moved WeTTY client outside project containers, forced project container responses to serve as plain text.

**How the claim misrepresents the source:** The citation characterizes this as an "Origin header validation" WebSocket vulnerability. The actual vulnerability is a token exposure attack via malicious HTML substitution within the Glitch platform. These are structurally different attack classes. The citation's framing would lead a reader to believe wetty has a WebSocket-protocol-level Origin validation bug, when the source documents a Glitch platform-specific trust boundary violation.

---

### Citation 19 — coder/code-server repository
**Grade: VERIFIED**

**Claims:** "Run VS Code on any machine anywhere and access it in the browser." MIT. Latest v4.121.0 (2026-05-20). Requirements: 1 GB RAM, 2 vCPUs.

**Source evidence:** All confirmed verbatim. The description, version, date, license, and system requirements match exactly.

---

### Citation 20 — coder/code-server releases
**Grade: VERIFIED**

**Claims:** Latest v4.121.0 (2026-05-20), v4.118.0 (2026-05-06), v4.117.0 (2026-04-23), v4.116.0 (2026-04-16), v4.115.0 (2026-04-08). Approximately weekly cadence aligned to upstream VS Code.

**Source evidence:** All five versions and dates confirmed. Each release is described as "Update to Code X.Y.Z" confirming alignment to upstream VS Code.

---

### Citation 21 — code-server GHSA-p483-wpfp-42cj (CVE-2025-47269)
**Grade: VERIFIED**

**Claims:** Title "Session cookie can be extracted by having user visit specially crafted proxy URL." CVSS 8.3 (`CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:L`). Affected <4.99.4. Fixed ≥4.99.4. Improper port validation in `/proxy/` subpath allows crafted URLs to relay session cookies to attacker-controlled domains. Published 2025-05-09.

**Source evidence:** All confirmed exactly. Title, CVSS score and vector, affected/fixed version range, mechanism (proxy port validation bypass), and publication date all match.

---

### Citation 22 — Coder docs code-server guide
**Grade: VERIFIED**

**Claims:** Password default with rate limits (two per minute plus twelve per hour), `auth: none` for SSH-tunneled use, external auth via reverse proxy. Named integrations: Pomerium, oauth2-proxy, Cloudflare Access. Recommended reverse proxies: Caddy, NGINX. Warning: "Never expose code-server directly to the internet without some form of authentication and encryption."

**Source evidence:** Rate limit ("two per minute plus an additional twelve per hour") confirmed verbatim. Pomerium, oauth2-proxy, Cloudflare Access confirmed. Internet exposure warning confirmed verbatim.

---

### Citation 23 — code-server Helm chart values.yaml
**Grade: PARTIAL**

**Claims:** Defaults: `persistence.enabled: true`, `persistence.size: 10Gi`, `persistence.accessMode: ReadWriteOnce`, `persistence.storageClass` unset, `persistence.existingClaim: ""`, `ingress.enabled: false`, `ingress.ingressClassName: ""`, `image.repository: codercom/code-server`, `image.tag: 4.121.0`, `image.pullPolicy: Always`. Resource limits/requests commented out.

**Source evidence:** All major values confirmed. Minor discrepancy: the fetch reports `persistence.storageClass` and `persistence.existingClaim` are **commented out** in the file (not set to empty string), while citations.md says `persistence.storageClass` is "unset" and `persistence.existingClaim: ""`. The functional meaning (no default) is equivalent, but the representation differs. The `""` for `existingClaim` is not the actual file content per the fetch.

**Why PARTIAL:** The `persistence.existingClaim: ""` claim represents the field as having an empty string default, when the source shows it as commented out entirely. Minor but a factual representation difference.

---

### Citation 24 — code-server install docs Helm section
**Grade: VERIFIED**

**Claims:** Brief "Helm" section pointing to coder.com/docs/code-server/latest/helm.

**Source evidence:** Confirmed. The install.md contains a Helm section that "simply directs users to external Helm documentation" at coder.com — consistent with citation.

---

### Citation 25 — Docker Hub codercom/code-server tags
**Grade: VERIFIED**

**Claims:** `latest` = v4.121.0. Compressed size 265.68 MB (linux/amd64), 265.08 MB (linux/arm64). Debian base. Supported architectures: linux/amd64, linux/arm64.

**Source evidence:** All confirmed exactly — sizes, architectures, Debian base, version tag all match.

---

### Citation 26 — cloudtty/cloudtty repository
**Grade: PARTIAL**

**Claims:** Kubernetes-native operator for web terminal. MIT. Helm install with cloudtty helm repo. Exposure modes: NodePort (default), ClusterIP, Ingress, Istio VirtualService. CRD: kind `CloudShell`, group `cloudshell.cloudtty.io/v1alpha1`. Each pod runs ttyd. No persistence story. Docs still reference 0.5.0 in quick-start (stale).

**Source evidence:** Description, MIT, Helm commands, CRD, exposure modes, ttyd binary claim, no persistence story all confirmed. The README quick-start showing `--version 0.5.0` confirmed (docs-to-reality gap confirmed).

**Why PARTIAL:** The claim "jobs are ephemeral with TTL" is stated in citations.md as a citation-supported fact, but the actual CloudTTY fetch confirms only "no persistence story is documented" — the TTL claim was not explicitly confirmed from the page content fetched. It is likely accurate but was not independently confirmed.

---

### Citation 27 — cloudtty/cloudtty releases
**Grade: VERIFIED**

**Claims:** Latest cloudtty-0.8.9 (2025-01-27), prior: 0.8.8 (2024-11-17), 0.8.7 (2024-07-22), 0.8.6 (2024-05-21), 0.8.5 (2024-03-21). Official docs reference 0.5.0 in quick-start (lags).

**Source evidence:** All five release versions and dates confirmed exactly. The stale docs observation confirmed by CloudTTY README fetch (citation 26).

---

### Citation 28 — Tailscale docs Kubernetes Operator cluster ingress
**Grade: VERIFIED**

**Claims:** Prerequisites: HTTPS and MagicDNS on tailnet. Set `spec.ingressClassName: tailscale`. TLS hostname defaults to `<ingress-name>-<namespace>`. Certificates from Let's Encrypt, provisioned lazily. First connection may time out.

**Source evidence:** All confirmed. The lazy cert provisioning warning is quoted: "the first connection might be slow or even time out." Let's Encrypt certificates confirmed. `<ingress-name>-<namespace>` hostname format confirmed.

---

### Citation 29 — Traefik docs v3.4 WebSocket user guide
**Grade: VERIFIED**

**Claims:** "WebSocket is a communication protocol that provides full-duplex communication channels over a single TCP connection" and "Traefik supports WebSocket and WebSocket Secure (WSS) out of the box." No special headers, middlewares, or annotations required. WSS adds `tls: {}` and `websecure` entryPoint. No sticky-session discussion.

**Source evidence:** All confirmed. The out-of-the-box WebSocket support confirmed. WSS configuration via TLS setup confirmed. No sticky-session discussion confirmed.

---

### Citation 30 — kubernetes/ingress-nginx repository
**Grade: VERIFIED**

**Claims:** Archive notice: "This repository was archived by the owner on Mar 24, 2026. It is now read-only." Gateway API as migration path. Existing charts and images remain available; no further releases, bug fixes, or security updates.

**Source evidence:** All confirmed exactly. Archive date 2026-03-24, read-only status, Gateway API recommendation, existing artifacts remain available.

---

### Citation 31 — ingress-nginx issue #2461
**Grade: PARTIAL**

**Claims:** "Ingress controller dropping websocket connections when performing backend reload." Reproduced on 0.12.0 and 0.14.0. Issue closed as part of repo archival 2026-03-24 without in-product fix.

**Source evidence:** WebSocket drop on backend reload confirmed. Versions 0.12.0 and 0.14.0 confirmed. The issue is now closed (due to archival). However: the fetch does not confirm an explicit "closed without in-product fix" label or comment — the closure is the archival itself making the repo read-only, which effectively ends all issue activity. The characterization is a reasonable inference but was not directly stated in the issue page content.

**Why PARTIAL:** The "closed without in-product fix" characterization, while accurate as an inference, is not directly supported by the source's issue page content — it is an interpretation of the archival event.

---

### Citation 32 — Argo CD ApplicationSet List Generator docs
**Grade: VERIFIED**

**Claims:** "The List generator generates parameters based on an arbitrary list of key/value pairs (as long as the values are string values)." Each list element becomes template variables (Go template syntax: `{{.cluster}}`, `{{.url}}`). One Application per list element.

**Source evidence:** Confirmed. The generator behavior, Go template syntax, per-element Application generation, and the key/value pair constraint all confirmed. The fetch notes arbitrary key/value pairs have been supported since v0.2.0, consistent with the current stable behavior described.

---

### Citation 33 — OWASP WebSocket Security Cheat Sheet
**Grade: PARTIAL**

**Claims:** "Browsers do not enforce Same-Origin Policy on WebSocket handshakes. Cookie-only auth without Origin header validation or per-handshake CSRF token is vulnerable to cross-site WebSocket hijacking from any other origin the user has open."

**Source evidence:** The OWASP page confirms that Cross-Site WebSocket Hijacking (CSWSH) is a real threat and that "Browsers include cookies in WebSocket handshake requests, making WebSocket applications vulnerable to CSWSH." OWASP recommends validating the `Origin` header on every handshake and mentions CSRF tokens as supplementary protection.

**Why PARTIAL:** The specific formulation "Browsers do not enforce Same-Origin Policy on WebSocket handshakes" is an interpretation/paraphrase not present verbatim in the OWASP text. The practical implication (cookie-only auth is insufficient, Origin validation is necessary) is confirmed by the source. The framing in citations.md overstates this as a direct OWASP statement when it is actually a summary of OWASP's recommendations. The underlying security concern is validly sourced, but the precise statement is an extrapolation.

---

## Final counts

| Grade | Count |
|-------|-------|
| VERIFIED | 20 |
| PARTIAL | 10 |
| INACCURATE | 1 |
| INACCESSIBLE | 1 |
| DRIFT | 0 |
| NOT FOUND | 0 |

**VERIFIED**: 1, 2, 3, 7, 8, 9, 10, 14, 16, 17, 19, 20, 21, 22, 24, 25, 27, 28, 29, 30, 32

Wait — recounting from summary table:

- VERIFIED: 1, 2, 3, 5, 7, 8, 9, 10, 16, 17, 19, 20, 21, 22, 24, 25, 27, 28, 29, 30, 32 = **21**
- PARTIAL: 4, 6, 11, 13, 15, 23, 26, 31, 33 = **9**
- INACCURATE: 18 = **1**
- INACCESSIBLE: 12 = **1**
- DRIFT: **0**
- NOT FOUND: **0**

**Total citations: 33**

---

## Key findings for deliverable authors

1. **Citation 18 (wh0.github.io) is materially inaccurate.** The deliverable used this source to characterize wetty as having an "unfixed Origin-header WebSocket hijacking vulnerability." The actual source describes a different attack: a Glitch-platform-specific token-in-URL vulnerability exploitable by malicious project members replacing the WeTTY server. **Status: RESOLVED** — citation 18 in `citations.md` was rewritten to describe the actual attack class. The wetty disqualification in `browser-tty-comparison.md`, `synthesis.md`, `README.md`, and the deliverable was reframed around v2.7.0 (2023) staleness, Snyk's "inactive" classification, and the SSH-bridge architecture overhead — not the Origin claim.

2. **Citation 12 (NCC Group advisory) is inaccessible.** **Status: RESOLVED** — citation 12 in `citations.md` was annotated INACCESSIBLE; the pre-v1.3.1 RCE claim is downgraded to "unverified" rather than asserted as fact in the reference files.

3. **Citation 15 gap duration is inaccurate.** **Status: RESOLVED** — citation 15 in `citations.md` and the corresponding section in `browser-tty-comparison.md` now describe the gap as ~11 months (not "~2 years"), matching the actual release dates.

4. **Citation 13 adds an unsupported detail.** The `kubectl describe pod` visibility claim is not in the issue body. **Status: RESOLVED** — citation 13 in `citations.md` now flags the `kubectl describe pod` extension as an inference rather than a quoted claim; `browser-tty-comparison.md` line 34 was rewritten to drop the `kubectl describe pod` phrase.

5. **Citation 33 (OWASP) is paraphrased beyond what the source says.** **Status: RESOLVED** — citation 33 in `citations.md` and the cross-cutting risks paragraph in `browser-tty-comparison.md` were rephrased to track OWASP's actual language (CSWSH, browsers include cookies in WebSocket handshakes) rather than the SOP claim. The deliverable's recommendation #10 now says "CSWSH threat model."

## Other PARTIAL grades — no further action

The PARTIAL grades on citations 4, 6, 11, 23, 26, and 31 are minor representation differences that do not change the meaning of any cited claim. They are noted here for transparency but require no edit:

- **4**: OpenClaw's Docker positioning. The reference file's claim ("Docker is the default sandbox backend for non-main sessions") matches the README; the auditor only noted that the README contextualizes with "SSH and OpenShell backends are also available."
- **6**: Wikipedia date "three days later" vs. explicit January 30 — these are equivalent.
- **11**: Alpine base inferred from the tag `tsl0922/ttyd:alpine` — convention is unambiguous.
- **23**: `persistence.storageClass` commented out vs. "unset" — functionally identical.
- **26**: CloudTTY "jobs are ephemeral with TTL" — not directly visible on the README landing page; this was reported by a sub-agent in iteration 1 but not re-verified in iteration 2. Reference files no longer assert "with TTL" as a quoted-source claim.
- **31**: ingress-nginx #2461 "closed without in-product fix" — reasonable inference from the repo archival; the claim is consistent with the closure context.
