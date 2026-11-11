# BugFix-Accounting — `rm_prod_summary_spli`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `rm_prod_summary_spli` — RM Prod. Summary Split

*Created by this repo.* Python: `models/rm_prod_summary_spli.py`, `models/x_rm_prod_summary_spli_gap.py`. Record name field: `name`.

Other repos that use this model: `server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:rm_prod_summary_spli -->
A line of the 'Production Summary - Split' report run from a Sales Report Model, giving product, job number, quantity, total and split figures for raw-material moves. Lines are recreated by the 'SRM - RPT - Production Summary - Split' action.
<!-- /SUMMARY -->

**Fields (42):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard computed field: calendar meeting linked to the next activity on this RM Prod. Summary Split record, if any. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard computed field: due date of the next scheduled activity on this RM Prod. Summary Split record. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard computed flag (Alert or Error) showing that an activity on this RM Prod. Summary Split record is in an exception state. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard computed icon shown when an activity on this RM Prod. Summary Split record is in an exception state. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Scheduled activities (to-dos, calls, meetings) attached to this RM Prod. Summary Split record, from the standard activity mixin. Displayed in the form view chatter. | stored | `model mail.activity` (mail) | `view BugFix-Accounting.view_rm_prod_summary_spli_form`<br>`rm_prod_summary_spli.activity_summary`<br>`rm_prod_summary_spli.activity_type_icon`<br>`rm_prod_summary_spli.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard computed activity status of this RM Prod. Summary Split record: Overdue, Today or Planned, based on the nearest activity deadline. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Summary text of the next scheduled activity on this RM Prod. Summary Split record, read via related from its activities. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`rm_prod_summary_spli.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Font Awesome icon of the next activity type on this RM Prod. Summary Split record, read via related from its activities; used for display only. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`rm_prod_summary_spli.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Type of the next scheduled activity on this RM Prod. Summary Split record, read via related from its activities (standard activity mixin). | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`rm_prod_summary_spli.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard computed field: the user responsible for the next scheduled activity on this RM Prod. Summary Split record. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time this RM Prod. Summary Split record was created; set automatically. | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created this RM Prod. Summary Split record; set automatically. | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Standard computed name of the RM Prod. Summary Split record as shown in links and dropdowns. | not stored |  |  |
| `has_message` | Has Message | boolean | Standard computed flag: true when this RM Prod. Summary Split record has at least one chatter message. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the RM Prod. Summary Split record, assigned automatically. | stored |  |  |
| `message_attachment_count` | Attachment Count | integer | Standard computed count of attachments linked to this RM Prod. Summary Split record. | not stored |  |  |
| `message_follower_ids` | Followers | one2many → `mail.followers` | Followers (partners) subscribed to notifications on this RM Prod. Summary Split record, from the standard mail thread mixin. Displayed in the form view chatter. | stored | `model mail.followers` (mail) | `view BugFix-Accounting.view_rm_prod_summary_spli_form` |
| `message_has_error` | Message Delivery error | boolean | Standard computed flag: true when a message on this RM Prod. Summary Split record failed to be delivered. | not stored |  |  |
| `message_has_error_counter` | Number of errors | integer | Standard computed count of messages on this RM Prod. Summary Split record with delivery errors. | not stored |  |  |
| `message_has_sms_error` | SMS Delivery error | boolean | Standard computed flag: true when an SMS sent from this RM Prod. Summary Split record failed to be delivered. | not stored |  |  |
| `message_ids` | Messages | one2many → `mail.message` | Chatter messages and log notes posted on this RM Prod. Summary Split record (standard mail thread). Displayed in the form view chatter. | stored | `model mail.message` (mail) | `view BugFix-Accounting.view_rm_prod_summary_spli_form` |
| `message_is_follower` | Is Follower | boolean | Standard computed flag: true when the current user follows this RM Prod. Summary Split record. | not stored |  |  |
| `message_needaction` | Action Needed | boolean | Standard computed flag: true when this RM Prod. Summary Split record has messages needing the current user's attention. | not stored |  |  |
| `message_needaction_counter` | Number of Actions | integer | Standard computed count of messages on this RM Prod. Summary Split record that need the current user's action. | not stored |  |  |
| `message_partner_ids` | Followers (Partners) | many2many → `res.partner` | Standard computed list of partners following this RM Prod. Summary Split record; mainly used for searching. | not stored | `model res.partner` (base) |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard computed field: due date of the current user's next activity on this RM Prod. Summary Split record. | not stored |  |  |
| `rating_ids` | Ratings | one2many → `rating.rating` | Customer ratings linked to this RM Prod. Summary Split record (standard rating mixin); not used by any view or logic in this repo. | stored | `model rating.rating` (rating) |  |
| `website_message_ids` | Website Messages | one2many → `mail.message` | Standard computed subset of chatter messages on this RM Prod. Summary Split record that are visible on the website/portal. | stored | `model mail.message` (mail) |  |
| `write_date` | Last Updated on | datetime | Date and time this RM Prod. Summary Split record was last modified; set automatically. | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last modified this RM Prod. Summary Split record; set automatically. | stored | `model res.users` (base) |  |
| `active` | Active | boolean | Archive flag of the Production Summary - Split report line; defaults to true (ir.default), and unticked (archived) records are hidden from normal lists. Shown in the form and search views. | stored |  | `default BugFix-Accounting.default_rm_prod_summary_spli_active`<br>`view BugFix-Accounting.view_rm_prod_summary_spli_form`<br>`view BugFix-Accounting.view_rm_prod_summary_spli_search` |
| `name` | Name | char | Name of the Production Summary - Split report line, used as its display name. Shown in the list, form and search views. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_rm_prod_summary_spli_list`<br>`view BugFix-Accounting.view_rm_prod_summary_spli_form`<br>`view BugFix-Accounting.view_rm_prod_summary_spli_search` |
| `description` | Description | many2one → `product.product` | Description: the product (`product.product`) this Production Summary - Split report line refers to. Filled by the SRM - RPT - Production Summary - Split action. Shown in the list view. | stored | `model product.product` (product) | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_prod_summary_spli_inherit`<br>`rm_prod_summary_spli.product_code` |
| `header_reference` | Header Reference | char | Text reference to the report header for this Production Summary - Split report line. Set by the SRM - RPT - Production Summary - Split action. Shown in the list view. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_prod_summary_spli_inherit` |
| `job_no` | Job No | char | Job No text on this Production Summary - Split report line; plain stored value. Shown in the list view. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_prod_summary_spli_inherit` |
| `product_code` | Product Code | char | Product Code of the product selected in the line, copied read-only via related field `description.default_code`. Shown in the list view. | related `description.default_code`; not stored | `product.product.default_code` (product)<br>`rm_prod_summary_spli.description` | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_prod_summary_spli_inherit` |
| `quantity` | Quantity | float | Quantity figure on this Production Summary - Split report line; plain stored number with no compute in this repo. Shown in the list view. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_prod_summary_spli_inherit` |
| `sales_report_model_id` | Sales Report Model Id | many2one → `sales_report_model` | Link to the parent Sales Report this Production Summary - Split report line belongs to; inverse of the report's corresponding tab list. Shown in the list view. | stored | `model sales_report_model` (Jinasena_Masterdata_Reporting) | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_prod_summary_spli_inherit` |
| `sequence` | Sequence | integer | Sort order of the Production Summary - Split report line (default 10); used as the drag handle in its list view. | default `10`; stored |  | `default BugFix-Accounting.default_rm_prod_summary_spli_sequence`<br>`view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_rm_prod_summary_spli_list` |
| `split` | Split | float | Split figure on this Production Summary - Split report line; plain stored number with no compute in this repo. Shown in the list view. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_prod_summary_spli_inherit` |
| `split_1` | Split | float | Split figure on this Production Summary - Split report line; plain stored number with no compute in this repo. Shown in the list view. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_prod_summary_spli_inherit` |
| `total` | Total | float | Total figure on this Production Summary - Split report line; plain stored number with no compute in this repo. Shown in the list view. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_prod_summary_spli_inherit` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| RM Prod. Summary Split | `action_rm_prod_summary_split` | Opens **RM Prod. Summary Split** records (tree,form). | `model rm_prod_summary_spli` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_rm_prod_summary_split` (BugFix-Studio-Misc) |

