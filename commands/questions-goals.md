---
description: Generates context-specific, thought-provoking questions focused on the user's goals and whether the current work serves them.
disable-model-invocation: true
---

# Goal Questions

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


Generate context-specific goal questions that work like an extended Q1–Q5 block focused on the user's goals.

- Use any topical focus from the user instruction.
  Without one, use the current conversation, work state, and the goals it states or implies.
- Treat the questions as a non-blocking inspiration accelerator, not as clarification requests or approval gates.
- Offer distinct, thought-provoking directions that sharpen, test, or advance the user's goals.
- Probe the goal behind the goal, its success criterion, and the signal that shows progress soon.
- Probe work that does not advance the goal, conflicting goals, and which goal wins when they collide.
- Probe proxy metrics that replaced the goal, goals made stale by changed conditions, and short-term wins that block long-term goals.
- Probe explicit non-goals, inherited goals the user never chose, and a more or less ambitious version of the goal.
- Mix evaluations, deeper explorations, and concrete offers to act.
- Make every offer to act distinguish returning a proposal or artifact from applying a change to a target.
- Make every question name a concrete goal and connect it to concrete current work.
- Never invent goals, metrics, or deadlines the context does not support.
- Exclude generic goal-setting frameworks and questions that delay, reopen, or imply incomplete work.
- Propose only and never implement, execute, or modify files in this response.

THINK HARD and THINK HARDER and ULTRATHINK.

Use the local `G` prefix.

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
