# BugFix-Accounting — `customer_posting_pro`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `customer_posting_pro` — Customer Posting Profile

*Created by this repo.* Python: `models/customer_posting_pro.py`, `models/x_customer_posting_pro_gap.py`. Record name field: `name`.

**Summary:**

<!-- SUMMARY:model:customer_posting_pro -->
Purpose not evident from code. It is a customer posting profile list with a name, an Item Relation Type (All, Group or Table), notes and a product link that no view shows; it is maintained through its own list and form, and no server action or automation in this repo uses it.
<!-- /SUMMARY -->

**Fields (23):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Calendar meeting linked to the next activity on the Customer Posting Profile record; standard mixin field. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Due date of the next scheduled activity on the Customer Posting Profile record; standard mixin field. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Warning or error decoration shown when an exception-type activity exists on the Customer Posting Profile record; standard mixin field. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Icon shown for an exception activity on the Customer Posting Profile record; standard mixin field. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Activities (to-dos, calls, meetings) scheduled on this Customer Posting Profile record; standard mail activity mixin field. | stored | `model mail.activity` (mail) | `customer_posting_pro.activity_summary`<br>`customer_posting_pro.activity_type_icon`<br>`customer_posting_pro.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity status of the Customer Posting Profile record (Overdue, Today, Planned), computed from its next activity deadline. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Summary text of the next scheduled activity on the Customer Posting Profile record; standard mixin field. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`customer_posting_pro.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Font Awesome icon of the next activity type, used in kanban/list activity widgets; standard mixin field. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`customer_posting_pro.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Type of the next scheduled activity on the Customer Posting Profile record, read from its activities; standard mixin field. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`customer_posting_pro.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | User responsible for the next scheduled activity on the Customer Posting Profile record; standard activity mixin field. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the Customer Posting Profile record was created; set automatically. | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the Customer Posting Profile record; set automatically. | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name Odoo shows for the Customer Posting Profile record in dropdowns, lists and breadcrumbs; computed from its name field. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the Customer Posting Profile record, assigned automatically. | stored |  |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Due date of the current user's next activity on the Customer Posting Profile record; standard mixin field. | not stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time the Customer Posting Profile record was last modified; set automatically. | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last modified the Customer Posting Profile record; set automatically. | stored | `model res.users` (base) |  |
| `active` | Active | boolean | Active flag of the Customer Posting Profile record: unchecking it archives the record and hides it from default searches; defaults to checked via ir.default. | stored |  | `default BugFix-Accounting.default_11_customer_posting_pro_active`<br>`view BugFix-Accounting.view_customer_posting_pro_form`<br>`view BugFix-Accounting.view_customer_posting_pro_search`<br>`view BugFix-Accounting.view_customer_posting_pro_search_2` |
| `name` | Customer Posting Profile | char | Name of the customer posting profile. | stored |  | `view BugFix-Accounting.view_customer_posting_pro_form`<br>`view BugFix-Accounting.view_customer_posting_pro_list`<br>`view BugFix-Accounting.view_customer_posting_pro_search`<br>`view BugFix-Accounting.view_customer_posting_pro_search_2` |
| `item_relation_type` | Item Relation Type | selection: All=All; Group=Group; Table=Table | How items relate to this posting profile: All, Group or Table. | stored |  | `view BugFix-Accounting.view_default_form_view_for_customer_posting_pro_inherit` |
| `many2one_field_eYVbe` | Product | many2one → `product.product` | Product linked to the posting profile; not shown in any view in this repo. | stored | `model product.product` (product) |  |
| `notes` | Notes | text | Free-text notes on the posting profile. | stored |  | `view BugFix-Accounting.view_customer_posting_pro_form` |
| `sequence` | Sequence | integer | Sort order of Customer Posting Profile records in the list view (drag-and-drop handle); default value set by ir.default. | stored |  | `default BugFix-Accounting.default_12_customer_posting_pro_sequence`<br>`view BugFix-Accounting.view_customer_posting_pro_list` |

**Window actions (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Customer Posting Profile | `action_customer_posting_profile` | Opens **Customer Posting Profile** records (tree,form). | `model customer_posting_pro` | `menu BugFix-Studio-Misc.menu_posting_profiles_customer_posting_profile` (BugFix-Studio-Misc) |
| customer_posting_pro | `action_customer_posting_pro` | Opens **Customer Posting Profile** records (tree,form). | `model customer_posting_pro` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_customer_posting_pro` (BugFix-Studio-Misc) |

**Views (6):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for customer_posting_pro | `view_customer_posting_pro_form` | form | full form layout with 3 fields | Base form screen for Customer Posting Profile: required Name title, Archived ribbon and a free-text Notes area. | `customer_posting_pro.active`<br>`customer_posting_pro.name`<br>`customer_posting_pro.notes` | `view BugFix-Accounting.view_default_form_view_for_customer_posting_pro_inherit` |
| Default list view for customer_posting_pro | `view_customer_posting_pro_list` | tree | full tree layout with 2 fields | Base list screen for Customer Posting Profile records showing Name with a drag handle for manual ordering by Sequence. | `customer_posting_pro.name`<br>`customer_posting_pro.sequence` | `view BugFix-Accounting.view_default_list_view_for_customer_posting_pro_inherit` |
| Default search view for customer_posting_pro | `view_customer_posting_pro_search` | search | full search layout with 1 fields | Search bar for Customer Posting Profile records: search by Name and an 'Archived' filter to show inactive records. | `customer_posting_pro.active`<br>`customer_posting_pro.name` |  |
| Default search view for customer_posting_pro | `view_customer_posting_pro_search_2` | search | full search layout with 1 fields | Default search view for Customer Posting Profile records: search by name plus an Archived filter. | `customer_posting_pro.active`<br>`customer_posting_pro.name` |  |
| Odoo Studio: Default form view for customer_posting_pro customization | `view_default_form_view_for_customer_posting_pro_inherit` | form | remove `//form[1]/sheet[1]/div[1]/h1[1]`; inside `//group[@name='studio_group_6195ed_left']`: add field item_relation_type | Customer Posting Profile form: removes the Name title block and adds the Item Relation Type field. | `view BugFix-Accounting.view_customer_posting_pro_form`<br>`customer_posting_pro.item_relation_type` |  |
| Odoo Studio: Default list view for customer_posting_pro customization | `view_default_list_view_for_customer_posting_pro_inherit` | tree | remove `//field[@name='name']`; remove `//field[@name='sequence']` | Removes the Name and Sequence columns from the Customer Posting Profile list. | `view BugFix-Accounting.view_customer_posting_pro_list` |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Customer Posting Profile group_system | `access_customer_posting_profile_group_system` | Gives **Administration / Settings** read/write/create/delete access to Customer Posting Profile records. | `group base.group_system` (base)<br>`model customer_posting_pro` |  |
| Customer Posting Profile group_user | `access_customer_posting_profile_group_user` | Gives **User types / Internal User** read access to Customer Posting Profile records. | `group base.group_user` (base)<br>`model customer_posting_pro` |  |
| customer_posting_pro user access | `access_customer_posting_pro_user` | Gives **User types / Internal User** read/write/create/delete access to Customer Posting Profile records. | `group base.group_user` (base)<br>`model customer_posting_pro` |  |
