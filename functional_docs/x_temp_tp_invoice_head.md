# BugFix-Accounting — `x_temp_tp_invoice_head`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_temp_tp_invoice_head` — Temp TP Invoice Header

*Created by this repo.* Python: `models/x_temp_tp_invoice_head.py`, `models/x_temp_tp_invoice_head_gap.py`. Record name field: `x_name`.

Other repos that use this model: `access right BugFix-Studio-Misc.access_g_x_temp_tp_invoice_head_x_temp_tp_invoice_head_purchase_jin_po_invoicing_payment_i` (BugFix-Studio-Misc)<br>`server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:x_temp_tp_invoice_head -->
The temporary header of the 'Create TP Invoice' wizard for an import consignment, holding the consignment, the supplier and the offered charge lines. Its Apply button runs 'IMP - Apply Selected Charge Lines to TP Invoice', which turns the ticked charge lines into a new TP Invoice for the supplier, flags the charges as TP processed, sets the consignment status to TP Invoice and deletes the wizard record.
<!-- /SUMMARY -->

**Fields (23):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard computed field: calendar meeting linked to the next activity on this Temp TP Invoice Header record, if any. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard computed field: due date of the next scheduled activity on this Temp TP Invoice Header record. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard computed flag (Alert or Error) showing that an activity on this Temp TP Invoice Header record is in an exception state. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard computed icon shown when an activity on this Temp TP Invoice Header record is in an exception state. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Scheduled activities (to-dos, calls, meetings) attached to this Temp TP Invoice Header record, from the standard activity mixin. | stored | `model mail.activity` (mail) | `x_temp_tp_invoice_head.activity_summary`<br>`x_temp_tp_invoice_head.activity_type_icon`<br>`x_temp_tp_invoice_head.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard computed activity status of this Temp TP Invoice Header record: Overdue, Today or Planned, based on the nearest activity deadline. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Summary text of the next scheduled activity on this Temp TP Invoice Header record, read via related from its activities. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_temp_tp_invoice_head.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Font Awesome icon of the next activity type on this Temp TP Invoice Header record, read via related from its activities; used for display only. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_temp_tp_invoice_head.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Type of the next scheduled activity on this Temp TP Invoice Header record, read via related from its activities (standard activity mixin). | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_temp_tp_invoice_head.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard computed field: the user responsible for the next scheduled activity on this Temp TP Invoice Header record. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time this Temp TP Invoice Header record was created; set automatically. | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created this Temp TP Invoice Header record; set automatically. | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Standard computed name of the Temp TP Invoice Header record as shown in links and dropdowns. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the Temp TP Invoice Header record, assigned automatically. | stored |  |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard computed field: due date of the current user's next activity on this Temp TP Invoice Header record. | not stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time this Temp TP Invoice Header record was last modified; set automatically. | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last modified this Temp TP Invoice Header record; set automatically. | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Archive flag of the temporary TP invoice header (Create TP Invoice popup); defaults to true (ir.default), and unticked (archived) records are hidden from normal lists. Shown in the search view. | stored |  | `default BugFix-Accounting.default_170_x_temp_tp_invoice_head_x_active`<br>`view BugFix-Accounting.ported_default_search_view__7a379603_7a3e_4f48_9edf_8ef493282a72`<br>`view BugFix-Accounting.ported_view_3033_default_search_view_7a379603_7a3e_4f48_9edf_8ef493282a72` |
| `x_name` | Name | char | Name of the temporary TP invoice header; shown in its list and search views. The header record is deleted once the TP invoice is created. | stored |  | `view BugFix-Accounting.ported_default_list_view_fo_e0a7e6f6_d908_4a20_91b6_3b7c31955737`<br>`view BugFix-Accounting.ported_default_search_view__7a379603_7a3e_4f48_9edf_8ef493282a72`<br>`view BugFix-Accounting.ported_view_3033_default_search_view_7a379603_7a3e_4f48_9edf_8ef493282a72` |
| `x_studio_charge_line` | Charge Line | one2many → `x_temp_tp_invoice_line` | Consignment charge lines offered in the Create TP Invoice popup; lines ticked "Select" are copied into the new TP invoice by "IMP - Apply Selected Charge Lines to TP Invoice". Shown in the form view. | stored | `model x_temp_tp_invoice_line` | `server action BugFix-Accounting.server_action_1378_imp_apply_selected_charge_lines_to_tp_invoice`<br>`server action BugFix-Accounting.srv_tp_invoice_apply_charges`<br>`view BugFix-Accounting.ported_view_3041_imp_copy_charges_to_02d06147_ff91_4ff4_bb53_489854bb1ddd` |
| `x_studio_consignment_header_id` | Consignment Header Id | many2one → `x_consignment_header` | Import consignment the TP invoice is being created for; becomes the TP invoice's consignment link, supplies its supplier invoice no/date, and the consignment status is set to "TP Invoice". Shown in the form view. | stored | `model x_consignment_header` (BugFix-Stock) | `server action BugFix-Accounting.server_action_1378_imp_apply_selected_charge_lines_to_tp_invoice`<br>`server action BugFix-Accounting.srv_tp_invoice_apply_charges`<br>`view BugFix-Accounting.ported_imp_copy_charges_to__02d06147_ff91_4ff4_bb53_489854bb1ddd`<br>`view BugFix-Accounting.ported_view_3041_imp_copy_charges_to_02d06147_ff91_4ff4_bb53_489854bb1ddd` |
| `x_studio_sequence` | Sequence | integer | Sort order of the temporary TP invoice header (Create TP Invoice popup) (default 10); used as the drag handle in its list view. | default `10`; stored |  | `default BugFix-Accounting.default_171_x_temp_tp_invoice_head_x_studio_sequence`<br>`view BugFix-Accounting.ported_default_list_view_fo_e0a7e6f6_d908_4a20_91b6_3b7c31955737` |
| `x_studio_supplier_id` | Vendor | many2one → `res.partner` | Vendor for the TP invoice to be created; copied to the new TP invoice, and the vendor's purchase currency becomes its currency. Shown in the form view. | stored | `model res.partner` (base) | `server action BugFix-Accounting.server_action_1378_imp_apply_selected_charge_lines_to_tp_invoice`<br>`server action BugFix-Accounting.srv_tp_invoice_apply_charges`<br>`view BugFix-Accounting.ported_imp_copy_charges_to__02d06147_ff91_4ff4_bb53_489854bb1ddd`<br>`view BugFix-Accounting.ported_view_3041_imp_copy_charges_to_02d06147_ff91_4ff4_bb53_489854bb1ddd` |

