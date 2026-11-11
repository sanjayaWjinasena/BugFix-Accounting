# BugFix-Accounting — `custom_currency_rate`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `custom_currency_rate` — Custom Currency Rate

*Created by this repo.* Python: `models/custom_currency_rate.py`, `models/x_custom_currency_rate_gap.py`. Record name field: `name`.

Other repos that use this model: `server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Stock.action_imp_consignment_vendor_despatch` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_allocate_consignment_header_charges` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_consignment_custom_duty` (BugFix-Stock)<br>`server action BugFix-Stock.action_project_update_month_end_entries` (BugFix-Stock)<br>`server action BugFix-Stock.action_consignment_vendor_dispatch_bugfix_purchase` (BugFix-Stock)

**Summary:**

<!-- SUMMARY:model:custom_currency_rate -->
A dated exchange rate (start date, end date and rate) belonging to a Custom Currency, used for import costing. Rates are edited inline in a list opened from the custom currency's Rates button. An automation raises 'End Date must be Greater than Start Date' when the dates are reversed, and the company is stamped on creation and enforced by a multi-company record rule.
<!-- /SUMMARY -->

**Fields (25):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Calendar meeting linked to the next activity on the Custom Currency Rate record; standard mixin field. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Due date of the next scheduled activity on the Custom Currency Rate record; standard mixin field. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Warning or error decoration shown when an exception-type activity exists on the Custom Currency Rate record; standard mixin field. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Icon shown for an exception activity on the Custom Currency Rate record; standard mixin field. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Activities (to-dos, calls, meetings) scheduled on this Custom Currency Rate record; standard mail activity mixin field. | stored | `model mail.activity` (mail) | `custom_currency_rate.activity_summary`<br>`custom_currency_rate.activity_type_icon`<br>`custom_currency_rate.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity status of the Custom Currency Rate record (Overdue, Today, Planned), computed from its next activity deadline. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Summary text of the next scheduled activity on the Custom Currency Rate record; standard mixin field. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`custom_currency_rate.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Font Awesome icon of the next activity type, used in kanban/list activity widgets; standard mixin field. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`custom_currency_rate.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Type of the next scheduled activity on the Custom Currency Rate record, read from its activities; standard mixin field. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`custom_currency_rate.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | User responsible for the next scheduled activity on the Custom Currency Rate record; standard activity mixin field. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the Custom Currency Rate record was created; set automatically. Used as the trigger of the on-creation automation(s): jin company id in custom currency rate. | stored |  | `automation BugFix-Accounting.automation_jin_company_id_in_custom_currency_rate_2` |
| `create_uid` | Created by | many2one → `res.users` | User who created the Custom Currency Rate record; set automatically. | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name Odoo shows for the Custom Currency Rate record in dropdowns, lists and breadcrumbs; computed from its name field. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the Custom Currency Rate record, assigned automatically. | stored |  |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Due date of the current user's next activity on the Custom Currency Rate record; standard mixin field. | not stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time the Custom Currency Rate record was last modified; set automatically. | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last modified the Custom Currency Rate record; set automatically. | stored | `model res.users` (base) |  |
| `active` | Active | boolean | Active flag of the Custom Currency Rate record: unchecking it archives the record and hides it from default searches; defaults to checked via ir.default. | stored |  | `default BugFix-Accounting.default_custom_currency_rate_active`<br>`view BugFix-Accounting.view_custom_currency_rate_form`<br>`view BugFix-Accounting.view_custom_currency_rate_search`<br>`view BugFix-Accounting.view_custom_currency_rate_search_2` |
| `name` | Name | char | Name of the custom currency rate record. | stored |  | `view BugFix-Accounting.view_custom_currency_rate_form`<br>`view BugFix-Accounting.view_custom_currency_rate_list`<br>`view BugFix-Accounting.view_custom_currency_rate_search`<br>`view BugFix-Accounting.view_custom_currency_rate_search_2` |
| `accounting_company_id` | Company | many2one → `res.company` | Company the Custom Currency Rate record belongs to; enforced by a multi-company record rule and filled on creation by the 'JIN Company Id' automation. | stored | `model res.company` (base) | `record rule BugFix-Accounting.rule_jin_multi_company_custom_currency_rate`<br>`record rule BugFix-Accounting.rule_f7_custom_currency_rate_jin_multi_company_custom_currency_rate`<br>`server action BugFix-Accounting.action_custom_currency_rate_jin_company_id_in_custom_currency_rate`<br>`server action BugFix-Accounting.action_jin_company_id_in_custom_currency_rate`<br>`view BugFix-Accounting.view_default_list_view_for_custom_currency_rate_inherit_2` |
| `custom_currency_id` | Custom Currency Id | many2one → `custom_currency` | Custom currency this rate belongs to; the 'Rates' window action filters by it. | stored | `model custom_currency` | `view BugFix-Accounting.view_default_form_view_for_custom_currency_rate_inherit`<br>`window action BugFix-Accounting.act_custom_currency_rates`<br>`window action BugFix-Accounting.action_rates` |
| `end_date` | End Date | date | Last date the rate applies; the 'IMP - Validate From/To Dates' automation checks it against the start date. | stored |  | `automation BugFix-Accounting.base_automation_60_imp_validate_from_to_dates_in_custom_rates`<br>`server action BugFix-Accounting.action_custom_currency_rate_imp_validate_from_to_dates_in_custom_rates`<br>`server action BugFix-Accounting.action_imp_validate_from_to_dates_in_custom_rates`<br>`view BugFix-Accounting.view_default_form_view_for_custom_currency_rate_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_custom_currency_rate_inherit_2` |
| `rate` | Rate | float | Exchange rate value for the period. | stored |  | `view BugFix-Accounting.view_default_form_view_for_custom_currency_rate_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_custom_currency_rate_inherit_2` |
| `sequence` | Sequence | integer | Sort order of Custom Currency Rate records in the list view (drag-and-drop handle); default value set by ir.default. | stored |  | `default BugFix-Accounting.default_custom_currency_rate_sequence`<br>`view BugFix-Accounting.view_custom_currency_rate_list` |
| `start_date` | Start Date | date | First date the rate applies; validated against the end date by the 'IMP - Validate From/To Dates' automation. | stored |  | `automation BugFix-Accounting.base_automation_60_imp_validate_from_to_dates_in_custom_rates`<br>`server action BugFix-Accounting.action_custom_currency_rate_imp_validate_from_to_dates_in_custom_rates`<br>`server action BugFix-Accounting.action_imp_validate_from_to_dates_in_custom_rates`<br>`view BugFix-Accounting.view_default_form_view_for_custom_currency_rate_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_custom_currency_rate_inherit_2` |

