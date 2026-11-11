# BugFix-Accounting — `account.move`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.move` — Journal Entry

*Extends a model created by `account`.* Python: `models/account_move.py`.

Other repos that use this model: `account.move._bugfix_purchase_auto_reconcile_cp()` (BugFix-Purchase)<br>`account.move._rug_auto_settle()` (Fix-repair)<br>`sale.order._create_repair_full_invoice()` (Fix-repair)<br>`sale.order.write()` (Fix-repair)<br>`server action BugFix-Project.action_project_update_month_end_entries_2` (BugFix-Project)<br>`server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_update_actual_spent_in_cash_purchase` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_cash_purchase_cash_issued` (BugFix-Purchase)<details><summary>+22 more</summary>`server action BugFix-Purchase.action_cash_purchase_cash_settled` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_npo_invoice_journal` (BugFix-Purchase)<br>`server action BugFix-Stock.action_work_center_costing_model_create_journal_entries` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_consignment_vendor_despatch` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_consignment_custom_duty` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_update_consignment` (BugFix-Stock)<br>`server action BugFix-Stock.action_project_update_month_end_entries` (BugFix-Stock)<br>`server action BugFix-Stock.action_movement_journals_update_offset_account` (BugFix-Stock)<br>`server action BugFix-Stock.action_work_center_costing_model_create_journal_entries_original` (BugFix-Stock)<br>`server action BugFix-Stock.action_consignment_vendor_dispatch_bugfix_purchase` (BugFix-Stock)<br>`server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up` (BugFix-Studio-Misc)<br>`server action BugFix-Studio-Misc.server_action_2831_mst_odoo_data_clean_up_001` (BugFix-Studio-Misc)<br>`server action BugFix-Studio-Misc.server_action_2883_mst_odoo_data_clean_up_004` (BugFix-Studio-Misc)<br>`window action BugFix-Stock.action_vendor_despatch` (BugFix-Stock)<br>`window action BugFix-Stock.action_custom_clearance` (BugFix-Stock)<br>`window action BugFix-Stock.action_vend_dispatch_reversal` (BugFix-Stock)<br>`window action BugFix-Stock.action_custom_clearance_reversal` (BugFix-Stock)<br>`po_non_inventory._compute_related_account_move_count()` (BugFix-Purchase)<br>`x_product_test.x_studio_many2one_field_wTxgi` (BugFix-Studio-Misc)<br>`purchase_request_cas._compute_related_account_move_count()` (BugFix-Purchase)<br>`sales_report_model.related_field_nfrkz` (Jinasena_Masterdata_Reporting)<br>`sales_report_type.journal_entry_id` (Jinasena_Masterdata_Reporting)</details>

**Summary:**

<!-- SUMMARY:model:account.move -->
This repo adds 48 fields, Python computes, 49 server actions, 26 automations and two approval rules to journal entries. Together they drive Jinasena's invoice and bill controls. On customer invoices they handle credit limit and bank guarantee checks (from the source sales order), Repair-Under-Guarantee account updates, payment and RUG validation, and credit note approval requests with an approval rule. On vendor bills they handle import consignment updates (landed-cost lines and despatch and custom-clearance reversal entries), LC paid status, manual currency rates, and supplier invoice number syncing. Other logic copies project numbers by journal type, moves advance payment lines to the project advance account, sets analytic and report type parameters, and blocks deleting entries linked to cash or non-inventory purchases. Many automations and actions are duplicated legacy copies or archived. The repo also adds a customized invoice/entry form and lists, three report prints and eleven record rules.
<!-- /SUMMARY -->

**Fields (48):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `account_mandatory` | Account Mandatory | boolean | Whether an analytic account is mandatory on this entry; set by the 'Update Analytic Tag Parameters' automations from the matching analytic distribution model. | stored |  | `account.payment.account_mandatory`<br>`server action BugFix-Accounting.action_update_analytic_tag_parameters_sales_invoice_customer`<br>`server action BugFix-Accounting.action_update_analytic_tag_parameters_sales_invoice_user`<br>`view BugFix-Accounting.view_account_move_form_inherit_3` |
| `advance_acc_updated` | Advance ACC Updated | boolean | Set by the 'Project - Update Advance Payment Account - Vendor Bill' action once the income/expense line has been moved to the project advance account. | stored |  | `account.payment.advance_acc_updated`<br>`server action BugFix-Accounting.action_project_update_advance_payment_account_vendor_bill`<br>`server action BugFix-Accounting.srv_update_advance_payment_account_vendor_bill`<br>`view BugFix-Accounting.view_account_move_form_inherit_3` |
| `bank_guarantee_approved` | Bank Guarantee Approved | boolean | Whether the source sales order's bank guarantee was approved (related to Sale_Id); suppresses the bank guarantee notification/validation flags. | related `sale_id.bank_guarantee_approved`; stored | `account.move.sale_id`<br>`sale.order.bank_guarantee_approved` (BugFix-Sales) | `account.move._compute_bank_guarantee_notification()`<br>`account.move._compute_bank_guarantee_validation()`<br>`account.payment.bank_guarantee_approved`<br>`view BugFix-Accounting.view_account_move_form_inherit_3` |
| `bank_guarantee_notification` | Bank Guarantee Notification | boolean | True on customer invoices for non-General customer groups without a mandatory bank guarantee when the guarantee is expired or below customer balance + invoice total, unless approved. Used for warning display. | computed by `_compute_bank_guarantee_notification`; stored | `account.move._compute_bank_guarantee_notification()` | `account.move._compute_bank_guarantee_notification()`<br>`account.payment.bank_guarantee_notification`<br>`view BugFix-Accounting.view_account_move_form_inherit_3`<br>`view BugFix-Accounting.view_account_move_form_inherit` |
| `bank_guarantee_validation` | Bank Guarantee Validation | boolean | True on customer invoices for non-General customer groups with a mandatory bank guarantee when it is expired or below customer balance + invoice total, unless approved. Used to gate invoice buttons. | computed by `_compute_bank_guarantee_validation`; stored | `account.move._compute_bank_guarantee_validation()` | `account.move._compute_bank_guarantee_validation()`<br>`account.payment.bank_guarantee_validation`<br>`view BugFix-Accounting.view_account_move_form_inherit_3`<br>`view BugFix-Accounting.view_account_move_form_inherit` |
| `bg_sent` | BG Sent | boolean | Set after the bank guarantee notification has been sent from the invoice, so the 'SLS - Send Bank Guarantee Notification' action does not send duplicates; also controls button visibility. | stored |  | `account.payment.bg_sent`<br>`server action BugFix-Accounting.action_sls_send_bank_guarantee_notification_in_customer_invoice`<br>`server action BugFix-Accounting.srv_sls_send_bank_guarantee_notification`<br>`view BugFix-Accounting.view_account_move_form_inherit_3`<br>`view BugFix-Accounting.view_account_move_form_inherit` |
| `co` | Co | many2one → `consignment_header` | Consignment header link on journal entries; mirrored on payments, not used by any view or logic in this repo. | stored | `model consignment_header` (BugFix-Stock) | `account.payment.co` |
| `consignment_no` | Consignment No | many2one → `consignment_header` | Import consignment this bill/entry relates to; used by the consignment and supplier-invoice-number update actions, and source of the Custom Clearance No. | stored | `model consignment_header` (BugFix-Stock) | `account.move.custom_clearance_no`<br>`account.payment.consignment_no`<br>`automation BugFix-Accounting.automation_supplier_invoice_no_update_in_import_vendor_bill_3`<br>`server action BugFix-Accounting.action_imp_update_consignment_vendor_bill`<br>`server action BugFix-Accounting.action_imp_update_consignment_pi`<details><summary>+5 more</summary>`server action BugFix-Accounting.action_imp_update_consignment_vendor_bill_2`<br>`server action BugFix-Accounting.action_supplier_invoice_no_update_in_import_vendor_bill`<br>`server action BugFix-Accounting.action_supplier_invoice_no_update_in_import_vendor_bill_2`<br>`server action BugFix-Accounting.srv_imp_update_consignment_pi`<br>`view BugFix-Accounting.view_account_move_form_inherit_3`</details> |
| `create_from_transfer` | Create From Transfer | many2one → `stock.picking` | Stock transfer this entry was created from; mirrored on payments, not used by any view or logic in this repo. | stored | `model stock.picking` (stock) | `account.payment.create_from_transfer` |
| `create_from_transfer_1` | Create From Transfer | many2one → `stock.picking` | Transfer this custom-clearance reversal entry was created from; used to filter the 'Custom Clearance Reversal' window action. | stored | `model stock.picking` (stock) | `account.payment.create_from_transfer_1`<br>`view BugFix-Accounting.view_account_move_form_inherit_3`<br>`window action BugFix-Accounting.action_custom_clearance_reversal_3`<br>`window action BugFix-Accounting.action_custom_clearance_reversal`<br>`window action BugFix-Accounting.aw_f4_account_move_custom_clearance_reversal`<details><summary>+1 more</summary>`window action BugFix-Stock.action_custom_clearance_reversal` (BugFix-Stock)</details> |
| `created_from_consignment` | Created From Consignment | many2one → `consignment_header` | Consignment this vendor despatch entry was created from; filters the 'Vendor Despatch' window action. | stored | `model consignment_header` (BugFix-Stock) | `account.payment.created_from_consignment`<br>`view BugFix-Accounting.view_account_move_form_inherit_3`<br>`window action BugFix-Accounting.action_vendor_despatch_2`<br>`window action BugFix-Accounting.action_vendor_despatch`<br>`window action BugFix-Accounting.aw_f4_account_move_vendor_despatch`<details><summary>+1 more</summary>`window action BugFix-Stock.action_vendor_despatch` (BugFix-Stock)</details> |
| `created_from_consignment_1` | Created From Consignment | many2one → `consignment_header` | Consignment this custom clearance entry was created from; filters the 'Custom Clearance' window action. | stored | `model consignment_header` (BugFix-Stock) | `account.payment.created_from_consignment_1`<br>`view BugFix-Accounting.view_account_move_form_inherit_3`<br>`window action BugFix-Accounting.action_custom_clearance_2`<br>`window action BugFix-Accounting.action_custom_clearance`<br>`window action BugFix-Accounting.aw_f4_account_move_custom_clearance`<details><summary>+1 more</summary>`window action BugFix-Stock.action_custom_clearance` (BugFix-Stock)</details> |
| `created_from_project` | Created From Project | boolean | Checkbox marking that the entry was created from a project, shown on the entry form. | stored |  | `account.payment.created_from_project`<br>`view BugFix-Accounting.view_account_move_form_inherit_3` |
| `created_from_project_no` | Created From Project No | many2one → `project.project` | Project whose month-end entries include this entry; filters the 'Month End Entries' window action. | stored | `model project.project` (project) | `account.payment.created_from_project_no`<br>`view BugFix-Accounting.view_account_move_form_inherit_3`<br>`window action BugFix-Accounting.action_month_end_entries_2`<br>`window action BugFix-Accounting.action_month_end_entries`<br>`window action BugFix-Accounting.aw_f4_account_move_month_end_entries` |
| `created_from_transfer` | Created From Transfer | many2one → `stock.picking` | Transfer this vendor-dispatch reversal entry was created from; filters the 'Vend. Dispatch Reversal' window action. | stored | `model stock.picking` (stock) | `account.payment.created_from_transfer`<br>`view BugFix-Accounting.view_account_move_form_inherit_3`<br>`window action BugFix-Accounting.action_vend_dispatch_reversal_2`<br>`window action BugFix-Accounting.action_vend_dispatch_reversal`<br>`window action BugFix-Accounting.aw_f4_account_move_vend_dispatch_reversal`<details><summary>+1 more</summary>`window action BugFix-Stock.action_vend_dispatch_reversal` (BugFix-Stock)</details> |
| `created_from_vendor_bill` | Created From Vendor Bill | many2one → `account.move` | Vendor bill this dispatch reversal was created from; filters the 'Dispatch Reversal' action and feeds the 'Created From Vendor Bill count' smart button. | stored | `model account.move` (account) | `account.payment.created_from_vendor_bill`<br>`server action BugFix-Accounting.action_imp_update_consignment_pi`<br>`server action BugFix-Accounting.srv_imp_update_consignment_pi`<br>`view BugFix-Accounting.view_account_move_form_inherit_3`<br>`window action BugFix-Accounting.act_dispatch_reversal`<details><summary>+3 more</summary>`window action BugFix-Accounting.action_dispatch_reversal_2`<br>`window action BugFix-Accounting.action_dispatch_reversal`<br>`window action BugFix-Accounting.aw_f4_account_move_dispatch_reversal`</details> |
| `created_from_vendor_bill_1` | Created From Vendor Bill | many2one → `account.move` | Vendor bill this custom clearance reversal was created from; filters the 'Custom Clearance Reversal' action and feeds its count smart button. | stored | `model account.move` (account) | `account.payment.created_from_vendor_bill_1`<br>`server action BugFix-Accounting.action_imp_update_consignment_pi`<br>`server action BugFix-Accounting.srv_imp_update_consignment_pi`<br>`view BugFix-Accounting.view_account_move_form_inherit_3`<br>`window action BugFix-Accounting.act_custom_clearance_reversal`<details><summary>+2 more</summary>`window action BugFix-Accounting.action_custom_clearance_reversal_4`<br>`window action BugFix-Accounting.action_custom_clearance_reversal_2`</details> |
| `credit_limit_approved` | Credit Limit Approved | boolean | Whether the source sales order's credit limit overrun was approved (related to Sale_Id); suppresses Credit Limit Validation. | related `sale_id.credit_limit_approved`; stored | `account.move.sale_id`<br>`sale.order.credit_limit_approved` (BugFix-Sales) | `account.move._compute_credit_limit_validation()`<br>`account.payment.credit_limit_approved`<br>`view BugFix-Accounting.view_account_move_form_inherit_3` |
| `credit_limit_validation` | Credit Limit Validation | boolean | True when the order payment method is Credit, not yet approved, and customer balance + invoice total exceeds the customer's credit limit; gates buttons on the invoice form. | computed by `_compute_credit_limit_validation`; stored | `account.move._compute_credit_limit_validation()` | `account.move._compute_credit_limit_validation()`<br>`account.payment.credit_limit_validation`<br>`view BugFix-Accounting.view_account_move_form_inherit_3`<br>`view BugFix-Accounting.view_account_move_form_inherit` |
| `credit_note_approved` | Credit Note Approved | boolean | Set by the 'SLS - Credit Note Approval' action when the credit note is approved; controls button visibility on the form. | stored |  | `account.payment.credit_note_approved`<br>`server action BugFix-Accounting.action_sls_credit_note_approval`<br>`server action BugFix-Accounting.srv_sls_credit_note_approved_flag`<br>`view BugFix-Accounting.view_account_move_form_inherit_3`<br>`view BugFix-Accounting.view_account_move_form_inherit` |
| `credit_note_request_sent` | Credit Note Request Sent | boolean | Set by the 'SLS - Request Credit Note Approval' action once approval has been requested. | stored |  | `account.payment.credit_note_request_sent`<br>`server action BugFix-Accounting.action_sls_request_credit_note_approval_sent`<br>`server action BugFix-Accounting.srv_sls_credit_note_request_sent_flag`<br>`view BugFix-Accounting.view_account_move_form_inherit_3` |
| `currency_rate` | Currency Rate | float | Exchange rate for the vendor bill, used and filled by the 'IMP - Vendor Bill Currency Rate' action. | stored |  | `account.payment.currency_rate`<br>`server action BugFix-Accounting.action_imp_vendor_bill_currency_rate`<br>`server action BugFix-Accounting.srv_imp_vendor_bill_currency_rate`<br>`view BugFix-Accounting.view_account_move_form_inherit_3` |
| `currency_rate_updated` | Currency Rate Updated | boolean | Set by the 'IMP - Vendor Bill Currency Rate' action once the rate has been applied; controls button visibility. | stored |  | `account.payment.currency_rate_updated`<br>`server action BugFix-Accounting.action_imp_vendor_bill_currency_rate`<br>`server action BugFix-Accounting.srv_imp_vendor_bill_currency_rate`<br>`view BugFix-Accounting.view_account_move_form_inherit_3`<br>`view BugFix-Accounting.view_account_move_form_inherit` |
| `custom_clearance_no` | Custom Clearance No | char | Customs clearance number copied from the linked consignment (related via Consignment No). | related `consignment_no.custom_clearance_no`; stored | `account.move.consignment_no`<br>`consignment_header.custom_clearance_no` (BugFix-Stock) | `account.payment.custom_clearance_no`<br>`view BugFix-Accounting.view_account_move_form_inherit_3` |
| `journal_type` | Journal Type | selection: Bill=Bill; Payment=Payment; Settlement=Settlement | Project journal type (Bill, Payment, Settlement) with an ir.default default; the 'Project - Update Project No for Manual Transactions' automation copies Project No into the matching Bill/Issue/Settle project field. | stored |  | `account.move.line.journal_type`<br>`account.payment.journal_type`<br>`automation BugFix-Accounting.automation_project_update_project_no_for_manual_transactions_2`<br>`default BugFix-Accounting.default_account_move_journal_type`<br>`server action BugFix-Accounting.action_account_move_project_update_project_no_for_manual_transactions`<details><summary>+3 more</summary>`server action BugFix-Accounting.action_project_update_project_no_for_manual_transactions`<br>`view BugFix-Accounting.view_account_move_form_inherit_3`<br>`view BugFix-Accounting.view_account_invoice_tree_inherit_2`</details> |
| `lc_no` | LC No | many2one → `lc_header` | Letter of credit linked to the bill; used by the consignment update and 'IMP - Update LC Status to Paid' actions. | stored | `model lc_header` | `account.payment.lc_no`<br>`server action BugFix-Accounting.action_imp_update_consignment_vendor_bill`<br>`server action BugFix-Accounting.action_imp_update_lc_status_to_paid`<br>`view BugFix-Accounting.view_account_move_form_inherit_3` |
| `lc_test1` | LC - test1 | boolean | True when the bill's purchase order has an LC flag (`lc` from BugFix-Purchase); recomputes only when the purchase order changes, not when the PO flag changes. | computed by `_compute_lc_test1`; stored | `account.move._compute_lc_test1()` | `account.move._compute_lc_test1()`<br>`account.payment.lc_test1` |
| `order_payment_method` | Order Payment Method | selection: Credit=Credit; Cash=Cash | Payment method (Credit or Cash) of the source sales order (related to Sale_Id); Credit enables the credit limit check. | related `sale_id.order_payment_method`; stored | `account.move.sale_id`<br>`sale.order.order_payment_method` (BugFix-Sales) | `account.move._compute_credit_limit_validation()`<br>`account.payment.order_payment_method`<br>`server action BugFix-Accounting.action_account_move_sls_validate_payment_in_customer_invoice`<br>`server action BugFix-Accounting.action_sls_validate_payment_in_customer_invoice`<br>`server action BugFix-Accounting.action_sls_view_credit_limit_validation_in_customer_invoice`<details><summary>+2 more</summary>`server action BugFix-Accounting.srv_sls_view_credit_limit_validation`<br>`view BugFix-Accounting.view_account_move_form_inherit_3`</details> |
| `over_bank_guarantee` | Over Bank Guarantee | boolean | Whether the source sales order exceeds the customer's bank guarantee (related to Sale_Id), shown on the invoice form. | related `sale_id.over_bank_guarantee`; stored | `account.move.sale_id`<br>`sale.order.over_bank_guarantee` (BugFix-Sales) | `account.payment.over_bank_guarantee`<br>`view BugFix-Accounting.view_account_move_form_inherit_3` |
| `project_no` | Project No | many2one → `project.project` | Project the journal entry is posted against; the manual-transaction automation copies it into the Bill/Issue/Settle project fields, and journal items show it. | stored | `model project.project` (project) | `account.move.line.project_no`<br>`account.payment.project_no`<br>`server action BugFix-Accounting.action_account_move_project_update_project_no_for_manual_transactions`<br>`server action BugFix-Accounting.action_project_update_project_no_for_manual_transactions`<br>`view BugFix-Accounting.view_account_move_form_inherit_3`<details><summary>+4 more</summary>`view BugFix-Accounting.view_account_invoice_tree_inherit_2`<br>`window action BugFix-Accounting.action_journal_entries_2`<br>`window action BugFix-Accounting.action_journal_entries`<br>`window action BugFix-Accounting.aw_f4_account_move_journal_entries`</details> |
| `project_no_bill` | Project No Bill | many2one → `project.project` | Project for cash-advance bills; set automatically when Journal Type is Bill and used by the 'Cash Advance Bills' window action. | stored | `model project.project` (project) | `account.payment.project_no_bill`<br>`server action BugFix-Accounting.action_account_move_project_update_project_no_for_manual_transactions`<br>`server action BugFix-Accounting.action_project_update_project_no_for_manual_transactions`<br>`view BugFix-Accounting.view_account_move_form_inherit_3`<br>`window action BugFix-Accounting.action_cash_advance_bills_2`<details><summary>+2 more</summary>`window action BugFix-Accounting.action_cash_advance_bills`<br>`window action BugFix-Accounting.aw_f4_account_move_cash_advance_bills`</details> |
| `project_no_issue` | Project No Issue | many2one → `project.project` | Project for issued cash advances; set automatically when Journal Type is Payment and used by the 'Issued Cash Advances' window action. | stored | `model project.project` (project) | `account.payment.project_no_issue`<br>`server action BugFix-Accounting.action_account_move_project_update_project_no_for_manual_transactions`<br>`server action BugFix-Accounting.action_project_update_project_no_for_manual_transactions`<br>`view BugFix-Accounting.view_account_move_form_inherit_3`<br>`window action BugFix-Accounting.action_issued_cash_advances_2`<details><summary>+2 more</summary>`window action BugFix-Accounting.action_issued_cash_advances`<br>`window action BugFix-Accounting.aw_f4_account_move_issued_cash_advances`</details> |
| `project_no_settle` | Project No Settle | many2one → `project.project` | Project for settled cash advances; set automatically when Journal Type is Settlement and used by the 'Settled Cash Advances' window action. | stored | `model project.project` (project) | `account.payment.project_no_settle`<br>`server action BugFix-Accounting.action_account_move_project_update_project_no_for_manual_transactions`<br>`server action BugFix-Accounting.action_project_update_project_no_for_manual_transactions`<br>`view BugFix-Accounting.view_account_move_form_inherit_3`<br>`window action BugFix-Accounting.action_settled_cash_advances_2`<details><summary>+2 more</summary>`window action BugFix-Accounting.action_settled_cash_advances`<br>`window action BugFix-Accounting.aw_f4_account_move_settled_cash_advances`</details> |
| `accounting_purchase_id` | Purchase Order | many2one → `purchase.order` | Purchase order linked to the bill; used by consignment-update and payment reconciliation actions and source of PR Type. | stored | `model purchase.order` (purchase) | `account.move._compute_purchase_type()`<br>`account.payment.accounting_purchase_id`<br>`server action BugFix-Accounting.action_imp_update_consignment_vendor_bill`<br>`server action BugFix-Accounting.action_imp_update_consignment_pi`<br>`server action BugFix-Accounting.action_imp_update_consignment_vendor_bill_2`<details><summary>+3 more</summary>`server action BugFix-Accounting.action_sls_payment_reconciliation_automate`<br>`server action BugFix-Accounting.srv_imp_update_consignment_pi`<br>`view BugFix-Accounting.view_account_move_form_inherit_3`</details> |
| `purchase_type` | PR Type | selection: Local=Local; Import=Import | PR type (Local or Import) copied at compute time from the linked purchase order's `pr_type` (BugFix-Purchase field); empty if that field is absent. | computed by `_compute_purchase_type`; stored | `account.move._compute_purchase_type()` | `account.move._compute_purchase_type()`<br>`account.move.line.pr_type`<br>`account.payment.purchase_type`<br>`view BugFix-Accounting.view_account_move_form_inherit_3` |
| `report_type_s_cust_aging` | Report Type (S - Cust Aging) | many2one → `sales_report_type` | Links a customer invoice to the Sales Report Type used for the Customer Aging report; set automatically on customer invoices by the 'SRM - Auto Populate Report Type in Account Move' automation and shown on the invoice form. Inverse of the report type's Journal Entry list. | stored | `model sales_report_type` (Jinasena_Masterdata_Reporting) | `account.payment.report_type_s_cust_aging` (Jinasena_Masterdata_Reporting)<br>`server action BugFix-Accounting.action_srm_auto_populate_report_type_in_account_move`<br>`view BugFix-Accounting.view_account_move_form_inherit_3`<br>`view BugFix-Accounting.view_account_out_invoice_tree_inherit_3` |
| `rug_acc_updated` | RUG Account Updated | boolean | Set by the 'RR - RUG Account Update in SI' action after the Repair-Under-Guarantee account is applied on the invoice; checked by the RUG validation. | stored |  | `account.payment.rug_acc_updated`<br>`server action BugFix-Accounting.action_account_move_rr_validate_rug_in_customer_invoice`<br>`server action BugFix-Accounting.action_rr_rug_account_update_in_si`<br>`server action BugFix-Accounting.action_rr_validate_rug_in_customer_invoice`<br>`server action BugFix-Accounting.srv_rug_account_update_in_si`<details><summary>+2 more</summary>`view BugFix-Accounting.view_account_move_form_inherit_3`<br>`view BugFix-Accounting.view_account_move_form_inherit`</details> |
| `rug_confirmed` | RUG Confirmed | boolean | Whether Repair-Under-Guarantee was confirmed on the source sales order (related to Sale_Id); triggers the RUG account update and validation. | related `sale_id.rug_confirmed`; stored | `account.move._compute_rug_confirmed()` (Fix-repair)<br>`account.move.sale_id`<br>`sale.order.rug_confirmed` (BugFix-Sales) | `account.payment.rug_confirmed`<br>`server action BugFix-Accounting.action_account_move_rr_validate_rug_in_customer_invoice`<br>`server action BugFix-Accounting.action_rr_rug_account_update_in_si`<br>`server action BugFix-Accounting.action_rr_validate_rug_in_customer_invoice`<br>`server action BugFix-Accounting.srv_rug_account_update_in_si`<details><summary>+2 more</summary>`view BugFix-Accounting.view_account_move_form_inherit_3`<br>`view BugFix-Accounting.view_account_move_form_inherit`</details> |
| `rug_rejected` | RUG Rejected | boolean | Whether Repair-Under-Guarantee was rejected on the source sales order (related to Sale_Id), so the customer pays; controls buttons on the invoice form. | related `sale_id.rug_rejected`; stored | `account.move.sale_id`<br>`sale.order.rug_rejected` (BugFix-Sales) | `account.payment.rug_rejected`<br>`view BugFix-Accounting.view_account_move_form_inherit_3`<br>`view BugFix-Accounting.view_account_move_form_inherit` |
| `sale_id` | Sale_Id | many2one → `sale.order` | Sales order this invoice was created from; source of the credit limit, bank guarantee, payment method and RUG flags, and used by the related validation actions. | stored | `model sale.order` (sale) | `account.move.bank_guarantee_approved`<br>`account.move.credit_limit_approved`<br>`account.move.order_payment_method`<br>`account.move.over_bank_guarantee`<br>`account.move.rug_confirmed`<details><summary>+14 more</summary>`account.move.rug_rejected`<br>`account.payment.sale_id`<br>`server action BugFix-Accounting.action_account_move_rr_validate_rug_in_customer_invoice`<br>`server action BugFix-Accounting.action_account_move_sls_validate_bank_guarantee_in_customer_invoice`<br>`server action BugFix-Accounting.action_account_move_sls_validate_payment_in_customer_invoice`<br>`server action BugFix-Accounting.action_srm_update_sales_order_customer_invoice`<br>`server action BugFix-Accounting.action_sls_validate_payment_in_customer_invoice`<br>`server action BugFix-Accounting.action_sls_validate_bank_guarantee_in_customer_invoice`<br>`server action BugFix-Accounting.action_sls_send_bank_guarantee_notification_in_customer_invoice`<br>`server action BugFix-Accounting.action_sls_view_bank_guarantee_validation_in_customer_invoice`<br>`server action BugFix-Accounting.action_rr_validate_rug_in_customer_invoice`<br>`server action BugFix-Accounting.srv_sls_send_bank_guarantee_notification`<br>`server action BugFix-Accounting.srv_sls_view_bank_guarantee_validation`<br>`view BugFix-Accounting.view_account_move_form_inherit_3`</details> |
| `supplier_invoice_number` | XXX Supplier's Invoice Number (Bill Reference) | char | Supplier's invoice number (bill reference) on the entry; kept in sync by the 'Supplier Invoice No Update' automations. | stored |  | `account.payment.supplier_invoice_number`<br>`server action BugFix-Accounting.action_supplier_invoice_no_update_in_import_vendor_bill`<br>`server action BugFix-Accounting.action_supplier_invoice_no_update_in_import_vendor_bill_2`<br>`view BugFix-Accounting.view_account_move_form_inherit_3` |
| `test_type` | Test Type | selection: One=One; Two=Two | Test selection (One/Two) shown on the entry form; no business logic uses it. | stored |  | `account.payment.test_type`<br>`view BugFix-Accounting.view_account_move_form_inherit_3` |
| `tp_id` | Created From TP Invoice | many2one → `tp_invoice_header` | TP invoice this vendor bill was created from; filters the 'Vendor Bill' window action of the TP invoice. | stored | `model tp_invoice_header` | `account.payment.tp_id`<br>`view BugFix-Accounting.view_account_move_form_inherit_3`<br>`window action BugFix-Accounting.act_tp_invoice_vendor_bill`<br>`window action BugFix-Accounting.action_vendor_bill_4`<br>`window action BugFix-Accounting.action_vendor_bill_2`<details><summary>+1 more</summary>`window action BugFix-Accounting.aw_f4_account_move_vendor_bill`</details> |
| `type` | Type | selection: General=General; Advance Payment=Advance Payment | Entry type: General or Advance Payment. When Advance Payment, the 'Project - Update Advance Payment Account' action moves the income/expense line to the project advance account. | stored |  | `server action BugFix-Accounting.action_project_update_advance_payment_account_vendor_bill`<br>`server action BugFix-Accounting.srv_update_advance_payment_account_vendor_bill`<br>`view BugFix-Accounting.view_account_move_form_inherit_3` |
| `update_consignment` | Update Consignment | boolean | Flag set by the 'IMP - Update Consignment' actions once the linked consignment has been updated from this bill; controls button visibility. | stored |  | `account.payment.update_consignment`<br>`server action BugFix-Accounting.action_imp_update_consignment_vendor_bill`<br>`server action BugFix-Accounting.action_imp_update_consignment_pi`<br>`server action BugFix-Accounting.action_imp_update_consignment_vendor_bill_2`<br>`server action BugFix-Accounting.srv_imp_update_consignment_pi`<details><summary>+2 more</summary>`view BugFix-Accounting.view_account_move_form_inherit_3`<br>`view BugFix-Accounting.view_account_move_form_inherit`</details> |
| `valid_lines` | Valid Lines | boolean | True when the invoice has no lines or when any non-display line has a zero unit price. Despite its name it flags zero-priced lines, not valid ones. | computed by `_compute_valid_lines`; not stored | `account.move._compute_valid_lines()` | `account.move._compute_valid_lines()`<br>`account.payment.valid_lines`<br>`view BugFix-Accounting.view_account_move_form_inherit_3` |
| `created_from_vendor_bill_1__account_move_count` | Created From Vendor Bill count | integer | Number of entries whose 'Created From Vendor Bill' (custom clearance reversal link) points to this entry; feeds a smart button. | computed by `_compute_vendor_bill_1_count`; not stored | `account.move._compute_vendor_bill_1_count()` | `account.move._compute_vendor_bill_1_count()`<br>`account.payment.created_from_vendor_bill_1__account_move_count`<br>`view BugFix-Accounting.view_account_move_form_inherit_3` |
| `created_from_vendor_bill__account_move_count` | Created From Vendor Bill count | integer | Number of entries whose 'Created From Vendor Bill' (dispatch reversal link) points to this entry; feeds a smart button. | computed by `_compute_vendor_bill_count`; not stored | `account.move._compute_vendor_bill_count()` | `account.move._compute_vendor_bill_count()`<br>`account.payment.created_from_vendor_bill__account_move_count`<br>`view BugFix-Accounting.view_account_move_form_inherit_3` |

**Python methods (8):**

| Method | Function | Decorators | Extends standard | Depends on | Used by | Where |
|---|---|---|---|---|---|---|
| `_compute_bank_guarantee_notification` | Compute for Bank Guarantee Notification: on unapproved customer invoices of non-General customer groups where the bank guarantee is NOT mandatory, flags True if the guarantee is expired or the guarantee amount is below customer credit plus invoice total. | api.depends('partner_id', 'amount_total', 'bank_guarantee_approved', 'm… |  | `account.move.amount_total` (account)<br>`account.move.move_type` (account)<br>`account.move.partner_id` (account)<br>`account.move.bank_guarantee_approved`<br>`account.move.bank_guarantee_notification` | `account.move.bank_guarantee_notification` | `models/account_move.py:116` |
| `_compute_bank_guarantee_validation` | Compute for Bank Guarantee Validation: on unapproved customer invoices of non-General customer groups where the bank guarantee IS mandatory, flags True if the guarantee is expired or below customer credit plus invoice total. | api.depends('partner_id', 'amount_total', 'bank_guarantee_approved', 'm… |  | `account.move.amount_total` (account)<br>`account.move.move_type` (account)<br>`account.move.partner_id` (account)<br>`account.move.bank_guarantee_approved`<br>`account.move.bank_guarantee_validation` | `account.move.bank_guarantee_validation` | `models/account_move.py:140` |
| `_compute_credit_limit_validation` | Compute for Credit Limit Validation: when not already credit-approved and payment method is Credit, True if the customer's current credit plus this invoice total exceeds the customer's credit limit. | api.depends('partner_id', 'partner_id.credit', 'partner_id.credit_limit', 'amoun… |  | `account.move.amount_total` (account)<br>`account.move.partner_id` (account)<br>`account.move.credit_limit_approved`<br>`account.move.credit_limit_validation`<br>`account.move.order_payment_method`<details><summary>+2 more</summary>`res.partner.credit_limit` (account)<br>`res.partner.credit` (account)</details> | `account.move.credit_limit_validation` | `models/account_move.py:165` |
| `_compute_valid_lines` | Compute for Valid Lines: True if any product line (non-section/note) has a unit price of 0, or if the invoice has no lines at all; otherwise False. | api.depends('invoice_line_ids', 'invoice_line_ids.price_unit', 'invoice_line_ids… |  | `account.move.invoice_line_ids` (account)<br>`account.move.line.display_type` (account)<br>`account.move.line.price_unit` (account)<br>`account.move.valid_lines` | `account.move.valid_lines` | `models/account_move.py:176` |
| `_compute_lc_test1` | Compute for LC Test1: True when the linked purchase order has an LC (`lc`) set; returns False if that PO field is not installed. Recalculates only when the purchase order changes. | api.depends('purchase_id') |  | `account.move.purchase_id` (purchase)<br>`account.move.lc_test1` | `account.move.lc_test1` | `models/account_move.py:187` |
| `_compute_purchase_type` | Compute for Purchase Type: copies the PR type (`pr_type`) from the linked purchase order, or False if no PO or the field is not installed. | api.depends('accounting_purchase_id') |  | `account.move.accounting_purchase_id`<br>`account.move.purchase_type` | `account.move.purchase_type` | `models/account_move.py:203` |
| `_compute_vendor_bill_count` | Compute for the smart-button count of journal entries whose Created From Vendor Bill field points at this entry. |  |  | `account.move.created_from_vendor_bill__account_move_count`<br>`model account.move` (account) | `account.move.created_from_vendor_bill__account_move_count` | `models/account_move.py:212` |
| `_compute_vendor_bill_1_count` | Compute for the smart-button count of journal entries whose Created From Vendor Bill 1 field points at this entry. |  |  | `account.move.created_from_vendor_bill_1__account_move_count`<br>`model account.move` (account) | `account.move.created_from_vendor_bill_1__account_move_count` | `models/account_move.py:217` |

**Server actions (49):**

- **Execute Code** (`action_rr_validate_rug_in_customer_invoice`, type `code`)
  - Function: Run by the RR Validate RUG automation: for posted RUG-confirmed, RUG-updated invoices, sets Payment Status to In Payment if the SO is Done, else raises 'Incomplete sales order'.
  - Depends on: `account.move.state` (account), `account.move.rug_acc_updated`, `account.move.rug_confirmed`, `account.move.sale_id`, `model account.move` (account)<details><summary>+1 more</summary>`model sale.order` (sale)</details>
  - Used by: `automation BugFix-Accounting.automation_rr_validate_rug_in_customer_invoice_2`
  <details><summary>code (9 lines)</summary>

```python
if record.rug_confirmed == True:
    if record.rug_acc_updated == True:
        if record.state == "posted":
            so = env["sale.order"].search(
                [("id", "=", record.sale_id.id), ("state", "=", "done")],
                limit=1,
            )
            if so:
                record["payment_state"] = "in_payment"
            else:
                raise UserError("Incomplete sales order. Process terminatedddd.")
