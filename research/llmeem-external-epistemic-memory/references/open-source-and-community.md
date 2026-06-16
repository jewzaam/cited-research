# Open Source and Community

## Author

Ben Thomasson — Senior Principal Software Engineer at Ansible by Red Hat [45][46]. Based in Raleigh, North Carolina. ~13 years at Red Hat before recently departing [46]. 847 public repositories on GitHub, 74 followers [45]. Member of @network-automation and @ftl-ai GitHub organizations [45].

Core expertise is in IT automation (Ansible, AWX) and network automation [45]. Pinned repositories are ansible/ansible (69K stars) and ansible/awx (15.5K stars) — organizational repos, not personal [45].

## Repositories

| Repository | Description | License | Stars | Forks | Downloads/month |
|-----------|-------------|---------|-------|-------|----------------|
| [ftl-reasons](https://github.com/benthomasson/ftl-reasons) | Full BMS (Doyle 1979) | Not specified | 0 | 1 | 321 (PyPI) |
| [ftl-beliefs](https://github.com/benthomasson/ftl-beliefs) | Simple markdown KB | MIT | 1 | 1 | 54 (PyPI) |
| [eem-expert](https://github.com/benthomasson/eem-expert) | Expert KB for EEM | MIT | — | — | — |
| [ftl2](https://github.com/benthomasson/ftl2) | AI-first automation | Apache-2.0 | 0 | 0 | — |

### ftl-reasons

Python implementation. Version 0.47.0 on PyPI [18]. 419 commits, 36 open issues, 1 open pull request [2]. 211 tests [2]. SQLite-backed. Dependencies include langchain-anthropic, sentence-transformers, mcp [18].

Download pattern shows sporadic, bursty activity (92 downloads in one day, 98 weekly, 321 monthly [18]) — suggesting automated or test-driven downloads rather than organic community adoption.

### ftl-beliefs

Version 0.2.0 on PyPI [17]. MIT license. Simpler tool using markdown files rather than database. 54 downloads/month [17].

### eem-expert

MIT license [16]. Contains 49 beliefs (19 premises, 30 derived), 0 nogoods, max derivation depth 3 [16]. Built with ftl-reasons 0.40.0 [16]. Includes evidence/ directory with methodology writeups and data/ directory with ablation questions and experiment harness [16].

## Public Belief Registry

expert.ftl2.com hosts the public belief registry [19]. Accessible via web browser. ~45 beliefs visible in the eem-expert KB. Export available in HTML, Markdown, and JSON formats [19]. References "40+ expert knowledge bases" across different domains [1], but no public listing of these KBs was found.

## Community Status

All evidence points to a single-developer project with minimal external engagement:

- 0–1 stars across repositories [2][17]
- 0–1 forks across repositories [2]
- No contributor guidelines, CODE_OF_CONDUCT, or CONTRIBUTING.md [2]
- No discoverable community forums, Discord, or communication channels
- Single contributor across all repositories [2]
- No published academic papers or conference presentations found
- No independent reviews or evaluations found

## Related Projects

The `ftl-ai` GitHub organization (referenced in Thomasson's profile [45]) appears to be private or have minimal public presence — web searches returned no results.

Other modern TMS implementations exist independently [counter-discovery]:
- hbeck/jtms — Justification-based Truth Maintenance System
- FellnerDotDev/ATMS-in-Python — Python 3 ATMS per de Kleer

The related "Memory as Metabolism" paper [14] references TMS as intellectual ancestor and LLMeem's framing of external epistemic memory, but is by a different author (Stefan Miteski, CODE University Berlin).

The PrecisionMemBench paper [13] (Jeffrey Flynt) argues a similar thesis — LLM memory as state management — using a different architecture (Tenure belief store with BM25 retrieval).

## License Concerns

The main ftl-reasons repository has no explicit license file visible on GitHub [2]. The companion tools use MIT (ftl-beliefs, eem-expert) and Apache-2.0 (ftl2) [16][17][47]. This inconsistency creates legal uncertainty for potential users of the core tool.

## Gaps and Limitations

1. **License ambiguity**: ftl-reasons license unspecified despite being the primary tool
2. **No community**: Zero external contributors, no community infrastructure
3. **No academic validation**: No peer-reviewed publications about LLMeem/EEM
4. **40+ KBs unverified**: Claimed expert knowledge bases not publicly listed or accessible
5. **Version gap**: eem-expert built with ftl-reasons 0.40.0 while current version is 0.47.0 — possible compatibility issues
