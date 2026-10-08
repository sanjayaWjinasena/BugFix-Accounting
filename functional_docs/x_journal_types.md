# BugFix-Accounting — `x_journal_types`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_journal_types` — Journal Types

*Extends a model created by `BugFix-Maintenance`.* Python: `models/x_journal_types.py`, `models/x_journal_types_gap.py`. Record name field: `x_name`.

Other repos that use this model: `access right BugFix-Stock.access_x_journal_types_user` (BugFix-Stock)<br>`maintenance.equipment.category.x_studio_journal_type` (BugFix-Maintenance)<br>`maintenance.request.x_studio_journal_type_1` (BugFix-Maintenance)<br>`server action BugFix-Stock.server_action_2448_movement_journals_update_offset_account` (BugFix-Stock)<br>`stock.picking.x_studio_journal_type` (BugFix-Stock)<br>`x_material_request.x_studio_journal_type` (BugFix-Stock)

**Summary:**

<!-- SUMMARY:model:x_journal_types -->
Journal type master (created by BugFix-Maintenance) that this repo also declares in Python, with Journal Type name, Description, an Offset Account and Company. This repo adds an inline-editable list showing Description, Offset Account and a read-only Company, a 'JIN - Company Id' automation that stamps the active company on save, and a multi-company record rule. Journal types are referenced by maintenance, stock picking and stock server actions in other repos.
<!-- /SUMMARY -->

