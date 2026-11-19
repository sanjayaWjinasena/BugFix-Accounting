# BugFix-Accounting — `account.bank.statement`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.bank.statement` — Bank Statement

*Extends a model created by `account`.*

Other repos that use this model: `server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up` (BugFix-Studio-Misc)<br>`window action BugFix-Studio-Misc.act_window_2815_account_bank_statement_d7` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:account.bank.statement -->
This repo adds no fields or logic to bank statements. It adds one window action (list, form, pivot and graph) and three record rules: a company rule and two open-access rules for Accounting Billing and Point of Sale users.
<!-- /SUMMARY -->

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| account.bank.statement | `action_2815_account_bank_statement` | Opens **Bank Statement** records (tree,form,pivot,graph). | `model account.bank.statement` (account) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_account_bank_statement` (BugFix-Studio-Misc) |

**Record rules (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Account bank statement company rule | `rule_87_account_bank_statement_company_rule` | For everyone (global rule): read/write/create/delete on Bank Statement only where `[('company_id', 'in', company_ids + [False])]`. | `account.bank.statement.company_id` (account)<br>`model account.bank.statement` (account) |  |
| Point Of Sale Bank Statement Accountant | `rule_147_point_of_sale_bank_statement_accountant` | For Accounting / Billing: read/write/create/delete on Bank Statement with no record filter (empty domain = all records). | `group account.group_account_invoice` (account)<br>`model account.bank.statement` (account) |  |
| Point Of Sale Bank Statement POS User | `rule_146_point_of_sale_bank_statement_pos_user` | For Point of Sale / User: read/write/create/delete on Bank Statement with no record filter (empty domain = all records). | `group point_of_sale.group_pos_user` (point_of_sale)<br>`model account.bank.statement` (account) |  |
