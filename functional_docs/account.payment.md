# BugFix-Accounting — `account.payment`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.payment` — account.payment

*Extends a model created by `account`.* Python: `models/account_payment.py`.

Other repos that use this model: `account.payment._fix_repair_onchange_validate_advance_pct()` (Fix-repair)<br>`project.task._compute_valid_invoiced_so()` (Fix-repair)<br>`purchase.order._compute_account_payment_count()` (BugFix-Purchase)<br>`server action BugFix-Sales.action_sls_create_customer_payment` (BugFix-Sales)<br>`server action BugFix-Stock.action_stock_picking_sls_validate_payment_in_shipment` (BugFix-Stock)<br>`server action BugFix-Stock.action_sls_validate_payment_in_shipment` (BugFix-Stock)<br>`server action BugFix-Stock.action_sls_validate_payment_in_xxx` (BugFix-Stock)<br>`stock.picking._fix_repair_compute_repair_payment_made()` (Fix-repair)

**Summary:**

<!-- SUMMARY:model:account.payment -->
This repo adds 114 fields to payments. Most are read-only mirrors of the Studio fields on the payment's journal entry or empty non-stored placeholders. Its own fields include Type (General or Advance Payment), Sales Order, Quotation Type, Project No, LC No, Purchase Order, TP Invoice No and a computed Payment Validation flag. Server actions and automations move advance payments to the configured advance payment account, block repair payments below the company's Advance Payment %, copy the project number onto the journal entry, and mark LCs as paid. The repo also adds Post Payments and Print Checks actions. It customizes the payment form and list, and adds three payment prints, including the Jinasena Payment Receipt.
<!-- /SUMMARY -->

