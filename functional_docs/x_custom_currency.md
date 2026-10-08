# BugFix-Accounting — `x_custom_currency`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_custom_currency` — Custom Currency

*Created by this repo.* Python: `models/x_custom_currency.py`, `models/x_custom_currency_gap.py`. Record name field: `x_name`.

Other repos that use this model: `server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Stock.server_action_1305_imp_consignment_vendor_despatch` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_1318_imp_allocate_consignment_header_charges` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_1321_imp_consignment_custom_duty` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_2118_project_update_month_end_entries` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_3647_consignment_vendor_dispatch_bugfix_purchase` (BugFix-Stock)

**Summary:**

<!-- SUMMARY:model:x_custom_currency -->
A custom (import) currency master used in the imports workflow, holding the currency name, ISO code, unit, symbol, current rate and date, linked to a standard Odoo currency. Choosing the Odoo currency triggers the 'IMP - Pass Currency Information' automation, which copies its symbol into ISO Currency Code and its name into Name. A Rates smart button opens the dated rates of the currency, and the company is stamped on creation and enforced by a multi-company record rule. The model is read by consignment server actions in BugFix-Purchase and BugFix-Stock.
<!-- /SUMMARY -->

**Fields (30):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Calendar meeting linked to the next activity on the Custom Currency record; standard mixin field. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Due date of the next scheduled activity on the Custom Currency record; standard mixin field. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Warning or error decoration shown when an exception-type activity exists on the Custom Currency record; standard mixin field. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Icon shown for an exception activity on the Custom Currency record; standard mixin field. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Activities (to-dos, calls, meetings) scheduled on this Custom Currency record; standard mail activity mixin field. | stored | `model mail.activity` (mail) | `x_custom_currency.activity_summary`<br>`x_custom_currency.activity_type_icon`<br>`x_custom_currency.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity status of the Custom Currency record (Overdue, Today, Planned), computed from its next activity deadline. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Summary text of the next scheduled activity on the Custom Currency record; standard mixin field. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_custom_currency.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Font Awesome icon of the next activity type, used in kanban/list activity widgets; standard mixin field. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_custom_currency.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Type of the next scheduled activity on the Custom Currency record, read from its activities; standard mixin field. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_custom_currency.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | User responsible for the next scheduled activity on the Custom Currency record; standard activity mixin field. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the Custom Currency record was created; set automatically. Used as the trigger of the on-creation automation(s): jin company id in custom currency. | stored |  | `automation BugFix-Accounting.base_automation_310_jin_company_id_in_custom_currency` |
| `create_uid` | Created by | many2one → `res.users` | User who created the Custom Currency record; set automatically. | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name Odoo shows for the Custom Currency record in dropdowns, lists and breadcrumbs; computed from its name field. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the Custom Currency record, assigned automatically. | stored |  |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Due date of the current user's next activity on the Custom Currency record; standard mixin field. | not stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time the Custom Currency record was last modified; set automatically. | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last modified the Custom Currency record; set automatically. | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Active flag of the Custom Currency record: unchecking it archives the record and hides it from default searches; defaults to checked via ir.default. | stored |  | `default BugFix-Accounting.default_155_x_custom_currency_x_active`<br>`view BugFix-Accounting.ported_default_form_view_fo_8a4b6def_7c88_4ab2_9f17_96bd901a9f4e`<br>`view BugFix-Accounting.ported_default_search_view__a298038c_e955_424c_892e_bd176971bcc1`<br>`view BugFix-Accounting.ported_view_2923_default_search_view_a298038c_e955_424c_892e_bd176971bcc1` |
| `x_name` | Name | char | Name of the custom (import) currency; passed on by the 'IMP - Pass Currency Information' action. | stored |  | `server action BugFix-Accounting.sa_f5_x_custom_currency_imp_pass_currency_information_to_custom_currency`<br>`server action BugFix-Accounting.server_action_1312_imp_pass_currency_information_to_custom_currency`<br>`view BugFix-Accounting.ported_default_form_view_fo_8a4b6def_7c88_4ab2_9f17_96bd901a9f4e`<br>`view BugFix-Accounting.ported_default_list_view_fo_c10f81e8_0461_45dc_bca4_c7824d05528e`<br>`view BugFix-Accounting.ported_default_search_view__a298038c_e955_424c_892e_bd176971bcc1`<details><summary>+1 more</summary>`view BugFix-Accounting.ported_view_2923_default_search_view_a298038c_e955_424c_892e_bd176971bcc1`</details> |
| `x_studio_active` | Active | boolean | Second 'Active' checkbox shown on the custom currency forms; does not archive the record (that is `x_active`). | stored |  | `view BugFix-Accounting.ported_view_2927_odoo_studio_default_d6e426ae_1b5c_4bbd_b6cf_aaab9463d6cb`<br>`view BugFix-Accounting.ported_view_2931_odoo_studio_default_527d6591_4b52_40f4_a210_0cfd294b2cf0` |
| `x_studio_company_id` | Company | many2one → `res.company` | Company the Custom Currency record belongs to; enforced by a multi-company record rule and filled on creation by the 'JIN Company Id' automation. | stored | `model res.company` (base) | `record rule BugFix-Accounting.rule_562_jin_multi_company_custom_currency`<br>`record rule BugFix-Accounting.rule_f7_x_custom_currency_jin_multi_company_custom_currency`<br>`server action BugFix-Accounting.sa_f5_x_custom_currency_jin_company_id_in_custom_currency`<br>`server action BugFix-Accounting.server_action_2674_jin_company_id_in_custom_currency`<br>`view BugFix-Accounting.ported_view_2927_odoo_studio_default_d6e426ae_1b5c_4bbd_b6cf_aaab9463d6cb` |
| `x_studio_currency_id` | Currency | many2one → `res.currency` | Odoo currency this custom currency maps to (default from ir.default); setting it triggers 'IMP - Pass Currency Information' to copy its details. | stored | `model res.currency` (base) | `automation BugFix-Accounting.base_automation_61_imp_pass_currency_information_to_custom_currency`<br>`default BugFix-Accounting.default_225_x_custom_currency_x_studio_currency_id`<br>`default BugFix-Accounting.default_426_x_custom_currency_x_studio_currency_id`<br>`server action BugFix-Accounting.sa_f5_x_custom_currency_imp_pass_currency_information_to_custom_currency`<br>`server action BugFix-Accounting.server_action_1312_imp_pass_currency_information_to_custom_currency`<details><summary>+2 more</summary>`view BugFix-Accounting.ported_view_2927_odoo_studio_default_d6e426ae_1b5c_4bbd_b6cf_aaab9463d6cb`<br>`view BugFix-Accounting.ported_view_2931_odoo_studio_default_527d6591_4b52_40f4_a210_0cfd294b2cf0`</details> |
| `x_studio_currency_unit` | Currency Unit | char | Currency unit name, entered on the form. | stored |  | `view BugFix-Accounting.ported_view_2927_odoo_studio_default_d6e426ae_1b5c_4bbd_b6cf_aaab9463d6cb` |
| `x_studio_current_rate` | Current Rate | float | Current exchange rate of the custom currency, shown on the forms. | stored |  | `view BugFix-Accounting.ported_view_2927_odoo_studio_default_d6e426ae_1b5c_4bbd_b6cf_aaab9463d6cb`<br>`view BugFix-Accounting.ported_view_2931_odoo_studio_default_527d6591_4b52_40f4_a210_0cfd294b2cf0` |
| `x_studio_date` | Date | date | Date of the current rate. | stored |  | `view BugFix-Accounting.ported_view_2927_odoo_studio_default_d6e426ae_1b5c_4bbd_b6cf_aaab9463d6cb`<br>`view BugFix-Accounting.ported_view_2931_odoo_studio_default_527d6591_4b52_40f4_a210_0cfd294b2cf0` |
| `x_studio_iso_currency_code` | ISO Currency Code | char | ISO currency code, filled by the 'IMP - Pass Currency Information' action from the linked currency. | stored; required |  | `server action BugFix-Accounting.sa_f5_x_custom_currency_imp_pass_currency_information_to_custom_currency`<br>`server action BugFix-Accounting.server_action_1312_imp_pass_currency_information_to_custom_currency`<br>`view BugFix-Accounting.ported_view_2927_odoo_studio_default_d6e426ae_1b5c_4bbd_b6cf_aaab9463d6cb`<br>`view BugFix-Accounting.ported_view_2931_odoo_studio_default_527d6591_4b52_40f4_a210_0cfd294b2cf0` |
| `x_studio_name` | Name | char | Currency name shown on the custom currency forms. | stored |  | `view BugFix-Accounting.ported_view_2927_odoo_studio_default_d6e426ae_1b5c_4bbd_b6cf_aaab9463d6cb`<br>`view BugFix-Accounting.ported_view_2931_odoo_studio_default_527d6591_4b52_40f4_a210_0cfd294b2cf0` |
| `x_studio_sequence` | Sequence | integer | Sort order of Custom Currency records in the list view (drag-and-drop handle); default value set by ir.default. | stored |  | `default BugFix-Accounting.default_156_x_custom_currency_x_studio_sequence`<br>`view BugFix-Accounting.ported_default_list_view_fo_c10f81e8_0461_45dc_bca4_c7824d05528e` |
| `x_studio_symbol` | Symbol | char | Currency symbol shown on the custom currency forms. | stored |  | `view BugFix-Accounting.ported_view_2927_odoo_studio_default_d6e426ae_1b5c_4bbd_b6cf_aaab9463d6cb`<br>`view BugFix-Accounting.ported_view_2931_odoo_studio_default_527d6591_4b52_40f4_a210_0cfd294b2cf0` |
| `x_x_studio_custom_currency_id__x_custom_currency_rate_count` | Custom Currency Id count | integer | Number of rate records for this currency, shown on the smart button; plain integer, not computed in this repo. | not stored |  | `view BugFix-Accounting.ported_view_2927_odoo_studio_default_d6e426ae_1b5c_4bbd_b6cf_aaab9463d6cb` |

**Server actions (4):**

- **Execute Code** (`server_action_1312_imp_pass_currency_information_to_custom_currency`, type `code`)
  - Function: Run by the 'IMP - Pass Currency Information' automation: copies the selected currency's symbol into ISO Currency Code and its name into Name on the Custom Currency.
  - Depends on: `model res.currency` (base), `model x_custom_currency`, `x_custom_currency.x_name`, `x_custom_currency.x_studio_currency_id`, `x_custom_currency.x_studio_iso_currency_code`
  - Used by: `automation BugFix-Accounting.base_automation_61_imp_pass_currency_information_to_custom_currency`
  <details><summary>code (6 lines)</summary>

```python