**Server actions (2):**

- **IMP - Apply Selected Charge Lines to TP Invoice** (`srv_tp_invoice_apply_charges`, type `code`)
  - Function: Wizard action: turns the selected consignment charge lines into a new TP Invoice (vendor, currency, invoice no/date from consignment), flags charges as TP processed, sets the consignment status to TP Invoice, deletes the wizard and opens the TP invoice.
  - Depends on: `model x_consignment_charge_h` (BugFix-Stock), `model x_consignment_header` (BugFix-Stock), `model x_temp_tp_invoice_head`, `model x_tp_invoice_header`, `x_temp_tp_invoice_head.x_studio_charge_line`<details><summary>+2 more</summary>`x_temp_tp_invoice_head.x_studio_consignment_header_id`, `x_temp_tp_invoice_head.x_studio_supplier_id`</details>
  - Used by: `view BugFix-Accounting.ported_view_3041_imp_copy_charges_to_02d06147_ff91_4ff4_bb53_489854bb1ddd`
  <details><summary>code (59 lines)</summary>

```python

lines = []
select = 0

for valid_line in record.x_studio_charge_line:
    if valid_line.x_studio_select == True:
        select += 1
        lines.append([0, 0, {
            'x_studio_consignment_charge_header_id': valid_line.x_studio_consignment_charge_header_id.id,
            'x_studio_consignment_id': valid_line.x_studio_consignment_id.id,
            'x_studio_charge_group': valid_line.x_studio_charge_group,
            'x_studio_charge_name': valid_line.x_studio_charge_name,
            'x_studio_basis': valid_line.x_studio_basis,
            'x_studio_original_amount': valid_line.x_studio_amount,
            'x_studio_invoice_amount': valid_line.x_studio_amount,
        }])

        charge_line = env['x_consignment_charge_h'].search([('id', '=', valid_line.x_studio_consignment_charge_header_id.id)])
        if charge_line:
            charge_line.write({'x_studio_tp_processed': True})

if select == 0:
    raise UserError("Atleast One Line Should be Selected to Proceed.")

con_header = env['x_consignment_header'].search([('id', '=', record.x_studio_consignment_header_id.id)], limit=1)

if con_header:
    tp_invoice = env['x_tp_invoice_header'].create({
        'x_studio_con_no': record.x_studio_consignment_header_id.id,
        'x_studio_vendor': record.x_studio_supplier_id.id,
        'x_studio_currency_id': record.x_studio_supplier_id.property_purchase_currency_id.id,
        'x_studio_invoice_no': con_header.x_studio_supplier_invoice_number,
        'x_studio_invoice_date': con_header.x_studio_invoice_date,
        'x_studio_tp_lines': lines,
    })
else:
    tp_invoice = env['x_tp_invoice_header'].create({
        'x_studio_con_no': record.x_studio_consignment_header_id.id,
        'x_studio_vendor': record.x_studio_supplier_id.id,
        'x_studio_currency_id': record.x_studio_supplier_id.property_purchase_currency_id.id,
        'x_studio_tp_lines': lines,
    })

if con_header:
    con_header.write({'x_studio_status': 'TP Invoice', 'x_studio_status_bar': 'TP Invoice'})

if record.id:
    temp_rec = env['x_temp_tp_invoice_head'].search([('id', '=', record.id)], limit=1)
    temp_rec.unlink()

action = {
    'name': 'TP Invoice',
    'domain': [('id', '=', tp_invoice.id)],
    'type': 'ir.actions.act_window',
    'res_model': 'x_tp_invoice_header',
    'view_mode': 'tree,form',
    'view_id': False,
    'context': False,
}
```
  </details>