**Fields (114):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `account_mandatory` | Account Mandatory | boolean | Read-only mirror of the 'Account Mandatory' field on the payment's journal entry (related to `move_id.account_mandatory`); stored copy kept in sync by Odoo. | related `move_id.account_mandatory`; stored | `account.move.account_mandatory`<br>`account.payment.move_id` (account) |  |
| `advance_acc_updated` | Advance ACC Updated | boolean | Read-only mirror of the 'Advance ACC Updated' field on the payment's journal entry (related to `move_id.advance_acc_updated`); stored copy kept in sync by Odoo. | related `move_id.advance_acc_updated`; stored | `account.move.advance_acc_updated`<br>`account.payment.move_id` (account) |  |
| `advance_payment_acc_updated` | Advance Payment ACC Updated | boolean | Set by the 'Project - Update Advance Payment Acc' action once the payment's advance account has been updated; shown on the payment form. | stored |  | `server action BugFix-Accounting.action_project_update_advance_payment_account`<br>`server action BugFix-Accounting.srv_advance_payment_acc_update`<br>`view BugFix-Accounting.view_account_payment_form_inherit` |
| `bank_guarantee_approved` | Bank Guarantee Approved | boolean | Read-only mirror of the 'Bank Guarantee Approved' field on the payment's journal entry (related to `move_id.bank_guarantee_approved`); stored copy kept in sync by Odoo. | related `move_id.bank_guarantee_approved`; stored | `account.move.bank_guarantee_approved`<br>`account.payment.move_id` (account) |  |
| `bank_guarantee_notification` | Bank Guarantee Notification | boolean | Read-only mirror of the 'Bank Guarantee Notification' field on the payment's journal entry (related to `move_id.bank_guarantee_notification`); stored copy kept in sync by Odoo. | related `move_id.bank_guarantee_notification`; stored | `account.move.bank_guarantee_notification`<br>`account.payment.move_id` (account) |  |
| `bank_guarantee_validation` | Bank Guarantee Validation | boolean | Read-only mirror of the 'Bank Guarantee Validation' field on the payment's journal entry (related to `move_id.bank_guarantee_validation`); stored copy kept in sync by Odoo. | related `move_id.bank_guarantee_validation`; stored | `account.move.bank_guarantee_validation`<br>`account.payment.move_id` (account) |  |
| `bg_sent` | BG Sent | boolean | Read-only mirror of the 'BG Sent' field on the payment's journal entry (related to `move_id.bg_sent`); stored copy kept in sync by Odoo. | related `move_id.bg_sent`; stored | `account.move.bg_sent`<br>`account.payment.move_id` (account) |  |
| `boolean_field_A32jc` | New Checkbox | boolean | Non-stored placeholder copied from the same-named Journal Entry field ('New Checkbox'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `boolean_field_E4oM7` | New Checkbox | boolean | Non-stored placeholder copied from the same-named Journal Entry field ('New Checkbox'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `boolean_field_EoMg9` | New Checkbox | boolean | Non-stored placeholder copied from the same-named Journal Entry field ('New Checkbox'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `boolean_field_MVlhn` | New Checkbox | boolean | Non-stored placeholder copied from the same-named Journal Entry field ('New Checkbox'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `boolean_field_RIlaO` | New Checkbox | boolean | Non-stored placeholder copied from the same-named Journal Entry field ('New Checkbox'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `boolean_field_XzV6D` | New Checkbox | boolean | Non-stored placeholder copied from the same-named Journal Entry field ('New Checkbox'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `boolean_field_bnVim` | New Checkbox | boolean | Non-stored placeholder copied from the same-named Journal Entry field ('New Checkbox'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `boolean_field_djczB` | New Checkbox | boolean | Non-stored placeholder copied from the same-named Journal Entry field ('New Checkbox'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `boolean_field_qcQya` | New Checkbox | boolean | Non-stored placeholder copied from the same-named Journal Entry field ('New Checkbox'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `boolean_field_xNbhc` | New Checkbox | boolean | Non-stored placeholder copied from the same-named Journal Entry field ('New Checkbox'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `boolean_field_xud0H` | New Checkbox | boolean | Non-stored placeholder copied from the same-named Journal Entry field ('New Checkbox'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `boolean_field_ydmJ5` | New Checkbox | boolean | Non-stored placeholder copied from the same-named Journal Entry field ('New Checkbox'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `boolean_field_ygnit` | New Checkbox | boolean | Non-stored placeholder copied from the same-named Journal Entry field ('New Checkbox'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `char_field_FnRNH` | New Text | char | Non-stored placeholder copied from the same-named Journal Entry field ('New Text'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `co` | Co | many2one → `consignment_header` | Read-only mirror of the 'Co' field on the payment's journal entry (related to `move_id.co`); not stored. | related `move_id.co`; not stored | `account.move.co`<br>`account.payment.move_id` (account)<br>`model consignment_header` (BugFix-Stock) |  |
| `consignment_no` | Consignment No | many2one → `consignment_header` | Read-only mirror of the 'Consignment No' field on the payment's journal entry (related to `move_id.consignment_no`); stored copy kept in sync by Odoo. | related `move_id.consignment_no`; stored | `account.move.consignment_no`<br>`account.payment.move_id` (account)<br>`model consignment_header` (BugFix-Stock) |  |
| `create_from_transfer` | Create From Transfer | many2one → `stock.picking` | Read-only mirror of the 'Create From Transfer' field on the payment's journal entry (related to `move_id.create_from_transfer`); not stored. | related `move_id.create_from_transfer`; not stored | `account.move.create_from_transfer`<br>`account.payment.move_id` (account)<br>`model stock.picking` (stock) |  |
| `create_from_transfer_1` | Create From Transfer | many2one → `stock.picking` | Read-only mirror of the 'Create From Transfer' field on the payment's journal entry (related to `move_id.create_from_transfer_1`); stored copy kept in sync by Odoo. | related `move_id.create_from_transfer_1`; stored | `account.move.create_from_transfer_1`<br>`account.payment.move_id` (account)<br>`model stock.picking` (stock) |  |
| `created_from_consignment` | Created From Consignment | many2one → `consignment_header` | Read-only mirror of the 'Created From Consignment' field on the payment's journal entry (related to `move_id.created_from_consignment`); stored copy kept in sync by Odoo. | related `move_id.created_from_consignment`; stored | `account.move.created_from_consignment`<br>`account.payment.move_id` (account)<br>`model consignment_header` (BugFix-Stock) |  |
| `created_from_consignment_1` | Created From Consignment | many2one → `consignment_header` | Read-only mirror of the 'Created From Consignment' field on the payment's journal entry (related to `move_id.created_from_consignment_1`); stored copy kept in sync by Odoo. | related `move_id.created_from_consignment_1`; stored | `account.move.created_from_consignment_1`<br>`account.payment.move_id` (account)<br>`model consignment_header` (BugFix-Stock) |  |
| `created_from_consignment_2` | Created From Consignment 2 | many2one → `consignment_header` | Non-stored placeholder copied from the same-named Journal Entry field ('Created From Consignment 2'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored | `model consignment_header` (BugFix-Stock) |  |
| `created_from_project` | Created From Project | boolean | Read-only mirror of the 'Created From Project' field on the payment's journal entry (related to `move_id.created_from_project`); stored copy kept in sync by Odoo. | related `move_id.created_from_project`; stored | `account.move.created_from_project`<br>`account.payment.move_id` (account) |  |
| `created_from_project_1` | Created From Project | boolean | Checkbox on the payment form marking a payment created from a project; no logic in this repo reads it. | stored |  | `view BugFix-Accounting.view_account_payment_form_inherit` |
| `created_from_project_no` | Created From Project No | many2one → `project.project` | Read-only mirror of the 'Created From Project No' field on the payment's journal entry (related to `move_id.created_from_project_no`); stored copy kept in sync by Odoo. | related `move_id.created_from_project_no`; stored | `account.move.created_from_project_no`<br>`account.payment.move_id` (account)<br>`model project.project` (project) |  |
| `created_from_tp_invoice` | Created From TP Invoice | many2one → `tp_invoice_header` | Non-stored placeholder copied from the same-named Journal Entry field ('Created From TP Invoice'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored | `model tp_invoice_header` |  |
| `created_from_transfer` | Created From Transfer | many2one → `stock.picking` | Read-only mirror of the 'Created From Transfer' field on the payment's journal entry (related to `move_id.created_from_transfer`); stored copy kept in sync by Odoo. | related `move_id.created_from_transfer`; stored | `account.move.created_from_transfer`<br>`account.payment.move_id` (account)<br>`model stock.picking` (stock) |  |
| `created_from_vendor_bill` | Created From Vendor Bill | many2one → `account.move` | Read-only mirror of the 'Created From Vendor Bill' field on the payment's journal entry (related to `move_id.created_from_vendor_bill`); not stored. | related `move_id.created_from_vendor_bill`; not stored | `account.move.created_from_vendor_bill`<br>`account.payment.move_id` (account)<br>`model account.move` (account) |  |
| `created_from_vendor_bill_1` | Created From Vendor Bill | many2one → `account.move` | Read-only mirror of the 'Created From Vendor Bill' field on the payment's journal entry (related to `move_id.created_from_vendor_bill_1`); not stored. | related `move_id.created_from_vendor_bill_1`; not stored | `account.move.created_from_vendor_bill_1`<br>`account.payment.move_id` (account)<br>`model account.move` (account) |  |
| `created_transfer` | Created Transfer | many2one → `stock.picking` | Non-stored placeholder copied from the same-named Journal Entry field ('Created Transfer'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored | `model stock.picking` (stock) |  |
| `credit_limit_approved` | Credit Limit Approved | boolean | Read-only mirror of the 'Credit Limit Approved' field on the payment's journal entry (related to `move_id.credit_limit_approved`); stored copy kept in sync by Odoo. | related `move_id.credit_limit_approved`; stored | `account.move.credit_limit_approved`<br>`account.payment.move_id` (account) |  |
| `credit_limit_validation` | Credit Limit Validation | boolean | Read-only mirror of the 'Credit Limit Validation' field on the payment's journal entry (related to `move_id.credit_limit_validation`); stored copy kept in sync by Odoo. | related `move_id.credit_limit_validation`; stored | `account.move.credit_limit_validation`<br>`account.payment.move_id` (account) |  |
| `credit_note_approved` | Credit Note Approved | boolean | Read-only mirror of the 'Credit Note Approved' field on the payment's journal entry (related to `move_id.credit_note_approved`); stored copy kept in sync by Odoo. | related `move_id.credit_note_approved`; stored | `account.move.credit_note_approved`<br>`account.payment.move_id` (account) |  |
| `credit_note_request_sent` | Credit Note Request Sent | boolean | Read-only mirror of the 'Credit Note Request Sent' field on the payment's journal entry (related to `move_id.credit_note_request_sent`); stored copy kept in sync by Odoo. | related `move_id.credit_note_request_sent`; stored | `account.move.credit_note_request_sent`<br>`account.payment.move_id` (account) |  |
| `currency_rate` | Currency Rate | float | Read-only mirror of the 'Currency Rate' field on the payment's journal entry (related to `move_id.currency_rate`); stored copy kept in sync by Odoo. | related `move_id.currency_rate`; stored | `account.move.currency_rate`<br>`account.payment.move_id` (account) |  |
| `currency_rate_updated` | Currency Rate Updated | boolean | Read-only mirror of the 'Currency Rate Updated' field on the payment's journal entry (related to `move_id.currency_rate_updated`); stored copy kept in sync by Odoo. | related `move_id.currency_rate_updated`; stored | `account.move.currency_rate_updated`<br>`account.payment.move_id` (account) |  |
| `custom_clearance_no` | Custom Clearance No | char | Read-only mirror of the 'Custom Clearance No' field on the payment's journal entry (related to `move_id.custom_clearance_no`); stored copy kept in sync by Odoo. | related `move_id.custom_clearance_no`; stored | `account.move.custom_clearance_no`<br>`account.payment.move_id` (account) |  |
| `float_field_5tma1` | New Decimal | float | Non-stored placeholder copied from the same-named Journal Entry field ('New Decimal'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `journal_type` | Journal Type | selection | Read-only mirror of the 'Journal Type' field on the payment's journal entry (related to `move_id.journal_type`); stored copy kept in sync by Odoo. Also read by the payment's 'Update Project No in Journal Entry' automation. | related `move_id.journal_type`; stored | `account.move.journal_type`<br>`account.payment.move_id` (account) | `server action BugFix-Accounting.action_account_payment_update_project_no_in_journal_entry`<br>`server action BugFix-Accounting.action_update_project_no_in_journal_entry` |
| `lc_no` | LC No | many2one → `lc_header` | Read-only mirror of the 'LC No' field on the payment's journal entry (related to `move_id.lc_no`); stored copy kept in sync by Odoo. | related `move_id.lc_no`; stored | `account.move.lc_no`<br>`account.payment.move_id` (account)<br>`model lc_header` |  |
| `lc_no_1` | LC No | many2one → `lc_header` | Letter of credit this payment settles; the 'IMP - Update LC Status to Paid' action uses it to mark the LC as paid. | stored | `model lc_header` | `server action BugFix-Accounting.action_imp_update_lc_status_to_paid_2`<br>`view BugFix-Accounting.view_account_payment_form_inherit` |
| `lc_test1` | LC - test1 | boolean | Read-only mirror of the 'LC - test1' field on the payment's journal entry (related to `move_id.lc_test1`); stored copy kept in sync by Odoo. | related `move_id.lc_test1`; stored | `account.move.lc_test1`<br>`account.payment.move_id` (account) |  |
| `many2one_field_6HjHy` | Journal Entry | many2one → `account.move` | Non-stored placeholder copied from the same-named Journal Entry field ('Journal Entry'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored | `model account.move` (account) |  |
| `many2one_field_6Sjmv` | Transfer | many2one → `stock.picking` | Non-stored placeholder copied from the same-named Journal Entry field ('Transfer'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored | `model stock.picking` (stock) |  |
| `many2one_field_A197A` | Consignment Header | many2one → `consignment_header` | Non-stored placeholder copied from the same-named Journal Entry field ('Consignment Header'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored | `model consignment_header` (BugFix-Stock) |  |
| `many2one_field_B4ibh` | Project | many2one → `project.project` | Non-stored placeholder copied from the same-named Journal Entry field ('Project'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored | `model project.project` (project) |  |
| `many2one_field_KKFaY` | TP Invoice Header | many2one → `tp_invoice_header` | Non-stored placeholder copied from the same-named Journal Entry field ('TP Invoice Header'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored | `model tp_invoice_header` |  |
| `many2one_field_L9MIu` | Sales Report Type | many2one → `sales_report_type` | Non-stored placeholder copied from the same-named Journal Entry field ('Sales Report Type'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored | `model sales_report_type` (Jinasena_Masterdata_Reporting) |  |
| `many2one_field_P4o2n` | Project | many2one → `project.project` | Non-stored placeholder copied from the same-named Journal Entry field ('Project'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored | `model project.project` (project) |  |
| `many2one_field_PJkjM` | LC Header | many2one → `lc_header` | Non-stored placeholder copied from the same-named Journal Entry field ('LC Header'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored | `model lc_header` |  |
| `many2one_field_R46Ke` | Project | many2one → `project.project` | Non-stored placeholder copied from the same-named Journal Entry field ('Project'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored | `model project.project` (project) |  |
| `many2one_field_TEK9K` | Transfer | many2one → `stock.picking` | Non-stored placeholder copied from the same-named Journal Entry field ('Transfer'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored | `model stock.picking` (stock) |  |
| `many2one_field_XhwuI` | Purchase Order | many2one → `purchase.order` | Non-stored placeholder copied from the same-named Journal Entry field ('Purchase Order'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored | `model purchase.order` (purchase) |  |
| `many2one_field_aIXMs` | TP Invoice Header | many2one → `tp_invoice_header` | Non-stored placeholder copied from the same-named Journal Entry field ('TP Invoice Header'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored | `model tp_invoice_header` |  |
| `many2one_field_ffAE3` | Journal Entry | many2one → `account.move` | Non-stored placeholder copied from the same-named Journal Entry field ('Journal Entry'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored | `model account.move` (account) |  |
| `many2one_field_jslCp` | Consignment Header | many2one → `consignment_header` | Non-stored placeholder copied from the same-named Journal Entry field ('Consignment Header'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored | `model consignment_header` (BugFix-Stock) |  |
| `many2one_field_mULOh` | Journal Entry | many2one → `account.move` | Non-stored placeholder copied from the same-named Journal Entry field ('Journal Entry'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored | `model account.move` (account) |  |
| `many2one_field_mucWu` | Consignment Header | many2one → `consignment_header` | Non-stored placeholder copied from the same-named Journal Entry field ('Consignment Header'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored | `model consignment_header` (BugFix-Stock) |  |
| `many2one_field_re1H2` | Sales Order | many2one → `sale.order` | Non-stored placeholder copied from the same-named Journal Entry field ('Sales Order'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored | `model sale.order` (sale) |  |
| `many2one_field_tpCkS` | Project | many2one → `project.project` | Non-stored placeholder copied from the same-named Journal Entry field ('Project'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored | `model project.project` (project) |  |
| `many2one_field_vAeTQ` | Project | many2one → `project.project` | Non-stored placeholder copied from the same-named Journal Entry field ('Project'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored | `model project.project` (project) |  |
| `many2one_field_xkSx5` | Journal Entry | many2one → `account.move` | Non-stored placeholder copied from the same-named Journal Entry field ('Journal Entry'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored | `model account.move` (account) |  |
| `order_payment_method` | Order Payment Method | selection | Read-only mirror of the 'Order Payment Method' field on the payment's journal entry (related to `move_id.order_payment_method`); stored copy kept in sync by Odoo. | related `move_id.order_payment_method`; stored | `account.move.order_payment_method`<br>`account.payment.move_id` (account) |  |
| `over_bank_guarantee` | Over Bank Guarantee | boolean | Read-only mirror of the 'Over Bank Guarantee' field on the payment's journal entry (related to `move_id.over_bank_guarantee`); stored copy kept in sync by Odoo. | related `move_id.over_bank_guarantee`; stored | `account.move.over_bank_guarantee`<br>`account.payment.move_id` (account) |  |
| `payment_validation` | Payment Validation | boolean | True when a Sales Order is linked and the payment amount is positive (simplified port of the Studio compute); shown on the payment form. | computed by `_compute_payment_validation`; stored | `account.payment._compute_payment_validation()` | `account.payment._compute_payment_validation()`<br>`view BugFix-Accounting.view_account_payment_form_inherit` |
| `payment_validation_1` | Payment Validation | char | Text field on the payment form with an ir.default default; no logic in this repo reads it. | stored |  | `default BugFix-Accounting.default_account_payment_payment_validation_1`<br>`view BugFix-Accounting.view_account_payment_form_inherit` |
| `project_no` | Project No | many2one → `project.project` | Read-only mirror of the 'Project No' field on the payment's journal entry (related to `move_id.project_no`); stored copy kept in sync by Odoo. Also read by the payment's 'Update Project No in Journal Entry' automation. | related `move_id.project_no`; stored | `account.move.project_no`<br>`account.payment.move_id` (account)<br>`model project.project` (project) | `server action BugFix-Accounting.action_account_payment_update_project_no_in_journal_entry`<br>`server action BugFix-Accounting.action_update_project_no_in_journal_entry` |
| `project_no_1` | Project No | many2one → `project.project` | Project chosen on the payment; the 'Update Project No in Journal Entry' automation copies it to the payment's journal entry as Project No and Project No Issue. Filters the 'Payments' window action. | stored | `model project.project` (project) | `server action BugFix-Accounting.action_account_payment_update_project_no_in_journal_entry`<br>`server action BugFix-Accounting.action_update_project_no_in_journal_entry`<br>`view BugFix-Accounting.view_account_payment_form_inherit`<br>`window action BugFix-Accounting.action_payments_4`<br>`window action BugFix-Accounting.action_payments_2`<details><summary>+1 more</summary>`window action BugFix-Accounting.aw_f4_account_payment_payments`</details> |
| `project_no_bill` | Project No Bill | many2one → `project.project` | Read-only mirror of the 'Project No Bill' field on the payment's journal entry (related to `move_id.project_no_bill`); stored copy kept in sync by Odoo. | related `move_id.project_no_bill`; stored | `account.move.project_no_bill`<br>`account.payment.move_id` (account)<br>`model project.project` (project) |  |
| `project_no_issue` | Project No Issue | many2one → `project.project` | Read-only mirror of the 'Project No Issue' field on the payment's journal entry (related to `move_id.project_no_issue`); stored copy kept in sync by Odoo. Also read by the payment's 'Update Project No in Journal Entry' automation. | related `move_id.project_no_issue`; stored | `account.move.project_no_issue`<br>`account.payment.move_id` (account)<br>`model project.project` (project) | `server action BugFix-Accounting.action_account_payment_update_project_no_in_journal_entry`<br>`server action BugFix-Accounting.action_update_project_no_in_journal_entry` |
| `project_no_settle` | Project No Settle | many2one → `project.project` | Read-only mirror of the 'Project No Settle' field on the payment's journal entry (related to `move_id.project_no_settle`); stored copy kept in sync by Odoo. | related `move_id.project_no_settle`; stored | `account.move.project_no_settle`<br>`account.payment.move_id` (account)<br>`model project.project` (project) |  |
| `project_no_settle_1` | Project No Settle | many2one → `project.project` | Non-stored placeholder copied from the same-named Journal Entry field ('Project No Settle'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored | `model project.project` (project) |  |
| `accounting_purchase_id` | Purchase Order | many2one → `purchase.order` | Read-only mirror of the 'Purchase Order' field on the payment's journal entry (related to `move_id.accounting_purchase_id`); not stored. | related `move_id.accounting_purchase_id`; not stored | `account.move.accounting_purchase_id`<br>`account.payment.move_id` (account)<br>`model purchase.order` (purchase) |  |
| `purchase_order` | Purchase Order | many2one → `purchase.order` | Purchase order an advance payment is made against; filters the 'Advance Payments' window action. | stored | `model purchase.order` (purchase) | `view BugFix-Accounting.view_account_payment_form_inherit`<br>`window action BugFix-Accounting.action_advance_payments_2`<br>`window action BugFix-Accounting.action_advance_payments`<br>`window action BugFix-Accounting.aw_f4_account_payment_advance_payments` |
| `purchase_type` | PR Type | selection | Read-only mirror of the 'PR Type' field on the payment's journal entry (related to `move_id.purchase_type`); stored copy kept in sync by Odoo. | related `move_id.purchase_type`; stored | `account.move.purchase_type`<br>`account.payment.move_id` (account) |  |
| `quotation_type` | Quotation Type | selection: Sales=Sales; Project=Project; Repair=Repair | Type of the related quotation (Sales, Project or Repair), shown on the payment form. When 'Repair', the 'RR - Validate Payment %' automation blocks draft payments below the minimum advance percentage. Python declares an empty selection; options come from seeded selection rows. | stored |  | `account.payment._compute_payment_validation()`<br>`account.payment._fix_repair_onchange_validate_advance_pct()` (Fix-repair)<br>`server action BugFix-Accounting.action_account_payment_rr_validate_payment`<br>`server action BugFix-Accounting.action_rr_validate_payment`<br>`view BugFix-Accounting.view_account_payment_form_inherit` |
| `related_field_1JsOz` | New Related Field | boolean | Non-stored placeholder copied from the same-named Journal Entry field ('New Related Field'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `related_field_7SPn1` | New Related Field | boolean | Non-stored placeholder copied from the same-named Journal Entry field ('New Related Field'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `related_field_DBwI2` | New Related Field | selection | Non-stored placeholder copied from the same-named Journal Entry field ('New Related Field'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `related_field_QgLxV` | New Related Field | boolean | Non-stored placeholder copied from the same-named Journal Entry field ('New Related Field'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `related_field_T4rIR` | New Related Field | selection | Non-stored placeholder copied from the same-named Journal Entry field ('New Related Field'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `related_field_VMbnh` | New Related Field | boolean | Non-stored placeholder copied from the same-named Journal Entry field ('New Related Field'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `related_field_bRYM3` | New Related Field | selection | Non-stored placeholder copied from the same-named Journal Entry field ('New Related Field'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `related_field_m4xKC` | New Related Field | selection | Non-stored placeholder copied from the same-named Journal Entry field ('New Related Field'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `related_field_nIq3I` | New Related Field | selection | Non-stored placeholder copied from the same-named Journal Entry field ('New Related Field'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `related_field_nQx1u` | New Related Field | boolean | Non-stored placeholder copied from the same-named Journal Entry field ('New Related Field'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `related_field_pSJXo` | New Related Field | char | Non-stored placeholder copied from the same-named Journal Entry field ('New Related Field'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `related_field_v5UEx` | New Related Field | boolean | Non-stored placeholder copied from the same-named Journal Entry field ('New Related Field'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `related_field_w1zkr` | New Related Field | selection | Non-stored placeholder copied from the same-named Journal Entry field ('New Related Field'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `related_field_yj3hQ` | New Related Field | selection | Non-stored placeholder copied from the same-named Journal Entry field ('New Related Field'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `report_type_s_cust_aging` | Report Type (S - Cust Aging) | many2one → `sales_report_type` | Read-only mirror of the Customer Aging report type on the payment's journal entry (related to `move_id`); not stored. | related `move_id.report_type_s_cust_aging`; not stored | `account.move.report_type_s_cust_aging` (Jinasena_Masterdata_Reporting)<br>`account.payment.move_id` (account)<br>`model sales_report_type` (Jinasena_Masterdata_Reporting) |  |
| `rug_acc_updated` | RUG Account Updated | boolean | Read-only mirror of the 'RUG Account Updated' field on the payment's journal entry (related to `move_id.rug_acc_updated`); stored copy kept in sync by Odoo. | related `move_id.rug_acc_updated`; stored | `account.move.rug_acc_updated`<br>`account.payment.move_id` (account) |  |
| `rug_confirmed` | RUG Confirmed | boolean | Read-only mirror of the 'RUG Confirmed' field on the payment's journal entry (related to `move_id.rug_confirmed`); stored copy kept in sync by Odoo. | related `move_id.rug_confirmed`; stored | `account.move.rug_confirmed`<br>`account.payment.move_id` (account) |  |
| `rug_rejected` | RUG Rejected | boolean | Read-only mirror of the 'RUG Rejected' field on the payment's journal entry (related to `move_id.rug_rejected`); stored copy kept in sync by Odoo. | related `move_id.rug_rejected`; stored | `account.move.rug_rejected`<br>`account.payment.move_id` (account) |  |
| `sale_id` | Sale_Id | many2one → `sale.order` | Read-only mirror of the 'Sale_Id' field on the payment's journal entry (related to `move_id.sale_id`); not stored. | related `move_id.sale_id`; not stored | `account.move.sale_id`<br>`account.payment.move_id` (account)<br>`model sale.order` (sale) |  |
| `sales_order` | Sales Order | many2one → `sale.order` | Sales order this customer payment/advance is for, chosen by the user. Drives Payment Validation and the 'RR - Validate Payment %' check that a Repair advance meets the company's minimum advance percentage of the order total. | stored | `model sale.order` (sale) | `account.payment._compute_payment_validation()`<br>`account.payment._fix_repair_onchange_validate_advance_pct()` (Fix-repair)<br>`server action BugFix-Accounting.action_account_payment_rr_validate_payment`<br>`server action BugFix-Accounting.action_rr_validate_payment`<br>`view BugFix-Accounting.view_account_payment_form_inherit`<details><summary>+2 more</summary>`window action BugFix-Accounting.action_payments_3`<br>`window action BugFix-Accounting.action_payments`</details> |
| `selection_field_5Gimk` | New Selection | selection | Non-stored placeholder copied from the same-named Journal Entry field ('New Selection'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `selection_field_KlNrV` | New Selection | selection | Non-stored placeholder copied from the same-named Journal Entry field ('New Selection'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `selection_field_N6ihz` | New Selection | selection | Non-stored placeholder copied from the same-named Journal Entry field ('New Selection'); it has no related path or compute, so it is always empty on payments (it hides the entry's value) and no view or logic in this repo uses it. | not stored |  |  |
| `supplier_invoice_number` | XXX Supplier's Invoice Number (Bill Reference) | char | Read-only mirror of the 'XXX Supplier's Invoice Number (Bill Reference)' field on the payment's journal entry (related to `move_id.supplier_invoice_number`); stored copy kept in sync by Odoo. | related `move_id.supplier_invoice_number`; stored | `account.move.supplier_invoice_number`<br>`account.payment.move_id` (account) |  |
| `test_type` | Test Type | selection | Read-only mirror of the 'Test Type' field on the payment's journal entry (related to `move_id.test_type`); stored copy kept in sync by Odoo. | related `move_id.test_type`; stored | `account.move.test_type`<br>`account.payment.move_id` (account) |  |
| `tp_id` | Created From TP Invoice | many2one → `tp_invoice_header` | Read-only mirror of the 'Created From TP Invoice' field on the payment's journal entry (related to `move_id.tp_id`); stored copy kept in sync by Odoo. | related `move_id.tp_id`; stored | `account.move.tp_id`<br>`account.payment.move_id` (account)<br>`model tp_invoice_header` |  |
| `tp_invoice_no` | TP Invoice No | many2one → `tp_invoice_header` | TP invoice the payment relates to, entered on the payment form. | stored | `model tp_invoice_header` | `view BugFix-Accounting.view_account_payment_form_inherit` |
| `type` | Type | selection: General=General; Advance Payment=Advance Payment | Payment type: General or Advance Payment (default from ir.default). Copied to the journal entry by the project-number automation and used by the advance payment account update. Stored separately from the journal entry's Type. | stored |  | `default BugFix-Accounting.default_account_payment_type`<br>`server action BugFix-Accounting.action_account_payment_update_project_no_in_journal_entry`<br>`server action BugFix-Accounting.action_update_project_no_in_journal_entry`<br>`server action BugFix-Accounting.action_project_update_advance_payment_account`<br>`server action BugFix-Accounting.srv_advance_payment_acc_update`<details><summary>+1 more</summary>`view BugFix-Accounting.view_account_payment_form_inherit`</details> |
| `update_consignment` | Update Consignment | boolean | Read-only mirror of the 'Update Consignment' field on the payment's journal entry (related to `move_id.update_consignment`); stored copy kept in sync by Odoo. | related `move_id.update_consignment`; stored | `account.move.update_consignment`<br>`account.payment.move_id` (account) |  |
| `valid_lines` | Valid Lines | boolean | Read-only mirror of the 'Valid Lines' field on the payment's journal entry (related to `move_id.valid_lines`); stored copy kept in sync by Odoo. | related `move_id.valid_lines`; stored | `account.move.valid_lines`<br>`account.payment.move_id` (account) |  |
| `created_from_vendor_bill_1__account_move_count` | Created From Vendor Bill count | integer | Read-only mirror of the 'Created From Vendor Bill count' field on the payment's journal entry (related to `move_id.created_from_vendor_bill_1__account_move_count`); stored copy kept in sync by Odoo. | related `move_id.created_from_vendor_bill_1__account_move_count`; stored | `account.move.created_from_vendor_bill_1__account_move_count`<br>`account.payment.move_id` (account) |  |
| `created_from_vendor_bill__account_move_count` | Created From Vendor Bill count | integer | Read-only mirror of the 'Created From Vendor Bill count' field on the payment's journal entry (related to `move_id.created_from_vendor_bill__account_move_count`); stored copy kept in sync by Odoo. | related `move_id.created_from_vendor_bill__account_move_count`; stored | `account.move.created_from_vendor_bill__account_move_count`<br>`account.payment.move_id` (account) |  |

**Python methods (1):**

| Method | Function | Decorators | Extends standard | Depends on | Used by | Where |
|---|---|---|---|---|---|---|
| `_compute_payment_validation` | Compute for Payment Validation: True when the payment is linked to a sales order and its amount is greater than 0 (simplified port of the Studio logic). | api.depends('quotation_type', 'sales_order', 'amount') |  | `account.payment.amount` (account)<br>`account.payment.payment_validation`<br>`account.payment.quotation_type` (BugFix-Sales)<br>`account.payment.sales_order` (BugFix-Sales) | `account.payment.payment_validation` | `models/account_payment.py:130` |

**Server actions (9):**

- **Execute Code** (`action_rr_validate_payment`, type `code`)
  - Function: Run by the RR Validate Payment automation: for draft Repair payments, blocks if this plus posted SO payments are below the company's Advance Payment % of the SO total.
  - Depends on: `account.payment.amount` (account), `account.payment.company_id` (account), `account.payment.state` (account), `account.payment.quotation_type` (BugFix-Sales), `account.payment.sales_order` (BugFix-Sales)<details><summary>+1 more</summary>`model account.payment` (account)</details>
  - Used by: `automation BugFix-Accounting.automation_rr_validate_payment_2`
  <details><summary>code (17 lines)</summary>

```python
# bugfix_sales:config-cutover-v22
if record.state == "draft":
    if record.quotation_type == "Repair":
        sum_total = 0
        so_value = 0
        payment = env["account.payment"].search(
            [
                ("sales_order", "=", record.sales_order.id),
                ("state", "=", "posted"),
            ]
        )
        if payment:
            for total in payment:
                sum_total += total.amount

        min_magin = record.company_id
        if min_magin:
            so_value = round(
                record.sales_order.amount_total
                * (min_magin.advance_payment_ / 100),
                2,
            )

        if so_value > (record.amount + sum_total):
            raise UserError("Payment is not within the minimum precentage.")
```
  </details>
- **Execute Code** (`action_update_project_no_in_journal_entry`, type `code`)
  - Function: Run by the automation on payments: when Project No 1 is set, writes it as Project No and Project No Issue, Journal Type 'Payment' and Type onto the payment's journal entry.
  - Depends on: `account.payment.journal_type`, `account.payment.project_no_1`, `account.payment.project_no_issue`, `account.payment.project_no`, `account.payment.type`<details><summary>+2 more</summary>`model account.move` (account), `model account.payment` (account)</details>
  - Used by: `automation BugFix-Accounting.automation_update_project_no_in_journal_entry_2`
  <details><summary>code (5 lines)</summary>

```python
if record.project_no_1 != False:
    journal_entry = env["account.move"].search(
        [("payment_id", "=", record.id)], limit=1
    )
    if journal_entry:
        journal_entry.write(
            {
                "project_no": record.project_no_1.id,
                "journal_type": "Payment",
                "project_no_issue": record.project_no_1.id,
                "type": record.type,
            }
        )
```
  </details>
- **IMP - Update LC Status to Paid - 2** (`action_imp_update_lc_status_to_paid_2`, type `code`)
  - Function: When a payment linked to a Posted LC is posted, marks the LC as Paid and stores the payment amount converted by the currency rate as Paid Amount (LCY). Searches res.currency on a non-existent 'date' field, which may error.
  - Depends on: `account.payment.amount` (account), `account.payment.currency_id` (account), `account.payment.state` (account), `account.payment.lc_no_1`, `model account.payment` (account)<details><summary>+2 more</summary>`model res.currency` (base), `model lc_header`</details>
  - Used by: `automation BugFix-Accounting.base_automation_73_imp_update_lc_status_to_paid_2`
  <details><summary>code (12 lines)</summary>

```python
if record.state == "posted":
    amount_lcy = 0.00
    if record.lc_no_1 != False:
        lc_lines = env["lc_header"].search(
            [
                ("id", "=", record.lc_no_1.id),
                ("status", "=", "Posted"),
            ],
            limit=1,
        )
        if lc_lines:
            currency = env["res.currency"].search(
                [
                    ("id", "=", record.currency_id.id),
                    ("date", "<=", datetime.datetime.now().date()),
                    ("active", "=", True),
                ],
                limit=1,
            )
            if currency:
                amount_lcy = round((record.amount * currency.rate), 2)
            else:
                amount_lcy = record.amount

            lc_lines.write(
                {
                    "status": "Paid",
                    "selection_field_yo4qM": "Paid",
                    "paid_amount_lcy": amount_lcy,
                }
            )
```
  </details>
- **Post Payments** (`action_post_payments`, type `code`)
  - Function: Posts (validates) all selected payments by calling `action_post`.
  - Depends on: `model account.payment` (account)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (2 lines)</summary>

```python
records.action_post()
```
  </details>
- **Print Checks** (`action_print_checks`, type `code`)
  - Function: Prints checks for the selected payments using Odoo's standard check printing action.
  - Depends on: `model account.payment` (account)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (3 lines)</summary>

```python
if records:
    action = records.print_checks()
```
  </details>
- **Project - Update Advance Payment Account** (`srv_advance_payment_acc_update`, type `code`)
  - Function: Payment button for Advance Payment type: moves the debit (inbound) or credit (outbound) line of the payment's journal entry to the configured advance payment account for Sales or Purchases and sets Advance Payment Acc Updated; errors if not configured.
  - Depends on: `account.payment.partner_type` (account), `account.payment.payment_type` (account), `account.payment.advance_payment_acc_updated`, `account.payment.type`, `model account.move.line` (account)<details><summary>+3 more</summary>`model account.move` (account), `model account.payment` (account), `model advance_payment_acco`</details>
  - Used by: `view BugFix-Accounting.view_account_payment_form_inherit`
  <details><summary>code (50 lines)</summary>

```python
if record.type == "Advance Payment":
    account = env["advance_payment_acco"].search([("id", "=", 1)], limit=1)
    if account:
        if record.partner_type == "customer":
            if account.advance_payment_account_sales == False:
                raise UserError(
                    "Advance Payment Account (Sales) must be Specified in Accounting Configuration"
                )

            journal_entry = env["account.move"].search(
                [("payment_id", "=", record.id)], limit=1
            )
            if journal_entry:
                if record.payment_type == "inbound":
                    lines = env["account.move.line"].search(
                        [("move_id", "=", journal_entry.id), ("debit", ">", 0)], limit=1
                    )
                    if lines:
                        lines.write(
                            {
                                "account_id": account.advance_payment_account_sales.id
                            }
                        )
                        record.write({"advance_payment_acc_updated": True})
                    else:
                        raise UserError("There is no payment line to update.")
                else:
                    lines = env["account.move.line"].search(
                        [("move_id", "=", journal_entry.id), ("credit", ">", 0)],
                        limit=1,
                    )
                    if lines:
                        lines.write(
                            {
                                "account_id": account.advance_payment_account_sales.id
                            }
                        )
                        record.write({"advance_payment_acc_updated": True})
                    else:
                        raise UserError("There is no payment line to update.")
            else:
                raise UserError("There is no payment to update.")
        else:
            if account.advance_payment_account_purchases_1 == False:
                raise UserError(
                    "Advance Payment Account (Purchases) must be Specified in Accounting Configuration"
                )

            journal_entry = env["account.move"].search(
                [("payment_id", "=", record.id)], limit=1
            )
            if journal_entry:
                if record.payment_type == "inbound":
                    lines = env["account.move.line"].search(
                        [("move_id", "=", journal_entry.id), ("debit", ">", 0)], limit=1
                    )
                    if lines:
                        lines.write(
                            {
                                "account_id": account.advance_payment_account_purchases_1.id
                            }
                        )
                        record.write({"advance_payment_acc_updated": True})
                    else:
                        raise UserError("There is no payment line to update.")
                else:
                    lines = env["account.move.line"].search(
                        [("move_id", "=", journal_entry.id), ("credit", ">", 0)],
                        limit=1,
                    )
                    if lines:
                        lines.write(
                            {
                                "account_id": account.advance_payment_account_purchases_1.id
                            }
                        )
                        record.write({"advance_payment_acc_updated": True})
                    else:
                        raise UserError("There is no payment line to update.")
            else:
                raise UserError("There is no payment to update.")
    else:
        raise UserError(
            "Advance Payment Accounts have not been setup in Accounting Configuration"
        )
```
  </details>
- **Project - Update Advance Payment Account** (`action_project_update_advance_payment_account`, type `code`)
  - Function: For Advance Payment type payments: moves the debit (inbound) or credit (outbound) line of the payment's journal entry to the configured Sales or Purchases advance payment account and sets Advance Payment Acc Updated.
  - Depends on: `account.payment.partner_type` (account), `account.payment.payment_type` (account), `account.payment.advance_payment_acc_updated`, `account.payment.type`, `model account.move.line` (account)<details><summary>+3 more</summary>`model account.move` (account), `model account.payment` (account), `model advance_payment_acco`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (49 lines)</summary>

```python
if record.type == "Advance Payment":
    account = env["advance_payment_acco"].search([("id", "=", 1)], limit=1)
    if account:
        if record.partner_type == "customer":
            if account.advance_payment_account_sales == False:
                raise UserError(
                    "Advance Payment Account (Sales) must be Specified in Accounting Configuration"
                )

            journal_entry = env["account.move"].search(
                [("payment_id", "=", record.id)], limit=1
            )
            if journal_entry:
                if record.payment_type == "inbound":
                    lines = env["account.move.line"].search(
                        [("move_id", "=", journal_entry.id), ("debit", ">", 0)], limit=1
                    )
                    if lines:
                        lines.write(
                            {
                                "account_id": account.advance_payment_account_sales.id
                            }
                        )
                        record.write({"advance_payment_acc_updated": True})
                    else:
                        raise UserError("There is no payment line to update.")
                else:
                    lines = env["account.move.line"].search(
                        [("move_id", "=", journal_entry.id), ("credit", ">", 0)],
                        limit=1,
                    )
                    if lines:
                        lines.write(
                            {
                                "account_id": account.advance_payment_account_sales.id
                            }
                        )
                        record.write({"advance_payment_acc_updated": True})
                    else:
                        raise UserError("There is no payment line to update.")
            else:
                raise UserError("There is no payment to update.")
        else:
            if account.advance_payment_account_purchases_1 == False:
                raise UserError(
                    "Advance Payment Account (Purchases) must be Specified in Accounting Configuration"
                )

            journal_entry = env["account.move"].search(
                [("payment_id", "=", record.id)], limit=1
            )
            if journal_entry:
                if record.payment_type == "inbound":
                    lines = env["account.move.line"].search(
                        [("move_id", "=", journal_entry.id), ("debit", ">", 0)], limit=1
                    )
                    if lines:
                        lines.write(
                            {
                                "account_id": account.advance_payment_account_purchases_1.id
                            }
                        )
                        record.write({"advance_payment_acc_updated": True})
                    else:
                        raise UserError("There is no payment line to update.")
                else:
                    lines = env["account.move.line"].search(
                        [("move_id", "=", journal_entry.id), ("credit", ">", 0)],
                        limit=1,
                    )
                    if lines:
                        lines.write(
                            {
                                "account_id": account.advance_payment_account_purchases_1.id
                            }
                        )
                        record.write({"advance_payment_acc_updated": True})
                    else:
                        raise UserError("There is no payment line to update.")
            else:
                raise UserError("There is no payment to update.")
    else:
        raise UserError(
            "Advance Payment Accounts have not been setup in Accounting Configuration"
        )
```
  </details>
- **RR - Validate Payment %** (`action_account_payment_rr_validate_payment`, type `code`)
  - Function: For draft Repair-type payments, blocks with 'Payment is not within the minimum percentage' if this payment plus posted payments on the sales order are below the company's Advance Payment % of the SO total.
  - Depends on: `account.payment.amount` (account), `account.payment.company_id` (account), `account.payment.state` (account), `account.payment.quotation_type` (BugFix-Sales), `account.payment.sales_order` (BugFix-Sales)<details><summary>+1 more</summary>`model account.payment` (account)</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (16 lines)</summary>

```python
# bugfix_sales:config-cutover-v22
if record.state == "draft":
    if record.quotation_type == "Repair":
        sum_total = 0
        so_value = 0
        payment = env["account.payment"].search(
            [
                ("sales_order", "=", record.sales_order.id),
                ("state", "=", "posted"),
            ]
        )
        if payment:
            for total in payment:
                sum_total += total.amount

        min_magin = record.company_id
        if min_magin:
            so_value = round(
                record.sales_order.amount_total
                * (min_magin.advance_payment_ / 100),
                2,
            )

        if so_value > (record.amount + sum_total):
            raise UserError("Payment is not within the minimum precentage.")
```
  </details>
- **Update Project No in Journal Entry** (`action_account_payment_update_project_no_in_journal_entry`, type `code`)
  - Function: When the payment has Project No 1, writes it as Project No and Project No Issue (with Journal Type 'Payment' and Type) on the payment's journal entry.
  - Depends on: `account.payment.journal_type`, `account.payment.project_no_1`, `account.payment.project_no_issue`, `account.payment.project_no`, `account.payment.type`<details><summary>+2 more</summary>`model account.move` (account), `model account.payment` (account)</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (4 lines)</summary>

```python
if record.project_no_1 != False:
    journal_entry = env["account.move"].search(
        [("payment_id", "=", record.id)], limit=1
    )
    if journal_entry:
        journal_entry.write(
            {
                "project_no": record.project_no_1.id,
                "journal_type": "Payment",
                "project_no_issue": record.project_no_1.id,
                "type": record.type,
            }
        )
```
  </details>
**Automations (6):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| IMP - Update LC Status to Paid - 2 | `automation_73_imp_update_lc_status_to_paid_2` |  | When a record is created or updated on account.payment, runs nothing (no action linked). | `model account.payment` (account) |  |
| IMP - Update LC Status to Paid - 2 | `base_automation_73_imp_update_lc_status_to_paid_2` |  | When a record is created or updated on account.payment, runs _IMP - Update LC Status to Paid - 2_. | `model account.payment` (account)<br>`server action BugFix-Accounting.action_imp_update_lc_status_to_paid_2` |  |
| RR - Validate Payment % | `automation_rr_validate_payment` |  | When a watched field changes in the form on account.payment, runs nothing (no action linked). | `model account.payment` (account) |  |
| RR - Validate Payment % | `automation_rr_validate_payment_2` |  | When a watched field changes in the form on account.payment, runs _Execute Code_. | `account.payment.amount` (account)<br>`model account.payment` (account)<br>`server action BugFix-Accounting.action_rr_validate_payment` |  |
| Update Project No in Journal Entry | `automation_update_project_no_in_journal_entry` |  | When a record is created or updated on account.payment, runs nothing (no action linked). | `model account.payment` (account) |  |
| Update Project No in Journal Entry | `automation_update_project_no_in_journal_entry_2` |  | When a record is created or updated on account.payment, runs _Execute Code_. | `model account.payment` (account)<br>`server action BugFix-Accounting.action_update_project_no_in_journal_entry` |  |

**Window actions (11):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Advance Payments | `aw_f4_account_payment_advance_payments` | Opens **account.payment** records (tree,form), filtered to `[('purchase_order', '=', active_id)]`. | `account.payment.purchase_order`<br>`model account.payment` (account) |  |
| Advance Payments | `action_advance_payments` | Opens **account.payment** records (tree,form), filtered to `[('purchase_order', '=', active_id)]`. | `account.payment.purchase_order`<br>`model account.payment` (account) |  |
| Advance Payments | `action_advance_payments_2` | Opens **account.payment** records (tree,form), filtered to `[('purchase_order', '=', active_id)]`. | `account.payment.purchase_order`<br>`model account.payment` (account) | `view BugFix-Purchase.view_purchase_order_form_inherit` (BugFix-Purchase) |
| Payments | `aw_f4_account_payment_payments` | Opens **account.payment** records (tree,form), filtered to `[('project_no_1', '=', active_id)]`. | `account.payment.project_no_1`<br>`model account.payment` (account) |  |
| Payments | `action_payments` | Opens **account.payment** records (tree,form), filtered to `[('sales_order', '=', active_id)]`. | `account.payment.sales_order` (BugFix-Sales)<br>`model account.payment` (account) |  |
| Payments | `action_payments_2` | Opens **account.payment** records (tree,form), filtered to `[('project_no_1', '=', active_id)]`. | `account.payment.project_no_1`<br>`model account.payment` (account) |  |
| Payments | `action_payments_3` | Opens **account.payment** records (tree,form), filtered to `[('sales_order', '=', active_id)]`. | `account.payment.sales_order` (BugFix-Sales)<br>`model account.payment` (account) | `view BugFix-Accounting.view_ported_sale_ord_acct` |
| Payments | `action_payments_4` | Opens **account.payment** records (tree,form), filtered to `[('project_no_1', '=', active_id)]`. | `account.payment.project_no_1`<br>`model account.payment` (account) |  |
| account.payment | `aw_f4_account_payment_account_payment` | Opens **account.payment** records (kanban,tree,form,graph). | `model account.payment` (account) |  |
| account.payment | `action_account_payment` | Opens **account.payment** records (kanban,tree,form,graph). | `model account.payment` (account) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_account_payment` (BugFix-Studio-Misc) |
| account.payment | `action_account_payment_2` | Opens **account.payment** records (kanban,tree,form,graph). | `model account.payment` (account) |  |

**Views (2):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: account.payment.form customization | `view_account_payment_form_inherit` | form | after `//button[@name='action_void_check']`: add button 'Update Advance Payment Account'; set invisible=(state != 'draft') or ((advance_payment_acc_updated == False) and (type == 'Advance Payment')) on `//button[@name='action_post']`; after `//field[@name='payment_method_line_id']`: add field type; after `//form[1]/sheet[1]/group[1]/group[@name='group2']/field[@name='partner_bank_id']`: add field sales_order, field project_no_1, field created_from_project_1, field lc_no_1, field purchase_order, field tp_invoice_no, field payment_validation; after `//field[@name='payment_transaction_id']`: add field quotation_type, field payment_validation_1, field advance_payment_acc_updated | Payment form customization: adds a Type field and an 'Update Advance Payment Account' button (shown for Advance Payments not yet updated), hides Confirm until that update is done, and adds Sales Order, Project No, LC No, Purchase Order, TP invoice and validation fields. | `account.payment.partner_id` (account)<br>`account.payment.state` (account)<br>`account.payment.advance_payment_acc_updated`<br>`account.payment.created_from_project_1`<br>`account.payment.lc_no_1`<details><summary>+10 more</summary>`account.payment.payment_validation_1`<br>`account.payment.payment_validation`<br>`account.payment.project_no_1`<br>`account.payment.purchase_order`<br>`account.payment.quotation_type` (BugFix-Sales)<br>`account.payment.sales_order` (BugFix-Sales)<br>`account.payment.tp_invoice_no`<br>`account.payment.type`<br>`server action BugFix-Accounting.srv_advance_payment_acc_update`<br>`view account.view_account_payment_form` (account)</details> |  |
| Odoo Studio: account.payment.tree customization | `view_account_payment_tree_inherit` | tree | after `//field[@name='date']`: add field ref; after `//field[@name='currency_id']`: add field id, field has_reconciled_entries, field reconciled_statement_lines_count, field is_reconciled, field reconciled_invoices_count, field reconciled_bills_count, field reconciled_invoice_ids, field move_id, field invoice_line_ids; after `//field[@name='state']`: add field create_uid | Payments list: adds Reference after Date, Created By after Status, and after Currency a set of technical columns (ID, reconciliation flags and counts, reconciled invoices, journal entry, invoice lines). | `account.payment.has_reconciled_entries` (account)<br>`account.payment.invoice_line_ids` (account)<br>`account.payment.is_reconciled` (account)<br>`account.payment.move_id` (account)<br>`account.payment.reconciled_bills_count` (account)<details><summary>+5 more</summary>`account.payment.reconciled_invoice_ids` (account)<br>`account.payment.reconciled_invoices_count` (account)<br>`account.payment.reconciled_statement_lines_count` (account)<br>`account.payment.ref` (account)<br>`view account.view_account_payment_tree` (account)</details> |  |

**Reports (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Jinasena Payment Receipt | `action_report_payment_receipt` | Prints **Jinasena Payment Receipt** (qweb-pdf) for account.payment records using template `BugFix-Accounting.report_payment_receipt`; listed in the Print menu. | `model account.payment` (account)<br>`view BugFix-Accounting.report_payment_receipt` |  |
| account.payment Report | `action_report_account_payment_1` | Prints **account.payment Report** (qweb-pdf) for account.payment records using template `BugFix-Accounting.report_account_payment_1`; listed in the Print menu. | `model account.payment` (account)<br>`view BugFix-Accounting.report_account_payment_1` |  |
| account.payment Report | `action_report_account_payment_2` | Prints **account.payment Report** (qweb-pdf) for account.payment records using template `BugFix-Accounting.report_account_payment_2`; listed in the Print menu. | `model account.payment` (account)<br>`view BugFix-Accounting.report_account_payment_2` |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Account payment company rule | `rule_91_account_payment_company_rule` | For everyone (global rule): read/write/create/delete on account.payment only where `[('company_id', 'in', company_ids)]`. | `account.payment.company_id` (account)<br>`model account.payment` (account) |  |