```
  </details>
- **Execute Code** (`action_project_update_project_no_for_manual_transactions`, type `code`)
  - Function: Run by the Project automation on journal entries: copies Project No into Project No Bill, Issue or Settle according to Journal Type (Bill/Payment/Settlement), clearing the other two; clears all three for other types.
  - Depends on: `account.move.journal_type`, `account.move.project_no_bill`, `account.move.project_no_issue`, `account.move.project_no_settle`, `account.move.project_no`<details><summary>+1 more</summary>`model account.move` (account)</details>
  - Used by: `automation BugFix-Accounting.automation_project_update_project_no_for_manual_transactions_2`
  <details><summary>code (10 lines)</summary>

```python
if record.project_no != False:
    if record.journal_type == "Bill":
        record.write(
            {
                "project_no_bill": record.project_no.id,
                "project_no_issue": False,
                "project_no_settle": False,
            }
        )
    elif record.journal_type == "Payment":
        record.write(
            {
                "project_no_bill": False,
                "project_no_issue": record.project_no.id,
                "project_no_settle": False,
            }
        )
    elif record.journal_type == "Settlement":
        record.write(
            {
                "project_no_bill": False,
                "project_no_issue": False,
                "project_no_settle": record.project_no.id,
            }
        )
    else:
        record.write(
            {
                "project_no_bill": False,
                "project_no_issue": False,
                "project_no_settle": False,
            }
        )
