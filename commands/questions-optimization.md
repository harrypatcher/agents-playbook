---
description: Generates context-specific optimization questions that find where the current work can become faster, cheaper, or more efficient.
disable-model-invocation: true
---

# Optimization Questions

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


Generate context-specific optimization questions that find how to deliver equal or more value at lower cost.

- Use any topical focus in the user instruction; otherwise use the current code, system, workflow, plan, or topic.
- Identify the optimization target the context supports, such as latency, throughput, cost, tokens, effort, or quality.
- Probe the actual bottleneck, where time or cost is spent, and whether that claim rests on measurement or assumption.
- Probe redundant work, repeated computation, unnecessary round trips, and waiting.
- Probe serialized steps that could run in parallel.
- Probe caching, batching, reuse, better defaults, cheaper alternatives, and automation of recurring manual steps.
- Probe trade-offs against correctness, maintainability, reliability, and readability.
- Probe where further optimization stops paying off.
- Probe the metric that proves an improvement and the baseline it must beat.
- Make every question name a concrete optimization candidate and the cost or resource it would reduce.
- Never invent measurements, bottlenecks, or costs the context does not support.
- Exclude premature micro-optimizations, generic tuning checklists, and gains too small to change the work.

THINK HARD and THINK HARDER and ULTRATHINK.

Use the local `O` prefix.

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
