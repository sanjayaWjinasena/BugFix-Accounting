# BugFix-Accounting — `consignment_charge_h`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `consignment_charge_h` — Consignment Charge Header

*Extends a model created by `BugFix-Stock`.* Python: `models/consignment_charge_h.py`, `models/x_consignment_charge_h_gap.py`. Record name field: `name`.

Other repos that use this model: `access right BugFix-Stock.access_consignment_charge_h_user` (BugFix-Stock)<br>`access right BugFix-Studio-Misc.access_g_consignment_charge_h_consignment_charge_h_purchase_jin_po_invoicing_payment_i` (BugFix-Studio-Misc)<br>`access right BugFix-Studio-Misc.access_g_consignment_charge_h_consignment_charge_h_purchase_jin_procurement_end_user_i` (BugFix-Studio-Misc)<br>`automation BugFix-Stock.automation_jin_company_id_in_consignment_charge_header` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_create_consignment_header_charges` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_allocate_consignment_header_charges` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_check_consignment_assessable_value` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_consignment_custom_duty` (BugFix-Stock)<details><summary>+10 more</summary>`server action BugFix-Stock.action_imp_copy_charges_to_tp_invoice` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_reset_header_charges_consignment` (BugFix-Stock)<br>`server action BugFix-Stock.action_jin_company_id_in_consignment_charge_header` (BugFix-Stock)<br>`server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up` (BugFix-Studio-Misc)<br>`window action BugFix-Stock.action_consignment_charge_header` (BugFix-Stock)<br>`window action BugFix-Stock.action_header_charges` (BugFix-Stock)<br>`window action BugFix-Stock.action_consignment_charge_header_2` (BugFix-Stock)<br>`window action BugFix-Stock.action_consignment_charge_header_3` (BugFix-Stock)<br>`window action BugFix-Stock.action_purchase_invoices_2` (BugFix-Stock)<br>`consignment_charge_l.consignment_charge_header_id` (BugFix-Stock)</details>

**Summary:**

<!-- SUMMARY:model:consignment_charge_h -->
The model is created by BugFix-Stock. This repo adds 16 fields for header charge lines of an import consignment. The fields include charge group (Charges, Duty, Taxes), charge name, basis (Percentage or Fixed Per Document), amount, tax applicable, ledger post, consignment link and company. BugFix-Stock's 'IMP - Check Consignment' action reads several of them. An automation sets the company to the user's active company. The repo also adds form, list and search views, five window actions (including 'Header Charges' filtered by consignment), access rights and a multi-company record rule.
<!-- /SUMMARY -->

**Fields (46):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Calendar meeting linked to the next activity on the Consignment Charge Header record; standard mixin field. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Due date of the next scheduled activity on the Consignment Charge Header record; standard mixin field. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Warning or error decoration shown when an exception-type activity exists on the Consignment Charge Header record; standard mixin field. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Icon shown for an exception activity on the Consignment Charge Header record; standard mixin field. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Activities (to-dos, calls, meetings) scheduled on this Consignment Charge Header record; standard mail activity mixin field. | stored | `model mail.activity` (mail) | `view BugFix-Accounting.view_consignment_charge_h_form`<br>`consignment_charge_h.activity_summary`<br>`consignment_charge_h.activity_type_icon`<br>`consignment_charge_h.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity status of the Consignment Charge Header record (Overdue, Today, Planned), computed from its next activity deadline. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Summary text of the next scheduled activity on the Consignment Charge Header record; standard mixin field. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`consignment_charge_h.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Font Awesome icon of the next activity type, used in kanban/list activity widgets; standard mixin field. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`consignment_charge_h.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Type of the next scheduled activity on the Consignment Charge Header record, read from its activities; standard mixin field. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`consignment_charge_h.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | User responsible for the next scheduled activity on the Consignment Charge Header record; standard activity mixin field. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the Consignment Charge Header record was created; set automatically. Used as the trigger of the on-creation automation(s): jin company id in consignment charge header. | stored |  | `automation BugFix-Accounting.automation_jin_company_id_in_consignment_charge_header` |
| `create_uid` | Created by | many2one → `res.users` | User who created the Consignment Charge Header record; set automatically. | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name Odoo shows for the Consignment Charge Header record in dropdowns, lists and breadcrumbs; computed from its name field. | not stored |  |  |
| `has_message` | Has Message | boolean | Whether the Consignment Charge Header record has any chatter messages; standard chatter field. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the Consignment Charge Header record, assigned automatically. | stored |  |  |
| `message_attachment_count` | Attachment Count | integer | Number of attachments on the Consignment Charge Header record; standard chatter field. | not stored |  |  |
| `message_follower_ids` | Followers | one2many → `mail.followers` | Followers who receive notifications for the Consignment Charge Header record, shown in the chatter. | stored | `model mail.followers` (mail) | `view BugFix-Accounting.view_consignment_charge_h_form` |
| `message_has_error` | Message Delivery error | boolean | Whether a message on the Consignment Charge Header record failed to be delivered; standard chatter field. | not stored |  |  |
| `message_has_error_counter` | Number of errors | integer | Number of messages on the Consignment Charge Header record with delivery errors; standard chatter field. | not stored |  |  |
| `message_has_sms_error` | SMS Delivery error | boolean | Whether an SMS sent from the Consignment Charge Header record failed; standard chatter field. | not stored |  |  |
| `message_ids` | Messages | one2many → `mail.message` | Chatter messages and log notes posted on the Consignment Charge Header record. | stored | `model mail.message` (mail) | `view BugFix-Accounting.view_consignment_charge_h_form` |
| `message_is_follower` | Is Follower | boolean | Whether the current user follows the Consignment Charge Header record; standard chatter field. | not stored |  |  |
| `message_needaction` | Action Needed | boolean | Whether the Consignment Charge Header record has unread messages that need the current user's attention; standard chatter field. | not stored |  |  |
| `message_needaction_counter` | Number of Actions | integer | Number of messages on the Consignment Charge Header record needing the current user's attention; standard chatter field. | not stored |  |  |
| `message_partner_ids` | Followers (Partners) | many2many → `res.partner` | Partners following the Consignment Charge Header record; standard chatter field used for searching. | not stored | `model res.partner` (base) |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Due date of the current user's next activity on the Consignment Charge Header record; standard mixin field. | not stored |  |  |
| `rating_ids` | Ratings | one2many → `rating.rating` | Customer ratings linked to the Consignment Charge Header record; standard field from the mail thread mixin, not used here. | stored | `model rating.rating` (rating) |  |
| `website_message_ids` | Website Messages | one2many → `mail.message` | Messages on the Consignment Charge Header record that are visible on the website/portal; standard chatter field. | stored | `model mail.message` (mail) |  |
| `write_date` | Last Updated on | datetime | Date and time the Consignment Charge Header record was last modified; set automatically. | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last modified the Consignment Charge Header record; set automatically. | stored | `model res.users` (base) |  |
| `active` | Active | boolean | Active flag of the Consignment Charge Header record: unchecking it archives the record and hides it from default searches; defaults to checked via ir.default. | stored |  | `default BugFix-Accounting.default_consignment_charge_h_active`<br>`view BugFix-Accounting.view_consignment_charge_h_form`<br>`view BugFix-Accounting.view_consignment_charge_h_search` |
| `name` | Name | char | Name of the consignment header charge line, shown in its list, form and search views. | stored |  | `view BugFix-Accounting.view_consignment_charge_h_list`<br>`view BugFix-Accounting.view_consignment_charge_h_form`<br>`view BugFix-Accounting.view_consignment_charge_h_search` |
| `allocate_header_charges` | Allocate Header Charges | boolean | Checkbox on the header charge form marking that the charge should be allocated across the consignment; no logic in this repo reads it. | stored |  | `view BugFix-Accounting.view_default_list_view_for_consignment_charge_h_inherit` |
| `amount` | Amount | float | Amount of the charge (a percentage or fixed value depending on Basis), entered on the consignment's header charges. | stored |  | `view BugFix-Accounting.view_default_form_view_for_consignment_charge_h_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_consignment_charge_h_inherit` |
| `basis` | Basis | selection: Percentage=Percentage; Percentage=Percentage; Fixed Per Document=Fixed Per Document; Fixed Per Document=Fixed Per Document | How the charge amount is applied: Percentage or Fixed Per Document. | stored |  | `view BugFix-Accounting.view_default_form_view_for_consignment_charge_h_inherit` |
| `charge_group` | Charge Group | selection: None=None; None=None; Charges=Charges; Charges=Charges; Duty=Duty; Duty=Duty; Taxes=Taxes; Taxes=Taxes | Group the charge belongs to (None, Charges, Duty, Taxes), with a default from ir.default; read by the BugFix-Stock 'IMP - Check Consignment' action when processing consignment charges. | stored |  | `default BugFix-Accounting.default_consignment_charge_h_charge_group`<br>`server action BugFix-Stock.action_imp_check_consignment_assessable_value` (BugFix-Stock)<br>`view BugFix-Accounting.view_default_form_view_for_consignment_charge_h_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_consignment_charge_h_inherit` |
| `charge_name` | Charge Name | char | Name of the charge on the consignment; read by the BugFix-Stock 'IMP - Check Consignment' action. | stored |  | `server action BugFix-Stock.action_imp_check_consignment_assessable_value` (BugFix-Stock)<br>`view BugFix-Accounting.view_default_form_view_for_consignment_charge_h_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_consignment_charge_h_inherit` |
| `accounting_company_id` | Company | many2one → `res.company` | Company the charge belongs to; enforced by the multi-company record rule and filled on creation by the 'JIN Company Id in Consignment Charge Header' automation. | stored | `model res.company` (base) | `record rule BugFix-Accounting.rule_jin_multi_company_consignment_charge_header`<br>`server action BugFix-Accounting.action_jin_company_id_in_consignment_charge_header`<br>`server action BugFix-Stock.action_jin_company_id_in_consignment_charge_header` (BugFix-Stock)<br>`view BugFix-Accounting.view_default_list_view_for_consignment_charge_h_inherit` |
| `consignment_id` | Consignment Id | many2one → `consignment_header` | Consignment header this charge line belongs to; the 'Header Charges' window action filters by it and the BugFix-Stock consignment check reads it. | stored | `model consignment_header` (BugFix-Stock) | `server action BugFix-Stock.action_imp_check_consignment_assessable_value` (BugFix-Stock)<br>`view BugFix-Accounting.view_default_form_view_for_consignment_charge_h_inherit`<br>`window action BugFix-Accounting.action_header_charges`<br>`window action BugFix-Stock.action_header_charges` (BugFix-Stock) |
| `formula` | Formula | char | Free-text formula for the charge, entered on the header charge form; not evaluated by any logic in this repo. | stored |  | `view BugFix-Accounting.view_default_form_view_for_consignment_charge_h_inherit` |
| `ledger_post` | Ledger Post | boolean | Whether the charge should be posted to the ledger; default from ir.default, shown on the charge forms. No logic in this repo reads it. | stored |  | `default BugFix-Accounting.default_consignment_charge_h_ledger_post`<br>`view BugFix-Accounting.view_default_form_view_for_consignment_charge_h_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_consignment_charge_h_inherit` |
| `sequence` | Sequence | integer | Sort order of Consignment Charge Header records in the list view (drag-and-drop handle); default value set by ir.default. | stored |  | `default BugFix-Accounting.default_consignment_charge_h_sequence`<br>`view BugFix-Accounting.view_consignment_charge_h_list` |
| `structure_no` | Structure No | integer | Structure number of the charge (default from ir.default), shown on the header charge form. | stored |  | `default BugFix-Accounting.default_consignment_charge_h_structure_no`<br>`view BugFix-Accounting.view_default_form_view_for_consignment_charge_h_inherit` |
| `tax_appicable` | Tax Applicable | boolean | Marks the charge as taxable; read by the BugFix-Stock 'IMP - Check Consignment' action. | stored |  | `server action BugFix-Stock.action_imp_check_consignment_assessable_value` (BugFix-Stock)<br>`view BugFix-Accounting.view_default_form_view_for_consignment_charge_h_inherit`<br>`view BugFix-Accounting.view_default_list_view_for_consignment_charge_h_inherit` |
| `tax_appicable2` | Tax Applicable2 | boolean | Second 'Tax Applicable' checkbox shown on one charge form; no logic in this repo reads it. | stored |  | `view BugFix-Accounting.view_default_list_view_for_consignment_charge_h_inherit` |
| `tp_processed` | TP Processed | boolean | Flag shown on the charge form indicating the charge has been processed for TP; no logic in this repo sets or reads it. | stored |  | `view BugFix-Accounting.view_default_list_view_for_consignment_charge_h_inherit` |

**Server actions (1):**

- **JIN - Company Id in Consignment Charge Header** (`action_jin_company_id_in_consignment_charge_header`, type `code`)
  - Function: Sets the Consignment Charge Header's Company to the user's currently active company.
  - Depends on: `model res.company` (base), `model consignment_charge_h` (BugFix-Stock), `consignment_charge_h.accounting_company_id` (BugFix-Stock)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (5 lines)</summary>

```python
company_id = env.context.get("allowed_company_ids", [env.user.company_id.id])[0]
company = env["res.company"].browse(company_id)

