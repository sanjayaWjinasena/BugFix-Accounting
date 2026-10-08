# BugFix-Accounting — `x_lc_header`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_lc_header` — LC Header

*Created by this repo.* Python: `models/x_lc_header.py`, `models/x_lc_header_gap.py`. Record name field: `x_name`.

Other repos that use this model: `purchase.order._compute_x_lc_header_count()` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_1400_imp_create_lc` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_1406_imp_change_payment_method_lc` (BugFix-Purchase)<br>`server action BugFix-Stock.server_action_1302_imp_apply_selected_po_lines_to_consignment` (BugFix-Stock)<br>`server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:x_lc_header -->
A Letter of Credit (LC) opened for an import purchase order, holding the SWIFT-style LC terms (issuing bank, beneficiary, amounts, currency, tolerance, shipment and expiry dates, documents and conditions). The LC Amount is converted to company currency and adjusted by the tolerance in two computed fields. The 'Post LC' button moves a Draft LC to Posted, and 'Amend LC' creates a new version with the version number increased and marks the old one Amended. Automations assign the registration number from the 'lc.registration.seq' sequence and block an LC whose amount plus the bank's posted LCs exceeds the issuing bank's LC limit; the list is read-only and a multi-company record rule applies.
<!-- /SUMMARY -->

**Fields (59):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Calendar meeting linked to the next activity on the LC Header record; standard mixin field. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Due date of the next scheduled activity on the LC Header record; standard mixin field. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Warning or error decoration shown when an exception-type activity exists on the LC Header record; standard mixin field. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Icon shown for an exception activity on the LC Header record; standard mixin field. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Activities (to-dos, calls, meetings) scheduled on this LC Header record; standard mail activity mixin field. | stored | `model mail.activity` (mail) | `x_lc_header.activity_summary`<br>`x_lc_header.activity_type_icon`<br>`x_lc_header.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity status of the LC Header record (Overdue, Today, Planned), computed from its next activity deadline. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Summary text of the next scheduled activity on the LC Header record; standard mixin field. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_lc_header.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Font Awesome icon of the next activity type, used in kanban/list activity widgets; standard mixin field. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_lc_header.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Type of the next scheduled activity on the LC Header record, read from its activities; standard mixin field. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_lc_header.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | User responsible for the next scheduled activity on the LC Header record; standard activity mixin field. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the LC Header record was created; set automatically. Used as the trigger of the on-creation automation(s): jin company id in lc header, jin lc registration seq no. | stored |  | `automation BugFix-Accounting.base_automation_284_jin_company_id_in_lc_header`<br>`automation BugFix-Accounting.base_automation_70_jin_lc_registration_seq_no` |
| `create_uid` | Created by | many2one → `res.users` | User who created the LC Header record; set automatically. | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name Odoo shows for the LC Header record in dropdowns, lists and breadcrumbs; computed from its name field. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the LC Header record, assigned automatically. | stored |  |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Due date of the current user's next activity on the LC Header record; standard mixin field. | not stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time the LC Header record was last modified; set automatically. | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last modified the LC Header record; set automatically. | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Active flag of the LC Header record: unchecking it archives the record and hides it from default searches; defaults to checked via ir.default. | stored |  | `default BugFix-Accounting.default_185_x_lc_header_x_active`<br>`view BugFix-Accounting.ported_default_form_view_fo_0505f2ad_156e_4774_9f56_2c28078f71bc`<br>`view BugFix-Accounting.ported_default_search_view__b401215c_a31a_436a_8006_25d5733275fa`<br>`view BugFix-Accounting.ported_view_3062_default_search_view_b401215c_a31a_436a_8006_25d5733275fa` |
| `x_name` | LC Registration No | char | LC registration number, assigned by the 'LC Registration Seq No' automation on creation (default from ir.default); copied when an LC is amended. | stored |  | `default BugFix-Accounting.default_195_x_lc_header_x_name`<br>`server action BugFix-Accounting.sa_f5_x_lc_header_lc_registration_seq_no`<br>`server action BugFix-Accounting.server_action_1402_lc_registration_seq_no`<br>`server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<details><summary>+4 more</summary>`view BugFix-Accounting.ported_default_form_view_fo_0505f2ad_156e_4774_9f56_2c28078f71bc`<br>`view BugFix-Accounting.ported_default_list_view_fo_a916dec6_fd01_439b_b5cc_5936bca48af2`<br>`view BugFix-Accounting.ported_default_search_view__b401215c_a31a_436a_8006_25d5733275fa`<br>`view BugFix-Accounting.ported_view_3062_default_search_view_b401215c_a31a_436a_8006_25d5733275fa`</details> |
| `x_studio_additional_conditions` | Additional Conditions (47A/B) | text | Additional conditions of the letter of credit (SWIFT field 47A/B), entered on the LC form; copied to the new version by the 'IMP - Amend LC' action. | stored |  | `server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9` |
| `x_studio_available_with_by` | Available with / By (41A) | char | Bank the credit is available with and how (SWIFT 41A), entered on the LC form; copied to the new version by the 'IMP - Amend LC' action. | stored |  | `server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9` |
| `x_studio_bank_charges` | Bank Charges (71B) | text | Which party bears bank charges (SWIFT 71B), entered on the LC form; copied to the new version by the 'IMP - Amend LC' action. | stored |  | `server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9` |
| `x_studio_beneficiary` | Beneficiary (59) | char | Beneficiary of the letter of credit (SWIFT 59), entered on the LC form; copied to the new version by the 'IMP - Amend LC' action. | stored |  | `server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9` |
| `x_studio_company_id` | Company | many2one → `res.company` | Company the LC belongs to; enforced by the multi-company record rule and filled on creation by the 'JIN Company Id in LC Header' automation. | stored | `model res.company` (base) | `record rule BugFix-Accounting.rule_516_jin_multi_company_lc_header`<br>`server action BugFix-Accounting.sa_f5_x_lc_header_jin_company_id_in_lc_header`<br>`server action BugFix-Accounting.server_action_2612_jin_company_id_in_lc_header`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9` |
| `x_studio_confirmation_instructions` | Confirmation Instructions (49) | selection: None=None; A=A; B=B; C=C | Confirmation instructions (SWIFT 49): None, A, B or C, with a default from ir.default; copied on LC amendment. | stored |  | `default BugFix-Accounting.default_194_x_lc_header_x_studio_confirmation_instructions`<br>`server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9` |
| `x_studio_created_from_purchase_order` | PO Number | many2one → `purchase.order` | Purchase order the letter of credit was opened from; filters the purchase order's 'LC' window action and is copied on amendment. | stored | `model purchase.order` (purchase) | `server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9`<br>`view BugFix-Accounting.ported_view_3064_odoo_studio_default_a61f262f_36fb_4249_a2be_011d2c858898`<br>`window action BugFix-Accounting.action_1403_lc` |
| `x_studio_currency_id` | Currency | many2one → `res.currency` | Currency of the LC amount (default from ir.default); used to convert LC Amount to local currency. | stored | `model res.currency` (base) | `default BugFix-Accounting.default_227_x_lc_header_x_studio_currency_id`<br>`default BugFix-Accounting.default_428_x_lc_header_x_studio_currency_id`<br>`server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9`<details><summary>+2 more</summary>`view BugFix-Accounting.ported_view_3064_odoo_studio_default_a61f262f_36fb_4249_a2be_011d2c858898`<br>`x_lc_header._compute_x_studio_lc_amount_lcy()`</details> |
| `x_studio_date_of_expiry` | Date of Expiry (31D) | date | Expiry date of the letter of credit (SWIFT 31D), entered on the LC form; copied to the new version by the 'IMP - Amend LC' action. | stored |  | `server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9`<br>`view BugFix-Accounting.ported_view_3064_odoo_studio_default_a61f262f_36fb_4249_a2be_011d2c858898` |
| `x_studio_date_of_issue` | Date of Issue (31C) | date | Issue date of the letter of credit (SWIFT 31C), entered on the LC form; copied to the new version by the 'IMP - Amend LC' action. | stored |  | `server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9` |
| `x_studio_date_of_receipt` | Date of Receipt | date | Date the letter of credit was received, entered on the LC form; copied to the new version by the 'IMP - Amend LC' action. | stored |  | `server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9`<br>`view BugFix-Accounting.ported_view_3064_odoo_studio_default_a61f262f_36fb_4249_a2be_011d2c858898` |
| `x_studio_deferred_days` | Deferred Days | float | Number of deferred-payment days, entered on the LC form; copied to the new version by the 'IMP - Amend LC' action. | stored |  | `server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9` |
| `x_studio_description_of_goods` | Description of Goods and / or Services (45A) | char | Description of goods and/or services covered (SWIFT 45A), entered on the LC form; copied to the new version by the 'IMP - Amend LC' action. | stored |  | `server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9` |
| `x_studio_document_required` | Document Required (46A/B) | text | Documents required for presentation (SWIFT 46A/B), entered on the LC form; copied to the new version by the 'IMP - Amend LC' action. | stored |  | `server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9` |
| `x_studio_draft` | Draft (42C) | selection: At Sight=At Sight; Deferred Payment=Deferred Payment | Draft terms (SWIFT 42C): At Sight or Deferred Payment, with an ir.default default; copied on amendment. | stored |  | `default BugFix-Accounting.default_193_x_lc_header_x_studio_draft`<br>`server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9` |
| `x_studio_indent_no` | Indent No | char | Indent number of the imported order, entered on the LC form; copied to the new version by the 'IMP - Amend LC' action. | stored |  | `server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9`<br>`view BugFix-Accounting.ported_view_3064_odoo_studio_default_a61f262f_36fb_4249_a2be_011d2c858898` |
| `x_studio_instruction_remarks` | Instruction / Remarks (78) | text | Instructions/remarks to the paying bank (SWIFT 78), entered on the LC form; copied to the new version by the 'IMP - Amend LC' action. | stored |  | `server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9` |
| `x_studio_issuing_bank` | Issuing Bank | many2one → `res.bank` | Bank issuing the letter of credit; used by the 'IMP - LC Amount Validation' check and copied on amendment. | stored | `model res.bank` (base) | `server action BugFix-Accounting.sa_f5_x_lc_header_imp_lc_amount_validation`<br>`server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.server_action_1407_imp_lc_amount_validation`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9`<details><summary>+1 more</summary>`view BugFix-Accounting.ported_view_3064_odoo_studio_default_a61f262f_36fb_4249_a2be_011d2c858898`</details> |
| `x_studio_issuing_bank_reference_no_1` | Issuing Bank Reference No | char | Issuing bank's reference number, entered on the LC form; copied to the new version by the 'IMP - Amend LC' action. | stored |  | `server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9` |
| `x_studio_latest_shipment_date` | Latest Shipment Date (44C) | date | Latest shipment date (SWIFT 44C), entered on the LC form; copied to the new version by the 'IMP - Amend LC' action. | stored |  | `server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9` |
| `x_studio_lc_amount` | LC Amount (32B) | float | Letter of credit amount in LC currency (SWIFT 32B); validated by the 'IMP - LC Amount Validation' automation and used to compute LC Amount (LCY) and Revised Amount. | stored |  | `automation BugFix-Accounting.base_automation_71_imp_lc_amount_validation`<br>`server action BugFix-Accounting.server_action_1404_imp_post_lc`<br>`server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`server action BugFix-Accounting.srv_lc_post_lc`<details><summary>+4 more</summary>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9`<br>`view BugFix-Accounting.ported_view_3064_odoo_studio_default_a61f262f_36fb_4249_a2be_011d2c858898`<br>`x_lc_header._compute_x_studio_lc_amount_lcy()`<br>`x_lc_header._compute_x_studio_revised_lc_amount()`</details> |
| `x_studio_lc_amount_lcy` | LC Amount (LCY) | float | LC Amount converted to company currency using the LC currency's current rate (rounded to 2 decimals); stored. | computed by `_compute_x_studio_lc_amount_lcy`; stored | `x_lc_header._compute_x_studio_lc_amount_lcy()` | `server action BugFix-Accounting.sa_f5_x_lc_header_imp_lc_amount_validation`<br>`server action BugFix-Accounting.server_action_1407_imp_lc_amount_validation`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9`<br>`view BugFix-Accounting.ported_view_3064_odoo_studio_default_a61f262f_36fb_4249_a2be_011d2c858898`<br>`x_lc_header._compute_x_studio_lc_amount_lcy()` |
| `x_studio_lc_credit_sub_type` | Documentary Credit Sub Type (40A) | selection: Non Transferable=Non Transferable; Transferable=Transferable; Revolving=Revolving | Documentary credit sub type (SWIFT 40A): Non Transferable, Transferable or Revolving (default from ir.default). | stored |  | `default BugFix-Accounting.default_188_x_lc_header_x_studio_lc_credit_sub_type`<br>`server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9`<br>`view BugFix-Accounting.ported_view_3064_odoo_studio_default_a61f262f_36fb_4249_a2be_011d2c858898` |
| `x_studio_lc_credit_type` | Documentary Credit Type (40A) | selection: Irrevocable=Irrevocable; Revocable=Revocable | Documentary credit type (SWIFT 40A): Irrevocable or Revocable (default from ir.default). | stored |  | `default BugFix-Accounting.default_187_x_lc_header_x_studio_lc_credit_type`<br>`server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9`<br>`view BugFix-Accounting.ported_view_3064_odoo_studio_default_a61f262f_36fb_4249_a2be_011d2c858898` |
| `x_studio_lc_no` | Documentatry Credit Number (20) | char | Documentary credit number assigned by the bank (SWIFT 20), entered on the LC form; copied to the new version by the 'IMP - Amend LC' action. | stored |  | `server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9`<br>`view BugFix-Accounting.ported_view_3064_odoo_studio_default_a61f262f_36fb_4249_a2be_011d2c858898` |
| `x_studio_loading_on_board` | Loading on Board (44A) | char | Port of loading / dispatch (SWIFT 44A), entered on the LC form; copied to the new version by the 'IMP - Amend LC' action. | stored |  | `server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9` |
| `x_studio_paid_amount_lcy` | Paid Amount (LCY) | float | Amount paid against the LC in local currency, shown on the LC form and list; not filled by logic in this repo. | stored |  | `view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9`<br>`view BugFix-Accounting.ported_view_3064_odoo_studio_default_a61f262f_36fb_4249_a2be_011d2c858898` |
| `x_studio_partial_shipment` | Partial Shipment (43P) | selection: Allowed=Allowed; Not Allowed=Not Allowed | Whether partial shipment is Allowed or Not Allowed (SWIFT 43P), with an ir.default default. | stored |  | `default BugFix-Accounting.default_191_x_lc_header_x_studio_partial_shipment`<br>`server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9` |
| `x_studio_period_for_presentation` | Period for Presentation (48) | float | Days allowed to present documents (SWIFT 48), entered on the LC form; copied to the new version by the 'IMP - Amend LC' action. | stored |  | `server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9` |
| `x_studio_place_of_expiry` | Place of Expiry (31D) | char | Place of expiry (SWIFT 31D), entered on the LC form; copied to the new version by the 'IMP - Amend LC' action. | stored |  | `server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9` |
| `x_studio_revised_lc_amount` | Revised Amount | float | LC Amount adjusted by the Tolerance percentage: increased when Tolerance Type is Plus, reduced when Minus, otherwise unchanged. | computed by `_compute_x_studio_revised_lc_amount`; stored | `x_lc_header._compute_x_studio_revised_lc_amount()` | `server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9`<br>`view BugFix-Accounting.ported_view_3064_odoo_studio_default_a61f262f_36fb_4249_a2be_011d2c858898`<br>`x_lc_header._compute_x_studio_revised_lc_amount()` |
| `x_studio_selection_field_yo4qM` | Pipeline status bar | selection: Draft=Draft; Posted=Posted; Amended=Amended; Paid=Paid; Cancelled=Cancelled | Status bar of the LC form (Draft, Posted, Amended, Paid, Cancelled), defaulted by ir.default; separate from the Status field used by actions. | stored |  | `default BugFix-Accounting.default_197_x_lc_header_x_studio_selection_field_yo4qM`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9` |
| `x_studio_sequence` | Sequence | integer | Sort order of LC Header records in the list view (drag-and-drop handle); default value set by ir.default. | stored |  | `default BugFix-Accounting.default_186_x_lc_header_x_studio_sequence`<br>`view BugFix-Accounting.ported_default_list_view_fo_a916dec6_fd01_439b_b5cc_5936bca48af2` |
| `x_studio_status` | Status | selection: Draft=Draft; Posted=Posted; Paid=Paid; Amended=Amended; Cancelled=Cancelled | LC lifecycle status (Draft, Posted, Paid, Amended, Cancelled); set by the 'IMP - Post LC', 'IMP - Amend LC' and paid-status actions and checked by LC amount validation. | stored |  | `default BugFix-Accounting.default_189_x_lc_header_x_studio_status`<br>`server action BugFix-Accounting.sa_f5_x_lc_header_imp_lc_amount_validation`<br>`server action BugFix-Accounting.server_action_1404_imp_post_lc`<br>`server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.server_action_1407_imp_lc_amount_validation`<details><summary>+5 more</summary>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`server action BugFix-Accounting.srv_lc_post_lc`<br>`view BugFix-Accounting.ported_default_form_view_fo_0505f2ad_156e_4774_9f56_2c28078f71bc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9`<br>`view BugFix-Accounting.ported_view_3064_odoo_studio_default_a61f262f_36fb_4249_a2be_011d2c858898`</details> |
| `x_studio_tolerance` | Tolerance (39A) | float | Tolerance percentage (SWIFT 39A) applied to the LC amount to get the Revised Amount. | stored |  | `server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9`<br>`x_lc_header._compute_x_studio_revised_lc_amount()` |
| `x_studio_tolerance_type` | Tolerance Type | selection: Plus=Plus; Minus=Minus | Whether the tolerance is Plus or Minus (default from ir.default); drives the Revised Amount. | stored |  | `default BugFix-Accounting.default_190_x_lc_header_x_studio_tolerance_type`<br>`server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9`<br>`x_lc_header._compute_x_studio_revised_lc_amount()` |
| `x_studio_transportation` | Transportation (44B) | char | Final destination / transportation (SWIFT 44B), entered on the LC form; copied to the new version by the 'IMP - Amend LC' action. | stored |  | `server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9` |
| `x_studio_transshipment` | Transshipment (43T) | selection: Allowed=Allowed; Not Allowed=Not Allowed | Whether transshipment is Allowed or Not Allowed (SWIFT 43T), with an ir.default default. | stored |  | `default BugFix-Accounting.default_192_x_lc_header_x_studio_transshipment`<br>`server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9` |
| `x_studio_vendor` | Vendor | many2one → `res.partner` | Vendor (supplier) the letter of credit is opened for, entered on the LC form; copied to the new version by the 'IMP - Amend LC' action. | stored | `model res.partner` (base) | `server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9`<br>`view BugFix-Accounting.ported_view_3064_odoo_studio_default_a61f262f_36fb_4249_a2be_011d2c858898` |
| `x_studio_version_no` | Version No | integer | Amendment version of the LC (default from ir.default); incremented on the new record by 'IMP - Amend LC'. | stored |  | `default BugFix-Accounting.default_199_x_lc_header_x_studio_version_no`<br>`server action BugFix-Accounting.server_action_1405_imp_amend_lc`<br>`server action BugFix-Accounting.srv_lc_amend_lc`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9`<br>`view BugFix-Accounting.ported_view_3064_odoo_studio_default_a61f262f_36fb_4249_a2be_011d2c858898` |