```
  </details>
- **Execute Code** (`action_sls_validate_bank_guarantee_in_customer_invoice`, type `code`)
  - Function: Run by the bank-guarantee automation on posted customer invoices of non-General customers: blocks posting if a mandatory guarantee is expired or below credit plus invoice total; for non-mandatory guarantees posts a chatter warning instead.
  - Depends on: `account.move.amount_total` (account), `account.move.move_type` (account), `account.move.partner_id` (account), `account.move.state` (account), `account.move.sale_id`<details><summary>+1 more</summary>`model account.move` (account)</details>
  - Used by: `automation BugFix-Accounting.automation_sls_validate_bank_guarantee_in_customer_invoice_2`
  <details><summary>code (23 lines)</summary>

```python
if record.partner_id.customer_rank > 0:
    if record.state == "posted":
        if record.move_type == "out_invoice":
            if (
                record.partner_id.customer_group.group_type
                != "General"
            ):
                if record.partner_id.mandatory_bank_guarantee == True:
                    if (
                        record.partner_id.expiry_date
                        and record.partner_id.expiry_date
                        < datetime.date.today()
                    ):
                        # raise UserError("Customer's bank guarantee is expired.")
                        raise UserError(
                            "Customer's bank guarantee is expired."
                            + "\n"
                            + "Bank guaranty expiry date: "
                            + str(record.partner_id.expiry_date)
                        )
                    else:
                        # if record.partner_id.mandatory_bank_guarantee < (record.partner_id.credit + record.amount_total):
                        if record.partner_id.bank_guarantee_amount < (
                            record.partner_id.credit + record.amount_total
                        ):
                            # raise UserError("Customer's balance exceeds the bank guarantee amount." + "\n" + "Bank guarantee limit: " + "\n" + str(record.partner_id.mandatory_bank_guarantee) + "\n" + "New balance: " + "\n" + str((record.partner_id.credit + record.amount_total)))
                            # raise UserError("Customer's balance exceeds the bank guarantee amount." + "\n" + "Bank guarantee amount: " + str(record.partner_id.bank_guarantee_amount) + "\n" + "Current Balance: " + str(record.partner_id.credit) + '\n' + "This Sale: " + str(record.amount_total) + "\n" + "New balance: " + str(record.partner_id.credit + record.amount_total))
                            raise UserError(
                                "The credit limit is higher than the bank guarantee amount."
                                + "\n"
                                + "Customer: "
                                + record.partner_id.name
                                + "\n"
                                + " Sales Order: "
                                + record.sale_id.name
                                + "\n"
                                + "Bank guarantee amount: "
                                + str(record.partner_id.bank_guarantee_amount)
                                + "\n"
                                + "Current Balance: "
                                + str(record.partner_id.credit)
                                + "\n"
                                + "This Sale: "
                                + str(record.amount_total)
                                + "\n"
                                + "New balance: "
                                + str(record.partner_id.credit + record.amount_total)
                            )
                else:
                    if (
                        record.partner_id.expiry_date
                        and record.partner_id.expiry_date
                        < datetime.date.today()
                    ):
                        records.message_post(
                            body="Customer's bank guarantee is expired."
                            + "\n"
                            + "Bank guaranty expiry date: "
                            + str(record.partner_id.expiry_date)
                        )
                    else:
                        if record.partner_id.bank_guarantee_amount < (
                            record.partner_id.credit + record.amount_total
                        ):
                            # records.message_post(body="Customer's balance exceeds the bank guarantee amount." + "\n" + "Bank guarantee limit: " + "\n" + str(record.partner_id.mandatory_bank_guarantee) + "\n" + "New balance: " + "\n" + str((record.partner_id.credit + record.amount_total)))
                            # records.message_post(body="Customer's balance exceeds the bank guarantee amount." + "\n" + "Bank guarantee amount: " + str(record.partner_id.bank_guarantee_amount) + "\n" + "Current Balance: " + str(record.partner_id.credit) + '\n' + "This Sale: " + str(record.amount_total) + "\n" + "New balance: " + str(record.partner_id.credit + record.amount_total))
                            records.message_post(
                                body="The credit limit is higher than the bank guarantee amount."
                                + "\n"
                                + "Customer: "
                                + str(record.partner_id.name)
                                + "\n"
                                + " Sales Order: "
                                + str(record.sale_id.name)
                                + "\n"
                                + "Bank guarantee amount: "
                                + str(record.partner_id.bank_guarantee_amount)
                                + "\n"
                                + "Current Balance: "
                                + str(record.partner_id.credit)
                                + "\n"
                                + "This Sale: "
                                + str(record.amount_total)
                                + "\n"
                                + "New balance: "
                                + str(record.partner_id.credit + record.amount_total)
                            )
```
  </details>
- **IMP - Testing** (`action_imp_testing`, type `code`)
  - Function: Test action on bills: adds hard-coded charge (10), duty (20) and tax (30) landed-cost lines plus a TP vendor offset line to the entry. Test code with fixed values and an Odoo 14 field (`exclude_from_invoice_tab`); not for production use.
  - Depends on: `account.move.currency_id` (account), `account.move.partner_id` (account), `model account.move.line` (account), `model account.move` (account), `model product.product` (product)<details><summary>+1 more</summary>`model imports_ledger_setup` (BugFix-Purchase)</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (85 lines)</summary>

```python
if record.id:
    invoice_lines = []
    charge = 0
    duty = 0
    tax = 0

    charge = 10
    duty = 20
    tax = 30

    if charge > 0.0000:
        product_charge = env["product.product"].search(
            [("charge", "=", True)], limit=1
        )
        if product_charge:
            invoice_lines.append(
                [
                    0,
                    0,
                    {
                        "move_id": record.id,
                        "partner_id": record.partner_id.id,
                        "product_id": product_charge.id,
                        "quantity": 1,
                        "currency_id": record.currency_id.id,
                        "name": product_charge.name,
                        "product_uom_id": product_charge.uom_id.id,
                        "is_landed_costs_line": True,
                        "price_unit": charge,
                        "price_subtotal": charge,
                        "account_id": 4,
                    },
                ]
            )

    if duty > 0.0000:
        product_duty = env["product.product"].search(
            [("duty", "=", True)], limit=1
        )
        if product_duty:
            invoice_lines.append(
                [
                    0,
                    0,
                    {
                        "move_id": record.id,
                        "partner_id": record.partner_id.id,
                        "product_id": product_duty.id,
                        "quantity": 1,
                        "currency_id": record.currency_id.id,
                        "name": product_duty.name,
                        "product_uom_id": product_duty.uom_id.id,
                        "is_landed_costs_line": True,
                        "price_unit": duty,
                        "price_subtotal": duty,
                        "account_id": 4,
                    },
                ]
            )

    if tax > 0.0000:
        product_tax = env["product.product"].search(
            [("tax", "=", True)], limit=1
        )
        if product_tax:
            invoice_lines.append(
                [
                    0,
                    0,
                    {
                        "move_id": record.id,
                        "partner_id": record.partner_id.id,
                        "product_id": product_tax.id,
                        "quantity": 1,
                        "currency_id": record.currency_id.id,
                        "name": product_tax.name,
                        "product_uom_id": product_tax.uom_id.id,
                        "is_landed_costs_line": True,
                        "price_unit": tax,
                        "price_subtotal": tax,
                        "account_id": 4,
                    },
                ]
            )

    if (charge + duty + tax) > 0.0000:
        tp_account = env["imports_ledger_setup"].search([("id", "=", 1)], limit=1)
        if tp_account:
            if tp_account.import_tp_vendor_account.id == 0:
                raise UserError(
                    "Import TP Vendor Account must be Specified in Imports Ledger Setup"
                )

            invoice_lines.append(
                [
                    0,
                    0,
                    {
                        "move_id": record.id,
                        "partner_id": record.partner_id.id,
                        "quantity": 1,
                        "currency_id": record.currency_id.id,
                        "name": tp_account.import_tp_vendor_account.name,
                        "price_unit": -(charge + duty + tax),
                        "price_subtotal": -(charge + duty + tax),
                        "credit": (charge + duty + tax),
                        "account_id": tp_account.import_tp_vendor_account.id,
                        "exclude_from_invoice_tab": True,
                    },
                ]
            )

            record.with_context(check_move_validity=True).write(
                {"line_ids": invoice_lines}
            )

# if (charge + duty + tax) > 0.0000:
#    record.with_context(check_move_validity = False).write({'line_ids':invoice_lines})

#    create_charges = env['account.move.line'].with_context(check_move_validity = False).create({'move_id':record.id,'partner_id':record.partner_id.id,'product_id':product_charge.id,'quantity':1,'currency_id':record.currency_id.id,'name':product_charge.name,'product_uom_id':product_charge.uom_id.id,'is_landed_costs_line':True,'price_unit':10.00,'price_subtotal':10.00,'account_id':4})
#    payable_account = env['account.move.line'].with_context(check_move_validity = True).search([('move_id', '=', record.id), ('account_id', '=', record.partner_id.property_account_payable_id.id)], limit=1)
#    if payable_account:
#      payable_account.write({'credit':(payable_account.credit + (charge + duty + tax))})
```
  </details>
- **IMP - Update Consignment - PI** (`srv_imp_update_consignment_pi`, type `code`)
  - Function: Import vendor bill button: validates the consignment matches the PO lines, then adds charge/duty/tax landed-cost lines and creates and posts vendor despatch and custom-clearance reversal entries using Imports Ledger Setup accounts; marks Update Consignment. Uses Odoo 14 field `exclude_from_invoice_tab`.
  - Depends on: `account.move.currency_id` (account), `account.move.invoice_line_ids` (account), `account.move.partner_id` (account), `account.move.consignment_no`, `account.move.created_from_vendor_bill_1`<details><summary>+14 more</summary>`account.move.created_from_vendor_bill`, `account.move.accounting_purchase_id`, `account.move.update_consignment`, `model account.journal` (account), `model account.move.line` (account), `model account.move` (account), `model product.product` (product), `model res.company` (base), `model res.config.settings` (base), `model res.currency.rate` (base), `model res.currency` (base), `model consignment_header` (BugFix-Stock), `model consignment_line` (BugFix-Stock), `model imports_ledger_setup` (BugFix-Purchase)</details>
  - Used by: `view BugFix-Accounting.view_account_move_form_inherit_3`
  <details><summary>code (575 lines)</summary>

```python
if record.id:
    company_id = env.context.get("allowed_company_ids", [env.user.company_id.id])[0]
    company = env["res.company"].browse(company_id)

    con_line = env["consignment_line"].search(
        [
            ("consignment_header_id", "=", record.consignment_no.id),
            ("accounting_purchase_id", "=", record.accounting_purchase_id.id),
        ],
        limit=1,
    )
    if not con_line:
        raise UserError(
            "The Selected Consignment No is not linked with the Current PO."
        )

    ex_rate = 1

    company_currency = env["res.config.settings"].search(
        [("currency_id", "=", record.currency_id.id)], limit=1
    )
    if company_currency:
        ex_rate = 1
    else:
        custom_currency = env["res.currency"].search(
            [("id", "=", record.currency_id.id), ("active", "=", True)], limit=1
        )
        if custom_currency:
            custom_currency_rate = env["res.currency.rate"].search(
                [
                    ("currency_id", "=", custom_currency.id),
                    ("name", "<=", datetime.datetime.today()),
                ],
                order="name desc",
                limit=1,
            )
            if custom_currency_rate.inverse_company_rate != 0:
                ex_rate = custom_currency_rate.inverse_company_rate

        """custom_currency = env['res.currency'].search([('id', '=', record.currency_id.id),('active', '=', True)],limit=1)
    if custom_currency.rate > 0:
      ex_rate = custom_currency.rate"""

    done = 0
    select = 0
    total_amount = 0
    total_charge = 0
    total_duty = 0
    total_tax = 0
    val_charge = False
    val_duty = False
    val_tax = False
    total_charge_cd = 0
    total_duty_cd = 0
    total_tax_cd = 0
    val_charge_cd = False
    val_duty_cd = False
    val_tax_cd = False
    total_charge_ex = 0
    total_duty_ex = 0
    total_tax_ex = 0
    val_charge_ex = False
    val_duty_ex = False
    val_tax_ex = False
    total_charge_ex_cd = 0
    total_duty_ex_cd = 0
    total_tax_ex_cd = 0
    val_charge_ex_cd = False
    val_duty_ex_cd = False
    val_tax_ex_cd = False

    tot_charge_ids = []
    tot_duty_ids = []
    tot_tax_ids = []
    tot_final_ids = []

    tot_charge_ex_ids = []
    tot_duty_ex_ids = []
    tot_tax_ex_ids = []
    tot_final_ex_ids = []

    tot_charge_cd_ids = []
    tot_duty_cd_ids = []
    tot_tax_cd_ids = []
    tot_final_cd_ids = []

    tot_charge_ex_cd_ids = []
    tot_duty_ex_cd_ids = []
    tot_tax_ex_cd_ids = []
    tot_final_ex_cd_ids = []

    for po_line in record.invoice_line_ids:
        con_line_2 = env["consignment_line"].search(
            [
                (
                    "consignment_header_id",
                    "=",
                    record.consignment_no.id,
                ),
                ("accounting_purchase_id", "=", record.accounting_purchase_id.id),
                ("product_id", "=", po_line.product_id.id),
                ("invoice_qty", "=", po_line.quantity),
                ("purchase_line_id", "=", po_line.purchase_line_id.id),
            ],
            limit=1,
        )
        if con_line_2:
            select += 1
            total_amount += po_line.quantity * (
                po_line.price_subtotal / po_line.quantity
            )
            po_line.write({"quantity": con_line_2.invoice_qty})

            if con_line_2.valid_charge == True:
                total_charge += con_line_2.tot_charge
                # tot_charge_ids = con_line_2.tot_charge_ids
                if con_line_2.tot_charge_ids != []:
                    for ids in con_line_2.tot_charge_ids:
                        tot_charge_ids.append(ids.id)
                        tot_final_ids.append(ids.id)
            if con_line_2.valid_duty == True:
                total_duty += con_line_2.tot_duty
                # tot_duty_ids = con_line_2.tot_duty_ids
                if con_line_2.tot_duty_ids != []:
                    for ids in con_line_2.tot_duty_ids:
                        tot_duty_ids.append(ids.id)
                        tot_final_ids.append(ids.id)
            if con_line_2.valid_tax == True:
                total_tax += con_line_2.tot_tax
                # tot_tax_ids = con_line_2.tot_tax_ids
                if con_line_2.tot_tax_ids != []:
                    for ids in con_line_2.tot_tax_ids:
                        tot_tax_ids.append(ids.id)
                        tot_final_ids.append(ids.id)

            if con_line_2.valid_charge_cd == True:
                total_charge_cd += con_line_2.tot_charge_cd
                # tot_charge_cd_ids = con_line_2.tot_charge_cd_ids
                if con_line_2.tot_charge_cd_ids != []:
                    for ids in con_line_2.tot_charge_cd_ids:
                        tot_charge_cd_ids.append(ids.id)
                        tot_final_cd_ids.append(ids.id)
            if con_line_2.valid_duty_cd == True:
                total_duty_cd += con_line_2.tot_duty_cd
                # tot_duty_cd_ids = con_line_2.tot_duty_cd_ids
                if con_line_2.tot_duty_cd_ids != []:
                    for ids in con_line_2.tot_duty_cd_ids:
                        tot_duty_cd_ids.append(ids.id)
                        tot_final_cd_ids.append(ids.id)
            if con_line_2.valid_tax_cd == True:
                total_tax_cd += con_line_2.tot_tax_cd
                # tot_tax_cd_ids = con_line_2.tot_tax_cd_ids
# … 455 more lines
```
  </details>
- **IMP - Update Consignment - PI** (`action_imp_update_consignment_pi`, type `code`)
  - Function: Legacy version of IMP - Update Consignment - PI: validates the consignment against PO lines, then adds landed-cost charge/duty/tax lines and posts despatch/custom-clearance reversal entries using Imports Ledger Setup accounts.
  - Depends on: `account.move.currency_id` (account), `account.move.invoice_line_ids` (account), `account.move.partner_id` (account), `account.move.consignment_no`, `account.move.created_from_vendor_bill_1`<details><summary>+14 more</summary>`account.move.created_from_vendor_bill`, `account.move.accounting_purchase_id`, `account.move.update_consignment`, `model account.journal` (account), `model account.move.line` (account), `model account.move` (account), `model product.product` (product), `model res.company` (base), `model res.config.settings` (base), `model res.currency.rate` (base), `model res.currency` (base), `model consignment_header` (BugFix-Stock), `model consignment_line` (BugFix-Stock), `model imports_ledger_setup` (BugFix-Purchase)</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (575 lines)</summary>

```python
if record.id:
    company_id = env.context.get("allowed_company_ids", [env.user.company_id.id])[0]
    company = env["res.company"].browse(company_id)

    con_line = env["consignment_line"].search(
        [
            ("consignment_header_id", "=", record.consignment_no.id),
            ("accounting_purchase_id", "=", record.accounting_purchase_id.id),
        ],
        limit=1,
    )
    if not con_line:
        raise UserError(
            "The Selected Consignment No is not linked with the Current PO."
        )

    ex_rate = 1

    company_currency = env["res.config.settings"].search(
        [("currency_id", "=", record.currency_id.id)], limit=1
    )
    if company_currency:
        ex_rate = 1
    else:
        custom_currency = env["res.currency"].search(
            [("id", "=", record.currency_id.id), ("active", "=", True)], limit=1
        )
        if custom_currency:
            custom_currency_rate = env["res.currency.rate"].search(
                [
                    ("currency_id", "=", custom_currency.id),
                    ("name", "<=", datetime.datetime.today()),
                ],
                order="name desc",
                limit=1,
            )
            if custom_currency_rate.inverse_company_rate != 0:
                ex_rate = custom_currency_rate.inverse_company_rate

        """custom_currency = env['res.currency'].search([('id', '=', record.currency_id.id),('active', '=', True)],limit=1)
    if custom_currency.rate > 0:
      ex_rate = custom_currency.rate"""

    done = 0
    select = 0
    total_amount = 0
    total_charge = 0
    total_duty = 0
    total_tax = 0
    val_charge = False
    val_duty = False
    val_tax = False
    total_charge_cd = 0
    total_duty_cd = 0
    total_tax_cd = 0
    val_charge_cd = False
    val_duty_cd = False
    val_tax_cd = False
    total_charge_ex = 0
    total_duty_ex = 0
    total_tax_ex = 0
    val_charge_ex = False
    val_duty_ex = False
    val_tax_ex = False
    total_charge_ex_cd = 0
    total_duty_ex_cd = 0
    total_tax_ex_cd = 0
    val_charge_ex_cd = False
    val_duty_ex_cd = False
    val_tax_ex_cd = False

    tot_charge_ids = []
    tot_duty_ids = []
    tot_tax_ids = []
    tot_final_ids = []

    tot_charge_ex_ids = []
    tot_duty_ex_ids = []
    tot_tax_ex_ids = []
    tot_final_ex_ids = []

    tot_charge_cd_ids = []
    tot_duty_cd_ids = []
    tot_tax_cd_ids = []
    tot_final_cd_ids = []

    tot_charge_ex_cd_ids = []
    tot_duty_ex_cd_ids = []
    tot_tax_ex_cd_ids = []
    tot_final_ex_cd_ids = []

    for po_line in record.invoice_line_ids:
        con_line_2 = env["consignment_line"].search(
            [
                (
                    "consignment_header_id",
                    "=",
                    record.consignment_no.id,
                ),
                ("accounting_purchase_id", "=", record.accounting_purchase_id.id),
                ("product_id", "=", po_line.product_id.id),
                ("invoice_qty", "=", po_line.quantity),
                ("purchase_line_id", "=", po_line.purchase_line_id.id),
            ],
            limit=1,
        )
        if con_line_2:
            select += 1
            total_amount += po_line.quantity * (
                po_line.price_subtotal / po_line.quantity
            )
            po_line.write({"quantity": con_line_2.invoice_qty})

            if con_line_2.valid_charge == True:
                total_charge += con_line_2.tot_charge
                # tot_charge_ids = con_line_2.tot_charge_ids
                if con_line_2.tot_charge_ids != []:
                    for ids in con_line_2.tot_charge_ids:
                        tot_charge_ids.append(ids.id)
                        tot_final_ids.append(ids.id)
            if con_line_2.valid_duty == True:
                total_duty += con_line_2.tot_duty
                # tot_duty_ids = con_line_2.tot_duty_ids
                if con_line_2.tot_duty_ids != []:
                    for ids in con_line_2.tot_duty_ids:
                        tot_duty_ids.append(ids.id)
                        tot_final_ids.append(ids.id)
            if con_line_2.valid_tax == True:
                total_tax += con_line_2.tot_tax
                # tot_tax_ids = con_line_2.tot_tax_ids
                if con_line_2.tot_tax_ids != []:
                    for ids in con_line_2.tot_tax_ids:
                        tot_tax_ids.append(ids.id)
                        tot_final_ids.append(ids.id)

            if con_line_2.valid_charge_cd == True:
                total_charge_cd += con_line_2.tot_charge_cd
                # tot_charge_cd_ids = con_line_2.tot_charge_cd_ids
                if con_line_2.tot_charge_cd_ids != []:
                    for ids in con_line_2.tot_charge_cd_ids:
                        tot_charge_cd_ids.append(ids.id)
                        tot_final_cd_ids.append(ids.id)
            if con_line_2.valid_duty_cd == True:
                total_duty_cd += con_line_2.tot_duty_cd
                # tot_duty_cd_ids = con_line_2.tot_duty_cd_ids
                if con_line_2.tot_duty_cd_ids != []:
                    for ids in con_line_2.tot_duty_cd_ids:
                        tot_duty_cd_ids.append(ids.id)
                        tot_final_cd_ids.append(ids.id)
            if con_line_2.valid_tax_cd == True:
                total_tax_cd += con_line_2.tot_tax_cd
                # tot_tax_cd_ids = con_line_2.tot_tax_cd_ids
