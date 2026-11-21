# Hypothetical Background-Agent Task

## Scope

Work only in an isolated branch or worktree named `agent/expense-validation`.

## Allowed files

`expenses.py`, `storage.py`, `tests/`, `README.md` and `AGENTS.md`.

## Allowed commands

`python -m unittest discover -s tests -v`, `python -m compileall ...`, `git diff` and
read-only file inspection.

## Limits and prohibitions

Time limit: 20 minutes. Do not access secrets, install unreviewed dependencies, deploy,
push to a remote, delete files recursively or merge automatically.

## Required artifacts

The agent must return a change summary, diff, test log, compile result and risk notes.
Human review and approval are required before merge. If checks fail, discard the branch
or revert the reviewed commit and keep the baseline intact.
