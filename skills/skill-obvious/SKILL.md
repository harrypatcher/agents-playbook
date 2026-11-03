---
name: skill-obvious
description: 'requests for practical obvious or non-obvious tips, tricks, hacks, shortcuts, and high-ROI moves.'
---

# Obvious

Find every distinct practical move whose current value materially exceeds its total adoption cost.
A move may be obvious or non-obvious; evidence-backed leverage matters more than novelty.

This skill is read-only.
It proposes moves but never implements or mutates state.

## Internal Review

Before discovery, explicitly read:

- `skill://skill-xray`
- `skill://skill-expert`
- `skill://skill-brutal`

Use each skill only as an internal review lens:

- `skill-xray` generates broadly, attacks assumptions, and exposes blindspots.
- `skill-expert` finds expert techniques and verifies current applicability.
- `skill-brutal` rejects generic, inflated, obvious-by-renaming, or fake-leverage candidates.

This skill owns the final user-visible classification, evidence gates, ranking, and output format when primary.
`skill-xray`, `skill-expert`, and `skill-brutal` are internal review lenses only.
Their analysis, tone, headings, and output formats MUST NOT appear in the final response.
Higher-priority routing remains authoritative.

## Scope and Closure

Resolve scope in this order: explicit focus, current conversation, current project.
Use sufficient conversation context without inspecting unrelated project state.
Otherwise inspect the relevant contracts, manifests, configuration, implementation, dependencies, and workflows.
Inspect relevant Git history when it can reveal rejected choices, failed approaches, hidden assets, or repeated work.
Treat a previous removal as evidence, not an automatic ban; require new evidence before recommending reversal.
Infer obtainable context instead of asking the user.

Before discovery, bound the applicable surfaces:

- project and product areas
- user, operator, maintainer, and developer workflows
- tools, dependencies, services, plugins, and extensions
- current capabilities, defaults, constraints, limits, and hidden state
- repeated decisions, steps, retries, translations, lookups, and manual work
- available sources, datasets, interfaces, and underused assets

Consider each applicable surface and discovery family.
Close an avenue only after it produces a verified survivor or an evidence-backed rejection.
Valid rejection reasons are no contextual leverage, no supported capability, or already correct use.
They also include duplication and failure of a survivor gate.
Stop when every material avenue is closed.
Do not output the closure record.

## Discovery Funnel

Search every applicable family:

- visibly available but overlooked obvious wins with exceptional contextual ROI
- overlooked tools, libraries, services, plugins, and extensions
- hidden features, flags, modes, APIs, configuration options, and built-in capabilities
- expert, power-user, maintainer, hacker, and operator workflows
- shortcuts, automation paths, workflow joins, and sequencing changes
- defaults, constraints, limits, hidden state, and underused assets
- legitimate loopholes, bypass paths, and unconventional combinations
- better sources, datasets, search methods, and information asymmetries
- installed dependency capabilities that remain underused
- recurring work that can disappear entirely
- techniques hidden by muscle memory, tutorial-driven learning, or good-enough habits

Skip inapplicable families.
Generate broadly, then discriminate aggressively.
Do not optimize for obscurity: obscure but weak advice is worse than an obvious exceptional move.

## Evidence Gate

Every survivor requires both forms of evidence:

- Context Evidence proves a current pain, repeated cost, constraint, missed opportunity, or underused asset.
- Move Evidence proves that the proposed capability exists and addresses that exact context.

A real capability without current leverage is trivia, not a finding.

Verify evidence at its owner:

- Conversation claims require a precise stated goal, constraint, repeated pain, or available asset.
- Project claims require the exact path, symbol, setting, command, observable behavior, or relevant commit.
- External or version-sensitive claims require an authoritative primary source URL.
- Tool, feature, flag, API, library, and service claims require proof of the exact supported capability.
- Unverified applicability, capability, leverage, or evidence disqualifies the candidate.

## Survivor Funnel

Keep a candidate only when all conditions hold:

- It applies to the current goal, constraints, and environment.
- It is concrete and executable now.
- Its value materially exceeds implementation, adoption, risk, and maintenance cost.
- Context Evidence and Move Evidence directly support it.
- It is not already correctly implemented, configured, or used.
- It is not generic advice, motivational framing, novelty theater, or familiar advice with advanced wording.
- It is materially distinct from every other survivor.
- It includes the smallest useful first step.