# … 455 more lines
```
  </details>
- **IMP - Update Consignment - Vendor Bill** (`action_imp_update_consignment_vendor_bill`, type `code`)
  - Function: On vendor bills: resets Update Consignment and Consignment No, links the purchase order matching Source Document, and sets LC No to that PO's latest-version Letter of Credit.
  - Depends on: `account.move.invoice_origin` (account), `account.move.consignment_no`, `account.move.lc_no`, `account.move.accounting_purchase_id`, `account.move.update_consignment`<details><summary>+3 more</summary>`model account.move` (account), `model purchase.order` (purchase), `model lc_header`</details>
  - Used by: `automation BugFix-Accounting.base_automation_64_imp_update_consignment_vendor_bill`
  <details><summary>code (10 lines)</summary>

```python
record["update_consignment"] = False
record["consignment_no"] = False

if record.invoice_origin:
    purchase = env["purchase.order"].search(
        [("name", "=", record.invoice_origin)], limit=1
    )
    if purchase:
        record["accounting_purchase_id"] = purchase.id
        lc = env["lc_header"].search(
            [("created_from_purchase_order", "=", purchase.id)],
            limit=1,
            order="version_no desc",
        )
        if lc:
            record["lc_no"] = lc.id
```
  </details>
- **IMP - Update Consignment - Vendor Bill** (`action_imp_update_consignment_vendor_bill_2`, type `code`)
  - Function: Legacy version: resets Update Consignment and Consignment No on the bill and links the purchase order matching Source Document (without setting the LC).
  - Depends on: `account.move.invoice_origin` (account), `account.move.consignment_no`, `account.move.accounting_purchase_id`, `account.move.update_consignment`, `model account.move` (account)<details><summary>+1 more</summary>`model purchase.order` (purchase)</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (7 lines)</summary>

```python
record["update_consignment"] = False
record["consignment_no"] = False

if record.invoice_origin:
    purchase = env["purchase.order"].search(
        [("name", "=", record.invoice_origin)], limit=1
    )
    if purchase:
        record["accounting_purchase_id"] = purchase.id
```
  </details>
- **IMP - Update LC Status to Paid** (`action_imp_update_lc_status_to_paid`, type `code`)
  - Function: When a bill linked to a Posted LC is posted, marks the LC as Paid (both status fields) and records the bill total as Paid Amount (LCY).
  - Depends on: `account.move.amount_total` (account), `account.move.state` (account), `account.move.lc_no`, `model account.move` (account), `model lc_header`
  - Used by: `automation BugFix-Accounting.base_automation_72_imp_update_lc_status_to_paid`
  <details><summary>code (5 lines)</summary>

```python
if record.state == "posted":
    if record.lc_no != False:
        lc_lines = env["lc_header"].search(
            [("id", "=", record.lc_no.id), ("status", "=", "Posted")],
            limit=1,
        )
        if lc_lines:
            lc_lines.write(
                {
                    "status": "Paid",
                    "selection_field_yo4qM": "Paid",
                    "paid_amount_lcy": record.amount_total,
                }
            )
```
  </details>
- **IMP - Vendor Bill Currency Rate** (`srv_imp_vendor_bill_currency_rate`, type `code`)
  - Function: Button that rewrites every journal line's debit/credit as the bill's manual Currency Rate times the foreign amount and sets Currency Rate Updated; errors if no rate is entered.
  - Depends on: `account.move.line_ids` (account), `account.move.currency_rate_updated`, `account.move.currency_rate`, `model account.move.line` (account), `model account.move` (account)
  - Used by: `view BugFix-Accounting.view_account_move_form_inherit_3`
  <details><summary>code (26 lines)</summary>

```python
if record.currency_rate > 0.00:
    tot_amount = 0

    # record.with_context(check_move_validity = False)

    for invoice_lines2 in record.line_ids:
        if invoice_lines2.credit == 0.00:
            invoice_lines2.with_context(check_move_validity=False).write(
                {
                    "debit": (
                        record.currency_rate
                        * abs(invoice_lines2.amount_currency)
                    )
                }
            )
        if invoice_lines2.debit == 0.00:
            invoice_lines2.with_context(check_move_validity=False).write(
                {
                    "credit": (
                        record.currency_rate
                        * abs(invoice_lines2.amount_currency)
                    )
                }
            )

    record["currency_rate_updated"] = True
else:
    raise UserError("Currency Rate must be defined!")

# record.with_context(check_move_validity = True).write({'line_ids':invoice_lines_cd})

"""  credit_line = self.env['account.move.line'].with_context(
            check_move_validity=False).create({
            'move_id': self.journal_entry.id,
            'account_id': self.product.revenue_account,
            'partner_id': self.container.partner.id,
            'name': 'Finish '+self.job_name,
            'credit': self.cost
         })"""
```
  </details>
- **IMP - Vendor Bill Currency Rate** (`action_imp_vendor_bill_currency_rate`, type `code`)
  - Function: Rewrites every journal line's debit/credit as the bill's manual Currency Rate times the foreign amount and sets Currency Rate Updated; errors if no rate is entered.
  - Depends on: `account.move.line_ids` (account), `account.move.currency_rate_updated`, `account.move.currency_rate`, `model account.move.line` (account), `model account.move` (account)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (25 lines)</summary>

```python
if record.currency_rate > 0.00:
    tot_amount = 0

    # record.with_context(check_move_validity = False)

    for invoice_lines2 in record.line_ids:
        if invoice_lines2.credit == 0.00:
            invoice_lines2.with_context(check_move_validity=False).write(
                {
                    "debit": (
                        record.currency_rate
                        * abs(invoice_lines2.amount_currency)
                    )
                }
            )
        if invoice_lines2.debit == 0.00:
            invoice_lines2.with_context(check_move_validity=False).write(
                {
                    "credit": (
                        record.currency_rate
                        * abs(invoice_lines2.amount_currency)
                    )
                }
            )

    record["currency_rate_updated"] = True
else:
    raise UserError("Currency Rate must be defined!")

# record.with_context(check_move_validity = True).write({'line_ids':invoice_lines_cd})

"""  credit_line = self.env['account.move.line'].with_context(
            check_move_validity=False).create({
            'move_id': self.journal_entry.id,
            'account_id': self.product.revenue_account,
            'partner_id': self.container.partner.id,
            'name': 'Finish '+self.job_name,
            'credit': self.cost
         })"""
```
  </details>
- **PR - Validate Cash Issued in NPO** (`action_pr_validate_cash_issued_in_npo`, type `code`)
  - Function: When an entry linked to a Cash Purchase (`cre`) is posted, sums posted 'Cash Issued' journal entries for that cash purchase and sets Payment Status to Paid if they cover the total.
  - Depends on: `account.move.amount_total` (account), `account.move.state` (account), `account.move.cre` (BugFix-Purchase), `model account.journal` (account), `model account.move` (account)<details><summary>+1 more</summary>`model res.company` (base)</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (16 lines)</summary>

```python
if record.state == "posted":
    company_id = env.context.get("allowed_company_ids", [env.user.company_id.id])[0]
    company = env["res.company"].browse(company_id)

    sum_total = 0

    if record.cre != False:
        journal = env["account.journal"].search(
            [("name", "=", "Cash Issued"), ("company_id", "=", company.id)], limit=1
        )
        if journal:
            cash_issued = env["account.move"].search(
                [
                    ("cre", "=", record.cre.id),
                    ("journal_id", "=", journal.id),
                    ("state", "=", "posted"),
                ]
            )
            if cash_issued:
                for total in cash_issued:
                    sum_total += total.amount_total

            if record.amount_total <= sum_total:
                record["payment_state"] = "paid"
```
  </details>
- **Project - Update Advance Payment Account - Vendor Bill** (`srv_update_advance_payment_account_vendor_bill`, type `code`)
  - Function: Button for Advance Payment invoices/bills: requires at least one line and the Advance Account (Project) setting, then switches the first income (customer) or expense (vendor) line to that account and sets Advance Acc Updated.
  - Depends on: `account.move.invoice_line_ids` (account), `account.move.move_type` (account), `account.move.advance_acc_updated`, `account.move.type`, `model account.move.line` (account)<details><summary>+2 more</summary>`model account.move` (account), `model advance_payment_acco`</details>
  - Used by: `view BugFix-Accounting.view_account_move_form_inherit_3`
  <details><summary>code (37 lines)</summary>

```python
if record.type == "Advance Payment":
    val = False
    for line in record.invoice_line_ids:
        val = True

    if val == False:
        raise UserError("You need to add a line before updating the advance account.")

    account = env["advance_payment_acco"].search([("id", "=", 1)], limit=1)
    if account:
        if account.advance_account_project == False:
            raise UserError(
                "Advance Account (Project) must be Specified in Accounting Configuration"
            )

        if record.move_type == "out_invoice":
            lines = env["account.move.line"].search(
                [
                    ("move_id", "=", record.id),
                    ("account_internal_group", "=", "income"),
                ],
                limit=1,
            )
            if lines:
                for line in lines:
                    line.write(
                        {"account_id": account.advance_account_project.id}
                    )
                    record.write({"advance_acc_updated": True})
        elif record.move_type == "in_invoice":
            lines = env["account.move.line"].search(
                [
                    ("move_id", "=", record.id),
                    ("account_internal_group", "=", "expense"),
                ],
                limit=1,
            )
            if lines:
                for line in lines:
                    line.write(
                        {"account_id": account.advance_account_project.id}
                    )
                    record.write({"advance_acc_updated": True})
        else:
            raise UserError("This feature is not supported.")
    else:
        raise UserError(
            "Advance Payment Accounts have not been setup in Accounting Configuration"
        )
```
  </details>
- **Project - Update Advance Payment Account - Vendor Bill** (`action_project_update_advance_payment_account_vendor_bill`, type `code`)
  - Function: For Advance Payment invoices/bills: requires a line and the Advance Account (Project) setting, then moves the first income (customer) or expense (vendor) line to that account and sets Advance Acc Updated.
  - Depends on: `account.move.invoice_line_ids` (account), `account.move.move_type` (account), `account.move.advance_acc_updated`, `account.move.type`, `model account.move.line` (account)<details><summary>+2 more</summary>`model account.move` (account), `model advance_payment_acco`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (30 lines)</summary>

```python
if record.type == "Advance Payment":
    val = False
    for line in record.invoice_line_ids:
        val = True

    if val == False:
        raise UserError("You need to add a line before updating the advance account.")

    account = env["advance_payment_acco"].search([("id", "=", 1)], limit=1)
    if account:
        if account.advance_account_project == False:
            raise UserError(
                "Advance Account (Project) must be Specified in Accounting Configuration"
            )

        if record.move_type == "out_invoice":
            lines = env["account.move.line"].search(
                [
                    ("move_id", "=", record.id),
                    ("account_internal_group", "=", "income"),
                ],
                limit=1,
            )
            if lines:
                for line in lines:
                    line.write(
                        {"account_id": account.advance_account_project.id}
                    )
                    record.write({"advance_acc_updated": True})
        elif record.move_type == "in_invoice":
            lines = env["account.move.line"].search(
                [
                    ("move_id", "=", record.id),
                    ("account_internal_group", "=", "expense"),
                ],
                limit=1,
            )
            if lines:
                for line in lines:
                    line.write(
                        {"account_id": account.advance_account_project.id}
                    )
                    record.write({"advance_acc_updated": True})
        else:
            raise UserError("This feature is not supported.")
    else:
        raise UserError(
            "Advance Payment Accounts have not been setup in Accounting Configuration"
        )
```
  </details>
- **Project - Update Project No for Manual Transactions** (`action_account_move_project_update_project_no_for_manual_transactions`, type `code`)
  - Function: Copies the entry's Project No into Project No Bill, Issue or Settle depending on Journal Type (Bill/Payment/Settlement), clearing the other two; clears all three for other types.
  - Depends on: `account.move.journal_type`, `account.move.project_no_bill`, `account.move.project_no_issue`, `account.move.project_no_settle`, `account.move.project_no`<details><summary>+1 more</summary>`model account.move` (account)</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (9 lines)</summary>

```python
if record.project_no != False:
    if record.journal_type == "Bill":
        record.write(
            {
                "project_no_bill": record.project_no.id,
                "project_no_issue": False,
                "project_no_settle": False,
            }
        )
    elif record.journal_type == "Payment":
        record.write(
            {
                "project_no_bill": False,
                "project_no_issue": record.project_no.id,
                "project_no_settle": False,
            }
        )
    elif record.journal_type == "Settlement":
        record.write(
            {
                "project_no_bill": False,
                "project_no_issue": False,
                "project_no_settle": record.project_no.id,
            }
        )
    else:
        record.write(
            {
                "project_no_bill": False,
                "project_no_issue": False,
                "project_no_settle": False,
            }
        )
```
  </details>
- **RR - RUG Account Update in SI** (`action_rr_rug_account_update_in_si`, type `code`)
  - Function: For RUG-confirmed invoices, reassigns the journal's default-account lines to the company's RUG account from Repair Accounts (error if not set) and marks RUG Account Updated.
  - Depends on: `account.move.journal_id` (account), `account.move.partner_id` (account), `account.move.rug_acc_updated`, `account.move.rug_confirmed`, `model account.move.line` (account)<details><summary>+3 more</summary>`model account.move` (account), `model res.company` (base), `model repair_accounts` (Fix-repair)</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (29 lines)</summary>

```python
if record.rug_confirmed == True:
    company_id = env.context.get("allowed_company_ids", [env.user.company_id.id])[0]

    company = env["res.company"].browse(company_id)

    rug_account = env["repair_accounts"].search(
        [("accounting_company_id", "=", company.id)], limit=1
    )

    if rug_account:
        if rug_account.rug_account == False:
            raise UserError("RUG Account must be Specified in Repair Accounts")

    lines = env["account.move.line"].search(
        [
            ("move_id", "=", record.id),
            ("account_id", "=", record.journal_id.default_account_id.id),
        ]
    )

    # lines = env['account.move.line'].search([('move_id', '=', record.id),('account_id', '=', record.partner_id.property_account_receivable_id.id)])

    for line in lines:
        line.write({"account_id": rug_account.rug_account.id})

    record.write({"rug_acc_updated": True})
```
  </details>
- **RR - RUG Account Update in SI** (`srv_rug_account_update_in_si`, type `code`)
  - Function: Button on the invoice form: for RUG-confirmed invoices, moves the journal's default-account lines to the company's RUG account from Repair Accounts (error if missing) and sets RUG Account Updated.
  - Depends on: `account.move.journal_id` (account), `account.move.rug_acc_updated`, `account.move.rug_confirmed`, `model account.move.line` (account), `model account.move` (account)<details><summary>+2 more</summary>`model res.company` (base), `model repair_accounts` (Fix-repair)</details>
  - Used by: `view BugFix-Accounting.view_account_move_form_inherit_3`
  <details><summary>code (18 lines)</summary>

```python
if record.rug_confirmed == True:
    company_id = env.context.get("allowed_company_ids", [env.user.company_id.id])[0]
    company = env["res.company"].browse(company_id)

    rug_account = env["repair_accounts"].search(
        [("accounting_company_id", "=", company.id)], limit=1
    )
    if rug_account:
        if rug_account.rug_account == False:
            raise UserError("RUG Account must be Specified in Repair Accounts")

    lines = env["account.move.line"].search(
        [
            ("move_id", "=", record.id),
            ("account_id", "=", record.journal_id.default_account_id.id),
        ]
    )
    for line in lines:
        line.write({"account_id": rug_account.rug_account.id})

    record.write({"rug_acc_updated": True})
```
  </details>
- **RR - Validate RUG in Customer Invoice** (`action_account_move_rr_validate_rug_in_customer_invoice`, type `code`)
  - Function: For posted invoices with RUG confirmed and RUG account updated, sets Payment Status to In Payment if the linked sales order is Done, otherwise raises 'Incomplete sales order'.
  - Depends on: `account.move.state` (account), `account.move.rug_acc_updated`, `account.move.rug_confirmed`, `account.move.sale_id`, `model account.move` (account)<details><summary>+1 more</summary>`model sale.order` (sale)</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (8 lines)</summary>

```python
if record.rug_confirmed == True:
    if record.rug_acc_updated == True:
        if record.state == "posted":
            so = env["sale.order"].search(
                [("id", "=", record.sale_id.id), ("state", "=", "done")],
                limit=1,
            )
            if so:
                record["payment_state"] = "in_payment"
            else:
                raise UserError("Incomplete sales order. Process terminatedddd.")
