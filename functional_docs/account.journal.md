# BugFix-Accounting — `account.journal`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.journal` — Journal

*Extends a model created by `account`.*

Other repos that use this model: `account.move._rug_auto_settle()` (Fix-repair)<br>`hr.contract.x_studio_related_field_Dj7xv` (BugFix-HR)<br>`sale.order._seed_advance_payment_method_lines()` (Fix-repair)<br>`server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_899_cash_purchase_cash_issued` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_917_cash_purchase_cash_settled` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_988_npo_invoice_journal` (BugFix-Purchase)<br>`server action BugFix-Sales.server_action_2341_sls_create_customer_payment` (BugFix-Sales)<details><summary>+5 more</summary>`server action BugFix-Stock.server_action_1305_imp_consignment_vendor_despatch` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_1321_imp_consignment_custom_duty` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_1358_imp_update_consignment` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_3647_consignment_vendor_dispatch_bugfix_purchase` (BugFix-Stock)<br>`window action BugFix-Studio-Misc.act_window_3275_journal_d7` (BugFix-Studio-Misc)</details>

**Summary:**

<!-- SUMMARY:model:account.journal -->
This repo adds no fields to journals. It adds a record ID column to the Journals list, an empty default pivot view and two window actions, one named 'Accounting Dashboard' and one named 'Journal'. It also ships the standard multi-company record rule.
<!-- /SUMMARY -->

**Window actions (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Accounting Dashboard | `act_window_339_accounting_dashboard` | Opens **Journal** records (kanban,form,pivot). | `model account.journal` (account) |  |
| Journal | `action_3275_journal` | Opens **Journal** records (kanban,tree,form,pivot). | `model account.journal` (account) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_journal` (BugFix-Studio-Misc) |

**Views (2):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default pivot view for ir.model(435,) | `ported_default_pivot_view_f_e6b5ae70_5837_410f_a7ec_43da4ff64f33` | pivot | full pivot layout with 0 fields | Empty default pivot view for Journals (no rows, columns or measures defined), with sample data enabled; gives the Journal action a pivot mode. |  |  |
| Odoo Studio: account.journal.tree customization | `ported_view_2549_customization_account_journal_tree` | tree | after `//field[@name='type']`: add field id | Adds the record ID column after Type in the Journals list. | `view account.view_account_journal_tree` (account) |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Journal multi-company | `rule_80_journal_multi_company` | For everyone (global rule): read/write/create/delete on Journal only where `[('company_id', 'parent_of', company_ids)]`. | `account.journal.company_id` (account)<br>`model account.journal` (account) |  |
