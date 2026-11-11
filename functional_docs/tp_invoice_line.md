# BugFix-Accounting — `tp_invoice_line`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `tp_invoice_line` — TP Invoice Line

*Created by this repo.* Python: `models/tp_invoice_line.py`, `models/x_tp_invoice_line_gap.py`. Record name field: `name`.

Other repos that use this model: `access right BugFix-Studio-Misc.access_g_tp_invoice_line_tp_invoice_line_purchase_jin_po_invoicing_payment_import` (BugFix-Studio-Misc)<br>`server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:tp_invoice_line -->
A charge line of a TP Invoice, with charge name, group, basis, original and invoice amounts, taxes, tax amount and links to the consignment and its charge record. Changing the taxes triggers the 'TP Invoice LineTAX Update' automation, which sets Tax Amount to the invoice amount times each selected tax rate. Line amounts are summed into the header totals.
<!-- /SUMMARY -->

**Fields (43):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Calendar meeting linked to the next activity, if any (standard activity mixin). | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Due date of the next scheduled activity on the line (standard activity mixin, computed). | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard activity mixin flag (Alert or Error) shown when an activity is in an exception state. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Icon displayed for an exception activity on the line (standard activity mixin). | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Activities (to-dos, calls, etc.) scheduled on this TP Invoice Line, from the standard mail activity mixin; shown in the form chatter. | stored | `model mail.activity` (mail) | `view BugFix-Accounting.view_tp_invoice_line_form`<br>`tp_invoice_line.activity_summary`<br>`tp_invoice_line.activity_type_icon`<br>`tp_invoice_line.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity mixin status computed from the next activity's due date: Overdue, Today or Planned. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Summary text of the next scheduled activity, taken from the activities via related field (standard mixin). | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`tp_invoice_line.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Font Awesome icon of the next activity type, taken from the activities via related field (standard mixin). | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`tp_invoice_line.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Type of the next scheduled activity, taken from the line's activities via related field (standard mixin). | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`tp_invoice_line.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | User responsible for the next scheduled activity on the line (standard activity mixin field). | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the TP Invoice Line was created (standard audit field set automatically). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the TP Invoice Line record (standard audit field set automatically). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the TP Invoice Line record in lookups and breadcrumbs, computed by Odoo (standard field). | not stored |  |  |
| `has_message` | Has Message | boolean | Whether the line has any chatter messages (standard mail thread, computed). | not stored |  |  |
| `id` | ID | integer | Technical unique database ID of the TP Invoice Line record (standard Odoo field). | stored |  |  |
| `message_attachment_count` | Attachment Count | integer | Number of attachments on the line's chatter (standard mail thread). | not stored |  |  |
| `message_follower_ids` | Followers | one2many → `mail.followers` | Followers subscribed to this TP Invoice Line's chatter (standard mail thread); shown in the form chatter. | stored | `model mail.followers` (mail) | `view BugFix-Accounting.view_tp_invoice_line_form` |
| `message_has_error` | Message Delivery error | boolean | True when some chatter messages on the line failed to be delivered (standard mail thread). | not stored |  |  |
| `message_has_error_counter` | Number of errors | integer | Number of chatter messages on the line with delivery errors (standard mail thread). | not stored |  |  |
| `message_has_sms_error` | SMS Delivery error | boolean | True when an SMS sent from this line failed to be delivered (standard SMS mixin). | not stored |  |  |
| `message_ids` | Messages | one2many → `mail.message` | Chatter messages and log notes posted on this TP Invoice Line (standard mail thread); shown in the form. | stored | `model mail.message` (mail) | `view BugFix-Accounting.view_tp_invoice_line_form` |
| `message_is_follower` | Is Follower | boolean | Whether the current user follows this TP Invoice Line (standard mail thread field). | not stored |  |  |
| `message_needaction` | Action Needed | boolean | True when the line has unread messages requiring the current user's attention (standard mail thread). | not stored |  |  |
| `message_needaction_counter` | Number of Actions | integer | Number of messages on the line that require action (standard mail thread). | not stored |  |  |
| `message_partner_ids` | Followers (Partners) | many2many → `res.partner` | Partners following this TP Invoice Line (standard mail thread, computed from followers). | not stored | `model res.partner` (base) |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Due date of the next activity assigned to the current user (standard activity mixin, computed). | not stored |  |  |
| `rating_ids` | Ratings | one2many → `rating.rating` | Customer ratings linked to the line (standard rating mixin); not used by any view or logic here. | stored | `model rating.rating` (rating) |  |
| `website_message_ids` | Website Messages | one2many → `mail.message` | Chatter messages visible on the website for this line (standard mail thread). | stored | `model mail.message` (mail) |  |
| `write_date` | Last Updated on | datetime | Date and time the TP Invoice Line record was last modified (standard audit field). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last modified the TP Invoice Line record (standard audit field set automatically). | stored | `model res.users` (base) |  |
| `active` | Active | boolean | Archive flag of the TP Invoice Line; default set via ir.default, unchecking it hides the line from normal searches (used by the form and search views). | stored |  | `default BugFix-Accounting.default_tp_invoice_line_active`<br>`view BugFix-Accounting.view_tp_invoice_line_form`<br>`view BugFix-Accounting.view_tp_invoice_line_search` |
| `name` | Name | char | Name/description of the TP Invoice Line, entered by the user and shown in the line's list, form and search views. | stored |  | `view BugFix-Accounting.view_default_form_view_for_tp_invoice_header_inherit`<br>`view BugFix-Accounting.view_tp_invoice_line_list`<br>`view BugFix-Accounting.view_tp_invoice_line_form`<br>`view BugFix-Accounting.view_tp_invoice_line_search` |
| `basis` | Basis | selection: Percentage=Percentage; Fixed Per Document=Fixed Per Document | How the charge is calculated: Percentage or Fixed Per Document; entered by the user on the line. | stored |  | `view BugFix-Accounting.view_default_form_view_for_tp_invoice_line_inherit` |
| `charge_group` | Charge Group | selection: None=None; Charges=Charges; Duty=Duty; Taxes=Taxes | Category of the charge on the line: None, Charges, Duty or Taxes; selected by the user. | stored |  | `view BugFix-Accounting.view_default_form_view_for_tp_invoice_header_inherit`<br>`view BugFix-Accounting.view_default_form_view_for_tp_invoice_line_inherit` |
| `charge_name` | Charge Name | char | Free-text name of the charge being invoiced on this TP line. | stored |  | `view BugFix-Accounting.view_default_form_view_for_tp_invoice_header_inherit`<br>`view BugFix-Accounting.view_default_form_view_for_tp_invoice_line_inherit` |
| `consignment_charge_header_id` | Consignment Charge Header Id | many2one → `consignment_charge_h` | Consignment charge header (consignment_charge_h) this TP line relates to. | stored | `model consignment_charge_h` (BugFix-Stock) | `view BugFix-Accounting.view_default_form_view_for_tp_invoice_line_inherit` |
| `consignment_id` | Consignment Id | many2one → `consignment_header` | Consignment (consignment_header) this third-party charge line belongs to. | stored | `model consignment_header` (BugFix-Stock) | `view BugFix-Accounting.view_default_form_view_for_tp_invoice_line_inherit` |
| `invoice_amount` | Invoice Amount | float | Untaxed amount of this charge line; summed into the header's Untaxed Amount and used by the LineTAX Update action to compute Tax Amount. | stored |  | `server action BugFix-Accounting.action_tp_invoice_line_tp_invoice_linetax_update`<br>`server action BugFix-Accounting.action_tp_invoice_linetax_update`<br>`view BugFix-Accounting.view_default_form_view_for_tp_invoice_header_inherit`<br>`view BugFix-Accounting.view_default_form_view_for_tp_invoice_line_inherit`<br>`tp_invoice_header._compute_taxes_1()`<details><summary>+1 more</summary>`tp_invoice_header._compute_total_invoice_amount()`</details> |
| `original_amount` | Original Amount | float | Original amount of the charge before adjustment; summed into the header's Total Original Invoice Amount. | stored |  | `view BugFix-Accounting.view_default_form_view_for_tp_invoice_header_inherit`<br>`view BugFix-Accounting.view_default_form_view_for_tp_invoice_line_inherit`<br>`tp_invoice_header._compute_total_original_invoice_amount()` |
| `sequence` | Sequence | integer | Sort order of the TP Invoice Line (default 10), used for drag-and-drop ordering in the list. | default `10`; stored |  | `default BugFix-Accounting.default_tp_invoice_line_sequence`<br>`view BugFix-Accounting.view_default_form_view_for_tp_invoice_header_inherit`<br>`view BugFix-Accounting.view_tp_invoice_line_list` |
| `tax_amount` | Tax Amount | float | Tax amount for the line, written by the TP Invoice LineTAX Update action as Invoice Amount times each selected tax rate; summed into the header Taxes. | stored |  | `server action BugFix-Accounting.action_tp_invoice_line_tp_invoice_linetax_update`<br>`server action BugFix-Accounting.action_tp_invoice_linetax_update`<br>`view BugFix-Accounting.view_default_form_view_for_tp_invoice_header_inherit` |
| `taxes` | Taxes | many2many → `account.tax` | Taxes applied to the line, chosen by the user; changing them triggers the LineTAX Update automation that recalculates Tax Amount. | stored | `model account.tax` (account) | `automation BugFix-Accounting.automation_tp_invoice_linetax_update`<br>`server action BugFix-Accounting.action_tp_invoice_line_tp_invoice_linetax_update`<br>`server action BugFix-Accounting.action_tp_invoice_linetax_update`<br>`view BugFix-Accounting.view_default_form_view_for_tp_invoice_header_inherit`<br>`tp_invoice_header._compute_taxes_1()` |
| `tp_invoice_header_id` | TP Invoice Header Id | many2one → `tp_invoice_header` | Parent TP Invoice Header this line belongs to (inverse of TP Lines). | stored | `model tp_invoice_header` | `view BugFix-Accounting.view_default_form_view_for_tp_invoice_line_inherit` |

**Server actions (2):**

- **Execute Code** (`action_tp_invoice_linetax_update`, type `code`)
  - Function: Run when TP line taxes change: sets Tax Amount to Invoice Amount times each selected tax percentage, summed.
  - Depends on: `model account.tax` (account), `model tp_invoice_line`, `tp_invoice_line.invoice_amount`, `tp_invoice_line.tax_amount`, `tp_invoice_line.taxes`
  - Used by: `automation BugFix-Accounting.automation_tp_invoice_linetax_update`
  <details><summary>code (10 lines)</summary>

```python
# if record.taxes.id:
taxes = 0
if record.taxes != []:
    for ids in record.taxes:
        tax = env["account.tax"].search([("id", "=", ids._origin.id)], limit=1)
        if tax:
            taxes += record.invoice_amount * (tax.amount / 100)

