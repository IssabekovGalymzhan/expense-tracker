# Focused Pattern Decision

The repository was evaluated for Strategy and Adapter.

No design pattern was implemented. The baseline contained one small category filter
and no family of interchangeable algorithms or external interfaces that would justify
additional abstraction. Adding Strategy would make this six-file educational project
harder to read without solving a demonstrated problem.

The focused structural improvement was domain validation:

- Before: `Expense.amount` was stored as `float`; blank categories were accepted;
  storage trusted JSON shape.
- After: `Expense` normalizes money with `Decimal`, rejects invalid categories and
  amounts, and `storage.py` validates JSON before constructing domain objects.

The acceptance criteria remain true and are checked by six passing unit tests.
