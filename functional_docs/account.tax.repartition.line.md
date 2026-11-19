# BugFix-Accounting — `account.tax.repartition.line`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.tax.repartition.line` — Tax Repartition Line

*Extends a model created by `account`.*

Other repos that use this model: `access right BugFix-Studio-Misc.access_g_account_tax_repartition_line_invoice_line_accounting_billing_limited_archived` (BugFix-Studio-Misc)<br>`access right BugFix-Studio-Misc.access_g_account_tax_repartition_line_invoice_line_accounting_billing_limited_cashier` (BugFix-Studio-Misc)<br>`access right BugFix-Studio-Misc.access_g_account_tax_repartition_line_invoice_line_accounting_test_inheritance` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:account.tax.repartition.line -->
This repo adds no fields or logic to tax repartition lines. It ships an editable inline list of distribution lines (percentage, base or tax type, account, tax grids, closing entry flag) and a multi-company record rule.
<!-- /SUMMARY -->

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| account.tax.repartition.line.tree | `ported_tax_repartition_line_tree` | tree | full tree layout with 8 fields | Editable inline list of tax distribution (repartition) lines: sequence handle, percentage, base/tax type, account, tax grid tags and 'Tax Closing Entry' flag; percentage, account and closing flag are hidden on Base lines. | `account.tax.repartition.line.account_id` (account)<br>`account.tax.repartition.line.company_id` (account)<br>`account.tax.repartition.line.factor_percent` (account)<br>`account.tax.repartition.line.repartition_type` (account)<br>`account.tax.repartition.line.sequence` (account)<details><summary>+3 more</summary>`account.tax.repartition.line.tag_ids_domain` (account)<br>`account.tax.repartition.line.tag_ids` (account)<br>`account.tax.repartition.line.use_in_tax_closing` (account)</details> |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Tax Repartition multi-company | `rule_631_tax_repartition_multi_company` | For everyone (global rule): read/write/create/delete on Tax Repartition Line only where `['|',('company_id','=',False), ('company_id', 'parent_of', company_ids)]`. | `account.tax.repartition.line.company_id` (account)<br>`model account.tax.repartition.line` (account) |  |
