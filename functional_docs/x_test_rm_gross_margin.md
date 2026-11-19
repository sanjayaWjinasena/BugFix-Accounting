# BugFix-Accounting — `x_test_rm_gross_margin`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_test_rm_gross_margin` — Test - RM Gross Margin - Actuals

*Created by this repo.* Python: `models/x_test_rm_gross_margin.py`, `models/x_test_rm_gross_margin_gap.py`. Record name field: `x_name`.

**Summary:**

<!-- SUMMARY:model:x_test_rm_gross_margin -->
Purpose not evident from code. It is a test model named 'Test - RM Gross Margin - Actuals' with only a description, active flag and sequence, plus default views and a window action.
<!-- /SUMMARY -->

**Fields (20):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard computed field: calendar meeting linked to the next activity on this Test - RM Gross Margin - Actuals record, if any. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard computed field: due date of the next scheduled activity on this Test - RM Gross Margin - Actuals record. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard computed flag (Alert or Error) showing that an activity on this Test - RM Gross Margin - Actuals record is in an exception state. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard computed icon shown when an activity on this Test - RM Gross Margin - Actuals record is in an exception state. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Scheduled activities (to-dos, calls, meetings) attached to this Test - RM Gross Margin - Actuals record, from the standard activity mixin. | stored | `model mail.activity` (mail) | `x_test_rm_gross_margin.activity_summary`<br>`x_test_rm_gross_margin.activity_type_icon`<br>`x_test_rm_gross_margin.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard computed activity status of this Test - RM Gross Margin - Actuals record: Overdue, Today or Planned, based on the nearest activity deadline. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Summary text of the next scheduled activity on this Test - RM Gross Margin - Actuals record, read via related from its activities. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_test_rm_gross_margin.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Font Awesome icon of the next activity type on this Test - RM Gross Margin - Actuals record, read via related from its activities; used for display only. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_test_rm_gross_margin.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Type of the next scheduled activity on this Test - RM Gross Margin - Actuals record, read via related from its activities (standard activity mixin). | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_test_rm_gross_margin.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard computed field: the user responsible for the next scheduled activity on this Test - RM Gross Margin - Actuals record. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time this Test - RM Gross Margin - Actuals record was created; set automatically. | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created this Test - RM Gross Margin - Actuals record; set automatically. | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Standard computed name of the Test - RM Gross Margin - Actuals record as shown in links and dropdowns. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the Test - RM Gross Margin - Actuals record, assigned automatically. | stored |  |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard computed field: due date of the current user's next activity on this Test - RM Gross Margin - Actuals record. | not stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time this Test - RM Gross Margin - Actuals record was last modified; set automatically. | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last modified this Test - RM Gross Margin - Actuals record; set automatically. | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Archive flag of the Test - RM Gross Margin - Actuals record (test model); defaults to true (ir.default), and unticked (archived) records are hidden from normal lists. Shown in the form and search views. | stored |  | `default BugFix-Accounting.default_642_x_test_rm_gross_margin_x_active`<br>`view BugFix-Accounting.ported_default_form_view_fo_e77232e4_e7f3_4769_97c0_439ce924b337`<br>`view BugFix-Accounting.ported_default_search_view__1ca0ea84_3938_4f26_ad80_7824d77d00f2`<br>`view BugFix-Accounting.ported_view_9491_default_search_view_1ca0ea84_3938_4f26_ad80_7824d77d00f2` |
| `x_name` | Description | char | Description of the test gross margin record; shown in its list, form and search views. | stored; required |  | `view BugFix-Accounting.ported_default_form_view_fo_e77232e4_e7f3_4769_97c0_439ce924b337`<br>`view BugFix-Accounting.ported_default_list_view_fo_ebc1fec3_02e8_4e3a_a42a_8a43aeef04c4`<br>`view BugFix-Accounting.ported_default_search_view__1ca0ea84_3938_4f26_ad80_7824d77d00f2`<br>`view BugFix-Accounting.ported_view_9491_default_search_view_1ca0ea84_3938_4f26_ad80_7824d77d00f2` |
| `x_studio_sequence` | Sequence | integer | Sort order of the Test - RM Gross Margin - Actuals record (test model) (default 10); used as the drag handle in its list view. | stored |  | `default BugFix-Accounting.default_643_x_test_rm_gross_margin_x_studio_sequence`<br>`view BugFix-Accounting.ported_default_list_view_fo_ebc1fec3_02e8_4e3a_a42a_8a43aeef04c4` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Test - RM Gross Margin - Actuals | `action_3623_test_rm_gross_margin_actuals` | Opens **Test - RM Gross Margin - Actuals** records (tree,form). | `model x_test_rm_gross_margin` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_test_rm_gross_margin_actuals` (BugFix-Studio-Misc) |

