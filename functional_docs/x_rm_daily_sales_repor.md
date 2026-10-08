# BugFix-Accounting — `x_rm_daily_sales_repor`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_rm_daily_sales_repor` — RM Daily Sales Report

*Created by this repo.* Python: `models/x_rm_daily_sales_repor.py`, `models/x_rm_daily_sales_repor_gap.py`. Record name field: `x_name`.

Other repos that use this model: `server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:x_rm_daily_sales_repor -->
A per-sales-centre line of the 'Daily Sales Report' run from a Sales Report Model, giving net invoice value for the day, month and cumulative, sales targets and achievement percentages. Lines are created by the 'RPT - Daily Sales Report - Generate' action and removed by its Clear action.
<!-- /SUMMARY -->

**Fields (42):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard computed field: calendar meeting linked to the next activity on this RM Daily Sales Report record, if any. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard computed field: due date of the next scheduled activity on this RM Daily Sales Report record. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard computed flag (Alert or Error) showing that an activity on this RM Daily Sales Report record is in an exception state. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard computed icon shown when an activity on this RM Daily Sales Report record is in an exception state. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Scheduled activities (to-dos, calls, meetings) attached to this RM Daily Sales Report record, from the standard activity mixin. Displayed in the form view chatter. | stored | `model mail.activity` (mail) | `view BugFix-Accounting.ported_view_3793_default_form_view_fo_f256f423_cc0e_4e76_8f35_2007e4720e58`<br>`x_rm_daily_sales_repor.activity_summary`<br>`x_rm_daily_sales_repor.activity_type_icon`<br>`x_rm_daily_sales_repor.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard computed activity status of this RM Daily Sales Report record: Overdue, Today or Planned, based on the nearest activity deadline. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Summary text of the next scheduled activity on this RM Daily Sales Report record, read via related from its activities. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_rm_daily_sales_repor.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Font Awesome icon of the next activity type on this RM Daily Sales Report record, read via related from its activities; used for display only. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_rm_daily_sales_repor.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Type of the next scheduled activity on this RM Daily Sales Report record, read via related from its activities (standard activity mixin). | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_rm_daily_sales_repor.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard computed field: the user responsible for the next scheduled activity on this RM Daily Sales Report record. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time this RM Daily Sales Report record was created; set automatically. | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created this RM Daily Sales Report record; set automatically. | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Standard computed name of the RM Daily Sales Report record as shown in links and dropdowns. | not stored |  |  |
| `has_message` | Has Message | boolean | Standard computed flag: true when this RM Daily Sales Report record has at least one chatter message. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the RM Daily Sales Report record, assigned automatically. | stored |  |  |
| `message_attachment_count` | Attachment Count | integer | Standard computed count of attachments linked to this RM Daily Sales Report record. | not stored |  |  |
| `message_follower_ids` | Followers | one2many → `mail.followers` | Followers (partners) subscribed to notifications on this RM Daily Sales Report record, from the standard mail thread mixin. Displayed in the form view chatter. | stored | `model mail.followers` (mail) | `view BugFix-Accounting.ported_view_3793_default_form_view_fo_f256f423_cc0e_4e76_8f35_2007e4720e58` |
| `message_has_error` | Message Delivery error | boolean | Standard computed flag: true when a message on this RM Daily Sales Report record failed to be delivered. | not stored |  |  |
| `message_has_error_counter` | Number of errors | integer | Standard computed count of messages on this RM Daily Sales Report record with delivery errors. | not stored |  |  |
| `message_has_sms_error` | SMS Delivery error | boolean | Standard computed flag: true when an SMS sent from this RM Daily Sales Report record failed to be delivered. | not stored |  |  |
| `message_ids` | Messages | one2many → `mail.message` | Chatter messages and log notes posted on this RM Daily Sales Report record (standard mail thread). Displayed in the form view chatter. | stored | `model mail.message` (mail) | `view BugFix-Accounting.ported_view_3793_default_form_view_fo_f256f423_cc0e_4e76_8f35_2007e4720e58` |
| `message_is_follower` | Is Follower | boolean | Standard computed flag: true when the current user follows this RM Daily Sales Report record. | not stored |  |  |
| `message_needaction` | Action Needed | boolean | Standard computed flag: true when this RM Daily Sales Report record has messages needing the current user's attention. | not stored |  |  |
| `message_needaction_counter` | Number of Actions | integer | Standard computed count of messages on this RM Daily Sales Report record that need the current user's action. | not stored |  |  |
| `message_partner_ids` | Followers (Partners) | many2many → `res.partner` | Standard computed list of partners following this RM Daily Sales Report record; mainly used for searching. | not stored | `model res.partner` (base) |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard computed field: due date of the current user's next activity on this RM Daily Sales Report record. | not stored |  |  |
| `rating_ids` | Ratings | one2many → `rating.rating` | Customer ratings linked to this RM Daily Sales Report record (standard rating mixin); not used by any view or logic in this repo. | stored | `model rating.rating` (rating) |  |
| `website_message_ids` | Website Messages | one2many → `mail.message` | Standard computed subset of chatter messages on this RM Daily Sales Report record that are visible on the website/portal. | stored | `model mail.message` (mail) |  |
| `write_date` | Last Updated on | datetime | Date and time this RM Daily Sales Report record was last modified; set automatically. | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last modified this RM Daily Sales Report record; set automatically. | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Archive flag of the Daily Sales Report line; defaults to true (ir.default), and unticked (archived) records are hidden from normal lists. Shown in the form and search views. | stored |  | `default BugFix-Accounting.default_254_x_rm_daily_sales_repor_x_active`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b`<br>`view BugFix-Accounting.ported_view_3793_default_form_view_fo_f256f423_cc0e_4e76_8f35_2007e4720e58`<br>`view BugFix-Accounting.ported_view_3794_default_search_view_2b244fc7_26c1_4c0f_bc8d_70d61268bb2c` |
| `x_name` | Name | char | Name of the Daily Sales Report line, used as its display name. Shown in the list, form and search views. | stored |  | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b`<br>`view BugFix-Accounting.ported_view_3792_default_list_view_fo_2e2d264d_b130_40f7_a4b3_2d6c0c9e123d`<br>`view BugFix-Accounting.ported_view_3793_default_form_view_fo_f256f423_cc0e_4e76_8f35_2007e4720e58`<br>`view BugFix-Accounting.ported_view_3794_default_search_view_2b244fc7_26c1_4c0f_bc8d_70d61268bb2c` |
| `x_studio_achieve_cumulative_` | Achieve Cumulative (%) | float | Achieve Cumulative (%) figure on this Daily Sales Report line; stored number. Filled by the RPT - Daily Sales Report - Generate action. | stored |  | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_achievement_` | Achievement (%) | float | Achievement (%) figure on this Daily Sales Report line; stored number. Filled by the RPT - Daily Sales Report - Generate action. | stored |  | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_m_sales_target` | M. Sales Target | float | M. Sales Target figure on this Daily Sales Report line; stored number. Filled by the RPT - Daily Sales Report - Generate action. | stored |  | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_net_invoice_value_cumulative` | Net Invoice Value - Cumulative | float | Net Invoice Value - Cumulative figure on this Daily Sales Report line; stored number. Filled by the RPT - Daily Sales Report - Generate action. | stored |  | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_net_invoice_value_day` | Net Invoice Value - Day | float | Net Invoice Value - Day figure on this Daily Sales Report line; stored number. Filled by the RPT - Daily Sales Report - Generate action. | stored |  | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_net_invoice_value_month` | Net Invoice Value - Month | float | Net Invoice Value - Month figure on this Daily Sales Report line; stored number. Filled by the RPT - Daily Sales Report - Generate action. | stored |  | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_s_target_cumulative` | S. Target - Cumulative | float | S. Target - Cumulative figure on this Daily Sales Report line; stored number. Filled by the RPT - Daily Sales Report - Generate action. | stored |  | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_sales_centre` | Sales Centre | char | Sales centre name (text) for this daily sales report line. Filled by the RPT - Daily Sales Report - Generate action. | stored |  | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_sales_report_model_id` | Sales Report Model Id | many2one → `x_sales_report_model` | Link to the parent Sales Report this Daily Sales Report line belongs to; inverse of the report's corresponding tab list. Shown in the form view. | stored | `model x_sales_report_model` (Jinasena_Masterdata_Reporting) | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b`<br>`view BugFix-Accounting.ported_view_3795_odoo_studio_default_f26fd96a_1773_4b01_a68c_57e4ab481f65` |
| `x_studio_sequence` | Sequence | integer | Sort order of the Daily Sales Report line (default 10); used as the drag handle in its list view. | default `10`; stored |  | `default BugFix-Accounting.default_255_x_rm_daily_sales_repor_x_studio_sequence`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b`<br>`view BugFix-Accounting.ported_view_3792_default_list_view_fo_2e2d264d_b130_40f7_a4b3_2d6c0c9e123d` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| RM Daily Sales Report | `action_1669_rm_daily_sales_report` | Opens **RM Daily Sales Report** records (tree,form). | `model x_rm_daily_sales_repor` | `menu BugFix-Accounting.menu_f6_rm_daily_sales_report` |

**Views (4):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_rm_daily_sales_repor | `ported_view_3793_default_form_view_fo_f256f423_cc0e_4e76_8f35_2007e4720e58` | form | full form layout with 5 fields | Default form for RM Daily Sales Report (`x_rm_daily_sales_repor`): archived ribbon, required Name title, two empty groups and chatter. | `x_rm_daily_sales_repor.activity_ids`<br>`x_rm_daily_sales_repor.message_follower_ids`<br>`x_rm_daily_sales_repor.message_ids`<br>`x_rm_daily_sales_repor.x_active`<br>`x_rm_daily_sales_repor.x_name` | `view BugFix-Accounting.ported_view_3795_odoo_studio_default_f26fd96a_1773_4b01_a68c_57e4ab481f65` |
| Default list view for x_rm_daily_sales_repor | `ported_view_3792_default_list_view_fo_2e2d264d_b130_40f7_a4b3_2d6c0c9e123d` | tree | full tree layout with 2 fields | Default list for RM Daily Sales Report (`x_rm_daily_sales_repor`) with sequence handle and Name. | `x_rm_daily_sales_repor.x_name`<br>`x_rm_daily_sales_repor.x_studio_sequence` |  |
| Default search view for x_rm_daily_sales_repor | `ported_view_3794_default_search_view_2b244fc7_26c1_4c0f_bc8d_70d61268bb2c` | search | full search layout with 1 fields | Default search view for RM Daily Sales Report records (`x_rm_daily_sales_repor`): search by name plus an Archived filter. | `x_rm_daily_sales_repor.x_active`<br>`x_rm_daily_sales_repor.x_name` |  |
| Odoo Studio: Default form view for x_rm_daily_sales_repor customization | `ported_view_3795_odoo_studio_default_f26fd96a_1773_4b01_a68c_57e4ab481f65` | form | inside `//group[@name='studio_group_0e0847_left']`: add field x_studio_sales_report_model_id | Adds a hidden, read-only (force-saved) link to the parent Sales Report Model on the RM Daily Sales Report line form. | `view BugFix-Accounting.ported_view_3793_default_form_view_fo_f256f423_cc0e_4e76_8f35_2007e4720e58`<br>`x_rm_daily_sales_repor.x_studio_sales_report_model_id` |  |

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| RM Daily Sales Report group_system | `access_1502_rm_daily_sales_report_group_system` | Gives **Administration / Settings** read/write/create/delete access to RM Daily Sales Report records. | `group base.group_system` (base)<br>`model x_rm_daily_sales_repor` |  |
| RM Daily Sales Report group_user | `access_1503_rm_daily_sales_report_group_user` | Gives **User types / Internal User** read access to RM Daily Sales Report records. | `group base.group_user` (base)<br>`model x_rm_daily_sales_repor` |  |