**Server actions (4):**

- **Execute Code** (`action_imp_validate_from_to_dates_in_custom_rates`, type `code`)
  - Function: Run by the custom-rate date validation automation: raises 'End Date must be Greater than Start Date' if End Date is before Start Date.
  - Depends on: `model custom_currency_rate`, `custom_currency_rate.end_date`, `custom_currency_rate.start_date`
  - Used by: `automation BugFix-Accounting.base_automation_60_imp_validate_from_to_dates_in_custom_rates`
  <details><summary>code (3 lines)</summary>

```python
if record.end_date < record.start_date:
    raise UserError("End Date must be Greater than Start Date.")
```
  </details>
- **Execute Code** (`action_jin_company_id_in_custom_currency_rate`, type `code`)
  - Function: Run by the JIN automation: sets the Custom Currency Rate's Company to the user's active company.
  - Depends on: `model res.company` (base), `model custom_currency_rate`, `custom_currency_rate.accounting_company_id`
  - Used by: `automation BugFix-Accounting.automation_jin_company_id_in_custom_currency_rate_2`
  <details><summary>code (5 lines)</summary>

```python
company_id = env.context.get("allowed_company_ids", [env.user.company_id.id])[0]
company = env["res.company"].browse(company_id)

record["accounting_company_id"] = company.id
```
  </details>
