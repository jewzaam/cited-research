# Comparison with Dedicated Tools

Dimension covering when GitHub Issues kanban is sufficient vs. when to consider dedicated PM tools.

Sources: see [citations.md](../citations.md) for full details.

## Feature Comparison

| Feature | GitHub Projects | Jira | Linear |
|---------|----------------|------|--------|
| Kanban board | Yes [1] | Yes | Yes |
| Scrum support | Basic (iterations) [1] | Full (sprints, velocity, burndown) | Yes |
| Custom workflows | Limited (Actions required) [2] | Fully customizable transitions | Yes |
| Reporting | Minimal [24] | Advanced analytics | Good |
| Hierarchy | Sub-issues (beta) [9] | Epics → Stories → Subtasks | Projects → Issues |
| Dependencies | Blocked by / Blocking [7][8] | Full dependency types + cross-project | Yes |
| Marketplace | Growing | 5,000+ apps [31] | Growing |
| Pricing | Free with GitHub [24] | $7.53/user/month [24] | $8/user/month |

## Cost Comparison

| Plan | GitHub | Jira |
|------|--------|------|
| Free tier | Unlimited repos, Projects included [24] | 10 users [24] |
| Team/Standard | $4/user/month [24] | $7.53/user/month [24] |
| Enterprise | GitHub Enterprise pricing | $14.50/user/month (Premium) [24] |

For teams already on GitHub, Projects is effectively zero additional cost [24].

## Team Size Thresholds

Multiple sources consistently identify team size as the key decision factor [24][39]:

| Team Size | Recommendation |
|-----------|---------------|
| Under 20 developers | GitHub Projects likely sufficient [24] |
| 20-30 developers | Transition zone; evaluate specific needs [24] |
| Over 30 developers | Consider dedicated tools if needing Agile metrics, hierarchy, or cross-project management [24] |

## When GitHub Projects is Sufficient

- Small to mid-size teams with straightforward workflows [24]
- Developer-centric teams that live primarily in code [24]
- Teams wanting zero context-switching between code and PM [24]
- Open source projects where all contributors have GitHub accounts [30]
- Teams that value simplicity over extensive customization [24]

## Migration Triggers (GitHub → Dedicated Tool)

Teams typically migrate when [20][24]:
1. Team exceeds 30 developers [24]
2. Non-technical stakeholders need regular access [20]
3. Advanced Agile metrics required (velocity, burndown, forecasting) [24]
4. Multi-level hierarchy needed (epic → story → subtask) [19]
5. Cross-project portfolio management required [24]
6. Regulatory compliance demands formal workflow approvals [24]

## Migration Stories: Jira → GitHub

Notable projects that moved FROM Jira TO GitHub Issues:

**Spring Framework (2019)** [29]:
- Motivation: single login/platform, markdown simplicity, unified view
- Challenge: markup conversion ("most painful part"), 25 Jira components → 5 GitHub labels
- Source was inaccessible during verification

**Apache Accumulo (2018)** [30]:
- Selective migration (only active/community-interest issues)
- Creating issue before PR made optional (reduced contributor friction)
- JIRA transitioned to read-only
- Pragmatic, iterative approach

**Common reasons for Jira → GitHub migration** [29][30]:
1. Single platform reduces login/context-switching overhead
2. Markdown better for code-related discussions
3. Tighter integration with development workflow
4. Reduced administrative burden

## GitHub's Feature Gap Trajectory

GitHub is actively closing feature gaps:
- Dependencies: GA August 2025 [7]
- Sub-issues: Public beta October 2024 [9]
- Item limits: Expanded to 50,000 (from 1,200) [5]
- Agentic Workflows: Technical preview February 2026 [27]

The trajectory suggests the "good enough" threshold is steadily rising, though enterprise-grade reporting and hierarchy remain gaps [20][24].

## Gaps and Limitations

- Limited quantitative data on "good enough" thresholds (mostly qualitative) [24]
- Spring Framework migration source was inaccessible [29]
- Cost comparisons don't include total cost of ownership (training, maintenance, integration)
- Few sources from 2025-2026 time period addressing recent GitHub improvements
