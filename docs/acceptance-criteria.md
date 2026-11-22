# Acceptance Criteria

1. A valid positive expense can be added to an in-memory list.
2. Empty categories, invalid amounts, zero amounts and negative amounts are rejected.
3. Non-finite amounts such as `NaN` and infinity are rejected with a clear `ValueError`.
4. The total expense amount is calculated using exact two-decimal money values.
5. Totals can be calculated for a selected category.
6. Valid expenses can be saved to JSON and loaded back without data loss.
7. The CLI loads existing records and saves each valid new record to `expenses.json`.
8. Malformed or structurally invalid JSON is rejected with a clear `ValueError`.
9. The complete automated test suite passes with one command.
