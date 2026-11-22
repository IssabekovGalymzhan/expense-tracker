# Expense Tracker

A small Python command-line project for recording expenses and calculating totals.

## Setup

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

This project has no external runtime dependencies. Tests use Python's standard `unittest` module.

## Run

```powershell
python main.py
```

The application loads existing records from `expenses.json` and saves each valid new
expense to that file. Runtime data is ignored by Git.

## Test

```powershell
python -m unittest discover -s tests -v
```

## Modules

- `expenses.py` - expense model and calculations.
- `storage.py` - JSON persistence.
- `main.py` - command-line entry point.
- `tests/` - automated tests.
