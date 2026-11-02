---
description: Generates context-specific solution questions that identify plausible implementation failures and root-cause fixes.
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
- Format each line as `<span style="color:<hex>">●</span> **<prefix><number>** — [question]`, using the command's prefix and numbering from 1.
- Color the dots in this order:

  1. `#ff6a6c`
  2. `#fe9032`
  3. `#fbcc02`
  4. `#9fe800`
  5. `#0be274`
  6. `#10d5bf`
  7. `#13d3ef`
  8. `#5ca5fe`
  9. `#a789fe`
  10. `#ec73fe`

- After the tenth color, start again with the first.
  For example, questions 11, 21, and 31 use color 1, and questions 12, 22, and 32 use color 2.
- The colors only help the reader keep track of lines and carry no meaning.


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
- Answer the user in natural German.
- Canonical English field names define semantic identity and order, not the rendered language.
- Localize human-facing headings, labels, categories, values, and examples into idiomatic German.
- Keep a human-facing token exact only when the command marks it as literal or machine-readable.
- Preserve the canonical contract's structure, order, meaning, modality, and completeness.
- Keep machine formats and code-like tokens exact.
- Never emit parallel English and German schemas.
- Retain English technical terms when German is less precise or natural.