record.write({"tax_amount": taxes})
```
  </details>
- **TP Invoice LineTAX Update** (`action_tp_invoice_line_tp_invoice_linetax_update`, type `code`)
  - Function: Recalculates the line's Tax Amount as Invoice Amount multiplied by each selected tax's percentage, summed over all taxes.
  - Depends on: `model account.tax` (account), `model tp_invoice_line`, `tp_invoice_line.invoice_amount`, `tp_invoice_line.tax_amount`, `tp_invoice_line.taxes`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (9 lines)</summary>

```python
# if record.taxes.id:
taxes = 0
if record.taxes != []:
    for ids in record.taxes:
        tax = env["account.tax"].search([("id", "=", ids._origin.id)], limit=1)
        if tax:
            taxes += record.invoice_amount * (tax.amount / 100)

record.write({"tax_amount": taxes})
```
  </details>
**Automations (1):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| TP Invoice LineTAX Update | `automation_tp_invoice_linetax_update` |  | When a watched field changes in the form on TP Invoice Line, runs _Execute Code_. | `model tp_invoice_line`<br>`server action BugFix-Accounting.action_tp_invoice_linetax_update`<br>`tp_invoice_line.taxes` |  |

**Window actions (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| TP Invoice Line | `action_tp_invoice_line` | Opens **TP Invoice Line** records (tree,form). | `model tp_invoice_line` | `menu BugFix-Accounting.menu_tp_invoice_line_2`<br>`menu BugFix-Studio-Misc.menu_f6r2_test_app_05_imports_tp_invoice_line` (BugFix-Studio-Misc) |
| TP Invoice Line | `action_tp_invoice_line_2` | Opens **TP Invoice Line** records (tree,form). | `model tp_invoice_line` | `menu BugFix-Accounting.menu_tp_invoice_line` |

**Views (4):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for tp_invoice_line | `view_tp_invoice_line_form` | form | full form layout with 5 fields | Default form for TP Invoice Line: archived ribbon, required Name title, two empty groups and chatter; extended by its Studio customization. | `tp_invoice_line.activity_ids`<br>`tp_invoice_line.message_follower_ids`<br>`tp_invoice_line.message_ids`<br>`tp_invoice_line.active`<br>`tp_invoice_line.name` | `view BugFix-Accounting.view_default_form_view_for_tp_invoice_line_inherit` |
| Default list view for tp_invoice_line | `view_tp_invoice_line_list` | tree | full tree layout with 2 fields | Default list for TP Invoice Line with sequence handle and Name. | `tp_invoice_line.name`<br>`tp_invoice_line.sequence` |  |
| Default search view for tp_invoice_line | `view_tp_invoice_line_search` | search | full search layout with 1 fields | Default search view for TP Invoice Line records: search by name plus an Archived filter. | `tp_invoice_line.active`<br>`tp_invoice_line.name` |  |
| Odoo Studio: Default form view for tp_invoice_line customization | `view_default_form_view_for_tp_invoice_line_inherit` | form | set invisible=1, required= on `//field[@name='name']`; inside `//group[@name='studio_group_6de1a3_left']`: add field charge_group, field charge_name, field original_amount, field invoice_amount, field basis, field consignment_id, field consignment_charge_header_id, field tp_invoice_header_id | TP Invoice Line form: hides Name and shows read-only Charge Group, Charge Name and Original Amount with an editable Invoice Amount; basis, consignment, charge header and TP header links are hidden. | `view BugFix-Accounting.view_tp_invoice_line_form`<br>`tp_invoice_line.basis`<br>`tp_invoice_line.charge_group`<br>`tp_invoice_line.charge_name`<br>`tp_invoice_line.consignment_charge_header_id`<details><summary>+4 more</summary>`tp_invoice_line.consignment_id`<br>`tp_invoice_line.invoice_amount`<br>`tp_invoice_line.original_amount`<br>`tp_invoice_line.tp_invoice_header_id`</details> |  |

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| TP Invoice Line group_system | `access_tp_invoice_line_group_system` | Gives **Administration / Settings** read/write/create/delete access to TP Invoice Line records. | `group base.group_system` (base)<br>`model tp_invoice_line` |  |
| TP Invoice Line group_user | `access_tp_invoice_line_group_user` | Gives **User types / Internal User** read access to TP Invoice Line records. | `group base.group_user` (base)<br>`model tp_invoice_line` |  |