```
  </details>
- **SLS - Credit Note Approval** (`srv_sls_credit_note_approved_flag`, type `object_write`)
  - Function: Sets Credit Note Approved to 'Yes' on the journal entry; step of the Credit Note Approval - Main action.
  - Depends on: `account.move.credit_note_approved`, `model account.move` (account)
  - Used by: `server action BugFix-Accounting.srv_sls_credit_note_approval_main`
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **SLS - Credit Note Approval** (`action_sls_credit_note_approval`, type `object_write`)
  - Function: Sets Credit Note Approved to 'Yes' on the journal entry; step of the legacy Credit Note Approval - Main action (1495).
  - Depends on: `account.move.credit_note_approved`, `model account.move` (account)
  - Used by: `server action BugFix-Accounting.action_sls_credit_note_approval_main`
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **SLS - Credit Note Approval - Confirm** (`srv_sls_credit_note_confirm_activity`, type `next_activity`)
  - Function: Schedules a To-Do activity 'Credit Note Approval - Confirm' due today for the entry's responsible user; step of Credit Note Approval - Main.
  - Depends on: `model account.move` (account)
  - Used by: `server action BugFix-Accounting.srv_sls_credit_note_approval_main`
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **SLS - Credit Note Approval - Confirm** (`action_sls_credit_note_approval_confirm`, type `next_activity`)
  - Function: Schedules a To-Do activity 'Credit Note Approval - Confirm' for the responsible user; step of the legacy Credit Note Approval - Main action (1495).
  - Depends on: `model account.move` (account)
  - Used by: `server action BugFix-Accounting.action_sls_credit_note_approval_main`
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **SLS - Credit Note Approval - Main** (`srv_sls_credit_note_approval_main`, type `multi`)
  - Function: Credit note approval action (button, also tied to an approval rule): sets Credit Note Approved to Yes and schedules the 'Credit Note Approval - Confirm' activity.
  - Depends on: `model account.move` (account), `server action BugFix-Accounting.srv_sls_credit_note_approved_flag`, `server action BugFix-Accounting.srv_sls_credit_note_confirm_activity`
  - Used by: `approval rule BugFix-Accounting.approval_rule_ar_final_journal_entry_sls_credit_note_approval_sales_credit_note`, `view BugFix-Accounting.view_account_move_form_inherit_3`
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **SLS - Credit Note Approval - Main** (`action_sls_credit_note_approval_main`, type `multi`)
  - Function: Legacy multi-step credit note approval action: sets Credit Note Approved to Yes and schedules the Confirm activity; not referenced by any view or rule (superseded by srv_sls_credit_note_approval_main).
  - Depends on: `model account.move` (account), `server action BugFix-Accounting.action_sls_credit_note_approval`, `server action BugFix-Accounting.action_sls_credit_note_approval_confirm`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **SLS - Payment Reconciliation - Automate** (`action_sls_payment_reconciliation_automate`, type `code`)
  - Function: For invoices with a Source Document, finds the sales order's payments and force-writes them as reconciled to this invoice and links the payment; the remaining work-center costing code is commented out.
  - Depends on: `account.move.invoice_origin` (account), `account.move.stock_move_id` (stock_account), `account.move.accounting_purchase_id`, `model account.move` (account), `model account.payment` (account)<details><summary>+4 more</summary>`model mrp.production` (mrp), `model sale.order` (sale), `model stock.move` (stock), `model work_center_costing` (BugFix-Studio-Misc)</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (94 lines)</summary>

```python
if record.invoice_origin:
    ids = [record.id]
    sale = env["sale.order"].search([("name", "=", record.invoice_origin)], limit=1)
    if sale:
        find_payment = env["account.payment"].search(
            [("sales_order", "=", sale.id)]
        )
        if find_payment:
            find_payment.write(
                {
                    "reconciled_invoice_ids": [(6, False, ids)],
                    "reconciled_invoices_count": 1,
                    "is_reconciled": True,
                }
            )
            record["payment_id"] = find_payment.id
            # for reconcil_payment in find_payment:
            #  reconcil_payment.update({'reconciled_invoice_ids':[(6, False, ids)],'reconciled_invoices_count':1})

        ##record['accounting_purchase_id'] = purchase.id

"""    
  if find_bom:
    if record.stock_move_id:
      stock_move = env['stock.move'].search([('id', '=', record.stock_move_id.id), ('product_tmpl_id', '=', record.product_tmpl_id.id)],limit=1)
      if stock_move:
        prod_order = env['mrp.production'].search([('id', '=', stock_move.production_id.id)],limit=1)
        if prod_order:
          ##########################JC
          work_center_costing = env['work_center_costing'].search([('id', '=', 1)], limit=1)
          if work_center_costing:
            if prod_order.prod_bom_total_actual_labour_cost > 0.0000:
              cost_lines=[]
              ids =[work_center_costing.labour_analytic_tag.id]
              cost_lines.append([0,0,{
                'account_id':work_center_costing.labour_cost_debit_account.id,
                'name':(prod_order.name + ' - ' + 'Labour Cost'),
                'analytic_tag_ids':[(6, False, ids)],
                'debit':prod_order.prod_bom_total_actual_labour_cost}])

              cost_lines.append([0,0,{
                'account_id':work_center_costing.labour_cost_credit_account.id,
                'name':(prod_order.name + ' - ' + 'Labour Cost'),
                'analytic_tag_ids':[(6, False, ids)],
                'credit':prod_order.prod_bom_total_actual_labour_cost}])	

              labour_cost_entry = env['account.move'].create({'date':datetime.datetime.today(),'ref':(prod_order.name + ' - ' + 'Labour Cost'),'journal_id':6,'move_type':'entry','line_ids':cost_lines})
              #######
              update_labour_cost_entry = env['account.move'].search([('id', '=', labour_cost_entry.id)],limit=1)
              if update_labour_cost_entry:
                update_labour_cost_entry.write({'state':'posted'})
              #######
          ########        
          if prod_order.prod_bom_total_actual_overhead_cost > 0.0000:
            cost_lines2=[]
            ids2 =[work_center_costing.overhead_analytic_tag.id]
            cost_lines2.append([0,0,{
              'account_id':work_center_costing.overhead_cost_debit_account.id,
              'name':(prod_order.name + ' - ' + 'Overhead Cost'),
              'analytic_tag_ids':[(6, False, ids2)],
              'debit':prod_order.prod_bom_total_actual_overhead_cost}])

            cost_lines2.append([0,0,{
              'account_id':work_center_costing.overhead_cost_credit_account.id,
              'name':(prod_order.name + ' - ' + 'Overhead Cost'),
              'analytic_tag_ids':[(6, False, ids2)],
              'credit':prod_order.prod_bom_total_actual_overhead_cost}])	

            overhead_cost_entry = env['account.move'].create({'date':datetime.datetime.today(),'ref':(prod_order.name + ' - ' + 'Overhead Cost'),'journal_id':6,'move_type':'entry','line_ids':cost_lines2})
            #######
            update_overhead_cost_entry = env['account.move'].search([('id', '=', overhead_cost_entry.id)],limit=1)
            if update_overhead_cost_entry:
              update_overhead_cost_entry.write({'state':'posted'})
            #######
          ########
          if prod_order.total_actual_general_cost > 0.0000:
            cost_lines3=[]
            ids3 =[work_center_costing.general_analytic_tag.id]
            cost_lines3.append([0,0,{
              'account_id':work_center_costing.general_cost_debit_account.id,
              'name':(prod_order.name + ' - ' + 'General Cost'),
              'analytic_tag_ids':[(6, False, ids3)],
              'debit':prod_order.total_actual_general_cost}])

            cost_lines3.append([0,0,{
              'account_id':work_center_costing.general_cost_credit_account.id,
              'name':(prod_order.name + ' - ' + 'General Cost'),
              'analytic_tag_ids':[(6, False, ids3)],
              'credit':prod_order.total_actual_general_cost}])	

            general_cost_entry = env['account.move'].create({'date':datetime.datetime.today(),'ref':(prod_order.name + ' - ' + 'General Cost'),'journal_id':6,'move_type':'entry','line_ids':cost_lines3})
            #######
            update_general_cost_entry = env['account.move'].search([('id', '=', general_cost_entry.id)],limit=1)
            if update_general_cost_entry:
              update_general_cost_entry.write({'state':'posted'})
            #######
          ##########################JC

"""
```
  </details>
- **SLS - Request Credit Note Approval** (`srv_sls_request_credit_note_approval`, type `multi`)
  - Function: Form button/action that requests credit note approval: runs the Notify User activity step and sets Credit Note Request Sent to Yes.
  - Depends on: `model account.move` (account), `server action BugFix-Accounting.srv_sls_credit_note_notify_tharaka`, `server action BugFix-Accounting.srv_sls_credit_note_request_sent_flag`
  - Used by: `view BugFix-Accounting.view_account_move_form_inherit_3`
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **SLS - Request Credit Note Approval** (`action_sls_request_credit_note_approval`, type `multi`)
  - Function: Legacy multi-step action that requests credit note approval: schedules the 'Approve Credit Note' activity and sets Credit Note Request Sent to Yes (steps 1491 and 1489); not referenced by any view.
  - Depends on: `model account.move` (account), `server action BugFix-Accounting.action_sls_request_credit_note_approval_sent`, `server action BugFix-Accounting.action_sls_request_credit_note_approval_notify_user`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **SLS - Request Credit Note Approval - Notify User** (`srv_sls_credit_note_notify_tharaka`, type `next_activity`)
  - Function: Schedules a To-Do activity 'Approve Credit Note' due today for a specific user on the journal entry; step of the Request Credit Note Approval action.
  - Depends on: `model account.move` (account)
  - Used by: `server action BugFix-Accounting.srv_sls_request_credit_note_approval`
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **SLS - Request Credit Note Approval - Notify User** (`action_sls_request_credit_note_approval_notify_user`, type `next_activity`)
  - Function: Schedules a To-Do activity 'Approve Credit Note' for a specific user; step of the legacy Request Credit Note Approval action (1493). No user is set in the port.
  - Depends on: `model account.move` (account)
  - Used by: `server action BugFix-Accounting.action_sls_request_credit_note_approval`
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **SLS - Request Credit Note Approval Sent** (`srv_sls_credit_note_request_sent_flag`, type `object_write`)
  - Function: Sets Credit Note Request Sent to 'Yes' on the journal entry; step of the Request Credit Note Approval action.
  - Depends on: `account.move.credit_note_request_sent`, `model account.move` (account)
  - Used by: `server action BugFix-Accounting.srv_sls_request_credit_note_approval`
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **SLS - Request Credit Note Approval Sent** (`action_sls_request_credit_note_approval_sent`, type `object_write`)
  - Function: Sets Credit Note Request Sent to 'Yes' on the journal entry; step of the legacy Request Credit Note Approval action (1493).
  - Depends on: `account.move.credit_note_request_sent`, `model account.move` (account)
  - Used by: `server action BugFix-Accounting.action_sls_request_credit_note_approval`
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **SLS - Send Bank Guarantee Notification in Customer Invoice** (`srv_sls_send_bank_guarantee_notification`, type `code`)
  - Function: Button on customer invoices of non-General customers without mandatory guarantee: posts a chatter warning if the bank guarantee is expired or below credit plus invoice total, and sets BG Sent.
  - Depends on: `account.move.amount_total` (account), `account.move.move_type` (account), `account.move.partner_id` (account), `account.move.bg_sent`, `account.move.sale_id`<details><summary>+1 more</summary>`model account.move` (account)</details>
  - Used by: `view BugFix-Accounting.view_account_move_form_inherit_3`
  <details><summary>code (12 lines)</summary>

```python
if record.partner_id.customer_rank > 0:
    if record.move_type == "out_invoice":
        if record.partner_id.customer_group.group_type != "General":
            if record.partner_id.mandatory_bank_guarantee == False:
                if (
                    record.partner_id.expiry_date
                    and record.partner_id.expiry_date < datetime.date.today()
                ):
                    records.message_post(
                        body="Customer's bank guarantee is expired."
                        + "\n"
                        + "Bank guaranty expiry date: "
                        + str(record.partner_id.expiry_date)
                    )
                    record["bg_sent"] = True
                else:
                    if record.partner_id.bank_guarantee_amount < (
                        record.partner_id.credit + record.amount_total
                    ):
                        records.message_post(
                            body="The credit limit is higher than the bank guarantee amount."
                            + "\n"
                            + "Customer: "
                            + str(record.partner_id.name)
                            + "\n"
                            + " Sales Order: "
                            + str(record.sale_id.name)
                            + "\n"
                            + "Bank guarantee amount: "
                            + str(record.partner_id.bank_guarantee_amount)
                            + "\n"
                            + "Current Balance: "
                            + str(record.partner_id.credit)
                            + "\n"
                            + "This Sale: "
                            + str(record.amount_total)
                            + "\n"
                            + "New balance: "
                            + str(record.partner_id.credit + record.amount_total)
                        )
                        record["bg_sent"] = True
```
  </details>
- **SLS - Send Bank Guarantee Notification in Customer Invoice** (`action_sls_send_bank_guarantee_notification_in_customer_invoice`, type `code`)
  - Function: On customer invoices of non-General customers without mandatory guarantee: posts a chatter warning if the bank guarantee is expired or below credit plus invoice total, and sets BG Sent.
  - Depends on: `account.move.amount_total` (account), `account.move.move_type` (account), `account.move.partner_id` (account), `account.move.bg_sent`, `account.move.sale_id`<details><summary>+1 more</summary>`model account.move` (account)</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (11 lines)</summary>

```python
if record.partner_id.customer_rank > 0:
    if record.move_type == "out_invoice":
        if record.partner_id.customer_group.group_type != "General":
            if record.partner_id.mandatory_bank_guarantee == False:
                if (
                    record.partner_id.expiry_date
                    and record.partner_id.expiry_date < datetime.date.today()
                ):
                    records.message_post(
                        body="Customer's bank guarantee is expired."
                        + "\n"
                        + "Bank guaranty expiry date: "
                        + str(record.partner_id.expiry_date)
                    )
                    record["bg_sent"] = True
                else:
                    if record.partner_id.bank_guarantee_amount < (
                        record.partner_id.credit + record.amount_total
                    ):
                        records.message_post(
                            body="The credit limit is higher than the bank guarantee amount."
                            + "\n"
                            + "Customer: "
                            + str(record.partner_id.name)
                            + "\n"
                            + " Sales Order: "
                            + str(record.sale_id.name)
                            + "\n"
                            + "Bank guarantee amount: "
                            + str(record.partner_id.bank_guarantee_amount)
                            + "\n"
                            + "Current Balance: "
                            + str(record.partner_id.credit)
                            + "\n"
                            + "This Sale: "
                            + str(record.amount_total)
                            + "\n"
                            + "New balance: "
                            + str(record.partner_id.credit + record.amount_total)
                        )
                        record["bg_sent"] = True
```
  </details>
- **SLS - Validate Bank Guarantee in Customer Invoice** (`action_account_move_sls_validate_bank_guarantee_in_customer_invoice`, type `code`)
  - Function: On posted customer invoices of non-General customers: if bank guarantee is mandatory, blocks when expired or below credit plus invoice total; otherwise posts a chatter warning for the same conditions.
  - Depends on: `account.move.amount_total` (account), `account.move.move_type` (account), `account.move.partner_id` (account), `account.move.state` (account), `account.move.sale_id`<details><summary>+1 more</summary>`model account.move` (account)</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (22 lines)</summary>

```python
if record.partner_id.customer_rank > 0:
    if record.state == "posted":
        if record.move_type == "out_invoice":
            if (
                record.partner_id.customer_group.group_type
                != "General"
            ):
                if record.partner_id.mandatory_bank_guarantee == True:
                    if (
                        record.partner_id.expiry_date
                        and record.partner_id.expiry_date
                        < datetime.date.today()
                    ):
                        # raise UserError("Customer's bank guarantee is expired.")
                        raise UserError(
                            "Customer's bank guarantee is expired."
                            + "\n"
                            + "Bank guaranty expiry date: "
                            + str(record.partner_id.expiry_date)
                        )
                    else:
                        # if record.partner_id.mandatory_bank_guarantee < (record.partner_id.credit + record.amount_total):
                        if record.partner_id.bank_guarantee_amount < (
                            record.partner_id.credit + record.amount_total
                        ):
                            # raise UserError("Customer's balance exceeds the bank guarantee amount." + "\n" + "Bank guarantee limit: " + "\n" + str(record.partner_id.mandatory_bank_guarantee) + "\n" + "New balance: " + "\n" + str((record.partner_id.credit + record.amount_total)))
                            # raise UserError("Customer's balance exceeds the bank guarantee amount." + "\n" + "Bank guarantee amount: " + str(record.partner_id.bank_guarantee_amount) + "\n" + "Current Balance: " + str(record.partner_id.credit) + '\n' + "This Sale: " + str(record.amount_total) + "\n" + "New balance: " + str(record.partner_id.credit + record.amount_total))
                            raise UserError(
                                "The credit limit is higher than the bank guarantee amount."
                                + "\n"
                                + "Customer: "
                                + record.partner_id.name
                                + "\n"
                                + " Sales Order: "
                                + record.sale_id.name
                                + "\n"
                                + "Bank guarantee amount: "
                                + str(record.partner_id.bank_guarantee_amount)
                                + "\n"
                                + "Current Balance: "
                                + str(record.partner_id.credit)
                                + "\n"
                                + "This Sale: "
                                + str(record.amount_total)
                                + "\n"
                                + "New balance: "
                                + str(record.partner_id.credit + record.amount_total)
                            )
                else:
                    if (
                        record.partner_id.expiry_date
                        and record.partner_id.expiry_date
                        < datetime.date.today()
                    ):
                        records.message_post(
                            body="Customer's bank guarantee is expired."
                            + "\n"
                            + "Bank guaranty expiry date: "
                            + str(record.partner_id.expiry_date)
                        )
                    else:
                        if record.partner_id.bank_guarantee_amount < (
                            record.partner_id.credit + record.amount_total
                        ):
                            # records.message_post(body="Customer's balance exceeds the bank guarantee amount." + "\n" + "Bank guarantee limit: " + "\n" + str(record.partner_id.mandatory_bank_guarantee) + "\n" + "New balance: " + "\n" + str((record.partner_id.credit + record.amount_total)))
                            # records.message_post(body="Customer's balance exceeds the bank guarantee amount." + "\n" + "Bank guarantee amount: " + str(record.partner_id.bank_guarantee_amount) + "\n" + "Current Balance: " + str(record.partner_id.credit) + '\n' + "This Sale: " + str(record.amount_total) + "\n" + "New balance: " + str(record.partner_id.credit + record.amount_total))
                            records.message_post(
                                body="The credit limit is higher than the bank guarantee amount."
                                + "\n"
                                + "Customer: "
                                + str(record.partner_id.name)
                                + "\n"
                                + " Sales Order: "
                                + str(record.sale_id.name)
                                + "\n"
                                + "Bank guarantee amount: "
                                + str(record.partner_id.bank_guarantee_amount)
                                + "\n"
                                + "Current Balance: "
                                + str(record.partner_id.credit)
                                + "\n"
                                + "This Sale: "
                                + str(record.amount_total)
                                + "\n"
                                + "New balance: "
                                + str(record.partner_id.credit + record.amount_total)
                            )