**Fields (36):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Calendar meeting linked to the next activity on the Journal Types record; standard mixin field. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Due date of the next scheduled activity on the Journal Types record; standard mixin field. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Warning or error decoration shown when an exception-type activity exists on the Journal Types record; standard mixin field. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Icon shown for an exception activity on the Journal Types record; standard mixin field. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Activities (to-dos, calls, meetings) scheduled on this Journal Types record; standard mail activity mixin field. | stored | `model mail.activity` (mail) | `view BugFix-Accounting.ported_view_5321_default_form_view_fo_dbddc8a1_ea9d_47ba_8335_c08e4a53fc5c`<br>`x_journal_types.activity_summary`<br>`x_journal_types.activity_type_icon`<br>`x_journal_types.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity status of the Journal Types record (Overdue, Today, Planned), computed from its next activity deadline. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Summary text of the next scheduled activity on the Journal Types record; standard mixin field. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_journal_types.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Font Awesome icon of the next activity type, used in kanban/list activity widgets; standard mixin field. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_journal_types.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Type of the next scheduled activity on the Journal Types record, read from its activities; standard mixin field. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_journal_types.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | User responsible for the next scheduled activity on the Journal Types record; standard activity mixin field. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the Journal Types record was created; set automatically. Used as the trigger of the on-creation automation(s): jin company id in journal types. | stored |  | `automation BugFix-Accounting.base_automation_337_jin_company_id_in_journal_types` |
| `create_uid` | Created by | many2one → `res.users` | User who created the Journal Types record; set automatically. | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name Odoo shows for the Journal Types record in dropdowns, lists and breadcrumbs; computed from its name field. | not stored |  |  |
| `has_message` | Has Message | boolean | Whether the Journal Types record has any chatter messages; standard chatter field. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the Journal Types record, assigned automatically. | stored |  |  |
| `message_attachment_count` | Attachment Count | integer | Number of attachments on the Journal Types record; standard chatter field. | not stored |  |  |
| `message_follower_ids` | Followers | one2many → `mail.followers` | Followers who receive notifications for the Journal Types record, shown in the chatter. | stored | `model mail.followers` (mail) | `view BugFix-Accounting.ported_view_5321_default_form_view_fo_dbddc8a1_ea9d_47ba_8335_c08e4a53fc5c` |
| `message_has_error` | Message Delivery error | boolean | Whether a message on the Journal Types record failed to be delivered; standard chatter field. | not stored |  |  |
| `message_has_error_counter` | Number of errors | integer | Number of messages on the Journal Types record with delivery errors; standard chatter field. | not stored |  |  |
| `message_has_sms_error` | SMS Delivery error | boolean | Whether an SMS sent from the Journal Types record failed; standard chatter field. | not stored |  |  |
| `message_ids` | Messages | one2many → `mail.message` | Chatter messages and log notes posted on the Journal Types record. | stored | `model mail.message` (mail) | `view BugFix-Accounting.ported_view_5321_default_form_view_fo_dbddc8a1_ea9d_47ba_8335_c08e4a53fc5c` |
| `message_is_follower` | Is Follower | boolean | Whether the current user follows the Journal Types record; standard chatter field. | not stored |  |  |
| `message_needaction` | Action Needed | boolean | Whether the Journal Types record has unread messages that need the current user's attention; standard chatter field. | not stored |  |  |
| `message_needaction_counter` | Number of Actions | integer | Number of messages on the Journal Types record needing the current user's attention; standard chatter field. | not stored |  |  |
| `message_partner_ids` | Followers (Partners) | many2many → `res.partner` | Partners following the Journal Types record; standard chatter field used for searching. | not stored | `model res.partner` (base) |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Due date of the current user's next activity on the Journal Types record; standard mixin field. | not stored |  |  |
| `rating_ids` | Ratings | one2many → `rating.rating` | Customer ratings linked to the Journal Types record; standard field from the mail thread mixin, not used here. | stored | `model rating.rating` (rating) |  |
| `website_message_ids` | Website Messages | one2many → `mail.message` | Messages on the Journal Types record that are visible on the website/portal; standard chatter field. | stored | `model mail.message` (mail) |  |
| `write_date` | Last Updated on | datetime | Date and time the Journal Types record was last modified; set automatically. | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last modified the Journal Types record; set automatically. | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Active flag of the Journal Types record: unchecking it archives the record and hides it from default searches; defaults to checked via ir.default. | stored |  | `default BugFix-Accounting.default_390_x_journal_types_x_active`<br>`view BugFix-Accounting.ported_view_5321_default_form_view_fo_dbddc8a1_ea9d_47ba_8335_c08e4a53fc5c`<br>`view BugFix-Accounting.ported_view_5322_default_search_view_d3c181ad_9bc3_4cfc_9d60_2500bd38fe9f` |
| `x_name` | Journal Type | char | Name of the journal type, shown in its list, form and search views. | stored; required |  | `view BugFix-Accounting.ported_view_5320_default_list_view_fo_02152264_7fd7_4b5e_8a84_ca3714db9fad`<br>`view BugFix-Accounting.ported_view_5321_default_form_view_fo_dbddc8a1_ea9d_47ba_8335_c08e4a53fc5c`<br>`view BugFix-Accounting.ported_view_5322_default_search_view_d3c181ad_9bc3_4cfc_9d60_2500bd38fe9f` |
| `x_studio_company_id` | Company | many2one → `res.company` | Company the Journal Types record belongs to; enforced by a multi-company record rule and filled on creation by the 'JIN Company Id' automation. | stored | `model res.company` (base) | `record rule BugFix-Accounting.rule_629_jin_multi_company_journal_types`<br>`server action BugFix-Accounting.sa_f5_x_journal_types_jin_company_id_in_journal_types`<br>`server action BugFix-Accounting.server_action_2871_jin_company_id_in_journal_types`<br>`view BugFix-Accounting.ported_view_5326_odoo_studio_default_7879380a_9ecc_4ca6_bfd3_fa82b991c3ce` |
| `x_studio_description` | Description | char | Free-text description of the journal type. | stored |  | `view BugFix-Accounting.ported_view_5326_odoo_studio_default_7879380a_9ecc_4ca6_bfd3_fa82b991c3ce` |
| `x_studio_offset_account` | Offset Account | many2one → `account.account` | Default offset (contra) G/L account for this journal type, entered on its form; not read by logic in this repo. | stored | `model account.account` (account) | `view BugFix-Accounting.ported_view_5326_odoo_studio_default_7879380a_9ecc_4ca6_bfd3_fa82b991c3ce` |
| `x_studio_sequence` | Sequence | integer | Sort order of Journal Types records in the list view (drag-and-drop handle); default value set by ir.default. | stored |  | `default BugFix-Accounting.default_391_x_journal_types_x_studio_sequence`<br>`view BugFix-Accounting.ported_view_5320_default_list_view_fo_02152264_7fd7_4b5e_8a84_ca3714db9fad` |

**Server actions (2):**

- **Execute Code** (`server_action_2871_jin_company_id_in_journal_types`, type `code`)
  - Function: Run by the JIN automation: sets the Journal Type's Company to the user's currently active company.
  - Depends on: `model res.company` (base), `model x_journal_types` (BugFix-Maintenance), `x_journal_types.x_studio_company_id` (BugFix-Maintenance)
  - Used by: `automation BugFix-Accounting.base_automation_337_jin_company_id_in_journal_types`
  <details><summary>code (5 lines)</summary>

```python

company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
company = env['res.company'].browse(company_id)

