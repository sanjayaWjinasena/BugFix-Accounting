# BugFix-Accounting — `tp_invoice_header`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `tp_invoice_header` — TP Invoice Header

*Created by this repo.* Python: `models/tp_invoice_header.py`, `models/x_tp_invoice_header_gap.py`. Record name field: `name`.

Other repos that use this model: `access right BugFix-Studio-Misc.access_g_tp_invoice_header_tp_invoice_header_purchase_jin_po_invoicing_payment_import` (BugFix-Studio-Misc)<br>`server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:tp_invoice_header -->
A third-party (TP) invoice for charges on an import consignment, created from the consignment through the Create TP Invoice wizard, with vendor, currency, supplier invoice number and date and charge lines. Untaxed amount, taxes, total and total original amount are computed from the lines, and a smart button opens the related vendor bills. Automations assign the number from the 'tp.invoice.seq' sequence and set the currency to the vendor's purchase currency. The 'Post TP Invoice' button validates the invoice and the Imports Ledger Setup, adjusts stock valuation for amount differences, creates and posts a vendor bill and sets the status to Posted.
<!-- /SUMMARY -->

**Fields (35):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard computed field: calendar meeting linked to the next activity on this TP Invoice Header record, if any. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard computed field: due date of the next scheduled activity on this TP Invoice Header record. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard computed flag (Alert or Error) showing that an activity on this TP Invoice Header record is in an exception state. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard computed icon shown when an activity on this TP Invoice Header record is in an exception state. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Scheduled activities (to-dos, calls, meetings) attached to this TP Invoice Header record, from the standard activity mixin. | stored | `model mail.activity` (mail) | `tp_invoice_header.activity_summary`<br>`tp_invoice_header.activity_type_icon`<br>`tp_invoice_header.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard computed activity status of this TP Invoice Header record: Overdue, Today or Planned, based on the nearest activity deadline. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Summary text of the next scheduled activity on this TP Invoice Header record, read via related from its activities. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`tp_invoice_header.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Font Awesome icon of the next activity type on this TP Invoice Header record, read via related from its activities; used for display only. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`tp_invoice_header.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Type of the next scheduled activity on this TP Invoice Header record, read via related from its activities (standard activity mixin). | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`tp_invoice_header.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard computed field: the user responsible for the next scheduled activity on this TP Invoice Header record. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the TP Invoice Header was created (standard audit field); also referenced by the JIN Third Party TP Invoice Seq No automation. | stored |  | `automation BugFix-Accounting.base_automation_65_jin_third_party_tp_invoice_seq_no` |
| `create_uid` | Created by | many2one → `res.users` | User who created the TP Invoice Header record (standard audit field set automatically). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the TP Invoice Header record in lookups and breadcrumbs, computed by Odoo (standard field). | not stored |  |  |
| `id` | ID | integer | Technical unique database ID of the TP Invoice Header record (standard Odoo field). | stored |  |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard computed field: due date of the current user's next activity on this TP Invoice Header record. | not stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time the TP Invoice Header record was last modified (standard audit field). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last modified the TP Invoice Header record (standard audit field set automatically). | stored | `model res.users` (base) |  |
| `active` | Active | boolean | Archive flag of the TP (third-party) invoice; defaults to true (ir.default), and unticked (archived) records are hidden from normal lists. Shown in the form and search views. | stored |  | `default BugFix-Accounting.default_tp_invoice_header_active`<br>`view BugFix-Accounting.view_tp_invoice_header_form`<br>`view BugFix-Accounting.view_tp_invoice_header_search`<br>`view BugFix-Accounting.view_tp_invoice_header_search_2` |
| `currency_id` | Currency | many2one → `res.currency` | Currency used to format the monetary totals (total invoice amount, taxes, total) on the TP invoice form; defaults via ir.default to currency database id 145. TP invoice posting logic uses the other Currency field, `accounting_currency_id`. | stored | `model res.currency` (base) | `default BugFix-Accounting.default_tp_invoice_header_currency_id` |
| `name` | Invoice Reference | char | TP invoice reference number. Defaults to "New" and is replaced with the next "tp.invoice.seq" sequence number by the TP Invoice Seq.No automation. Shown in the form, list and search views. | stored |  | `default BugFix-Accounting.default_tp_invoice_header_name`<br>`server action BugFix-Accounting.action_tp_invoice_header_tp_invoice_seq_no`<br>`server action BugFix-Accounting.action_tp_invoice_seq_no`<br>`view BugFix-Accounting.view_tp_invoice_header_form`<br>`view BugFix-Accounting.view_tp_invoice_header_list`<details><summary>+2 more</summary>`view BugFix-Accounting.view_tp_invoice_header_search`<br>`view BugFix-Accounting.view_tp_invoice_header_search_2`</details> |
| `con_no` | Created From Consignment No | many2one → `consignment_header` | Import consignment this TP invoice was created from. Set by "IMP - Apply Selected Charge Lines to TP Invoice", used by "IMP - Post TP Invoice" and as the filter of the consignment's TP Invoices action. Shown in the form view. | stored | `model consignment_header` (BugFix-Stock) | `server action BugFix-Accounting.action_imp_post_tp_invoice`<br>`server action BugFix-Accounting.srv_tp_invoice_post`<br>`view BugFix-Accounting.view_default_form_view_for_tp_invoice_header_inherit`<br>`window action BugFix-Accounting.action_tp_invoices_2` |
| `accounting_currency_id` | Currency | many2one → `res.currency` | Currency of the TP invoice. Defaults to currency id 145, is reset to the vendor's purchase currency by the TP Invoice Currency Update automation, and is required when posting. Shown in the form and list views. | stored | `model res.currency` (base) | `default BugFix-Accounting.default_tp_invoice_header_accounting_currency_id`<br>`default BugFix-Accounting.default_tp_invoice_header_accounting_currency_id_2`<br>`server action BugFix-Accounting.action_tp_invoice_header_tp_invoice_currency_update`<br>`server action BugFix-Accounting.action_imp_post_tp_invoice`<br>`server action BugFix-Accounting.action_tp_invoice_currency_update`<details><summary>+3 more</summary>`server action BugFix-Accounting.srv_tp_invoice_post`<br>`view BugFix-Accounting.view_default_form_view_for_tp_invoice_header_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_tp_invoice_header_inherit_2`</details> |
| `accounting_invoice_date` | Supplier's Invoice Date (Bill Date) | date | Supplier's invoice (bill) date, copied from the consignment when the TP invoice is created; posting raises an error if it is empty. Shown in the form and list views. | stored |  | `server action BugFix-Accounting.action_imp_post_tp_invoice`<br>`server action BugFix-Accounting.srv_tp_invoice_post`<br>`view BugFix-Accounting.view_default_form_view_for_tp_invoice_header_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_tp_invoice_header_inherit_2` |
| `invoice_no` | Supplier's Invoice No (Bill Reference) | char | Supplier's invoice number (bill reference), copied from the consignment's supplier invoice number on creation; posting raises an error if it is empty. Shown in the form and list views. | stored |  | `server action BugFix-Accounting.action_imp_post_tp_invoice`<br>`server action BugFix-Accounting.srv_tp_invoice_post`<br>`view BugFix-Accounting.view_default_form_view_for_tp_invoice_header_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_tp_invoice_header_inherit_2` |
| `accounting_name` | Name | char | Vendor's name, copied automatically from the selected Vendor via related field (`vendor.name`); shown on the TP Invoice Header form. | related `vendor.name`; not stored | `res.partner.name` (base)<br>`tp_invoice_header.vendor` | `view BugFix-Accounting.view_default_form_view_for_tp_invoice_header_inherit` |
| `pipeline_status_bar` | Pipeline status bar | selection: Draft=Draft; Posted=Posted | Stage of the third-party invoice (Draft or Posted) shown as a status bar on the form; has a default value and is updated by the Post TP Invoice server actions. | stored |  | `default BugFix-Accounting.default_tp_invoice_header_pipeline_status_bar`<br>`server action BugFix-Accounting.action_imp_post_tp_invoice`<br>`server action BugFix-Accounting.srv_tp_invoice_post`<br>`view BugFix-Accounting.view_default_form_view_for_tp_invoice_header_inherit` |
| `sequence` | Sequence | integer | Sort order of TP Invoice Header records (default 10), used for drag-and-drop ordering in the list view. | default `10`; stored |  | `default BugFix-Accounting.default_tp_invoice_header_sequence`<br>`view BugFix-Accounting.view_tp_invoice_header_list` |
| `status` | Status | selection: Draft=Draft; Posted=Posted | Posting status of the third-party invoice (Draft or Posted); defaults via an ir.default, is set by the Post TP Invoice server actions and is shown on the TP Invoice Header form and list views. | stored |  | `default BugFix-Accounting.default_tp_invoice_header_status`<br>`server action BugFix-Accounting.action_imp_post_tp_invoice`<br>`server action BugFix-Accounting.srv_tp_invoice_post`<br>`view BugFix-Accounting.view_tp_invoice_header_form`<br>`view BugFix-Accounting.view_default_form_view_for_tp_invoice_header_inherit`<details><summary>+1 more</summary>`view BugFix-Accounting.view_default_list_view_for_tp_invoice_header_inherit_2`</details> |
| `taxes_1` | Taxes | monetary | Total tax of the TP invoice, computed as the sum of Tax Amount on all TP Lines; added into Total and used by the Post TP Invoice server actions. | computed by `_compute_taxes_1`; not stored | `tp_invoice_header._compute_taxes_1()` | `server action BugFix-Accounting.action_imp_post_tp_invoice`<br>`server action BugFix-Accounting.srv_tp_invoice_post`<br>`view BugFix-Accounting.view_default_form_view_for_tp_invoice_header_inherit`<br>`tp_invoice_header._compute_taxes_1()`<br>`tp_invoice_header._compute_total_1()` |
| `total_1` | Total | monetary | Grand total of the TP invoice, computed as Untaxed Amount plus Taxes. | computed by `_compute_total_1`; not stored | `tp_invoice_header._compute_total_1()` | `view BugFix-Accounting.view_default_form_view_for_tp_invoice_header_inherit`<br>`tp_invoice_header._compute_total_1()` |
| `total_invoice_amount` | Untaxed Amount | monetary | Untaxed total of the TP invoice, computed as the sum of Invoice Amount on all TP Lines; feeds the Total field. | computed by `_compute_total_invoice_amount`; not stored | `tp_invoice_header._compute_total_invoice_amount()` | `view BugFix-Accounting.view_default_form_view_for_tp_invoice_header_inherit`<br>`tp_invoice_header._compute_total_1()`<br>`tp_invoice_header._compute_total_invoice_amount()` |
| `total_original_invoice_amount` | Total Original Invoice Amount | float | Sum of Original Amount across all TP Lines; computed and used by the Post TP Invoice server actions. | computed by `_compute_total_original_invoice_amount`; not stored | `tp_invoice_header._compute_total_original_invoice_amount()` | `server action BugFix-Accounting.action_imp_post_tp_invoice`<br>`server action BugFix-Accounting.srv_tp_invoice_post`<br>`tp_invoice_header._compute_total_original_invoice_amount()` |
| `tp_lines` | TP Lines | one2many → `tp_invoice_line` | Charge lines of this third-party invoice (TP Invoice Line records); their amounts are summed into Untaxed Amount, Taxes and Total Original Invoice Amount. | stored | `model tp_invoice_line` | `view BugFix-Accounting.view_default_form_view_for_tp_invoice_header_inherit`<br>`tp_invoice_header._compute_taxes_1()`<br>`tp_invoice_header._compute_total_invoice_amount()`<br>`tp_invoice_header._compute_total_original_invoice_amount()` |
| `vendor` | Vendor | many2one → `res.partner` | Third-party vendor (partner) the invoice is from, chosen by the user; changing it triggers the TP Invoice Currency Update automation that copies the vendor's purchase currency, and it is used when posting the TP invoice. | stored | `model res.partner` (base) | `automation BugFix-Accounting.automation_tp_invoice_currency_update`<br>`server action BugFix-Accounting.action_tp_invoice_header_tp_invoice_currency_update`<br>`server action BugFix-Accounting.action_imp_post_tp_invoice`<br>`server action BugFix-Accounting.action_tp_invoice_currency_update`<br>`server action BugFix-Accounting.srv_tp_invoice_post`<details><summary>+3 more</summary>`view BugFix-Accounting.view_default_form_view_for_tp_invoice_header_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_tp_invoice_header_inherit_2`<br>`tp_invoice_header.accounting_name`</details> |
| `tp_id__account_move_count` | Created From TP Invoice count | integer | Number of journal entries/bills whose `tp_id` points at this TP invoice, shown on the smart button; returns 0 if that link field is not installed on account.move. | computed by `_compute_tp_id__account_move_count`; not stored | `tp_invoice_header._compute_tp_id__account_move_count()` | `view BugFix-Accounting.view_default_form_view_for_tp_invoice_header_inherit`<br>`tp_invoice_header._compute_tp_id__account_move_count()` |

**Python methods (5):**

| Method | Function | Decorators | Extends standard | Depends on | Used by | Where |
|---|---|---|---|---|---|---|
| `_compute_total_invoice_amount` | Compute for Untaxed Amount: sums Invoice Amount over all TP Lines. | api.depends('tp_lines', 'tp_lines.invoice_amount') |  | `tp_invoice_header.total_invoice_amount`<br>`tp_invoice_header.tp_lines`<br>`tp_invoice_line.invoice_amount` | `tp_invoice_header.total_invoice_amount` | `models/tp_invoice_header.py:96` |
| `_compute_taxes_1` | Compute for Taxes: sums Tax Amount over all TP Lines. | api.depends('tp_lines', 'tp_lines.taxes', 'x_studio_t… |  | `tp_invoice_header.taxes_1`<br>`tp_invoice_header.tp_lines`<br>`tp_invoice_line.invoice_amount`<br>`tp_invoice_line.taxes` | `tp_invoice_header.taxes_1` | `models/tp_invoice_header.py:108` |
| `_compute_total_1` | Compute for Total: Untaxed Amount plus Taxes. | api.depends('total_invoice_amount', 'taxes_1') |  | `tp_invoice_header.taxes_1`<br>`tp_invoice_header.total_1`<br>`tp_invoice_header.total_invoice_amount` | `tp_invoice_header.total_1` | `models/tp_invoice_header.py:119` |
| `_compute_total_original_invoice_amount` | Compute for Total Original Invoice Amount: sums Original Amount over all TP Lines. | api.depends('tp_lines', 'tp_lines.original_amount') |  | `tp_invoice_header.total_original_invoice_amount`<br>`tp_invoice_header.tp_lines`<br>`tp_invoice_line.original_amount` | `tp_invoice_header.total_original_invoice_amount` | `models/tp_invoice_header.py:129` |
| `_compute_tp_id__account_move_count` | Compute for the linked-journal-entry count: groups account.move by `tp_id` and counts entries per TP invoice; returns 0 if that field is not installed. |  |  | `model account.move` (account)<br>`tp_invoice_header.tp_id__account_move_count` | `tp_invoice_header.tp_id__account_move_count` | `models/tp_invoice_header.py:136` |

**Server actions (6):**

- **Execute Code** (`action_tp_invoice_seq_no`, type `code`)
  - Function: Run by the TP Invoice Seq No automation: when Name is 'New', assigns the next number from the 'tp.invoice.seq' sequence.
  - Depends on: `model ir.sequence` (base), `model tp_invoice_header`, `tp_invoice_header.name`
  - Used by: `automation BugFix-Accounting.base_automation_65_jin_third_party_tp_invoice_seq_no`
  <details><summary>code (6 lines)</summary>

```python
# record['name'] = env['ir.sequence'].next_by_code('purchase.request.seq')

