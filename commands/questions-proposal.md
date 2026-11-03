---
description: Generates context-specific proposal questions that offer concrete next actions for selection.
disable-model-invocation: true
---

# Proposal Questions

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


Generate context-specific proposal questions that each offer one concrete action the user can select.

- Use any topical focus from the user instruction.
  Without one, use the current conversation and work state.
- Phrase each question as a direct offer to act, such as `Should I …?`.
- Name the concrete target, change, or deliverable in each question.
- Make clear whether the offer returns a proposal or artifact, or applies a change to a target.
- Prefer unfinished, feasible actions that resolve blockers or create immediate value.
- Order the questions by expected value, strongest first.
- Ground every offer in the context and never invent files, tools, or requirements.
- Exclude rhetorical questions, open-ended inquiries, clarification requests, and offers that repeat completed work.
- Propose only and never implement, execute, or modify files in this response.
- A later selection of a `P` question follows the same rules as a Q selection.

THINK HARD and THINK HARDER and ULTRATHINK.

Use the local `P` prefix.

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
