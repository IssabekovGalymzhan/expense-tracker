# Mitigation Records

## M1 - Reject non-finite amounts

- Related risk: R3.
- Change: `Expense` now rejects `NaN`, positive infinity and negative infinity with a
  clear `ValueError`.
- Verification: `test_add_expense_rejects_non_finite_values` passes.
- Residual risk: locale-specific number formats are not supported.

## M2 - Persist CLI records

- Related risk: R4.
- Change: `main.py` loads existing records from `expenses.json` and saves each valid new
  expense through `storage.py`.
- Verification: `test_main_saves_expenses_to_storage` passes.
- Residual risk: concurrent multi-user writes are not supported; this remains
  plausible/unverified for the single-user assignment scope.
