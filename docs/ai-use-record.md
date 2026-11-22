# AI-Use Record

## ChatGPT / Codex

- Model: GPT-5 / Codex.
- Date: 2026-11-22.
- Context: Assignment 05 requirements, the Expense Tracker repository, local test output
  and manual checks in PowerShell.
- Used for: project structure, read-only risk review, code corrections, tests and report
  structure.
- Useful result: identify missing persistence and non-finite money input as risks.
- Verification: I ran the test suite locally and reproduced the `NaN` exception locally.

## Claude

- Model: Claude Sonnet 5.5, Medium.
- Date: 2026-11-22.
- Context: the assignment plan, test output and the two manual risk checks.
- Used for: checking whether the evidence and AI-use documentation met the assignment.
- Useful result: distinguish a blank `Select-String` result from a hung terminal and
  recommend preserving the command evidence.
- Verification: I ran the commands locally and compared the result with the source code.

Both assistants were treated as sources of suggestions. Findings were not accepted
without a local code or command check.
