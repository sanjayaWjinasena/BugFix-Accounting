# BugFix-Accounting — `account.account`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.account` — Account

*Extends a model created by `account`.*

Other repos that use this model: `sale.order._seed_advance_payment_method_lines()` (Fix-repair)<br>`window action BugFix-Studio-Misc.act_window_1977_stock_picking_d7` (BugFix-Studio-Misc)<br>`window action BugFix-Studio-Misc.act_window_2190_project_budgeted_cash_flow_d7` (BugFix-Studio-Misc)<br>`window action BugFix-Studio-Misc.act_window_2191_project_budgeted_cash_flow_d7` (BugFix-Studio-Misc)<br>`x_bve.samplebalancemovementreport.x_bve_t1_account_id` (BugFix-Studio-Misc)<br>`x_consignment_header.x_studio_account_charge` (BugFix-Stock)<br>`x_consignment_header.x_studio_account_duty` (BugFix-Stock)<br>`x_consignment_header.x_studio_account_tax` (BugFix-Stock)<details><summary>+27 more</summary>`x_consignment_header.x_studio_offset_account` (BugFix-Stock)<br>`x_customer_group.x_studio_receivable_account` (studio_usermodel_migration)<br>`x_import_charges.x_studio_ledger_account` (BugFix-Purchase)<br>`x_imports_ledger_setup.x_studio_cash_issue_credit_acc` (BugFix-Purchase)<br>`x_imports_ledger_setup.x_studio_cash_settle_debit_acc` (BugFix-Purchase)<br>`x_imports_ledger_setup.x_studio_expense_account` (BugFix-Purchase)<br>`x_imports_ledger_setup.x_studio_import_tp_vend_acc_non_billable` (BugFix-Purchase)<br>`x_imports_ledger_setup.x_studio_import_tp_vend_non_billable_debit_acc` (BugFix-Purchase)<br>`x_imports_ledger_setup.x_studio_import_tp_vendor_account` (BugFix-Purchase)<br>`x_imports_ledger_setup.x_studio_import_tp_vendor_debit_acc` (BugFix-Purchase)<br>`x_imports_ledger_setup.x_studio_purch_packing_slip_offset_account` (BugFix-Purchase)<br>`x_imports_ledger_setup.x_studio_vat_receivable_account` (BugFix-Purchase)<br>`x_imports_ledger_setup.x_studio_vendor_despatch_credit_account` (BugFix-Purchase)<br>`x_imports_ledger_setup.x_studio_vendor_despatch_debit_account` (BugFix-Purchase)<br>`x_journal_types.x_studio_offset_account` (BugFix-Maintenance)<br>`x_misc_charge_codes.x_studio_credit_account` (BugFix-Stock)<br>`x_misc_charge_codes.x_studio_debit_account` (BugFix-Stock)<br>`x_repair_accounts.x_studio_rug_account` (Fix-repair)<br>`x_vendor_group.x_studio_payable_account` (studio_usermodel_migration)<br>`x_work_center_costing.x_studio_general_cost_credit_account` (BugFix-Studio-Misc)<br>`x_work_center_costing.x_studio_general_cost_debit_account` (BugFix-Studio-Misc)<br>`x_work_center_costing.x_studio_labour_cost_credit_account` (BugFix-Studio-Misc)<br>`x_work_center_costing.x_studio_labour_cost_debit_account` (BugFix-Studio-Misc)<br>`x_work_center_costing.x_studio_labour_ot_cost_credit_account` (BugFix-Studio-Misc)<br>`x_work_center_costing.x_studio_labour_ot_cost_debit_account` (BugFix-Studio-Misc)<br>`x_work_center_costing.x_studio_overhead_cost_credit_account` (BugFix-Studio-Misc)<br>`x_work_center_costing.x_studio_overhead_cost_debit_account` (BugFix-Studio-Misc)</details>

**Summary:**

<!-- SUMMARY:model:account.account -->
This repo adds no fields or logic to Chart of Accounts records. It ships two Studio list and form customizations: the list gains a record ID column and the form customization is empty. It also adds three window actions on accounts (two named 'Project Budgeted Cash Flow' and one named 'stock.picking') and the standard multi-company record rule.
<!-- /SUMMARY -->

**Window actions (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Project Budgeted Cash Flow | `action_2190_project_budgeted_cash_flow` | Opens **Account** records (kanban,tree,form). | `model account.account` (account) |  |
| Project Budgeted Cash Flow | `action_2191_project_budgeted_cash_flow` | Opens **Account** records (kanban,tree,form). | `model account.account` (account) |  |
| stock.picking | `action_1977_stock_picking` | Opens **Account** records (kanban,tree,form). | `model account.account` (account) |  |

**Views (2):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: account.account.form customization | `ported_view_2195_customization_account_account_form` | form |  | Empty Studio customization of the Chart of Accounts form; changes nothing. | `view account.view_account_form` (account) |  |
| Odoo Studio: account.account.list customization | `ported_view_2943_customization_account_account_tree` | tree | after `//field[@name='currency_id']`: add field id | Adds the record ID column after Currency in the Chart of Accounts list. | `view account.view_account_list` (account) |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Account multi-company | `rule_81_account_multi_company` | For everyone (global rule): read/write/create/delete on Account only where `[('company_id', 'parent_of', company_ids)]`. | `account.account.company_id` (account)<br>`model account.account` (account) |  |
