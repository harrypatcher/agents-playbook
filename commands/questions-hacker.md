---
description: Generates context-specific hacker-style questions using unconventional but practical approaches.
---

# Hacker-Style Questions

<user-instruction>
$ARGUMENTS
</user-instruction>

- Generate the number of context-specific questions explicitly requested in the user instruction.
- Without an explicit count, generate ten questions.
- Treat a standalone positive integer as the question count; otherwise count numbers only when they explicitly request questions.
- Make the questions materially different and individually capable of changing the user's reasoning or action.
- Each question MUST have between 7 and 15 words.
- Count words after the `—` marker only.
- Return only consecutive question lines, without blank lines or surrounding commentary.
- Never append the global Q1–Q5 block after the question lines.
- Format each line as `● **<prefix><number>** — [question]`, using the command's prefix and numbering from 1.


Generate context-specific hacker-style questions.
They expose unconventional but practical approaches.

- Use any topical focus in the user instruction; otherwise use the current topic.
- Push beyond conventional approaches through creative workarounds and rule-bending solutions.
- Consider edge cases, system loopholes, reverse engineering, system deconstruction, and information extraction.
- Consider repurposing existing tools or resources, combining unrelated features, and challenging fundamental assumptions.
- Select only relevant angles and fit them to the user's realistic capabilities.
- Exclude absurd, purely theoretical, blockchain, and cryptocurrency suggestions.

THINK HARD and THINK HARDER and ULTRATHINK.

Use the local `H` prefix.

## Language

- Thinking and reasoning MUST be in English.
- Answer the user in natural German.
- Canonical English field names define semantic identity and order, not the rendered language.
- Localize human-facing headings, labels, categories, values, and examples into idiomatic German.
- Keep a human-facing token exact only when the command marks it as literal or machine-readable.
- Preserve the canonical contract's structure, order, meaning, modality, and completeness.
- Keep machine formats and code-like tokens exact.
- Never emit parallel English and German schemas.
- Retain English technical terms when German is less precise or natural.
