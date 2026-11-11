# BugFix-Accounting — `rm_gross_margin_esti`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `rm_gross_margin_esti` — RM Gross Margin - Estimated

*Created by this repo.* Python: `models/rm_gross_margin_esti.py`, `models/x_rm_gross_margin_esti_gap.py`. Record name field: `name`.

Other repos that use this model: `server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:rm_gross_margin_esti -->
An estimated (quotation) line of the 'Project Gross Margin' report run from a Sales Report Model, giving transaction type, category, estimated amount, delivered cost and balance, with a flag for total rows. Each line can hold its underlying sales order lines (Temp_Estimated). Lines are rebuilt by the 'SRM - RPT - Project Gross Margin' action.
<!-- /SUMMARY -->

**Fields (43):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard computed field: calendar meeting linked to the next activity on this RM Gross Margin - Estimated record, if any. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard computed field: due date of the next scheduled activity on this RM Gross Margin - Estimated record. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard computed flag (Alert or Error) showing that an activity on this RM Gross Margin - Estimated record is in an exception state. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard computed icon shown when an activity on this RM Gross Margin - Estimated record is in an exception state. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Scheduled activities (to-dos, calls, meetings) attached to this RM Gross Margin - Estimated record, from the standard activity mixin. Displayed in the form view chatter. | stored | `model mail.activity` (mail) | `view BugFix-Accounting.view_rm_gross_margin_esti_form`<br>`rm_gross_margin_esti.activity_summary`<br>`rm_gross_margin_esti.activity_type_icon`<br>`rm_gross_margin_esti.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard computed activity status of this RM Gross Margin - Estimated record: Overdue, Today or Planned, based on the nearest activity deadline. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Summary text of the next scheduled activity on this RM Gross Margin - Estimated record, read via related from its activities. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`rm_gross_margin_esti.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Font Awesome icon of the next activity type on this RM Gross Margin - Estimated record, read via related from its activities; used for display only. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`rm_gross_margin_esti.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Type of the next scheduled activity on this RM Gross Margin - Estimated record, read via related from its activities (standard activity mixin). | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`rm_gross_margin_esti.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard computed field: the user responsible for the next scheduled activity on this RM Gross Margin - Estimated record. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time this RM Gross Margin - Estimated record was created; set automatically. | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created this RM Gross Margin - Estimated record; set automatically. | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Standard computed name of the RM Gross Margin - Estimated record as shown in links and dropdowns. | not stored |  |  |
| `has_message` | Has Message | boolean | Standard computed flag: true when this RM Gross Margin - Estimated record has at least one chatter message. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the RM Gross Margin - Estimated record, assigned automatically. | stored |  |  |
| `message_attachment_count` | Attachment Count | integer | Standard computed count of attachments linked to this RM Gross Margin - Estimated record. | not stored |  |  |
| `message_follower_ids` | Followers | one2many → `mail.followers` | Followers (partners) subscribed to notifications on this RM Gross Margin - Estimated record, from the standard mail thread mixin. Displayed in the form view chatter. | stored | `model mail.followers` (mail) | `view BugFix-Accounting.view_rm_gross_margin_esti_form` |
| `message_has_error` | Message Delivery error | boolean | Standard computed flag: true when a message on this RM Gross Margin - Estimated record failed to be delivered. | not stored |  |  |
| `message_has_error_counter` | Number of errors | integer | Standard computed count of messages on this RM Gross Margin - Estimated record with delivery errors. | not stored |  |  |
| `message_has_sms_error` | SMS Delivery error | boolean | Standard computed flag: true when an SMS sent from this RM Gross Margin - Estimated record failed to be delivered. | not stored |  |  |
| `message_ids` | Messages | one2many → `mail.message` | Chatter messages and log notes posted on this RM Gross Margin - Estimated record (standard mail thread). Displayed in the form view chatter. | stored | `model mail.message` (mail) | `view BugFix-Accounting.view_rm_gross_margin_esti_form` |
| `message_is_follower` | Is Follower | boolean | Standard computed flag: true when the current user follows this RM Gross Margin - Estimated record. | not stored |  |  |
| `message_needaction` | Action Needed | boolean | Standard computed flag: true when this RM Gross Margin - Estimated record has messages needing the current user's attention. | not stored |  |  |
| `message_needaction_counter` | Number of Actions | integer | Standard computed count of messages on this RM Gross Margin - Estimated record that need the current user's action. | not stored |  |  |
| `message_partner_ids` | Followers (Partners) | many2many → `res.partner` | Standard computed list of partners following this RM Gross Margin - Estimated record; mainly used for searching. | not stored | `model res.partner` (base) |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard computed field: due date of the current user's next activity on this RM Gross Margin - Estimated record. | not stored |  |  |
| `rating_ids` | Ratings | one2many → `rating.rating` | Customer ratings linked to this RM Gross Margin - Estimated record (standard rating mixin); not used by any view or logic in this repo. | stored | `model rating.rating` (rating) |  |
| `website_message_ids` | Website Messages | one2many → `mail.message` | Standard computed subset of chatter messages on this RM Gross Margin - Estimated record that are visible on the website/portal. | stored | `model mail.message` (mail) |  |
| `write_date` | Last Updated on | datetime | Date and time this RM Gross Margin - Estimated record was last modified; set automatically. | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last modified this RM Gross Margin - Estimated record; set automatically. | stored | `model res.users` (base) |  |
| `active` | Active | boolean | Archive flag of the Project Gross Margin estimated line; defaults to true (ir.default), and unticked (archived) records are hidden from normal lists. Shown in the form and search views. | stored |  | `default BugFix-Accounting.default_rm_gross_margin_esti_active`<br>`view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_rm_gross_margin_esti_form`<br>`view BugFix-Accounting.view_rm_gross_margin_esti_search` |
| `name` | Name | char | Name of the Project Gross Margin estimated line, used as its display name. Shown in the list, form and search views. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_rm_gross_margin_esti_list`<br>`view BugFix-Accounting.view_rm_gross_margin_esti_form`<br>`view BugFix-Accounting.view_rm_gross_margin_esti_search` |
| `actual_cost` | Delivered Amount | float | Delivered (actual) amount for this estimated line (technical name says actual cost). Filled by the SRM - RPT - Project Gross Margin action. Shown in the list view. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_gross_margin_esti_inherit` |
| `balance_cost` | Balance Amount | float | Balance amount remaining for this estimated line (estimated minus delivered, per its label). Filled by the SRM - RPT - Project Gross Margin action. Shown in the list view. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_gross_margin_esti_inherit` |
| `category` | Category | char | Category text of the estimated line (e.g. grouping of quotation items). Filled by the SRM - RPT - Project Gross Margin action. Shown in the list view. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_gross_margin_esti_inherit` |
| `estimated_amt` | Estimated Amt. | float | Estimated (quoted) amount for this line. Filled by the SRM - RPT - Project Gross Margin action. Shown in the list view. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_gross_margin_esti_inherit` |
| `group_title` |  | char | Group title text with a blank label, shown as an unlabelled column in the report’s Quotation/ Estimated tab. Filled by the SRM - RPT - Project Gross Margin action. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit` |
| `header_reference` | Header Reference | char | Text reference to the report header for this Project Gross Margin estimated line. Set by the SRM - RPT - Project Gross Margin action. Shown in the list view. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_gross_margin_esti_inherit` |
| `sales_order_line_ids` | Sales Order Line Ids | one2many → `temp_estimated` | Sales order lines (Temp_Estimated) making up this estimated line; shown on its "Sales Order Lines" sub-tab in the report. Filled by the SRM - RPT - Project Gross Margin action. | stored | `model temp_estimated` | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit` |
| `sales_report_model_id` | Sales Report Model Id | many2one → `sales_report_model` | Link to the parent Sales Report this Project Gross Margin estimated line belongs to; inverse of the report's corresponding tab list. Shown in the list view. | stored | `model sales_report_model` (Jinasena_Masterdata_Reporting) | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_gross_margin_esti_inherit` |
| `sequence` | Sequence | integer | Sort order of the Project Gross Margin estimated line (default 10); used as the drag handle in its list view. | default `10`; stored |  | `default BugFix-Accounting.default_rm_gross_margin_esti_sequence`<br>`view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_rm_gross_margin_esti_list` |
| `total` | Total | boolean | Flag marking this estimated line as a total/subtotal row. Filled by the SRM - RPT - Project Gross Margin action. Shown in the list view. | stored |  | `view BugFix-Accounting.view_default_list_view_for_rm_gross_margin_esti_inherit` |
| `transaction_type` | Transaction Type | selection: Item=Item; Expense=Expense; Fee=Fee; Hour=Hour | Transaction type of the estimated line: Item, Expense, Fee or Hour. Filled by the SRM - RPT - Project Gross Margin action. Shown in the list view. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_gross_margin_esti_inherit` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| RM Gross Margin - Estimated | `action_rm_gross_margin_estimated` | Opens **RM Gross Margin - Estimated** records (tree,form). | `model rm_gross_margin_esti` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_rm_gross_margin_estimated` (BugFix-Studio-Misc) |

