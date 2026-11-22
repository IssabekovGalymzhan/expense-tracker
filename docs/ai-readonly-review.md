# Read-Only AI Risk Review

## Prompt used

```text
Review this repository in read-only mode. Do not modify files. Find at least five
candidate risks across correctness, maintainability, security, dependency and agent
operations. For each finding, provide the affected file and a verification method.
Separate confirmed, plausible/unverified and unsupported claims.
```

## AI response and human verification

| Candidate | AI suggestion | Human verification | Classification |
|---|---|---|---|
| C1 | Money stored as floating point may round incorrectly | Baseline code used `float`; final code uses `Decimal` and exact-total test | Confirmed |
| C2 | Blank category may create unreliable reports | Baseline accepted blank category; final invalid-input test covers it | Confirmed |
| C3 | Non-finite input such as `NaN` may break comparison | Local command reproduced `decimal.InvalidOperation`; final test covers NaN and infinity | Confirmed |
| C4 | CLI may not persist records | `main.py` had no storage import or call; final persistence test passes | Confirmed |
| C5 | Malformed JSON may crash loading | Baseline used raw JSON loading; malformed-JSON test and validation now pass | Confirmed |
| C6 | Concurrent writers may overwrite each other | No concurrency test or multi-user deployment exists; not verified | Plausible/unverified |
| C7 | SQL injection may be possible | No SQL, database or query interface exists | Unsupported |

The AI did not modify files during this review. Code changes were made only after the
candidate findings were checked against source code and executable commands.
