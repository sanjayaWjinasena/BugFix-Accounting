# BugFix-Accounting — `rm_daily_s2`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `rm_daily_s2` — RM Daily S2

*Created by this repo.* Python: `models/rm_daily_s2.py`, `models/x_rm_daily_s2_gap.py`. Record name field: `name`.

Other repos that use this model: `server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:rm_daily_s2 -->
Purpose not evident from code. It is a report line linked to a Sales Report Model with invoice number, date, partner, product, sales centre, quantity and value, shown in a hidden 'Invoices - For the Month' tab; no action in this repo fills these lines.
<!-- /SUMMARY -->

**Fields (41):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard computed field: calendar meeting linked to the next activity on this RM Daily S2 record, if any. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard computed field: due date of the next scheduled activity on this RM Daily S2 record. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard computed flag (Alert or Error) showing that an activity on this RM Daily S2 record is in an exception state. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard computed icon shown when an activity on this RM Daily S2 record is in an exception state. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Scheduled activities (to-dos, calls, meetings) attached to this RM Daily S2 record, from the standard activity mixin. Displayed in the form view chatter. | stored | `model mail.activity` (mail) | `view BugFix-Accounting.view_rm_daily_s2_form`<br>`rm_daily_s2.activity_summary`<br>`rm_daily_s2.activity_type_icon`<br>`rm_daily_s2.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard computed activity status of this RM Daily S2 record: Overdue, Today or Planned, based on the nearest activity deadline. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Summary text of the next scheduled activity on this RM Daily S2 record, read via related from its activities. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`rm_daily_s2.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Font Awesome icon of the next activity type on this RM Daily S2 record, read via related from its activities; used for display only. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`rm_daily_s2.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Type of the next scheduled activity on this RM Daily S2 record, read via related from its activities (standard activity mixin). | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`rm_daily_s2.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard computed field: the user responsible for the next scheduled activity on this RM Daily S2 record. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time this RM Daily S2 record was created; set automatically. | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created this RM Daily S2 record; set automatically. | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Standard computed name of the RM Daily S2 record as shown in links and dropdowns. | not stored |  |  |
| `has_message` | Has Message | boolean | Standard computed flag: true when this RM Daily S2 record has at least one chatter message. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the RM Daily S2 record, assigned automatically. | stored |  |  |
| `message_attachment_count` | Attachment Count | integer | Standard computed count of attachments linked to this RM Daily S2 record. | not stored |  |  |
| `message_follower_ids` | Followers | one2many → `mail.followers` | Followers (partners) subscribed to notifications on this RM Daily S2 record, from the standard mail thread mixin. Displayed in the form view chatter. | stored | `model mail.followers` (mail) | `view BugFix-Accounting.view_rm_daily_s2_form` |
| `message_has_error` | Message Delivery error | boolean | Standard computed flag: true when a message on this RM Daily S2 record failed to be delivered. | not stored |  |  |
| `message_has_error_counter` | Number of errors | integer | Standard computed count of messages on this RM Daily S2 record with delivery errors. | not stored |  |  |
| `message_has_sms_error` | SMS Delivery error | boolean | Standard computed flag: true when an SMS sent from this RM Daily S2 record failed to be delivered. | not stored |  |  |
| `message_ids` | Messages | one2many → `mail.message` | Chatter messages and log notes posted on this RM Daily S2 record (standard mail thread). Displayed in the form view chatter. | stored | `model mail.message` (mail) | `view BugFix-Accounting.view_rm_daily_s2_form` |
| `message_is_follower` | Is Follower | boolean | Standard computed flag: true when the current user follows this RM Daily S2 record. | not stored |  |  |
| `message_needaction` | Action Needed | boolean | Standard computed flag: true when this RM Daily S2 record has messages needing the current user's attention. | not stored |  |  |
| `message_needaction_counter` | Number of Actions | integer | Standard computed count of messages on this RM Daily S2 record that need the current user's action. | not stored |  |  |
| `message_partner_ids` | Followers (Partners) | many2many → `res.partner` | Standard computed list of partners following this RM Daily S2 record; mainly used for searching. | not stored | `model res.partner` (base) |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard computed field: due date of the current user's next activity on this RM Daily S2 record. | not stored |  |  |
| `rating_ids` | Ratings | one2many → `rating.rating` | Customer ratings linked to this RM Daily S2 record (standard rating mixin); not used by any view or logic in this repo. | stored | `model rating.rating` (rating) |  |
| `website_message_ids` | Website Messages | one2many → `mail.message` | Standard computed subset of chatter messages on this RM Daily S2 record that are visible on the website/portal. | stored | `model mail.message` (mail) |  |
| `write_date` | Last Updated on | datetime | Date and time this RM Daily S2 record was last modified; set automatically. | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last modified this RM Daily S2 record; set automatically. | stored | `model res.users` (base) |  |
| `active` | Active | boolean | Archive flag of the RM Daily S2 line (Invoices - For the Month tab, hidden); defaults to true (ir.default), and unticked (archived) records are hidden from normal lists. Shown in the form and search views. | stored |  | `default BugFix-Accounting.default_rm_daily_s2_active`<br>`view BugFix-Accounting.view_rm_daily_s2_form`<br>`view BugFix-Accounting.view_rm_daily_s2_search` |
| `name` | Name | char | Name of the RM Daily S2 line (Invoices - For the Month tab, hidden), used as its display name. Shown in the list, form and search views. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_rm_daily_s2_list`<br>`view BugFix-Accounting.view_rm_daily_s2_form`<br>`view BugFix-Accounting.view_rm_daily_s2_search` |
| `accounting_invoice_date` | Invoice Date | date | Invoice Date of this RM Daily S2 line (Invoices - For the Month tab, hidden); plain stored date. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit` |
| `number` | Number | char | Number text on this RM Daily S2 line (Invoices - For the Month tab, hidden); plain stored value. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit` |
| `partner` | Partner | many2one → `res.partner` | Partner: the contact (`res.partner`) this RM Daily S2 line (Invoices - For the Month tab, hidden) refers to; plain stored link. | stored | `model res.partner` (base) | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit` |
| `product_id` | Product | many2one → `product.product` | Product: the product (`product.product`) this RM Daily S2 line (Invoices - For the Month tab, hidden) refers to; plain stored link. | stored | `model product.product` (product) |  |
| `quantity` | Quantity | float | Quantity figure on this RM Daily S2 line (Invoices - For the Month tab, hidden); plain stored number with no compute in this repo. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit` |
| `sales_centre` | Sales Centre | many2one → `crm.team` | Sales Centre: the sales team (`crm.team`) this RM Daily S2 line (Invoices - For the Month tab, hidden) refers to; plain stored link. | stored | `model crm.team` (sales_team) | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit` |
| `sales_report_model_id` | Sales Report Model | many2one → `sales_report_model` | Link to the parent Sales Report this RM Daily S2 line (Invoices - For the Month tab, hidden) belongs to; inverse of the report's corresponding tab list. Shown in the form view. | stored | `model sales_report_model` (Jinasena_Masterdata_Reporting) | `view BugFix-Accounting.view_default_form_view_for_rm_daily_s2_inherit` |
| `sequence` | Sequence | integer | Sort order of the RM Daily S2 line (Invoices - For the Month tab, hidden) (default 10); used as the drag handle in its list view. | default `10`; stored |  | `default BugFix-Accounting.default_rm_daily_s2_sequence`<br>`view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_rm_daily_s2_list` |
| `value` | Value | float | Value figure on this RM Daily S2 line (Invoices - For the Month tab, hidden); plain stored number with no compute in this repo. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| RM Daily S2 | `action_rm_daily_s2` | Opens **RM Daily S2** records (tree,form). | `model rm_daily_s2` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_rm_daily_s2` (BugFix-Studio-Misc) |

