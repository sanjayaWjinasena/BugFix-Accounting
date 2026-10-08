# BugFix-Accounting — `account.tax`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.tax` — Tax

*Extends a model created by `account`.*

Other repos that use this model: `window action BugFix-Studio-Misc.act_window_2758_taxes_d7` (BugFix-Studio-Misc)<br>`x_po_line_non_inventor.x_studio_taxes` (BugFix-Purchase)

**Summary:**

<!-- SUMMARY:model:account.tax -->
This repo adds no fields to taxes. It extends the Taxes list with Tax Type, Tax Scope, Company, Active, Created By and Amount Type columns. It also adds a 'Taxes' window action used by the Accounting/Taxes menu and the standard multi-company record rule.
<!-- /SUMMARY -->

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Taxes | `action_2758_taxes` | Opens **Tax** records (kanban,tree,form). | `model account.tax` (account) | `menu BugFix-Accounting.menu_1340_taxes`<br>`menu BugFix-Studio-Misc.menu_f6_taxes` (BugFix-Studio-Misc) |

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: account.invoice.line.tax.search customization | `ported_view_5957_customization_account_tax_tree` | tree | after `//field[@name='display_name']`: add field type_tax_use, field tax_scope; after `//field[@name='description']`: add field company_id, field active, field create_uid, field amount_type | Taxes list: adds Tax Type (sales/purchase use) and Tax Scope after the name, and Company, an Active toggle, Created By and Tax Computation after the description. | `account.tax.active` (account)<br>`account.tax.amount_type` (account)<br>`account.tax.company_id` (account)<br>`account.tax.tax_scope` (account)<br>`account.tax.type_tax_use` (account)<details><summary>+1 more</summary>`view account.account_tax_view_tree` (account)</details> |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Tax multi-company | `rule_84_tax_multi_company` | For everyone (global rule): read/write/create/delete on Tax only where `[('company_id', 'parent_of', company_ids)]`. | `account.tax.company_id` (account)<br>`model account.tax` (account) |  |
