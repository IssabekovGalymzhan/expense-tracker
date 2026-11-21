# Release Decision

## Decision: CONDITIONAL

The reviewed version passes six automated tests, including money arithmetic, input
validation, JSON round-trip and malformed JSON handling. The two selected confirmed
risks have mitigations and residual risks documented.

Release is conditional because no linter, type checker, CI workflow or full end-to-end
CLI test is configured. The project is suitable for the assignment demonstration, but
additional verification is required before treating it as production software.
