# BugFix-Accounting — `account.tax.group`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.tax.group` — Tax Group

*Extends a model created by `account`.* Python: `models/account_tax_group.py`.

Other repos that use this model: `access right BugFix-Studio-Misc.access_g_account_tax_group_group_accounting_billing_limited_archived` (BugFix-Studio-Misc)<br>`access right BugFix-Studio-Misc.access_g_account_tax_group_group_accounting_billing_limited_cashier` (BugFix-Studio-Misc)<br>`access right BugFix-Studio-Misc.access_g_account_tax_group_group_accounting_test_inheritance` (BugFix-Studio-Misc)<br>`access right BugFix-Studio-Misc.access_g_account_tax_group_sale_manager_group_sales_jin_sales_view_only` (BugFix-Studio-Misc)<br>`access right BugFix-Studio-Misc.access_g_account_tax_group_sale_manager_group_sales_user_new` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:account.tax.group -->
This repo adds full form and list views for Tax Groups showing the tax payable, receivable and advance payment accounts. It adds a 'Tax Groups' window action and menu under Accounting Configuration, read access for the Rohana group, and the standard multi-company record rule. It adds no fields.
<!-- /SUMMARY -->

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Tax Groups | `action_1891_tax_groups` | Opens **Tax Group** records (tree,form). | `model account.tax.group` (account) | `menu BugFix-Accounting.menu_f6_tax_groups` |

**Views (2):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| account.tax.group.form | `ported_view_tax_group_form` | form | full form layout with 9 fields | Full form view for Tax Groups showing name, country, company, sequence, the tax payable/receivable/advance-payment accounts (filtered to the group's company) and the Preceding Subtotal label. | `account.tax.group.advance_tax_payment_account_id` (account)<br>`account.tax.group.company_id` (account)<br>`account.tax.group.country_id` (account)<br>`account.tax.group.name` (account)<br>`account.tax.group.preceding_subtotal` (account)<details><summary>+4 more</summary>`account.tax.group.sequence` (account)<br>`account.tax.group.tax_payable_account_id` (account)<br>`account.tax.group.tax_receivable_account_id` (account)<br>`group base.group_multi_company` (base)</details> |  |
| account.tax.group.tree | `ported_view_tax_group_tree` | tree | full tree layout with 10 fields | Editable list of Tax Groups (no create from the list) with drag-to-reorder sequence, name, country, company and the payable/receivable/advance tax accounts; Preceding Subtotal is an optional hidden column. | `account.tax.group.advance_tax_payment_account_id` (account)<br>`account.tax.group.company_id` (account)<br>`account.tax.group.country_code` (account)<br>`account.tax.group.country_id` (account)<br>`account.tax.group.name` (account)<details><summary>+5 more</summary>`account.tax.group.preceding_subtotal` (account)<br>`account.tax.group.sequence` (account)<br>`account.tax.group.tax_payable_account_id` (account)<br>`account.tax.group.tax_receivable_account_id` (account)<br>`group base.group_multi_company` (base)</details> |  |

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| access_account_tax_group_rohana_read | `access_f3_access_account_tax_group_rohana_read` | Gives **Other Extra Rights / Rohana** read access to Tax Group records. | `group studio_usermodel_migration.group_studio_518_rohana` (studio_usermodel_migration)<br>`model account.tax.group` (account) |  |
| access_account_tax_group_rohana_read | `access_g_access_account_tax_group_rohana_read_group_rohana` | Gives **Other Extra Rights / Rohana** read access to Tax Group records. | `group studio_usermodel_migration.group_studio_518_rohana` (studio_usermodel_migration)<br>`model account.tax.group` (account) |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Tax group multi-company | `rule_768_tax_group_multi_company` | For everyone (global rule): read/write/create/delete on Tax Group only where `[('company_id', 'parent_of', company_ids)]`. | `account.tax.group.company_id` (account)<br>`model account.tax.group` (account) |  |
