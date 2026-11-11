# BugFix-Accounting — `advance_payment_acco`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `advance_payment_acco` — Advance Payment Account

*Created by this repo.* Python: `models/advance_payment_acco.py`, `models/x_advance_payment_acco_gap.py`. Record name field: `name`.

**Summary:**

<!-- SUMMARY:model:advance_payment_acco -->
This model is created by this repo. Each record is an Advance Payment Account configuration record that holds the G/L accounts for sales advance payments, purchase advance payments and project advances. The advance payment update actions on invoices, bills and payments read these accounts. The project action reads configuration record id 1 and raises an error if the project account is not set. Users open it from Accounting, Configuration, Online Payments, Advance Payment Account. Create and delete are disabled in the list.
<!-- /SUMMARY -->

**Fields (24):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Calendar meeting linked to the next activity on the Advance Payment Account record; standard mixin field. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Due date of the next scheduled activity on the Advance Payment Account record; standard mixin field. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Warning or error decoration shown when an exception-type activity exists on the Advance Payment Account record; standard mixin field. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Icon shown for an exception activity on the Advance Payment Account record; standard mixin field. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Activities (to-dos, calls, meetings) scheduled on this Advance Payment Account record; standard mail activity mixin field. | stored | `model mail.activity` (mail) | `advance_payment_acco.activity_summary`<br>`advance_payment_acco.activity_type_icon`<br>`advance_payment_acco.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity status of the Advance Payment Account record (Overdue, Today, Planned), computed from its next activity deadline. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Summary text of the next scheduled activity on the Advance Payment Account record; standard mixin field. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`advance_payment_acco.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Font Awesome icon of the next activity type, used in kanban/list activity widgets; standard mixin field. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`advance_payment_acco.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Type of the next scheduled activity on the Advance Payment Account record, read from its activities; standard mixin field. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`advance_payment_acco.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | User responsible for the next scheduled activity on the Advance Payment Account record; standard activity mixin field. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the Advance Payment Account record was created; set automatically. | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the Advance Payment Account record; set automatically. | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name Odoo shows for the Advance Payment Account record in dropdowns, lists and breadcrumbs; computed from its name field. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the Advance Payment Account record, assigned automatically. | stored |  |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Due date of the current user's next activity on the Advance Payment Account record; standard mixin field. | not stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time the Advance Payment Account record was last modified; set automatically. | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last modified the Advance Payment Account record; set automatically. | stored | `model res.users` (base) |  |
| `active` | Active | boolean | Active flag of the Advance Payment Account record: unchecking it archives the record and hides it from default searches; defaults to checked via ir.default. | stored |  | `default BugFix-Accounting.default_advance_payment_acco_active`<br>`view BugFix-Accounting.view_advance_payment_acco_form`<br>`view BugFix-Accounting.view_advance_payment_acco_search`<br>`view BugFix-Accounting.view_advance_payment_acco_search_2` |
| `name` | Name | char | Name of the advance payment account configuration record. | stored |  | `view BugFix-Accounting.view_advance_payment_acco_form`<br>`view BugFix-Accounting.view_advance_payment_acco_list`<br>`view BugFix-Accounting.view_advance_payment_acco_search`<br>`view BugFix-Accounting.view_advance_payment_acco_search_2` |
| `advance_account_project` | Advance Account (Project) | many2one → `account.account` | G/L account used for project advance payments; the advance payment update actions move invoice/bill lines to it and raise an error if it is not set (config record id 1). | stored | `model account.account` (account) | `view BugFix-Accounting.view_default_form_view_for_advance_payment_acco_inherit` |
| `advance_payment_account_purchases` | Account | many2one → `account.account` | Older 'Account' field for purchase advances; not shown in any view in this repo. | stored | `model account.account` (account) |  |
| `advance_payment_account_purchases_1` | Advance Payment Account (Purchases) | many2one → `account.account` | G/L account for purchase advance payments, set on the configuration form. | stored | `model account.account` (account) | `view BugFix-Accounting.view_default_form_view_for_advance_payment_acco_inherit` |
| `advance_payment_account_sales` | Advance Payment Account (Sales) | many2one → `account.account` | G/L account for sales advance payments, set on the configuration form. | stored | `model account.account` (account) | `view BugFix-Accounting.view_default_form_view_for_advance_payment_acco_inherit` |
| `sequence` | Sequence | integer | Sort order of Advance Payment Account records in the list view (drag-and-drop handle); default value set by ir.default. | stored |  | `default BugFix-Accounting.default_advance_payment_acco_sequence`<br>`view BugFix-Accounting.view_advance_payment_acco_list` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Advance Payment Account | `action_advance_payment_account` | Opens **Advance Payment Account** records (tree,form). | `model advance_payment_acco` | `menu BugFix-Accounting.menu_advance_payment_account_2`<br>`menu BugFix-Accounting.menu_advance_payment_account` |

