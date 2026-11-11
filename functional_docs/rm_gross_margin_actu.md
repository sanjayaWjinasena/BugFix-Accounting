# BugFix-Accounting — `rm_gross_margin_actu`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `rm_gross_margin_actu` — RM Gross Margin - Actuals

*Created by this repo.* Python: `models/rm_gross_margin_actu.py`, `models/x_rm_gross_margin_actu_gap.py`. Record name field: `name`.

Other repos that use this model: `server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:rm_gross_margin_actu -->
An actuals line of the 'Project Gross Margin' report run from a Sales Report Model, giving transaction type, estimated total, delivered amount and the estimated-versus-actual variance. Each line can hold its underlying sales order lines (Temp_Estimated) or analytic budget lines (Temp_Actual_Budget), shown in sub-tabs depending on its flags. Lines are rebuilt by the 'SRM - RPT - Project Gross Margin' action.
<!-- /SUMMARY -->

**Fields (31):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard computed field: calendar meeting linked to the next activity on this RM Gross Margin - Actuals record, if any. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard computed field: due date of the next scheduled activity on this RM Gross Margin - Actuals record. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard computed flag (Alert or Error) showing that an activity on this RM Gross Margin - Actuals record is in an exception state. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard computed icon shown when an activity on this RM Gross Margin - Actuals record is in an exception state. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Scheduled activities (to-dos, calls, meetings) attached to this RM Gross Margin - Actuals record, from the standard activity mixin. | stored | `model mail.activity` (mail) | `rm_gross_margin_actu.activity_summary`<br>`rm_gross_margin_actu.activity_type_icon`<br>`rm_gross_margin_actu.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard computed activity status of this RM Gross Margin - Actuals record: Overdue, Today or Planned, based on the nearest activity deadline. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Summary text of the next scheduled activity on this RM Gross Margin - Actuals record, read via related from its activities. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`rm_gross_margin_actu.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Font Awesome icon of the next activity type on this RM Gross Margin - Actuals record, read via related from its activities; used for display only. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`rm_gross_margin_actu.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Type of the next scheduled activity on this RM Gross Margin - Actuals record, read via related from its activities (standard activity mixin). | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`rm_gross_margin_actu.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard computed field: the user responsible for the next scheduled activity on this RM Gross Margin - Actuals record. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time this RM Gross Margin - Actuals record was created; set automatically. | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created this RM Gross Margin - Actuals record; set automatically. | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Standard computed name of the RM Gross Margin - Actuals record as shown in links and dropdowns. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the RM Gross Margin - Actuals record, assigned automatically. | stored |  |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard computed field: due date of the current user's next activity on this RM Gross Margin - Actuals record. | not stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time this RM Gross Margin - Actuals record was last modified; set automatically. | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last modified this RM Gross Margin - Actuals record; set automatically. | stored | `model res.users` (base) |  |
| `active` | Active | boolean | Archive flag of the Project Gross Margin actuals line; defaults to true (ir.default), and unticked (archived) records are hidden from normal lists. Shown in the form and search views. | stored |  | `default BugFix-Accounting.default_rm_gross_margin_actu_active`<br>`view BugFix-Accounting.view_rm_gross_margin_actu_form`<br>`view BugFix-Accounting.view_rm_gross_margin_actu_search`<br>`view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_rm_gross_margin_actu_search_2` |
| `name` | Name | char | Name of the Project Gross Margin actuals line, used as its display name. Shown in the form, list and search views. | stored |  | `view BugFix-Accounting.view_rm_gross_margin_actu_form`<br>`view BugFix-Accounting.view_rm_gross_margin_actu_list`<br>`view BugFix-Accounting.view_rm_gross_margin_actu_search`<br>`view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_rm_gross_margin_actu_search_2` |
| `budget_line` | Budget Line | boolean | Flag marking this actuals line as a budget-based line; when ticked the "Budget Lines" sub-tab is shown on the line in the report. Filled by the SRM - RPT - Project Gross Margin action. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit` |
| `budget_line_ids` | Budget Line Ids | one2many → `temp_actual_budget` | Analytic budget lines (Temp_Actual_Budget) making up this actuals line; shown on its "Budget Lines" sub-tab when Budget Line is ticked. Filled by the SRM - RPT - Project Gross Margin action. | stored | `model temp_actual_budget` | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit` |
| `cost_price` | Delivered Amount | float | Delivered (actual) amount for this actuals line (technical name says cost price). Filled by the SRM - RPT - Project Gross Margin action. Shown in the list view. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_gross_margin_actu_inherit_2` |
| `estimated_total` | Estimated Amount | float | Estimated amount for this actuals line, for comparison with the delivered amount. Filled by the SRM - RPT - Project Gross Margin action. Shown in the list view. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_gross_margin_actu_inherit_2` |
| `header_reference` | Header Reference | char | Text reference to the report header for this Project Gross Margin actuals line. Set by the SRM - RPT - Project Gross Margin action. Shown in the list view. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_gross_margin_actu_inherit_2` |
| `normal_line` | Normal Line | boolean | Flag marking this actuals line as a sales-order-based line; when ticked the "Sales Order Lines" sub-tab is shown on the line in the report. Filled by the SRM - RPT - Project Gross Margin action. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit` |
| `other_expenses` | Other Expenses | char | Text label/description for an "other expenses" actuals line. Filled by the SRM - RPT - Project Gross Margin action. Shown in the list view. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_gross_margin_actu_inherit_2` |
| `sales_order_line_ids` | Sales Order Line Ids | one2many → `temp_estimated` | Sales order lines (Temp_Estimated) making up this actuals line; shown on its "Sales Order Lines" sub-tab when Normal Line is ticked. Filled by the SRM - RPT - Project Gross Margin action. | stored | `model temp_estimated` | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit` |
| `sales_report_model_id` | Sales Report Model Id | many2one → `sales_report_model` | Link to the parent Sales Report this Project Gross Margin actuals line belongs to; inverse of the report's corresponding tab list. Shown in the list view. | stored | `model sales_report_model` (Jinasena_Masterdata_Reporting) | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_gross_margin_actu_inherit_2` |
| `sequence` | Sequence | integer | Sort order of the Project Gross Margin actuals line (default 10); used as the drag handle in its list view. | default `10`; stored |  | `default BugFix-Accounting.default_rm_gross_margin_actu_sequence`<br>`view BugFix-Accounting.view_rm_gross_margin_actu_list`<br>`view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit` |
| `transaction_type_1` | Transaction Type | selection: Item=Item; Expense=Expense; Fee=Fee; Hour=Hour | Transaction type of the actuals line: Item, Expense, Fee or Hour. Filled by the SRM - RPT - Project Gross Margin action. Shown in the list view. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_gross_margin_actu_inherit_2` |
| `variance_est_act` | Variance (Est - Act) | float | Variance between estimated and actual (delivered) amount for this line. Filled by the SRM - RPT - Project Gross Margin action. Shown in the list view. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_gross_margin_actu_inherit_2` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| RM Gross Margin - Actuals | `action_rm_gross_margin_actuals` | Opens **RM Gross Margin - Actuals** records (tree,form). | `model rm_gross_margin_actu` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_rm_gross_margin_actuals` (BugFix-Studio-Misc) |

**Views (6):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for rm_gross_margin_actu | `view_rm_gross_margin_actu_form` | form | full form layout with 2 fields | Base form screen for RM Gross Margin - Actuals records: required Name title, an Archived ribbon when inactive and empty column groups that Studio extensions fill. | `rm_gross_margin_actu.active`<br>`rm_gross_margin_actu.name` |  |
| Default list view for rm_gross_margin_actu | `view_rm_gross_margin_actu_list` | tree | full tree layout with 2 fields | Base list screen for RM Gross Margin - Actuals records showing Name with a drag handle for manual ordering by Sequence. | `rm_gross_margin_actu.name`<br>`rm_gross_margin_actu.sequence` | `view BugFix-Accounting.view_default_list_view_for_rm_gross_margin_actu_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_gross_margin_actu_inherit_2` |
| Default search view for rm_gross_margin_actu | `view_rm_gross_margin_actu_search` | search | full search layout with 1 fields | Search bar for RM Gross Margin - Actuals records: search by Name and an 'Archived' filter to show inactive records. | `rm_gross_margin_actu.active`<br>`rm_gross_margin_actu.name` |  |
| Default search view for rm_gross_margin_actu | `view_rm_gross_margin_actu_search_2` | search | full search layout with 1 fields | Default search view for RM Gross Margin - Actual records (`rm_gross_margin_actu`): search by name plus an Archived filter. | `rm_gross_margin_actu.active`<br>`rm_gross_margin_actu.name` |  |
| Odoo Studio: Default list view for rm_gross_margin_actu customization | `view_default_list_view_for_rm_gross_margin_actu_inherit` | tree | set editable=bottom on `//tree[1]` | Studio customization of the RM Gross Margin - Actuals list: makes rows editable inline at the bottom. | `view BugFix-Accounting.view_rm_gross_margin_actu_list` |  |
| Odoo Studio: Default list view for rm_gross_margin_actu customization | `view_default_list_view_for_rm_gross_margin_actu_inherit_2` | tree | set editable=bottom on `//tree[1]`; before `//field[@name='sequence']`: add field transaction_type_1, field other_expenses, field estimated_total, field cost_price, field variance_est_act; set column_invisible=1 on `//field[@name='sequence']`; set column_invisible=1 on `//field[@name='name']`; after `//field[@name='name']`: add field sales_report_model_id, field header_reference | Makes the RM Gross Margin - Actual list inline-editable with Transaction Type, Other Expenses, Estimated Total, Cost Price and Variance (Est - Act) columns, plus report link and header reference; sequence and name hidden. | `view BugFix-Accounting.view_rm_gross_margin_actu_list`<br>`rm_gross_margin_actu.cost_price`<br>`rm_gross_margin_actu.estimated_total`<br>`rm_gross_margin_actu.header_reference`<br>`rm_gross_margin_actu.other_expenses`<details><summary>+3 more</summary>`rm_gross_margin_actu.sales_report_model_id`<br>`rm_gross_margin_actu.transaction_type_1`<br>`rm_gross_margin_actu.variance_est_act`</details> |  |