```
  </details>
- **SLS - Validate Payment in Customer Invoice** (`action_account_move_sls_validate_payment_in_customer_invoice`, type `code`)
  - Function: On posted invoices from Done cash sales orders without temporary credit, blocks if posted payments are less than the invoice total, then sets Payment Status to In Payment.
  - Depends on: `account.move.amount_total` (account), `account.move.state` (account), `account.move.order_payment_method`, `account.move.sale_id`, `model account.move` (account)<details><summary>+2 more</summary>`model account.payment` (account), `model sale.order` (sale)</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (14 lines)</summary>

```python
if record.state == "posted":
    so = env["sale.order"].search(
        [
            ("id", "=", record.sale_id.id),
            ("state", "=", "done"),
            ("order_payment_method", "=", "Cash"),
            ("grant_temporary_credit", "=", False),
        ],
        limit=1,
    )
    if so:
        sum_total = 0
        payment = env["account.payment"].search(
            [
                ("sales_order", "=", record.sale_id.id),
                ("state", "=", "posted"),
            ]
        )
        if payment:
            for total in payment:
                sum_total += total.amount

        if record.amount_total > sum_total:
            # raise UserError('The Payment Against the Cash Sales Order must be equal to the total invoice amount.')
            raise UserError(
                "The Payment Against the Cash Sales Order must be equal to the total invoice amount."
                + "\n"
                + "\n"
                + "This sale: "
                + str(record.amount_total)
                + "\n"
                + "Total payments: "
                + str(sum_total)
                + "\n"
                + "Payment due: "
                + str(record.amount_total - sum_total)
            )

        record["payment_state"] = "in_payment"
```
  </details>
- **SLS - Validate Payment in Customer Invoice** (`action_sls_validate_payment_in_customer_invoice`, type `code`)
  - Function: Run by the automation on posted invoices from Done cash sales orders without temporary credit: blocks if posted SO payments are below the invoice total, otherwise sets Payment Status to In Payment.
  - Depends on: `account.move.amount_total` (account), `account.move.state` (account), `account.move.order_payment_method`, `account.move.sale_id`, `model account.move` (account)<details><summary>+2 more</summary>`model account.payment` (account), `model sale.order` (sale)</details>
  - Used by: `automation BugFix-Accounting.automation_sls_validate_payment_in_customer_invoice`
  <details><summary>code (15 lines)</summary>

```python
if record.state == "posted":
    so = env["sale.order"].search(
        [
            ("id", "=", record.sale_id.id),
            ("state", "=", "done"),
            ("order_payment_method", "=", "Cash"),
            ("grant_temporary_credit", "=", False),
        ],
        limit=1,
    )
    if so:
        sum_total = 0
        payment = env["account.payment"].search(
            [
                ("sales_order", "=", record.sale_id.id),
                ("state", "=", "posted"),
            ]
        )
        if payment:
            for total in payment:
                sum_total += total.amount

        if record.amount_total > sum_total:
            # raise UserError('The Payment Against the Cash Sales Order must be equal to the total invoice amount.')
            raise UserError(
                "The Payment Against the Cash Sales Order must be equal to the total invoice amount."
                + "\n"
                + "\n"
                + "This sale: "
                + str(record.amount_total)
                + "\n"
                + "Total payments: "
                + str(sum_total)
                + "\n"
                + "Payment due: "
                + str(record.amount_total - sum_total)
            )

        record["payment_state"] = "in_payment"
```
  </details>
- **SLS - View Bank Guarantee Validation in Customer Invoice** (`srv_sls_view_bank_guarantee_validation`, type `code`)
  - Function: Button on customer invoices of non-General customers with mandatory guarantee: raises an error if the bank guarantee is expired or insufficient for credit plus invoice total.
  - Depends on: `account.move.amount_total` (account), `account.move.move_type` (account), `account.move.partner_id` (account), `account.move.sale_id`, `model account.move` (account)
  - Used by: `view BugFix-Accounting.view_account_move_form_inherit_3`
  <details><summary>code (10 lines)</summary>

```python
if record.partner_id.customer_rank > 0:
    if record.move_type == "out_invoice":
        if record.partner_id.customer_group.group_type != "General":
            if record.partner_id.mandatory_bank_guarantee == True:
                if (
                    record.partner_id.expiry_date
                    and record.partner_id.expiry_date < datetime.date.today()
                ):
                    raise UserError(
                        "Customer's bank guarantee is expired."
                        + "\n"
                        + "Bank guaranty expiry date: "
                        + str(record.partner_id.expiry_date)
                    )
                else:
                    if record.partner_id.bank_guarantee_amount < (
                        record.partner_id.credit + record.amount_total
                    ):
                        raise UserError(
                            "Insufficient bank guarantee."
                            + "\n"
                            + "Customer: "
                            + record.partner_id.name
                            + "\n"
                            + "Sales Order: "
                            + record.sale_id.name
                            + "\n"
                            + "Bank guarantee amount: "
                            + str(record.partner_id.bank_guarantee_amount)
                            + "\n"
                            + "Current Balance: "
                            + str(record.partner_id.credit)
                            + "\n"
                            + "This Sale: "
                            + str(record.amount_total)
                            + "\n"
                            + "New balance: "
                            + str(record.partner_id.credit + record.amount_total)
                        )
```
  </details>
- **SLS - View Bank Guarantee Validation in Customer Invoice** (`action_sls_view_bank_guarantee_validation_in_customer_invoice`, type `code`)
  - Function: On customer invoices of non-General customers with mandatory guarantee: raises an error if the bank guarantee is expired or insufficient for credit plus invoice total.
  - Depends on: `account.move.amount_total` (account), `account.move.move_type` (account), `account.move.partner_id` (account), `account.move.sale_id`, `model account.move` (account)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (10 lines)</summary>

```python
if record.partner_id.customer_rank > 0:
    if record.move_type == "out_invoice":
        if record.partner_id.customer_group.group_type != "General":
            if record.partner_id.mandatory_bank_guarantee == True:
                if (
                    record.partner_id.expiry_date
                    and record.partner_id.expiry_date < datetime.date.today()
                ):
                    raise UserError(
                        "Customer's bank guarantee is expired."
                        + "\n"
                        + "Bank guaranty expiry date: "
                        + str(record.partner_id.expiry_date)
                    )

                else:
                    if record.partner_id.bank_guarantee_amount < (
                        record.partner_id.credit + record.amount_total
                    ):
                        raise UserError(
                            "Insufficient bank guarantee."
                            + "\n"
                            + "Customer: "
                            + record.partner_id.name
                            + "\n"
                            + "Sales Order: "
                            + record.sale_id.name
                            + "\n"
                            + "Bank guarantee amount: "
                            + str(record.partner_id.bank_guarantee_amount)
                            + "\n"
                            + "Current Balance: "
                            + str(record.partner_id.credit)
                            + "\n"
                            + "This Sale: "
                            + str(record.amount_total)
                            + "\n"
                            + "New balance: "
                            + str(record.partner_id.credit + record.amount_total)
                        )
```
  </details>
- **SLS - View Credit Limit Validation in Customer Invoice** (`srv_sls_view_credit_limit_validation`, type `code`)
  - Function: Button on customer invoices with Credit payment method: raises an error showing limit, receivable and excess when customer credit plus this invoice exceeds the credit limit.
  - Depends on: `account.move.amount_total` (account), `account.move.partner_id` (account), `account.move.order_payment_method`, `model account.move` (account)
  - Used by: `view BugFix-Accounting.view_account_move_form_inherit_3`
  <details><summary>code (12 lines)</summary>

```python
if record.partner_id.customer_rank > 0:
    if record.partner_id.id:
        if record.order_payment_method == "Credit":
            if (
                record.partner_id.credit + record.amount_total
            ) > record.partner_id.credit_limit:
                raise UserError(
                    "Customer's credit limit is exceeded."
                    + "\n"
                    + "Customer credit limit: "
                    + str(record.partner_id.credit_limit)
                    + "\n"
                    + "Cust. Total Receivable: "
                    + str(record.partner_id.credit)
                    + "\n"
                    + "Current Tot. Amount: "
                    + str(record.amount_total)
                    + "\n"
                    + "Over Credit Amount: "
                    + str(
                        (record.partner_id.credit + record.amount_total)
                        - record.partner_id.credit_limit
                    )
                )
```
  </details>
- **SLS - View Credit Limit Validation in Customer Invoice** (`action_sls_view_credit_limit_validation_in_customer_invoice`, type `code`)
  - Function: On customer invoices with Credit payment method: raises an error with limit details when customer credit plus this invoice exceeds the credit limit.
  - Depends on: `account.move.amount_total` (account), `account.move.partner_id` (account), `account.move.order_payment_method`, `model account.move` (account)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (5 lines)</summary>

```python
if record.partner_id.customer_rank > 0:
    if record.partner_id.id:
        if record.order_payment_method == "Credit":
            if (
                record.partner_id.credit + record.amount_total
            ) > record.partner_id.credit_limit:
                raise UserError(
                    "Customer's credit limit is exceeded."
                    + "\n"
                    + "Customer credit limit: "
                    + str(record.partner_id.credit_limit)
                    + "\n"
                    + "Cust. Total Receivable: "
                    + str(record.partner_id.credit)
                    + "\n"
                    + "Current Tot. Amount: "
                    + str(record.amount_total)
                    + "\n"
                    + "Over Credit Amount: "
                    + str(
                        (record.partner_id.credit + record.amount_total)
                        - record.partner_id.credit_limit
                    )
                )
```
  </details>
- **SRM - Auto Populate Report Type in Account Move** (`action_srm_auto_populate_report_type_in_account_move`, type `code`)
  - Function: On customer invoices, sets the Customer Aging report type (`report_type_s_cust_aging`) to the 'Customer Aging Report' sales report type.
  - Depends on: `account.move.move_type` (account), `account.move.report_type_s_cust_aging` (Jinasena_Masterdata_Reporting), `model account.move` (account), `model sales_report_type` (Jinasena_Masterdata_Reporting)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (4 lines)</summary>

```python
if record.move_type == "out_invoice":
    rpt_id = env["sales_report_type"].search(
        [("report_code", "=", "Customer Aging Report")], limit=1
    )
    if rpt_id:
        record["report_type_s_cust_aging"] = rpt_id.id
```
  </details>
- **SRM - Update Sales Order - Customer Invoice** (`action_srm_update_sales_order_customer_invoice`, type `code`)
  - Function: If an invoice has a Source Document but no Sale ID, links the sales order whose name matches the Source Document.
  - Depends on: `account.move.invoice_origin` (account), `account.move.sale_id`, `model account.move` (account), `model sale.order` (sale)
  - Used by: `automation BugFix-Accounting.automation_srm_update_sales_order_customer_invoice_2`
  <details><summary>code (6 lines)</summary>

```python
# fix_repair:idempotent-v1
if record.invoice_origin and not record.sale_id:
    sale = (
        env["sale.order"].sudo().search([("name", "=", record.invoice_origin)], limit=1)
    )
    if sale:
        record.write({"sale_id": sale.id})
```
  </details>
- **Supplier Invoice No Update in Import Vendor Bill** (`action_supplier_invoice_no_update_in_import_vendor_bill`, type `code`)
  - Function: On import vendor bills with a Consignment No, copies the consignment's Supplier Invoice Number and Invoice Date onto the bill.
  - Depends on: `account.move.consignment_no`, `account.move.supplier_invoice_number`, `model account.move` (account), `model consignment_header` (BugFix-Stock)
  - Used by: `automation BugFix-Accounting.automation_supplier_invoice_no_update_in_import_vendor_bill_3`
  <details><summary>code (5 lines)</summary>

```python
if record.consignment_no:
    consignment = env["consignment_header"].search(
        [("id", "=", record.consignment_no.id)], limit=1
    )
    if consignment:
        record["supplier_invoice_number"] = (
            consignment.supplier_invoice_number
        )
        record["invoice_date"] = consignment.accounting_invoice_date
```
  </details>
- **Supplier Invoice No Update in Import Vendor Bill - 2** (`action_supplier_invoice_no_update_in_import_vendor_bill_2`, type `code`)
  - Function: On import vendor bills with a Consignment No, copies the consignment's Supplier Invoice Number onto the bill (without the date).
  - Depends on: `account.move.consignment_no`, `account.move.supplier_invoice_number`, `model account.move` (account), `model consignment_header` (BugFix-Stock)
  - Used by: `automation BugFix-Accounting.automation_supplier_invoice_no_update_in_import_vendor_bill_2_2`
  <details><summary>code (4 lines)</summary>

```python
if record.consignment_no:
    consignment = env["consignment_header"].search(
        [("id", "=", record.consignment_no.id)], limit=1
    )
    if consignment:
        record["supplier_invoice_number"] = (
            consignment.supplier_invoice_number
        )
```
  </details>
- **TEST - 22** (`server_action_1441_test_22`, type `code`)
  - Function: Test action that just raises an error showing `document_request_line_id`; debugging leftover with no business purpose.
  - Depends on: `model account.move` (account)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (1 lines)</summary>

```python
raise UserError(record.document_request_line_id.id)
```
  </details>
- **Update Analytic Tag Parameters - Sales Invoice - Customer** (`action_update_analytic_tag_parameters_sales_invoice_customer`, type `code`)
  - Function: Sets the invoice's Account Mandatory flag from the 'Partner Mandatory' setting of the analytic distribution model for the customer, or False if none exists.
  - Depends on: `account.move.partner_id` (account), `account.move.account_mandatory`, `model account.analytic.distribution.model` (analytic), `model account.move` (account)
  - Used by: `automation BugFix-Accounting.automation_update_analytic_tag_parameters_sales_invoice_customer_2`
  <details><summary>code (6 lines)</summary>

```python
if record.partner_id:
    tag_rule = env["account.analytic.distribution.model"].search(
        [("partner_id", "=", record.partner_id.id)], limit=1
    )
    if tag_rule:
        record["account_mandatory"] = tag_rule.partner_mandatory
    else:
        record["account_mandatory"] = False
```
  </details>
- **Update Analytic Tag Parameters - Sales Invoice - User** (`action_update_analytic_tag_parameters_sales_invoice_user`, type `code`)
  - Function: Sets the invoice's Account Mandatory flag from the 'User Mandatory' setting of the analytic distribution model whose partner's salesperson is the invoice creator, else False.
  - Depends on: `account.move.account_mandatory`, `model account.analytic.distribution.model` (analytic), `model account.move` (account)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (6 lines)</summary>

```python
if record.create_uid:
    tag_rule = env["account.analytic.distribution.model"].search(
        [("partner_id.user_id", "=", record.create_uid.id)], limit=1
    )
    if tag_rule:
        record["account_mandatory"] = tag_rule.x_studio_user_mandatory
    else:
        record["account_mandatory"] = False
```
  </details>
- **Validate Journals Created from CP & NPO** (`action_validate_journals_created_from_cp_npo`, type `code`)
  - Function: Prevents deleting journal entries linked to a Cash Purchase or a Non-Inventory Purchase Order by raising an error.
  - Depends on: `account.move.cre` (BugFix-Purchase), `account.move.created_from_npo_no` (BugFix-Purchase), `model account.move` (account)
  - Used by: `automation BugFix-Accounting.automation_validate_journals_created_from_cp_npo_2`
  <details><summary>code (5 lines)</summary>

```python
if record.cre.id != False:
    raise UserError("The Journal is Liked with a Cash Purchase and can not be deleted.")

if record.created_from_npo_no.id != False:
    raise UserError(
        "The Journal is Liked with a Non-Inventory Purchase Order and can not be deleted."
    )
```
  </details>
- **Work Center Costing Model - Update Journal Entries** (`action_work_center_costing_model_update_journal_entries`, type `code`)
  - Function: For stock valuation entries of BoM products produced by a manufacturing order, overwrites the entry total and its debit/credit line amounts with the MO's total actual material cost.
  - Depends on: `model account.move.line` (account), `model account.move` (account), `model mrp.bom` (mrp), `model mrp.production` (mrp), `model stock.move` (stock)<details><summary>+1 more</summary>`model stock.valuation.layer` (stock_account)</details>
  - Used by: `automation BugFix-Accounting.base_automation_43_work_center_costing_model_update_journal_entries`
  <details><summary>code (18 lines)</summary>

```python
if record.id:
    stock_valuation = env["stock.valuation.layer"].search(
        [("account_move_id", "=", record.id)], limit=1
    )
    if stock_valuation.product_tmpl_id:
        find_bom = env["mrp.bom"].search(
            [("product_tmpl_id", "=", stock_valuation.product_tmpl_id.id)], limit=1
        )
        if find_bom:
            if stock_valuation.stock_move_id:
                stock_move = env["stock.move"].search(
                    [
                        ("id", "=", stock_valuation.stock_move_id.id),
                        ("product_tmpl_id", "=", stock_valuation.product_tmpl_id.id),
                    ],
                    limit=1,
                )
                if stock_move:
                    prod_order = env["mrp.production"].search(
                        [("id", "=", stock_move.production_id.id)], limit=1
                    )
                    if prod_order:
                        journal_lines = env["account.move.line"].search(
                            [("move_id", "=", record.id), ("quantity", "!=", 0.00)]
                        )
                        if journal_lines:
                            record.write(
                                {
                                    "amount_total": prod_order.prod_bom_total_actual_material_cost,
                                    "amount_total_signed": prod_order.prod_bom_total_actual_material_cost,
                                }
                            )
                            for update in journal_lines:
                                if update.credit == 0.00:
                                    update.write(
                                        {
                                            "debit": prod_order.prod_bom_total_actual_material_cost
                                        }
                                    )
                                if update.debit == 0.00:
                                    update.write(
                                        {
                                            "credit": prod_order.prod_bom_total_actual_material_cost
                                        }
                                    )
