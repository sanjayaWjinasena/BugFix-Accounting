# BugFix-Accounting — `x_customer_posting_pro`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_customer_posting_pro` — Customer Posting Profile

*Created by this repo.* Python: `models/x_customer_posting_pro.py`, `models/x_customer_posting_pro_gap.py`. Record name field: `x_name`.

**Summary:**

<!-- SUMMARY:model:x_customer_posting_pro -->
Purpose not evident from code. It is a customer posting profile list with a name, an Item Relation Type (All, Group or Table), notes and a product link that no view shows; it is maintained through its own list and form, and no server action or automation in this repo uses it.
<!-- /SUMMARY -->

**Fields (23):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Calendar meeting linked to the next activity on the Customer Posting Profile record; standard mixin field. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Due date of the next scheduled activity on the Customer Posting Profile record; standard mixin field. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Warning or error decoration shown when an exception-type activity exists on the Customer Posting Profile record; standard mixin field. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Icon shown for an exception activity on the Customer Posting Profile record; standard mixin field. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Activities (to-dos, calls, meetings) scheduled on this Customer Posting Profile record; standard mail activity mixin field. | stored | `model mail.activity` (mail) | `x_customer_posting_pro.activity_summary`<br>`x_customer_posting_pro.activity_type_icon`<br>`x_customer_posting_pro.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity status of the Customer Posting Profile record (Overdue, Today, Planned), computed from its next activity deadline. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Summary text of the next scheduled activity on the Customer Posting Profile record; standard mixin field. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_customer_posting_pro.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Font Awesome icon of the next activity type, used in kanban/list activity widgets; standard mixin field. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_customer_posting_pro.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Type of the next scheduled activity on the Customer Posting Profile record, read from its activities; standard mixin field. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_customer_posting_pro.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | User responsible for the next scheduled activity on the Customer Posting Profile record; standard activity mixin field. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the Customer Posting Profile record was created; set automatically. | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the Customer Posting Profile record; set automatically. | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name Odoo shows for the Customer Posting Profile record in dropdowns, lists and breadcrumbs; computed from its name field. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the Customer Posting Profile record, assigned automatically. | stored |  |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Due date of the current user's next activity on the Customer Posting Profile record; standard mixin field. | not stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time the Customer Posting Profile record was last modified; set automatically. | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last modified the Customer Posting Profile record; set automatically. | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Active flag of the Customer Posting Profile record: unchecking it archives the record and hides it from default searches; defaults to checked via ir.default. | stored |  | `default BugFix-Accounting.default_11_x_customer_posting_pro_x_active`<br>`view BugFix-Accounting.ported_default_form_view_fo_f49a8f85_9bb2_43ef_8f4f_8b962b411265`<br>`view BugFix-Accounting.ported_default_search_view__75c14789_fbd8_4c3b_9714_053aebf3de17`<br>`view BugFix-Accounting.ported_view_2312_default_search_view_75c14789_fbd8_4c3b_9714_053aebf3de17` |
| `x_name` | Customer Posting Profile | char | Name of the customer posting profile. | stored |  | `view BugFix-Accounting.ported_default_form_view_fo_f49a8f85_9bb2_43ef_8f4f_8b962b411265`<br>`view BugFix-Accounting.ported_default_list_view_fo_3031fe1e_398f_4098_9918_014ea6ba462f`<br>`view BugFix-Accounting.ported_default_search_view__75c14789_fbd8_4c3b_9714_053aebf3de17`<br>`view BugFix-Accounting.ported_view_2312_default_search_view_75c14789_fbd8_4c3b_9714_053aebf3de17` |
| `x_studio_item_relation_type` | Item Relation Type | selection: All=All; Group=Group; Table=Table | How items relate to this posting profile: All, Group or Table. | stored |  | `view BugFix-Accounting.ported_view_2313_odoo_studio_default_48b939b5_01fe_4c2d_8fb8_dbabd7799b2f` |
| `x_studio_many2one_field_eYVbe` | Product | many2one → `product.product` | Product linked to the posting profile; not shown in any view in this repo. | stored | `model product.product` (product) |  |
| `x_studio_notes` | Notes | text | Free-text notes on the posting profile. | stored |  | `view BugFix-Accounting.ported_default_form_view_fo_f49a8f85_9bb2_43ef_8f4f_8b962b411265` |
| `x_studio_sequence` | Sequence | integer | Sort order of Customer Posting Profile records in the list view (drag-and-drop handle); default value set by ir.default. | stored |  | `default BugFix-Accounting.default_12_x_customer_posting_pro_x_studio_sequence`<br>`view BugFix-Accounting.ported_default_list_view_fo_3031fe1e_398f_4098_9918_014ea6ba462f` |

**Window actions (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Customer Posting Profile | `action_779_customer_posting_profile` | Opens **Customer Posting Profile** records (tree,form). | `model x_customer_posting_pro` | `menu BugFix-Studio-Misc.menu_f6r3_posting_profiles_customer_posting_profile` (BugFix-Studio-Misc) |
| x_customer_posting_pro | `action_2678_x_customer_posting_pro` | Opens **Customer Posting Profile** records (tree,form). | `model x_customer_posting_pro` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_x_customer_posting_pro` (BugFix-Studio-Misc) |

