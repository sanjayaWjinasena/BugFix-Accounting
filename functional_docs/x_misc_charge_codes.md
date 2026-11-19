# BugFix-Accounting — `x_misc_charge_codes`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_misc_charge_codes` — Misc Charge Codes

*Extends a model created by `BugFix-Stock`.* Python: `models/x_misc_charge_codes.py`, `models/x_misc_charge_codes_gap.py`. Record name field: `x_name`.

Other repos that use this model: `access right BugFix-Purchase.access_x_misc_charge_codes_user` (BugFix-Purchase)<br>`access right BugFix-Stock.access_x_misc_charge_codes_user` (BugFix-Stock)<br>`server action BugFix-Purchase.sa_f5_x_tariff_date_imp_create_charges_for_tariff_dates` (BugFix-Purchase)<br>`server action BugFix-Purchase.sa_f5_x_trf_charges_imp_create_charges_in_misc_charge_codes` (BugFix-Purchase)<br>`server action BugFix-Purchase.sa_f5_x_trf_taxes_imp_create_taxes_in_misc_charge_codes` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_1169_imp_create_charges_for_tariff_dates` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_1173_imp_create_charges_in_misc_charge_codes` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_1174_imp_create_duties_in_misc_charge_codes` (BugFix-Purchase)<details><summary>+21 more</summary>`server action BugFix-Purchase.server_action_1175_imp_create_taxes_in_misc_charge_codes` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_1179_imp_copy_charges_to_structure_details` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_1296_imp_create_duties_in_misc_charge_codes` (BugFix-Purchase)<br>`server action BugFix-Sales.server_action_1207_imp_copy_charges_to_delivery_terms` (BugFix-Sales)<br>`server action BugFix-Stock.server_action_1318_imp_allocate_consignment_header_charges` (BugFix-Stock)<br>`x_consignment_line.x_studio_many2many_field_ZvmKu` (BugFix-Stock)<br>`x_consignment_line.x_studio_tot_charge_cd_ids` (BugFix-Stock)<br>`x_consignment_line.x_studio_tot_charge_ex_cd_ids` (BugFix-Stock)<br>`x_consignment_line.x_studio_tot_charge_ex_ids` (BugFix-Stock)<br>`x_consignment_line.x_studio_tot_charge_ids` (BugFix-Stock)<br>`x_consignment_line.x_studio_tot_duty_cd_ids` (BugFix-Stock)<br>`x_consignment_line.x_studio_tot_duty_ex_cd_ids` (BugFix-Stock)<br>`x_consignment_line.x_studio_tot_duty_ex_ids` (BugFix-Stock)<br>`x_consignment_line.x_studio_tot_duty_ids` (BugFix-Stock)<br>`x_consignment_line.x_studio_tot_tax_cd_ids` (BugFix-Stock)<br>`x_consignment_line.x_studio_tot_tax_ex_cd_ids` (BugFix-Stock)<br>`x_consignment_line.x_studio_tot_tax_ex_ids` (BugFix-Stock)<br>`x_consignment_line.x_studio_tot_tax_ids` (BugFix-Stock)<br>`x_structure_details.x_studio_misc_charge_line_id` (BugFix-Purchase)<br>`x_tariff_rates.x_studio_misc_charge_line_id` (BugFix-Purchase)<br>`x_test02.x_studio_many2many_field_JKvVx` (BugFix-Studio-Misc)</details>

**Summary:**

<!-- SUMMARY:model:x_misc_charge_codes -->
Miscellaneous import charge code master (created by BugFix-Stock) that this repo also declares in Python, with description, charge group (Charges, Duty or Taxes), cost load type, debit and credit account types and accounts, company and a system-entry flag. This repo adds a read-only form, an inline-editable list sorted by charge group, a 'JIN - Company Id' automation that stamps the active company, an 'IMP - Validate Debit Acc Type' action that clears the Debit Account when the type is Item, and a multi-company record rule.
<!-- /SUMMARY -->

**Fields (41):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard computed field: calendar meeting linked to the next activity on this Misc Charge Codes record, if any. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Due date of the next scheduled activity on the Misc Charge Codes record; standard mixin field. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard computed flag (Alert or Error) showing that an activity on this Misc Charge Codes record is in an exception state. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard computed icon shown when an activity on this Misc Charge Codes record is in an exception state. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Activities (to-dos, calls, meetings) scheduled on this Misc Charge Codes record; standard mail activity mixin field. | stored | `model mail.activity` (mail) | `view BugFix-Accounting.ported_view_2682_default_form_view_fo_79d2000d_8484_4cdb_befd_2dbcf0fb6a69`<br>`x_misc_charge_codes.activity_summary`<br>`x_misc_charge_codes.activity_type_icon`<br>`x_misc_charge_codes.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity status of the Misc Charge Codes record (Overdue, Today, Planned), computed from its next activity deadline. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Summary text of the next scheduled activity on the Misc Charge Codes record; standard mixin field. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_misc_charge_codes.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Font Awesome icon of the next activity type, used in kanban/list activity widgets; standard mixin field. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_misc_charge_codes.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Type of the next scheduled activity on the Misc Charge Codes record, read from its activities; standard mixin field. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_misc_charge_codes.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | User responsible for the next scheduled activity on the Misc Charge Codes record; standard activity mixin field. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the Misc Charge Codes record was created; set automatically. Used as the trigger of the on-creation automation(s): jin company id in misc charge codes. | stored |  | `automation BugFix-Accounting.base_automation_318_jin_company_id_in_misc_charge_codes` |
| `create_uid` | Created by | many2one → `res.users` | User who created the Misc Charge Codes record; set automatically. | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name Odoo shows for the Misc Charge Codes record in dropdowns, lists and breadcrumbs; computed from its name field. | not stored |  |  |
| `has_message` | Has Message | boolean | Standard computed flag: true when this Misc Charge Codes record has at least one chatter message. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the Misc Charge Codes record, assigned automatically. | stored |  |  |
| `message_attachment_count` | Attachment Count | integer | Standard computed count of attachments linked to this Misc Charge Codes record. | not stored |  |  |
| `message_follower_ids` | Followers | one2many → `mail.followers` | Followers (partners) subscribed to notifications on this Misc Charge Codes record, from the standard mail thread mixin. Displayed in the form view chatter. | stored | `model mail.followers` (mail) | `view BugFix-Accounting.ported_view_2682_default_form_view_fo_79d2000d_8484_4cdb_befd_2dbcf0fb6a69` |
| `message_has_error` | Message Delivery error | boolean | Standard computed flag: true when a message on this Misc Charge Codes record failed to be delivered. | not stored |  |  |
| `message_has_error_counter` | Number of errors | integer | Standard computed count of messages on this Misc Charge Codes record with delivery errors. | not stored |  |  |
| `message_has_sms_error` | SMS Delivery error | boolean | Standard computed flag: true when an SMS sent from this Misc Charge Codes record failed to be delivered. | not stored |  |  |
| `message_ids` | Messages | one2many → `mail.message` | Chatter messages and log notes posted on this Misc Charge Codes record (standard mail thread). Displayed in the form view chatter. | stored | `model mail.message` (mail) | `view BugFix-Accounting.ported_view_2682_default_form_view_fo_79d2000d_8484_4cdb_befd_2dbcf0fb6a69` |
| `message_is_follower` | Is Follower | boolean | Standard computed flag: true when the current user follows this Misc Charge Codes record. | not stored |  |  |
| `message_needaction` | Action Needed | boolean | Standard computed flag: true when this Misc Charge Codes record has messages needing the current user's attention. | not stored |  |  |
| `message_needaction_counter` | Number of Actions | integer | Standard computed count of messages on this Misc Charge Codes record that need the current user's action. | not stored |  |  |
| `message_partner_ids` | Followers (Partners) | many2many → `res.partner` | Standard computed list of partners following this Misc Charge Codes record; mainly used for searching. | not stored | `model res.partner` (base) |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Due date of the current user's next activity on the Misc Charge Codes record; standard mixin field. | not stored |  |  |
| `rating_ids` | Ratings | one2many → `rating.rating` | Customer ratings linked to this Misc Charge Codes record (standard rating mixin); not used by any view or logic in this repo. | stored | `model rating.rating` (rating) |  |
| `website_message_ids` | Website Messages | one2many → `mail.message` | Standard computed subset of chatter messages on this Misc Charge Codes record that are visible on the website/portal. | stored | `model mail.message` (mail) |  |
| `write_date` | Last Updated on | datetime | Date and time the Misc Charge Codes record was last modified; set automatically. | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last modified the Misc Charge Codes record; set automatically. | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Active flag of the Misc Charge Codes record: unchecking it archives the record and hides it from default searches; defaults to checked via ir.default. | stored |  | `default BugFix-Accounting.default_109_x_misc_charge_codes_x_active`<br>`default BugFix-Studio-Misc.default_x_misc_charge_codes_x_active_109` (BugFix-Studio-Misc)<br>`view BugFix-Accounting.ported_view_2682_default_form_view_fo_79d2000d_8484_4cdb_befd_2dbcf0fb6a69`<br>`view BugFix-Accounting.ported_view_2683_default_search_view_26c03071_07d8_4292_934f_fd75e2f5f6db` |
| `x_name` | Misc. Charge Code | char | Code of the miscellaneous charge, shown in its list, form and search views. | stored |  | `view BugFix-Accounting.ported_view_2681_default_list_view_fo_d3bfc8f6_5ce5_4404_9e14_e4e077d23300`<br>`view BugFix-Accounting.ported_view_2682_default_form_view_fo_79d2000d_8484_4cdb_befd_2dbcf0fb6a69`<br>`view BugFix-Accounting.ported_view_2683_default_search_view_26c03071_07d8_4292_934f_fd75e2f5f6db` |
| `x_studio_charge_group` | Charge Group | selection: None=None; None=None; Charges=Charges; Charges=Charges; Duty=Duty; Duty=Duty; Taxes=Taxes; Taxes=Taxes | Group the charge code belongs to: None, Charges, Duty or Taxes. | stored |  | `view BugFix-Accounting.ported_view_2684_odoo_studio_default_2389c30f_1a37_4097_87d2_180fcdcddcb0`<br>`view BugFix-Accounting.ported_view_2685_odoo_studio_default_f4328649_f0ce_4d1a_9a3b_45e7f1c2e802` |
| `x_studio_company_id` | Company | many2one → `res.company` | Company the Misc Charge Codes record belongs to; enforced by a multi-company record rule and filled on creation by the 'JIN Company Id' automation. | stored | `model res.company` (base) | `record rule BugFix-Accounting.rule_570_jin_multi_company_misc_charge_codes`<br>`server action BugFix-Accounting.sa_f5_x_misc_charge_codes_jin_company_id_in_misc_charge_codes`<br>`server action BugFix-Accounting.server_action_2684_jin_company_id_in_misc_charge_codes`<br>`view BugFix-Accounting.ported_view_2685_odoo_studio_default_f4328649_f0ce_4d1a_9a3b_45e7f1c2e802` |
| `x_studio_credit_acc_type` | Credit Acc. Type | selection: Item=Item; Item=Item; G/L Account=G/L Account; G/L Account=G/L Account | Whether the credit side of the charge posts to an Item or a G/L Account. | stored |  | `view BugFix-Accounting.ported_view_2685_odoo_studio_default_f4328649_f0ce_4d1a_9a3b_45e7f1c2e802` |
| `x_studio_credit_account` | Credit Account | many2one → `account.account` | G/L account credited for this charge code. | stored | `model account.account` (account) | `view BugFix-Accounting.ported_view_2685_odoo_studio_default_f4328649_f0ce_4d1a_9a3b_45e7f1c2e802` |
| `x_studio_debit_acc_type` | Cost Load Type | selection: Item=Item; Item=Item; G/L Account=G/L Account; G/L Account=G/L Account | Cost Load Type: whether the cost is loaded onto the Item or a G/L Account. When set to Item, the 'IMP - Validate Debit Acc Type' automation clears the Debit Account. | stored |  | `server action BugFix-Accounting.server_action_1715_imp_validate_debit_acc_type`<br>`view BugFix-Accounting.ported_view_2684_odoo_studio_default_2389c30f_1a37_4097_87d2_180fcdcddcb0`<br>`view BugFix-Accounting.ported_view_2685_odoo_studio_default_f4328649_f0ce_4d1a_9a3b_45e7f1c2e802` |
| `x_studio_debit_account` | Debit Account | many2one → `account.account` | G/L account debited for this charge code; cleared automatically when Cost Load Type is Item. | stored | `model account.account` (account) | `server action BugFix-Accounting.server_action_1715_imp_validate_debit_acc_type`<br>`view BugFix-Accounting.ported_view_2685_odoo_studio_default_f4328649_f0ce_4d1a_9a3b_45e7f1c2e802` |
| `x_studio_description` | Description | char | Free-text description of the charge code. | stored |  | `view BugFix-Accounting.ported_view_2684_odoo_studio_default_2389c30f_1a37_4097_87d2_180fcdcddcb0`<br>`view BugFix-Accounting.ported_view_2685_odoo_studio_default_f4328649_f0ce_4d1a_9a3b_45e7f1c2e802` |
| `x_studio_sequence` | Sequence | integer | Sort order of Misc Charge Codes records in the list view (drag-and-drop handle); default value set by ir.default. | stored |  | `default BugFix-Accounting.default_110_x_misc_charge_codes_x_studio_sequence`<br>`default BugFix-Studio-Misc.default_x_misc_charge_codes_x_studio_sequence_110` (BugFix-Studio-Misc)<br>`view BugFix-Accounting.ported_view_2681_default_list_view_fo_d3bfc8f6_5ce5_4404_9e14_e4e077d23300` |
| `x_studio_system_entry` | System Entry | boolean | Checkbox on the charge code form marking it as a system-generated entry; no logic in this repo reads it. | stored |  | `view BugFix-Accounting.ported_view_2685_odoo_studio_default_f4328649_f0ce_4d1a_9a3b_45e7f1c2e802` |