if record.name == "New":
    seq = env["ir.sequence"].next_by_code("tp.invoice.seq")
    record.write({"name": seq})
```
  </details>
- **Execute Code** (`action_tp_invoice_currency_update`, type `code`)
  - Function: Run when the TP invoice vendor changes: sets Currency to the vendor's purchase currency.
  - Depends on: `model tp_invoice_header`, `tp_invoice_header.accounting_currency_id`, `tp_invoice_header.vendor`
  - Used by: `automation BugFix-Accounting.automation_tp_invoice_currency_update`
  <details><summary>code (2 lines)</summary>

```python
record["accounting_currency_id"] = record.vendor.property_purchase_currency_id.id
```
  </details>
- **IMP - Post TP Invoice** (`srv_tp_invoice_post`, type `code`)
  - Function: Post TP Invoice button: validates lines, vendor, currency, invoice no/date and Imports Ledger Setup, adjusts stock valuation for amount differences, creates and posts a vendor bill in 'TP Vendor Bills' journal, sets status Posted and opens the bill.
  - Depends on: `model account.journal` (account), `model account.move` (account), `model res.company` (base), `model stock.valuation.layer` (stock_account), `model consignment_header` (BugFix-Stock)<details><summary>+12 more</summary>`model imports_ledger_setup` (BugFix-Purchase), `model tp_invoice_header`, `model tp_invoice_line`, `tp_invoice_header.con_no`, `tp_invoice_header.accounting_currency_id`, `tp_invoice_header.accounting_invoice_date`, `tp_invoice_header.invoice_no`, `tp_invoice_header.pipeline_status_bar`, `tp_invoice_header.status`, `tp_invoice_header.taxes_1`, `tp_invoice_header.total_original_invoice_amount`, `tp_invoice_header.vendor`</details>
  - Used by: `view BugFix-Accounting.view_tp_invoice_header_form`
  <details><summary>code (150 lines)</summary>

```python
if record.id:
    company_id = env.context.get("allowed_company_ids", [env.user.company_id.id])[0]
    company = env["res.company"].browse(company_id)

    invalid_lines = env["tp_invoice_line"].search(
        [("tp_invoice_header_id", "=", record.id)]
    )
    diff = 0
    diff_found = False
    if invalid_lines:
        for val in invalid_lines:
            if val.invoice_amount == 0.0000:
                raise UserError(
                    "Invoice Amount of Individual TP Lines Should be Greater than Zero!"
                )
            if val.invoice_amount != val.original_amount:
                diff_found = True
                diff += val.invoice_amount - val.original_amount

    if record.vendor.id == 0:
        raise UserError("Vendor Account must be Specified!")
    if record.accounting_currency_id.id == 0:
        raise UserError("Currency must be Specified!")
    if record.invoice_no == False:
        raise UserError("Invoice No must be Specified!")
    if record.accounting_invoice_date == False:
        raise UserError("Invoice Date must be Specified!")

    tax_account = env["imports_ledger_setup"].search(
        [("accounting_company_id", "=", company.id)], limit=1
    )
    if tax_account:
        if tax_account.x_studio_tp_invoicing_tax_acc.id == 0:
            raise UserError(
                "TP Invoicing Tax Account must be Specified in Imports Ledger Setup"
            )
        if tax_account.import_tp_vendor_account.id == 0:
            raise UserError(
                "Import TP Vendor Account must be Specified in Imports Ledger Setup"
            )
    else:
        raise UserError(
            "Imports Ledger Setup must be specified for the selected company "
        )

    tp_lines = []

    if diff_found == True:
        qty = 0
        con_lines = env["consignment_header"].search(
            [("id", "=", record.con_no.id)]
        )
        if con_lines:
            qty = 1 if diff > 0 else -1

            if tax_account.cost_allocation_method == "by_weight":
                for diff_lines in con_lines.consignment_line_ids:
                    tp_lines.append(
                        [
                            0,
                            0,
                            {
                                "product_id": diff_lines.product_id.id,
                                "quantity": qty,
                                "currency_id": record.accounting_currency_id.id,
                                "name": diff_lines.product_id.name,
                                "product_uom_id": diff_lines.product_id.uom_id.id,
                                "price_unit": abs(diff)
                                * (
                                    diff_lines.weight
                                    / con_lines.total_amount_cost_allocation_method
                                ),
                                "price_subtotal": (
                                    abs(diff)
                                    * (
                                        diff_lines.weight
                                        / con_lines.total_amount_cost_allocation_method
                                    )
                                )
                                * qty,
                                "account_id": diff_lines.product_id.categ_id.property_stock_account_input_categ_id.id,
                            },
                        ]
                    )
                    value_entry = env["stock.valuation.layer"].search(
                        [("stock_move_id", "=", diff_lines.stock_move_id.id)],
                        limit=1,
                    )
                    if value_entry:
                        adj = (
                            abs(diff)
                            * (
                                diff_lines.weight
                                / con_lines.total_amount_cost_allocation_method
                            )
                        ) * qty
                        value_entry.write(
                            {
                                "value": value_entry.value + adj,
                                "unit_cost": (value_entry.value + adj)
                                / value_entry.quantity,
                                "remaining_value": (value_entry.value + adj)
                                / value_entry.remaining_qty,
                            }
                        )
            elif tax_account.cost_allocation_method == "by_volume":
                for diff_lines in con_lines.consignment_line_ids:
                    tp_lines.append(
                        [
                            0,
                            0,
                            {
                                "product_id": diff_lines.product_id.id,
                                "quantity": qty,
                                "currency_id": record.accounting_currency_id.id,
                                "name": diff_lines.product_id.name,
                                "product_uom_id": diff_lines.product_id.uom_id.id,
                                "price_unit": abs(diff)
                                * (
                                    diff_lines.volume
                                    / con_lines.total_amount_cost_allocation_method
                                ),
                                "price_subtotal": (
                                    abs(diff)
                                    * (
                                        diff_lines.volume
                                        / con_lines.total_amount_cost_allocation_method
                                    )
                                )
                                * qty,
                                "account_id": diff_lines.product_id.categ_id.property_stock_account_input_categ_id.id,
                            },
                        ]
                    )
                    value_entry = env["stock.valuation.layer"].search(
                        [("stock_move_id", "=", diff_lines.stock_move_id.id)],
                        limit=1,
                    )
                    if value_entry:
                        adj = (
                            abs(diff)
                            * (
                                diff_lines.volume
                                / con_lines.total_amount_cost_allocation_method
                            )
                        ) * qty
                        value_entry.write(
                            {
                                "value": value_entry.value + adj,
                                "unit_cost": (value_entry.value + adj)
                                / value_entry.quantity,
                                "remaining_value": (value_entry.value + adj)
                                / value_entry.remaining_qty,
                            }
                        )
            else:
                for diff_lines in con_lines.consignment_line_ids:
                    tp_lines.append(
                        [
                            0,
                            0,
                            {
                                "product_id": diff_lines.product_id.id,
                                "quantity": qty,
                                "currency_id": record.accounting_currency_id.id,
                                "name": diff_lines.product_id.name,
                                "product_uom_id": diff_lines.product_id.uom_id.id,
                                "price_unit": abs(diff)
                                * (
                                    diff_lines.amount
                                    / con_lines.total_amount
                                ),
                                "price_subtotal": (
                                    abs(diff)
                                    * (
                                        diff_lines.amount
                                        / con_lines.total_amount
                                    )
                                )
                                * qty,
                                "account_id": diff_lines.product_id.categ_id.property_stock_account_input_categ_id.id,
                            },
                        ]
                    )
                    value_entry = env["stock.valuation.layer"].search(
                        [("stock_move_id", "=", diff_lines.stock_move_id.id)],
                        limit=1,
                    )
                    if value_entry:
                        adj = (
                            abs(diff)
                            * (
                                diff_lines.amount
                                / con_lines.total_amount
                            )
                        ) * qty
                        value_entry.write(
                            {
                                "value": value_entry.value + adj,
                                "unit_cost": (value_entry.value + adj)
                                / value_entry.quantity,
                                "remaining_value": (value_entry.value + adj)
                                / value_entry.remaining_qty,
                            }
                        )

    tp_lines.append(
        [
            0,
            0,
            {
                "account_id": tax_account.import_tp_vendor_account.id,
                "name": "Import TP Invoice - Reversal",
                "quantity": 1.00,
                "currency_id": record.accounting_currency_id.id,
                "price_unit": record.total_original_invoice_amount,
            },
        ]
    )

    tp_lines.append(
        [
            0,
            0,
            {
                "account_id": tax_account.x_studio_tp_invoicing_tax_acc.id,
                "name": "Total Tax",
                "quantity": 1.00,
                "currency_id": record.accounting_currency_id.id,
                "price_unit": record.taxes_1,
            },
        ]
    )

    journal = env["account.journal"].search(
        [("name", "=", "TP Vendor Bills"), ("company_id", "=", company.id)], limit=1
    )
