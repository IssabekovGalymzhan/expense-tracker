# AI Reflection

I used ChatGPT/Codex on November 21, 2026 to help structure this software-engineering
audit. The assistant received the assignment requirements, the repository structure,
the source files and the actual output of commands run in the repository. I asked for a
read-only risk review before accepting changes, because the assignment required human
verification of AI findings.

The most useful suggestion was to treat money as a correctness risk and to use decimal
values instead of binary floating-point values. This led to a focused improvement in
the domain model and a test that verifies exact two-decimal totals. A second useful
finding was that raw JSON loading could fail with an unclear exception when the file was
malformed. I added input validation and a test for malformed JSON.

One weak suggestion was to rely on pytest immediately. The environment did not allow
the package installation, so I did not claim that pytest had run. I changed the tests to
Python's standard unittest module and recorded the limitation in the AI-use record.

I personally inspected the baseline code, checked the diff, ran the baseline five-test
suite and the final six-test suite, and reviewed the acceptance criteria after the
changes. The test results changed the release decision to CONDITIONAL rather than GO:
the core behavior is verified, but linting, type checking, CI and full CLI testing remain
unimplemented. The `AGENTS.md` file improved the process by making safe commands,
forbidden actions and review gates explicit. The next improvement would be a small CI
workflow with static checks and an end-to-end command-line test.
