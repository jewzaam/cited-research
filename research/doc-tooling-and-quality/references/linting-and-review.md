# Documentation Linting and Review Tools

Comparison of linting tools for documentation quality enforcement. Sources: [citations.md](../citations.md).

## Tool Comparison Matrix

| Tool | Language | Focus | Custom Rules | Style Guides | CI Integration | False Positive Mgmt | Solo Setup |
|------|----------|-------|--------------|--------------|----------------|---------------------|------------|
| Vale | Go | Prose/style | YAML (11 check types) [12] | Google, Microsoft, write-good [11] | Official GH Action [20] | Vocabularies, inline suppression [12] | Medium |
| markdownlint | Node.js | Markdown structure | JavaScript API [14] | N/A (structural) | Multiple GH Actions [14] | Inline comments, config ignores [14] | Easy |
| textlint | Node.js | Pluggable (anything) | Plugin system [16] | Via plugins [16] | Custom setup [16] | Per-plugin [16] | Hard |
| alex | Node.js | Inclusive language | Limited [17] | Built-in [17] | Via textlint or Vale [17] | .alexrc.js config [17] | Easy |
| lychee | Rust | Link checking | N/A | N/A | Official GH Action [19] | Config excludes [18] | Easy |

## Recommended Stack: Vale + markdownlint + lychee

The Earthly blog's analysis concludes that combining tools is superior to using any single tool [13]:

- **markdownlint** handles structural validation: "It can't be beaten for dealing with markdown structure" [13]. 60+ built-in rules, 32 support autofix [14]. Catches heading hierarchy, list formatting, trailing whitespace, line length.

- **Vale** handles prose quality: "Most comprehensive option for teams serious about documentation quality" [13]. Combines spelling, grammar, and clarity checks with pre-packaged style guides. "Vale is fast and configurable but not necessarily easy to get started with" [13].

- **lychee** handles link integrity: Rust-based async checker, "designed for speed, making it perfect for large projects" [18]. Single static binary with no runtime dependencies [18].

The Earthly blog itself "uses Vale and markdownlint in an Earthfile for every commit" [13].

## Vale Deep Dive

### Architecture

Open-source CLI written in Go [11]. Runs entirely offline — content never sent to remote servers [11]. Cross-platform single binary — no Python/Node.js runtime needed [11]. 3M+ downloads, 4,500+ GitHub stars [11].

### Rule System

YAML-based rules with 11 built-in check types [12]:

| Check Type | Purpose |
|-----------|---------|
| existence | Match regex patterns |
| substitution | Replace patterns with preferred terms |
| occurrence | Ensure patterns appear N times |
| repetition | Flag repeated patterns |
| consistency | Enforce consistent usage |
| conditional | Pattern checks with conditions |
| capitalization | Validate casing rules |
| metric | Readability formulas |
| spelling | Hunspell dictionaries |
| sequence | POS-tagged pattern ordering |
| script | Custom Tengo scripts |

Every rule requires `extends` (check type) and `message` fields. Optional: `level` (suggestion/warning/error), `scope`, `link`, `limit` [12].

### Style Guide Packages

Pre-packaged implementations available for Google, Microsoft, write-good, proselint, alex [11][12]. Installed via `Packages` in `.vale.ini` and `vale sync` command. Vale's separation of styles from the tool "enables reusability across projects" [13] — critical for a solo developer maintaining multiple repos with consistent standards.

### CI Integration

Official GitHub Action (vale-cli/vale-action) with reporter options: github-pr-check, github-pr-review, github-check [20]. Requires Vale >= 2.16.0 [20].

## markdownlint Deep Dive

60+ built-in rules with 32 supporting autofix [14]. Performance-optimized variant (markdownlint-cli2) handles large repositories better, with .gitignore mode for faster tree traversal [15]. Custom rules authored in JavaScript [14]. VSCode extension provides inline fixes and auto-fix-on-save [14].

## Other Tools

**textlint**: Maximum flexibility through plugin architecture, but "harder to set up and configure" [13]. Ships with no built-in rules — each capability installed separately [16]. Requires Node.js >= 20 [16]. Best when you need capabilities no other tool offers.

**alex**: Specialized for inclusive language. Detects gender, race, religion, ableist, condescending patterns [17]. Available as standalone, textlint plugin, or Vale package [17]. Prone to false positives [17].

**proselint**: Python-based prose linter aggregating advice from style experts [21]. "Ignoring and excluding rules are also not fully supported" [13]. Available as Vale package.

**write-good**: Detects passive voice, lexical illusions, weakening adverbs [22]. "Rich clarity suggestions but lacks rule customization for CI environments" [13]. Available as Vale package.

**markdown-link-check**: Node.js alternative to lychee with JUnit reporter [22]. Slower than lychee but adequate for smaller projects. (From discovery agent.)

## False Positive Management

The severity level strategy matters for adoption: start with `suggestion` or `warning` for new rules, graduate to `error` only after tuning [12]. Vale supports custom vocabularies (accept.txt/reject.txt) to suppress legitimate terms flagged as spelling errors [12]. Inline suppression comments available in both Vale and markdownlint [12][14].

## Gaps and Limitations

- No published false positive rate comparisons across tools on standardized corpora
- No systematic benchmarks comparing Vale (Go) vs markdownlint (Node.js) performance
- Custom rule authoring learning curve is qualitatively described but not measured
- RedPen (Java-based, multi-format including LaTeX) exists but has limited recent adoption evidence