- **IMP - Validate From To Dates in Custom Rates** (`action_custom_currency_rate_imp_validate_from_to_dates_in_custom_rates`, type `code`)
  - Function: Raises an error 'End Date must be Greater than Start Date' when a custom currency rate's End Date is before its Start Date.
  - Depends on: `model custom_currency_rate`, `custom_currency_rate.end_date`, `custom_currency_rate.start_date`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (2 lines)</summary>

```python
if record.end_date < record.start_date:
    raise UserError("End Date must be Greater than Start Date.")
```
  </details>
- **JIN - Company Id in Custom Currency Rate** (`action_custom_currency_rate_jin_company_id_in_custom_currency_rate`, type `code`)
  - Function: Sets the Custom Currency Rate record's Company field to the user's currently active company (first allowed company in context).
  - Depends on: `model res.company` (base), `model custom_currency_rate`, `custom_currency_rate.accounting_company_id`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (4 lines)</summary>

```python
company_id = env.context.get("allowed_company_ids", [env.user.company_id.id])[0]
company = env["res.company"].browse(company_id)

record["accounting_company_id"] = company.id
```
  </details>
**Automations (4):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| IMP - Validate From To Dates in Custom Rates | `automation_60_imp_validate_from_to_dates_in_custom_rates` |  | When a record is created or updated on Custom Currency Rate, runs nothing (no action linked). | `model custom_currency_rate` |  |
| IMP - Validate From To Dates in Custom Rates | `base_automation_60_imp_validate_from_to_dates_in_custom_rates` |  | When a record is created or updated on Custom Currency Rate, runs _Execute Code_. | `model custom_currency_rate`<br>`server action BugFix-Accounting.action_imp_validate_from_to_dates_in_custom_rates`<br>`custom_currency_rate.end_date`<br>`custom_currency_rate.start_date` |  |
| JIN - Company Id in Custom Currency Rate | `automation_jin_company_id_in_custom_currency_rate` | archived | When a record is created or updated on Custom Currency Rate, runs nothing (no action linked). **Archived — does not run.** | `model custom_currency_rate` |  |
| JIN - Company Id in Custom Currency Rate | `automation_jin_company_id_in_custom_currency_rate_2` |  | When a record is created or updated on Custom Currency Rate, runs _Execute Code_. | `model custom_currency_rate`<br>`server action BugFix-Accounting.action_jin_company_id_in_custom_currency_rate`<br>`custom_currency_rate.create_date` |  |

