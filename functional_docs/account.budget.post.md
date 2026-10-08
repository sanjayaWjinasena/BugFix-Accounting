# BugFix-Accounting — `account.budget.post`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.budget.post` — Budgetary Position

*Extends a model created by `account_budget`.*

Other repos that use this model: `sale.order.x_studio_many2one_field_KjdJ3` (BugFix-Sales)

**Summary:**

<!-- SUMMARY:model:account.budget.post -->
This repo adds no fields or logic to budgetary positions. It only ships the standard multi-company record rule that limits access to the user's companies.
<!-- /SUMMARY -->

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Budget post multi-company | `rule_330_budget_post_multi_company` | For everyone (global rule): read/write/create/delete on Budgetary Position only where `[('company_id', 'in', company_ids)]`. | `account.budget.post.company_id` (account_budget)<br>`model account.budget.post` (account_budget) |  |
