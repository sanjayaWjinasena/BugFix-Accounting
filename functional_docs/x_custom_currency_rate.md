# BugFix-Accounting — `x_custom_currency_rate`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_custom_currency_rate` — Custom Currency Rate

*Created by this repo.* Python: `models/x_custom_currency_rate.py`, `models/x_custom_currency_rate_gap.py`. Record name field: `x_name`.

Other repos that use this model: `server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Stock.server_action_1305_imp_consignment_vendor_despatch` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_1318_imp_allocate_consignment_header_charges` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_1321_imp_consignment_custom_duty` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_2118_project_update_month_end_entries` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_3647_consignment_vendor_dispatch_bugfix_purchase` (BugFix-Stock)

**Summary:**

<!-- SUMMARY:model:x_custom_currency_rate -->
A dated exchange rate (start date, end date and rate) belonging to a Custom Currency, used for import costing. Rates are edited inline in a list opened from the custom currency's Rates button. An automation raises 'End Date must be Greater than Start Date' when the dates are reversed, and the company is stamped on creation and enforced by a multi-company record rule.
<!-- /SUMMARY -->

**Fields (25):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Calendar meeting linked to the next activity on the Custom Currency Rate record; standard mixin field. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Due date of the next scheduled activity on the Custom Currency Rate record; standard mixin field. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Warning or error decoration shown when an exception-type activity exists on the Custom Currency Rate record; standard mixin field. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Icon shown for an exception activity on the Custom Currency Rate record; standard mixin field. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Activities (to-dos, calls, meetings) scheduled on this Custom Currency Rate record; standard mail activity mixin field. | stored | `model mail.activity` (mail) | `x_custom_currency_rate.activity_summary`<br>`x_custom_currency_rate.activity_type_icon`<br>`x_custom_currency_rate.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity status of the Custom Currency Rate record (Overdue, Today, Planned), computed from its next activity deadline. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Summary text of the next scheduled activity on the Custom Currency Rate record; standard mixin field. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_custom_currency_rate.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Font Awesome icon of the next activity type, used in kanban/list activity widgets; standard mixin field. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_custom_currency_rate.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Type of the next scheduled activity on the Custom Currency Rate record, read from its activities; standard mixin field. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_custom_currency_rate.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | User responsible for the next scheduled activity on the Custom Currency Rate record; standard activity mixin field. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the Custom Currency Rate record was created; set automatically. Used as the trigger of the on-creation automation(s): jin company id in custom currency rate. | stored |  | `automation BugFix-Accounting.base_automation_311_jin_company_id_in_custom_currency_rate` |
| `create_uid` | Created by | many2one → `res.users` | User who created the Custom Currency Rate record; set automatically. | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name Odoo shows for the Custom Currency Rate record in dropdowns, lists and breadcrumbs; computed from its name field. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the Custom Currency Rate record, assigned automatically. | stored |  |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Due date of the current user's next activity on the Custom Currency Rate record; standard mixin field. | not stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time the Custom Currency Rate record was last modified; set automatically. | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last modified the Custom Currency Rate record; set automatically. | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Active flag of the Custom Currency Rate record: unchecking it archives the record and hides it from default searches; defaults to checked via ir.default. | stored |  | `default BugFix-Accounting.default_157_x_custom_currency_rate_x_active`<br>`view BugFix-Accounting.ported_default_form_view_fo_f5872bac_d1f7_4709_a9b1_364b0db1710c`<br>`view BugFix-Accounting.ported_default_search_view__008371aa_6777_483b_a35b_55bb47e097eb`<br>`view BugFix-Accounting.ported_view_2926_default_search_view_008371aa_6777_483b_a35b_55bb47e097eb` |
| `x_name` | Name | char | Name of the custom currency rate record. | stored |  | `view BugFix-Accounting.ported_default_form_view_fo_f5872bac_d1f7_4709_a9b1_364b0db1710c`<br>`view BugFix-Accounting.ported_default_list_view_fo_ca009934_0cbf_4bef_b9a5_cc7156daa1a9`<br>`view BugFix-Accounting.ported_default_search_view__008371aa_6777_483b_a35b_55bb47e097eb`<br>`view BugFix-Accounting.ported_view_2926_default_search_view_008371aa_6777_483b_a35b_55bb47e097eb` |
| `x_studio_company_id` | Company | many2one → `res.company` | Company the Custom Currency Rate record belongs to; enforced by a multi-company record rule and filled on creation by the 'JIN Company Id' automation. | stored | `model res.company` (base) | `record rule BugFix-Accounting.rule_563_jin_multi_company_custom_currency_rate`<br>`record rule BugFix-Accounting.rule_f7_x_custom_currency_rate_jin_multi_company_custom_currency_rate`<br>`server action BugFix-Accounting.sa_f5_x_custom_currency_rate_jin_company_id_in_custom_currency_rate`<br>`server action BugFix-Accounting.server_action_2675_jin_company_id_in_custom_currency_rate`<br>`view BugFix-Accounting.ported_view_2930_odoo_studio_default_3d5acdf8_7c5e_4d86_bee2_d071d148e8e7` |
| `x_studio_custom_currency_id` | Custom Currency Id | many2one → `x_custom_currency` | Custom currency this rate belongs to; the 'Rates' window action filters by it. | stored | `model x_custom_currency` | `view BugFix-Accounting.ported_view_2929_odoo_studio_default_98249da6_8d85_410b_8ba9_952472bdd50c`<br>`window action BugFix-Accounting.act_custom_currency_rates`<br>`window action BugFix-Accounting.action_1310_rates` |
| `x_studio_end_date` | End Date | date | Last date the rate applies; the 'IMP - Validate From/To Dates' automation checks it against the start date. | stored |  | `automation BugFix-Accounting.base_automation_60_imp_validate_from_to_dates_in_custom_rates`<br>`server action BugFix-Accounting.sa_f5_x_custom_currency_rate_imp_validate_from_to_dates_in_custom_rates`<br>`server action BugFix-Accounting.server_action_1311_imp_validate_from_to_dates_in_custom_rates`<br>`view BugFix-Accounting.ported_view_2929_odoo_studio_default_98249da6_8d85_410b_8ba9_952472bdd50c`<br>`view BugFix-Accounting.ported_view_2930_odoo_studio_default_3d5acdf8_7c5e_4d86_bee2_d071d148e8e7` |
| `x_studio_rate` | Rate | float | Exchange rate value for the period. | stored |  | `view BugFix-Accounting.ported_view_2929_odoo_studio_default_98249da6_8d85_410b_8ba9_952472bdd50c`<br>`view BugFix-Accounting.ported_view_2930_odoo_studio_default_3d5acdf8_7c5e_4d86_bee2_d071d148e8e7` |
| `x_studio_sequence` | Sequence | integer | Sort order of Custom Currency Rate records in the list view (drag-and-drop handle); default value set by ir.default. | stored |  | `default BugFix-Accounting.default_158_x_custom_currency_rate_x_studio_sequence`<br>`view BugFix-Accounting.ported_default_list_view_fo_ca009934_0cbf_4bef_b9a5_cc7156daa1a9` |
| `x_studio_start_date` | Start Date | date | First date the rate applies; validated against the end date by the 'IMP - Validate From/To Dates' automation. | stored |  | `automation BugFix-Accounting.base_automation_60_imp_validate_from_to_dates_in_custom_rates`<br>`server action BugFix-Accounting.sa_f5_x_custom_currency_rate_imp_validate_from_to_dates_in_custom_rates`<br>`server action BugFix-Accounting.server_action_1311_imp_validate_from_to_dates_in_custom_rates`<br>`view BugFix-Accounting.ported_view_2929_odoo_studio_default_98249da6_8d85_410b_8ba9_952472bdd50c`<br>`view BugFix-Accounting.ported_view_2930_odoo_studio_default_3d5acdf8_7c5e_4d86_bee2_d071d148e8e7` |

**Server actions (4):**

- **Execute Code** (`server_action_1311_imp_validate_from_to_dates_in_custom_rates`, type `code`)
  - Function: Run by the custom-rate date validation automation: raises 'End Date must be Greater than Start Date' if End Date is before Start Date.
  - Depends on: `model x_custom_currency_rate`, `x_custom_currency_rate.x_studio_end_date`, `x_custom_currency_rate.x_studio_start_date`
  - Used by: `automation BugFix-Accounting.base_automation_60_imp_validate_from_to_dates_in_custom_rates`
  <details><summary>code (3 lines)</summary>

```python

