# Risk Register

Score = likelihood × impact. Scores are from 1 to 9.

| ID | Category | Cause -> event -> consequence | Component | Classification and evidence | L | I | Score | Mitigation | Owner | Verification | Residual risk |
|---|---|---|---|---|---:|---:|---:|---|---|---|---|
| R1 | Correctness | Binary floating point -> rounding error -> incorrect money total | `expenses.py` | Confirmed in baseline: amount was stored as `float`; inspected in baseline commit `d0adfc8` | 2 | 3 | 6 | Use `Decimal` quantized to cents | Student | Decimal total test | External currency conversion is out of scope |
| R2 | Correctness | Empty category accepted -> unusable record -> unreliable category reports | `expenses.py` | Confirmed in baseline: no category validation; baseline code inspection | 2 | 2 | 4 | Reject blank categories and trim whitespace | Student | Invalid-input test | Category naming rules remain simple |
| R3 | Reliability | Untrusted JSON shape or syntax -> load exception -> application failure | `storage.py` | Confirmed in baseline: raw `json.loads` and dataclass construction had no friendly validation | 2 | 3 | 6 | Validate JSON type, records and errors | Student | Malformed JSON test | File permissions and disk failures remain possible |
| R4 | Agent operations | No repository instruction file -> agent may use unsafe workflow -> unreviewed changes | Repository root | Confirmed: `AGENTS.md` did not exist at baseline | 2 | 3 | 6 | Add `AGENTS.md` with forbidden actions and review gates | Student | Manual file review | Agents may still ignore instructions |
| R5 | Maintainability | Input loop and presentation remain in one entry point -> future UI changes touch CLI code | `main.py` | Confirmed by code inspection; no duplicated conditional logic requiring a pattern was found | 2 | 2 | 4 | Keep domain logic outside `main.py`; defer larger UI split | Student | Repository map review | CLI remains intentionally small |
| R6 | Verification | No lint/type-check configuration -> defects may escape unit tests | Repository | Confirmed: no linter or type-check command is configured | 2 | 2 | 4 | Record as a readiness gap and run compile check | Student | `compileall` command | Static analysis is still absent |

Top two corrective risks: R1 and R3. R2 is also addressed by the same domain validation change.
