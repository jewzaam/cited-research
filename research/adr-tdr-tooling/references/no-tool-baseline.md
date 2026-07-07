# "No Tool" Baseline

Dimension grounding the comparison: plain markdown + naming convention + git.
What do you lose vs. what a tool provides?

Sources: [citations](../citations.md) referenced as [N].

## The Minimal Approach

The simplest ADR setup requires no tool [8][22][38]:

1. Create a directory: `docs/decisions/` or `doc/adr/`
2. Copy a template file with a numbered name: `0001-title.md`
3. Edit in any text editor
4. Commit to git alongside code
5. Use pull requests for review

Common directory conventions [38]:
- `docs/adr/`, `doc/adr/`, `adr/`
- `architecture/decisions/`, `docs/architecture/`
- `decisions/` (broader scope beyond architecture)

File naming: `NNNN-title-with-dashes.md` [7][38]

## What You Keep Without Tools

| Capability | How |
|-----------|-----|
| Version control | Git tracks all changes [8][22] |
| Searchability | grep, IDE search, GitHub search [22] |
| Readability | Any text editor, GitHub/GitLab rendering [22] |
| Review workflow | Pull requests [8][22] |
| Co-location with code | Same repo [8][22] |
| Zero maintenance | No dependencies to update |
| Cross-platform | Markdown works everywhere |

Martin Fowler's guidance centers on this approach — the only tool he
mentions is adr-tools, described merely as "a simple command line tool" [8].
The Red Hat blog reinforces: "co-location with source code matters more than
tooling" and "pull requests handle the workflow natively" [22].

## What You Lose Without Tools

| Capability | Impact | Counter |
|-----------|--------|---------|
| Auto-numbering | Manual tracking, collision risk [33] | Acceptable for solo/small team |
| Superseding links | Manual status updates in old ADR | Error-prone at volume |
| Template enforcement | Inconsistent records [29] | Code review catches this |
| Index generation | Manual TOC maintenance | grep + find sufficient for <50 ADRs |
| Status lifecycle | Manual state transitions | Discipline-dependent |
| Visualization | No decision chain graphs [28] | Rarely needed in practice |
| Cross-repo discovery | No unified search [1] | Backstage plugin solves this separately |

## The "In-Repo Markdown" Consensus

Multiple independent sources converge on in-repo markdown as the most popular
and often sufficient approach:

- "In-repo markdown is most popular approach 'for good reason'" [50]
- "Co-location with source code matters more than tooling" [22]
- "No complex tools needed; basic template + version control + consistent
  updates are sufficient" [22]
- "Simple markdown + git is sufficient" for many teams [22]
- Fowler: lightweight Markdown stored in `doc/adr` [8]

## When No-Tool Breaks Down

### Concurrency Collisions [33]
The most concrete failure mode. When two developers create ADRs in parallel
PRs, both assign the same number. The MADR repo documents this as a known
issue [33]. Proposed solutions (lock files) still rely on developer discipline.

Automated numbering in any CLI tool (adr-tools [9], adrs [11], ADG [10])
eliminates this entirely.

### Scale Limits [50][25]
ADR collections exceeding ~50 records become difficult to browse without
indexing or search tooling. Cross-repo visibility requires infrastructure
(Backstage plugin [1]).

### Write-Only Graveyards [44]
ADRs are written but never read. This failure mode affects tooled and
no-tool approaches equally [44]. The solution is cultural (triggers, review
habits), not tooling.

### Enforcement Gaps [35]
"Recording a decision is pointless if agents never read it" [35]. Without
enforcement hooks, ADRs become suggestions rather than constraints.
Deterministic hooks and validation are needed for AI agent compliance [35].

## The Agent Consumption Angle

For AI agents specifically, no-tool markdown is surprisingly viable because:

1. **LLMs read any markdown** — no special format needed for comprehension [36]
2. **Plain AGENTS.md outperforms complex systems** for agent memory (74% vs
   68.5%) [36]
3. **Markdown-KV format beats CSV** for LLM accuracy (60.7% vs 44.3%) [37]
4. **Over-structuring harms reasoning** — strict schemas degrade LLM
   performance on reasoning tasks [18]

However, no-tool lacks the *filtering* capability that YAML frontmatter
provides. An agent that needs to find "all accepted database decisions" must
parse free-form text rather than querying structured metadata [5].

## Recommendation Threshold

Based on the evidence, the no-tool baseline is sufficient when:
- Single developer or small team (≤5)
- ADR volume stays below ~30-50
- No cross-repo discovery needed
- No CI/CD validation required
- Agent consumption is read-all, not filter-by-metadata

A tool becomes justified when any of these conditions no longer holds.

## Gaps and Limitations

- No empirical study compares ADR maintenance quality between tooled and
  no-tool approaches
- "50% of repos with <5 ADRs" abandonment claim found in search snippets
  but not substantiated [from counter-discovery agent]
- The concurrency collision [33] is documented but its frequency in practice
  is unknown
- No data on how many teams use the no-tool approach vs. dedicated tooling