**Views (4):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_test_rm_gross_margin | `ported_default_form_view_fo_e77232e4_e7f3_4769_97c0_439ce924b337` | form | full form layout with 2 fields | Base form screen for Test - RM Gross Margin - Actuals records: required Name title, an Archived ribbon when inactive and empty column groups that Studio extensions fill. | `x_test_rm_gross_margin.x_active`<br>`x_test_rm_gross_margin.x_name` |  |
| Default list view for x_test_rm_gross_margin | `ported_default_list_view_fo_ebc1fec3_02e8_4e3a_a42a_8a43aeef04c4` | tree | full tree layout with 2 fields | Base list screen for Test - RM Gross Margin - Actuals records showing Name with a drag handle for manual ordering by Sequence. | `x_test_rm_gross_margin.x_name`<br>`x_test_rm_gross_margin.x_studio_sequence` |  |
| Default search view for x_test_rm_gross_margin | `ported_default_search_view__1ca0ea84_3938_4f26_ad80_7824d77d00f2` | search | full search layout with 1 fields | Search bar for Test - RM Gross Margin - Actuals records: search by Name and an 'Archived' filter to show inactive records. | `x_test_rm_gross_margin.x_active`<br>`x_test_rm_gross_margin.x_name` |  |
| Default search view for x_test_rm_gross_margin | `ported_view_9491_default_search_view_1ca0ea84_3938_4f26_ad80_7824d77d00f2` | search | full search layout with 1 fields | Default search view for the Test RM Gross Margin model: search by name plus an Archived filter. | `x_test_rm_gross_margin.x_active`<br>`x_test_rm_gross_margin.x_name` |  |

**Access rights (5):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Test - RM Gross Margin - Actuals group_system | `access_8576_test___rm_gross_margin___actuals_group_system` | Gives **Administration / Settings** read/write/create/delete access to Test - RM Gross Margin - Actuals records. | `group base.group_system` (base)<br>`model x_test_rm_gross_margin` |  |
| Test - RM Gross Margin - Actuals group_system | `access_8576_test_rm_gross_margin_actuals_group_system` | Gives **Administration / Settings** read/write/create/delete access to Test - RM Gross Margin - Actuals records. | `group base.group_system` (base)<br>`model x_test_rm_gross_margin` |  |
| Test - RM Gross Margin - Actuals group_user | `access_8577_test___rm_gross_margin___actuals_group_user` | Gives **User types / Internal User** read/write/create access to Test - RM Gross Margin - Actuals records. | `group base.group_user` (base)<br>`model x_test_rm_gross_margin` |  |
| Test - RM Gross Margin - Actuals group_user | `access_8577_test_rm_gross_margin_actuals_group_user` | Gives **User types / Internal User** read/write/create access to Test - RM Gross Margin - Actuals records. | `group base.group_user` (base)<br>`model x_test_rm_gross_margin` |  |
| x_test_rm_gross_margin user access | `access_x_test_rm_gross_margin_user` | Gives **User types / Internal User** read/write/create/delete access to Test - RM Gross Margin - Actuals records. | `group base.group_user` (base)<br>`model x_test_rm_gross_margin` |  |