if record.x_studio_currency_id.id:
  currency = env['res.currency'].search([('id', '=', record.x_studio_currency_id.id)], limit=1)
  if currency:
    record['x_studio_iso_currency_code'] = currency.symbol
    record['x_name'] = currency.name
```
  </details>
- **Execute Code** (`server_action_2674_jin_company_id_in_custom_currency`, type `code`)
  - Function: Run by the JIN automation: sets the Custom Currency's Company to the user's active company.
  - Depends on: `model res.company` (base), `model x_custom_currency`, `x_custom_currency.x_studio_company_id`
  - Used by: `automation BugFix-Accounting.base_automation_310_jin_company_id_in_custom_currency`
  <details><summary>code (5 lines)</summary>

```python

company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
company = env['res.company'].browse(company_id)

record['x_studio_company_id'] = company.id
```
  </details>
- **IMP - Pass Currency Information to Custom Currency** (`sa_f5_x_custom_currency_imp_pass_currency_information_to_custom_currency`, type `code`)
  - Function: Copies the selected currency's symbol into ISO Currency Code and its name into Name on the Custom Currency record.
  - Depends on: `model res.currency` (base), `model x_custom_currency`, `x_custom_currency.x_name`, `x_custom_currency.x_studio_currency_id`, `x_custom_currency.x_studio_iso_currency_code`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (5 lines)</summary>

```python
if record.x_studio_currency_id.id:
  currency = env['res.currency'].search([('id', '=', record.x_studio_currency_id.id)], limit=1)
  if currency:
    record['x_studio_iso_currency_code'] = currency.symbol
    record['x_name'] = currency.name
