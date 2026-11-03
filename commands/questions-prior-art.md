---
description: Generates context-specific prior-art questions that find existing solutions, standards, and tools before building custom work.
disable-model-invocation: true
---

# Prior-Art Questions

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


Generate context-specific prior-art questions that find existing solutions to reuse instead of building.

- Use any topical focus in the user instruction; otherwise use the current code, product, plan, or topic.
- Identify the general problem class behind the concrete task, not only its local wording.
- Probe existing libraries, standards, protocols, platform features, tools, services, and established patterns.
- Probe solutions already present in the codebase, its dependencies, or the user's other projects.
- Probe build, buy, and adapt trade-offs, including maintenance, lock-in, licensing, and fit.
- Probe why existing solutions supposedly do not fit and whether that reason survives scrutiny.
- Probe known failures and lessons that prior solutions already learned.
- Make every question name a concrete problem and a concrete prior-art candidate or category.
- Name a specific candidate only when confident it exists; otherwise ask about its category.
- Never claim a candidate's capabilities, maintenance status, or fit without support from the context.
- Exclude generic "do not reinvent the wheel" advice and questions that cannot change the work.

THINK HARD and THINK HARDER and ULTRATHINK.

Use the local `B` prefix.

## Language

- Thinking and reasoning MUST be in English.
- Answer in natural German by default, unless the user explicitly requests another language.
- Canonical English field names define semantic identity and order, not the rendered language.
- Localize human-facing headings, labels, categories, values, and examples into that language.
- Keep a human-facing token exact only when the command marks it as literal or machine-readable.
- Preserve the canonical contract's structure, order, meaning, modality, and completeness.
- Keep machine formats and code-like tokens exact.
- Never emit parallel schemas in two languages.
- Retain English technical terms when the answer language is less precise or natural.
