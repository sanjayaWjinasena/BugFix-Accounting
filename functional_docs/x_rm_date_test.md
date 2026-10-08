# BugFix-Accounting — `x_rm_date_test`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_rm_date_test` — RM Date Test

*Created by this repo.* Python: `models/x_rm_date_test.py`, `models/x_rm_date_test_gap.py`. Record name field: `x_name`.

**Summary:**

<!-- SUMMARY:model:x_rm_date_test -->
Purpose not evident from code. It is a test model with a single Date Test field shown in its list; no business logic uses it.
<!-- /SUMMARY -->

**Fields (34):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard computed field: calendar meeting linked to the next activity on this RM Date Test record, if any. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard computed field: due date of the next scheduled activity on this RM Date Test record. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard computed flag (Alert or Error) showing that an activity on this RM Date Test record is in an exception state. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard computed icon shown when an activity on this RM Date Test record is in an exception state. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Scheduled activities (to-dos, calls, meetings) attached to this RM Date Test record, from the standard activity mixin. Displayed in the form view chatter. | stored | `model mail.activity` (mail) | `view BugFix-Accounting.ported_view_3915_default_form_view_fo_d88777b5_8251_4e43_ad64_0e506e49f9fb`<br>`x_rm_date_test.activity_summary`<br>`x_rm_date_test.activity_type_icon`<br>`x_rm_date_test.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard computed activity status of this RM Date Test record: Overdue, Today or Planned, based on the nearest activity deadline. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Summary text of the next scheduled activity on this RM Date Test record, read via related from its activities. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_rm_date_test.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Font Awesome icon of the next activity type on this RM Date Test record, read via related from its activities; used for display only. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_rm_date_test.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Type of the next scheduled activity on this RM Date Test record, read via related from its activities (standard activity mixin). | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_rm_date_test.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard computed field: the user responsible for the next scheduled activity on this RM Date Test record. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time this RM Date Test record was created; set automatically. | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created this RM Date Test record; set automatically. | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Standard computed name of the RM Date Test record as shown in links and dropdowns. | not stored |  |  |
| `has_message` | Has Message | boolean | Standard computed flag: true when this RM Date Test record has at least one chatter message. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the RM Date Test record, assigned automatically. | stored |  |  |
| `message_attachment_count` | Attachment Count | integer | Standard computed count of attachments linked to this RM Date Test record. | not stored |  |  |
| `message_follower_ids` | Followers | one2many → `mail.followers` | Followers (partners) subscribed to notifications on this RM Date Test record, from the standard mail thread mixin. Displayed in the form view chatter. | stored | `model mail.followers` (mail) | `view BugFix-Accounting.ported_view_3915_default_form_view_fo_d88777b5_8251_4e43_ad64_0e506e49f9fb` |
| `message_has_error` | Message Delivery error | boolean | Standard computed flag: true when a message on this RM Date Test record failed to be delivered. | not stored |  |  |
| `message_has_error_counter` | Number of errors | integer | Standard computed count of messages on this RM Date Test record with delivery errors. | not stored |  |  |
| `message_has_sms_error` | SMS Delivery error | boolean | Standard computed flag: true when an SMS sent from this RM Date Test record failed to be delivered. | not stored |  |  |
| `message_ids` | Messages | one2many → `mail.message` | Chatter messages and log notes posted on this RM Date Test record (standard mail thread). Displayed in the form view chatter. | stored | `model mail.message` (mail) | `view BugFix-Accounting.ported_view_3915_default_form_view_fo_d88777b5_8251_4e43_ad64_0e506e49f9fb` |
| `message_is_follower` | Is Follower | boolean | Standard computed flag: true when the current user follows this RM Date Test record. | not stored |  |  |
| `message_needaction` | Action Needed | boolean | Standard computed flag: true when this RM Date Test record has messages needing the current user's attention. | not stored |  |  |
| `message_needaction_counter` | Number of Actions | integer | Standard computed count of messages on this RM Date Test record that need the current user's action. | not stored |  |  |
| `message_partner_ids` | Followers (Partners) | many2many → `res.partner` | Standard computed list of partners following this RM Date Test record; mainly used for searching. | not stored | `model res.partner` (base) |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard computed field: due date of the current user's next activity on this RM Date Test record. | not stored |  |  |
| `rating_ids` | Ratings | one2many → `rating.rating` | Customer ratings linked to this RM Date Test record (standard rating mixin); not used by any view or logic in this repo. | stored | `model rating.rating` (rating) |  |
| `website_message_ids` | Website Messages | one2many → `mail.message` | Standard computed subset of chatter messages on this RM Date Test record that are visible on the website/portal. | stored | `model mail.message` (mail) |  |
| `write_date` | Last Updated on | datetime | Date and time this RM Date Test record was last modified; set automatically. | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last modified this RM Date Test record; set automatically. | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Archive flag of the RM Date Test (test model); defaults to true (ir.default), and unticked (archived) records are hidden from normal lists. Shown in the form and search views. | stored |  | `default BugFix-Accounting.default_283_x_rm_date_test_x_active`<br>`view BugFix-Accounting.ported_view_3915_default_form_view_fo_d88777b5_8251_4e43_ad64_0e506e49f9fb`<br>`view BugFix-Accounting.ported_view_3916_default_search_view_e7a99ab7_8776_4f92_acf1_7409a5917f9d` |
| `x_name` | Name | char | Name of the RM Date Test (test model), used as its display name. Shown in the list, form and search views. | stored |  | `view BugFix-Accounting.ported_view_3914_default_list_view_fo_77a72e54_ec9a_410e_8cec_7eb0098c24da`<br>`view BugFix-Accounting.ported_view_3915_default_form_view_fo_d88777b5_8251_4e43_ad64_0e506e49f9fb`<br>`view BugFix-Accounting.ported_view_3916_default_search_view_e7a99ab7_8776_4f92_acf1_7409a5917f9d` |
| `x_studio_date_test` | Date Test | date | Test date field on the RM Date Test model; shown in its list view. No business logic uses it. | stored |  | `view BugFix-Accounting.ported_view_3917_odoo_studio_default_6f8232ab_b685_499c_a92e_e1f0a6371c68` |
| `x_studio_sequence` | Sequence | integer | Sort order of the RM Date Test (test model) (default 10); used as the drag handle in its list view. | default `10`; stored |  | `default BugFix-Accounting.default_284_x_rm_date_test_x_studio_sequence`<br>`view BugFix-Accounting.ported_view_3914_default_list_view_fo_77a72e54_ec9a_410e_8cec_7eb0098c24da` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| RM Date Test | `action_1744_rm_date_test` | Opens **RM Date Test** records (tree,form). | `model x_rm_date_test` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_rm_date_test` (BugFix-Studio-Misc) |

