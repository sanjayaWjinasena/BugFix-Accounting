# BugFix-Accounting — `x_temp_actual_budget`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_temp_actual_budget` — Temp_Actual_Budget

*Created by this repo.* Python: `models/x_temp_actual_budget.py`, `models/x_temp_actual_budget_gap.py`. Record name field: `x_name`.

Other repos that use this model: `access right BugFix-Studio-Misc.access_g_temp_budget_x_temp_actual_budget_accounting_jin_projectinvoice` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:x_temp_actual_budget -->
A temporary copy of an analytic budget line (budget, analytic account, dates and planned amount) attached to a Project Gross Margin actuals line. Records are created by the 'SRM - RPT - Project Gross Margin' action and shown in the actuals line's Budget Lines sub-tab.
<!-- /SUMMARY -->

**Fields (28):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard computed field: calendar meeting linked to the next activity on this Temp_Actual_Budget record, if any. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard computed field: due date of the next scheduled activity on this Temp_Actual_Budget record. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard computed flag (Alert or Error) showing that an activity on this Temp_Actual_Budget record is in an exception state. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard computed icon shown when an activity on this Temp_Actual_Budget record is in an exception state. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Scheduled activities (to-dos, calls, meetings) attached to this Temp_Actual_Budget record, from the standard activity mixin. | stored | `model mail.activity` (mail) | `x_temp_actual_budget.activity_summary`<br>`x_temp_actual_budget.activity_type_icon`<br>`x_temp_actual_budget.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard computed activity status of this Temp_Actual_Budget record: Overdue, Today or Planned, based on the nearest activity deadline. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Summary text of the next scheduled activity on this Temp_Actual_Budget record, read via related from its activities. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_temp_actual_budget.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Font Awesome icon of the next activity type on this Temp_Actual_Budget record, read via related from its activities; used for display only. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_temp_actual_budget.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Type of the next scheduled activity on this Temp_Actual_Budget record, read via related from its activities (standard activity mixin). | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_temp_actual_budget.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard computed field: the user responsible for the next scheduled activity on this Temp_Actual_Budget record. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time this Temp_Actual_Budget record was created; set automatically. | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created this Temp_Actual_Budget record; set automatically. | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Standard computed name of the Temp_Actual_Budget record as shown in links and dropdowns. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the Temp_Actual_Budget record, assigned automatically. | stored |  |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard computed field: due date of the current user's next activity on this Temp_Actual_Budget record. | not stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time this Temp_Actual_Budget record was last modified; set automatically. | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last modified this Temp_Actual_Budget record; set automatically. | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Archive flag of the budget line under a Project Gross Margin actuals line; defaults to true (ir.default), and unticked (archived) records are hidden from normal lists. Shown in the form and search views. | stored |  | `default BugFix-Accounting.default_321_x_temp_actual_budget_x_active`<br>`view BugFix-Accounting.ported_default_form_view_fo_741643ee_ca4d_4aa5_a8e3_76dfefa6c8c1`<br>`view BugFix-Accounting.ported_default_search_view__65bb7bb5_0341_4946_8b0e_8040521503cf`<br>`view BugFix-Accounting.ported_view_4914_default_search_view_65bb7bb5_0341_4946_8b0e_8040521503cf` |
| `x_currency_id` | Currency | many2one → `res.currency` | Currency of the budget amounts; defaults via ir.default to currency database id 145. Shown in the list. Filled by the SRM - RPT - Project Gross Margin action. | stored | `model res.currency` (base) | `default BugFix-Accounting.default_323_x_temp_actual_budget_x_currency_id`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b`<br>`view BugFix-Accounting.ported_view_4915_odoo_studio_default_4d82d10a_a936_4ed9_b0f0_c50c40f19759` |
| `x_name` | Name | char | Name of the budget line under a Project Gross Margin actuals line, used as its display name. Shown in the form, list and search views. | stored |  | `view BugFix-Accounting.ported_default_form_view_fo_741643ee_ca4d_4aa5_a8e3_76dfefa6c8c1`<br>`view BugFix-Accounting.ported_default_list_view_fo_bcc5f161_0ade_4995_9c51_35002b4f9d4d`<br>`view BugFix-Accounting.ported_default_search_view__65bb7bb5_0341_4946_8b0e_8040521503cf`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b`<br>`view BugFix-Accounting.ported_view_4914_default_search_view_65bb7bb5_0341_4946_8b0e_8040521503cf` |
| `x_studio_actual_line_ids` | Actual Line Ids | many2one → `x_rm_gross_margin_actu` | Parent Project Gross Margin actuals line this budget line belongs to (inverse of its Budget Line Ids). Shown in the list view. | stored | `model x_rm_gross_margin_actu` | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b`<br>`view BugFix-Accounting.ported_view_4915_odoo_studio_default_4d82d10a_a936_4ed9_b0f0_c50c40f19759` |
| `x_studio_analytic_account_id` | Analytic Account | many2one → `account.analytic.account` | Analytic Account: the analytic account (`account.analytic.account`) this budget line under a Project Gross Margin actuals line refers to. Filled by the SRM - RPT - Project Gross Margin action. Shown in the list view. | stored | `model account.analytic.account` (analytic) | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b`<br>`view BugFix-Accounting.ported_view_4915_odoo_studio_default_4d82d10a_a936_4ed9_b0f0_c50c40f19759` |
| `x_studio_budget_line_ids` | Budget Line Ids | many2one → `crossovered.budget.lines` | Source analytic budget line (crossovered.budget.lines) this record copies. Filled by the SRM - RPT - Project Gross Margin action. Shown in the list view. | stored | `model crossovered.budget.lines` (account_budget) | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b`<br>`view BugFix-Accounting.ported_view_4915_odoo_studio_default_4d82d10a_a936_4ed9_b0f0_c50c40f19759` |
| `x_studio_crossovered_budget_id` | Budget | many2one → `crossovered.budget` | Budget: the budget (`crossovered.budget`) this budget line under a Project Gross Margin actuals line refers to. Filled by the SRM - RPT - Project Gross Margin action. Shown in the list view. | stored | `model crossovered.budget` (account_budget) | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b`<br>`view BugFix-Accounting.ported_view_4915_odoo_studio_default_4d82d10a_a936_4ed9_b0f0_c50c40f19759` |
| `x_studio_date_from` | Start Date | date | Start Date of this budget line under a Project Gross Margin actuals line. Filled by the SRM - RPT - Project Gross Margin action. Shown in the list view. | stored |  | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b`<br>`view BugFix-Accounting.ported_view_4915_odoo_studio_default_4d82d10a_a936_4ed9_b0f0_c50c40f19759` |
| `x_studio_date_to` | End Date | date | End Date of this budget line under a Project Gross Margin actuals line. Filled by the SRM - RPT - Project Gross Margin action. Shown in the list view. | stored |  | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b`<br>`view BugFix-Accounting.ported_view_4915_odoo_studio_default_4d82d10a_a936_4ed9_b0f0_c50c40f19759` |
| `x_studio_planned_amount` | Planned Amount | float | Planned amount of the source budget line. Filled by the SRM - RPT - Project Gross Margin action. Shown in the list view. | stored |  | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b`<br>`view BugFix-Accounting.ported_view_4915_odoo_studio_default_4d82d10a_a936_4ed9_b0f0_c50c40f19759` |
| `x_studio_sequence` | Sequence | integer | Sort order of the budget line under a Project Gross Margin actuals line (default 10); used as the drag handle in its list view. | stored |  | `default BugFix-Accounting.default_322_x_temp_actual_budget_x_studio_sequence`<br>`view BugFix-Accounting.ported_default_list_view_fo_bcc5f161_0ade_4995_9c51_35002b4f9d4d`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Temp_Actual_Budget | `action_2123_temp_actual_budget` | Opens **Temp_Actual_Budget** records (tree,form). | `model x_temp_actual_budget` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_temp_actual_budget` (BugFix-Studio-Misc) |

**Views (5):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_temp_actual_budget | `ported_default_form_view_fo_741643ee_ca4d_4aa5_a8e3_76dfefa6c8c1` | form | full form layout with 2 fields | Base form screen for Temp Actual Budget records: required Name title, an Archived ribbon when inactive and empty column groups that Studio extensions fill. | `x_temp_actual_budget.x_active`<br>`x_temp_actual_budget.x_name` |  |
| Default list view for x_temp_actual_budget | `ported_default_list_view_fo_bcc5f161_0ade_4995_9c51_35002b4f9d4d` | tree | full tree layout with 2 fields | Base list screen for Temp Actual Budget records showing Name with a drag handle for manual ordering by Sequence. | `x_temp_actual_budget.x_name`<br>`x_temp_actual_budget.x_studio_sequence` | `view BugFix-Accounting.ported_view_4915_odoo_studio_default_4d82d10a_a936_4ed9_b0f0_c50c40f19759` |
| Default search view for x_temp_actual_budget | `ported_default_search_view__65bb7bb5_0341_4946_8b0e_8040521503cf` | search | full search layout with 1 fields | Search bar for Temp Actual Budget records: search by Name and an 'Archived' filter to show inactive records. | `x_temp_actual_budget.x_active`<br>`x_temp_actual_budget.x_name` |  |
| Default search view for x_temp_actual_budget | `ported_view_4914_default_search_view_65bb7bb5_0341_4946_8b0e_8040521503cf` | search | full search layout with 1 fields | Default search view for Temp Actual Budget records (`x_temp_actual_budget`): search by name plus an Archived filter. | `x_temp_actual_budget.x_active`<br>`x_temp_actual_budget.x_name` |  |
| Odoo Studio: Default list view for x_temp_actual_budget customization | `ported_view_4915_odoo_studio_default_4d82d10a_a936_4ed9_b0f0_c50c40f19759` | tree | after `//field[@name='x_studio_sequence']`: add field x_studio_budget_line_ids, field x_studio_crossovered_budget_id, field x_studio_analytic_account_id, field x_studio_date_from, field x_studio_date_to, field x_studio_planned_amount, field x_currency_id; set column_invisible=1 on `//field[@name='x_name']`; after `//field[@name='x_name']`: add field x_studio_actual_line_ids | Temp Actual Budget list: shows Budget, Analytic Account, Start/End Date and Planned Amount (budget lines, currency and name hidden) and adds actual lines after the name. | `view BugFix-Accounting.ported_default_list_view_fo_bcc5f161_0ade_4995_9c51_35002b4f9d4d`<br>`x_temp_actual_budget.x_currency_id`<br>`x_temp_actual_budget.x_studio_actual_line_ids`<br>`x_temp_actual_budget.x_studio_analytic_account_id`<br>`x_temp_actual_budget.x_studio_budget_line_ids`<details><summary>+4 more</summary>`x_temp_actual_budget.x_studio_crossovered_budget_id`<br>`x_temp_actual_budget.x_studio_date_from`<br>`x_temp_actual_budget.x_studio_date_to`<br>`x_temp_actual_budget.x_studio_planned_amount`</details> |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Temp_Actual_Budget group_system | `access_1753_temp_actual_budget_group_system` | Gives **Administration / Settings** read/write/create/delete access to Temp_Actual_Budget records. | `group base.group_system` (base)<br>`model x_temp_actual_budget` |  |
| Temp_Actual_Budget group_user | `access_1754_temp_actual_budget_group_user` | Gives **User types / Internal User** read access to Temp_Actual_Budget records. | `group base.group_user` (base)<br>`model x_temp_actual_budget` |  |
| x_temp_actual_budget user access | `access_x_temp_actual_budget_user` | Gives **User types / Internal User** read/write/create/delete access to Temp_Actual_Budget records. | `group base.group_user` (base)<br>`model x_temp_actual_budget` |  |
