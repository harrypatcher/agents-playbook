---
description: Generates context-specific inspiration questions that open distinct, thought-provoking directions like the Q1–Q5 block.
disable-model-invocation: true
---

# Inspiration Questions

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


Generate context-specific inspiration questions that work like an extended Q1–Q5 block.

- Use any topical focus from the user instruction.
  Without one, use the current conversation and work state.
- Treat the questions as a non-blocking inspiration accelerator, not as clarification requests or approval gates.
- Offer distinct, thought-provoking directions that deepen the current topic.
- Mix evaluations, deeper explorations, and concrete offers to act.
- Make every offer to act distinguish returning a proposal or artifact from applying a change to a target.
- Order the questions from short and immediate to longer and more far-reaching.
- Ground every question in the context and never invent files, tools, or requirements.
- Exclude questions that delay, reopen, or imply incomplete work.
- Propose only and never implement, execute, or modify files in this response.
- A later selection of an `I` question follows the same rules as a Q selection.

THINK HARD and THINK HARDER and ULTRATHINK.

Use the local `I` prefix.

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
