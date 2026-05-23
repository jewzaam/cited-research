# Citations

All URLs visited in-session via WebSearch, multi-engine search (DuckDuckGo via `scripts/multi_search.py`), or WebFetch on 2026-05-23. Tier per [SKILL.md §Phase 1 Principles](https://github.com/anthropics/cited-research): 1 = peer-reviewed/government, 2 = manufacturer/established reference/university, 3 = industry blog/tech press, 4 = forum/personal blog/issue/social.

## NVIDIA OpenShell

1. **NVIDIA/OpenShell repository.** Tier 2. https://github.com/NVIDIA/OpenShell — Project description "OpenShell is the safe, private runtime for autonomous AI agents." Apache 2.0. Rust 89.6% of codebase. Supports Docker, Podman, MicroVM, and Kubernetes compute drivers. Alpha-stage ("proof-of-life: one developer, one environment, one gateway"). Operator interaction is CLI (`openshell sandbox create`, `openshell policy set`) plus optional TUI dashboard (`openshell term`); no browser-based terminal mentioned.

2. **NVIDIA/OpenShell releases.** Tier 2. https://github.com/NVIDIA/OpenShell/releases — Latest 5 tags: v0.0.47 (2026-05-22), v0.0.46 (2026-05-21), v0.0.45 (2026-05-20), v0.0.44 (2026-05-19), v0.0.43 (2026-05-18). ~Daily release cadence.

3. **htek.dev — NVIDIA OpenShell: The Sandbox Your AI Agents Should Be Running In.** Tier 3. https://htek.dev/articles/nvidia-openshell-sandbox-ai-agents — "NVIDIA open-sourced OpenShell at GTC 2026 — a policy-driven sandbox for AI agents." Third-party confirmation of GTC 2026 launch and contributor (Copilot CLI provider).

## OpenClaw

4. **openclaw/openclaw repository.** Tier 2. https://github.com/openclaw/openclaw — "OpenClaw is a personal AI assistant you run on your own devices. It answers you on the channels you already use." MIT license. TypeScript (with Swift for macOS/iOS). Operator interfaces: CLI (`openclaw onboard`, `openclaw gateway`, `openclaw agent --message "..."`), macOS menu-bar app with voice wake, iOS/Android nodes, WebChat. Docker listed as "the default sandbox backend for non-main sessions." No official Helm chart or Kubernetes operator in README. 374k stars, 51,743 commits on main as of 2026-05-23 fetch.

5. **openclaw.ai — official site.** Tier 2. https://openclaw.ai/ — Marketed as personal AI assistant for mail, Beeper messages, ordering, reminders, GitHub issues, bookmarks, voice calls, 1Password vault management.

6. **Wikipedia — OpenClaw.** Tier 2. https://en.wikipedia.org/wiki/OpenClaw — Created by Austrian developer Peter Steinberger. Initial release November 2025 as "Clawdbot." Renamed "Moltbot" 2026-01-27 (Anthropic trademark complaint), renamed "OpenClaw" three days later. Steinberger joined OpenAI 2026-02-14 with plans for non-profit foundation to oversee project. MIT license. 247,000 stars and 47,700 forks as of 2026-03-02.

7. **steipete.me — OpenClaw, OpenAI and the future.** Tier 3. https://steipete.me/posts/2026/openclaw — Creator's blog post (2026-02-15) on next direction.

## ttyd

8. **tsl0922/ttyd repository.** Tier 2. https://github.com/tsl0922/ttyd — Features built on libuv and WebGL2; CJK/IME support; ZMODEM/trzsz file transfer; Sixel images; SSL; cross-platform. Authentication options: `-c, --credential username:password` (HTTP Basic) and `-H, --auth-header` (trust an upstream header). Concurrency flags: `-m, --max-clients` (default: unlimited), `-o, --once` (exit after first client disconnect), `-q, --exit-no-conn`. Default port: 7681. Terminal type flag: `-T, --terminal-type` (default `xterm-256color`). Languages: 56% C, 26.4% TypeScript. Last commit: 2024-03-30 (release v1.7.7).

9. **tsl0922/ttyd releases.** Tier 2. https://github.com/tsl0922/ttyd/releases — Last 5 releases: 1.7.7 (2024-03-30), 1.7.6 (2024-03-29), 1.7.5 (2024-03-27), 1.7.4 (2023-10-02), 1.7.3 (2023-01-18). Release notes for 1.7.4 flag a breaking change: web terminal read-only by default, requires `-W` to enable writing.

10. **tsl0922/ttyd wiki — Auth Proxy.** Tier 2. https://github.com/tsl0922/ttyd/wiki/Auth-Proxy — `-H, --auth-header` makes ttyd trust the `X-WEBAUTH-USER` header. Documentation states: "Since the auth proxy feature will make ttyd trust any request with none empty `X-WEBAUTH-USER` header value, you should always start ttyd on a unix domain socket." Examples for Apache `RequestHeader set X-WEBAUTH-USER` and nginx `proxy_set_header X-WEBAUTH-USER $remote_user;`.

11. **Docker Hub — tsl0922/ttyd.** Tier 2. https://hub.docker.com/r/tsl0922/ttyd — `tsl0922/ttyd:alpine` compressed size 6.9 MB. Alpine Linux base.

12. **NCC Group — Technical Advisory: Remote Shell Commands Execution in ttyd.** Tier 1 (security firm advisory). https://research.nccgroup.com/2017/09/08/technical-advisory-remote-shell-commands-execution-in-ttyd/ — Pre-v1.3.1 unauthenticated RCE via `LWS_CALLBACK_RECEIVE` callback claim. **Source is INACCESSIBLE as of 2026-05-23** — URL returns a 307 redirect to https://www.nccgroup.com/research/ with no trace of the specific advisory. Historical claim cannot be verified from this URL. Reference files should treat the pre-v1.3.1 RCE assertion as unverified.

13. **tsl0922/ttyd issue #872 — credential plaintext exposure.** Tier 4. https://github.com/tsl0922/ttyd/issues/872 — `-c user:pass` stored as plaintext CLI argument, visible in `ps aux`. Feature request for hashed/file-based credentials, open as of search date. (The further extrapolation to `kubectl describe pod` visibility is not in the issue body itself but is a derivative consequence of running on Kubernetes — flagged here as an inference rather than a quoted claim.)

## gotty (sorenisanerd fork)

14. **sorenisanerd/gotty repository.** Tier 2. https://github.com/sorenisanerd/gotty — "Share your terminal as a web application." MIT. Authentication: `-c user:pass` (basic, plaintext-on-wire warning), `-t` + `-tls-crt`/`-tls-key` (TLS), `--tls-ca-crt` (TLS client cert), `-r` random URL with `--random-url-length` (default 8), `--pass-headers` (HTTP request headers → env vars). Multi-client behavior: "GoTTY starts a new process with the given command when a new client connects to the server." For shared session, recommends tmux or screen. Write permission requires explicit `-w` flag ("BE CAREFUL"). Config file: `~/.gotty`.

15. **sorenisanerd/gotty releases.** Tier 2. https://github.com/sorenisanerd/gotty/releases — Latest: v1.7.2 (2026-05-17). Recent cadence: v1.7.1 (2026-05-14), v1.7.0 (2026-05-14), v1.6.0 (2025-08-03), v1.5.1 (2025-08-03), v1.5.0 (2024-09-01). ~11-month gap between v1.5.0 (2024-09-01) and v1.6.0 (2025-08-03), then a ~9-month gap to the May 2026 release burst.

## wetty

16. **butlerx/wetty repository.** Tier 2. https://github.com/butlerx/wetty — "Terminal access in browser over HTTP/HTTPS, using xterm.js with WebSocket support." MIT. Last release v2.7.0 (2023-09-16). Authentication: SSH password (default), SSH public key via `--ssh-auth publickey`, `--ssh-key` for passwordless ("connection will be password-less and insecure!"), `--ssh-config` custom config file, `--force-ssh` even when running as root. Default port: 3000. Multi-client session behavior not explicitly documented in README. No explicit "maintenance mode" or "archived" banner.

17. **Snyk Advisor — wetty (npm package).** Tier 2. https://security.snyk.io/package/npm/wetty — Reports wetty as having limited maintenance signal. Latest npm publish v2.7.0; no recent npm release in >12 months as of 2026 search.

18. **wh0.github.io — Compromised by an embedded wetty in Glitch.** Tier 4. https://wh0.github.io/2023/08/19/wetty-origin.html — Personal blog documenting an attack on wetty as deployed inside Glitch. A malicious project member could replace the WeTTY server with one that served a page exposing the persistent auth token via the URL (a token-in-URL / content-injection class of vulnerability). The writeup does **not** describe a WebSocket Origin-header validation flaw despite the URL slug suggesting otherwise. Glitch's mitigation was platform-side (short-lived tokens, separating client serving from project containers), not an upstream wetty patch.

## code-server

19. **coder/code-server repository.** Tier 2. https://github.com/coder/code-server — "Run VS Code on any machine anywhere and access it in the browser." MIT. Latest v4.121.0 (2026-05-20). Requirements stated: "1 GB RAM, and 2 vCPUs."

20. **coder/code-server releases.** Tier 2. https://github.com/coder/code-server/releases — Latest: v4.121.0 (2026-05-20). Prior 4: v4.118.0 (2026-05-06), v4.117.0 (2026-04-23), v4.116.0 (2026-04-16), v4.115.0 (2026-04-08). Approx weekly cadence aligned to upstream VS Code.

21. **code-server security advisory GHSA-p483-wpfp-42cj (CVE-2025-47269).** Tier 2 (vendor self-disclosure). https://github.com/coder/code-server/security/advisories/GHSA-p483-wpfp-42cj — Title: "Session cookie can be extracted by having user visit specially crafted proxy URL." CVSS 8.3 (`CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:L`). Affected: <4.99.4. Fixed: ≥4.99.4. Description: improper port validation in `/proxy/` subpath allows crafted URLs to relay session cookies to attacker-controlled domains. Published 2025-05-09.

22. **Coder docs — code-server guide.** Tier 2. https://coder.com/docs/code-server/guide — Authentication: password by default (rate-limited "two per minute plus an additional twelve per hour"), `auth: none` config option for SSH-tunneled use, external authentication via reverse proxy. Named integrations: Pomerium, oauth2-proxy, Cloudflare Access. Recommended reverse proxies: Caddy with Let's Encrypt, NGINX with Let's Encrypt, SSH port forwarding. Explicit warning: "Never expose code-server directly to the internet without some form of authentication and encryption."

23. **code-server Helm chart values.yaml.** Tier 2. https://github.com/coder/code-server/blob/main/ci/helm-chart/values.yaml — Defaults: `persistence.enabled: true`, `persistence.size: 10Gi`, `persistence.accessMode: ReadWriteOnce`, `persistence.storageClass` unset, `persistence.existingClaim: ""`, `ingress.enabled: false`, `ingress.ingressClassName: ""`, `image.repository: codercom/code-server`, `image.tag: 4.121.0`, `image.pullPolicy: Always`. Resource limits/requests commented out by default.

24. **code-server install docs — Helm section.** Tier 2. https://github.com/coder/code-server/blob/main/docs/install.md — Brief "Helm" section pointing to coder.com/docs/code-server/latest/helm.

25. **Docker Hub — codercom/code-server.** Tier 2. https://hub.docker.com/r/codercom/code-server/tags — `latest` tag (= v4.121.0) compressed size: 265.68 MB (linux/amd64), 265.08 MB (linux/arm64). Debian base. Supported architectures: linux/amd64, linux/arm64.

## CloudTTY

26. **cloudtty/cloudtty repository.** Tier 2. https://github.com/cloudtty/cloudtty — Kubernetes-native operator for web terminal access. MIT license. Helm install commands: `helm repo add cloudtty https://cloudtty.github.io/cloudtty && helm repo update && helm install cloudtty-operator --version <V> cloudtty/cloudtty`. Supported exposure modes: NodePort (default), ClusterIP, Ingress, Istio VirtualService. CRD: kind `CloudShell`, group `cloudshell.cloudtty.io/v1alpha1`. Each CloudShell pod runs ttyd inside ("the ttyd binary inside the container also comes from ttyd project"). No persistence story documented for shell state; jobs are ephemeral with TTL.

27. **cloudtty/cloudtty releases.** Tier 2. https://github.com/cloudtty/cloudtty/releases — Latest: cloudtty-0.8.9 (2025-01-27). Prior: 0.8.8 (2024-11-17), 0.8.7 (2024-07-22), 0.8.6 (2024-05-21), 0.8.5 (2024-03-21). The CloudTTY official docs still reference 0.5.0 in their quick-start, which lags actual releases.

## Kubernetes / Ingress / Argo CD

28. **Tailscale docs — Kubernetes Operator: Expose a cluster Service to your tailnet.** Tier 2. https://tailscale.com/kb/1439/kubernetes-operator-cluster-ingress — Prerequisite: "You must enable HTTPS and MagicDNS on your tailnet." Set `spec.ingressClassName: tailscale` on a standard Kubernetes Ingress resource. TLS hostname defaults to `<ingress-name>-<namespace>`; customize via `tls.hosts` (first label only). Certificates from Let's Encrypt, provisioned lazily: "Currently, the certificates are provisioned on the first connect. This means that the first connection might be slow or even time out."

29. **Traefik docs v3.4 — WebSocket user guide.** Tier 2. https://doc.traefik.io/traefik/v3.4/user-guides/websocket/ — "WebSocket is a communication protocol that provides full-duplex communication channels over a single TCP connection" and "Traefik supports WebSocket and WebSocket Secure (WSS) out of the box." No special headers, middlewares, or annotations required for basic WebSocket. WSS adds `tls: {}` and uses `websecure` entryPoint. No sticky-session discussion for single-pod backends.

30. **kubernetes/ingress-nginx repository.** Tier 2. https://github.com/kubernetes/ingress-nginx — Archive notice: "This repository was archived by the owner on Mar 24, 2026. It is now read-only." Project recommends Gateway API implementations as the migration path. Existing Helm charts and container images remain available; no further releases, bug fixes, or security updates.

31. **ingress-nginx issue #2461 — WebSocket dropped on backend reload.** Tier 4. https://github.com/kubernetes/ingress-nginx/issues/2461 — "Ingress controller dropping websocket connections when performing backend reload." Reproduced across versions 0.12.0 and 0.14.0. Reporter expected: "Websockets should be left connected to the target server" despite backend configuration changes. Issue closed as part of repo archival 2026-03-24 without an in-product fix.

32. **Argo CD docs — ApplicationSet List Generator.** Tier 2. https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Generators-List/ — "The List generator generates parameters based on an arbitrary list of key/value pairs (as long as the values are string values)." Each list element becomes template variables (Go template syntax: `{{.cluster}}`, `{{.url}}`). One Application per list element, parameterized by element fields.

33. **OWASP Cheat Sheet — WebSocket Security.** Tier 1. https://cheatsheetseries.owasp.org/cheatsheets/WebSocket_Security_Cheat_Sheet.html — Describes Cross-Site WebSocket Hijacking (CSWSH). Browsers include cookies in WebSocket handshake requests, so a tool that relies solely on cookie-based authentication is vulnerable to CSWSH from a concurrently open malicious origin unless the server validates the `Origin` header or uses a per-handshake CSRF token. The phrasing "browsers do not enforce Same-Origin Policy on WebSocket handshakes" is an interpretation of the page, not a direct quote.

## Sources noted but not verified in-session

The following URLs surfaced during discovery and are mentioned here so a future revisit can complete verification. Each was reported by a sub-agent based on search snippets; full-page content was not fetched in this iteration. **Do not cite these from the deliverable without first verifying their contents.**

- https://www.oasis.security/blog/openclaw-vulnerability — "ClawJacked" WebSocket localhost hijacking claim (Tier 3).
- https://thehackernews.com/2026/05/four-openclaw-flaws-enable-data-theft.html — "Claw Chain" 4-CVE claim (Tier 3).
- https://thehackerwire.com/vulnerability/CVE-2026-44113/ and CVE-2026-44112/CVE-2026-44115 — OpenShell CVE claims (Tier 3-4). The CVE numbering and severity were extracted from a single source family and have not been cross-referenced with NIST NVD or NVIDIA's own security advisory page in this session.
- https://github.com/openclaw/openclaw/security/advisories/GHSA-h9g4-589h-68xv — OpenClaw auth-bypass advisory claim (Tier 2 if real).
- https://github.com/yudai/gotty — original gotty repo archive status not verified.
