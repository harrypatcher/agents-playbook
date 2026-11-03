---
description: Generates context-specific self-check questions the agent should ask itself to test whether it fully understood the request.
disable-model-invocation: true
---

# Agent Understanding Check Questions

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


Generate context-specific questions the agent should ask itself to test whether it fully understood the request.

- Use any topical focus in the user instruction; otherwise use the current request and conversation.
- Phrase each question from the agent's perspective, such as `Have I …?` or `Do I know …?`.
- Probe the goal, the deliverable, the target, the scope, and what counts as done.
- Probe constraints, prior decisions, user preferences, and what the user explicitly ruled out.
- Probe ambiguous terms, unstated assumptions, conflicting instructions, and silently filled gaps.
- Probe whether the request asks for analysis or for changes, and what effects it authorizes.
- Make every question name a concrete element of the current request that could be misunderstood.
- Prefer questions whose wrong answer would send the work in a materially different direction.
- Exclude generic comprehension checklists and questions the conversation already answers unambiguously.

THINK HARD and THINK HARDER and ULTRATHINK.

Use the local `A` prefix.

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