```
  </details>
**Automations (26):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| IMP - Update Consignment - Vendor Bill | `automation_64_imp_update_consignment_vendor_bill` |  | When a record is created or updated on Journal Entry, runs nothing (no action linked). | `model account.move` (account) |  |
| IMP - Update Consignment - Vendor Bill | `base_automation_64_imp_update_consignment_vendor_bill` |  | When a record is created or updated on Journal Entry, runs _IMP - Update Consignment - Vendor Bill_. | `account.move.create_date` (account)<br>`model account.move` (account)<br>`server action BugFix-Accounting.action_imp_update_consignment_vendor_bill` |  |
| IMP - Update LC Status to Paid | `automation_72_imp_update_lc_status_to_paid` |  | When a record is created or updated on Journal Entry, runs nothing (no action linked). | `model account.move` (account) |  |
| IMP - Update LC Status to Paid | `base_automation_72_imp_update_lc_status_to_paid` |  | When a record is created or updated on Journal Entry, runs _IMP - Update LC Status to Paid_. | `model account.move` (account)<br>`server action BugFix-Accounting.action_imp_update_lc_status_to_paid` |  |
| PR - Validate Cash Issued in NPO | `automation_pr_validate_cash_issued_in_npo` | archived | When a record is created or updated on Journal Entry, runs nothing (no action linked). **Archived — does not run.** | `model account.move` (account) |  |
| Project - Update Project No for Manual Transactions | `automation_project_update_project_no_for_manual_transactions` | archived | When a watched field changes in the form on Journal Entry, runs nothing (no action linked). **Archived — does not run.** | `model account.move` (account) |  |
| Project - Update Project No for Manual Transactions | `automation_project_update_project_no_for_manual_transactions_2` |  | When a watched field changes in the form on Journal Entry, runs _Execute Code_. | `account.move.journal_type`<br>`model account.move` (account)<br>`server action BugFix-Accounting.action_project_update_project_no_for_manual_transactions` |  |
| RR - Validate RUG in Customer Invoice | `automation_rr_validate_rug_in_customer_invoice` |  | When a record is created or updated on Journal Entry, runs nothing (no action linked). | `model account.move` (account) |  |
| RR - Validate RUG in Customer Invoice | `automation_rr_validate_rug_in_customer_invoice_2` |  | When a record is created or updated on Journal Entry, runs _Execute Code_. | `model account.move` (account)<br>`server action BugFix-Accounting.action_rr_validate_rug_in_customer_invoice` |  |
| SLS - Validate Bank Guarantee in Customer Invoice | `automation_sls_validate_bank_guarantee_in_customer_invoice` |  | When a record is created or updated on Journal Entry, runs nothing (no action linked). | `model account.move` (account) |  |
| SLS - Validate Bank Guarantee in Customer Invoice | `automation_sls_validate_bank_guarantee_in_customer_invoice_2` | archived | When a record is created or updated on Journal Entry, runs _Execute Code_. **Archived — does not run.** | `model account.move` (account)<br>`server action BugFix-Accounting.action_sls_validate_bank_guarantee_in_customer_invoice` |  |
| SLS - Validate Payment in Customer Invoice | `automation_sls_validate_payment_in_customer_invoice` | archived | When a record is updated on Journal Entry, runs _SLS - Validate Payment in Customer Invoice_. **Archived — does not run.** | `model account.move` (account)<br>`server action BugFix-Accounting.action_sls_validate_payment_in_customer_invoice` |  |
| SRM - Auto Populate Report Type in Account Move | `automation_srm_auto_populate_report_type_in_account_move` | archived | When a record is created or updated on Journal Entry and `[]`, runs nothing (no action linked). **Archived — does not run.** | `model account.move` (account) |  |
| SRM - Update Sales Order - Customer Invoice | `automation_srm_update_sales_order_customer_invoice` |  | When a record is created or updated on Journal Entry, runs nothing (no action linked). | `model account.move` (account) |  |
| SRM - Update Sales Order - Customer Invoice | `automation_srm_update_sales_order_customer_invoice_2` |  | When a record is created or updated on Journal Entry, runs _SRM - Update Sales Order - Customer Invoice_. | `account.move.create_date` (account)<br>`model account.move` (account)<br>`server action BugFix-Accounting.action_srm_update_sales_order_customer_invoice` |  |
| Supplier Invoice No Update in Import Vendor Bill | `automation_supplier_invoice_no_update_in_import_vendor_bill` |  | When a watched field changes in the form on Journal Entry, runs nothing (no action linked). | `model account.move` (account) |  |
| Supplier Invoice No Update in Import Vendor Bill | `automation_supplier_invoice_no_update_in_import_vendor_bill_3` | archived | When a watched field changes in the form on Journal Entry, runs _Supplier Invoice No Update in Import Vendor Bill_. **Archived — does not run.** | `account.move.consignment_no`<br>`model account.move` (account)<br>`server action BugFix-Accounting.action_supplier_invoice_no_update_in_import_vendor_bill` |  |
| Supplier Invoice No Update in Import Vendor Bill - 2 | `automation_supplier_invoice_no_update_in_import_vendor_bill_2` |  | When a record is created or updated on Journal Entry, runs nothing (no action linked). | `model account.move` (account) |  |
| Supplier Invoice No Update in Import Vendor Bill - 2 | `automation_supplier_invoice_no_update_in_import_vendor_bill_2_2` |  | When a record is created or updated on Journal Entry, runs _Supplier Invoice No Update in Import Vendor Bill - 2_. | `model account.move` (account)<br>`server action BugFix-Accounting.action_supplier_invoice_no_update_in_import_vendor_bill_2` |  |
| Update Analytic Tag Parameters - Sales Invoice - Customer | `automation_update_analytic_tag_parameters_sales_invoice_customer` |  | When a watched field changes in the form on Journal Entry, runs nothing (no action linked). | `model account.move` (account) |  |
| Update Analytic Tag Parameters - Sales Invoice - Customer | `automation_update_analytic_tag_parameters_sales_invoice_customer_2` |  | When a watched field changes in the form on Journal Entry, runs _Update Analytic Tag Parameters - Sales Invoice - Customer_. | `account.move.partner_id` (account)<br>`model account.move` (account)<br>`server action BugFix-Accounting.action_update_analytic_tag_parameters_sales_invoice_customer` |  |
| Update Analytic Tag Parameters - Sales Invoice - User | `automation_update_analytic_tag_parameters_sales_invoice_user` | archived | When a record is created or updated on Journal Entry, runs nothing (no action linked). **Archived — does not run.** | `model account.move` (account) |  |
| Validate Journals Created from CP & NPO | `automation_validate_journals_created_from_cp_npo` |  | When a record is deleted on Journal Entry, runs nothing (no action linked). | `model account.move` (account) |  |
| Validate Journals Created from CP & NPO | `automation_validate_journals_created_from_cp_npo_2` |  | When a record is deleted on Journal Entry, runs _Validate Journals Created from CP & NPO_. | `model account.move` (account)<br>`server action BugFix-Accounting.action_validate_journals_created_from_cp_npo` |  |
| Work Center Costing Model - Update Journal Entries | `automation_43_work_center_costing_model_update_journal_entries` |  | When a record is created or updated on Journal Entry, runs nothing (no action linked). | `model account.move` (account) |  |
| Work Center Costing Model - Update Journal Entries | `base_automation_43_work_center_costing_model_update_journal_entries` |  | When a record is created or updated on Journal Entry, runs _Work Center Costing Model - Update Journal Entries_. | `account.move.create_date` (account)<br>`model account.move` (account)<br>`server action BugFix-Accounting.action_work_center_costing_model_update_journal_entries` |  |

**Approval rules (2):**

| Name | Record name | Approver group | Function | Depends on | Used by |
|---|---|---|---|---|---|
| Journal Entry/SLS - Credit Note Approval (Sales / Credit Note Approver) (25) | `approval_rule_ar_final_journal_entry_sls_credit_note_approval_sales_credit_note` | Sales / Jin - Sales - Credit Note Approvers | Before action _SLS - Credit Note Approval - Main_ on Journal Entry runs, an approval from **Sales / Jin - Sales - Credit Note Approvers** is required (step 1). | `group BugFix-Approvals.group_jin_sales_credit_note_approvers` (BugFix-Approvals)<br>`model account.move` (account)<br>`server action BugFix-Accounting.srv_sls_credit_note_approval_main` |  |
| Journal Entry/SLS - Overdue Approval (Sales / Credit Note Approver) (24) | `approval_rule_ar_relaxed_journal_entry_sls_overdue_approval_sales_credit_note_ap` | Sales / Jin - Sales - Credit Note Approvers | Before action _SLS - Overdue Approval_ on Journal Entry runs, an approval from **Sales / Jin - Sales - Credit Note Approvers** is required (step 1). | `group BugFix-Approvals.group_jin_sales_credit_note_approvers` (BugFix-Approvals)<br>`model account.move` (account)<br>`server action BugFix-Sales.action_sls_overdue_approval` (BugFix-Sales) |  |

**Window actions (58):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Cash Advance Bills | `aw_f4_account_move_cash_advance_bills` | Opens **Journal Entry** records (tree,form), filtered to `[('project_no_bill', '=', active_id)]`. | `account.move.project_no_bill`<br>`model account.move` (account) |  |
| Cash Advance Bills | `action_cash_advance_bills` | Opens **Journal Entry** records (tree,form), filtered to `[('project_no_bill', '=', active_id)]`. | `account.move.project_no_bill`<br>`model account.move` (account) |  |
| Cash Advance Bills | `action_cash_advance_bills_2` | Opens **Journal Entry** records (tree,form), filtered to `[('project_no_bill', '=', active_id)]`. | `account.move.project_no_bill`<br>`model account.move` (account) |  |
| Cash Issued | `aw_f4_account_move_cash_issued` | Opens **Journal Entry** records (tree,form), filtered to `[('cre', '=', active_id)]`. | `account.move.cre` (BugFix-Purchase)<br>`model account.move` (account) |  |
| Cash Issued | `action_cash_issued` | Opens **Journal Entry** records (tree,form), filtered to `[('cre', '=', active_id)]`. | `account.move.cre` (BugFix-Purchase)<br>`model account.move` (account) | `view BugFix-Purchase.view_default_form_view_for_purchase_request_cas_inherit` (BugFix-Purchase) |
| Cash Issued | `action_cash_issued_2` | Opens **Journal Entry** records (tree,form), filtered to `[('cre', '=', active_id)]`. | `account.move.cre` (BugFix-Purchase)<br>`model account.move` (account) |  |
| Custom Clearance | `aw_f4_account_move_custom_clearance` | Opens **Journal Entry** records (tree,form), filtered to `[('created_from_consignment_1', '=', active_id)]`. | `account.move.created_from_consignment_1`<br>`model account.move` (account) |  |
| Custom Clearance | `action_custom_clearance` | Opens **Journal Entry** records (tree,form), filtered to `[('created_from_consignment_1', '=', active_id)]`. | `account.move.created_from_consignment_1`<br>`model account.move` (account) |  |
| Custom Clearance | `action_custom_clearance_2` | Opens **Journal Entry** records (tree,form), filtered to `[('created_from_consignment_1', '=', active_id)]`. | `account.move.created_from_consignment_1`<br>`model account.move` (account) |  |
| Custom Clearance Reversal | `aw_f4_account_move_custom_clearance_reversal` | Opens **Journal Entry** records (tree,form), filtered to `[('create_from_transfer_1', '=', active_id)]`. | `account.move.create_from_transfer_1`<br>`model account.move` (account) |  |
| Custom Clearance Reversal | `act_custom_clearance_reversal` | Opens **Journal Entry** records (tree,form), filtered to `[('created_from_vendor_bill_1', '=', active_id)]`. | `account.move.created_from_vendor_bill_1`<br>`model account.move` (account) | `view BugFix-Accounting.view_account_move_form_inherit_3` |
| Custom Clearance Reversal | `action_custom_clearance_reversal_2` | Opens **Journal Entry** records (tree,form), filtered to `[('created_from_vendor_bill_1', '=', active_id)]`. | `account.move.created_from_vendor_bill_1`<br>`model account.move` (account) |  |
| Custom Clearance Reversal | `action_custom_clearance_reversal` | Opens **Journal Entry** records (tree,form), filtered to `[('create_from_transfer_1', '=', active_id)]`. | `account.move.create_from_transfer_1`<br>`model account.move` (account) |  |
| Custom Clearance Reversal | `action_custom_clearance_reversal_4` | Opens **Journal Entry** records (tree,form), filtered to `[('created_from_vendor_bill_1', '=', active_id)]`. | `account.move.created_from_vendor_bill_1`<br>`model account.move` (account) |  |
| Custom Clearance Reversal | `action_custom_clearance_reversal_3` | Opens **Journal Entry** records (tree,form), filtered to `[('create_from_transfer_1', '=', active_id)]`. | `account.move.create_from_transfer_1`<br>`model account.move` (account) |  |
| Dispatch Reversal | `aw_f4_account_move_dispatch_reversal` | Opens **Journal Entry** records (tree,form), filtered to `[('created_from_vendor_bill', '=', active_id)]`. | `account.move.created_from_vendor_bill`<br>`model account.move` (account) |  |
| Dispatch Reversal | `act_dispatch_reversal` | Opens **Journal Entry** records (tree,form), filtered to `[('created_from_vendor_bill', '=', active_id)]`. | `account.move.created_from_vendor_bill`<br>`model account.move` (account) | `view BugFix-Accounting.view_account_move_form_inherit_3` |
| Dispatch Reversal | `action_dispatch_reversal` | Opens **Journal Entry** records (tree,form), filtered to `[('created_from_vendor_bill', '=', active_id)]`. | `account.move.created_from_vendor_bill`<br>`model account.move` (account) |  |
| Dispatch Reversal | `action_dispatch_reversal_2` | Opens **Journal Entry** records (tree,form), filtered to `[('created_from_vendor_bill', '=', active_id)]`. | `account.move.created_from_vendor_bill`<br>`model account.move` (account) |  |
| Invoice Wise Revenue Report | `aw_f4_account_move_invoice_wise_revenue_report` | Opens **Journal Entry** records (kanban,tree,form,pivot,activity). | `model account.move` (account) |  |
| Invoice Wise Revenue Report | `action_invoice_wise_revenue_report` | Opens **Journal Entry** records (kanban,tree,form,pivot,activity). | `model account.move` (account) |  |
| Invoice Wise Revenue Report | `action_invoice_wise_revenue_report_3` | Opens **Journal Entry** records (kanban,tree,form,pivot,activity). | `model account.move` (account) | `menu BugFix-Accounting.menu_invoice_wise_revenue_report_1` |
| Invoices | `aw_f4_account_move_invoices` | Opens **Journal Entry** records (tree,form,pivot). | `model account.move` (account) |  |
| Invoices | `action_invoices` | Opens **Journal Entry** records (tree,form,pivot). | `model account.move` (account) | `menu BugFix-Accounting.menu_invoices_2` |
| Invoices | `action_invoices_2` | Opens **Journal Entry** records (tree,form,pivot). | `model account.move` (account) | `menu BugFix-Accounting.menu_invoices` |
| Issued Cash Advances | `aw_f4_account_move_issued_cash_advances` | Opens **Journal Entry** records (tree,form), filtered to `[('project_no_issue', '=', active_id)]`. | `account.move.project_no_issue`<br>`model account.move` (account) |  |
| Issued Cash Advances | `action_issued_cash_advances` | Opens **Journal Entry** records (tree,form), filtered to `[('project_no_issue', '=', active_id)]`. | `account.move.project_no_issue`<br>`model account.move` (account) |  |
| Issued Cash Advances | `action_issued_cash_advances_2` | Opens **Journal Entry** records (tree,form), filtered to `[('project_no_issue', '=', active_id)]`. | `account.move.project_no_issue`<br>`model account.move` (account) |  |
| Journal Entries | `aw_f4_account_move_journal_entries` | Opens **Journal Entry** records (tree,form), filtered to `[('project_no', '=', active_id)]`. | `account.move.project_no`<br>`model account.move` (account) |  |
| Journal Entries | `action_journal_entries` | Opens **Journal Entry** records (tree,form), filtered to `[('project_no', '=', active_id)]`. | `account.move.project_no`<br>`model account.move` (account) | `menu BugFix-Accounting.menu_journal_entries` |
| Journal Entries | `action_journal_entries_2` | Opens **Journal Entry** records (tree,form), filtered to `[('project_no', '=', active_id)]`. | `account.move.project_no`<br>`model account.move` (account) |  |
| Month End Entries | `aw_f4_account_move_month_end_entries` | Opens **Journal Entry** records (tree,form), filtered to `[('created_from_project_no', '=', active_id)]`. | `account.move.created_from_project_no`<br>`model account.move` (account) |  |
| Month End Entries | `action_month_end_entries` | Opens **Journal Entry** records (tree,form), filtered to `[('created_from_project_no', '=', active_id)]`. | `account.move.created_from_project_no`<br>`model account.move` (account) |  |
| Month End Entries | `action_month_end_entries_2` | Opens **Journal Entry** records (tree,form), filtered to `[('created_from_project_no', '=', active_id)]`. | `account.move.created_from_project_no`<br>`model account.move` (account) |  |
| Related Invoice Journal | `aw_f4_account_move_related_invoice_journal` | Opens **Journal Entry** records (tree,form), filtered to `[('created_from_npo_no', '=', active_id)]`. | `account.move.created_from_npo_no` (BugFix-Purchase)<br>`model account.move` (account) |  |
| Related Invoice Journal | `action_related_invoice_journal` | Opens **Journal Entry** records (tree,form), filtered to `[('created_from_npo_no', '=', active_id)]`. | `account.move.created_from_npo_no` (BugFix-Purchase)<br>`model account.move` (account) | `view BugFix-Purchase.view_default_form_view_for_po_non_inventory_inherit` (BugFix-Purchase) |
| Related Invoice Journal | `action_related_invoice_journal_2` | Opens **Journal Entry** records (tree,form), filtered to `[('created_from_npo_no', '=', active_id)]`. | `account.move.created_from_npo_no` (BugFix-Purchase)<br>`model account.move` (account) |  |
| Sales Invoice lines | `aw_f4_account_move_sales_invoice_lines` | Opens **Journal Entry** records (kanban,tree,form,pivot). | `model account.move` (account) |  |
| Sales Invoice lines | `action_sales_invoice_lines` | Opens **Journal Entry** records (kanban,tree,form,pivot). | `model account.move` (account) |  |
| Sales Invoice lines | `action_sales_invoice_lines_3` | Opens **Journal Entry** records (kanban,tree,form,pivot). | `model account.move` (account) | `menu BugFix-Accounting.menu_sales_invoice_lines_1` |
| Settled Cash Advances | `aw_f4_account_move_settled_cash_advances` | Opens **Journal Entry** records (tree,form), filtered to `[('project_no_settle', '=', active_id)]`. | `account.move.project_no_settle`<br>`model account.move` (account) |  |
| Settled Cash Advances | `action_settled_cash_advances` | Opens **Journal Entry** records (tree,form), filtered to `[('project_no_settle', '=', active_id)]`. | `account.move.project_no_settle`<br>`model account.move` (account) |  |
| Settled Cash Advances | `action_settled_cash_advances_2` | Opens **Journal Entry** records (tree,form), filtered to `[('project_no_settle', '=', active_id)]`. | `account.move.project_no_settle`<br>`model account.move` (account) |  |
| Vend. Dispatch Reversal | `aw_f4_account_move_vend_dispatch_reversal` | Opens **Journal Entry** records (tree,form), filtered to `[('created_from_transfer', '=', active_id)]`. | `account.move.created_from_transfer`<br>`model account.move` (account) |  |
| Vend. Dispatch Reversal | `action_vend_dispatch_reversal` | Opens **Journal Entry** records (tree,form), filtered to `[('created_from_transfer', '=', active_id)]`. | `account.move.created_from_transfer`<br>`model account.move` (account) |  |
| Vend. Dispatch Reversal | `action_vend_dispatch_reversal_2` | Opens **Journal Entry** records (tree,form), filtered to `[('created_from_transfer', '=', active_id)]`. | `account.move.created_from_transfer`<br>`model account.move` (account) |  |
| Vendor Bill | `aw_f4_account_move_vendor_bill` | Opens **Journal Entry** records (tree,form), filtered to `[('tp_id', '=', active_id)]`. | `account.move.tp_id`<br>`model account.move` (account) |  |
| Vendor Bill | `act_tp_invoice_vendor_bill` | Opens **Journal Entry** records (tree,form), filtered to `[('tp_id', '=', active_id)]`. | `account.move.tp_id`<br>`model account.move` (account) | `view BugFix-Accounting.view_default_form_view_for_tp_invoice_header_inherit` |
| Vendor Bill | `action_vendor_bill` | Opens **Journal Entry** records (tree,form), filtered to `[('created_from_tp_invoice', '=', active_id)]`. | `model account.move` (account) |  |
| Vendor Bill | `action_vendor_bill_2` | Opens **Journal Entry** records (tree,form), filtered to `[('tp_id', '=', active_id)]`. | `account.move.tp_id`<br>`model account.move` (account) |  |
| Vendor Bill | `action_vendor_bill_3` | Opens **Journal Entry** records (tree,form), filtered to `[('created_from_tp_invoice', '=', active_id)]`. | `model account.move` (account) |  |
| Vendor Bill | `action_vendor_bill_4` | Opens **Journal Entry** records (tree,form), filtered to `[('tp_id', '=', active_id)]`. | `account.move.tp_id`<br>`model account.move` (account) |  |
| Vendor Despatch | `aw_f4_account_move_vendor_despatch` | Opens **Journal Entry** records (tree,form), filtered to `[('created_from_consignment', '=', active_id)]`. | `account.move.created_from_consignment`<br>`model account.move` (account) |  |
| Vendor Despatch | `action_vendor_despatch` | Opens **Journal Entry** records (tree,form), filtered to `[('created_from_consignment', '=', active_id)]`. | `account.move.created_from_consignment`<br>`model account.move` (account) |  |
| Vendor Despatch | `action_vendor_despatch_2` | Opens **Journal Entry** records (tree,form), filtered to `[('created_from_consignment', '=', active_id)]`. | `account.move.created_from_consignment`<br>`model account.move` (account) |  |
| account.move | `aw_f4_account_move_account_move` | Opens **Journal Entry** records (kanban,tree,form,pivot). | `model account.move` (account) |  |
| account.move | `action_account_move` | Opens **Journal Entry** records (kanban,tree,form,pivot). | `model account.move` (account) |  |
| account.move | `action_account_move_2` | Opens **Journal Entry** records (kanban,tree,form,pivot). | `model account.move` (account) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_account_move` (BugFix-Studio-Misc) |