**Views (4):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_rm_date_test | `ported_view_3915_default_form_view_fo_d88777b5_8251_4e43_ad64_0e506e49f9fb` | form | full form layout with 5 fields | Default form for RM Date Test (`x_rm_date_test`): archived ribbon, required Name title, two empty groups and chatter. | `x_rm_date_test.activity_ids`<br>`x_rm_date_test.message_follower_ids`<br>`x_rm_date_test.message_ids`<br>`x_rm_date_test.x_active`<br>`x_rm_date_test.x_name` |  |
| Default list view for x_rm_date_test | `ported_view_3914_default_list_view_fo_77a72e54_ec9a_410e_8cec_7eb0098c24da` | tree | full tree layout with 2 fields | Default list for RM Date Test (`x_rm_date_test`) with sequence handle and Name. | `x_rm_date_test.x_name`<br>`x_rm_date_test.x_studio_sequence` | `view BugFix-Accounting.ported_view_3917_odoo_studio_default_6f8232ab_b685_499c_a92e_e1f0a6371c68` |
| Default search view for x_rm_date_test | `ported_view_3916_default_search_view_e7a99ab7_8776_4f92_acf1_7409a5917f9d` | search | full search layout with 1 fields | Default search view for RM Date Test records (`x_rm_date_test`): search by name plus an Archived filter. | `x_rm_date_test.x_active`<br>`x_rm_date_test.x_name` |  |
| Odoo Studio: Default list view for x_rm_date_test customization | `ported_view_3917_odoo_studio_default_6f8232ab_b685_499c_a92e_e1f0a6371c68` | tree | after `//field[@name='x_studio_sequence']`: add field x_studio_date_test; set column_invisible=1 on `//field[@name='x_name']` | Adds a Date Test column and hides the Name column in the RM Date Test list; appears to be a test model. | `view BugFix-Accounting.ported_view_3914_default_list_view_fo_77a72e54_ec9a_410e_8cec_7eb0098c24da`<br>`x_rm_date_test.x_studio_date_test` |  |

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| RM Date Test group_system | `access_1529_rm_date_test_group_system` | Gives **Administration / Settings** read/write/create/delete access to RM Date Test records. | `group base.group_system` (base)<br>`model x_rm_date_test` |  |
| RM Date Test group_user | `access_1530_rm_date_test_group_user` | Gives **User types / Internal User** read access to RM Date Test records. | `group base.group_user` (base)<br>`model x_rm_date_test` |  |
