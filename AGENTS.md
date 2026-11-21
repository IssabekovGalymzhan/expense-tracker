# Agent Instructions

## Purpose

Expense Tracker is a small Python command-line application for recording expenses,
calculating totals and persisting records as JSON.

## Architecture

- `expenses.py` contains the `Expense` domain model and calculations.
- `storage.py` contains JSON persistence and input validation.
- `main.py` is the command-line entry point.
- `tests/` contains automated tests.

## Setup and safe commands

The project uses only the Python standard library.

```powershell
python -m unittest discover -s tests -v
python -m compileall expenses.py storage.py main.py tests
python main.py
```

## Coding conventions

- Use type annotations for public functions.
- Keep money values as `Decimal` and serialize them as strings.
- Raise clear `ValueError` messages for invalid user or file data.
- Keep user-interface code in `main.py` and domain logic in `expenses.py`.

## Required verification

- Run the full unittest suite after every code change.
- Report the exact command and result.
- Inspect the diff before accepting any generated change.

## Forbidden actions

- Never print, commit or transmit secrets, tokens or personal data.
- Never deploy or connect to production systems.
- Never run destructive commands such as recursive deletion or hard reset.
- Do not change dependencies without human review.
- Do not modify files outside this repository.