**Access rights (5):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| RM Gross Margin - Actuals group_system | `access_rm_gross_margin_actuals_group_system_2` | Gives **Administration / Settings** read/write/create/delete access to RM Gross Margin - Actuals records. | `group base.group_system` (base)<br>`model rm_gross_margin_actu` |  |
| RM Gross Margin - Actuals group_system | `access_rm_gross_margin_actuals_group_system` | Gives **Administration / Settings** read/write/create/delete access to RM Gross Margin - Actuals records. | `group base.group_system` (base)<br>`model rm_gross_margin_actu` |  |
| RM Gross Margin - Actuals group_user | `access_rm_gross_margin_actuals_group_user_2` | Gives **User types / Internal User** read access to RM Gross Margin - Actuals records. | `group base.group_user` (base)<br>`model rm_gross_margin_actu` |  |
| RM Gross Margin - Actuals group_user | `access_rm_gross_margin_actuals_group_user` | Gives **User types / Internal User** read access to RM Gross Margin - Actuals records. | `group base.group_user` (base)<br>`model rm_gross_margin_actu` |  |
| rm_gross_margin_actu user access | `access_rm_gross_margin_actu_user` | Gives **User types / Internal User** read/write/create/delete access to RM Gross Margin - Actuals records. | `group base.group_user` (base)<br>`model rm_gross_margin_actu` |  |