**Views (7):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for advance_payment_acco | `view_advance_payment_acco_form` | form | full form layout with 2 fields | Base form screen for Advance Payment Account records: required Name title, an Archived ribbon when inactive and empty column groups that Studio extensions fill. | `advance_payment_acco.active`<br>`advance_payment_acco.name` | `view BugFix-Accounting.view_default_form_view_for_advance_payment_acco_inherit` |
| Default list view for advance_payment_acco | `view_advance_payment_acco_list` | tree | full tree layout with 2 fields | Base list screen for Advance Payment Account records showing Name with a drag handle for manual ordering by Sequence. | `advance_payment_acco.name`<br>`advance_payment_acco.sequence` | `view BugFix-Accounting.view_default_list_view_for_advance_payment_acco_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_advance_payment_acco_inherit_2` |
| Default search view for advance_payment_acco | `view_advance_payment_acco_search` | search | full search layout with 1 fields | Search bar for Advance Payment Account records: search by Name and an 'Archived' filter to show inactive records. | `advance_payment_acco.active`<br>`advance_payment_acco.name` |  |
| Default search view for advance_payment_acco | `view_advance_payment_acco_search_2` | search | full search layout with 1 fields | Default search view for Advance Payment Accounts configuration records: search by name plus an Archived filter. | `advance_payment_acco.active`<br>`advance_payment_acco.name` |  |
| Odoo Studio: Default form view for advance_payment_acco customization | `view_default_form_view_for_advance_payment_acco_inherit` | form | set string=Advance Payment Accounts on `//group[@name='studio_group_9ff9b8_left']`; inside `//group[@name='studio_group_9ff9b8_left']`: add field advance_payment_account_sales, field advance_payment_account_purchases_1; set string=Advance Accounts on `//group[@name='studio_group_9ff9b8_right']`; inside `//group[@name='studio_group_9ff9b8_right']`: add field advance_account_project | Advance Payment Accounts form: titles the two groups and adds the Advance Payment Account (Sales), Advance Payment Account (Purchases) and Advance Account (Project) fields. | `view BugFix-Accounting.view_advance_payment_acco_form`<br>`advance_payment_acco.advance_account_project`<br>`advance_payment_acco.advance_payment_account_purchases_1`<br>`advance_payment_acco.advance_payment_account_sales` |  |
| Odoo Studio: Default list view for advance_payment_acco customization | `view_default_list_view_for_advance_payment_acco_inherit` | tree | set create=false, delete=false on `//tree[1]` | Studio customization of the Advance Payment Account list: disables creating and deleting records from the list. | `view BugFix-Accounting.view_advance_payment_acco_list` |  |
| Odoo Studio: Default list view for advance_payment_acco customization | `view_default_list_view_for_advance_payment_acco_inherit_2` | tree | set create=false, delete=false on `//tree[1]` | Disables Create and Delete on the Advance Payment Accounts list. | `view BugFix-Accounting.view_advance_payment_acco_list` |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Advance Payment Account group_system | `access_advance_payment_account_group_system` | Gives **Administration / Settings** read/write/create/delete access to Advance Payment Account records. | `group base.group_system` (base)<br>`model advance_payment_acco` |  |
| Advance Payment Account group_user | `access_advance_payment_account_group_user` | Gives **User types / Internal User** read/write/create access to Advance Payment Account records. | `group base.group_user` (base)<br>`model advance_payment_acco` |  |
| advance_payment_acco user access | `access_advance_payment_acco_user` | Gives **User types / Internal User** read/write/create/delete access to Advance Payment Account records. | `group base.group_user` (base)<br>`model advance_payment_acco` |  |