record['x_studio_company_id'] = company.id
```
  </details>
- **JIN - Company Id in Journal Types** (`sa_f5_x_journal_types_jin_company_id_in_journal_types`, type `code`)
  - Function: Sets the Journal Types record's Company field to the user's currently active company (first allowed company in context).
  - Depends on: `model res.company` (base), `model x_journal_types` (BugFix-Maintenance), `x_journal_types.x_studio_company_id` (BugFix-Maintenance)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (4 lines)</summary>

```python
company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
company = env['res.company'].browse(company_id)

record['x_studio_company_id'] = company.id
```
  </details>
**Automations (1):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| JIN - Company Id in Journal Types | `base_automation_337_jin_company_id_in_journal_types` |  | When a record is created or updated on Journal Types, runs _Execute Code_. | `model x_journal_types` (BugFix-Maintenance)<br>`server action BugFix-Accounting.server_action_2871_jin_company_id_in_journal_types`<br>`x_journal_types.create_date` (BugFix-Maintenance) |  |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Journal Types | `action_2447_journal_types` | Opens **Journal Types** records (tree,form). | `model x_journal_types` (BugFix-Maintenance) | `menu BugFix-Accounting.menu_1132_journal_types`<br>`menu BugFix-Accounting.menu_f6_journal_types` |

**Views (4):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_journal_types | `ported_view_5321_default_form_view_fo_dbddc8a1_ea9d_47ba_8335_c08e4a53fc5c` | form | full form layout with 5 fields | Default form for Journal Types: archived ribbon, required Name title, two empty groups and chatter. | `x_journal_types.activity_ids`<br>`x_journal_types.message_follower_ids`<br>`x_journal_types.message_ids`<br>`x_journal_types.x_active` (BugFix-Maintenance)<br>`x_journal_types.x_name` (BugFix-Maintenance) |  |
| Default list view for x_journal_types | `ported_view_5320_default_list_view_fo_02152264_7fd7_4b5e_8a84_ca3714db9fad` | tree | full tree layout with 2 fields | Base list of Journal Types with sequence handle and Name; extended by its Studio customization. | `x_journal_types.x_name` (BugFix-Maintenance)<br>`x_journal_types.x_studio_sequence` (BugFix-Maintenance) | `view BugFix-Accounting.ported_view_5326_odoo_studio_default_7879380a_9ecc_4ca6_bfd3_fa82b991c3ce` |
| Default search view for x_journal_types | `ported_view_5322_default_search_view_d3c181ad_9bc3_4cfc_9d60_2500bd38fe9f` | search | full search layout with 1 fields | Default search view for Journal Types: search by name plus an Archived filter. | `x_journal_types.x_active` (BugFix-Maintenance)<br>`x_journal_types.x_name` (BugFix-Maintenance) |  |
| Odoo Studio: Default list view for x_journal_types customization | `ported_view_5326_odoo_studio_default_7879380a_9ecc_4ca6_bfd3_fa82b991c3ce` | tree | set editable=bottom on `//tree[1]`; set string=Journal Type on `//field[@name='x_name']`; after `//field[@name='x_name']`: add field x_studio_description, field x_studio_offset_account, field x_studio_company_id | Makes the Journal Types list inline-editable, labels Name as 'Journal Type' and adds Description, Offset Account and read-only Company columns. | `view BugFix-Accounting.ported_view_5320_default_list_view_fo_02152264_7fd7_4b5e_8a84_ca3714db9fad`<br>`x_journal_types.x_studio_company_id` (BugFix-Maintenance)<br>`x_journal_types.x_studio_description` (BugFix-Maintenance)<br>`x_journal_types.x_studio_offset_account` (BugFix-Maintenance) |  |

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Journal Types group_system | `access_5950_journal_types_group_system` | Gives **Administration / Settings** read/write/create/delete access to Journal Types records. | `group base.group_system` (base)<br>`model x_journal_types` (BugFix-Maintenance) |  |
| Journal Types group_user | `access_5951_journal_types_group_user` | Gives **User types / Internal User** read access to Journal Types records. | `group base.group_user` (base)<br>`model x_journal_types` (BugFix-Maintenance) |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| JIN - Multi-Company - Journal Types | `rule_629_jin_multi_company_journal_types` | For everyone (global rule): read/write/create/delete on Journal Types only where `['|', ('x_studio_company_id', 'in', company_ids), ('x_studio_company_id', '=', False)]`. | `model x_journal_types` (BugFix-Maintenance)<br>`x_journal_types.x_studio_company_id` (BugFix-Maintenance) |  |
