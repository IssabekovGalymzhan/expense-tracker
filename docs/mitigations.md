# Mitigation Records

## M1 - Exact money and input validation

- Related risks: R1 and R2.
- Change: replaced baseline `float` amounts with quantized `Decimal` values; blank,
  non-numeric, zero and negative amounts are rejected.
- Verification: `test_total_expenses_uses_decimal_money` and
  `test_add_expense_rejects_invalid_values` pass.
- Residual risk: the project does not implement currency conversion or locale-specific
  number parsing.

## M2 - Validated JSON loading

- Related risk: R3.
- Change: `storage.py` catches file/JSON errors, requires a list, validates each record
  and reports the record index in a `ValueError`.
- Verification: `test_load_rejects_malformed_json` and the round-trip test pass.
- Residual risk: filesystem permissions and disk-full failures still depend on the host.
