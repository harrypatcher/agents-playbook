---
description: Generates context-specific solution questions that identify plausible implementation failures and root-cause fixes.
disable-model-invocation: true
---

# Solution Questions

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
- Draft more candidates internally than requested and drop near-duplicates.
- Order the questions by expected impact, strongest first, unless the command defines another order.
- A later selection such as `<prefix><number>` follows the Q selection rules and refers to this list.


Generate context-specific solution questions that identify concrete problems and practical root-cause fixes.

- Use any topical focus in the user instruction; otherwise use the current code, implementation, or problem.
- Examine code flow, logic, state transitions, boundary conditions, validation, and error propagation.
- Consider concurrency, timing, resource lifecycle, data integrity, and recovery only when relevant.
- Make each question name a context-grounded failure mechanism and an implementable solution direction.
- Fit the existing architecture, conventions, and caller expectations.
- Exclude invented errors, generic best practices, premature optimization, and speculative redesign.

THINK HARD and THINK HARDER and ULTRATHINK.

Use the local `S` prefix.

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
