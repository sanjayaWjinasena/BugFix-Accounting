# BugFix-Accounting — `x_tp_invoice_header`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_tp_invoice_header` — TP Invoice Header

*Created by this repo.* Python: `models/x_tp_invoice_header.py`, `models/x_tp_invoice_header_gap.py`. Record name field: `x_name`.

Other repos that use this model: `access right BugFix-Studio-Misc.access_g_x_tp_invoice_header_x_tp_invoice_header_purchase_jin_po_invoicing_payment_import` (BugFix-Studio-Misc)<br>`server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:x_tp_invoice_header -->
A third-party (TP) invoice for charges on an import consignment, created from the consignment through the Create TP Invoice wizard, with vendor, currency, supplier invoice number and date and charge lines. Untaxed amount, taxes, total and total original amount are computed from the lines, and a smart button opens the related vendor bills. Automations assign the number from the 'tp.invoice.seq' sequence and set the currency to the vendor's purchase currency. The 'Post TP Invoice' button validates the invoice and the Imports Ledger Setup, adjusts stock valuation for amount differences, creates and posts a vendor bill and sets the status to Posted.
<!-- /SUMMARY -->

**Fields (35):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard computed field: calendar meeting linked to the next activity on this TP Invoice Header record, if any. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard computed field: due date of the next scheduled activity on this TP Invoice Header record. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard computed flag (Alert or Error) showing that an activity on this TP Invoice Header record is in an exception state. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard computed icon shown when an activity on this TP Invoice Header record is in an exception state. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Scheduled activities (to-dos, calls, meetings) attached to this TP Invoice Header record, from the standard activity mixin. | stored | `model mail.activity` (mail) | `x_tp_invoice_header.activity_summary`<br>`x_tp_invoice_header.activity_type_icon`<br>`x_tp_invoice_header.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard computed activity status of this TP Invoice Header record: Overdue, Today or Planned, based on the nearest activity deadline. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Summary text of the next scheduled activity on this TP Invoice Header record, read via related from its activities. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_tp_invoice_header.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Font Awesome icon of the next activity type on this TP Invoice Header record, read via related from its activities; used for display only. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_tp_invoice_header.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Type of the next scheduled activity on this TP Invoice Header record, read via related from its activities (standard activity mixin). | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_tp_invoice_header.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard computed field: the user responsible for the next scheduled activity on this TP Invoice Header record. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the TP Invoice Header was created (standard audit field); also referenced by the JIN Third Party TP Invoice Seq No automation. | stored |  | `automation BugFix-Accounting.base_automation_65_jin_third_party_tp_invoice_seq_no` |
| `create_uid` | Created by | many2one → `res.users` | User who created the TP Invoice Header record (standard audit field set automatically). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the TP Invoice Header record in lookups and breadcrumbs, computed by Odoo (standard field). | not stored |  |  |
| `id` | ID | integer | Technical unique database ID of the TP Invoice Header record (standard Odoo field). | stored |  |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard computed field: due date of the current user's next activity on this TP Invoice Header record. | not stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time the TP Invoice Header record was last modified (standard audit field). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last modified the TP Invoice Header record (standard audit field set automatically). | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Archive flag of the TP (third-party) invoice; defaults to true (ir.default), and unticked (archived) records are hidden from normal lists. Shown in the form and search views. | stored |  | `default BugFix-Accounting.default_174_x_tp_invoice_header_x_active`<br>`view BugFix-Accounting.ported_default_form_view_fo_b04274bb_8930_4e7e_a2cc_e65229996a48`<br>`view BugFix-Accounting.ported_default_search_view__12511c2f_92e3_4ad8_a81a_9adf7a7e038f`<br>`view BugFix-Accounting.ported_view_3044_default_search_view_12511c2f_92e3_4ad8_a81a_9adf7a7e038f` |
| `x_currency_id` | Currency | many2one → `res.currency` | Currency used to format the monetary totals (total invoice amount, taxes, total) on the TP invoice form; defaults via ir.default to currency database id 145. TP invoice posting logic uses the other Currency field, `x_studio_currency_id`. | stored | `model res.currency` (base) | `default BugFix-Accounting.default_386_x_tp_invoice_header_x_currency_id` |
| `x_name` | Invoice Reference | char | TP invoice reference number. Defaults to "New" and is replaced with the next "tp.invoice.seq" sequence number by the TP Invoice Seq.No automation. Shown in the form, list and search views. | stored |  | `default BugFix-Accounting.default_178_x_tp_invoice_header_x_name`<br>`server action BugFix-Accounting.sa_f5_x_tp_invoice_header_tp_invoice_seq_no`<br>`server action BugFix-Accounting.server_action_1381_tp_invoice_seq_no`<br>`view BugFix-Accounting.ported_default_form_view_fo_b04274bb_8930_4e7e_a2cc_e65229996a48`<br>`view BugFix-Accounting.ported_default_list_view_fo_87762a20_9628_4266_a414_8bb858fd9746`<details><summary>+2 more</summary>`view BugFix-Accounting.ported_default_search_view__12511c2f_92e3_4ad8_a81a_9adf7a7e038f`<br>`view BugFix-Accounting.ported_view_3044_default_search_view_12511c2f_92e3_4ad8_a81a_9adf7a7e038f`</details> |
| `x_studio_con_no` | Created From Consignment No | many2one → `x_consignment_header` | Import consignment this TP invoice was created from. Set by "IMP - Apply Selected Charge Lines to TP Invoice", used by "IMP - Post TP Invoice" and as the filter of the consignment's TP Invoices action. Shown in the form view. | stored | `model x_consignment_header` (BugFix-Stock) | `server action BugFix-Accounting.server_action_1384_imp_post_tp_invoice`<br>`server action BugFix-Accounting.srv_tp_invoice_post`<br>`view BugFix-Accounting.ported_view_3045_odoo_studio_default_fc4d9ef7_2d23_4a16_911c_66cf2185de9b`<br>`window action BugFix-Accounting.action_1383_tp_invoices` |
| `x_studio_currency_id` | Currency | many2one → `res.currency` | Currency of the TP invoice. Defaults to currency id 145, is reset to the vendor's purchase currency by the TP Invoice Currency Update automation, and is required when posting. Shown in the form and list views. | stored | `model res.currency` (base) | `default BugFix-Accounting.default_226_x_tp_invoice_header_x_studio_currency_id`<br>`default BugFix-Accounting.default_427_x_tp_invoice_header_x_studio_currency_id`<br>`server action BugFix-Accounting.sa_f5_x_tp_invoice_header_tp_invoice_currency_update`<br>`server action BugFix-Accounting.server_action_1384_imp_post_tp_invoice`<br>`server action BugFix-Accounting.server_action_2112_tp_invoice_currency_update`<details><summary>+3 more</summary>`server action BugFix-Accounting.srv_tp_invoice_post`<br>`view BugFix-Accounting.ported_view_3045_odoo_studio_default_fc4d9ef7_2d23_4a16_911c_66cf2185de9b`<br>`view BugFix-Accounting.ported_view_3050_odoo_studio_default_c572715b_284c_469b_9b41_7a04b3431fc6`</details> |
| `x_studio_invoice_date` | Supplier's Invoice Date (Bill Date) | date | Supplier's invoice (bill) date, copied from the consignment when the TP invoice is created; posting raises an error if it is empty. Shown in the form and list views. | stored |  | `server action BugFix-Accounting.server_action_1384_imp_post_tp_invoice`<br>`server action BugFix-Accounting.srv_tp_invoice_post`<br>`view BugFix-Accounting.ported_view_3045_odoo_studio_default_fc4d9ef7_2d23_4a16_911c_66cf2185de9b`<br>`view BugFix-Accounting.ported_view_3050_odoo_studio_default_c572715b_284c_469b_9b41_7a04b3431fc6` |
| `x_studio_invoice_no` | Supplier's Invoice No (Bill Reference) | char | Supplier's invoice number (bill reference), copied from the consignment's supplier invoice number on creation; posting raises an error if it is empty. Shown in the form and list views. | stored |  | `server action BugFix-Accounting.server_action_1384_imp_post_tp_invoice`<br>`server action BugFix-Accounting.srv_tp_invoice_post`<br>`view BugFix-Accounting.ported_view_3045_odoo_studio_default_fc4d9ef7_2d23_4a16_911c_66cf2185de9b`<br>`view BugFix-Accounting.ported_view_3050_odoo_studio_default_c572715b_284c_469b_9b41_7a04b3431fc6` |
| `x_studio_name` | Name | char | Vendor's name, copied automatically from the selected Vendor via related field (`x_studio_vendor.name`); shown on the TP Invoice Header form. | related `x_studio_vendor.name`; not stored | `res.partner.name` (base)<br>`x_tp_invoice_header.x_studio_vendor` | `view BugFix-Accounting.ported_view_3045_odoo_studio_default_fc4d9ef7_2d23_4a16_911c_66cf2185de9b` |
| `x_studio_pipeline_status_bar` | Pipeline status bar | selection: Draft=Draft; Posted=Posted | Stage of the third-party invoice (Draft or Posted) shown as a status bar on the form; has a default value and is updated by the Post TP Invoice server actions. | stored |  | `default BugFix-Accounting.default_179_x_tp_invoice_header_x_studio_pipeline_status_bar`<br>`server action BugFix-Accounting.server_action_1384_imp_post_tp_invoice`<br>`server action BugFix-Accounting.srv_tp_invoice_post`<br>`view BugFix-Accounting.ported_view_3045_odoo_studio_default_fc4d9ef7_2d23_4a16_911c_66cf2185de9b` |
| `x_studio_sequence` | Sequence | integer | Sort order of TP Invoice Header records (default 10), used for drag-and-drop ordering in the list view. | default `10`; stored |  | `default BugFix-Accounting.default_175_x_tp_invoice_header_x_studio_sequence`<br>`view BugFix-Accounting.ported_default_list_view_fo_87762a20_9628_4266_a414_8bb858fd9746` |
| `x_studio_status` | Status | selection: Draft=Draft; Posted=Posted | Posting status of the third-party invoice (Draft or Posted); defaults via an ir.default, is set by the Post TP Invoice server actions and is shown on the TP Invoice Header form and list views. | stored |  | `default BugFix-Accounting.default_180_x_tp_invoice_header_x_studio_status`<br>`server action BugFix-Accounting.server_action_1384_imp_post_tp_invoice`<br>`server action BugFix-Accounting.srv_tp_invoice_post`<br>`view BugFix-Accounting.ported_default_form_view_fo_b04274bb_8930_4e7e_a2cc_e65229996a48`<br>`view BugFix-Accounting.ported_view_3045_odoo_studio_default_fc4d9ef7_2d23_4a16_911c_66cf2185de9b`<details><summary>+1 more</summary>`view BugFix-Accounting.ported_view_3050_odoo_studio_default_c572715b_284c_469b_9b41_7a04b3431fc6`</details> |
| `x_studio_taxes_1` | Taxes | monetary | Total tax of the TP invoice, computed as the sum of Tax Amount on all TP Lines; added into Total and used by the Post TP Invoice server actions. | computed by `_compute_x_studio_taxes_1`; not stored | `x_tp_invoice_header._compute_x_studio_taxes_1()` | `server action BugFix-Accounting.server_action_1384_imp_post_tp_invoice`<br>`server action BugFix-Accounting.srv_tp_invoice_post`<br>`view BugFix-Accounting.ported_view_3045_odoo_studio_default_fc4d9ef7_2d23_4a16_911c_66cf2185de9b`<br>`x_tp_invoice_header._compute_x_studio_taxes_1()`<br>`x_tp_invoice_header._compute_x_studio_total_1()` |
| `x_studio_total_1` | Total | monetary | Grand total of the TP invoice, computed as Untaxed Amount plus Taxes. | computed by `_compute_x_studio_total_1`; not stored | `x_tp_invoice_header._compute_x_studio_total_1()` | `view BugFix-Accounting.ported_view_3045_odoo_studio_default_fc4d9ef7_2d23_4a16_911c_66cf2185de9b`<br>`x_tp_invoice_header._compute_x_studio_total_1()` |
| `x_studio_total_invoice_amount` | Untaxed Amount | monetary | Untaxed total of the TP invoice, computed as the sum of Invoice Amount on all TP Lines; feeds the Total field. | computed by `_compute_x_studio_total_invoice_amount`; not stored | `x_tp_invoice_header._compute_x_studio_total_invoice_amount()` | `view BugFix-Accounting.ported_view_3045_odoo_studio_default_fc4d9ef7_2d23_4a16_911c_66cf2185de9b`<br>`x_tp_invoice_header._compute_x_studio_total_1()`<br>`x_tp_invoice_header._compute_x_studio_total_invoice_amount()` |
| `x_studio_total_original_invoice_amount` | Total Original Invoice Amount | float | Sum of Original Amount across all TP Lines; computed and used by the Post TP Invoice server actions. | computed by `_compute_x_studio_total_original_invoice_amount`; not stored | `x_tp_invoice_header._compute_x_studio_total_original_invoice_amount()` | `server action BugFix-Accounting.server_action_1384_imp_post_tp_invoice`<br>`server action BugFix-Accounting.srv_tp_invoice_post`<br>`x_tp_invoice_header._compute_x_studio_total_original_invoice_amount()` |
| `x_studio_tp_lines` | TP Lines | one2many → `x_tp_invoice_line` | Charge lines of this third-party invoice (TP Invoice Line records); their amounts are summed into Untaxed Amount, Taxes and Total Original Invoice Amount. | stored | `model x_tp_invoice_line` | `view BugFix-Accounting.ported_view_3045_odoo_studio_default_fc4d9ef7_2d23_4a16_911c_66cf2185de9b`<br>`x_tp_invoice_header._compute_x_studio_taxes_1()`<br>`x_tp_invoice_header._compute_x_studio_total_invoice_amount()`<br>`x_tp_invoice_header._compute_x_studio_total_original_invoice_amount()` |
| `x_studio_vendor` | Vendor | many2one → `res.partner` | Third-party vendor (partner) the invoice is from, chosen by the user; changing it triggers the TP Invoice Currency Update automation that copies the vendor's purchase currency, and it is used when posting the TP invoice. | stored | `model res.partner` (base) | `automation BugFix-Accounting.base_automation_184_tp_invoice_currency_update`<br>`server action BugFix-Accounting.sa_f5_x_tp_invoice_header_tp_invoice_currency_update`<br>`server action BugFix-Accounting.server_action_1384_imp_post_tp_invoice`<br>`server action BugFix-Accounting.server_action_2112_tp_invoice_currency_update`<br>`server action BugFix-Accounting.srv_tp_invoice_post`<details><summary>+3 more</summary>`view BugFix-Accounting.ported_view_3045_odoo_studio_default_fc4d9ef7_2d23_4a16_911c_66cf2185de9b`<br>`view BugFix-Accounting.ported_view_3050_odoo_studio_default_c572715b_284c_469b_9b41_7a04b3431fc6`<br>`x_tp_invoice_header.x_studio_name`</details> |
| `x_x_studio_tp_id__account_move_count` | Created From TP Invoice count | integer | Number of journal entries/bills whose `x_studio_tp_id` points at this TP invoice, shown on the smart button; returns 0 if that link field is not installed on account.move. | computed by `_compute_x_x_studio_tp_id__account_move_count`; not stored | `x_tp_invoice_header._compute_x_x_studio_tp_id__account_move_count()` | `view BugFix-Accounting.ported_view_3045_odoo_studio_default_fc4d9ef7_2d23_4a16_911c_66cf2185de9b`<br>`x_tp_invoice_header._compute_x_x_studio_tp_id__account_move_count()` |