if record.x_studio_end_date < record.x_studio_start_date:
  raise UserError('End Date must be Greater than Start Date.')
```
  </details>
- **Execute Code** (`server_action_2675_jin_company_id_in_custom_currency_rate`, type `code`)
  - Function: Run by the JIN automation: sets the Custom Currency Rate's Company to the user's active company.
  - Depends on: `model res.company` (base), `model x_custom_currency_rate`, `x_custom_currency_rate.x_studio_company_id`
  - Used by: `automation BugFix-Accounting.base_automation_311_jin_company_id_in_custom_currency_rate`
  <details><summary>code (5 lines)</summary>

```python

company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
company = env['res.company'].browse(company_id)

record['x_studio_company_id'] = company.id
```
  </details>
- **IMP - Validate From To Dates in Custom Rates** (`sa_f5_x_custom_currency_rate_imp_validate_from_to_dates_in_custom_rates`, type `code`)
  - Function: Raises an error 'End Date must be Greater than Start Date' when a custom currency rate's End Date is before its Start Date.
  - Depends on: `model x_custom_currency_rate`, `x_custom_currency_rate.x_studio_end_date`, `x_custom_currency_rate.x_studio_start_date`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (2 lines)</summary>

```python
if record.x_studio_end_date < record.x_studio_start_date:
  raise UserError('End Date must be Greater than Start Date.')