**Views (4):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for rm_gross_margin_esti | `view_rm_gross_margin_esti_form` | form | full form layout with 5 fields | Default form for RM Gross Margin - Estimated (`rm_gross_margin_esti`): archived ribbon, required Name title, two empty groups and chatter. | `rm_gross_margin_esti.activity_ids`<br>`rm_gross_margin_esti.message_follower_ids`<br>`rm_gross_margin_esti.message_ids`<br>`rm_gross_margin_esti.active`<br>`rm_gross_margin_esti.name` |  |
| Default list view for rm_gross_margin_esti | `view_rm_gross_margin_esti_list` | tree | full tree layout with 2 fields | Default list for RM Gross Margin - Estimated (`rm_gross_margin_esti`) with sequence handle and Name. | `rm_gross_margin_esti.name`<br>`rm_gross_margin_esti.sequence` | `view BugFix-Accounting.view_default_list_view_for_rm_gross_margin_esti_inherit` |
| Default search view for rm_gross_margin_esti | `view_rm_gross_margin_esti_search` | search | full search layout with 1 fields | Default search view for RM Gross Margin - Estimated records (`rm_gross_margin_esti`): search by name plus an Archived filter. | `rm_gross_margin_esti.active`<br>`rm_gross_margin_esti.name` |  |
| Odoo Studio: Default list view for rm_gross_margin_esti customization | `view_default_list_view_for_rm_gross_margin_esti_inherit` | tree | set editable=bottom on `//tree[1]`; after `//field[@name='sequence']`: add field header_reference, field sales_report_model_id, field transaction_type, field category, field estimated_amt, field actual_cost, field balance_cost, field total; set column_invisible=1 on `//field[@name='name']` | Makes the RM Gross Margin - Estimated list inline-editable with Transaction Type, Category, Estimated Amt., Actual Cost, Balance Cost and Total; report link, header reference and name hidden. | `view BugFix-Accounting.view_rm_gross_margin_esti_list`<br>`rm_gross_margin_esti.actual_cost`<br>`rm_gross_margin_esti.balance_cost`<br>`rm_gross_margin_esti.category`<br>`rm_gross_margin_esti.estimated_amt`<details><summary>+4 more</summary>`rm_gross_margin_esti.header_reference`<br>`rm_gross_margin_esti.sales_report_model_id`<br>`rm_gross_margin_esti.total`<br>`rm_gross_margin_esti.transaction_type`</details> |  |

**Access rights (4):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| RM Gross Margin - Estimated group_system | `access_rm_gross_margin_estimated_group_system_2` | Gives **Administration / Settings** read/write/create/delete access to RM Gross Margin - Estimated records. | `group base.group_system` (base)<br>`model rm_gross_margin_esti` |  |
| RM Gross Margin - Estimated group_system | `access_rm_gross_margin_estimated_group_system` | Gives **Administration / Settings** read/write/create/delete access to RM Gross Margin - Estimated records. | `group base.group_system` (base)<br>`model rm_gross_margin_esti` |  |
| RM Gross Margin - Estimated group_user | `access_rm_gross_margin_estimated_group_user_2` | Gives **User types / Internal User** read access to RM Gross Margin - Estimated records. | `group base.group_user` (base)<br>`model rm_gross_margin_esti` |  |
| RM Gross Margin - Estimated group_user | `access_rm_gross_margin_estimated_group_user` | Gives **User types / Internal User** read access to RM Gross Margin - Estimated records. | `group base.group_user` (base)<br>`model rm_gross_margin_esti` |  |