record["accounting_company_id"] = company.id
```
  </details>
**Automations (1):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| JIN - Company Id in Consignment Charge Header | `automation_jin_company_id_in_consignment_charge_header` |  | When a record is created or updated on Consignment Charge Header, runs _JIN - Company Id in Consignment Charge Header_. | `model consignment_charge_h` (BugFix-Stock)<br>`server action BugFix-Stock.action_jin_company_id_in_consignment_charge_header` (BugFix-Stock)<br>`consignment_charge_h.create_date` (BugFix-Stock) |  |

**Window actions (5):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Consignment Charge Header | `action_consignment_charge_header` | Opens **Consignment Charge Header** records (tree,form). | `model consignment_charge_h` (BugFix-Stock) |  |
| Consignment Charge Header | `action_consignment_charge_header_2` | Opens **Consignment Charge Header** records (tree,form). | `model consignment_charge_h` (BugFix-Stock) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_imports_consignment_charge_header` (BugFix-Studio-Misc) |
| Consignment Charge Header | `action_consignment_charge_header_3` | Opens **Consignment Charge Header** records (tree,form). | `model consignment_charge_h` (BugFix-Stock) |  |
| Header Charges | `action_header_charges` | Opens **Consignment Charge Header** records (tree,form), filtered to `[('consignment_id', '=', active_id)]`. | `model consignment_charge_h` (BugFix-Stock)<br>`consignment_charge_h.consignment_id` (BugFix-Stock) |  |
| Purchase Invoices | `action_purchase_invoices` | Opens **Consignment Charge Header** records (tree,form). | `model consignment_charge_h` (BugFix-Stock) |  |

