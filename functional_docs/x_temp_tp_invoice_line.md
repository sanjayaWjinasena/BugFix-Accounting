# BugFix-Accounting — `x_temp_tp_invoice_line`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_temp_tp_invoice_line` — Temp TP Invoice Line

*Created by this repo.* Python: `models/x_temp_tp_invoice_line.py`, `models/x_temp_tp_invoice_line_gap.py`. Record name field: `x_name`.

Other repos that use this model: `access right BugFix-Studio-Misc.access_g_x_temp_tp_invoice_line_x_temp_tp_invoice_line_purchase_jin_po_invoicing_payment_i` (BugFix-Studio-Misc)<br>`server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:x_temp_tp_invoice_line -->
A consignment charge line offered in the 'Create TP Invoice' wizard, with charge name, group, basis, amount, consignment and original charge record. Lines ticked Select are copied into the new TP invoice; at least one must be ticked or the apply action raises an error.
<!-- /SUMMARY -->

**Fields (28):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard computed field: calendar meeting linked to the next activity on this Temp TP Invoice Line record, if any. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard computed field: due date of the next scheduled activity on this Temp TP Invoice Line record. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard computed flag (Alert or Error) showing that an activity on this Temp TP Invoice Line record is in an exception state. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard computed icon shown when an activity on this Temp TP Invoice Line record is in an exception state. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Scheduled activities (to-dos, calls, meetings) attached to this Temp TP Invoice Line record, from the standard activity mixin. | stored | `model mail.activity` (mail) | `x_temp_tp_invoice_line.activity_summary`<br>`x_temp_tp_invoice_line.activity_type_icon`<br>`x_temp_tp_invoice_line.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard computed activity status of this Temp TP Invoice Line record: Overdue, Today or Planned, based on the nearest activity deadline. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Summary text of the next scheduled activity on this Temp TP Invoice Line record, read via related from its activities. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_temp_tp_invoice_line.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Font Awesome icon of the next activity type on this Temp TP Invoice Line record, read via related from its activities; used for display only. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_temp_tp_invoice_line.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Type of the next scheduled activity on this Temp TP Invoice Line record, read via related from its activities (standard activity mixin). | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_temp_tp_invoice_line.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard computed field: the user responsible for the next scheduled activity on this Temp TP Invoice Line record. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time this Temp TP Invoice Line record was created; set automatically. | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created this Temp TP Invoice Line record; set automatically. | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Standard computed name of the Temp TP Invoice Line record as shown in links and dropdowns. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the Temp TP Invoice Line record, assigned automatically. | stored |  |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard computed field: due date of the current user's next activity on this Temp TP Invoice Line record. | not stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time this Temp TP Invoice Line record was last modified; set automatically. | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last modified this Temp TP Invoice Line record; set automatically. | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Archive flag of the temporary TP invoice charge line; defaults to true (ir.default), and unticked (archived) records are hidden from normal lists. Shown in the form and search views. | stored |  | `default BugFix-Accounting.default_172_x_temp_tp_invoice_line_x_active`<br>`view BugFix-Accounting.ported_default_form_view_fo_8e00b755_fbe6_4921_925a_91bb567326d7`<br>`view BugFix-Accounting.ported_default_search_view__262de343_80f0_46e9_b0a4_3cbfe09d933f`<br>`view BugFix-Accounting.ported_view_3036_default_search_view_262de343_80f0_46e9_b0a4_3cbfe09d933f` |
| `x_name` | Name | char | Name of the temporary TP invoice charge line, used as its display name. Shown in the form, list and search views. | stored |  | `view BugFix-Accounting.ported_default_form_view_fo_8e00b755_fbe6_4921_925a_91bb567326d7`<br>`view BugFix-Accounting.ported_default_list_view_fo_a6e6b3ad_20ca_4271_b887_d78bf98e2073`<br>`view BugFix-Accounting.ported_default_search_view__262de343_80f0_46e9_b0a4_3cbfe09d933f`<br>`view BugFix-Accounting.ported_view_3036_default_search_view_262de343_80f0_46e9_b0a4_3cbfe09d933f` |
| `x_studio_amount` | Amount | float | Charge amount of this consignment charge line; copied as both original and invoice amount into the TP invoice line when selected. Shown in the form view. | stored |  | `view BugFix-Accounting.ported_view_3038_odoo_studio_default_cb099adf_20d3_4e33_8500_801e1c815b1f`<br>`view BugFix-Accounting.ported_view_3041_imp_copy_charges_to_02d06147_ff91_4ff4_bb53_489854bb1ddd` |
| `x_studio_basis` | Basis | selection: Percentage=Percentage; Fixed Per Document=Fixed Per Document | How the charge is calculated: Percentage or Fixed Per Document; copied to the TP invoice line when selected. Shown in the form view. | stored |  | `view BugFix-Accounting.ported_view_3038_odoo_studio_default_cb099adf_20d3_4e33_8500_801e1c815b1f`<br>`view BugFix-Accounting.ported_view_3041_imp_copy_charges_to_02d06147_ff91_4ff4_bb53_489854bb1ddd` |
| `x_studio_charge_group` | Charge Group | selection: None=None; Charges=Charges; Duty=Duty; Taxes=Taxes | Group of the charge (None, Charges, Duty, Taxes); copied to the TP invoice line when selected. Shown in the form view. | stored |  | `view BugFix-Accounting.ported_view_3038_odoo_studio_default_cb099adf_20d3_4e33_8500_801e1c815b1f`<br>`view BugFix-Accounting.ported_view_3041_imp_copy_charges_to_02d06147_ff91_4ff4_bb53_489854bb1ddd` |
| `x_studio_charge_name` | Charge Name | char | Name of the charge; copied to the TP invoice line when selected. Shown in the form view. | stored |  | `view BugFix-Accounting.ported_view_3038_odoo_studio_default_cb099adf_20d3_4e33_8500_801e1c815b1f`<br>`view BugFix-Accounting.ported_view_3041_imp_copy_charges_to_02d06147_ff91_4ff4_bb53_489854bb1ddd` |
| `x_studio_consignment_charge_header_id` | Consignment Charge Header Id | many2one → `x_consignment_charge_h` | Original consignment charge record behind this line; copied to the TP invoice line and flagged as TP processed when the line is applied. Shown in the form view. | stored | `model x_consignment_charge_h` (BugFix-Stock) | `view BugFix-Accounting.ported_view_3038_odoo_studio_default_cb099adf_20d3_4e33_8500_801e1c815b1f`<br>`view BugFix-Accounting.ported_view_3041_imp_copy_charges_to_02d06147_ff91_4ff4_bb53_489854bb1ddd` |
| `x_studio_consignment_id` | Consignment Id | many2one → `x_consignment_header` | Import consignment the charge belongs to; copied to the TP invoice line when selected. Shown in the form view. | stored | `model x_consignment_header` (BugFix-Stock) | `view BugFix-Accounting.ported_view_3038_odoo_studio_default_cb099adf_20d3_4e33_8500_801e1c815b1f`<br>`view BugFix-Accounting.ported_view_3041_imp_copy_charges_to_02d06147_ff91_4ff4_bb53_489854bb1ddd` |
| `x_studio_select` | Select | boolean | Tick box to include this charge in the TP invoice; at least one line must be ticked or "IMP - Apply Selected Charge Lines to TP Invoice" raises an error. Shown in the form view. | stored |  | `view BugFix-Accounting.ported_view_3038_odoo_studio_default_cb099adf_20d3_4e33_8500_801e1c815b1f`<br>`view BugFix-Accounting.ported_view_3041_imp_copy_charges_to_02d06147_ff91_4ff4_bb53_489854bb1ddd` |
| `x_studio_sequence` | Sequence | integer | Sort order of the temporary TP invoice charge line (default 10); used as the drag handle in its list view. | stored |  | `default BugFix-Accounting.default_173_x_temp_tp_invoice_line_x_studio_sequence`<br>`view BugFix-Accounting.ported_default_list_view_fo_a6e6b3ad_20ca_4271_b887_d78bf98e2073` |
| `x_studio_temp_tp_invoice_header_id` | Temp TP Invoice Header Id | many2one → `x_temp_tp_invoice_head` | Temporary TP invoice header (Create TP Invoice popup) this charge line belongs to; inverse of its Charge Line list. Shown in the form view. | stored | `model x_temp_tp_invoice_head` | `view BugFix-Accounting.ported_view_3038_odoo_studio_default_cb099adf_20d3_4e33_8500_801e1c815b1f`<br>`view BugFix-Accounting.ported_view_3041_imp_copy_charges_to_02d06147_ff91_4ff4_bb53_489854bb1ddd` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Temp TP Invoice Line | `action_1376_temp_tp_invoice_line` | Opens **Temp TP Invoice Line** records (tree,form). | `model x_temp_tp_invoice_line` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_temp_tp_invoice_line` (BugFix-Studio-Misc) |

**Views (5):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_temp_tp_invoice_line | `ported_default_form_view_fo_8e00b755_fbe6_4921_925a_91bb567326d7` | form | full form layout with 2 fields | Base form screen for Temp TP Invoice Line records: required Name title, an Archived ribbon when inactive and empty column groups that Studio extensions fill. | `x_temp_tp_invoice_line.x_active`<br>`x_temp_tp_invoice_line.x_name` | `view BugFix-Accounting.ported_view_3038_odoo_studio_default_cb099adf_20d3_4e33_8500_801e1c815b1f` |
| Default list view for x_temp_tp_invoice_line | `ported_default_list_view_fo_a6e6b3ad_20ca_4271_b887_d78bf98e2073` | tree | full tree layout with 2 fields | Base list screen for Temp TP Invoice Line records showing Name with a drag handle for manual ordering by Sequence. | `x_temp_tp_invoice_line.x_name`<br>`x_temp_tp_invoice_line.x_studio_sequence` |  |
| Default search view for x_temp_tp_invoice_line | `ported_default_search_view__262de343_80f0_46e9_b0a4_3cbfe09d933f` | search | full search layout with 1 fields | Search bar for Temp TP Invoice Line records: search by Name and an 'Archived' filter to show inactive records. | `x_temp_tp_invoice_line.x_active`<br>`x_temp_tp_invoice_line.x_name` |  |
| Default search view for x_temp_tp_invoice_line | `ported_view_3036_default_search_view_262de343_80f0_46e9_b0a4_3cbfe09d933f` | search | full search layout with 1 fields | Default search view for Temp TP Invoice Line records: search by name plus an Archived filter. | `x_temp_tp_invoice_line.x_active`<br>`x_temp_tp_invoice_line.x_name` |  |
| Odoo Studio: Default form view for x_temp_tp_invoice_line customization | `ported_view_3038_odoo_studio_default_cb099adf_20d3_4e33_8500_801e1c815b1f` | form | inside `//group[@name='studio_group_0b2b4a_left']`: add field x_studio_temp_tp_invoice_header_id, field x_studio_select, field x_studio_amount, field x_studio_basis, field x_studio_charge_group, field x_studio_charge_name, field x_studio_consignment_id, field x_studio_consignment_charge_header_id | Temp TP Invoice Line form: adds the read-only parent header, Select flag, Amount, Basis, Charge Group, Charge Name, Consignment and Consignment Charge Header fields. | `view BugFix-Accounting.ported_default_form_view_fo_8e00b755_fbe6_4921_925a_91bb567326d7`<br>`x_temp_tp_invoice_line.x_studio_amount`<br>`x_temp_tp_invoice_line.x_studio_basis`<br>`x_temp_tp_invoice_line.x_studio_charge_group`<br>`x_temp_tp_invoice_line.x_studio_charge_name`<details><summary>+4 more</summary>`x_temp_tp_invoice_line.x_studio_consignment_charge_header_id`<br>`x_temp_tp_invoice_line.x_studio_consignment_id`<br>`x_temp_tp_invoice_line.x_studio_select`<br>`x_temp_tp_invoice_line.x_studio_temp_tp_invoice_header_id`</details> |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Temp TP Invoice Line group_system | `access_1368_temp_tp_invoice_line_group_system` | Gives **Administration / Settings** read/write/create/delete access to Temp TP Invoice Line records. | `group base.group_system` (base)<br>`model x_temp_tp_invoice_line` |  |
| Temp TP Invoice Line group_user | `access_1369_temp_tp_invoice_line_group_user` | Gives **User types / Internal User** read access to Temp TP Invoice Line records. | `group base.group_user` (base)<br>`model x_temp_tp_invoice_line` |  |
| x_temp_tp_invoice_line user access | `access_x_temp_tp_invoice_line_user` | Gives **User types / Internal User** read/write/create/delete access to Temp TP Invoice Line records. | `group base.group_user` (base)<br>`model x_temp_tp_invoice_line` |  |