# … 30 more lines
```
  </details>
- **IMP - Post TP Invoice** (`action_imp_post_tp_invoice`, type `code`)
  - Function: Legacy Post TP Invoice action: validates the TP invoice and Imports Ledger Setup, adjusts stock valuation for amount differences, creates and posts a vendor bill and sets the TP invoice to Posted.
  - Depends on: `model account.journal` (account), `model account.move` (account), `model res.company` (base), `model stock.valuation.layer` (stock_account), `model consignment_header` (BugFix-Stock)<details><summary>+12 more</summary>`model imports_ledger_setup` (BugFix-Purchase), `model tp_invoice_header`, `model tp_invoice_line`, `tp_invoice_header.con_no`, `tp_invoice_header.accounting_currency_id`, `tp_invoice_header.accounting_invoice_date`, `tp_invoice_header.invoice_no`, `tp_invoice_header.pipeline_status_bar`, `tp_invoice_header.status`, `tp_invoice_header.taxes_1`, `tp_invoice_header.total_original_invoice_amount`, `tp_invoice_header.vendor`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (139 lines)</summary>

```python
if record.id:
    company_id = env.context.get("allowed_company_ids", [env.user.company_id.id])[0]
    company = env["res.company"].browse(company_id)

    invalid_lines = env["tp_invoice_line"].search(
        [("tp_invoice_header_id", "=", record.id)]
    )
    if invalid_lines:
        diff = 0
        diff_found = False
        for val in invalid_lines:
            if val.invoice_amount == 0.0000:
                raise UserError(
                    "Invoice Amount of Individual TP Lines Should be Greater than Zero!"
                )

            if val.invoice_amount != val.original_amount:
                diff_found = True
                diff += val.invoice_amount - val.original_amount

    if record.vendor.id == 0:
        raise UserError("Vendor Account must be Specified!")

    if record.accounting_currency_id.id == 0:
        raise UserError("Currency must be Specified!")

    if record.invoice_no == False:
        raise UserError("Invoice No must be Specified!")

    if record.accounting_invoice_date == False:
        raise UserError("Invoice Date must be Specified!")

    tax_account = env["imports_ledger_setup"].search(
        [("accounting_company_id", "=", company.id)], limit=1
    )
    if tax_account:
        if tax_account.x_studio_tp_invoicing_tax_acc.id == 0:
            raise UserError(
                "TP Invoicing Tax Account must be Specified in Imports Ledger Setup"
            )

        if tax_account.import_tp_vendor_account.id == 0:
            raise UserError(
                "Import TP Vendor Account must be Specified in Imports Ledger Setup"
            )
    else:
        raise UserError(
            "Imports Ledger Setup must be specified for the selected company "
        )

    tp_lines = []

    if diff_found == True:
        qty = 0
        con_lines = env["consignment_header"].search(
            [("id", "=", record.con_no.id)]
        )
        if con_lines:
            if diff > 0:
                qty = 1
            else:
                qty = -1

            if tax_account.cost_allocation_method == "by_weight":
                for diff_lines in con_lines.consignment_line_ids:
                    tp_lines.append(
                        [
                            0,
                            0,
                            {
                                "product_id": diff_lines.product_id.id,
                                "quantity": qty,
                                "currency_id": record.accounting_currency_id.id,
                                "name": diff_lines.product_id.name,
                                "product_uom_id": diff_lines.product_id.uom_id.id,
                                "price_unit": abs(diff)
                                * (
                                    diff_lines.weight
                                    / con_lines.total_amount_cost_allocation_method
                                ),
                                "price_subtotal": (
                                    abs(diff)
                                    * (
                                        diff_lines.weight
                                        / con_lines.total_amount_cost_allocation_method
                                    )
                                )
                                * qty,
                                "account_id": diff_lines.product_id.categ_id.property_stock_account_input_categ_id.id,
                            },
                        ]
                    )

                    value_entry = env["stock.valuation.layer"].search(
                        [("stock_move_id", "=", diff_lines.stock_move_id.id)],
                        limit=1,
                    )
                    if value_entry:
                        value_entry.write(
                            {
                                "value": (
                                    value_entry.value
                                    + (
                                        (
                                            abs(diff)
                                            * (
                                                diff_lines.weight
                                                / con_lines.total_amount_cost_allocation_method
                                            )
                                        )
                                        * qty
                                    )
                                ),
                                "unit_cost": (
                                    value_entry.value
                                    + (
                                        (
                                            abs(diff)
                                            * (
                                                diff_lines.weight
                                                / con_lines.total_amount_cost_allocation_method
                                            )
                                        )
                                        * qty
                                    )
                                )
                                / value_entry.quantity,
                                "remaining_value": (
                                    value_entry.value
                                    + (
                                        (
                                            abs(diff)
                                            * (
                                                diff_lines.weight
                                                / con_lines.total_amount_cost_allocation_method
                                            )
                                        )
                                        * qty
                                    )
                                )
                                / value_entry.remaining_qty,
                            }
                        )
            elif tax_account.cost_allocation_method == "by_volume":
                for diff_lines in con_lines.consignment_line_ids:
                    tp_lines.append(
                        [
                            0,
                            0,
                            {
                                "product_id": diff_lines.product_id.id,
                                "quantity": qty,
                                "currency_id": record.accounting_currency_id.id,
                                "name": diff_lines.product_id.name,
                                "product_uom_id": diff_lines.product_id.uom_id.id,
                                "price_unit": abs(diff)
                                * (
                                    diff_lines.volume
                                    / con_lines.total_amount_cost_allocation_method
                                ),
                                "price_subtotal": (
                                    abs(diff)
                                    * (
                                        diff_lines.volume
                                        / con_lines.total_amount_cost_allocation_method
                                    )
                                )
                                * qty,
                                "account_id": diff_lines.product_id.categ_id.property_stock_account_input_categ_id.id,
                            },
                        ]
                    )

                    value_entry = env["stock.valuation.layer"].search(
                        [("stock_move_id", "=", diff_lines.stock_move_id.id)],
                        limit=1,
                    )
                    if value_entry:
                        value_entry.write(
                            {
                                "value": (
                                    value_entry.value
                                    + (
                                        (
                                            abs(diff)
                                            * (
                                                diff_lines.volume
                                                / con_lines.total_amount_cost_allocation_method
                                            )
                                        )
                                        * qty
                                    )
                                ),
                                "unit_cost": (
                                    value_entry.value
                                    + (
                                        (
                                            abs(diff)
                                            * (
                                                diff_lines.volume
                                                / con_lines.total_amount_cost_allocation_method
                                            )
                                        )
                                        * qty
                                    )
                                )
                                / value_entry.quantity,
                                "remaining_value": (
                                    value_entry.value
                                    + (
                                        (
                                            abs(diff)
                                            * (
                                                diff_lines.volume
                                                / con_lines.total_amount_cost_allocation_method
                                            )
                                        )
                                        * qty
                                    )
                                )
                                / value_entry.remaining_qty,
                            }
                        )
            else:
                for diff_lines in con_lines.consignment_line_ids:
                    tp_lines.append(
                        [
                            0,
                            0,
                            {
                                "product_id": diff_lines.product_id.id,
                                "quantity": qty,
                                "currency_id": record.accounting_currency_id.id,
                                "name": diff_lines.product_id.name,
                                "product_uom_id": diff_lines.product_id.uom_id.id,
                                "price_unit": abs(diff)
                                * (
                                    diff_lines.amount
                                    / con_lines.total_amount
                                ),
                                "price_subtotal": (
                                    abs(diff)
                                    * (
                                        diff_lines.amount
                                        / con_lines.total_amount
                                    )
                                )
                                * qty,
                                "account_id": diff_lines.product_id.categ_id.property_stock_account_input_categ_id.id,
                            },
                        ]
                    )

                    value_entry = env["stock.valuation.layer"].search(
                        [("stock_move_id", "=", diff_lines.stock_move_id.id)],
                        limit=1,
                    )
                    if value_entry:
                        value_entry.write(
                            {
                                "value": (
                                    value_entry.value
                                    + (
                                        (
                                            abs(diff)
                                            * (
                                                diff_lines.amount
                                                / con_lines.total_amount
                                            )
                                        )
                                        * qty
                                    )
                                ),
                                "unit_cost": (
                                    value_entry.value
                                    + (
                                        (
                                            abs(diff)
                                            * (
                                                diff_lines.amount
                                                / con_lines.total_amount
                                            )
                                        )
                                        * qty
                                    )
                                )
                                / value_entry.quantity,
                                "remaining_value": (
                                    value_entry.value
                                    + (
                                        (
                                            abs(diff)
                                            * (
                                                diff_lines.amount
                                                / con_lines.total_amount
                                            )
                                        )
                                        * qty
                                    )
                                )
                                / value_entry.remaining_qty,
                            }
                        )

    tp_lines.append(
        [
            0,
            0,
            {
                "account_id": tax_account.import_tp_vendor_account.id,
                "name": "Import TP Invoice - Reversal",
                "quantity": 1.00,
                "currency_id": record.accounting_currency_id.id,
                "price_unit": record.total_original_invoice_amount,
            },
        ]
    )
    #'price_unit':record.total_original_invoice_amount * currency_rate.rate}])

    tp_lines.append(
        [
            0,
            0,
            {
                "account_id": tax_account.x_studio_tp_invoicing_tax_acc.id,
                "name": "Total Tax",
                "quantity": 1.00,
                "currency_id": record.accounting_currency_id.id,
                "price_unit": record.taxes_1,
            },
        ]
    )

    journal = env["account.journal"].search(
        [("name", "=", "TP Vendor Bills"), ("company_id", "=", company.id)], limit=1
    )
    if not journal:
        raise UserError("The required journal has not been setup. Process terminated.")

