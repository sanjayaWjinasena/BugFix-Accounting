# BugFix-Accounting — `rm_production_orders`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `rm_production_orders` — RM Production Orders

*Created by this repo.* Python: `models/rm_production_orders.py`, `models/x_rm_production_orders_gap.py`. Record name field: `name`.

Other repos that use this model: `server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:rm_production_orders -->
A line of the 'Production Overview - WIP' report run from a Sales Report Model, listing an in-progress manufacturing order with product, location, status, estimated, started and good quantities and start and end dates. Lines are recreated by the 'SRM - RPT - Production Overview - WIP' action and can be viewed as a pivot through the WIP Production Orders action.
<!-- /SUMMARY -->

**Fields (45):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard computed field: calendar meeting linked to the next activity on this RM Production Orders record, if any. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard computed field: due date of the next scheduled activity on this RM Production Orders record. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard computed flag (Alert or Error) showing that an activity on this RM Production Orders record is in an exception state. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard computed icon shown when an activity on this RM Production Orders record is in an exception state. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Scheduled activities (to-dos, calls, meetings) attached to this RM Production Orders record, from the standard activity mixin. Displayed in the form view chatter. | stored | `model mail.activity` (mail) | `view BugFix-Accounting.view_rm_production_orders_form`<br>`rm_production_orders.activity_summary`<br>`rm_production_orders.activity_type_icon`<br>`rm_production_orders.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard computed activity status of this RM Production Orders record: Overdue, Today or Planned, based on the nearest activity deadline. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Summary text of the next scheduled activity on this RM Production Orders record, read via related from its activities. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`rm_production_orders.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Font Awesome icon of the next activity type on this RM Production Orders record, read via related from its activities; used for display only. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`rm_production_orders.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Type of the next scheduled activity on this RM Production Orders record, read via related from its activities (standard activity mixin). | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`rm_production_orders.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard computed field: the user responsible for the next scheduled activity on this RM Production Orders record. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time this RM Production Orders record was created; set automatically. | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created this RM Production Orders record; set automatically. | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Standard computed name of the RM Production Orders record as shown in links and dropdowns. | not stored |  |  |
| `has_message` | Has Message | boolean | Standard computed flag: true when this RM Production Orders record has at least one chatter message. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the RM Production Orders record, assigned automatically. | stored |  |  |
| `message_attachment_count` | Attachment Count | integer | Standard computed count of attachments linked to this RM Production Orders record. | not stored |  |  |
| `message_follower_ids` | Followers | one2many → `mail.followers` | Followers (partners) subscribed to notifications on this RM Production Orders record, from the standard mail thread mixin. Displayed in the form view chatter. | stored | `model mail.followers` (mail) | `view BugFix-Accounting.view_rm_production_orders_form` |
| `message_has_error` | Message Delivery error | boolean | Standard computed flag: true when a message on this RM Production Orders record failed to be delivered. | not stored |  |  |
| `message_has_error_counter` | Number of errors | integer | Standard computed count of messages on this RM Production Orders record with delivery errors. | not stored |  |  |
| `message_has_sms_error` | SMS Delivery error | boolean | Standard computed flag: true when an SMS sent from this RM Production Orders record failed to be delivered. | not stored |  |  |
| `message_ids` | Messages | one2many → `mail.message` | Chatter messages and log notes posted on this RM Production Orders record (standard mail thread). Displayed in the form view chatter. | stored | `model mail.message` (mail) | `view BugFix-Accounting.view_rm_production_orders_form` |
| `message_is_follower` | Is Follower | boolean | Standard computed flag: true when the current user follows this RM Production Orders record. | not stored |  |  |
| `message_needaction` | Action Needed | boolean | Standard computed flag: true when this RM Production Orders record has messages needing the current user's attention. | not stored |  |  |
| `message_needaction_counter` | Number of Actions | integer | Standard computed count of messages on this RM Production Orders record that need the current user's action. | not stored |  |  |
| `message_partner_ids` | Followers (Partners) | many2many → `res.partner` | Standard computed list of partners following this RM Production Orders record; mainly used for searching. | not stored | `model res.partner` (base) |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard computed field: due date of the current user's next activity on this RM Production Orders record. | not stored |  |  |
| `rating_ids` | Ratings | one2many → `rating.rating` | Customer ratings linked to this RM Production Orders record (standard rating mixin); not used by any view or logic in this repo. | stored | `model rating.rating` (rating) |  |
| `website_message_ids` | Website Messages | one2many → `mail.message` | Standard computed subset of chatter messages on this RM Production Orders record that are visible on the website/portal. | stored | `model mail.message` (mail) |  |
| `write_date` | Last Updated on | datetime | Date and time this RM Production Orders record was last modified; set automatically. | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last modified this RM Production Orders record; set automatically. | stored | `model res.users` (base) |  |
| `active` | Active | boolean | Archive flag of the Production Overview - WIP report line; defaults to true (ir.default), and unticked (archived) records are hidden from normal lists. Shown in the form and search views. | stored |  | `default BugFix-Accounting.default_rm_production_orders_active`<br>`view BugFix-Accounting.view_rm_production_orders_form`<br>`view BugFix-Accounting.view_rm_production_orders_search` |
| `name` | Name | char | Name of the Production Overview - WIP report line, used as its display name. Shown in the list, form and search views. | stored |  | `view BugFix-Accounting.view_rm_production_orders_list`<br>`view BugFix-Accounting.view_rm_production_orders_form`<br>`view BugFix-Accounting.view_rm_production_orders_search` |
| `description` | Description | char | Description text on this Production Overview - WIP report line. Filled by the SRM - RPT - Production Overview - WIP action. Shown in the list view. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_production_orders_inherit` |
| `accounting_end` | End | datetime | End date/time of this Production Overview - WIP report line. Filled by the SRM - RPT - Production Overview - WIP action. Shown in the list view. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_production_orders_inherit` |
| `estimated` | Estimated | float | Estimated figure on this Production Overview - WIP report line; stored number. Filled by the SRM - RPT - Production Overview - WIP action. Shown in the list view. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_production_orders_inherit` |
| `good_qty` | Good Qty | float | Good Qty figure on this Production Overview - WIP report line; plain stored number with no compute in this repo. Shown in the list view. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_production_orders_inherit` |
| `header_reference` | Header Reference | char | Text reference to the report header for this Production Overview - WIP report line. Set by the SRM - RPT - Production Overview - WIP action. Shown in the list view. | stored |  | `view BugFix-Accounting.view_default_list_view_for_rm_production_orders_inherit` |
| `product_code` | Product Code | many2one → `product.product` | Product Code: the product (`product.product`) this Production Overview - WIP report line refers to. Filled by the SRM - RPT - Production Overview - WIP action. Shown in the list view. | stored | `model product.product` (product) | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_production_orders_inherit` |
| `production_id` | Production Id | many2one → `mrp.production` | Production Id: the manufacturing order (`mrp.production`) this Production Overview - WIP report line refers to. Filled by the SRM - RPT - Production Overview - WIP action. Shown in the list view. | stored | `model mrp.production` (mrp) | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_production_orders_inherit` |
| `sales_report_model_id` | Sales Report Model Id | many2one → `sales_report_model` | Link to the parent Sales Report this Production Overview - WIP report line belongs to; inverse of the report's corresponding tab list. Shown in the list view. | stored | `model sales_report_model` (Jinasena_Masterdata_Reporting) | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_production_orders_inherit` |
| `sequence` | Sequence | integer | Sort order of the Production Overview - WIP report line (default 10); used as the drag handle in its list view. | default `10`; stored |  | `default BugFix-Accounting.default_rm_production_orders_sequence`<br>`view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_rm_production_orders_list` |
| `start` | Start | datetime | Start date/time of this Production Overview - WIP report line. Filled by the SRM - RPT - Production Overview - WIP action. Shown in the list view. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_production_orders_inherit` |
| `started` | Started | float | Started figure on this Production Overview - WIP report line; stored number. Filled by the SRM - RPT - Production Overview - WIP action. Shown in the list view. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_production_orders_inherit` |
| `status` | Status | selection: draft=Draft; confirmed=Confirmed; progress=In Progress; to_close=To Close; done=Done; canccel=Cancelled | Status of the manufacturing order: Draft, Confirmed, In Progress, To Close, Done or Cancelled (stored key misspelled "canccel"). Filled by the SRM - RPT - Production Overview - WIP action. Shown in the list view. | stored |  | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_production_orders_inherit` |
| `warehouse` | Warehouse | many2one → `stock.location` | Stock location of the manufacturing order, labelled "Warehouse". Filled by the SRM - RPT - Production Overview - WIP action. Shown in the list view. | stored | `model stock.location` (stock) | `view BugFix-Accounting.view_default_form_view_for_sales_report_model_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_rm_production_orders_inherit` |

**Window actions (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Pivot Views | `action_pivot_views` | Opens **RM Production Orders** records (tree,form). | `model rm_production_orders` |  |
| WIP Production Orders | `action_wip_production_orders` | Opens **RM Production Orders** records (pivot). | `model rm_production_orders` | `menu BugFix-Accounting.menu_pivot_views_2`<br>`menu BugFix-Accounting.menu_production_overview_wip_2`<br>`menu BugFix-Accounting.menu_pivot_views`<br>`menu BugFix-Accounting.menu_production_overview_wip`<br>`menu BugFix-Studio-Misc.menu_f6r2_test_app_05_rm_production_orders` (BugFix-Studio-Misc) |

**Views (4):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for rm_production_orders | `view_rm_production_orders_form` | form | full form layout with 5 fields | Default form for RM Production Orders (`rm_production_orders`): archived ribbon, required Name title, two empty groups and chatter. | `rm_production_orders.activity_ids`<br>`rm_production_orders.message_follower_ids`<br>`rm_production_orders.message_ids`<br>`rm_production_orders.active`<br>`rm_production_orders.name` |  |
| Default list view for rm_production_orders | `view_rm_production_orders_list` | tree | full tree layout with 2 fields | Default list for RM Production Orders (`rm_production_orders`) with sequence handle and Name. | `rm_production_orders.name`<br>`rm_production_orders.sequence` | `view BugFix-Accounting.view_default_list_view_for_rm_production_orders_inherit` |
| Default search view for rm_production_orders | `view_rm_production_orders_search` | search | full search layout with 1 fields | Default search view for RM Production Orders records (`rm_production_orders`): search by name plus an Archived filter. | `rm_production_orders.active`<br>`rm_production_orders.name` |  |
| Odoo Studio: Default list view for rm_production_orders customization | `view_default_list_view_for_rm_production_orders_inherit` | tree | replace `//field[@name='name']`: add field header_reference, field production_id, field product_code, field description, field warehouse, field status, field estimated, field started, field good_qty, field start, field accounting_end, field sales_report_model_id | Replaces Name in the RM Production Orders list with production report columns: Production Id, Product Code, Description, Warehouse, Status, Estimated, Started, Good Qty, Start and End dates, plus hidden header reference and report link. | `view BugFix-Accounting.view_rm_production_orders_list`<br>`rm_production_orders.description`<br>`rm_production_orders.accounting_end`<br>`rm_production_orders.estimated`<br>`rm_production_orders.good_qty`<details><summary>+8 more</summary>`rm_production_orders.header_reference`<br>`rm_production_orders.product_code`<br>`rm_production_orders.production_id`<br>`rm_production_orders.sales_report_model_id`<br>`rm_production_orders.start`<br>`rm_production_orders.started`<br>`rm_production_orders.status`<br>`rm_production_orders.warehouse`</details> |  |

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| RM Production Orders group_system | `access_rm_production_orders_group_system` | Gives **Administration / Settings** read/write/create/delete access to RM Production Orders records. | `group base.group_system` (base)<br>`model rm_production_orders` |  |
| RM Production Orders group_user | `access_rm_production_orders_group_user` | Gives **User types / Internal User** read access to RM Production Orders records. | `group base.group_user` (base)<br>`model rm_production_orders` |  |
