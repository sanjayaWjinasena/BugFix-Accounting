# BugFix-Accounting — `account.reconcile.model`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.reconcile.model` — Preset to create journal entries during a invoices and payments matching

*Extends a model created by `account`.*

**Summary:**

<!-- SUMMARY:model:account.reconcile.model -->
This repo adds no fields or logic to reconciliation models. It only ships the standard multi-company record rule.
<!-- /SUMMARY -->

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Account reconcile model template company rule | `rule_89_account_reconcile_model_template_company_rule` | For everyone (global rule): read/write/create/delete on Preset to create journal entries during a invoices and payments matching only where `[('company_id', 'parent_of', company_ids)]`. | `account.reconcile.model.company_id` (account)<br>`model account.reconcile.model` (account) |  |
