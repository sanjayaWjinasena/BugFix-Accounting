# BugFix-Accounting — `x_rm_cust_invoice_s1`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_rm_cust_invoice_s1` — RM Cust Invoice S1

*Created by this repo.* Python: `models/x_rm_cust_invoice_s1.py`, `models/x_rm_cust_invoice_s1_gap.py`. Record name field: `x_name`.

Other repos that use this model: `server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:x_rm_cust_invoice_s1 -->
A detail line of the 'Customer wise Invoices' report run from a Sales Report Model, giving an invoice number, date, partner, product, sales centre, quantity and value. Lines are filled by the 'RPT - Customer wise Invoices - Generate' action and removed by its Clear action.
<!-- /SUMMARY -->

**Fields (28):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard computed field: calendar meeting linked to the next activity on this RM Cust Invoice S1 record, if any. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard computed field: due date of the next scheduled activity on this RM Cust Invoice S1 record. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard computed flag (Alert or Error) showing that an activity on this RM Cust Invoice S1 record is in an exception state. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard computed icon shown when an activity on this RM Cust Invoice S1 record is in an exception state. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Scheduled activities (to-dos, calls, meetings) attached to this RM Cust Invoice S1 record, from the standard activity mixin. | stored | `model mail.activity` (mail) | `x_rm_cust_invoice_s1.activity_summary`<br>`x_rm_cust_invoice_s1.activity_type_icon`<br>`x_rm_cust_invoice_s1.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard computed activity status of this RM Cust Invoice S1 record: Overdue, Today or Planned, based on the nearest activity deadline. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Summary text of the next scheduled activity on this RM Cust Invoice S1 record, read via related from its activities. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_rm_cust_invoice_s1.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Font Awesome icon of the next activity type on this RM Cust Invoice S1 record, read via related from its activities; used for display only. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_rm_cust_invoice_s1.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Type of the next scheduled activity on this RM Cust Invoice S1 record, read via related from its activities (standard activity mixin). | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_rm_cust_invoice_s1.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard computed field: the user responsible for the next scheduled activity on this RM Cust Invoice S1 record. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time this RM Cust Invoice S1 record was created; set automatically. | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created this RM Cust Invoice S1 record; set automatically. | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Standard computed name of the RM Cust Invoice S1 record as shown in links and dropdowns. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the RM Cust Invoice S1 record, assigned automatically. | stored |  |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard computed field: due date of the current user's next activity on this RM Cust Invoice S1 record. | not stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time this RM Cust Invoice S1 record was last modified; set automatically. | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last modified this RM Cust Invoice S1 record; set automatically. | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Archive flag of the Invoice Breakup line (Customer wise Invoices report); defaults to true (ir.default), and unticked (archived) records are hidden from normal lists. Shown in the form and search views. | stored |  | `default BugFix-Accounting.default_265_x_rm_cust_invoice_s1_x_active`<br>`view BugFix-Accounting.ported_default_form_view_fo_7a09d097_0d14_4d92_aaab_95b003fbf75f`<br>`view BugFix-Accounting.ported_default_search_view__57a6d70d_a772_4194_afbe_241836e855ac`<br>`view BugFix-Accounting.ported_view_3821_default_search_view_57a6d70d_a772_4194_afbe_241836e855ac` |
| `x_name` | Name | char | Name of the Invoice Breakup line (Customer wise Invoices report), used as its display name. Shown in the form, list and search views. | stored |  | `view BugFix-Accounting.ported_default_form_view_fo_7a09d097_0d14_4d92_aaab_95b003fbf75f`<br>`view BugFix-Accounting.ported_default_list_view_fo_ec66ddc5_7ff8_42ac_8238_bdb020f850a2`<br>`view BugFix-Accounting.ported_default_search_view__57a6d70d_a772_4194_afbe_241836e855ac`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b`<br>`view BugFix-Accounting.ported_view_3821_default_search_view_57a6d70d_a772_4194_afbe_241836e855ac` |
| `x_studio_invoice_date` | Invoice Date | date | Invoice Date of this Invoice Breakup line (Customer wise Invoices report). Filled by the RPT - Customer wise Invoices - Generate action. | stored |  | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_number` | Number | char | Number text on this Invoice Breakup line (Customer wise Invoices report). Filled by the RPT - Customer wise Invoices - Generate action. | stored |  | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_partner` | Partner | many2one → `res.partner` | Partner: the contact (`res.partner`) this Invoice Breakup line (Customer wise Invoices report) refers to. Filled by the RPT - Customer wise Invoices - Generate action. | stored | `model res.partner` (base) | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_product_id` | Product | many2one → `product.product` | Product: the product (`product.product`) this Invoice Breakup line (Customer wise Invoices report) refers to. Filled by the RPT - Customer wise Invoices - Generate action. | stored | `model product.product` (product) | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_quantity` | Quantity | float | Quantity figure on this Invoice Breakup line (Customer wise Invoices report); stored number. Filled by the RPT - Customer wise Invoices - Generate action. | stored |  | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_sales_centre` | Sales Centre | many2one → `crm.team` | Sales Centre: the sales team (`crm.team`) this Invoice Breakup line (Customer wise Invoices report) refers to. Filled by the RPT - Customer wise Invoices - Generate action. | stored | `model crm.team` (sales_team) | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_sales_report_model_id` | Customer Invoice Details | many2one → `x_sales_report_model` | Link to the parent Sales Report this Invoice Breakup line (Customer wise Invoices report) belongs to; inverse of the report's corresponding tab list. Shown in the form view. | stored | `model x_sales_report_model` (Jinasena_Masterdata_Reporting) | `view BugFix-Accounting.ported_view_3823_odoo_studio_default_b7f83450_d158_4b53_ab6a_3722eac4db7f` |
| `x_studio_sequence` | Sequence | integer | Sort order of the Invoice Breakup line (Customer wise Invoices report) (default 10); used as the drag handle in its list view. | stored |  | `default BugFix-Accounting.default_266_x_rm_cust_invoice_s1_x_studio_sequence`<br>`view BugFix-Accounting.ported_default_list_view_fo_ec66ddc5_7ff8_42ac_8238_bdb020f850a2`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_value` | Value | float | Value figure on this Invoice Breakup line (Customer wise Invoices report); stored number. Filled by the RPT - Customer wise Invoices - Generate action. | stored |  | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| RM Cust Invoice S1 | `action_1683_rm_cust_invoice_s1` | Opens **RM Cust Invoice S1** records (tree,form). | `model x_rm_cust_invoice_s1` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_rm_cust_invoice_s1` (BugFix-Studio-Misc) |

**Views (5):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_rm_cust_invoice_s1 | `ported_default_form_view_fo_7a09d097_0d14_4d92_aaab_95b003fbf75f` | form | full form layout with 2 fields | Base form screen for RM Cust Invoice S1 records: required Name title, an Archived ribbon when inactive and empty column groups that Studio extensions fill. | `x_rm_cust_invoice_s1.x_active`<br>`x_rm_cust_invoice_s1.x_name` | `view BugFix-Accounting.ported_view_3823_odoo_studio_default_b7f83450_d158_4b53_ab6a_3722eac4db7f` |
| Default list view for x_rm_cust_invoice_s1 | `ported_default_list_view_fo_ec66ddc5_7ff8_42ac_8238_bdb020f850a2` | tree | full tree layout with 2 fields | Base list screen for RM Cust Invoice S1 records showing Name with a drag handle for manual ordering by Sequence. | `x_rm_cust_invoice_s1.x_name`<br>`x_rm_cust_invoice_s1.x_studio_sequence` |  |
| Default search view for x_rm_cust_invoice_s1 | `ported_default_search_view__57a6d70d_a772_4194_afbe_241836e855ac` | search | full search layout with 1 fields | Search bar for RM Cust Invoice S1 records: search by Name and an 'Archived' filter to show inactive records. | `x_rm_cust_invoice_s1.x_active`<br>`x_rm_cust_invoice_s1.x_name` |  |
| Default search view for x_rm_cust_invoice_s1 | `ported_view_3821_default_search_view_57a6d70d_a772_4194_afbe_241836e855ac` | search | full search layout with 1 fields | Default search view for RM Customer Invoice S1 records (`x_rm_cust_invoice_s1`): search by name plus an Archived filter. | `x_rm_cust_invoice_s1.x_active`<br>`x_rm_cust_invoice_s1.x_name` |  |
| Odoo Studio: Default form view for x_rm_cust_invoice_s1 customization | `ported_view_3823_odoo_studio_default_b7f83450_d158_4b53_ab6a_3722eac4db7f` | form | inside `//group[@name='studio_group_1b21a2_left']`: add field x_studio_sales_report_model_id | Adds a hidden link to the parent Sales Report Model on the RM Customer Invoice S1 report-line form. | `view BugFix-Accounting.ported_default_form_view_fo_7a09d097_0d14_4d92_aaab_95b003fbf75f`<br>`x_rm_cust_invoice_s1.x_studio_sales_report_model_id` |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| RM Cust Invoice S1 group_system | `access_1512_rm_cust_invoice_s1_group_system` | Gives **Administration / Settings** read/write/create/delete access to RM Cust Invoice S1 records. | `group base.group_system` (base)<br>`model x_rm_cust_invoice_s1` |  |
| RM Cust Invoice S1 group_user | `access_1513_rm_cust_invoice_s1_group_user` | Gives **User types / Internal User** read access to RM Cust Invoice S1 records. | `group base.group_user` (base)<br>`model x_rm_cust_invoice_s1` |  |
| x_rm_cust_invoice_s1 user access | `access_x_rm_cust_invoice_s1_user` | Gives **User types / Internal User** read/write/create/delete access to RM Cust Invoice S1 records. | `group base.group_user` (base)<br>`model x_rm_cust_invoice_s1` |  |
