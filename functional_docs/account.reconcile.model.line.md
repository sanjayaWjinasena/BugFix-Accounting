# BugFix-Accounting — `account.reconcile.model.line`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.reconcile.model.line` — Rules for the reconciliation model

*Extends a model created by `account`.*

**Summary:**

<!-- SUMMARY:model:account.reconcile.model.line -->
This repo adds no fields or logic to reconciliation model lines. It only ships the standard multi-company record rule.
<!-- /SUMMARY -->

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Account reconcile model_line template company rule | `rule_90_account_reconcile_model_line_template_company_rule` | For everyone (global rule): read/write/create/delete on Rules for the reconciliation model only where `[('company_id', 'parent_of', company_ids)]`. | `account.reconcile.model.line.company_id` (account)<br>`model account.reconcile.model.line` (account) |  |
