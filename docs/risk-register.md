# Risk Register

Score = likelihood x impact. Allowed categories are correctness, maintainability,
security, dependency and agent operations.

| ID | Category | Classification | Cause -> event -> consequence | Evidence | L | I | Score | Mitigation / status |
|---|---|---|---|---|---:|---:|---:|---|
| R1 | Correctness | Confirmed | Float money values -> rounding error -> incorrect total | Baseline `expenses.py` in commit `d0adfc8` stored `float` | 2 | 3 | 6 | Replaced with `Decimal`; verified by exact-total test |
| R2 | Correctness | Confirmed | Empty category -> unusable record -> unreliable report | Baseline code accepted blank category | 2 | 2 | 4 | Reject and trim blank categories; verified by test |
| R3 | Correctness | Confirmed | `NaN` or infinity -> invalid comparison -> uncaught `InvalidOperation` | Local command reproduced `decimal.InvalidOperation` | 2 | 3 | 6 | Reject non-finite values as `ValueError`; verified by test |
| R4 | Correctness | Confirmed | CLI never called storage -> records lost after exit | `Select-String` returned no match in `main.py`; code inspection confirmed no save call | 2 | 3 | 6 | Load at startup and save after each valid expense; verified by test |
| R5 | Correctness | Confirmed | Malformed JSON -> load exception -> application failure | Baseline `storage.py` used raw JSON loading | 2 | 3 | 6 | Validate JSON and report `ValueError`; verified by test |
| R6 | Maintainability | Confirmed | CLI input and orchestration remain in one entry point -> future UI changes touch `main.py` | Code inspection; no justified pattern was found | 2 | 2 | 4 | Keep domain and storage modules separate; defer larger UI split |
| R7 | Agent operations | Confirmed | Missing instructions at baseline -> unsafe agent workflow -> unreviewed changes | `AGENTS.md` was absent in baseline commit | 2 | 3 | 6 | Added safe commands, prohibitions and review gates |
| R8 | Agent operations | Confirmed | No lint/type-check/CI configuration -> defects may escape tests | Repository inspection found no static checks | 2 | 2 | 4 | Record as readiness gap; run compile check |
| R9 | Security | Plausible/unverified | Concurrent writers -> last write wins -> one record could be lost | No concurrency test was run; single-user CLI is the current scope | 1 | 2 | 2 | Add file-locking or database storage if multi-user use is required |
| R10 | Security | Unsupported | SQL injection -> database compromise | No SQL, database or query interface exists in this repository | 1 | 3 | 3 | Do not treat as a confirmed risk |

Top two corrective risks were R3 and R4. Both are now mitigated and verified. R9 remains
plausible/unverified and R10 is explicitly unsupported.
