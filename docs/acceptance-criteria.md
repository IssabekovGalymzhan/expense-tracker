# Acceptance Criteria

1. A valid positive expense can be added to an in-memory list.
2. Empty categories, invalid amounts, zero amounts and negative amounts are rejected.
3. The total expense amount is calculated using exact two-decimal money values.
4. Totals can be calculated for a selected category.
5. Valid expenses can be saved to JSON and loaded back without data loss.
6. Malformed or structurally invalid JSON is rejected with a clear `ValueError`.
7. The complete automated test suite passes with one command.