**Views (6):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_customer_posting_pro | `ported_default_form_view_fo_f49a8f85_9bb2_43ef_8f4f_8b962b411265` | form | full form layout with 3 fields | Base form screen for Customer Posting Profile: required Name title, Archived ribbon and a free-text Notes area. | `x_customer_posting_pro.x_active`<br>`x_customer_posting_pro.x_name`<br>`x_customer_posting_pro.x_studio_notes` | `view BugFix-Accounting.ported_view_2313_odoo_studio_default_48b939b5_01fe_4c2d_8fb8_dbabd7799b2f` |
| Default list view for x_customer_posting_pro | `ported_default_list_view_fo_3031fe1e_398f_4098_9918_014ea6ba462f` | tree | full tree layout with 2 fields | Base list screen for Customer Posting Profile records showing Name with a drag handle for manual ordering by Sequence. | `x_customer_posting_pro.x_name`<br>`x_customer_posting_pro.x_studio_sequence` | `view BugFix-Accounting.ported_view_2314_odoo_studio_default_92045e29_920d_457c_8bbc_c4568805914e` |
| Default search view for x_customer_posting_pro | `ported_default_search_view__75c14789_fbd8_4c3b_9714_053aebf3de17` | search | full search layout with 1 fields | Search bar for Customer Posting Profile records: search by Name and an 'Archived' filter to show inactive records. | `x_customer_posting_pro.x_active`<br>`x_customer_posting_pro.x_name` |  |
| Default search view for x_customer_posting_pro | `ported_view_2312_default_search_view_75c14789_fbd8_4c3b_9714_053aebf3de17` | search | full search layout with 1 fields | Default search view for Customer Posting Profile records: search by name plus an Archived filter. | `x_customer_posting_pro.x_active`<br>`x_customer_posting_pro.x_name` |  |
| Odoo Studio: Default form view for x_customer_posting_pro customization | `ported_view_2313_odoo_studio_default_48b939b5_01fe_4c2d_8fb8_dbabd7799b2f` | form | remove `//form[1]/sheet[1]/div[1]/h1[1]`; inside `//group[@name='studio_group_6195ed_left']`: add field x_studio_item_relation_type | Customer Posting Profile form: removes the Name title block and adds the Item Relation Type field. | `view BugFix-Accounting.ported_default_form_view_fo_f49a8f85_9bb2_43ef_8f4f_8b962b411265`<br>`x_customer_posting_pro.x_studio_item_relation_type` |  |
| Odoo Studio: Default list view for x_customer_posting_pro customization | `ported_view_2314_odoo_studio_default_92045e29_920d_457c_8bbc_c4568805914e` | tree | remove `//field[@name='x_name']`; remove `//field[@name='x_studio_sequence']` | Removes the Name and Sequence columns from the Customer Posting Profile list. | `view BugFix-Accounting.ported_default_list_view_fo_3031fe1e_398f_4098_9918_014ea6ba462f` |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Customer Posting Profile group_system | `access_1117_customer_posting_profile_group_system` | Gives **Administration / Settings** read/write/create/delete access to Customer Posting Profile records. | `group base.group_system` (base)<br>`model x_customer_posting_pro` |  |
| Customer Posting Profile group_user | `access_1118_customer_posting_profile_group_user` | Gives **User types / Internal User** read access to Customer Posting Profile records. | `group base.group_user` (base)<br>`model x_customer_posting_pro` |  |
| x_customer_posting_pro user access | `access_x_customer_posting_pro_user` | Gives **User types / Internal User** read/write/create/delete access to Customer Posting Profile records. | `group base.group_user` (base)<br>`model x_customer_posting_pro` |  |