# … 19 more lines
```
  </details>
- **TP Invoice Currency Update** (`action_tp_invoice_header_tp_invoice_currency_update`, type `code`)
  - Function: Sets the TP invoice's Currency to the selected vendor's purchase currency.
  - Depends on: `model tp_invoice_header`, `tp_invoice_header.accounting_currency_id`, `tp_invoice_header.vendor`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (1 lines)</summary>

```python
record["accounting_currency_id"] = record.vendor.property_purchase_currency_id.id
```
  </details>
- **TP Invoice Seq.No** (`action_tp_invoice_header_tp_invoice_seq_no`, type `code`)
  - Function: When the TP invoice's Name is still 'New', assigns the next number from the 'tp.invoice.seq' sequence.
  - Depends on: `model ir.sequence` (base), `model tp_invoice_header`, `tp_invoice_header.name`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (5 lines)</summary>

```python
# record['name'] = env['ir.sequence'].next_by_code('purchase.request.seq')

if record.name == "New":
    seq = env["ir.sequence"].next_by_code("tp.invoice.seq")
    record.write({"name": seq})
```
  </details>
**Automations (2):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| JIN-Third Party(TP) Invoice Seq.No | `base_automation_65_jin_third_party_tp_invoice_seq_no` |  | When a record is created or updated on TP Invoice Header, runs _Execute Code_. | `model tp_invoice_header`<br>`server action BugFix-Accounting.action_tp_invoice_seq_no`<br>`tp_invoice_header.create_date` |  |
| TP Invoice Currency Update | `automation_tp_invoice_currency_update` |  | When a watched field changes in the form on TP Invoice Header, runs _Execute Code_. | `model tp_invoice_header`<br>`server action BugFix-Accounting.action_tp_invoice_currency_update`<br>`tp_invoice_header.vendor` |  |

**Window actions (5):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| TP Invoice Header | `action_tp_invoice_header` | Opens **TP Invoice Header** records (tree,form). | `model tp_invoice_header` |  |
| TP Invoice Header | `action_tp_invoice_header_2_2` | Opens **TP Invoice Header** records (tree,form). | `model tp_invoice_header` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_imports_tp_invoice_header` (BugFix-Studio-Misc) |
| TP Invoices | `action_tp_invoices` | Opens **TP Invoice Header** records (tree,form), filtered to `[('consignment_header_id', '=', active_id)]`. | `model tp_invoice_header` |  |
| TP Invoices | `action_tp_invoices_2` | Opens **TP Invoice Header** records (tree,form), filtered to `[('con_no', '=', active_id)]`. | `model tp_invoice_header`<br>`tp_invoice_header.con_no` |  |
| tp_invoice_header | `action_tp_invoice_header_2` | Opens **TP Invoice Header** records (tree,form). | `model tp_invoice_header` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_tp_invoice_header` (BugFix-Studio-Misc) |

**Views (7):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for tp_invoice_header | `view_tp_invoice_header_form` | form | full form layout with 3 fields | Base TP Invoice form: a 'Post' header button shown only in Draft status (runs IMP - Post TP Invoice), hidden status field, Invoice Reference title and Archived ribbon. | `server action BugFix-Accounting.srv_tp_invoice_post`<br>`tp_invoice_header.active`<br>`tp_invoice_header.name`<br>`tp_invoice_header.status` | `view BugFix-Accounting.view_default_form_view_for_tp_invoice_header_inherit` |
| Default list view for tp_invoice_header | `view_tp_invoice_header_list` | tree | full tree layout with 2 fields | Base list screen for TP Invoice Header records showing Name with a drag handle for manual ordering by Sequence. | `tp_invoice_header.name`<br>`tp_invoice_header.sequence` | `view BugFix-Accounting.view_default_list_view_for_tp_invoice_header_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_tp_invoice_header_inherit_2` |
| Default search view for tp_invoice_header | `view_tp_invoice_header_search` | search | full search layout with 1 fields | Search bar for TP Invoice Header records: search by Name and an 'Archived' filter to show inactive records. | `tp_invoice_header.active`<br>`tp_invoice_header.name` |  |
| Default search view for tp_invoice_header | `view_tp_invoice_header_search_2` | search | full search layout with 1 fields | Default search view for TP Invoice Header records: search by name plus an Archived filter. | `tp_invoice_header.active`<br>`tp_invoice_header.name` |  |
| Odoo Studio: Default form view for tp_invoice_header customization | `view_default_form_view_for_tp_invoice_header_inherit` | form | after `//header[1]/button[1]`: add field pipeline_status_bar; before `//widget[@name='web_ribbon']`: add div; set force_save=True, readonly=1 on `//form[1]/sheet[1]/div[not(@name)][1]/h1[1]/field[@name='name']`; inside `//group[@name='studio_group_c9cf25_left']`: add field vendor, field accounting_name, field con_no; inside `//group[@name='studio_group_c9cf25_right']`: add field invoice_no, field accounting_invoice_date, field accounting_currency_id, field status; after `//group[@name='studio_group_c9cf25']`: add notebook | TP Invoice Header form: adds a pipeline status bar, a 'Vendor Bill' smart button (when bills exist), makes the reference read-only, and adds Vendor, Name, Consignment No, Invoice No/Date, Currency, Status and a lines notebook. | `view BugFix-Accounting.view_tp_invoice_header_form`<br>`window action BugFix-Accounting.act_tp_invoice_vendor_bill`<br>`tp_invoice_header.con_no`<br>`tp_invoice_header.accounting_currency_id`<br>`tp_invoice_header.accounting_invoice_date`<details><summary>+18 more</summary>`tp_invoice_header.invoice_no`<br>`tp_invoice_header.accounting_name`<br>`tp_invoice_header.pipeline_status_bar`<br>`tp_invoice_header.status`<br>`tp_invoice_header.taxes_1`<br>`tp_invoice_header.total_1`<br>`tp_invoice_header.total_invoice_amount`<br>`tp_invoice_header.tp_lines`<br>`tp_invoice_header.vendor`<br>`tp_invoice_header.tp_id__account_move_count`<br>`tp_invoice_line.name`<br>`tp_invoice_line.charge_group`<br>`tp_invoice_line.charge_name`<br>`tp_invoice_line.invoice_amount`<br>`tp_invoice_line.original_amount`<br>`tp_invoice_line.sequence`<br>`tp_invoice_line.tax_amount`<br>`tp_invoice_line.taxes`</details> |  |
| Odoo Studio: Default list view for tp_invoice_header customization | `view_default_list_view_for_tp_invoice_header_inherit` | tree | set create=false, delete=false on `//tree[1]` | Studio customization of the TP Invoice list: disables creating and deleting TP invoices from the list. | `view BugFix-Accounting.view_tp_invoice_header_list` |  |
| Odoo Studio: Default list view for tp_invoice_header customization | `view_default_list_view_for_tp_invoice_header_inherit_2` | tree | set create=false, delete=false on `//tree[1]`; set column_invisible=1 on `//field[@name='sequence']`; set string=Invoice Reference on `//field[@name='name']`; after `//field[@name='name']`: add field status, field vendor, field invoice_no, field accounting_invoice_date, field accounting_currency_id | TP Invoice Header list (no create/delete): labels Name as 'Invoice Reference' and adds Status, Vendor, Invoice No, Invoice Date and Currency; sequence hidden. | `view BugFix-Accounting.view_tp_invoice_header_list`<br>`tp_invoice_header.accounting_currency_id`<br>`tp_invoice_header.accounting_invoice_date`<br>`tp_invoice_header.invoice_no`<br>`tp_invoice_header.status`<details><summary>+1 more</summary>`tp_invoice_header.vendor`</details> |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| TP Invoice Header group_system | `access_tp_invoice_header_group_system` | Gives **Administration / Settings** read/write/create/delete access to TP Invoice Header records. | `group base.group_system` (base)<br>`model tp_invoice_header` |  |
| TP Invoice Header group_user | `access_tp_invoice_header_group_user` | Gives **User types / Internal User** read access to TP Invoice Header records. | `group base.group_user` (base)<br>`model tp_invoice_header` |  |
| tp_invoice_header user access | `access_tp_invoice_header_user` | Gives **User types / Internal User** read/write/create/delete access to TP Invoice Header records. | `group base.group_user` (base)<br>`model tp_invoice_header` |  |