**Window actions (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Custom Currency Rate | `action_custom_currency_rate` | Opens **Custom Currency Rate** records (tree,form). | `model custom_currency_rate` | `menu BugFix-Studio-Misc.menu_purchase_configuration_setups_custom_currency_rate` (BugFix-Studio-Misc) |
| Rates | `act_custom_currency_rates` | Opens **Custom Currency Rate** records (tree,form), filtered to `[('custom_currency_id', '=', active_id)]`. | `model custom_currency_rate`<br>`custom_currency_rate.custom_currency_id` | `view BugFix-Accounting.view_default_form_view_for_custom_currency_inherit` |
| Rates | `action_rates` | Opens **Custom Currency Rate** records (tree,form), filtered to `[('custom_currency_id', '=', active_id)]`. | `model custom_currency_rate`<br>`custom_currency_rate.custom_currency_id` |  |

**Views (7):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for custom_currency_rate | `view_custom_currency_rate_form` | form | full form layout with 2 fields | Base form screen for Custom Currency Rate records: required Name title, an Archived ribbon when inactive and empty column groups that Studio extensions fill. | `custom_currency_rate.active`<br>`custom_currency_rate.name` | `view BugFix-Accounting.view_default_form_view_for_custom_currency_rate_inherit` |
| Default list view for custom_currency_rate | `view_custom_currency_rate_list` | tree | full tree layout with 2 fields | Base list screen for Custom Currency Rate records showing Name with a drag handle for manual ordering by Sequence. | `custom_currency_rate.name`<br>`custom_currency_rate.sequence` | `view BugFix-Accounting.view_default_list_view_for_custom_currency_rate_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_custom_currency_rate_inherit_2` |
| Default search view for custom_currency_rate | `view_custom_currency_rate_search` | search | full search layout with 1 fields | Search bar for Custom Currency Rate records: search by Name and an 'Archived' filter to show inactive records. | `custom_currency_rate.active`<br>`custom_currency_rate.name` |  |
| Default search view for custom_currency_rate | `view_custom_currency_rate_search_2` | search | full search layout with 1 fields | Default search view for Custom Currency Rate records: search by name plus an Archived filter. | `custom_currency_rate.active`<br>`custom_currency_rate.name` |  |
| Odoo Studio: Default form view for custom_currency_rate customization | `view_default_form_view_for_custom_currency_rate_inherit` | form | set invisible=1, required= on `//field[@name='name']`; inside `//group[@name='studio_group_e8c751_left']`: add field start_date, field end_date, field rate, field custom_currency_id | Custom Currency Rate form: hides the Name and adds Start Date, End Date, Rate and a hidden link to the Custom Currency. | `view BugFix-Accounting.view_custom_currency_rate_form`<br>`custom_currency_rate.custom_currency_id`<br>`custom_currency_rate.end_date`<br>`custom_currency_rate.rate`<br>`custom_currency_rate.start_date` |  |
| Odoo Studio: Default list view for custom_currency_rate customization | `view_default_list_view_for_custom_currency_rate_inherit` | tree | set editable=bottom on `//tree[1]` | Studio customization of the Custom Currency Rate list: makes rows editable inline, with new lines added at the bottom. | `view BugFix-Accounting.view_custom_currency_rate_list` |  |
| Odoo Studio: Default list view for custom_currency_rate customization | `view_default_list_view_for_custom_currency_rate_inherit_2` | tree | set editable=bottom on `//tree[1]`; before `//field[@name='sequence']`: add field start_date, field end_date, field rate, field accounting_company_id; set column_invisible=1 on `//field[@name='sequence']`; set column_invisible=1 on `//field[@name='name']` | Makes the Custom Currency Rate list inline-editable with required Start Date, End Date and Rate (company hidden), hiding the sequence and name columns. | `view BugFix-Accounting.view_custom_currency_rate_list`<br>`custom_currency_rate.accounting_company_id`<br>`custom_currency_rate.end_date`<br>`custom_currency_rate.rate`<br>`custom_currency_rate.start_date` |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Custom Currency Rate group_system | `access_custom_currency_rate_group_system` | Gives **Administration / Settings** read/write/create/delete access to Custom Currency Rate records. | `group base.group_system` (base)<br>`model custom_currency_rate` |  |
| Custom Currency Rate group_user | `access_custom_currency_rate_group_user` | Gives **User types / Internal User** read access to Custom Currency Rate records. | `group base.group_user` (base)<br>`model custom_currency_rate` |  |
| custom_currency_rate user access | `access_custom_currency_rate_user` | Gives **User types / Internal User** read/write/create/delete access to Custom Currency Rate records. | `group base.group_user` (base)<br>`model custom_currency_rate` |  |

**Record rules (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| JIN - Multi-Company - Custom Currency Rate | `rule_f7_custom_currency_rate_jin_multi_company_custom_currency_rate` | For everyone (global rule): read/write/create/delete on Custom Currency Rate only where `['|', ('accounting_company_id', 'in', company_ids), ('accounting_company_id', '=', False)]`. | `model custom_currency_rate`<br>`custom_currency_rate.accounting_company_id` |  |
| JIN - Multi-Company - Custom Currency Rate | `rule_jin_multi_company_custom_currency_rate` | For everyone (global rule): read/write/create/delete on Custom Currency Rate only where `['|', ('accounting_company_id', 'in', company_ids), ('accounting_company_id', '=', False)]`. | `model custom_currency_rate`<br>`custom_currency_rate.accounting_company_id` |  |
