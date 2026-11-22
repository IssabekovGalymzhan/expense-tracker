# Repository Map

| Component | Purpose | Verification |
|---|---|---|
| `main.py` | Command-line entry point, load/save orchestration and input loop | `python main.py` |
| `expenses.py` | Expense model, validation and totals | `python -m unittest discover -s tests -v` |
| `storage.py` | JSON serialization and validation | `python -m unittest discover -s tests -v` |
| `tests/test_expenses.py` | Nine unit tests for core behavior, persistence and CLI validation | `python -m unittest discover -s tests -v` |
| `README.md` | Setup, run and test instructions | Manual review |
| `AGENTS.md` | Agent boundaries and verification gates | Manual review |

The project has no external runtime dependencies. Python 3.13.1 was used for verification.
