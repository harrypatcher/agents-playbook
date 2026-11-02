---
description: Generates context-specific proposal questions that offer concrete next actions for selection.
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
- If the user later selects a `P` question, carry out exactly that offer and nothing more.

THINK HARD and THINK HARDER and ULTRATHINK.

Use the local `P` prefix.

## Language

- Think and reason in English.
- Answer in the language of the conversation.
- Localize human-facing headings, labels, and values, but keep code-like tokens exact.
