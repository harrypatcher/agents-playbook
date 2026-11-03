---
description: Generates context-specific user questions that expose how the current work affects the people who use it.
disable-model-invocation: true
---

# User Questions

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
- Format each line as `• **<prefix><number>** — [question]`, using the command's prefix and numbering from 1.


Generate context-specific user questions that expose how the current work affects the people who use it.

- Use any topical focus in the user instruction; otherwise use the current code, product, content, or topic.
- Identify the affected user groups from the context, such as new, power, paying, silent, or downstream users.
- Consider user needs, jobs to be done, workflows, friction, expectations, trust, and perceived value.
- Consider breaking changes, migration effort, defaults, discoverability, accessibility, privacy, and support burden.
- Distinguish what users demonstrably do from what the work assumes they do.
- Make every question name a concrete user group and a concrete effect on them.
- Never invent user research, metrics, feedback, or user groups the context does not support.
- Exclude generic UX checklists, persona theater, and questions that cannot change the work.

THINK HARD and THINK HARDER and ULTRATHINK.

Use the local `E` prefix.

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