**Views (4):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for rm_prod_summary_spli | `view_rm_prod_summary_spli_form` | form | full form layout with 5 fields | Default form for RM Prod. Summary Split (`rm_prod_summary_spli`): archived ribbon, required Name title, two empty groups and chatter. | `rm_prod_summary_spli.activity_ids`<br>`rm_prod_summary_spli.message_follower_ids`<br>`rm_prod_summary_spli.message_ids`<br>`rm_prod_summary_spli.active`<br>`rm_prod_summary_spli.name` |  |
| Default list view for rm_prod_summary_spli | `view_rm_prod_summary_spli_list` | tree | full tree layout with 2 fields | Default list for RM Prod. Summary Split (`rm_prod_summary_spli`) with sequence handle and Name. | `rm_prod_summary_spli.name`<br>`rm_prod_summary_spli.sequence` | `view BugFix-Accounting.view_default_list_view_for_rm_prod_summary_spli_inherit` |
| Default search view for rm_prod_summary_spli | `view_rm_prod_summary_spli_search` | search | full search layout with 1 fields | Default search view for RM Prod. Summary Split records (`rm_prod_summary_spli`): search by name plus an Archived filter. | `rm_prod_summary_spli.active`<br>`rm_prod_summary_spli.name` |  |
| Odoo Studio: Default list view for rm_prod_summary_spli customization | `view_default_list_view_for_rm_prod_summary_spli_inherit` | tree | set editable=bottom on `//tree[1]`; set column_invisible=1 on `//field[@name='sequence']`; after `//field[@name='sequence']`: add field sales_report_model_id, field header_reference, field product_code, field description, field job_no, field quantity, field total, field split_1, field split; set column_invisible=1 on `//field[@name='name']` | Makes the RM Prod. Summary Split list inline-editable with report link, header reference, product code, description, job no, quantity, total and split columns; sequence and name hidden. | `view BugFix-Accounting.view_rm_prod_summary_spli_list`<br>`rm_prod_summary_spli.description`<br>`rm_prod_summary_spli.header_reference`<br>`rm_prod_summary_spli.job_no`<br>`rm_prod_summary_spli.product_code`<details><summary>+5 more</summary>`rm_prod_summary_spli.quantity`<br>`rm_prod_summary_spli.sales_report_model_id`<br>`rm_prod_summary_spli.split_1`<br>`rm_prod_summary_spli.split`<br>`rm_prod_summary_spli.total`</details> |  |

**Access rights (4):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| RM Prod. Summary Split group_system | `access_rm_prod_summary_split_group_system_2` | Gives **Administration / Settings** read/write/create/delete access to RM Prod. Summary Split records. | `group base.group_system` (base)<br>`model rm_prod_summary_spli` |  |
| RM Prod. Summary Split group_system | `access_rm_prod_summary_split_group_system` | Gives **Administration / Settings** read/write/create/delete access to RM Prod. Summary Split records. | `group base.group_system` (base)<br>`model rm_prod_summary_spli` |  |
| RM Prod. Summary Split group_user | `access_rm_prod_summary_split_group_user_2` | Gives **User types / Internal User** read access to RM Prod. Summary Split records. | `group base.group_user` (base)<br>`model rm_prod_summary_spli` |  |
| RM Prod. Summary Split group_user | `access_rm_prod_summary_split_group_user` | Gives **User types / Internal User** read access to RM Prod. Summary Split records. | `group base.group_user` (base)<br>`model rm_prod_summary_spli` |  |
