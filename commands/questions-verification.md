---
description: Generates context-specific verification questions focused on decisive, falsifiable evidence.
---

# Verification Questions

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


Generate context-specific verification questions that test what evidence establishes and what remains uncertain.

- Use any topical focus in the user instruction; otherwise use the current topic.
- Consider decisive evidence, falsifiers, baselines, observability, confounders, measurement quality, and unresolved uncertainty.
- Require each question to name a concrete observation, test, metric, or evidence source and the result that would change a decision.
- Distinguish what is observed from what is inferred.
- Never invent evidence, measurements, access, or certainty not present in the context.
- Select only relevant angles.
- Exclude generic QA checklists, “test more,” non-falsifiable prompts, vanity metrics, and implementation advice.
- Exclude experiments incapable of changing a decision.

THINK HARD and THINK HARDER and ULTRATHINK.

Use the local `V` prefix.

## Language

- Think and reason in English.
- Answer in the language of the conversation.
- Localize human-facing headings, labels, and values, but keep code-like tokens exact.
