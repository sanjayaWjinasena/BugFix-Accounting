# BugFix-Accounting — `x_advance_payment_acco`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_advance_payment_acco` — Advance Payment Account

*Created by this repo.* Python: `models/x_advance_payment_acco.py`, `models/x_advance_payment_acco_gap.py`. Record name field: `x_name`.

**Summary:**

<!-- SUMMARY:model:x_advance_payment_acco -->
This model is created by this repo. Each record is an Advance Payment Account configuration record that holds the G/L accounts for sales advance payments, purchase advance payments and project advances. The advance payment update actions on invoices, bills and payments read these accounts. The project action reads configuration record id 1 and raises an error if the project account is not set. Users open it from Accounting, Configuration, Online Payments, Advance Payment Account. Create and delete are disabled in the list.
<!-- /SUMMARY -->

**Fields (24):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Calendar meeting linked to the next activity on the Advance Payment Account record; standard mixin field. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Due date of the next scheduled activity on the Advance Payment Account record; standard mixin field. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Warning or error decoration shown when an exception-type activity exists on the Advance Payment Account record; standard mixin field. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Icon shown for an exception activity on the Advance Payment Account record; standard mixin field. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Activities (to-dos, calls, meetings) scheduled on this Advance Payment Account record; standard mail activity mixin field. | stored | `model mail.activity` (mail) | `x_advance_payment_acco.activity_summary`<br>`x_advance_payment_acco.activity_type_icon`<br>`x_advance_payment_acco.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity status of the Advance Payment Account record (Overdue, Today, Planned), computed from its next activity deadline. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Summary text of the next scheduled activity on the Advance Payment Account record; standard mixin field. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_advance_payment_acco.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Font Awesome icon of the next activity type, used in kanban/list activity widgets; standard mixin field. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_advance_payment_acco.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Type of the next scheduled activity on the Advance Payment Account record, read from its activities; standard mixin field. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_advance_payment_acco.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | User responsible for the next scheduled activity on the Advance Payment Account record; standard activity mixin field. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the Advance Payment Account record was created; set automatically. | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the Advance Payment Account record; set automatically. | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name Odoo shows for the Advance Payment Account record in dropdowns, lists and breadcrumbs; computed from its name field. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the Advance Payment Account record, assigned automatically. | stored |  |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Due date of the current user's next activity on the Advance Payment Account record; standard mixin field. | not stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time the Advance Payment Account record was last modified; set automatically. | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last modified the Advance Payment Account record; set automatically. | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Active flag of the Advance Payment Account record: unchecking it archives the record and hides it from default searches; defaults to checked via ir.default. | stored |  | `default BugFix-Accounting.default_452_x_advance_payment_acco_x_active`<br>`view BugFix-Accounting.ported_default_form_view_fo_c97b1ccb_8539_4035_a437_f09e7ab96775`<br>`view BugFix-Accounting.ported_default_search_view__0e667438_cb9e_47fc_a925_bb838c4999b2`<br>`view BugFix-Accounting.ported_view_5902_default_search_view_0e667438_cb9e_47fc_a925_bb838c4999b2` |
| `x_name` | Name | char | Name of the advance payment account configuration record. | stored |  | `view BugFix-Accounting.ported_default_form_view_fo_c97b1ccb_8539_4035_a437_f09e7ab96775`<br>`view BugFix-Accounting.ported_default_list_view_fo_631d132b_10b2_4e4a_b9e3_a90375e170a1`<br>`view BugFix-Accounting.ported_default_search_view__0e667438_cb9e_47fc_a925_bb838c4999b2`<br>`view BugFix-Accounting.ported_view_5902_default_search_view_0e667438_cb9e_47fc_a925_bb838c4999b2` |
| `x_studio_advance_account_project` | Advance Account (Project) | many2one → `account.account` | G/L account used for project advance payments; the advance payment update actions move invoice/bill lines to it and raise an error if it is not set (config record id 1). | stored | `model account.account` (account) | `view BugFix-Accounting.ported_view_5904_odoo_studio_default_d44ef857_6f61_4cce_b760_cde110a7cae9` |
| `x_studio_advance_payment_account_purchases` | Account | many2one → `account.account` | Older 'Account' field for purchase advances; not shown in any view in this repo. | stored | `model account.account` (account) |  |
| `x_studio_advance_payment_account_purchases_1` | Advance Payment Account (Purchases) | many2one → `account.account` | G/L account for purchase advance payments, set on the configuration form. | stored | `model account.account` (account) | `view BugFix-Accounting.ported_view_5904_odoo_studio_default_d44ef857_6f61_4cce_b760_cde110a7cae9` |
| `x_studio_advance_payment_account_sales` | Advance Payment Account (Sales) | many2one → `account.account` | G/L account for sales advance payments, set on the configuration form. | stored | `model account.account` (account) | `view BugFix-Accounting.ported_view_5904_odoo_studio_default_d44ef857_6f61_4cce_b760_cde110a7cae9` |
| `x_studio_sequence` | Sequence | integer | Sort order of Advance Payment Account records in the list view (drag-and-drop handle); default value set by ir.default. | stored |  | `default BugFix-Accounting.default_453_x_advance_payment_acco_x_studio_sequence`<br>`view BugFix-Accounting.ported_default_list_view_fo_631d132b_10b2_4e4a_b9e3_a90375e170a1` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Advance Payment Account | `action_2740_advance_payment_account` | Opens **Advance Payment Account** records (tree,form). | `model x_advance_payment_acco` | `menu BugFix-Accounting.menu_1323_advance_payment_account`<br>`menu BugFix-Accounting.menu_f6_advance_payment_account` |

**Views (7):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_advance_payment_acco | `ported_default_form_view_fo_c97b1ccb_8539_4035_a437_f09e7ab96775` | form | full form layout with 2 fields | Base form screen for Advance Payment Account records: required Name title, an Archived ribbon when inactive and empty column groups that Studio extensions fill. | `x_advance_payment_acco.x_active`<br>`x_advance_payment_acco.x_name` | `view BugFix-Accounting.ported_view_5904_odoo_studio_default_d44ef857_6f61_4cce_b760_cde110a7cae9` |
| Default list view for x_advance_payment_acco | `ported_default_list_view_fo_631d132b_10b2_4e4a_b9e3_a90375e170a1` | tree | full tree layout with 2 fields | Base list screen for Advance Payment Account records showing Name with a drag handle for manual ordering by Sequence. | `x_advance_payment_acco.x_name`<br>`x_advance_payment_acco.x_studio_sequence` | `view BugFix-Accounting.ported_odoo_studio_default__41a634d6_2040_4c1a_aca8_66e1b57d1cfa`<br>`view BugFix-Accounting.ported_view_5903_odoo_studio_default_41a634d6_2040_4c1a_aca8_66e1b57d1cfa` |
| Default search view for x_advance_payment_acco | `ported_default_search_view__0e667438_cb9e_47fc_a925_bb838c4999b2` | search | full search layout with 1 fields | Search bar for Advance Payment Account records: search by Name and an 'Archived' filter to show inactive records. | `x_advance_payment_acco.x_active`<br>`x_advance_payment_acco.x_name` |  |
| Default search view for x_advance_payment_acco | `ported_view_5902_default_search_view_0e667438_cb9e_47fc_a925_bb838c4999b2` | search | full search layout with 1 fields | Default search view for Advance Payment Accounts configuration records: search by name plus an Archived filter. | `x_advance_payment_acco.x_active`<br>`x_advance_payment_acco.x_name` |  |
| Odoo Studio: Default form view for x_advance_payment_acco customization | `ported_view_5904_odoo_studio_default_d44ef857_6f61_4cce_b760_cde110a7cae9` | form | set string=Advance Payment Accounts on `//group[@name='studio_group_9ff9b8_left']`; inside `//group[@name='studio_group_9ff9b8_left']`: add field x_studio_advance_payment_account_sales, field x_studio_advance_payment_account_purchases_1; set string=Advance Accounts on `//group[@name='studio_group_9ff9b8_right']`; inside `//group[@name='studio_group_9ff9b8_right']`: add field x_studio_advance_account_project | Advance Payment Accounts form: titles the two groups and adds the Advance Payment Account (Sales), Advance Payment Account (Purchases) and Advance Account (Project) fields. | `view BugFix-Accounting.ported_default_form_view_fo_c97b1ccb_8539_4035_a437_f09e7ab96775`<br>`x_advance_payment_acco.x_studio_advance_account_project`<br>`x_advance_payment_acco.x_studio_advance_payment_account_purchases_1`<br>`x_advance_payment_acco.x_studio_advance_payment_account_sales` |  |
| Odoo Studio: Default list view for x_advance_payment_acco customization | `ported_odoo_studio_default__41a634d6_2040_4c1a_aca8_66e1b57d1cfa` | tree | set create=false, delete=false on `//tree[1]` | Studio customization of the Advance Payment Account list: disables creating and deleting records from the list. | `view BugFix-Accounting.ported_default_list_view_fo_631d132b_10b2_4e4a_b9e3_a90375e170a1` |  |
| Odoo Studio: Default list view for x_advance_payment_acco customization | `ported_view_5903_odoo_studio_default_41a634d6_2040_4c1a_aca8_66e1b57d1cfa` | tree | set create=false, delete=false on `//tree[1]` | Disables Create and Delete on the Advance Payment Accounts list. | `view BugFix-Accounting.ported_default_list_view_fo_631d132b_10b2_4e4a_b9e3_a90375e170a1` |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Advance Payment Account group_system | `access_7203_advance_payment_account_group_system` | Gives **Administration / Settings** read/write/create/delete access to Advance Payment Account records. | `group base.group_system` (base)<br>`model x_advance_payment_acco` |  |
| Advance Payment Account group_user | `access_7204_advance_payment_account_group_user` | Gives **User types / Internal User** read/write/create access to Advance Payment Account records. | `group base.group_user` (base)<br>`model x_advance_payment_acco` |  |
| x_advance_payment_acco user access | `access_x_advance_payment_acco_user` | Gives **User types / Internal User** read/write/create/delete access to Advance Payment Account records. | `group base.group_user` (base)<br>`model x_advance_payment_acco` |  |