- **IMP - Apply Selected Charge Lines to TP Invoice** (`server_action_1378_imp_apply_selected_charge_lines_to_tp_invoice`, type `code`)
  - Function: Legacy wizard action: converts selected consignment charge lines into a new TP Invoice, flags the charges as TP processed, sets the consignment status to TP Invoice, deletes the wizard and opens the TP invoice.
  - Depends on: `model x_consignment_charge_h` (BugFix-Stock), `model x_consignment_header` (BugFix-Stock), `model x_temp_tp_invoice_head`, `model x_tp_invoice_header`, `x_temp_tp_invoice_head.x_studio_charge_line`<details><summary>+2 more</summary>`x_temp_tp_invoice_head.x_studio_consignment_header_id`, `x_temp_tp_invoice_head.x_studio_supplier_id`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (47 lines)</summary>

```python
lines=[]
select = 0

for valid_line in record.x_studio_charge_line:
  if (valid_line.x_studio_select == True):
    select += 1
    lines.append([0,0,{
      'x_studio_consignment_charge_header_id':valid_line.x_studio_consignment_charge_header_id.id,
      'x_studio_consignment_id':valid_line.x_studio_consignment_id.id,
      'x_studio_charge_group':valid_line.x_studio_charge_group,
      'x_studio_charge_name':valid_line.x_studio_charge_name,
      'x_studio_basis':valid_line.x_studio_basis,
      'x_studio_original_amount':valid_line.x_studio_amount,
      'x_studio_invoice_amount':valid_line.x_studio_amount}])
      
    charge_line = env['x_consignment_charge_h'].search([('id', '=', valid_line.x_studio_consignment_charge_header_id.id)])
    if charge_line:
      charge_line.write({'x_studio_tp_processed':True})
 
if select == 0:
 raise UserError("Atleast One Line Should be Selected to Proceed.")

con_header = env['x_consignment_header'].search([('id', '=', record.x_studio_consignment_header_id.id)],limit=1)

#tp_invoice = env['x_tp_invoice_header'].create({'x_studio_con_no':record.x_studio_consignment_header_id.id,'x_studio_vendor':record.x_studio_supplier_id.id,'x_studio_currency_id':record.x_studio_consignment_header_id.x_studio_currency_id.id,'x_studio_tp_lines':lines})
if con_header:
  tp_invoice = env['x_tp_invoice_header'].create({'x_studio_con_no':record.x_studio_consignment_header_id.id,'x_studio_vendor':record.x_studio_supplier_id.id,'x_studio_currency_id':record.x_studio_supplier_id.property_purchase_currency_id.id,'x_studio_invoice_no':con_header.x_studio_supplier_invoice_number,'x_studio_invoice_date':con_header.x_studio_invoice_date,'x_studio_tp_lines':lines})
else:
  tp_invoice = env['x_tp_invoice_header'].create({'x_studio_con_no':record.x_studio_consignment_header_id.id,'x_studio_vendor':record.x_studio_supplier_id.id,'x_studio_currency_id':record.x_studio_supplier_id.property_purchase_currency_id.id,'x_studio_tp_lines':lines})
#con_header = env['x_consignment_header'].search([('id', '=', record.x_studio_consignment_header_id.id)],limit=1)
if con_header:
  con_header.write({'x_studio_status':'TP Invoice','x_studio_status_bar':'TP Invoice'})

if record.id:
  temp_rec = env['x_temp_tp_invoice_head'].search([('id', '=', record.id)],limit=1)
  temp_rec.unlink()

action = {
          'name': 'TP Invoice',
          'domain': [('id', '=', tp_invoice.id)],
          'type': 'ir.actions.act_window',
          'res_model': 'x_tp_invoice_header',
          'view_mode': 'tree,form',
          'view_type': 'form',
          'view_id': False,
          'context': False,
          }
```
  </details>