**Views (12):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default pivot view for ir.model(446,) | `view_account_move_pivot_2` | pivot | full pivot layout with 0 fields | Empty default pivot view for Journal Entries (no rows, columns or measures defined); gives Journal Entry actions a pivot mode. |  |  |
| Default pivot view for ir.model(446,) | `view_account_move_pivot` | pivot | full pivot layout with 0 fields | Empty default pivot view for Journal Entries; a duplicate of `ported_default_pivot_view_f_579a1e20...` with the same name and content. |  |  |
| Odoo Studio: account.invoice.tree customization | `view_account_invoice_tree_inherit` | tree | set create=false on `//tree[1]` | Disables the Create button on the standard invoice list (`account.view_invoice_tree`). Earlier port of the same Studio customization that `ported_view_2442` also ships, so the create=false change is applied twice. | `view account.view_invoice_tree` (account) |  |
| Odoo Studio: account.invoice.tree customization | `view_account_invoice_tree_inherit_2` | tree | set create=false on `//tree[1]`; after `//tree[1]/field[@name='name']`: add field partner_id, field project_no, field journal_type | Customizes the standard invoice list: disables Create and adds Partner, Project No and Journal Type columns after the Number. | `account.move.partner_id` (account)<br>`account.move.journal_type`<br>`account.move.project_no`<br>`view account.view_invoice_tree` (account) |  |
| Odoo Studio: account.move.form customization | `view_account_move_form_inherit_2` | form | set create=false, delete=false on `//form[1]` | Disables Create and Delete on the Journal Entry/Invoice form (`account.view_move_form`). Earlier, slimmer port of the same Studio customization that `ported_view_2440` ships in full; the change is duplicated. | `view account.view_move_form` (account) |  |
| Odoo Studio: account.move.form customization | `view_account_move_form_inherit_3` | form | set create=false, delete=false on `//form[1]`; before `//form[1]/header[1]/button[@name='action_post']`: add button 'Update RUG Account'; set groups=account.group_account_invoice,__export__.res_groups_172_455e3f01, invisible=(hide_post_button or move_type != 'entry') or ((payment_id != False) or ((move_type != 'entry') or ((auto_post == True) or (state != 'draft')))) on `//form[1]/header[1]/button[@name='action_post']`; after `//form[1]/header[1]/button[@name='action_post']`: add button 'Update Advance Account', button 'Update Consignment', button 'Update Currency Rate', button 'Request Credit Note Approval', button 'Approve Credit Note', button 'View Credit Limit Overdue Details', button 'Send Bank Guarantee Validity Notification', button 'View Bank Guarantee Validity'; set groups=account.group_account_invoice,__export__.res_groups_246_295324b5,__export__.res_groups_227_f695d21c,__export__.res_groups_251_c8b4a865,__export__.res_groups_263_168d4e47, invisible=(hide_post_button or move_type == 'entry' or display_inactive_currency_warning) or (((payment_id != False) and ((advance_acc_updated == False) and (type == 'Advance Payment'))) or (((rug_acc_updated == False) and ((rug_rejected == False) and (rug_confirmed == True))) or (((bg_sent == False) and (bank_guarantee_notification == True)) or (((credit_note_approved == False) and (move_type == 'out_refund')) or (((currency_rate_updated == False) and (purchase_type == 'Import')) or (((update_consignment == False) and (purchase_type == 'Import')) or ((move_type == 'entry') or ((auto_post == True) or ((state != 'draft') or ((bank_guarantee_validation == True) or ((credit_limit_validation == True) or (valid_lines == True)))))))))))) on `//form[1]/header[1]/button[@name='action_post'][2]`; set invisible=(state != 'posted' or payment_state not in ('partial', 'not_paid') or move_type not in ('out_invoice', 'out_refund', 'in_invoice', 'in_refund', 'out_receipt', 'in_receipt') or authorized_transaction_ids) or ((project_no != False) or ((((rug_acc_updated == True) and (rug_confirmed == True)) or ((move_type not in ('out_invoice', 'out_refund', 'in_invoice', 'in_refund', 'out_receipt', 'in_receipt')) or ((payment_state not in ('not_paid', 'partial')) or (state != 'posted')))))) on `//button[@name='action_register_payment']`; set groups=account.group_account_invoice,studio_customization.sales_credit_note_ap_ee96b839-2a01-48d8-9116-c110a15beb4e on `//button[@name='action_reverse']`; after `//button[@name='action_view_landed_costs']`: add button '2563', button '2564' … | Main Jinasena customization of the Journal Entry/Invoice form: disables create/delete, adds approval and update buttons (RUG/Advance account, Consignment, Currency Rate, Credit Note approval, credit-limit and bank-guarantee checks), restricts Post/Register Payment/Reverse by groups and Studio flags, adds reversal smart buttons and consignment/transfer link fields. | `account.move.move_type` (account)<br>`account.move.payment_id` (account)<br>`account.move.state` (account)<br>`account.move.stock_move_id` (stock_account)<br>`account.move.account_mandatory`<details><summary>+56 more</summary>`account.move.advance_acc_updated`<br>`account.move.bank_guarantee_approved`<br>`account.move.bank_guarantee_notification`<br>`account.move.bank_guarantee_validation`<br>`account.move.bg_sent`<br>`account.move.consignment_no`<br>`account.move.create_from_transfer_1`<br>`account.move.created_from_consignment_1`<br>`account.move.created_from_consignment`<br>`account.move.created_from_project_no`<br>`account.move.created_from_project`<br>`account.move.created_from_transfer`<br>`account.move.created_from_vendor_bill_1`<br>`account.move.created_from_vendor_bill`<br>`account.move.credit_limit_approved`<br>`account.move.credit_limit_validation`<br>`account.move.credit_note_approved`<br>`account.move.credit_note_request_sent`<br>`account.move.currency_rate_updated`<br>`account.move.currency_rate`<br>`account.move.custom_clearance_no`<br>`account.move.journal_type`<br>`account.move.lc_no`<br>`account.move.order_payment_method`<br>`account.move.over_bank_guarantee`<br>`account.move.project_no_bill`<br>`account.move.project_no_issue`<br>`account.move.project_no_settle`<br>`account.move.project_no`<br>`account.move.accounting_purchase_id`<br>`account.move.purchase_type`<br>`account.move.report_type_s_cust_aging` (Jinasena_Masterdata_Reporting)<br>`account.move.rug_acc_updated`<br>`account.move.rug_confirmed`<br>`account.move.rug_rejected`<br>`account.move.sale_id`<br>`account.move.supplier_invoice_number`<br>`account.move.test_type`<br>`account.move.tp_id`<br>`account.move.type`<br>`account.move.update_consignment`<br>`account.move.valid_lines`<br>`account.move.created_from_vendor_bill_1__account_move_count`<br>`account.move.created_from_vendor_bill__account_move_count`<br>`server action BugFix-Accounting.srv_imp_update_consignment_pi`<br>`server action BugFix-Accounting.srv_imp_vendor_bill_currency_rate`<br>`server action BugFix-Accounting.srv_rug_account_update_in_si`<br>`server action BugFix-Accounting.srv_sls_credit_note_approval_main`<br>`server action BugFix-Accounting.srv_sls_request_credit_note_approval`<br>`server action BugFix-Accounting.srv_sls_send_bank_guarantee_notification`<br>`server action BugFix-Accounting.srv_sls_view_bank_guarantee_validation`<br>`server action BugFix-Accounting.srv_sls_view_credit_limit_validation`<br>`server action BugFix-Accounting.srv_update_advance_payment_account_vendor_bill`<br>`view account.view_move_form` (account)<br>`window action BugFix-Accounting.act_custom_clearance_reversal`<br>`window action BugFix-Accounting.act_dispatch_reversal`</details> |  |
| Odoo Studio: account.move.form customization_button | `view_account_move_form_inherit` | form | inside `//form`: add field bank_guarantee_notification, field bank_guarantee_validation, field bg_sent, field credit_limit_validation, field credit_note_approved, field currency_rate_updated, field rug_acc_updated, field rug_confirmed, field rug_rejected, field update_consignment; before `//header/button[@name='action_post']`: add ; after `//header/button[@name='action_post']`: add ; set invisible=((rug_acc_updated == False) and ((rug_rejected == False) and (rug_confirmed == True))) or (((bg_sent == False) and (bank_guarantee_notification == True)) or (((credit_note_approved == False) and (move_type == 'out_refund')) or (((currency_rate_updated == False) and (x_studio_pr_type_1 == 'Import')) or (((update_consignment == False) and (x_studio_pr_type_1 == 'Import')) or ((move_type == 'entry') or ((auto_post == True) or ((state != 'draft') or ((bank_guarantee_validation == True) or (credit_limit_validation == True))))))))) on `//header/button[@name='action_post'][2]`; set readonly=((update_consignment == True) and (x_studio_pr_type_1 == 'Import')) or (state == 'posted') on `//sheet/notebook/page/field[@name='invoice_line_ids']`; before `//header/button[@name='action_post'][2]`: add ; set invisible=(((rug_acc_updated == True) and (rug_confirmed == True)) or ((move_type not in ('out_invoice', 'out_refund', 'in_invoice', 'in_refund', 'out_receipt', 'in_receipt')) or ((payment_state not in ('not_paid', 'partial')) or (state != 'posted')))) on `//header/button[@name='action_register_payment']` | Inactive (archived) older Journal Entry form customization: hidden Studio flag fields, stripped action buttons and Post/Register Payment/invoice-line lock conditions; has no effect (superseded by the active move-form customizations). | `account.move.bank_guarantee_notification`<br>`account.move.bank_guarantee_validation`<br>`account.move.bg_sent`<br>`account.move.credit_limit_validation`<br>`account.move.credit_note_approved`<details><summary>+6 more</summary>`account.move.currency_rate_updated`<br>`account.move.rug_acc_updated`<br>`account.move.rug_confirmed`<br>`account.move.rug_rejected`<br>`account.move.update_consignment`<br>`view account.view_move_form` (account)</details> |  |
| Odoo Studio: account.move.tree customization | `view_account_move_tree_inherit` | tree | after `//tree[1]/field[@name='name']`: add field id; after `//field[@name='state']`: add field create_uid, field create_date | Adds the record ID after Number, and Created By / Created On columns after Status, to the Journal Entries list. | `view account.view_move_tree` (account) |  |
| Odoo Studio: account.out.invoice.tree customization | `view_account_out_invoice_tree_inherit` | tree | set create=true on `//tree[1]` | Re-enables the Create button on the Customer Invoices list (`account.view_out_invoice_tree`). Duplicate of the attribute change in `ported_view_3906`. | `view account.view_out_invoice_tree` (account) |  |
| Odoo Studio: account.out.invoice.tree customization | `view_account_out_invoice_tree_inherit_2` | tree | set create=true on `//tree[1]` | Re-enables the Create button on the Vendor Bills list (`account.view_in_invoice_tree`), overriding the create=false set on the base invoice list. Duplicate of `ported_view_3907`. | `view account.view_in_invoice_tree` (account) |  |
| Odoo Studio: account.out.invoice.tree customization | `view_account_out_invoice_tree_inherit_3` | tree | set create=true on `//tree[1]`; after `//tree[1]/field[@name='name']`: add field journal_id; after `//field[@name='amount_total_signed']`: add field report_type_s_cust_aging | Customer Invoices list: re-enables Create, adds a Journal column after Number and the 'Report Type (Customer Aging)' field after the signed total. | `account.move.journal_id` (account)<br>`account.move.report_type_s_cust_aging` (Jinasena_Masterdata_Reporting)<br>`view account.view_out_invoice_tree` (account) |  |
| Odoo Studio: account.out.invoice.tree customization | `view_account_out_invoice_tree_inherit_4` | tree | set create=true on `//tree[1]` | Re-enables the Create button on the Vendor Bills list (`account.view_in_invoice_tree`). | `view account.view_in_invoice_tree` (account) |  |

**Reports (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Journal Entry Report | `action_report_journal_entry_1` | Prints **Journal Entry Report** (qweb-pdf) for account.move records using template `BugFix-Accounting.report_journal_entry_1`; listed in the Print menu. | `model account.move` (account)<br>`view BugFix-Accounting.report_journal_entry_1` |  |
| Journal Entry Report | `action_report_journal_entry_2` | Prints **Journal Entry Report** (qweb-pdf) for account.move records using template `BugFix-Accounting.report_journal_entry_2`; listed in the Print menu. | `model account.move` (account)<br>`view BugFix-Accounting.report_journal_entry_2` |  |
| Pro forma Invoice | `action_report_pro_forma_invoice` | Prints **Pro forma Invoice** (qweb-pdf) for account.move records using template `BugFix-Accounting.report_pro_forma_invoice`; listed in the Print menu. | `model account.move` (account)<br>`view BugFix-Accounting.report_pro_forma_invoice` |  |

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| account.move | `access_account_move` | Gives **Sales / Jin - Sales - POS Users** read/write/create/delete access to Journal Entry records. | `group BugFix-Approvals.group_jin_sales_pos_users` (BugFix-Approvals)<br>`model account.move` (account) |  |

**Record rules (11):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Account Entry | `rule_77_account_entry` | For everyone (global rule): read/write/create/delete on Journal Entry only where `[('company_id', 'in', company_ids + [False])]`. | `account.move.company_id` (account)<br>`model account.move` (account) |  |
| All Invoices | `rule_all_invoices` | For Sales / User: All Documents: read/write/create/delete on Journal Entry only where `[('move_type', 'in', ('out_invoice', 'out_refund', 'in_invoice', 'in_refund'))]`. | `account.move.move_type` (account)<br>`group sales_team.group_sale_salesman_all_leads` (sales_team)<br>`model account.move` (account) |  |
| All Journal Entries | `rule_93_all_journal_entries` | For Accounting / Billing: read/write/create/delete on Journal Entry with no record filter (empty domain = all records). | `group account.group_account_invoice` (account)<br>`model account.move` (account) |  |
| Expense Team Approver Account Move | `rule_expense_team_approver_account_move` | For Expenses / Team Approver: read/write/create/delete on Journal Entry only where `[('line_ids.expense_id', '!=', False)]`. | `account.move.line.expense_id` (hr_expense)<br>`account.move.line_ids` (account)<br>`group hr_expense.group_hr_expense_team_approver` (hr_expense)<br>`model account.move` (account) |  |
| Invoice POS User | `rule_invoice_pos_user` | For Point of Sale / User: read/write/create/delete on Journal Entry only where `[('pos_order_ids', '!=', False)]`. | `account.move.pos_order_ids` (point_of_sale)<br>`group point_of_sale.group_pos_user` (point_of_sale)<br>`model account.move` (account) |  |
| Personal Invoices | `rule_personal_invoices` | For Sales / User: Own Documents Only: read/write/create/delete on Journal Entry only where `[('move_type', 'in', ('out_invoice', 'out_refund', 'in_invoice', 'in_refund')), '|', ('invoice_user_id', '=', user.id), ('invoice_user_id', '=', False)]`. | `account.move.invoice_user_id` (account)<br>`account.move.move_type` (account)<br>`group sales_team.group_sale_salesman` (sales_team)<br>`model account.move` (account) |  |
| Point Of Sale Account move | `rule_point_of_sale_account_move` | For Point of Sale / User: read/write/create/delete on Journal Entry only where `[('pos_order_ids', '!=', False)]`. | `account.move.pos_order_ids` (point_of_sale)<br>`group point_of_sale.group_pos_user` (point_of_sale)<br>`model account.move` (account) |  |
| Portal Personal Account Invoices | `rule_95_portal_personal_account_invoices` | For User types / Portal: read/write/create/delete on Journal Entry only where `[('move_type', 'in', ('out_invoice', 'out_refund', 'in_invoice', 'in_refund')), ('message_partner_ids','child_of',[user.commercial_partner_id.id])]`. | `account.move.message_partner_ids` (account)<br>`account.move.move_type` (account)<br>`group base.group_portal` (base)<br>`model account.move` (account) |  |
| Purchase User Account Move | `rule_purchase_user_account_move` | For Purchase / User: read/write/create/delete on Journal Entry only where `[('move_type', 'in', ('in_invoice', 'in_refund', 'in_receipt'))]`. | `account.move.move_type` (account)<br>`group purchase.group_purchase_user` (purchase)<br>`model account.move` (account) |  |
| Readonly Move | `rule_97_readonly_move` | For Accounting / Read-only: read on Journal Entry with no record filter (empty domain = all records). | `group account.group_account_readonly` (account)<br>`model account.move` (account) |  |
| Readonly Move | `rule_99_readonly_move` | For Accounting / Billing: read/write/create/delete on Journal Entry with no record filter (empty domain = all records). | `group account.group_account_invoice` (account)<br>`model account.move` (account) |  |