**Views (5):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for consignment_charge_h | `view_consignment_charge_h_form` | form | full form layout with 5 fields | Base form for Consignment Charge Header lines: archived ribbon, Name title, two empty groups filled by its Studio extension, and chatter. | `consignment_charge_h.activity_ids`<br>`consignment_charge_h.message_follower_ids`<br>`consignment_charge_h.message_ids`<br>`consignment_charge_h.active` (BugFix-Stock)<br>`consignment_charge_h.name` (BugFix-Stock) | `view BugFix-Accounting.view_default_form_view_for_consignment_charge_h_inherit`<br>`view BugFix-Purchase.view_consignment_charge_h_form_upstream_link_fields` (BugFix-Purchase) |
| Default list view for consignment_charge_h | `view_consignment_charge_h_list` | tree | full tree layout with 2 fields | Base list for Consignment Charge Header records with a sequence handle and Name; columns are extended by its Studio extension. | `consignment_charge_h.name` (BugFix-Stock)<br>`consignment_charge_h.sequence` (BugFix-Stock) | `view BugFix-Accounting.view_default_list_view_for_consignment_charge_h_inherit` |
| Default search view for consignment_charge_h | `view_consignment_charge_h_search` | search | full search layout with 1 fields | Default search view for Consignment Charge Header records: search by name plus an Archived filter. | `consignment_charge_h.active` (BugFix-Stock)<br>`consignment_charge_h.name` (BugFix-Stock) |  |
| Odoo Studio: Default form view for consignment_charge_h customization | `view_default_form_view_for_consignment_charge_h_inherit` | form | inside `//group[@name='studio_group_99a601_left']`: add field charge_group, field charge_name, field basis, field formula, field amount, field ledger_post; inside `//group[@name='studio_group_99a601_right']`: add field consignment_id, field structure_no, field tax_appicable | Consignment Charge Header form: adds Charge Group, Charge Name, Amount and Ledger Post, plus hidden Basis, Formula, Consignment Id, Structure No and Tax Applicable fields. | `view BugFix-Accounting.view_consignment_charge_h_form`<br>`consignment_charge_h.amount` (BugFix-Stock)<br>`consignment_charge_h.basis` (BugFix-Stock)<br>`consignment_charge_h.charge_group` (BugFix-Stock)<br>`consignment_charge_h.charge_name` (BugFix-Stock)<details><summary>+5 more</summary>`consignment_charge_h.consignment_id` (BugFix-Stock)<br>`consignment_charge_h.formula` (BugFix-Stock)<br>`consignment_charge_h.ledger_post` (BugFix-Stock)<br>`consignment_charge_h.structure_no` (BugFix-Stock)<br>`consignment_charge_h.tax_appicable` (BugFix-Stock)</details> |  |
| Odoo Studio: Default list view for consignment_charge_h customization | `view_default_list_view_for_consignment_charge_h_inherit` | tree | set create=false, delete=false, editable=bottom on `//tree[1]`; set column_invisible=1 on `//field[@name='sequence']`; after `//field[@name='sequence']`: add field charge_group, field charge_name, field amount, field ledger_post, field accounting_company_id, field tax_appicable, field tax_appicable2, field tp_processed, field allocate_header_charges; set column_invisible=1 on `//field[@name='name']` | Makes the Consignment Charge Header list inline-editable (no create/delete), showing read-only Charge Group/Name, Amount (editable only for Charges not allocated from header) and Ledger Post, with hidden company, tax, TP and allocation flags. | `view BugFix-Accounting.view_consignment_charge_h_list`<br>`consignment_charge_h.allocate_header_charges` (BugFix-Stock)<br>`consignment_charge_h.amount` (BugFix-Stock)<br>`consignment_charge_h.charge_group` (BugFix-Stock)<br>`consignment_charge_h.charge_name` (BugFix-Stock)<details><summary>+5 more</summary>`consignment_charge_h.accounting_company_id` (BugFix-Stock)<br>`consignment_charge_h.ledger_post` (BugFix-Stock)<br>`consignment_charge_h.tax_appicable2` (BugFix-Stock)<br>`consignment_charge_h.tax_appicable` (BugFix-Stock)<br>`consignment_charge_h.tp_processed` (BugFix-Stock)</details> |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Consignment Charge Header group_system | `access_consignment_charge_header_group_system` | Gives **Administration / Settings** read/write/create/delete access to Consignment Charge Header records. | `group base.group_system` (base)<br>`model consignment_charge_h` (BugFix-Stock) |  |
| Consignment Charge Header group_user | `access_consignment_charge_header_group_user` | Gives **User types / Internal User** read access to Consignment Charge Header records. | `group base.group_user` (base)<br>`model consignment_charge_h` (BugFix-Stock) |  |
| consignment_charge_h user access | `access_consignment_charge_h_user` | Gives **User types / Internal User** read/write/create/delete access to Consignment Charge Header records. | `group base.group_user` (base)<br>`model consignment_charge_h` (BugFix-Stock) |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| JIN - Multi-Company - Consignment Charge Header | `rule_jin_multi_company_consignment_charge_header` | For everyone (global rule): read/write/create/delete on Consignment Charge Header only where `['|', ('accounting_company_id', 'in', company_ids), ('accounting_company_id', '=', False)]`. | `model consignment_charge_h` (BugFix-Stock)<br>`consignment_charge_h.accounting_company_id` (BugFix-Stock) |  |
