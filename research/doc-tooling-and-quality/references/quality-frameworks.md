# Documentation Quality Frameworks

Frameworks and heuristics for evaluating documentation quality, focused on practical applicability for a solo maintainer. Sources: [citations.md](../citations.md).

## Framework Comparison

| Framework | Focus | Practical Output | Solo Applicability | Effort to Apply |
|-----------|-------|-------------------|-------------------|-----------------|
| Diátaxis | Document classification | 4-type reorganization | High — clear audit process | Medium |
| Good Docs Project | Templates | Ready-to-use doc templates | High — pick and fill | Low |
| Tom Johnson's Checklist | Quality measurement | 75-item or 12-item checklist | High — self-assessment | Low-Medium |
| Nielsen's Heuristic #10 | Usability | Evaluation criteria | Medium — requires user testing | Medium |
| Every Page is Page One | Information architecture | Topic-based writing principles | High — design guidance | Medium |
| Google/Microsoft Guides | Writing style | Consistent voice and formatting | High — enforceable via Vale | Low |

## Diátaxis Framework

Created by Daniele Procida [23]. The core insight: "There isn't one thing called documentation, there are four" [23].

### The Four Types

Organized along two axes — theory/practice and studying/working [23]:

|  | Studying (learning) | Working (doing) |
|--|---------------------|-----------------|
| **Practical** | Tutorials | How-to Guides |
| **Theoretical** | Explanation | Reference |

- **Tutorials**: Guided learning experiences. The user follows along to gain skills.
- **How-to Guides**: Task-oriented steps for solving specific problems.
- **Reference**: Technical specifications, factual, complete.
- **Explanation**: Conceptual background, context, "why" discussions.

### How a Solo Developer Audits with Diátaxis

1. Inventory existing docs and classify each page by type
2. Identify pages that mix types (explanation buried in a how-to, reference scattered through tutorials)
3. Separate mixed content into distinct pages by type
4. Check coverage: do you have all four types where needed?

Daniele Procida clarified these are not "four rigid buckets" — they naturally emerge from analyzing user needs [24]. The framework "offers simplicity for solo developers: clear organizational logic without requiring complex tooling" [24].

### Case Study: Sequin

Before: disorganized, explanation-heavy docs leading with "How Sequin works" [25]. After applying Diátaxis:

- Rebuilt quickstart to show one core achievement in ~3 minutes [25]
- How-to guides for real scenarios surfaced product gaps — "If a guide felt too complex, we'd revisit the feature design" [25]
- Used "phantom links" to non-existent reference pages as a map of needed documentation [25]
- Used Claude to catch when explanation crept into how-tos [25]

Key lesson: "Engineers instinctively over-explain. Users need hands-on experience first, not comprehensive mental models upfront" [25].

### Diátaxis vs. Other Approaches

- **vs. DITA**: Diátaxis is less formal, not XML-based or tool-dependent. DITA emphasizes content reusability; Diátaxis focuses on user needs [24].
- **vs. Information Mapping**: Both chunk content, but IM uses different categories (procedure, process, principle, concept, structure, fact) [24].
- **vs. Good Docs Project**: Good Docs provides tactical templates; Diátaxis provides higher-level organizational principles [24]. They complement each other.

## Good Docs Project

Open source community producing documentation templates, maintained by 75+ experienced technical writers [26]. Templates organized in "packs" — latest release v1.5.0 ("Helix") [26]. Templates "guide you and your team through the process of creating great documentation" [26].

Templates include README, API references, how-to guides, tutorials, code of conduct, release notes, changelogs (from discovery agent). Templates embed quality standards through their structure — filling in a well-designed template produces documentation that meets basic quality standards without requiring the writer to know those standards explicitly.

### Solo Developer Application

Three-step process: pick templates for your needs, share with team (or just use them yourself), write documentation [26]. The templates work well with Diátaxis — you can select templates matching each Diátaxis type.

## Tom Johnson's Quality Checklist

~75 criteria in 6 categories [27]:

| Category | Items | Covers |
|----------|-------|--------|
| Findability | 11 | Search discoverability, navigation, site-specific search, release notes |
| Accuracy | 9 | Steps work, code samples run, information current |
| Relevance | 7 | Use case coverage, audience targeting |
| Clarity | 24 | Consistent terminology, placeholder indication, progressive complexity |
| Completeness | 8 | Authentication docs, error handling, all endpoints covered |
| Readability | 16 | Formatting, visual aids, paragraph length, heading hierarchy |

Johnson's advice for solo developers: "Limit scope to content you personally own." Use the shortened 12-item version for a "lightweight" approach [27]. "It might take more than a year working with the docs" to fully assess all criteria [27]. Criteria should be "specific, actionable, and unambiguous" [27].

## Nielsen's Usability Heuristics Applied to Documentation

Heuristic #10 (Help and Documentation) [28]:

1. Documentation must be **"easy to search"** — users locate information via search, not by browsing hierarchies
2. **"Present the documentation in context right at the moment that the user requires it"** — just-in-time help beats separate documentation
3. **"List concrete steps to be carried out"** — concise, actionable instructions over verbose explanations

Related: Information Scent theory [31] — users follow "scent" cues (link descriptions, headings, breadcrumbs) to estimate whether content will be useful. Weak scent means users leave for a different source. This applies directly to documentation navigation: heading clarity, link text quality, and structural cues determine whether users find what they need.

## Every Page is Page One

Mark Baker's framework [32]: bottom-up information architecture where every page is a potential entry point. Users arrive via search, not sequential reading. Each topic must be self-sufficient but interconnected.

Application: design each documentation page to work for someone who landed on it from Google, not someone who read the previous page.

## Style Guides as Quality Enforcement

Google Developer Documentation Style Guide [29]: freely available under Creative Commons Attribution 4.0. Establishes voice, tone, formatting, and terminology standards. Reference hierarchy: project-specific > Google guide > Merriam-Webster/Chicago Manual/Microsoft Guide [29].

Microsoft Writing Style Guide (from discovery agent): similar principles — casual/friendly tone, simple sentences, active voice.

Both guides have Vale packages, enabling automated enforcement. This transforms style guidance from aspirational documents into CI-enforced quality gates.

## Practical Solo Developer Audit Process

Combining frameworks into a lightweight audit:

1. **Classify** (Diátaxis): categorize each doc page as tutorial/how-to/reference/explanation
2. **Check coverage** (Diátaxis): identify missing types
3. **Score** (Johnson's 12-item checklist): quick quality pass
4. **Test findability** (Nielsen): can you find each page via search and navigation?
5. **Enforce style** (Vale + style guide): automate what can be automated

## Gaps and Limitations

- No peer-reviewed studies comparing framework effectiveness (which approach produces measurably better documentation?)
- Diátaxis adoption evidence is primarily case studies, not controlled experiments
- Tom Johnson's checklist is designed for API documentation — some criteria need adaptation for project docs
- Nielsen's heuristics were designed for UI evaluation, not documentation specifically — Heuristic #10 is the most directly applicable
- No quantitative benchmarks for "good enough" documentation quality
