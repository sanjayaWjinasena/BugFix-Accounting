# BugFix-Accounting — `rm_customer_wise_inv`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `rm_customer_wise_inv` — RM Customer wise Invoices

*Created by this repo.* Python: `models/rm_customer_wise_inv.py`, `models/x_rm_customer_wise_inv_gap.py`. Record name field: `name`.

Other repos that use this model: `server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:rm_customer_wise_inv -->
A summary line of the 'Customer wise Invoices' report run from a Sales Report Model, giving one customer's total invoice amount. Lines are filled by the 'RPT - Customer wise Invoices - Generate' action and removed by its Clear action.
<!-- /SUMMARY -->

**Fields (23):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard computed field: calendar meeting linked to the next activity on this RM Customer wise Invoices record, if any. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard computed field: due date of the next scheduled activity on this RM Customer wise Invoices record. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard computed flag (Alert or Error) showing that an activity on this RM Customer wise Invoices record is in an exception state. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard computed icon shown when an activity on this RM Customer wise Invoices record is in an exception state. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Scheduled activities (to-dos, calls, meetings) attached to this RM Customer wise Invoices record, from the standard activity mixin. | stored | `model mail.activity` (mail) | `rm_customer_wise_inv.activity_summary`<br>`rm_customer_wise_inv.activity_type_icon`<br>`rm_customer_wise_inv.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard computed activity status of this RM Customer wise Invoices record: Overdue, Today or Planned, based on the nearest activity deadline. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Summary text of the next scheduled activity on this RM Customer wise Invoices record, read via related from its activities. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`rm_customer_wise_inv.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Font Awesome icon of the next activity type on this RM Customer wise Invoices record, read via related from its activities; used for display only. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`rm_customer_wise_inv.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Type of the next scheduled activity on this RM Customer wise Invoices record, read via related from its activities (standard activity mixin). | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`rm_customer_wise_inv.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard computed field: the user responsible for the next scheduled activity on this RM Customer wise Invoices record. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time this RM Customer wise Invoices record was created; set automatically. | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created this RM Customer wise Invoices record; set automatically. | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Standard computed name of the RM Customer wise Invoices record as shown in links and dropdowns. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the RM Customer wise Invoices record, assigned automatically. | stored |  |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard computed field: due date of the current user's next activity on this RM Customer wise Invoices record. | not stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time this RM Customer wise Invoices record was last modified; set automatically. | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last modified this RM Customer wise Invoices record; set automatically. | stored | `model res.users` (base) |  |
| `active` | Active | boolean | Archive flag of the Customer wise Invoices report line; defaults to true (ir.default), and unticked (archived) records are hidden from normal lists. Shown in the form and search views. | stored |  | `default BugFix-Accounting.default_263_x_rm_customer_wise_inv_active`<br>`view BugFix-Accounting.ported_default_form_view_fo_28459b2e_d60c_4b3a_9ee2_68b375f0d598`<br>`view BugFix-Accounting.ported_default_search_view__49a7dbb3_8287_49cd_8415_ee80c4cf86ad`<br>`view BugFix-Accounting.ported_view_3817_default_search_view_49a7dbb3_8287_49cd_8415_ee80c4cf86ad` |
| `name` | Name | char | Name of the Customer wise Invoices report line, used as its display name. Shown in the form, list and search views. | stored |  | `view BugFix-Accounting.ported_default_form_view_fo_28459b2e_d60c_4b3a_9ee2_68b375f0d598`<br>`view BugFix-Accounting.ported_default_list_view_fo_051fc709_c824_40ce_92e9_91a84d268510`<br>`view BugFix-Accounting.ported_default_search_view__49a7dbb3_8287_49cd_8415_ee80c4cf86ad`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b`<br>`view BugFix-Accounting.ported_view_3817_default_search_view_49a7dbb3_8287_49cd_8415_ee80c4cf86ad` |
| `customer` | Customer | many2one → `res.partner` | Customer: the contact (`res.partner`) this Customer wise Invoices report line refers to. Filled by the RPT - Customer wise Invoices - Generate action. | stored | `model res.partner` (base) | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `sales_report_model_id` | Sales Report Model Id | many2one → `sales_report_model` | Link to the parent Sales Report this Customer wise Invoices report line belongs to; inverse of the report's corresponding tab list. Shown in the form view. | stored | `model sales_report_model` (Jinasena_Masterdata_Reporting) | `view BugFix-Accounting.ported_view_3818_odoo_studio_default_461f7504_2101_403c_880e_62b0d141b1b4` |
| `sequence` | Sequence | integer | Sort order of the Customer wise Invoices report line (default 10); used as the drag handle in its list view. | stored |  | `default BugFix-Accounting.default_264_x_rm_customer_wise_inv_sequence`<br>`view BugFix-Accounting.ported_default_list_view_fo_051fc709_c824_40ce_92e9_91a84d268510`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `total_invoice_amount` | Total Invoice Amount | float | Total Invoice Amount figure on this Customer wise Invoices report line; stored number. Filled by the RPT - Customer wise Invoices - Generate action. | stored |  | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| RM Customer wise Invoices | `action_1682_rm_customer_wise_invoices` | Opens **RM Customer wise Invoices** records (tree,form). | `model rm_customer_wise_inv` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_rm_customer_wise_invoices` (BugFix-Studio-Misc) |

**Views (5):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for rm_customer_wise_inv | `ported_default_form_view_fo_28459b2e_d60c_4b3a_9ee2_68b375f0d598` | form | full form layout with 2 fields | Base form screen for RM Customer wise Invoices records: required Name title, an Archived ribbon when inactive and empty column groups that Studio extensions fill. | `rm_customer_wise_inv.active`<br>`rm_customer_wise_inv.name` | `view BugFix-Accounting.ported_view_3818_odoo_studio_default_461f7504_2101_403c_880e_62b0d141b1b4` |
| Default list view for rm_customer_wise_inv | `ported_default_list_view_fo_051fc709_c824_40ce_92e9_91a84d268510` | tree | full tree layout with 2 fields | Base list screen for RM Customer wise Invoices records showing Name with a drag handle for manual ordering by Sequence. | `rm_customer_wise_inv.name`<br>`rm_customer_wise_inv.sequence` |  |
| Default search view for rm_customer_wise_inv | `ported_default_search_view__49a7dbb3_8287_49cd_8415_ee80c4cf86ad` | search | full search layout with 1 fields | Search bar for RM Customer wise Invoices records: search by Name and an 'Archived' filter to show inactive records. | `rm_customer_wise_inv.active`<br>`rm_customer_wise_inv.name` |  |
| Default search view for rm_customer_wise_inv | `ported_view_3817_default_search_view_49a7dbb3_8287_49cd_8415_ee80c4cf86ad` | search | full search layout with 1 fields | Default search view for RM Customer-wise Invoice records (`rm_customer_wise_inv`): search by name plus an Archived filter. | `rm_customer_wise_inv.active`<br>`rm_customer_wise_inv.name` |  |
| Odoo Studio: Default form view for rm_customer_wise_inv customization | `ported_view_3818_odoo_studio_default_461f7504_2101_403c_880e_62b0d141b1b4` | form | inside `//group[@name='studio_group_907795_left']`: add field sales_report_model_id | Adds a hidden link to the parent Sales Report Model on the RM Customer-wise Invoice report-line form. | `view BugFix-Accounting.ported_default_form_view_fo_28459b2e_d60c_4b3a_9ee2_68b375f0d598`<br>`rm_customer_wise_inv.sales_report_model_id` |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| RM Customer wise Invoices group_system | `access_1510_rm_customer_wise_invoices_group_system` | Gives **Administration / Settings** read/write/create/delete access to RM Customer wise Invoices records. | `group base.group_system` (base)<br>`model rm_customer_wise_inv` |  |
| RM Customer wise Invoices group_user | `access_1511_rm_customer_wise_invoices_group_user` | Gives **User types / Internal User** read access to RM Customer wise Invoices records. | `group base.group_user` (base)<br>`model rm_customer_wise_inv` |  |
| rm_customer_wise_inv user access | `access_x_rm_customer_wise_inv_user` | Gives **User types / Internal User** read/write/create/delete access to RM Customer wise Invoices records. | `group base.group_user` (base)<br>`model rm_customer_wise_inv` |  |