**Python methods (5):**

| Method | Function | Decorators | Extends standard | Depends on | Used by | Where |
|---|---|---|---|---|---|---|
| `_compute_x_studio_total_invoice_amount` | Compute for Untaxed Amount: sums Invoice Amount over all TP Lines. | api.depends('x_studio_tp_lines', 'x_studio_tp_lines.x_studio_invoice_amount') |  | `x_tp_invoice_header.x_studio_total_invoice_amount`<br>`x_tp_invoice_header.x_studio_tp_lines`<br>`x_tp_invoice_line.x_studio_invoice_amount` | `x_tp_invoice_header.x_studio_total_invoice_amount` | `models/x_tp_invoice_header.py:96` |
| `_compute_x_studio_taxes_1` | Compute for Taxes: sums Tax Amount over all TP Lines. | api.depends('x_studio_tp_lines', 'x_studio_tp_lines.x_studio_taxes', 'x_studio_t… |  | `x_tp_invoice_header.x_studio_taxes_1`<br>`x_tp_invoice_header.x_studio_tp_lines`<br>`x_tp_invoice_line.x_studio_invoice_amount`<br>`x_tp_invoice_line.x_studio_taxes` | `x_tp_invoice_header.x_studio_taxes_1` | `models/x_tp_invoice_header.py:108` |
| `_compute_x_studio_total_1` | Compute for Total: Untaxed Amount plus Taxes. | api.depends('x_studio_total_invoice_amount', 'x_studio_taxes_1') |  | `x_tp_invoice_header.x_studio_taxes_1`<br>`x_tp_invoice_header.x_studio_total_1`<br>`x_tp_invoice_header.x_studio_total_invoice_amount` | `x_tp_invoice_header.x_studio_total_1` | `models/x_tp_invoice_header.py:119` |
| `_compute_x_studio_total_original_invoice_amount` | Compute for Total Original Invoice Amount: sums Original Amount over all TP Lines. | api.depends('x_studio_tp_lines', 'x_studio_tp_lines.x_studio_original_amount') |  | `x_tp_invoice_header.x_studio_total_original_invoice_amount`<br>`x_tp_invoice_header.x_studio_tp_lines`<br>`x_tp_invoice_line.x_studio_original_amount` | `x_tp_invoice_header.x_studio_total_original_invoice_amount` | `models/x_tp_invoice_header.py:129` |
| `_compute_x_x_studio_tp_id__account_move_count` | Compute for the linked-journal-entry count: groups account.move by `x_studio_tp_id` and counts entries per TP invoice; returns 0 if that field is not installed. |  |  | `model account.move` (account)<br>`x_tp_invoice_header.x_x_studio_tp_id__account_move_count` | `x_tp_invoice_header.x_x_studio_tp_id__account_move_count` | `models/x_tp_invoice_header.py:136` |

**Server actions (6):**

- **Execute Code** (`server_action_1381_tp_invoice_seq_no`, type `code`)
  - Function: Run by the TP Invoice Seq No automation: when Name is 'New', assigns the next number from the 'tp.invoice.seq' sequence.
  - Depends on: `model ir.sequence` (base), `model x_tp_invoice_header`, `x_tp_invoice_header.x_name`
  - Used by: `automation BugFix-Accounting.base_automation_65_jin_third_party_tp_invoice_seq_no`
  <details><summary>code (6 lines)</summary>

```python

#record['x_name'] = env['ir.sequence'].next_by_code('purchase.request.seq')

if record.x_name == 'New':
 seq = env['ir.sequence'].next_by_code('tp.invoice.seq')
 record.write({'x_name': seq})
```
  </details>
- **Execute Code** (`server_action_2112_tp_invoice_currency_update`, type `code`)
  - Function: Run when the TP invoice vendor changes: sets Currency to the vendor's purchase currency.
  - Depends on: `model x_tp_invoice_header`, `x_tp_invoice_header.x_studio_currency_id`, `x_tp_invoice_header.x_studio_vendor`
  - Used by: `automation BugFix-Accounting.base_automation_184_tp_invoice_currency_update`
  <details><summary>code (2 lines)</summary>

```python

record['x_studio_currency_id'] = record.x_studio_vendor.property_purchase_currency_id.id
```
  </details>
- **IMP - Post TP Invoice** (`srv_tp_invoice_post`, type `code`)
  - Function: Post TP Invoice button: validates lines, vendor, currency, invoice no/date and Imports Ledger Setup, adjusts stock valuation for amount differences, creates and posts a vendor bill in 'TP Vendor Bills' journal, sets status Posted and opens the bill.
  - Depends on: `model account.journal` (account), `model account.move` (account), `model res.company` (base), `model stock.valuation.layer` (stock_account), `model x_consignment_header` (BugFix-Stock)<details><summary>+12 more</summary>`model x_imports_ledger_setup` (BugFix-Purchase), `model x_tp_invoice_header`, `model x_tp_invoice_line`, `x_tp_invoice_header.x_studio_con_no`, `x_tp_invoice_header.x_studio_currency_id`, `x_tp_invoice_header.x_studio_invoice_date`, `x_tp_invoice_header.x_studio_invoice_no`, `x_tp_invoice_header.x_studio_pipeline_status_bar`, `x_tp_invoice_header.x_studio_status`, `x_tp_invoice_header.x_studio_taxes_1`, `x_tp_invoice_header.x_studio_total_original_invoice_amount`, `x_tp_invoice_header.x_studio_vendor`</details>
  - Used by: `view BugFix-Accounting.ported_default_form_view_fo_b04274bb_8930_4e7e_a2cc_e65229996a48`
  <details><summary>code (150 lines)</summary>

```python

if record.id:
    company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
    company = env['res.company'].browse(company_id)

    invalid_lines = env['x_tp_invoice_line'].search([('x_studio_tp_invoice_header_id', '=', record.id)])
    diff = 0
    diff_found = False
    if invalid_lines:
        for val in invalid_lines:
            if val.x_studio_invoice_amount == 0.0000:
                raise UserError("Invoice Amount of Individual TP Lines Should be Greater than Zero!")
            if val.x_studio_invoice_amount != val.x_studio_original_amount:
                diff_found = True
                diff += (val.x_studio_invoice_amount - val.x_studio_original_amount)

    if record.x_studio_vendor.id == 0:
        raise UserError("Vendor Account must be Specified!")
    if record.x_studio_currency_id.id == 0:
        raise UserError("Currency must be Specified!")
    if record.x_studio_invoice_no == False:
        raise UserError("Invoice No must be Specified!")
    if record.x_studio_invoice_date == False:
        raise UserError("Invoice Date must be Specified!")

    tax_account = env['x_imports_ledger_setup'].search([('x_studio_company_id', '=', company.id)], limit=1)
    if tax_account:
        if tax_account.x_studio_tp_invoicing_tax_acc.id == 0:
            raise UserError('TP Invoicing Tax Account must be Specified in Imports Ledger Setup')
        if tax_account.x_studio_import_tp_vendor_account.id == 0:
            raise UserError('Import TP Vendor Account must be Specified in Imports Ledger Setup')
    else:
        raise UserError('Imports Ledger Setup must be specified for the selected company ')

    tp_lines = []

    if diff_found == True:
        qty = 0
        con_lines = env['x_consignment_header'].search([('id', '=', record.x_studio_con_no.id)])
        if con_lines:
            qty = 1 if diff > 0 else -1

            if tax_account.x_studio_cost_allocation_method == 'by_weight':
                for diff_lines in con_lines.x_studio_consignment_line_ids:
                    tp_lines.append([0, 0, {
                        'product_id': diff_lines.x_studio_product_id.id,
                        'quantity': qty,
                        'currency_id': record.x_studio_currency_id.id,
                        'name': diff_lines.x_studio_product_id.name,
                        'product_uom_id': diff_lines.x_studio_product_id.uom_id.id,
                        'price_unit': abs(diff) * (diff_lines.x_studio_weight / con_lines.x_studio_total_amount_cost_allocation_method),
                        'price_subtotal': (abs(diff) * (diff_lines.x_studio_weight / con_lines.x_studio_total_amount_cost_allocation_method)) * qty,
                        'account_id': diff_lines.x_studio_product_id.categ_id.property_stock_account_input_categ_id.id,
                    }])
                    value_entry = env['stock.valuation.layer'].search([('stock_move_id', '=', diff_lines.x_studio_stock_move_id.id)], limit=1)
                    if value_entry:
                        adj = (abs(diff) * (diff_lines.x_studio_weight / con_lines.x_studio_total_amount_cost_allocation_method)) * qty
                        value_entry.write({
                            'value': value_entry.value + adj,
                            'unit_cost': (value_entry.value + adj) / value_entry.quantity,
                            'remaining_value': (value_entry.value + adj) / value_entry.remaining_qty,
                        })
            elif tax_account.x_studio_cost_allocation_method == 'by_volume':
                for diff_lines in con_lines.x_studio_consignment_line_ids:
                    tp_lines.append([0, 0, {
                        'product_id': diff_lines.x_studio_product_id.id,
                        'quantity': qty,
                        'currency_id': record.x_studio_currency_id.id,
                        'name': diff_lines.x_studio_product_id.name,
                        'product_uom_id': diff_lines.x_studio_product_id.uom_id.id,
                        'price_unit': abs(diff) * (diff_lines.x_studio_volume / con_lines.x_studio_total_amount_cost_allocation_method),
                        'price_subtotal': (abs(diff) * (diff_lines.x_studio_volume / con_lines.x_studio_total_amount_cost_allocation_method)) * qty,
                        'account_id': diff_lines.x_studio_product_id.categ_id.property_stock_account_input_categ_id.id,
                    }])
                    value_entry = env['stock.valuation.layer'].search([('stock_move_id', '=', diff_lines.x_studio_stock_move_id.id)], limit=1)
                    if value_entry:
                        adj = (abs(diff) * (diff_lines.x_studio_volume / con_lines.x_studio_total_amount_cost_allocation_method)) * qty
                        value_entry.write({
                            'value': value_entry.value + adj,
                            'unit_cost': (value_entry.value + adj) / value_entry.quantity,
                            'remaining_value': (value_entry.value + adj) / value_entry.remaining_qty,
                        })
            else:
                for diff_lines in con_lines.x_studio_consignment_line_ids:
                    tp_lines.append([0, 0, {
                        'product_id': diff_lines.x_studio_product_id.id,
                        'quantity': qty,
                        'currency_id': record.x_studio_currency_id.id,
                        'name': diff_lines.x_studio_product_id.name,
                        'product_uom_id': diff_lines.x_studio_product_id.uom_id.id,
                        'price_unit': abs(diff) * (diff_lines.x_studio_amount / con_lines.x_studio_total_amount),
                        'price_subtotal': (abs(diff) * (diff_lines.x_studio_amount / con_lines.x_studio_total_amount)) * qty,
                        'account_id': diff_lines.x_studio_product_id.categ_id.property_stock_account_input_categ_id.id,
                    }])
                    value_entry = env['stock.valuation.layer'].search([('stock_move_id', '=', diff_lines.x_studio_stock_move_id.id)], limit=1)
                    if value_entry:
                        adj = (abs(diff) * (diff_lines.x_studio_amount / con_lines.x_studio_total_amount)) * qty
                        value_entry.write({
                            'value': value_entry.value + adj,
                            'unit_cost': (value_entry.value + adj) / value_entry.quantity,
                            'remaining_value': (value_entry.value + adj) / value_entry.remaining_qty,
                        })

    tp_lines.append([0, 0, {
        'account_id': tax_account.x_studio_import_tp_vendor_account.id,
        'name': 'Import TP Invoice - Reversal',
        'quantity': 1.00,
        'currency_id': record.x_studio_currency_id.id,
        'price_unit': record.x_studio_total_original_invoice_amount,
    }])

    tp_lines.append([0, 0, {
        'account_id': tax_account.x_studio_tp_invoicing_tax_acc.id,
        'name': 'Total Tax',
        'quantity': 1.00,
        'currency_id': record.x_studio_currency_id.id,
        'price_unit': record.x_studio_taxes_1,
    }])

    journal = env['account.journal'].search([('name', '=', 'TP Vendor Bills'), ('company_id', '=', company.id)], limit=1)
# … 30 more lines
```
  </details>
- **IMP - Post TP Invoice** (`server_action_1384_imp_post_tp_invoice`, type `code`)
  - Function: Legacy Post TP Invoice action: validates the TP invoice and Imports Ledger Setup, adjusts stock valuation for amount differences, creates and posts a vendor bill and sets the TP invoice to Posted.
  - Depends on: `model account.journal` (account), `model account.move` (account), `model res.company` (base), `model stock.valuation.layer` (stock_account), `model x_consignment_header` (BugFix-Stock)<details><summary>+12 more</summary>`model x_imports_ledger_setup` (BugFix-Purchase), `model x_tp_invoice_header`, `model x_tp_invoice_line`, `x_tp_invoice_header.x_studio_con_no`, `x_tp_invoice_header.x_studio_currency_id`, `x_tp_invoice_header.x_studio_invoice_date`, `x_tp_invoice_header.x_studio_invoice_no`, `x_tp_invoice_header.x_studio_pipeline_status_bar`, `x_tp_invoice_header.x_studio_status`, `x_tp_invoice_header.x_studio_taxes_1`, `x_tp_invoice_header.x_studio_total_original_invoice_amount`, `x_tp_invoice_header.x_studio_vendor`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (139 lines)</summary>

```python
if record.id:
  company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
  company = env['res.company'].browse(company_id)
  
  invalid_lines = env['x_tp_invoice_line'].search([('x_studio_tp_invoice_header_id', '=', record.id)])
  if invalid_lines:
    diff = 0
    diff_found = False
    for val in invalid_lines:
      if val.x_studio_invoice_amount == 0.0000:
        raise UserError("Invoice Amount of Individual TP Lines Should be Greater than Zero!")
        
      if val.x_studio_invoice_amount != val.x_studio_original_amount:
        diff_found = True
        diff += (val.x_studio_invoice_amount - val.x_studio_original_amount)
        
  if record.x_studio_vendor.id == 0:
    raise UserError("Vendor Account must be Specified!")
    
  if record.x_studio_currency_id.id == 0:
    raise UserError("Currency must be Specified!")
    
  if record.x_studio_invoice_no == False:
    raise UserError("Invoice No must be Specified!")
    
  if record.x_studio_invoice_date == False:
    raise UserError("Invoice Date must be Specified!")
  
  tax_account = env['x_imports_ledger_setup'].search([('x_studio_company_id', '=', company.id)], limit=1)
  if tax_account:
    if tax_account.x_studio_tp_invoicing_tax_acc.id == 0:
      raise UserError('TP Invoicing Tax Account must be Specified in Imports Ledger Setup')
      
    if tax_account.x_studio_import_tp_vendor_account.id == 0:
      raise UserError('Import TP Vendor Account must be Specified in Imports Ledger Setup')
  else:
    raise UserError('Imports Ledger Setup must be specified for the selected company ')
   
  tp_lines=[]

  if diff_found == True:
    qty = 0
    con_lines = env['x_consignment_header'].search([('id', '=', record.x_studio_con_no.id)])
    if con_lines:
      if diff > 0:
        qty = 1
      else:
        qty = -1
      
      if tax_account.x_studio_cost_allocation_method == 'by_weight':
        for diff_lines in con_lines.x_studio_consignment_line_ids:
          tp_lines.append([0,0,{
            'product_id':diff_lines.x_studio_product_id.id,
            'quantity':qty,
            'currency_id':record.x_studio_currency_id.id,
            'name':diff_lines.x_studio_product_id.name,
            'product_uom_id':diff_lines.x_studio_product_id.uom_id.id,
            'price_unit':abs(diff) * (diff_lines.x_studio_weight / con_lines.x_studio_total_amount_cost_allocation_method), 
            'price_subtotal':(abs(diff) * (diff_lines.x_studio_weight / con_lines.x_studio_total_amount_cost_allocation_method)) * qty, 
            'account_id':diff_lines.x_studio_product_id.categ_id.property_stock_account_input_categ_id.id}])
            
          value_entry = env['stock.valuation.layer'].search([('stock_move_id', '=', diff_lines.x_studio_stock_move_id.id)], limit=1)
          if value_entry:
            value_entry.write({'value':(value_entry.value + ((abs(diff) * (diff_lines.x_studio_weight / con_lines.x_studio_total_amount_cost_allocation_method)) * qty)),
                               'unit_cost':(value_entry.value + ((abs(diff) * (diff_lines.x_studio_weight / con_lines.x_studio_total_amount_cost_allocation_method)) * qty)) / value_entry.quantity,
                               'remaining_value':(value_entry.value + ((abs(diff) * (diff_lines.x_studio_weight / con_lines.x_studio_total_amount_cost_allocation_method)) * qty)) / value_entry.remaining_qty})
      elif tax_account.x_studio_cost_allocation_method == 'by_volume':
        for diff_lines in con_lines.x_studio_consignment_line_ids:
          tp_lines.append([0,0,{
            'product_id':diff_lines.x_studio_product_id.id,
            'quantity':qty,
            'currency_id':record.x_studio_currency_id.id,
            'name':diff_lines.x_studio_product_id.name,
            'product_uom_id':diff_lines.x_studio_product_id.uom_id.id,
            'price_unit':abs(diff) * (diff_lines.x_studio_volume / con_lines.x_studio_total_amount_cost_allocation_method), 
            'price_subtotal':(abs(diff) * (diff_lines.x_studio_volume / con_lines.x_studio_total_amount_cost_allocation_method)) * qty, 
            'account_id':diff_lines.x_studio_product_id.categ_id.property_stock_account_input_categ_id.id}])
            
          value_entry = env['stock.valuation.layer'].search([('stock_move_id', '=', diff_lines.x_studio_stock_move_id.id)], limit=1)
          if value_entry:
            value_entry.write({'value':(value_entry.value + ((abs(diff) * (diff_lines.x_studio_volume / con_lines.x_studio_total_amount_cost_allocation_method)) * qty)),
                               'unit_cost':(value_entry.value + ((abs(diff) * (diff_lines.x_studio_volume / con_lines.x_studio_total_amount_cost_allocation_method)) * qty)) / value_entry.quantity,
                               'remaining_value':(value_entry.value + ((abs(diff) * (diff_lines.x_studio_volume / con_lines.x_studio_total_amount_cost_allocation_method)) * qty)) / value_entry.remaining_qty})
      else: 
        for diff_lines in con_lines.x_studio_consignment_line_ids:
          tp_lines.append([0,0,{
            'product_id':diff_lines.x_studio_product_id.id,
            'quantity':qty,
            'currency_id':record.x_studio_currency_id.id,
            'name':diff_lines.x_studio_product_id.name,
            'product_uom_id':diff_lines.x_studio_product_id.uom_id.id,
            'price_unit':abs(diff) * (diff_lines.x_studio_amount / con_lines.x_studio_total_amount), 
            'price_subtotal':(abs(diff) * (diff_lines.x_studio_amount / con_lines.x_studio_total_amount)) * qty, 
            'account_id':diff_lines.x_studio_product_id.categ_id.property_stock_account_input_categ_id.id}])
            
          value_entry = env['stock.valuation.layer'].search([('stock_move_id', '=', diff_lines.x_studio_stock_move_id.id)], limit=1)
          if value_entry:
            value_entry.write({'value':(value_entry.value + ((abs(diff) * (diff_lines.x_studio_amount / con_lines.x_studio_total_amount)) * qty)),
                               'unit_cost':(value_entry.value + ((abs(diff) * (diff_lines.x_studio_amount / con_lines.x_studio_total_amount)) * qty)) / value_entry.quantity,
                               'remaining_value':(value_entry.value + ((abs(diff) * (diff_lines.x_studio_amount / con_lines.x_studio_total_amount)) * qty)) / value_entry.remaining_qty})
 
  tp_lines.append([0,0,{
    'account_id':tax_account.x_studio_import_tp_vendor_account.id,
    'name':'Import TP Invoice - Reversal',
    'quantity':1.00,
    'currency_id':record.x_studio_currency_id.id,
    'price_unit':record.x_studio_total_original_invoice_amount}])
    #'price_unit':record.x_studio_total_original_invoice_amount * currency_rate.x_studio_rate}])
    
  tp_lines.append([0,0,{
    'account_id':tax_account.x_studio_tp_invoicing_tax_acc.id,
    'name':'Total Tax',
    'quantity':1.00,
    'currency_id':record.x_studio_currency_id.id,
    'price_unit':record.x_studio_taxes_1}])
 
  journal = env['account.journal'].search([('name', '=', 'TP Vendor Bills'),('company_id', '=', company.id)], limit=1) 
  if not journal:
     raise UserError('The required journal has not been setup. Process terminated.')
                
# … 19 more lines
```
  </details>
- **TP Invoice Currency Update** (`sa_f5_x_tp_invoice_header_tp_invoice_currency_update`, type `code`)
  - Function: Sets the TP invoice's Currency to the selected vendor's purchase currency.
  - Depends on: `model x_tp_invoice_header`, `x_tp_invoice_header.x_studio_currency_id`, `x_tp_invoice_header.x_studio_vendor`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (1 lines)</summary>

```python
record['x_studio_currency_id'] = record.x_studio_vendor.property_purchase_currency_id.id
```
  </details>
- **TP Invoice Seq.No** (`sa_f5_x_tp_invoice_header_tp_invoice_seq_no`, type `code`)
  - Function: When the TP invoice's Name is still 'New', assigns the next number from the 'tp.invoice.seq' sequence.
  - Depends on: `model ir.sequence` (base), `model x_tp_invoice_header`, `x_tp_invoice_header.x_name`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (5 lines)</summary>

```python
#record['x_name'] = env['ir.sequence'].next_by_code('purchase.request.seq')

if record.x_name == 'New':
 seq = env['ir.sequence'].next_by_code('tp.invoice.seq')
 record.write({'x_name': seq})
```
  </details>
**Automations (2):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| JIN-Third Party(TP) Invoice Seq.No | `base_automation_65_jin_third_party_tp_invoice_seq_no` |  | When a record is created or updated on TP Invoice Header, runs _Execute Code_. | `model x_tp_invoice_header`<br>`server action BugFix-Accounting.server_action_1381_tp_invoice_seq_no`<br>`x_tp_invoice_header.create_date` |  |
| TP Invoice Currency Update | `base_automation_184_tp_invoice_currency_update` |  | When a watched field changes in the form on TP Invoice Header, runs _Execute Code_. | `model x_tp_invoice_header`<br>`server action BugFix-Accounting.server_action_2112_tp_invoice_currency_update`<br>`x_tp_invoice_header.x_studio_vendor` |  |

**Window actions (5):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| TP Invoice Header | `action_1379_tp_invoice_header` | Opens **TP Invoice Header** records (tree,form). | `model x_tp_invoice_header` |  |
| TP Invoice Header | `action_2864_tp_invoice_header` | Opens **TP Invoice Header** records (tree,form). | `model x_tp_invoice_header` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_imports_tp_invoice_header` (BugFix-Studio-Misc) |
| TP Invoices | `action_1382_tp_invoices` | Opens **TP Invoice Header** records (tree,form), filtered to `[('x_studio_consignment_header_id', '=', active_id)]`. | `model x_tp_invoice_header` |  |
| TP Invoices | `action_1383_tp_invoices` | Opens **TP Invoice Header** records (tree,form), filtered to `[('x_studio_con_no', '=', active_id)]`. | `model x_tp_invoice_header`<br>`x_tp_invoice_header.x_studio_con_no` |  |
| x_tp_invoice_header | `action_2430_x_tp_invoice_header` | Opens **TP Invoice Header** records (tree,form). | `model x_tp_invoice_header` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_x_tp_invoice_header` (BugFix-Studio-Misc) |

**Views (7):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_tp_invoice_header | `ported_default_form_view_fo_b04274bb_8930_4e7e_a2cc_e65229996a48` | form | full form layout with 3 fields | Base TP Invoice form: a 'Post' header button shown only in Draft status (runs IMP - Post TP Invoice), hidden status field, Invoice Reference title and Archived ribbon. | `server action BugFix-Accounting.srv_tp_invoice_post`<br>`x_tp_invoice_header.x_active`<br>`x_tp_invoice_header.x_name`<br>`x_tp_invoice_header.x_studio_status` | `view BugFix-Accounting.ported_view_3045_odoo_studio_default_fc4d9ef7_2d23_4a16_911c_66cf2185de9b` |
| Default list view for x_tp_invoice_header | `ported_default_list_view_fo_87762a20_9628_4266_a414_8bb858fd9746` | tree | full tree layout with 2 fields | Base list screen for TP Invoice Header records showing Name with a drag handle for manual ordering by Sequence. | `x_tp_invoice_header.x_name`<br>`x_tp_invoice_header.x_studio_sequence` | `view BugFix-Accounting.ported_odoo_studio_default__c572715b_284c_469b_9b41_7a04b3431fc6`<br>`view BugFix-Accounting.ported_view_3050_odoo_studio_default_c572715b_284c_469b_9b41_7a04b3431fc6` |
| Default search view for x_tp_invoice_header | `ported_default_search_view__12511c2f_92e3_4ad8_a81a_9adf7a7e038f` | search | full search layout with 1 fields | Search bar for TP Invoice Header records: search by Name and an 'Archived' filter to show inactive records. | `x_tp_invoice_header.x_active`<br>`x_tp_invoice_header.x_name` |  |
| Default search view for x_tp_invoice_header | `ported_view_3044_default_search_view_12511c2f_92e3_4ad8_a81a_9adf7a7e038f` | search | full search layout with 1 fields | Default search view for TP Invoice Header records: search by name plus an Archived filter. | `x_tp_invoice_header.x_active`<br>`x_tp_invoice_header.x_name` |  |
| Odoo Studio: Default form view for x_tp_invoice_header customization | `ported_view_3045_odoo_studio_default_fc4d9ef7_2d23_4a16_911c_66cf2185de9b` | form | after `//header[1]/button[1]`: add field x_studio_pipeline_status_bar; before `//widget[@name='web_ribbon']`: add div; set force_save=True, readonly=1 on `//form[1]/sheet[1]/div[not(@name)][1]/h1[1]/field[@name='x_name']`; inside `//group[@name='studio_group_c9cf25_left']`: add field x_studio_vendor, field x_studio_name, field x_studio_con_no; inside `//group[@name='studio_group_c9cf25_right']`: add field x_studio_invoice_no, field x_studio_invoice_date, field x_studio_currency_id, field x_studio_status; after `//group[@name='studio_group_c9cf25']`: add notebook | TP Invoice Header form: adds a pipeline status bar, a 'Vendor Bill' smart button (when bills exist), makes the reference read-only, and adds Vendor, Name, Consignment No, Invoice No/Date, Currency, Status and a lines notebook. | `view BugFix-Accounting.ported_default_form_view_fo_b04274bb_8930_4e7e_a2cc_e65229996a48`<br>`window action BugFix-Accounting.act_tp_invoice_vendor_bill`<br>`x_tp_invoice_header.x_studio_con_no`<br>`x_tp_invoice_header.x_studio_currency_id`<br>`x_tp_invoice_header.x_studio_invoice_date`<details><summary>+18 more</summary>`x_tp_invoice_header.x_studio_invoice_no`<br>`x_tp_invoice_header.x_studio_name`<br>`x_tp_invoice_header.x_studio_pipeline_status_bar`<br>`x_tp_invoice_header.x_studio_status`<br>`x_tp_invoice_header.x_studio_taxes_1`<br>`x_tp_invoice_header.x_studio_total_1`<br>`x_tp_invoice_header.x_studio_total_invoice_amount`<br>`x_tp_invoice_header.x_studio_tp_lines`<br>`x_tp_invoice_header.x_studio_vendor`<br>`x_tp_invoice_header.x_x_studio_tp_id__account_move_count`<br>`x_tp_invoice_line.x_name`<br>`x_tp_invoice_line.x_studio_charge_group`<br>`x_tp_invoice_line.x_studio_charge_name`<br>`x_tp_invoice_line.x_studio_invoice_amount`<br>`x_tp_invoice_line.x_studio_original_amount`<br>`x_tp_invoice_line.x_studio_sequence`<br>`x_tp_invoice_line.x_studio_tax_amount`<br>`x_tp_invoice_line.x_studio_taxes`</details> |  |
| Odoo Studio: Default list view for x_tp_invoice_header customization | `ported_odoo_studio_default__c572715b_284c_469b_9b41_7a04b3431fc6` | tree | set create=false, delete=false on `//tree[1]` | Studio customization of the TP Invoice list: disables creating and deleting TP invoices from the list. | `view BugFix-Accounting.ported_default_list_view_fo_87762a20_9628_4266_a414_8bb858fd9746` |  |
| Odoo Studio: Default list view for x_tp_invoice_header customization | `ported_view_3050_odoo_studio_default_c572715b_284c_469b_9b41_7a04b3431fc6` | tree | set create=false, delete=false on `//tree[1]`; set column_invisible=1 on `//field[@name='x_studio_sequence']`; set string=Invoice Reference on `//field[@name='x_name']`; after `//field[@name='x_name']`: add field x_studio_status, field x_studio_vendor, field x_studio_invoice_no, field x_studio_invoice_date, field x_studio_currency_id | TP Invoice Header list (no create/delete): labels Name as 'Invoice Reference' and adds Status, Vendor, Invoice No, Invoice Date and Currency; sequence hidden. | `view BugFix-Accounting.ported_default_list_view_fo_87762a20_9628_4266_a414_8bb858fd9746`<br>`x_tp_invoice_header.x_studio_currency_id`<br>`x_tp_invoice_header.x_studio_invoice_date`<br>`x_tp_invoice_header.x_studio_invoice_no`<br>`x_tp_invoice_header.x_studio_status`<details><summary>+1 more</summary>`x_tp_invoice_header.x_studio_vendor`</details> |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| TP Invoice Header group_system | `access_1370_tp_invoice_header_group_system` | Gives **Administration / Settings** read/write/create/delete access to TP Invoice Header records. | `group base.group_system` (base)<br>`model x_tp_invoice_header` |  |
| TP Invoice Header group_user | `access_1371_tp_invoice_header_group_user` | Gives **User types / Internal User** read access to TP Invoice Header records. | `group base.group_user` (base)<br>`model x_tp_invoice_header` |  |
| x_tp_invoice_header user access | `access_x_tp_invoice_header_user` | Gives **User types / Internal User** read/write/create/delete access to TP Invoice Header records. | `group base.group_user` (base)<br>`model x_tp_invoice_header` |  |
