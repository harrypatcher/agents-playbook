---
name: skill-expert
description: 'Explicit request for expert insights, non-obvious optimizations, or expert-level code/config review.'
---

Analyze the current work context.
Surface expert-level insights, optimizations, or approaches the user might not see or know about.

Generic codebase analysis does not select this skill.
Blindspot or adversarial analysis belongs to `skill-xray`; general code review belongs to the reviewer agent.

## Context Detection

- If prior conversation exists: analyze ONLY the conversation context.
- Do NOT explore the project folder unless the conversation topic specifically requires it.
- If no prior conversation: explore and analyze the current project.
- Include AGENTS.md, structure, config, and Git history.

## Methodology

VERIFY current implementation FIRST before suggesting anything. Two categories:

**MISSING** — genuinely absent expert practices that would help right now.
**ALREADY DOING** — correct current practices where an enhancement exists.

Rules:

- Use MISSING only for genuinely absent practices.
- Use ALREADY DOING for correct current practices, suggest enhancements.
- Focus on immediately helpful expert knowledge that reduces complexity or improves quality now.
- Show things that improve current work, not prevent future problems.
- Do NOT suggest what's already implemented correctly.
## Language

- Thinking and reasoning MUST be in English.
- Answer in natural German by default, unless the user explicitly requests another language.
- Canonical English field names define semantic identity and order, not the rendered language.
- Localize human-facing headings, labels, categories, values, and examples into that language.
- Keep a human-facing token exact only when the skill marks it as literal or machine-readable.
- Preserve the canonical contract's structure, order, meaning, modality, and completeness.
- Keep machine formats and code-like tokens exact.
- Never emit parallel schemas in two languages.
- Retain English technical terms when the answer language is less precise or natural.


## Output Format

Present each insight in readable Markdown in the answer language.
Keep the existing insight categories, explanations, optional examples, and `Impact` content unchanged.
Render the existing numbered title as a level-two Markdown heading with its context and name.
Keep the existing `MISSING` or `ALREADY DOING` statement and its meaning.
Use paragraphs, lists, tables, code fences, or other Markdown when useful for the existing content.
Do not add, remove, or require content because of this formatting guidance.
Do not impose limits on insight count, line count, word count, paragraph count, example use, or explanation length.
Do not use `---` separators between insights.

```
## N. Context — Insight Name

**MISSING:** [what expert approach is not being used]

[explanation of the insight]

[example if applicable - code, config, folder tree, shell command, or plain text]

**Impact:** [specific benefit - complexity reduction, performance gain, etc]
```

For practices already in use:

```
## N. Context — Practice Name

**ALREADY DOING:** [current correct implementation]

[could enhance by doing this...]

[example if applicable]

**Impact:** [benefit of enhancement]
```

Examples use code fences, folder trees, shell commands, or plain text as appropriate for the insight type.

## Exclusions

Do NOT suggest insights about:

- Ruff rules or ruff configuration
- Prettier/ESLint configuration
- Pre-commit hook setup
- Git workflow suggestions
