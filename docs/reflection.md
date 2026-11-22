# AI Reflection

I used ChatGPT/Codex and Claude on November 22, 2026 while reviewing a small Python
Expense Tracker for Assignment 05. I gave the assistants the assignment requirements,
the repository structure and the outputs of commands that I ran locally. I asked for
read-only risk suggestions before accepting any code changes.

The most useful findings were that the command-line entry point did not call
`storage.py`, and that the value `NaN` caused an unhandled `decimal.InvalidOperation`.
I personally reproduced both findings in PowerShell. I then checked the changed source
and ran the full test suite again. The final suite passed nine tests, including a test
that proves CLI persistence and a test that rejects NaN and infinity.

Claude also helped clarify that a blank `Select-String` result means the command
completed without matches, not that the terminal froze. I recorded that advice as a
useful process suggestion and checked it against the visible PowerShell prompt.

One unsupported AI candidate was SQL injection: the project has no SQL, database or
query interface. One plausible but unverified candidate was data loss from concurrent
writers; I did not claim it was confirmed because I ran only single-user tests.

The repository instructions improved the process by defining safe commands, forbidden
operations and review gates. The final decision remains CONDITIONAL because static
analysis, CI and concurrent multi-user storage are outside the verified scope. Before a
production release, I would add a linter, type checker, CI workflow and a locking or
database-based storage design.