**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Temp TP Invoice Header | `action_1375_temp_tp_invoice_header` | Opens **Temp TP Invoice Header** records (tree,form). | `model x_temp_tp_invoice_head` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_temp_tp_invoice_header` (BugFix-Studio-Misc) |

**Views (5):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default list view for x_temp_tp_invoice_head | `ported_default_list_view_fo_e0a7e6f6_d908_4a20_91b6_3b7c31955737` | tree | full tree layout with 2 fields | Base list screen for Temp TP Invoice Header records showing Name with a drag handle for manual ordering by Sequence. | `x_temp_tp_invoice_head.x_name`<br>`x_temp_tp_invoice_head.x_studio_sequence` |  |
| Default search view for x_temp_tp_invoice_head | `ported_default_search_view__7a379603_7a3e_4f48_9edf_8ef493282a72` | search | full search layout with 1 fields | Search bar for Temp TP Invoice Header records: search by Name and an 'Archived' filter to show inactive records. | `x_temp_tp_invoice_head.x_active`<br>`x_temp_tp_invoice_head.x_name` |  |
| Default search view for x_temp_tp_invoice_head | `ported_view_3033_default_search_view_7a379603_7a3e_4f48_9edf_8ef493282a72` | search | full search layout with 1 fields | Default search view for Temp TP Invoice Header (wizard) records: search by name plus an Archived filter. | `x_temp_tp_invoice_head.x_active`<br>`x_temp_tp_invoice_head.x_name` |  |
| IMP Copy Charges to TP Invoice | `ported_imp_copy_charges_to__02d06147_ff91_4ff4_bb53_489854bb1ddd` | form | full form layout with 2 fields | 'Create TP Invoice' wizard form for copying consignment charges: asks for a required Supplier (consignment link kept hidden) with a Cancel button. | `x_temp_tp_invoice_head.x_studio_consignment_header_id`<br>`x_temp_tp_invoice_head.x_studio_supplier_id` |  |
| IMP Copy Charges to TP Invoice | `ported_view_3041_imp_copy_charges_to_02d06147_ff91_4ff4_bb53_489854bb1ddd` | form | full form layout with 11 fields | 'Create TP Invoice' wizard form for import consignments: pick the Supplier, tick charge lines (read-only group, name, amount) to copy, then Apply runs a server action to build the TP invoice; Cancel closes it. | `server action BugFix-Accounting.srv_tp_invoice_apply_charges`<br>`x_temp_tp_invoice_head.x_studio_charge_line`<br>`x_temp_tp_invoice_head.x_studio_consignment_header_id`<br>`x_temp_tp_invoice_head.x_studio_supplier_id`<br>`x_temp_tp_invoice_line.x_studio_amount`<details><summary>+7 more</summary>`x_temp_tp_invoice_line.x_studio_basis`<br>`x_temp_tp_invoice_line.x_studio_charge_group`<br>`x_temp_tp_invoice_line.x_studio_charge_name`<br>`x_temp_tp_invoice_line.x_studio_consignment_charge_header_id`<br>`x_temp_tp_invoice_line.x_studio_consignment_id`<br>`x_temp_tp_invoice_line.x_studio_select`<br>`x_temp_tp_invoice_line.x_studio_temp_tp_invoice_header_id`</details> |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Temp TP Invoice Header group_system | `access_1366_temp_tp_invoice_header_group_system` | Gives **Administration / Settings** read/write/create/delete access to Temp TP Invoice Header records. | `group base.group_system` (base)<br>`model x_temp_tp_invoice_head` |  |
| Temp TP Invoice Header group_user | `access_1367_temp_tp_invoice_header_group_user` | Gives **User types / Internal User** read access to Temp TP Invoice Header records. | `group base.group_user` (base)<br>`model x_temp_tp_invoice_head` |  |
| x_temp_tp_invoice_head user access | `access_x_temp_tp_invoice_head_user` | Gives **User types / Internal User** read/write/create/delete access to Temp TP Invoice Header records. | `group base.group_user` (base)<br>`model x_temp_tp_invoice_head` |  |