**Server actions (3):**

- **Execute Code** (`server_action_2684_jin_company_id_in_misc_charge_codes`, type `code`)
  - Function: Run by the JIN automation: sets the Misc Charge Code's Company to the user's currently active company.
  - Depends on: `model res.company` (base), `model x_misc_charge_codes` (BugFix-Stock), `x_misc_charge_codes.x_studio_company_id` (BugFix-Stock)
  - Used by: `automation BugFix-Accounting.base_automation_318_jin_company_id_in_misc_charge_codes`
  <details><summary>code (5 lines)</summary>

```python

company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
company = env['res.company'].browse(company_id)

record['x_studio_company_id'] = company.id
```
  </details>
- **IMP - Validate Debit Acc Type** (`server_action_1715_imp_validate_debit_acc_type`, type `code`)
  - Function: On Misc Charge Codes, clears the Debit Account when Debit Acc Type is 'Item'.
  - Depends on: `model x_misc_charge_codes` (BugFix-Stock), `x_misc_charge_codes.x_studio_debit_acc_type` (BugFix-Stock), `x_misc_charge_codes.x_studio_debit_account` (BugFix-Stock)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (2 lines)</summary>

```python
if record.x_studio_debit_acc_type == 'Item':
  record['x_studio_debit_account'] = 0
```
  </details>