**Views (4):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for rm_daily_s2 | `view_rm_daily_s2_form` | form | full form layout with 5 fields | Default form for RM Daily S2 (`rm_daily_s2`): archived ribbon, required Name title, two empty groups and chatter. | `rm_daily_s2.activity_ids`<br>`rm_daily_s2.message_follower_ids`<br>`rm_daily_s2.message_ids`<br>`rm_daily_s2.active`<br>`rm_daily_s2.name` | `view BugFix-Accounting.view_default_form_view_for_rm_daily_s2_inherit` |
| Default list view for rm_daily_s2 | `view_rm_daily_s2_list` | tree | full tree layout with 2 fields | Default list for RM Daily S2 (`rm_daily_s2`) with sequence handle and Name. | `rm_daily_s2.name`<br>`rm_daily_s2.sequence` |  |
| Default search view for rm_daily_s2 | `view_rm_daily_s2_search` | search | full search layout with 1 fields | Default search view for RM Daily S2 records (`rm_daily_s2`): search by name plus an Archived filter. | `rm_daily_s2.active`<br>`rm_daily_s2.name` |  |
| Odoo Studio: Default form view for rm_daily_s2 customization | `view_default_form_view_for_rm_daily_s2_inherit` | form | inside `//group[@name='studio_group_f18209_left']`: add field sales_report_model_id | Adds a hidden link to the parent Sales Report Model on the RM Daily S2 report-line form. | `view BugFix-Accounting.view_rm_daily_s2_form`<br>`rm_daily_s2.sales_report_model_id` |  |

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| RM Daily S2 group_system | `access_rm_daily_s2_group_system` | Gives **Administration / Settings** read/write/create/delete access to RM Daily S2 records. | `group base.group_system` (base)<br>`model rm_daily_s2` |  |
| RM Daily S2 group_user | `access_rm_daily_s2_group_user` | Gives **User types / Internal User** read access to RM Daily S2 records. | `group base.group_user` (base)<br>`model rm_daily_s2` |  |
