# BugFix-Accounting — `x_rm_daily_s3`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_rm_daily_s3` — RM Daily S3

*Created by this repo.* Python: `models/x_rm_daily_s3.py`, `models/x_rm_daily_s3_gap.py`. Record name field: `x_name`.

Other repos that use this model: `server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:x_rm_daily_s3 -->
Purpose not evident from code. It is a report line linked to a Sales Report Model with invoice number, date, a customer link, product, sales centre, quantity and value, shown in a hidden 'Invoices - For the Year' tab; no action in this repo fills these lines.
<!-- /SUMMARY -->

**Fields (41):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard computed field: calendar meeting linked to the next activity on this RM Daily S3 record, if any. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard computed field: due date of the next scheduled activity on this RM Daily S3 record. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard computed flag (Alert or Error) showing that an activity on this RM Daily S3 record is in an exception state. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard computed icon shown when an activity on this RM Daily S3 record is in an exception state. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Scheduled activities (to-dos, calls, meetings) attached to this RM Daily S3 record, from the standard activity mixin. Displayed in the form view chatter. | stored | `model mail.activity` (mail) | `view BugFix-Accounting.ported_view_3810_default_form_view_fo_a5dfdae0_6aa5_4ccc_9466_84fde1363927`<br>`x_rm_daily_s3.activity_summary`<br>`x_rm_daily_s3.activity_type_icon`<br>`x_rm_daily_s3.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard computed activity status of this RM Daily S3 record: Overdue, Today or Planned, based on the nearest activity deadline. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Summary text of the next scheduled activity on this RM Daily S3 record, read via related from its activities. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_rm_daily_s3.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Font Awesome icon of the next activity type on this RM Daily S3 record, read via related from its activities; used for display only. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_rm_daily_s3.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Type of the next scheduled activity on this RM Daily S3 record, read via related from its activities (standard activity mixin). | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_rm_daily_s3.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard computed field: the user responsible for the next scheduled activity on this RM Daily S3 record. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time this RM Daily S3 record was created; set automatically. | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created this RM Daily S3 record; set automatically. | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Standard computed name of the RM Daily S3 record as shown in links and dropdowns. | not stored |  |  |
| `has_message` | Has Message | boolean | Standard computed flag: true when this RM Daily S3 record has at least one chatter message. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the RM Daily S3 record, assigned automatically. | stored |  |  |
| `message_attachment_count` | Attachment Count | integer | Standard computed count of attachments linked to this RM Daily S3 record. | not stored |  |  |
| `message_follower_ids` | Followers | one2many → `mail.followers` | Followers (partners) subscribed to notifications on this RM Daily S3 record, from the standard mail thread mixin. Displayed in the form view chatter. | stored | `model mail.followers` (mail) | `view BugFix-Accounting.ported_view_3810_default_form_view_fo_a5dfdae0_6aa5_4ccc_9466_84fde1363927` |
| `message_has_error` | Message Delivery error | boolean | Standard computed flag: true when a message on this RM Daily S3 record failed to be delivered. | not stored |  |  |
| `message_has_error_counter` | Number of errors | integer | Standard computed count of messages on this RM Daily S3 record with delivery errors. | not stored |  |  |
| `message_has_sms_error` | SMS Delivery error | boolean | Standard computed flag: true when an SMS sent from this RM Daily S3 record failed to be delivered. | not stored |  |  |
| `message_ids` | Messages | one2many → `mail.message` | Chatter messages and log notes posted on this RM Daily S3 record (standard mail thread). Displayed in the form view chatter. | stored | `model mail.message` (mail) | `view BugFix-Accounting.ported_view_3810_default_form_view_fo_a5dfdae0_6aa5_4ccc_9466_84fde1363927` |
| `message_is_follower` | Is Follower | boolean | Standard computed flag: true when the current user follows this RM Daily S3 record. | not stored |  |  |
| `message_needaction` | Action Needed | boolean | Standard computed flag: true when this RM Daily S3 record has messages needing the current user's attention. | not stored |  |  |
| `message_needaction_counter` | Number of Actions | integer | Standard computed count of messages on this RM Daily S3 record that need the current user's action. | not stored |  |  |
| `message_partner_ids` | Followers (Partners) | many2many → `res.partner` | Standard computed list of partners following this RM Daily S3 record; mainly used for searching. | not stored | `model res.partner` (base) |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard computed field: due date of the current user's next activity on this RM Daily S3 record. | not stored |  |  |
| `rating_ids` | Ratings | one2many → `rating.rating` | Customer ratings linked to this RM Daily S3 record (standard rating mixin); not used by any view or logic in this repo. | stored | `model rating.rating` (rating) |  |
| `website_message_ids` | Website Messages | one2many → `mail.message` | Standard computed subset of chatter messages on this RM Daily S3 record that are visible on the website/portal. | stored | `model mail.message` (mail) |  |
| `write_date` | Last Updated on | datetime | Date and time this RM Daily S3 record was last modified; set automatically. | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last modified this RM Daily S3 record; set automatically. | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Archive flag of the RM Daily S3 line (Invoices - For the Year tab, hidden); defaults to true (ir.default), and unticked (archived) records are hidden from normal lists. Shown in the form and search views. | stored |  | `default BugFix-Accounting.default_261_x_rm_daily_s3_x_active`<br>`view BugFix-Accounting.ported_view_3810_default_form_view_fo_a5dfdae0_6aa5_4ccc_9466_84fde1363927`<br>`view BugFix-Accounting.ported_view_3811_default_search_view_caa9a3e6_5a95_452d_b66f_aeaa32017275` |
| `x_name` | Name | char | Name of the RM Daily S3 line (Invoices - For the Year tab, hidden), used as its display name. Shown in the list, form and search views. | stored |  | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b`<br>`view BugFix-Accounting.ported_view_3809_default_list_view_fo_bb0154ee_5685_4655_a271_a89ac8597200`<br>`view BugFix-Accounting.ported_view_3810_default_form_view_fo_a5dfdae0_6aa5_4ccc_9466_84fde1363927`<br>`view BugFix-Accounting.ported_view_3811_default_search_view_caa9a3e6_5a95_452d_b66f_aeaa32017275` |
| `x_studio_invoice_date` | Invoice Date | date | Invoice Date of this RM Daily S3 line (Invoices - For the Year tab, hidden); plain stored date. | stored |  | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_many2one_field_CiZHF` | Partner | many2one → `res.partner` | Customer (partner) of the invoice line; Studio technical name kept from a default "New Many2one" field. Plain stored link. | stored | `model res.partner` (base) | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_number` | Number | char | Number text on this RM Daily S3 line (Invoices - For the Year tab, hidden); plain stored value. | stored |  | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_product_id` | Product | many2one → `product.product` | Product: the product (`product.product`) this RM Daily S3 line (Invoices - For the Year tab, hidden) refers to; plain stored link. | stored | `model product.product` (product) | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_quantity` | Quantity | float | Quantity figure on this RM Daily S3 line (Invoices - For the Year tab, hidden); plain stored number with no compute in this repo. | stored |  | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_sales_centre` | Sales Centre | many2one → `crm.team` | Sales Centre: the sales team (`crm.team`) this RM Daily S3 line (Invoices - For the Year tab, hidden) refers to; plain stored link. | stored | `model crm.team` (sales_team) | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_sales_report_model_id` | Sales Report Model | many2one → `x_sales_report_model` | Link to the parent Sales Report this RM Daily S3 line (Invoices - For the Year tab, hidden) belongs to; inverse of the report's corresponding tab list. Shown in the form view. | stored | `model x_sales_report_model` (Jinasena_Masterdata_Reporting) | `view BugFix-Accounting.ported_view_3814_odoo_studio_default_bbdb4d27_c755_4b18_a675_1142c0001aa0` |
| `x_studio_sequence` | Sequence | integer | Sort order of the RM Daily S3 line (Invoices - For the Year tab, hidden) (default 10); used as the drag handle in its list view. | default `10`; stored |  | `default BugFix-Accounting.default_262_x_rm_daily_s3_x_studio_sequence`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b`<br>`view BugFix-Accounting.ported_view_3809_default_list_view_fo_bb0154ee_5685_4655_a271_a89ac8597200` |
| `x_studio_value` | Value | float | Value figure on this RM Daily S3 line (Invoices - For the Year tab, hidden); plain stored number with no compute in this repo. | stored |  | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| RM Daily S3 | `action_1679_rm_daily_s3` | Opens **RM Daily S3** records (tree,form). | `model x_rm_daily_s3` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_rm_daily_s3` (BugFix-Studio-Misc) |

**Views (4):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_rm_daily_s3 | `ported_view_3810_default_form_view_fo_a5dfdae0_6aa5_4ccc_9466_84fde1363927` | form | full form layout with 5 fields | Default form for RM Daily S3 (`x_rm_daily_s3`): archived ribbon, required Name title, two empty groups and chatter. | `x_rm_daily_s3.activity_ids`<br>`x_rm_daily_s3.message_follower_ids`<br>`x_rm_daily_s3.message_ids`<br>`x_rm_daily_s3.x_active`<br>`x_rm_daily_s3.x_name` | `view BugFix-Accounting.ported_view_3814_odoo_studio_default_bbdb4d27_c755_4b18_a675_1142c0001aa0` |
| Default list view for x_rm_daily_s3 | `ported_view_3809_default_list_view_fo_bb0154ee_5685_4655_a271_a89ac8597200` | tree | full tree layout with 2 fields | Default list for RM Daily S3 (`x_rm_daily_s3`) with sequence handle and Name. | `x_rm_daily_s3.x_name`<br>`x_rm_daily_s3.x_studio_sequence` |  |
| Default search view for x_rm_daily_s3 | `ported_view_3811_default_search_view_caa9a3e6_5a95_452d_b66f_aeaa32017275` | search | full search layout with 1 fields | Default search view for RM Daily S3 records (`x_rm_daily_s3`): search by name plus an Archived filter. | `x_rm_daily_s3.x_active`<br>`x_rm_daily_s3.x_name` |  |
| Odoo Studio: Default form view for x_rm_daily_s3 customization | `ported_view_3814_odoo_studio_default_bbdb4d27_c755_4b18_a675_1142c0001aa0` | form | inside `//group[@name='studio_group_2c1b48_left']`: add field x_studio_sales_report_model_id | Adds a hidden link to the parent Sales Report Model on the RM Daily S3 report-line form. | `view BugFix-Accounting.ported_view_3810_default_form_view_fo_a5dfdae0_6aa5_4ccc_9466_84fde1363927`<br>`x_rm_daily_s3.x_studio_sales_report_model_id` |  |

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| RM Daily S3 group_system | `access_1508_rm_daily_s3_group_system` | Gives **Administration / Settings** read/write/create/delete access to RM Daily S3 records. | `group base.group_system` (base)<br>`model x_rm_daily_s3` |  |
| RM Daily S3 group_user | `access_1509_rm_daily_s3_group_user` | Gives **User types / Internal User** read access to RM Daily S3 records. | `group base.group_user` (base)<br>`model x_rm_daily_s3` |  |