- **JIN - Company Id in Misc Charge Codes** (`sa_f5_x_misc_charge_codes_jin_company_id_in_misc_charge_codes`, type `code`)
  - Function: Sets the Misc Charge Codes record's Company field to the user's currently active company (first allowed company in context).
  - Depends on: `model res.company` (base), `model x_misc_charge_codes` (BugFix-Stock), `x_misc_charge_codes.x_studio_company_id` (BugFix-Stock)
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
| JIN - Company Id in Misc Charge Codes | `base_automation_318_jin_company_id_in_misc_charge_codes` |  | When a record is created or updated on Misc Charge Codes, runs _Execute Code_. | `model x_misc_charge_codes` (BugFix-Stock)<br>`server action BugFix-Accounting.server_action_2684_jin_company_id_in_misc_charge_codes`<br>`x_misc_charge_codes.create_date` (BugFix-Stock) |  |

**Window actions (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Misc. Charge Codes | `action_1172_misc_charge_codes` | Opens **Misc Charge Codes** records (tree,form). | `model x_misc_charge_codes` (BugFix-Stock) |  |
| Misc. Charge Codes | `action_2061_misc_charge_codes` | Opens **Misc Charge Codes** records (tree,form). | `model x_misc_charge_codes` (BugFix-Stock) | `menu BugFix-Studio-Misc.menu_f6r3_purchase_configuration_imports_configurations_misc_charge_co` (BugFix-Studio-Misc)<br>`menu BugFix-Studio-Misc.menu_f6r3_purchase_configuration_setups_misc_charges_misc_charge_codes` (BugFix-Studio-Misc)<br>`menu BugFix-Studio-Misc.menu_f6r3_purchase_configuration_setups_misc_charges` (BugFix-Studio-Misc)<br>`menu BugFix-Studio-Misc.menu_f6r3_purchase_imports_01_imports_configuration_misc_charge_codes` (BugFix-Studio-Misc) |

**Views (5):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_misc_charge_codes | `ported_view_2682_default_form_view_fo_79d2000d_8484_4cdb_befd_2dbcf0fb6a69` | form | full form layout with 5 fields | Default form for Misc Charge Codes: archived ribbon, required Name title, two empty groups and chatter. | `x_misc_charge_codes.activity_ids`<br>`x_misc_charge_codes.message_follower_ids`<br>`x_misc_charge_codes.message_ids`<br>`x_misc_charge_codes.x_active` (BugFix-Stock)<br>`x_misc_charge_codes.x_name` (BugFix-Stock) | `view BugFix-Accounting.ported_view_2684_odoo_studio_default_2389c30f_1a37_4097_87d2_180fcdcddcb0`<br>`view BugFix-Purchase.view_x_misc_charge_codes_form_link_fields` (BugFix-Purchase) |
| Default list view for x_misc_charge_codes | `ported_view_2681_default_list_view_fo_d3bfc8f6_5ce5_4404_9e14_e4e077d23300` | tree | full tree layout with 2 fields | Default list of Misc Charge Codes with sequence handle and Name. | `x_misc_charge_codes.x_name` (BugFix-Stock)<br>`x_misc_charge_codes.x_studio_sequence` (BugFix-Stock) | `view BugFix-Accounting.ported_view_2685_odoo_studio_default_f4328649_f0ce_4d1a_9a3b_45e7f1c2e802`<br>`view BugFix-Purchase.view_x_misc_charge_codes_tree_link_fields` (BugFix-Purchase) |
| Default search view for x_misc_charge_codes | `ported_view_2683_default_search_view_26c03071_07d8_4292_934f_fd75e2f5f6db` | search | full search layout with 1 fields | Default search view for Misc Charge Codes: search by name plus an Archived filter. | `x_misc_charge_codes.x_active` (BugFix-Stock)<br>`x_misc_charge_codes.x_name` (BugFix-Stock) |  |
| Odoo Studio: Default form view for x_misc_charge_codes customization | `ported_view_2684_odoo_studio_default_2389c30f_1a37_4097_87d2_180fcdcddcb0` | form | set create=false, delete=false, edit=false on `//form[1]`; set string=Misc. Charge Code on `//field[@name='x_name']`; inside `//group[@name='studio_group_d67062_left']`: add field x_studio_description, field x_studio_charge_group, field x_studio_debit_acc_type | Makes the Misc Charge Code form read-only (no create/edit/delete), labels Name as 'Misc. Charge Code' and adds Description, Charge Group (Charge/Duty/Tax) and Debit Account Type (item or ledger costing). | `view BugFix-Accounting.ported_view_2682_default_form_view_fo_79d2000d_8484_4cdb_befd_2dbcf0fb6a69`<br>`x_misc_charge_codes.x_studio_charge_group` (BugFix-Stock)<br>`x_misc_charge_codes.x_studio_debit_acc_type` (BugFix-Stock)<br>`x_misc_charge_codes.x_studio_description` (BugFix-Stock) |  |
| Odoo Studio: Default list view for x_misc_charge_codes customization | `ported_view_2685_odoo_studio_default_f4328649_f0ce_4d1a_9a3b_45e7f1c2e802` | tree | set default_order=x_studio_charge_group,x_name asc, editable=bottom on `//tree[1]`; set column_invisible=1 on `//field[@name='x_studio_sequence']`; set readonly=x_studio_system_entry == True on `//field[@name='x_name']`; after `//field[@name='x_name']`: add field x_studio_description, field x_studio_charge_group, field x_studio_debit_acc_type, field x_studio_company_id, field x_studio_debit_account, field x_studio_credit_acc_type, field x_studio_credit_account, field x_studio_system_entry | Makes the Misc Charge Codes list inline-editable, sorted by Charge Group then code, adding Description, Charge Group, cost loading type, Company, debit/credit account types and accounts, and System Entry; code, description and group are read-only on system entries. | `view BugFix-Accounting.ported_view_2681_default_list_view_fo_d3bfc8f6_5ce5_4404_9e14_e4e077d23300`<br>`x_misc_charge_codes.x_studio_charge_group` (BugFix-Stock)<br>`x_misc_charge_codes.x_studio_company_id` (BugFix-Stock)<br>`x_misc_charge_codes.x_studio_credit_acc_type` (BugFix-Stock)<br>`x_misc_charge_codes.x_studio_credit_account` (BugFix-Stock)<details><summary>+4 more</summary>`x_misc_charge_codes.x_studio_debit_acc_type` (BugFix-Stock)<br>`x_misc_charge_codes.x_studio_debit_account` (BugFix-Stock)<br>`x_misc_charge_codes.x_studio_description` (BugFix-Stock)<br>`x_misc_charge_codes.x_studio_system_entry` (BugFix-Stock)</details> |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Misc Charge Codes group_system | `access_1239_misc_charge_codes_group_system` | Gives **Administration / Settings** read/write/create/delete access to Misc Charge Codes records. | `group base.group_system` (base)<br>`model x_misc_charge_codes` (BugFix-Stock) |  |
| Misc Charge Codes group_user | `access_1240_misc_charge_codes_group_user` | Gives **User types / Internal User** read access to Misc Charge Codes records. | `group base.group_user` (base)<br>`model x_misc_charge_codes` (BugFix-Stock) |  |
| x_misc_charge_codes user access | `access_x_misc_charge_codes_user` | Gives **User types / Internal User** read/write/create/delete access to Misc Charge Codes records. | `group base.group_user` (base)<br>`model x_misc_charge_codes` (BugFix-Stock) |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| JIN - Multi-Company - Misc Charge Codes | `rule_570_jin_multi_company_misc_charge_codes` | For everyone (global rule): read/write/create/delete on Misc Charge Codes only where `['|', ('x_studio_company_id', 'in', company_ids), ('x_studio_company_id', '=', False)]`. | `model x_misc_charge_codes` (BugFix-Stock)<br>`x_misc_charge_codes.x_studio_company_id` (BugFix-Stock) |  |
