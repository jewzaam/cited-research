# StackBlitz / WebContainers

Dimension: how StackBlitz's WebContainers solve the four recurring problems, and which design ideas (if any) transfer to a server-hosted sandbox. Sources in [citations.md](../citations.md).

## Architectural orientation — why this product is different

WebContainers run the *workspace itself* inside the browser tab. "WebContainers are a browser-based runtime for executing Node.js applications and operating system commands, entirely inside your browser tab" [29]. The runtime is "a WebAssembly-based operating system powerful enough to run Node.js" with "a virtualized TCP network stack that's mapped to your browser's ServiceWorker API" [33]. "100% of code execution occurs in the browser security sandbox" [33].

This architectural choice inverts every other product in the survey. There is no server-side sandbox to defend, no scheduler to design, no per-user namespace to provision. The four recurring problems mostly become non-problems — at the cost of being unable to run anything the user agent can't run.

## Session persistence

The filesystem is in-memory: "WebContainer API gives you access to work with a virtual file system, right in memory" [32]. Mount format is a nested object — `{ 'package.json': { file: { contents: '...' } } }` with directories as `{ src: { directory: { ... } } }` [32]. The runtime itself does not persist anything across page reload — persistence is delegated to (a) the embedding application's IndexedDB / localStorage writes of the working tree, or (b) Git: StackBlitz's Codeflow UI commits and pushes back to GitHub. "Only a single instance of WebContainer can be booted concurrently" [31]; restart requires `teardown()` first.

The portable design lesson: treat the sandbox as ephemeral and Git as the truth. The Git-as-persistence pattern shows up across the survey but is most explicit here, because there is no other option.

## Browser access UX

Two browser-side hard requirements: `Cross-Origin-Embedder-Policy: require-corp` and `Cross-Origin-Opener-Policy: same-origin` [30]. "WebContainer requires SharedArrayBuffer, which, in turn, requires your website to be cross-origin isolated" [30] — Atomics + SAB underpin atomic file writes and the locks Node expects. The COOP/COEP requirement is a real integration constraint for embedders: the *hosting page* must be cross-origin isolated, which constrains what third-party resources can be embedded.

The most portable UX pattern is **URL-as-entry-point**. Replace `github.com` with `pr.new` in any repo or PR URL and it opens in the Codeflow IDE; PR URLs auto-spin in 'PR Review mode' for side-by-side comparison [34]. This is a low-cost onboarding affordance that transfers cleanly to a server-hosted sandbox — a homelab could host a `pr.your-domain` shim that swaps to the local dev environment.

## Multi-tenant isolation

The tenancy boundary is the browser tab. The user agent enforces same-origin separation; each project running in its own origin gets process-level isolation from the OS. There is no shared tenant boundary that StackBlitz must defend at runtime. The defended boundary is the integration boundary — StackBlitz must require embedders to enable cross-origin isolation, which protects the embedder's other origins from the WebContainer process.

For a server-hosted sandbox this doesn't transfer directly. But the design principle does: **make the trust boundary visible and structural, not configurable**. The COOP/COEP requirement is non-bypassable — if the page isn't isolated, the runtime refuses to boot. That's harder to mis-deploy than a config-flag.

## Credential injection

WebContainers ship no first-class secrets primitive. Env vars are set per-spawned-process via the `spawn()` `options.env` field: `env?: Record<string, string | number | boolean>` [31]. The runtime API does not surface a secret store; secrets that an embedded app needs are either typed into a form (writes to env on next spawn), set by the embedding page before boot, or read from query strings — all of which mean secrets traverse the browser. The discovery agent surfaced explicit external-ecosystem caution about this pattern in the AI-sandbox context (Bolt.diy issue #1730).

For a server-hosted sandbox: the *anti-lesson* from WebContainers is that env-var-only secrets injection is fragile when the host is untrusted. The credential-brokering patterns from Coder and Daytona transfer better than the WebContainers approach.

## What does and does not transfer to a server-hosted sandbox

Transfers cleanly:
- URL-as-entry-point onboarding [34].
- Treat persistence as Git; sandbox is ephemeral.
- One-instance-per-session boot lifecycle simplifies isolation reasoning [31].
- Structural (not config-flag) enforcement of trust-boundary requirements [30].

Does not transfer:
- Runtime substrate (WASM + ServiceWorker) is browser-bound.
- "100% in browser security sandbox" tenancy model is not available server-side.
- Performance characteristics (`spinning up the entire dev environment in milliseconds` [29]) come from the absence of cold-start network round-trips and don't apply to a server sandbox.

## Gaps

- No StackBlitz-published page on credential-injection patterns surfaced [29–34].
- Per-project subdomain scheme (`*.local-credentialless.webcontainer.io` per discovery) not confirmed at primary source in this pass.
- CDN-cached npm layer pattern (~500 ms install) reported by discovery agent (PostHog/Bolt writeup); not in the WebContainers docs themselves.