```
  </details>
- **JIN - Company Id in Custom Currency Rate** (`sa_f5_x_custom_currency_rate_jin_company_id_in_custom_currency_rate`, type `code`)
  - Function: Sets the Custom Currency Rate record's Company field to the user's currently active company (first allowed company in context).
  - Depends on: `model res.company` (base), `model x_custom_currency_rate`, `x_custom_currency_rate.x_studio_company_id`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (4 lines)</summary>

```python
company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
company = env['res.company'].browse(company_id)

record['x_studio_company_id'] = company.id
```
  </details>
**Automations (4):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| IMP - Validate From To Dates in Custom Rates | `automation_60_imp_validate_from_to_dates_in_custom_rates` |  | When a record is created or updated on Custom Currency Rate, runs nothing (no action linked). | `model x_custom_currency_rate` |  |
| IMP - Validate From To Dates in Custom Rates | `base_automation_60_imp_validate_from_to_dates_in_custom_rates` |  | When a record is created or updated on Custom Currency Rate, runs _Execute Code_. | `model x_custom_currency_rate`<br>`server action BugFix-Accounting.server_action_1311_imp_validate_from_to_dates_in_custom_rates`<br>`x_custom_currency_rate.x_studio_end_date`<br>`x_custom_currency_rate.x_studio_start_date` |  |
| JIN - Company Id in Custom Currency Rate | `automation_311_jin_company_id_in_custom_currency_rate` | archived | When a record is created or updated on Custom Currency Rate, runs nothing (no action linked). **Archived — does not run.** | `model x_custom_currency_rate` |  |
| JIN - Company Id in Custom Currency Rate | `base_automation_311_jin_company_id_in_custom_currency_rate` |  | When a record is created or updated on Custom Currency Rate, runs _Execute Code_. | `model x_custom_currency_rate`<br>`server action BugFix-Accounting.server_action_2675_jin_company_id_in_custom_currency_rate`<br>`x_custom_currency_rate.create_date` |  |

**Window actions (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Custom Currency Rate | `action_1309_custom_currency_rate` | Opens **Custom Currency Rate** records (tree,form). | `model x_custom_currency_rate` | `menu BugFix-Studio-Misc.menu_f6r3_purchase_configuration_setups_custom_currency_rate` (BugFix-Studio-Misc) |
| Rates | `act_custom_currency_rates` | Opens **Custom Currency Rate** records (tree,form), filtered to `[('x_studio_custom_currency_id', '=', active_id)]`. | `model x_custom_currency_rate`<br>`x_custom_currency_rate.x_studio_custom_currency_id` | `view BugFix-Accounting.ported_view_2927_odoo_studio_default_d6e426ae_1b5c_4bbd_b6cf_aaab9463d6cb` |
| Rates | `action_1310_rates` | Opens **Custom Currency Rate** records (tree,form), filtered to `[('x_studio_custom_currency_id', '=', active_id)]`. | `model x_custom_currency_rate`<br>`x_custom_currency_rate.x_studio_custom_currency_id` |  |

**Views (7):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_custom_currency_rate | `ported_default_form_view_fo_f5872bac_d1f7_4709_a9b1_364b0db1710c` | form | full form layout with 2 fields | Base form screen for Custom Currency Rate records: required Name title, an Archived ribbon when inactive and empty column groups that Studio extensions fill. | `x_custom_currency_rate.x_active`<br>`x_custom_currency_rate.x_name` | `view BugFix-Accounting.ported_view_2929_odoo_studio_default_98249da6_8d85_410b_8ba9_952472bdd50c` |
| Default list view for x_custom_currency_rate | `ported_default_list_view_fo_ca009934_0cbf_4bef_b9a5_cc7156daa1a9` | tree | full tree layout with 2 fields | Base list screen for Custom Currency Rate records showing Name with a drag handle for manual ordering by Sequence. | `x_custom_currency_rate.x_name`<br>`x_custom_currency_rate.x_studio_sequence` | `view BugFix-Accounting.ported_odoo_studio_default__3d5acdf8_7c5e_4d86_bee2_d071d148e8e7`<br>`view BugFix-Accounting.ported_view_2930_odoo_studio_default_3d5acdf8_7c5e_4d86_bee2_d071d148e8e7` |
| Default search view for x_custom_currency_rate | `ported_default_search_view__008371aa_6777_483b_a35b_55bb47e097eb` | search | full search layout with 1 fields | Search bar for Custom Currency Rate records: search by Name and an 'Archived' filter to show inactive records. | `x_custom_currency_rate.x_active`<br>`x_custom_currency_rate.x_name` |  |
| Default search view for x_custom_currency_rate | `ported_view_2926_default_search_view_008371aa_6777_483b_a35b_55bb47e097eb` | search | full search layout with 1 fields | Default search view for Custom Currency Rate records: search by name plus an Archived filter. | `x_custom_currency_rate.x_active`<br>`x_custom_currency_rate.x_name` |  |
| Odoo Studio: Default form view for x_custom_currency_rate customization | `ported_view_2929_odoo_studio_default_98249da6_8d85_410b_8ba9_952472bdd50c` | form | set invisible=1, required= on `//field[@name='x_name']`; inside `//group[@name='studio_group_e8c751_left']`: add field x_studio_start_date, field x_studio_end_date, field x_studio_rate, field x_studio_custom_currency_id | Custom Currency Rate form: hides the Name and adds Start Date, End Date, Rate and a hidden link to the Custom Currency. | `view BugFix-Accounting.ported_default_form_view_fo_f5872bac_d1f7_4709_a9b1_364b0db1710c`<br>`x_custom_currency_rate.x_studio_custom_currency_id`<br>`x_custom_currency_rate.x_studio_end_date`<br>`x_custom_currency_rate.x_studio_rate`<br>`x_custom_currency_rate.x_studio_start_date` |  |
| Odoo Studio: Default list view for x_custom_currency_rate customization | `ported_odoo_studio_default__3d5acdf8_7c5e_4d86_bee2_d071d148e8e7` | tree | set editable=bottom on `//tree[1]` | Studio customization of the Custom Currency Rate list: makes rows editable inline, with new lines added at the bottom. | `view BugFix-Accounting.ported_default_list_view_fo_ca009934_0cbf_4bef_b9a5_cc7156daa1a9` |  |
| Odoo Studio: Default list view for x_custom_currency_rate customization | `ported_view_2930_odoo_studio_default_3d5acdf8_7c5e_4d86_bee2_d071d148e8e7` | tree | set editable=bottom on `//tree[1]`; before `//field[@name='x_studio_sequence']`: add field x_studio_start_date, field x_studio_end_date, field x_studio_rate, field x_studio_company_id; set column_invisible=1 on `//field[@name='x_studio_sequence']`; set column_invisible=1 on `//field[@name='x_name']` | Makes the Custom Currency Rate list inline-editable with required Start Date, End Date and Rate (company hidden), hiding the sequence and name columns. | `view BugFix-Accounting.ported_default_list_view_fo_ca009934_0cbf_4bef_b9a5_cc7156daa1a9`<br>`x_custom_currency_rate.x_studio_company_id`<br>`x_custom_currency_rate.x_studio_end_date`<br>`x_custom_currency_rate.x_studio_rate`<br>`x_custom_currency_rate.x_studio_start_date` |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Custom Currency Rate group_system | `access_1331_custom_currency_rate_group_system` | Gives **Administration / Settings** read/write/create/delete access to Custom Currency Rate records. | `group base.group_system` (base)<br>`model x_custom_currency_rate` |  |
| Custom Currency Rate group_user | `access_1332_custom_currency_rate_group_user` | Gives **User types / Internal User** read access to Custom Currency Rate records. | `group base.group_user` (base)<br>`model x_custom_currency_rate` |  |
| x_custom_currency_rate user access | `access_x_custom_currency_rate_user` | Gives **User types / Internal User** read/write/create/delete access to Custom Currency Rate records. | `group base.group_user` (base)<br>`model x_custom_currency_rate` |  |

**Record rules (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| JIN - Multi-Company - Custom Currency Rate | `rule_f7_x_custom_currency_rate_jin_multi_company_custom_currency_rate` | For everyone (global rule): read/write/create/delete on Custom Currency Rate only where `['|', ('x_studio_company_id', 'in', company_ids), ('x_studio_company_id', '=', False)]`. | `model x_custom_currency_rate`<br>`x_custom_currency_rate.x_studio_company_id` |  |
| JIN - Multi-Company - Custom Currency Rate | `rule_563_jin_multi_company_custom_currency_rate` | For everyone (global rule): read/write/create/delete on Custom Currency Rate only where `['|', ('x_studio_company_id', 'in', company_ids), ('x_studio_company_id', '=', False)]`. | `model x_custom_currency_rate`<br>`x_custom_currency_rate.x_studio_company_id` |  |
