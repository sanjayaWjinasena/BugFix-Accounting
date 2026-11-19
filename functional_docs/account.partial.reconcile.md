# BugFix-Accounting — `account.partial.reconcile`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.partial.reconcile` — Partial Reconcile

*Extends a model created by `account`.*

**Summary:**

<!-- SUMMARY:model:account.partial.reconcile -->
This repo adds no fields or logic to partial reconciliations. It only grants read access to the 'Jin - Sales - POS Users' group (from BugFix-Approvals).
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| account.partial.reconcile | `access_6866_account_partial_reconcile` | Gives **Sales / Jin - Sales - POS Users** read access to Partial Reconcile records. | `group BugFix-Approvals.group_132_jin_sales_pos_users` (BugFix-Approvals)<br>`model account.partial.reconcile` (account) |  |