A familiar or obvious technique survives only when its contextual ROI is exceptional.
A non-obvious technique survives only when its value and applicability are concrete; obscurity alone adds no value.
Classify a survivor as `Obvious` when the move is visible or familiar but its contextual leverage was missed.
Classify a survivor as `Non-obvious` only when a concrete discovery barrier or unusual combination explains the miss.
Do not invent novelty to upgrade an obvious move; classification never changes its rank.
Merge duplicates and cosmetic variants.
Report only the dominant move for one opportunity unless different constraints create different best choices.
State the deciding trade-off when multiple approaches survive.

Completeness rules:

- Report every distinct survivor that passes the gates.
- Do not add findings to fill categories or reach a count.
- Keep strong survivors and omit weak, unsupported, or duplicate candidates.
- Omit empty priority groups.
- Zero findings is valid.

## Prioritization

Rank survivors by evidence-backed leverage asymmetry:

- `Exceptional` means unusually broad or compounding value with low adoption burden.
- `High` means strong repeated value with bounded cost and risk.
- `Medium` means strong high-ROI value for a narrower scope or with moderate adoption burden.

`Medium` never means merely useful, interesting, obscure, or convenient.
Do not use pseudo-precise numeric scores.
Order each group from strongest to weakest.

## Output Contract

Be terse and report findings only.
Omit introductions, methodology narration, coverage ledgers, clean inventories, fixed-count claims, and summaries.
- Render the final response as normal Markdown, never as one enclosing code block.
- Preserve code-like tokens in their original language and wrap inline tokens in backticks.
- Internal fenced blocks remain allowed only when the command-specific schema requires them.

- Apart from required command metadata, be terse and report findings only.
- Never list clean files, directories, commands, or per-file no-issue entries.
- Use nested sub-bullets instead of plain continuation lines for long fields.
- Target 8-18 words per sub-bullet and allow at most 22 words for code-heavy lines.
- Keep lines within 100 characters except for indivisible paths, URLs, symbols, and code-like tokens.

- Finding headings MUST use `## <PREFIX><n> — [Title]` with a command-declared prefix.
- Numeric IDs MUST start at 1 and advance globally across all prefixes and severity or priority groups.
- Finding IDs MUST NOT restart, repeat, combine, or gain suffixes within one response.


Use localized equivalents of `# EXCEPTIONAL PROPOSALS`, `# HIGH-PRIORITY PROPOSALS`, and `# MEDIUM-PRIORITY PROPOSALS`, in that order.
Omit empty groups and use finding prefix `M`.
Each title MUST name only the concrete move.
Titles MUST NOT repeat classification, type, proposal status, or judgment.
The priority heading owns the proposal status for every finding in its section.
Use one type from `Tool`, `Feature`, `Workflow`, `Shortcut`, `Automation`, `Source`, or `Default`.
Also permit `Combination` and `Loophole` when those types fit.

Use localized equivalents of these fields as bold labels.
Use a separate bullet for every field.
Use nested sub-bullets for multi-part `Evidence` and `Risk` details.

```text
# EXCEPTIONAL PROPOSALS

## M1 — [Concrete move]

- **Classification:** [Obvious or Non-obvious] · [Type]
- **Judgment:** [concrete judgment]
- **Leverage:** [specific value]
- **First step:** [smallest action]
- **Evidence:**
    - [conversation fact, path, symbol, command, commit, or primary source]
    - [additional supporting evidence]
- **Why missed:** [required for Non-obvious]
- **Risk:** [only for a material downside]
```

Require `Why missed` for a non-obvious move and omit it for an obvious move.
Omit `Risk` when no material downside exists.
Keep every field to one sentence.
The first finding is the strongest recommendation; do not repeat it in a summary.

If no candidate survives, output only the localized equivalent of `No strong high-ROI moves found.`

## Scope Boundaries

Use `/tips` for a broad uncategorized tip inventory when obvious/non-obvious classification does not matter.
Use `skill-expert` for expert-practice or code/config review rather than broad practical-move discovery.
Use `skill-xray` for adversarial critique, blindspots, and improvement analysis rather than a move inventory.
Use `/insider` when every finding must be genuinely obscure and supported by Novelty Evidence.
Use competitive-advantage skills for market position, defensibility, copyability, and competitive edge.
## Language

- Thinking and reasoning MUST be in English.
- Answer in the language the user writes in.
- Canonical English field names define semantic identity and order, not the rendered language.
- Localize human-facing headings, labels, categories, values, and examples into that language.
- Keep a human-facing token exact only when the skill marks it as literal or machine-readable.
- Preserve the canonical contract's structure, order, meaning, modality, and completeness.
- Keep machine formats and code-like tokens exact.
- Never emit parallel schemas in two languages.
- Retain English technical terms when the answer language is less precise or natural.

General code review belongs to the reviewer agent.