```
  </details>
- **JIN - Company Id in Custom Currency** (`sa_f5_x_custom_currency_jin_company_id_in_custom_currency`, type `code`)
  - Function: Sets the Custom Currency record's Company field to the user's currently active company (first allowed company in context).
  - Depends on: `model res.company` (base), `model x_custom_currency`, `x_custom_currency.x_studio_company_id`
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
| IMP - Pass Currency Information to Custom Currency | `automation_61_imp_pass_currency_information_to_custom_currency` |  | When a watched field changes in the form on Custom Currency, runs nothing (no action linked). | `model x_custom_currency` |  |
| IMP - Pass Currency Information to Custom Currency | `base_automation_61_imp_pass_currency_information_to_custom_currency` |  | When a watched field changes in the form on Custom Currency, runs _Execute Code_. | `model x_custom_currency`<br>`server action BugFix-Accounting.server_action_1312_imp_pass_currency_information_to_custom_currency`<br>`x_custom_currency.x_studio_currency_id` |  |
| JIN - Company Id in Custom Currency | `automation_310_jin_company_id_in_custom_currency` |  | When a record is created or updated on Custom Currency, runs nothing (no action linked). | `model x_custom_currency` |  |
| JIN - Company Id in Custom Currency | `base_automation_310_jin_company_id_in_custom_currency` |  | When a record is created or updated on Custom Currency, runs _Execute Code_. | `model x_custom_currency`<br>`server action BugFix-Accounting.server_action_2674_jin_company_id_in_custom_currency`<br>`x_custom_currency.create_date` |  |

**Window actions (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Custom Currency | `action_1308_custom_currency` | Opens **Custom Currency** records (tree,form). | `model x_custom_currency` | `menu BugFix-Studio-Misc.menu_f6r3_purchase_configuration_setups_custom_currency_rates` (BugFix-Studio-Misc)<br>`menu BugFix-Studio-Misc.menu_f6r3_purchase_imports_01_imports_configuration_custom_currency_ra` (BugFix-Studio-Misc) |
| Custom Currency Rates | `action_2063_custom_currency_rates` | Opens **Custom Currency** records (tree,form). | `model x_custom_currency` | `menu BugFix-Studio-Misc.menu_f6r3_purchase_configuration_imports_configurations_custom_currenc` (BugFix-Studio-Misc) |

**Views (6):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_custom_currency | `ported_default_form_view_fo_8a4b6def_7c88_4ab2_9f17_96bd901a9f4e` | form | full form layout with 2 fields | Base form screen for Custom Currency records: required Name title, an Archived ribbon when inactive and empty column groups that Studio extensions fill. | `x_custom_currency.x_active`<br>`x_custom_currency.x_name` | `view BugFix-Accounting.ported_view_2927_odoo_studio_default_d6e426ae_1b5c_4bbd_b6cf_aaab9463d6cb` |
| Default list view for x_custom_currency | `ported_default_list_view_fo_c10f81e8_0461_45dc_bca4_c7824d05528e` | tree | full tree layout with 2 fields | Base list screen for Custom Currency records showing Name with a drag handle for manual ordering by Sequence. | `x_custom_currency.x_name`<br>`x_custom_currency.x_studio_sequence` | `view BugFix-Accounting.ported_view_2931_odoo_studio_default_527d6591_4b52_40f4_a210_0cfd294b2cf0` |
| Default search view for x_custom_currency | `ported_default_search_view__a298038c_e955_424c_892e_bd176971bcc1` | search | full search layout with 1 fields | Search bar for Custom Currency records: search by Name and an 'Archived' filter to show inactive records. | `x_custom_currency.x_active`<br>`x_custom_currency.x_name` |  |
| Default search view for x_custom_currency | `ported_view_2923_default_search_view_a298038c_e955_424c_892e_bd176971bcc1` | search | full search layout with 1 fields | Default search view for Custom Currency records: search by name plus an Archived filter. | `x_custom_currency.x_active`<br>`x_custom_currency.x_name` |  |
| Odoo Studio: Default form view for x_custom_currency customization | `ported_view_2927_odoo_studio_default_d6e426ae_1b5c_4bbd_b6cf_aaab9463d6cb` | form | before `//widget[@name='web_ribbon']`: add div; set invisible=1, required= on `//field[@name='x_name']`; inside `//group[@name='studio_group_6e4bb6_left']`: add field x_studio_currency_id, field x_studio_name, field x_studio_iso_currency_code; inside `//group[@name='studio_group_6e4bb6_right']`: add field x_studio_currency_unit, field x_studio_symbol, field x_studio_current_rate, field x_studio_date, field x_studio_active, field x_studio_company_id | Custom Currency form: adds a Rates smart button (when active), hides the Name, and adds Currency, Name, ISO code, unit, symbol, date, active flag, company and a hidden current rate. | `view BugFix-Accounting.ported_default_form_view_fo_8a4b6def_7c88_4ab2_9f17_96bd901a9f4e`<br>`window action BugFix-Accounting.act_custom_currency_rates`<br>`x_custom_currency.x_studio_active`<br>`x_custom_currency.x_studio_company_id`<br>`x_custom_currency.x_studio_currency_id`<details><summary>+7 more</summary>`x_custom_currency.x_studio_currency_unit`<br>`x_custom_currency.x_studio_current_rate`<br>`x_custom_currency.x_studio_date`<br>`x_custom_currency.x_studio_iso_currency_code`<br>`x_custom_currency.x_studio_name`<br>`x_custom_currency.x_studio_symbol`<br>`x_custom_currency.x_x_studio_custom_currency_id__x_custom_currency_rate_count`</details> |  |
| Odoo Studio: Default list view for x_custom_currency customization | `ported_view_2931_odoo_studio_default_527d6591_4b52_40f4_a210_0cfd294b2cf0` | tree | before `//field[@name='x_studio_sequence']`: add field x_studio_currency_id, field x_studio_name, field x_studio_iso_currency_code, field x_studio_symbol, field x_studio_date, field x_studio_current_rate, field x_studio_active, xpath; set column_invisible=1 on `//field[@name='x_studio_sequence']`; set column_invisible=1 on `//field[@name='x_name']` | Custom Currency list: shows Currency, Name, ISO code, Symbol and an Active toggle (date and current rate hidden), hiding the sequence and name columns. | `view BugFix-Accounting.ported_default_list_view_fo_c10f81e8_0461_45dc_bca4_c7824d05528e`<br>`x_custom_currency.x_studio_active`<br>`x_custom_currency.x_studio_currency_id`<br>`x_custom_currency.x_studio_current_rate`<br>`x_custom_currency.x_studio_date`<details><summary>+3 more</summary>`x_custom_currency.x_studio_iso_currency_code`<br>`x_custom_currency.x_studio_name`<br>`x_custom_currency.x_studio_symbol`</details> |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Custom Currency group_system | `access_1329_custom_currency_group_system` | Gives **Administration / Settings** read/write/create/delete access to Custom Currency records. | `group base.group_system` (base)<br>`model x_custom_currency` |  |
| Custom Currency group_user | `access_1330_custom_currency_group_user` | Gives **User types / Internal User** read access to Custom Currency records. | `group base.group_user` (base)<br>`model x_custom_currency` |  |
| x_custom_currency user access | `access_x_custom_currency_user` | Gives **User types / Internal User** read/write/create/delete access to Custom Currency records. | `group base.group_user` (base)<br>`model x_custom_currency` |  |

**Record rules (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| JIN - Multi-Company - Custom Currency | `rule_f7_x_custom_currency_jin_multi_company_custom_currency` | For everyone (global rule): read/write/create/delete on Custom Currency only where `['|', ('x_studio_company_id', 'in', company_ids), ('x_studio_company_id', '=', False)]`. | `model x_custom_currency`<br>`x_custom_currency.x_studio_company_id` |  |
| JIN - Multi-Company - Custom Currency | `rule_562_jin_multi_company_custom_currency` | For everyone (global rule): read/write/create/delete on Custom Currency only where `['|', ('x_studio_company_id', 'in', company_ids), ('x_studio_company_id', '=', False)]`. | `model x_custom_currency`<br>`x_custom_currency.x_studio_company_id` |  |
