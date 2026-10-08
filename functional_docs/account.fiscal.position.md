# BugFix-Accounting — `account.fiscal.position`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.fiscal.position` — Fiscal Position

*Extends a model created by `account`.*

**Summary:**

<!-- SUMMARY:model:account.fiscal.position -->
This repo adds no fields or logic to fiscal positions. It only ships the standard multi-company record rule.
<!-- /SUMMARY -->

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Account fiscal Mapping company rule | `rule_86_account_fiscal_mapping_company_rule` | For everyone (global rule): read/write/create/delete on Fiscal Position only where `[('company_id', 'parent_of', company_ids)]`. | `account.fiscal.position.company_id` (account)<br>`model account.fiscal.position` (account) |  |
