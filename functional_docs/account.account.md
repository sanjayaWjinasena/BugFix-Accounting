# BugFix-Accounting — `account.account`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.account` — Account

*Extends a model created by `account`.*

Other repos that use this model: `sale.order._seed_advance_payment_method_lines()` (Fix-repair)<br>`window action BugFix-Studio-Misc.act_window_1977_stock_picking_d7` (BugFix-Studio-Misc)<br>`window action BugFix-Studio-Misc.act_window_2190_project_budgeted_cash_flow_d7` (BugFix-Studio-Misc)<br>`window action BugFix-Studio-Misc.act_window_2191_project_budgeted_cash_flow_d7` (BugFix-Studio-Misc)<br>`bve.samplebalancemovementreport.bve_t1_account_id` (BugFix-Studio-Misc)<br>`consignment_header.account_charge` (BugFix-Stock)<br>`consignment_header.account_duty` (BugFix-Stock)<br>`consignment_header.account_tax` (BugFix-Stock)<details><summary>+27 more</summary>`consignment_header.offset_account` (BugFix-Stock)<br>`customer_group.receivable_account` (studio_usermodel_migration)<br>`import_charges.ledger_account` (BugFix-Purchase)<br>`imports_ledger_setup.cash_issue_credit_acc` (BugFix-Purchase)<br>`imports_ledger_setup.cash_settle_debit_acc` (BugFix-Purchase)<br>`imports_ledger_setup.expense_account` (BugFix-Purchase)<br>`imports_ledger_setup.import_tp_vend_acc_non_billable` (BugFix-Purchase)<br>`imports_ledger_setup.import_tp_vend_non_billable_debit_acc` (BugFix-Purchase)<br>`imports_ledger_setup.import_tp_vendor_account` (BugFix-Purchase)<br>`imports_ledger_setup.import_tp_vendor_debit_acc` (BugFix-Purchase)<br>`imports_ledger_setup.purch_packing_slip_offset_account` (BugFix-Purchase)<br>`imports_ledger_setup.vat_receivable_account` (BugFix-Purchase)<br>`imports_ledger_setup.vendor_despatch_credit_account` (BugFix-Purchase)<br>`imports_ledger_setup.vendor_despatch_debit_account` (BugFix-Purchase)<br>`journal_types.offset_account` (BugFix-Maintenance)<br>`misc_charge_codes.credit_account` (BugFix-Stock)<br>`misc_charge_codes.debit_account` (BugFix-Stock)<br>`repair_accounts.rug_account` (Fix-repair)<br>`vendor_group.payable_account` (studio_usermodel_migration)<br>`work_center_costing.general_cost_credit_account` (BugFix-Studio-Misc)<br>`work_center_costing.general_cost_debit_account` (BugFix-Studio-Misc)<br>`work_center_costing.labour_cost_credit_account` (BugFix-Studio-Misc)<br>`work_center_costing.labour_cost_debit_account` (BugFix-Studio-Misc)<br>`work_center_costing.labour_ot_cost_credit_account` (BugFix-Studio-Misc)<br>`work_center_costing.labour_ot_cost_debit_account` (BugFix-Studio-Misc)<br>`work_center_costing.overhead_cost_credit_account` (BugFix-Studio-Misc)<br>`work_center_costing.overhead_cost_debit_account` (BugFix-Studio-Misc)</details>

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
