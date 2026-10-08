# BugFix-Accounting — `account.payment.method.line`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.payment.method.line` — Payment Methods

*Extends a model created by `account`.*

Other repos that use this model: `sale.order._seed_advance_payment_method_lines()` (Fix-repair)<br>`window action BugFix-Studio-Misc.act_window_2741_account_payment_method_line_d7` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:account.payment.method.line -->
This repo adds no fields or logic to payment methods. It only adds one window action that opens payment methods (list and form).
<!-- /SUMMARY -->

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| account.payment.method.line | `act_window_2741_account_payment_method_line` | Opens **Payment Methods** records (tree,form). | `model account.payment.method.line` (account) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_account_payment_method_line` (BugFix-Studio-Misc) |
