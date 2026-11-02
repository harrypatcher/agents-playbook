## Q1–Q5 Contract

- Every conversational response, including skill and slash-command output, MUST end with exactly one Q1–Q5 block.
- Exact-output contracts are the only exception and MUST NOT receive the Q1–Q5 block.
- This exception includes JSON-only, code-only, protocol output, and user-specified literal formats.
- Output of `/questions-*` commands is such an exact-output contract.
- These outputs MUST remain exact.
- The block is a non-blocking inspiration accelerator, not an `ask` interaction.
- It is not a clarification request or approval gate.
- Questions MUST offer distinct, thought-provoking directions.
- They MUST NOT delay, reopen, or imply incomplete work.
- The block MUST be final, preceded by exactly one blank line, followed by nothing, and match this format exactly:

```
● **Q1** — [question]
● **Q2** — [question]
● **Q3** — [question]
● **Q4** — [question]
● **Q5** — [question]
```

- Q1–Q5 MUST be consecutive, with no blank lines between question lines.
- A Q selection applies only to the immediately preceding block.
- It MUST preserve that block's deliverable, target, scope, approval state, and read-only or mutating status.
- Explicit target or scope in the latest user message overrides an assistant-authored Q-block.
- Bare yes/no and single-word replies are actionable only when exactly one preceding question matches.
- Fulfill an unambiguous Q selection without `?` immediately, without restating or confirming it.
- A Q selection with `?` requests evaluation, not execution.
- Work-offering Q questions MUST distinguish returning a proposal or artifact from applying it to a target.
- Proposing a Q MUST NOT authorize implementation.
- Selecting a Q that offers to apply a named change authorizes exactly that change, target, and scope.
- Put any material target or scope conflict before the block.
- Ask only for the unresolved choice.
- Follow-up questions SHOULD deepen the current topic.
- The question-length pyramid SHOULD target approximately 7, 9, 11, 13, and 14 words for Q1–Q5.
- Count question words after the `—` marker; Markdown labels, punctuation, and the `Qn` marker do not count.
- Each question MUST NOT exceed 14 words.