**Python methods (2):**

| Method | Function | Decorators | Extends standard | Depends on | Used by | Where |
|---|---|---|---|---|---|---|
| `_compute_x_studio_lc_amount_lcy` | Compute for LC Amount (LCY): converts the LC Amount into company currency by dividing by the selected currency's current rate, rounded to 2 decimals; 0 if no currency/rate. | api.depends('x_studio_currency_id', 'x_studio_currency_id.rate', 'x_studio_lc_am… |  | `res.currency.rate` (base)<br>`x_lc_header.x_studio_currency_id`<br>`x_lc_header.x_studio_lc_amount_lcy`<br>`x_lc_header.x_studio_lc_amount` | `x_lc_header.x_studio_lc_amount_lcy` | `models/x_lc_header.py:51` |
| `_compute_x_studio_revised_lc_amount` | Compute for Revised LC Amount: LC Amount plus or minus Tolerance % depending on Tolerance Type (Plus/Minus); unchanged otherwise. | api.depends('x_studio_lc_amount', 'x_studio_tolerance_type', 'x_studio_tolerance… |  | `x_lc_header.x_studio_lc_amount`<br>`x_lc_header.x_studio_revised_lc_amount`<br>`x_lc_header.x_studio_tolerance_type`<br>`x_lc_header.x_studio_tolerance` | `x_lc_header.x_studio_revised_lc_amount` | `models/x_lc_header.py:64` |

**Server actions (10):**

- **Execute Code** (`server_action_1402_lc_registration_seq_no`, type `code`)
  - Function: Run by the LC Registration Seq No automation: when Name is 'New', assigns the next number from the 'lc.registration.seq' sequence.
  - Depends on: `model ir.sequence` (base), `model x_lc_header`, `x_lc_header.x_name`
  - Used by: `automation BugFix-Accounting.base_automation_70_jin_lc_registration_seq_no`
  <details><summary>code (6 lines)</summary>

```python

#record['x_name'] = env['ir.sequence'].next_by_code('purchase.request.seq')

if record.x_name == 'New':
 seq = env['ir.sequence'].next_by_code('lc.registration.seq')
 record.write({'x_name': seq})
```
  </details>
- **Execute Code** (`server_action_1407_imp_lc_amount_validation`, type `code`)
  - Function: Run by the LC Amount Validation automation: requires an Issuing Bank with an LC limit and blocks when this LC (LCY) plus the bank's Posted LCs exceeds that limit.
  - Depends on: `model x_lc_header`, `x_lc_header.x_studio_issuing_bank`, `x_lc_header.x_studio_lc_amount_lcy`, `x_lc_header.x_studio_status`
  - Used by: `automation BugFix-Accounting.base_automation_71_imp_lc_amount_validation`
  <details><summary>code (19 lines)</summary>

```python

if record.x_studio_issuing_bank.id != 0:
  if record.x_studio_issuing_bank.x_studio_lc_limit != 0.00:
    sum_lc = 0
    lc_lines = env['x_lc_header'].search([('x_studio_issuing_bank', '=', record.x_studio_issuing_bank.id), ('x_studio_status', '=', 'Posted')])
    if lc_lines:
      for sum_lines in lc_lines:
        sum_lc += sum_lines.x_studio_lc_amount_lcy
    
    if (record.x_studio_lc_amount_lcy + sum_lc) > record.x_studio_issuing_bank.x_studio_lc_limit:
      raise UserError('Current LC Amount must be within the Available LC Balance.' + '\n' +
                    'Current LC Amount (LCY): ' + str(record.x_studio_lc_amount_lcy) + '\n' + '\n' +
                    'Bank LC Limit (LCY): ' + str(record.x_studio_issuing_bank.x_studio_lc_limit) + '\n' + 
                    'Posted LC Amount (LCY): ' + str(sum_lc) + '\n' +
                    'Available LC Balance (LCY): ' + str(record.x_studio_issuing_bank.x_studio_lc_limit - sum_lc))
  else:
    raise UserError('LC Limit of the Selected Issuing Bank must be Specified.')
else:
  raise UserError('Issuing Bank must be Specified.')
```
  </details>
- **Execute Code** (`server_action_2612_jin_company_id_in_lc_header`, type `code`)
  - Function: Run by the JIN automation: sets the LC's Company to the user's currently active company.
  - Depends on: `model res.company` (base), `model x_lc_header`, `x_lc_header.x_studio_company_id`
  - Used by: `automation BugFix-Accounting.base_automation_284_jin_company_id_in_lc_header`
  <details><summary>code (5 lines)</summary>

```python

company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
company = env['res.company'].browse(company_id)

record['x_studio_company_id'] = company.id
```
  </details>
- **IMP - Amend LC** (`srv_lc_amend_lc`, type `code`)
  - Function: Amend LC button: creates a new LC copying all terms of the current one with version number +1, marks the current LC as Amended and opens the new version.
  - Depends on: `model x_lc_header`, `x_lc_header.x_name`, `x_lc_header.x_studio_additional_conditions`, `x_lc_header.x_studio_available_with_by`, `x_lc_header.x_studio_bank_charges`<details><summary>+32 more</summary>`x_lc_header.x_studio_beneficiary`, `x_lc_header.x_studio_confirmation_instructions`, `x_lc_header.x_studio_created_from_purchase_order`, `x_lc_header.x_studio_currency_id`, `x_lc_header.x_studio_date_of_expiry`, `x_lc_header.x_studio_date_of_issue`, `x_lc_header.x_studio_date_of_receipt`, `x_lc_header.x_studio_deferred_days`, `x_lc_header.x_studio_description_of_goods`, `x_lc_header.x_studio_document_required`, `x_lc_header.x_studio_draft`, `x_lc_header.x_studio_indent_no`, `x_lc_header.x_studio_instruction_remarks`, `x_lc_header.x_studio_issuing_bank_reference_no_1`, `x_lc_header.x_studio_issuing_bank`, `x_lc_header.x_studio_latest_shipment_date`, `x_lc_header.x_studio_lc_amount`, `x_lc_header.x_studio_lc_credit_sub_type`, `x_lc_header.x_studio_lc_credit_type`, `x_lc_header.x_studio_lc_no`, `x_lc_header.x_studio_loading_on_board`, `x_lc_header.x_studio_partial_shipment`, `x_lc_header.x_studio_period_for_presentation`, `x_lc_header.x_studio_place_of_expiry`, `x_lc_header.x_studio_revised_lc_amount`, `x_lc_header.x_studio_status`, `x_lc_header.x_studio_tolerance_type`, `x_lc_header.x_studio_tolerance`, `x_lc_header.x_studio_transportation`, `x_lc_header.x_studio_transshipment`, `x_lc_header.x_studio_vendor`, `x_lc_header.x_studio_version_no`</details>
  - Used by: `view BugFix-Accounting.ported_default_form_view_fo_0505f2ad_156e_4774_9f56_2c28078f71bc`
  <details><summary>code (52 lines)</summary>

```python

if record.id:
    lc = env['x_lc_header'].create({'x_studio_created_from_purchase_order': record.x_studio_created_from_purchase_order.id})
    lc.write({
        'x_name': record.x_name,
        'x_studio_indent_no': record.x_studio_indent_no,
        'x_studio_additional_conditions': record.x_studio_additional_conditions,
        'x_studio_available_with_by': record.x_studio_available_with_by,
        'x_studio_bank_charges': record.x_studio_bank_charges,
        'x_studio_beneficiary': record.x_studio_beneficiary,
        'x_studio_confirmation_instructions': record.x_studio_confirmation_instructions,
        'x_studio_currency_id': record.x_studio_currency_id,
        'x_studio_date_of_expiry': record.x_studio_date_of_expiry,
        'x_studio_date_of_issue': record.x_studio_date_of_issue,
        'x_studio_date_of_receipt': record.x_studio_date_of_receipt,
        'x_studio_deferred_days': record.x_studio_deferred_days,
        'x_studio_description_of_goods': record.x_studio_description_of_goods,
        'x_studio_document_required': record.x_studio_document_required,
        'x_studio_draft': record.x_studio_draft,
        'x_studio_instruction_remarks': record.x_studio_instruction_remarks,
        'x_studio_issuing_bank': record.x_studio_issuing_bank.id,
        'x_studio_issuing_bank_reference_no_1': record.x_studio_issuing_bank_reference_no_1,
        'x_studio_latest_shipment_date': record.x_studio_latest_shipment_date,
        'x_studio_lc_amount': record.x_studio_lc_amount,
        'x_studio_lc_credit_sub_type': record.x_studio_lc_credit_sub_type,
        'x_studio_lc_credit_type': record.x_studio_lc_credit_type,
        'x_studio_lc_no': record.x_studio_lc_no,
        'x_studio_loading_on_board': record.x_studio_loading_on_board,
        'x_studio_partial_shipment': record.x_studio_partial_shipment,
        'x_studio_period_for_presentation': record.x_studio_period_for_presentation,
        'x_studio_place_of_expiry': record.x_studio_place_of_expiry,
        'x_studio_revised_lc_amount': record.x_studio_revised_lc_amount,
        'x_studio_tolerance': record.x_studio_tolerance,
        'x_studio_tolerance_type': record.x_studio_tolerance_type,
        'x_studio_transportation': record.x_studio_transportation,
        'x_studio_transshipment': record.x_studio_transshipment,
        'x_studio_vendor': record.x_studio_vendor.id,
        'x_studio_version_no': (record.x_studio_version_no + 1),
    })

    action = {
        'name': 'Letter of Credit',
        'domain': [('id', '=', lc.id)],
        'type': 'ir.actions.act_window',
        'res_model': 'x_lc_header',
        'view_mode': 'tree,form',
        'view_id': False,
        'context': False,
    }

    record['x_studio_status'] = 'Amended'
    record['x_studio_selection_field_yo4qM'] = 'Amended'
```
  </details>
- **IMP - Amend LC** (`server_action_1405_imp_amend_lc`, type `code`)
  - Function: Legacy Amend LC action: creates a new LC copying the current LC's terms with version number +1, marks the current LC as Amended and opens the new one.
  - Depends on: `model x_lc_header`, `x_lc_header.x_name`, `x_lc_header.x_studio_additional_conditions`, `x_lc_header.x_studio_available_with_by`, `x_lc_header.x_studio_bank_charges`<details><summary>+32 more</summary>`x_lc_header.x_studio_beneficiary`, `x_lc_header.x_studio_confirmation_instructions`, `x_lc_header.x_studio_created_from_purchase_order`, `x_lc_header.x_studio_currency_id`, `x_lc_header.x_studio_date_of_expiry`, `x_lc_header.x_studio_date_of_issue`, `x_lc_header.x_studio_date_of_receipt`, `x_lc_header.x_studio_deferred_days`, `x_lc_header.x_studio_description_of_goods`, `x_lc_header.x_studio_document_required`, `x_lc_header.x_studio_draft`, `x_lc_header.x_studio_indent_no`, `x_lc_header.x_studio_instruction_remarks`, `x_lc_header.x_studio_issuing_bank_reference_no_1`, `x_lc_header.x_studio_issuing_bank`, `x_lc_header.x_studio_latest_shipment_date`, `x_lc_header.x_studio_lc_amount`, `x_lc_header.x_studio_lc_credit_sub_type`, `x_lc_header.x_studio_lc_credit_type`, `x_lc_header.x_studio_lc_no`, `x_lc_header.x_studio_loading_on_board`, `x_lc_header.x_studio_partial_shipment`, `x_lc_header.x_studio_period_for_presentation`, `x_lc_header.x_studio_place_of_expiry`, `x_lc_header.x_studio_revised_lc_amount`, `x_lc_header.x_studio_status`, `x_lc_header.x_studio_tolerance_type`, `x_lc_header.x_studio_tolerance`, `x_lc_header.x_studio_transportation`, `x_lc_header.x_studio_transshipment`, `x_lc_header.x_studio_vendor`, `x_lc_header.x_studio_version_no`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (51 lines)</summary>

```python
if record.id:
  lc = env['x_lc_header'].create({'x_studio_created_from_purchase_order':record.x_studio_created_from_purchase_order.id})
  lc.write({'x_name':record.x_name,
            'x_studio_indent_no':record.x_studio_indent_no,
            'x_studio_additional_conditions':record.x_studio_additional_conditions,
            'x_studio_available_with_by':record.x_studio_available_with_by,
            'x_studio_bank_charges':record.x_studio_bank_charges,
            'x_studio_beneficiary':record.x_studio_beneficiary,
            'x_studio_confirmation_instructions':record.x_studio_confirmation_instructions,
            'x_studio_currency_id':record.x_studio_currency_id,
            'x_studio_date_of_expiry':record.x_studio_date_of_expiry,
            'x_studio_date_of_issue':record.x_studio_date_of_issue,
            'x_studio_date_of_receipt':record.x_studio_date_of_receipt,
            'x_studio_deferred_days':record.x_studio_deferred_days,
            'x_studio_description_of_goods':record.x_studio_description_of_goods,
            'x_studio_document_required':record.x_studio_document_required,
            'x_studio_draft':record.x_studio_draft,
            'x_studio_instruction_remarks':record.x_studio_instruction_remarks,
            'x_studio_issuing_bank':record.x_studio_issuing_bank.id,
            'x_studio_issuing_bank_reference_no_1':record.x_studio_issuing_bank_reference_no_1,
            'x_studio_latest_shipment_date':record.x_studio_latest_shipment_date,
            'x_studio_lc_amount':record.x_studio_lc_amount,
            'x_studio_lc_credit_sub_type':record.x_studio_lc_credit_sub_type,
            'x_studio_lc_credit_type':record.x_studio_lc_credit_type,
            'x_studio_lc_no':record.x_studio_lc_no,
            'x_studio_loading_on_board':record.x_studio_loading_on_board,
            'x_studio_partial_shipment':record.x_studio_partial_shipment,
            'x_studio_period_for_presentation':record.x_studio_period_for_presentation,
            'x_studio_place_of_expiry':record.x_studio_place_of_expiry,
            'x_studio_revised_lc_amount':record.x_studio_revised_lc_amount,
            'x_studio_tolerance':record.x_studio_tolerance,
            'x_studio_tolerance_type':record.x_studio_tolerance_type,
            'x_studio_transportation':record.x_studio_transportation,
            'x_studio_transshipment':record.x_studio_transshipment,
            'x_studio_vendor':record.x_studio_vendor.id,
            'x_studio_version_no': (record.x_studio_version_no + 1)})

  action = {
            'name': 'Letter of Credit',
            'domain': [('id', '=', lc.id)],
            'type': 'ir.actions.act_window',
            'res_model': 'x_lc_header',
            'view_mode': 'tree,form',
            'view_type': 'form',
            'view_id': False,
            'context': False,
            } 
    
 
  record['x_studio_status'] = 'Amended'
  record['x_studio_selection_field_yo4qM'] = 'Amended'
```
  </details>
- **IMP - LC Amount Validation** (`sa_f5_x_lc_header_imp_lc_amount_validation`, type `code`)
  - Function: Validates an LC: errors if no Issuing Bank or the bank has no LC limit, and blocks if this LC amount (LCY) plus all Posted LCs of the bank exceeds the bank's LC limit, showing the available balance.
  - Depends on: `model x_lc_header`, `x_lc_header.x_studio_issuing_bank`, `x_lc_header.x_studio_lc_amount_lcy`, `x_lc_header.x_studio_status`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (18 lines)</summary>

```python
if record.x_studio_issuing_bank.id != 0:
  if record.x_studio_issuing_bank.x_studio_lc_limit != 0.00:
    sum_lc = 0
    lc_lines = env['x_lc_header'].search([('x_studio_issuing_bank', '=', record.x_studio_issuing_bank.id), ('x_studio_status', '=', 'Posted')])
    if lc_lines:
      for sum_lines in lc_lines:
        sum_lc += sum_lines.x_studio_lc_amount_lcy
    
    if (record.x_studio_lc_amount_lcy + sum_lc) > record.x_studio_issuing_bank.x_studio_lc_limit:
      raise UserError('Current LC Amount must be within the Available LC Balance.' + '\n' +
                    'Current LC Amount (LCY): ' + str(record.x_studio_lc_amount_lcy) + '\n' + '\n' +
                    'Bank LC Limit (LCY): ' + str(record.x_studio_issuing_bank.x_studio_lc_limit) + '\n' + 
                    'Posted LC Amount (LCY): ' + str(sum_lc) + '\n' +
                    'Available LC Balance (LCY): ' + str(record.x_studio_issuing_bank.x_studio_lc_limit - sum_lc))
  else:
    raise UserError('LC Limit of the Selected Issuing Bank must be Specified.')
else:
  raise UserError('Issuing Bank must be Specified.')
```
  </details>
- **IMP - Post LC** (`srv_lc_post_lc`, type `code`)
  - Function: Post LC button: errors if LC Amount is zero, otherwise sets the LC status and status bar to Posted.
  - Depends on: `model x_lc_header`, `x_lc_header.x_studio_lc_amount`, `x_lc_header.x_studio_status`
  - Used by: `view BugFix-Accounting.ported_default_form_view_fo_0505f2ad_156e_4774_9f56_2c28078f71bc`
  <details><summary>code (6 lines)</summary>

```python

if record.x_studio_lc_amount == 0.00:
    raise UserError('LC Amount must be Specified')

record['x_studio_status'] = 'Posted'
record['x_studio_selection_field_yo4qM'] = 'Posted'
```
  </details>
- **IMP - Post LC** (`server_action_1404_imp_post_lc`, type `code`)
  - Function: Legacy Post LC action: errors if LC Amount is zero, otherwise sets the LC status fields to Posted.
  - Depends on: `model x_lc_header`, `x_lc_header.x_studio_lc_amount`, `x_lc_header.x_studio_status`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (5 lines)</summary>

```python
if record.x_studio_lc_amount == 0.00:
  raise UserError('LC Amount must be Specified')
  
record['x_studio_status'] = 'Posted'
record['x_studio_selection_field_yo4qM'] = 'Posted'
```
  </details>
- **JIN - Company Id in LC Header** (`sa_f5_x_lc_header_jin_company_id_in_lc_header`, type `code`)
  - Function: Sets the LC Header record's Company field to the user's currently active company (first allowed company in context).
  - Depends on: `model res.company` (base), `model x_lc_header`, `x_lc_header.x_studio_company_id`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (4 lines)</summary>

```python
company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
company = env['res.company'].browse(company_id)

record['x_studio_company_id'] = company.id
```
  </details>
- **LC Registration Seq.No** (`sa_f5_x_lc_header_lc_registration_seq_no`, type `code`)
  - Function: When the LC's Name is still 'New', assigns the next number from the 'lc.registration.seq' sequence.
  - Depends on: `model ir.sequence` (base), `model x_lc_header`, `x_lc_header.x_name`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (5 lines)</summary>

```python
#record['x_name'] = env['ir.sequence'].next_by_code('purchase.request.seq')

if record.x_name == 'New':
 seq = env['ir.sequence'].next_by_code('lc.registration.seq')
 record.write({'x_name': seq})
```
  </details>
**Automations (3):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| IMP - LC Amount Validation | `base_automation_71_imp_lc_amount_validation` |  | When a watched field changes in the form on LC Header, runs _Execute Code_. | `model x_lc_header`<br>`server action BugFix-Accounting.server_action_1407_imp_lc_amount_validation`<br>`x_lc_header.x_studio_lc_amount` |  |
| JIN - Company Id in LC Header | `base_automation_284_jin_company_id_in_lc_header` | archived | When a record is created or updated on LC Header, runs _Execute Code_. **Archived — does not run.** | `model x_lc_header`<br>`server action BugFix-Accounting.server_action_2612_jin_company_id_in_lc_header`<br>`x_lc_header.create_date` |  |
| JIN-LC Registration Seq.No | `base_automation_70_jin_lc_registration_seq_no` |  | When a record is created or updated on LC Header, runs _Execute Code_. | `model x_lc_header`<br>`server action BugFix-Accounting.server_action_1402_lc_registration_seq_no`<br>`x_lc_header.create_date` |  |

**Window actions (4):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| LC | `action_1403_lc` | Opens **LC Header** records (tree,form), filtered to `[('x_studio_created_from_purchase_order', '=', active_id)]`. | `model x_lc_header`<br>`x_lc_header.x_studio_created_from_purchase_order` | `view BugFix-Purchase.view_2409_odoo_studio_purchase_order_form_customization_e` (BugFix-Purchase) |
| LC Header | `action_1401_lc_header` | Opens **LC Header** records (tree,form). | `model x_lc_header` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_lc_header` (BugFix-Studio-Misc) |
| Letter of Credit | `action_2071_letter_of_credit` | Opens **LC Header** records (tree,form). | `model x_lc_header` | `menu BugFix-Studio-Misc.menu_f6r3_purchase_imports_letter_of_credit` (BugFix-Studio-Misc) |
| Letter of Credit | `action_2889_letter_of_credit` | Opens **LC Header** records (tree,form). | `model x_lc_header` |  |

**Views (8):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_lc_header | `ported_default_form_view_fo_0505f2ad_156e_4774_9f56_2c28078f71bc` | form | full form layout with 3 fields | Base LC (Letter of Credit) form: header buttons 'Post LC' (only in Draft) and 'Amend LC' (only when Posted), a hidden status field, Registration No title and Archived ribbon. | `server action BugFix-Accounting.srv_lc_amend_lc`<br>`server action BugFix-Accounting.srv_lc_post_lc`<br>`x_lc_header.x_active`<br>`x_lc_header.x_name`<br>`x_lc_header.x_studio_status` | `view BugFix-Accounting.ported_odoo_studio_default__20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9`<br>`view BugFix-Accounting.ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9` |
| Default list view for x_lc_header | `ported_default_list_view_fo_a916dec6_fd01_439b_b5cc_5936bca48af2` | tree | full tree layout with 2 fields | Base list screen for LC Header records showing Name with a drag handle for manual ordering by Sequence. | `x_lc_header.x_name`<br>`x_lc_header.x_studio_sequence` | `view BugFix-Accounting.ported_odoo_studio_default__a61f262f_36fb_4249_a2be_011d2c858898`<br>`view BugFix-Accounting.ported_view_3064_odoo_studio_default_a61f262f_36fb_4249_a2be_011d2c858898` |
| Default search view for x_lc_header | `ported_default_search_view__b401215c_a31a_436a_8006_25d5733275fa` | search | full search layout with 1 fields | Search bar for LC Header records: search by Name and an 'Archived' filter to show inactive records. | `x_lc_header.x_active`<br>`x_lc_header.x_name` |  |
| Default search view for x_lc_header | `ported_view_3062_default_search_view_b401215c_a31a_436a_8006_25d5733275fa` | search | full search layout with 1 fields | Default search view for LC (Letter of Credit) Header records: search by name plus an Archived filter. | `x_lc_header.x_active`<br>`x_lc_header.x_name` |  |
| Odoo Studio: Default form view for x_lc_header customization | `ported_odoo_studio_default__20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9` | form | set create=false, delete=false on `//form[1]` | Studio customization of the LC form: disables creating and deleting LCs from the form. | `view BugFix-Accounting.ported_default_form_view_fo_0505f2ad_156e_4774_9f56_2c28078f71bc` |  |
| Odoo Studio: Default form view for x_lc_header customization | `ported_view_3063_odoo_studio_default_20735bbc_d408_4d7a_8c04_a3bf6b3dfcd9` | form | set create=false, delete=false on `//form[1]`; after `//header[1]/button[1]`: add field x_studio_selection_field_yo4qM; set force_save=True, string=Registration No, readonly=1 on `//field[@name='x_name']`; inside `//group[@name='studio_group_535d1b_left']`: add field x_studio_created_from_purchase_order, field x_studio_version_no, field x_studio_company_id; after `//group[@name='studio_group_535d1b']`: add notebook | LC Header form customization: disables create/delete, adds a status bar after the first header button, makes Registration No read-only, adds Ref. PO, Version No and Company, and appends a notebook of LC details. | `view BugFix-Accounting.ported_default_form_view_fo_0505f2ad_156e_4774_9f56_2c28078f71bc`<br>`x_lc_header.x_studio_additional_conditions`<br>`x_lc_header.x_studio_available_with_by`<br>`x_lc_header.x_studio_bank_charges`<br>`x_lc_header.x_studio_beneficiary`<details><summary>+35 more</summary>`x_lc_header.x_studio_company_id`<br>`x_lc_header.x_studio_confirmation_instructions`<br>`x_lc_header.x_studio_created_from_purchase_order`<br>`x_lc_header.x_studio_currency_id`<br>`x_lc_header.x_studio_date_of_expiry`<br>`x_lc_header.x_studio_date_of_issue`<br>`x_lc_header.x_studio_date_of_receipt`<br>`x_lc_header.x_studio_deferred_days`<br>`x_lc_header.x_studio_description_of_goods`<br>`x_lc_header.x_studio_document_required`<br>`x_lc_header.x_studio_draft`<br>`x_lc_header.x_studio_indent_no`<br>`x_lc_header.x_studio_instruction_remarks`<br>`x_lc_header.x_studio_issuing_bank_reference_no_1`<br>`x_lc_header.x_studio_issuing_bank`<br>`x_lc_header.x_studio_latest_shipment_date`<br>`x_lc_header.x_studio_lc_amount_lcy`<br>`x_lc_header.x_studio_lc_amount`<br>`x_lc_header.x_studio_lc_credit_sub_type`<br>`x_lc_header.x_studio_lc_credit_type`<br>`x_lc_header.x_studio_lc_no`<br>`x_lc_header.x_studio_loading_on_board`<br>`x_lc_header.x_studio_paid_amount_lcy`<br>`x_lc_header.x_studio_partial_shipment`<br>`x_lc_header.x_studio_period_for_presentation`<br>`x_lc_header.x_studio_place_of_expiry`<br>`x_lc_header.x_studio_revised_lc_amount`<br>`x_lc_header.x_studio_selection_field_yo4qM`<br>`x_lc_header.x_studio_status`<br>`x_lc_header.x_studio_tolerance_type`<br>`x_lc_header.x_studio_tolerance`<br>`x_lc_header.x_studio_transportation`<br>`x_lc_header.x_studio_transshipment`<br>`x_lc_header.x_studio_vendor`<br>`x_lc_header.x_studio_version_no`</details> |  |
| Odoo Studio: Default list view for x_lc_header customization | `ported_odoo_studio_default__a61f262f_36fb_4249_a2be_011d2c858898` | tree | set create=false, default_order=x_name desc, delete=false, edit=false on `//tree[1]` | Studio customization of the LC list: read-only list (no create, edit or delete) sorted by Registration No descending. | `view BugFix-Accounting.ported_default_list_view_fo_a916dec6_fd01_439b_b5cc_5936bca48af2` |  |
| Odoo Studio: Default list view for x_lc_header customization | `ported_view_3064_odoo_studio_default_a61f262f_36fb_4249_a2be_011d2c858898` | tree | set create=false, default_order=x_name desc, delete=false, edit=false on `//tree[1]`; set column_invisible=1 on `//field[@name='x_studio_sequence']`; after `//field[@name='x_studio_sequence']`: add field x_studio_created_from_purchase_order, field x_studio_indent_no, field x_studio_vendor; set string=LC Registration No on `//field[@name='x_name']`; after `//field[@name='x_name']`: add field x_studio_status, field x_studio_currency_id, field x_studio_issuing_bank, field x_studio_lc_amount_lcy, field x_studio_lc_amount, field x_studio_revised_lc_amount, field x_studio_paid_amount_lcy, field x_studio_date_of_receipt, field x_studio_lc_credit_type, field x_studio_lc_credit_sub_type, field x_studio_lc_no, field x_studio_date_of_expiry … | LC Header list: read-only (no create/edit/delete), newest first, showing PO number, indent no, vendor, LC Registration No, status, currency, issuing bank, LC amounts, paid amount, receipt/expiry dates, credit types and LC No. | `view BugFix-Accounting.ported_default_list_view_fo_a916dec6_fd01_439b_b5cc_5936bca48af2`<br>`x_lc_header.x_studio_created_from_purchase_order`<br>`x_lc_header.x_studio_currency_id`<br>`x_lc_header.x_studio_date_of_expiry`<br>`x_lc_header.x_studio_date_of_receipt`<details><summary>+12 more</summary>`x_lc_header.x_studio_indent_no`<br>`x_lc_header.x_studio_issuing_bank`<br>`x_lc_header.x_studio_lc_amount_lcy`<br>`x_lc_header.x_studio_lc_amount`<br>`x_lc_header.x_studio_lc_credit_sub_type`<br>`x_lc_header.x_studio_lc_credit_type`<br>`x_lc_header.x_studio_lc_no`<br>`x_lc_header.x_studio_paid_amount_lcy`<br>`x_lc_header.x_studio_revised_lc_amount`<br>`x_lc_header.x_studio_status`<br>`x_lc_header.x_studio_vendor`<br>`x_lc_header.x_studio_version_no`</details> |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| LC Header group_system | `access_1376_lc_header_group_system` | Gives **Administration / Settings** read/write/create/delete access to LC Header records. | `group base.group_system` (base)<br>`model x_lc_header` |  |
| LC Header group_user | `access_1377_lc_header_group_user` | Gives **User types / Internal User** read access to LC Header records. | `group base.group_user` (base)<br>`model x_lc_header` |  |
| x_lc_header user access | `access_x_lc_header_user` | Gives **User types / Internal User** read/write/create/delete access to LC Header records. | `group base.group_user` (base)<br>`model x_lc_header` |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| JIN - Multi-Company - LC Header | `rule_516_jin_multi_company_lc_header` | For everyone (global rule): read/write/create/delete on LC Header only where `['|', ('x_studio_company_id', 'in', company_ids), ('x_studio_company_id', '=', False)]`. | `model x_lc_header`<br>`x_lc_header.x_studio_company_id` |  |
