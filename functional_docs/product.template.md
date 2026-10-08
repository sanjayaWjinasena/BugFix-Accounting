# BugFix-Accounting — `product.template`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `product.template` — Product

*Extends a model created by `product`.* Python: `models/product_template.py`.

Other repos that use this model: `automation BugFix-Sales.base_automation_268_jin_company_id_in_product` (BugFix-Sales)<br>`automation BugFix-Sales.base_automation_66_imp_service_item_charge_duty_tax` (BugFix-Sales)<br>`automation BugFix-Sales.base_automation_83_imp_validate_default_split_method_in_item_master` (BugFix-Sales)<br>`automation BugFix-Sales.base_automation_84_imp_pass_split_method_in_item_master` (BugFix-Sales)<br>`server action BugFix-Purchase.sa_f5_x_imports_ledger_setup_imp_update_cost_allocation_method_in_items` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_1453_imp_update_cost_allocation_method_in_items` (BugFix-Purchase)<br>`server action BugFix-Sales.server_action_1142_update_product_cost_work_center_cost_2` (BugFix-Sales)<br>`server action BugFix-Sales.server_action_1387_imp_service_item_charge_duty_tax` (BugFix-Sales)<details><summary>+18 more</summary>`server action BugFix-Sales.server_action_1451_imp_validate_default_split_method_in_item_master` (BugFix-Sales)<br>`server action BugFix-Sales.server_action_1452_imp_pass_split_method_in_item_master` (BugFix-Sales)<br>`server action BugFix-Sales.server_action_2289_plm_item_approval_request_sent` (BugFix-Sales)<br>`server action BugFix-Sales.server_action_2291_plm_item_approval_request_notify_user` (BugFix-Sales)<br>`server action BugFix-Sales.server_action_2293_plm_request_item_approval` (BugFix-Sales)<br>`server action BugFix-Sales.server_action_2295_plm_item_approval` (BugFix-Sales)<br>`server action BugFix-Sales.server_action_2297_plm_item_approval_notify_project_user` (BugFix-Sales)<br>`server action BugFix-Sales.server_action_2299_plm_item_approval_validate` (BugFix-Sales)<br>`server action BugFix-Sales.server_action_2301_plm_item_approval_final` (BugFix-Sales)<br>`server action BugFix-Sales.server_action_2587_jin_company_id_in_product` (BugFix-Sales)<br>`server action BugFix-Sales.server_action_808_avoid_product_duplicate` (BugFix-Sales)<br>`server action BugFix-Studio-Misc.server_action_1743_sample_server_action` (BugFix-Studio-Misc)<br>`server action BugFix-Studio-Misc.server_action_2586_sample_server_action_to_get_company_id` (BugFix-Studio-Misc)<br>`server action BugFix-Studio-Misc.server_action_2831_mst_odoo_data_clean_up_001` (BugFix-Studio-Misc)<br>`window action BugFix-Sales.act_window_204_products` (BugFix-Sales)<br>`window action BugFix-Sales.act_window_2288_product_template` (BugFix-Sales)<br>`window action BugFix-Sales.act_window_2622_product_template` (BugFix-Sales)<br>`x_product_test.x_studio_product_1` (BugFix-Studio-Misc)</details>

**Summary:**

<!-- SUMMARY:model:product.template -->
This repo adds two product fields: Charge Type (Charge, Duty or Tax) and Non Billable. Both are shown on the product form. A server action enforces that only one billable or non-billable service product per company can be set up for each charge type. Another sets the product's company to the active company, but neither action is linked to a button, menu or automation. The repo also adds window actions, an archived 'Avoid Product Duplicate' automation and three record rules, including a global rule named 'test_access_rights' with an empty domain, so it does not filter any products.
<!-- /SUMMARY -->

**Fields (2):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `x_studio_charge_type` | Charge Type | selection: Charge=Charge; Duty=Duty; Tax=Tax | Classifies a service product as a Charge, Duty or Tax; read by the 'IMP - Service Item Charge/Duty' action and shown on the product form. | stored |  | `product.product.x_studio_charge_type`<br>`server action BugFix-Accounting.server_action_1387_imp_service_item_charge_duty_tax`<br>`server action BugFix-Sales.server_action_1387_imp_service_item_charge_duty_tax` (BugFix-Sales)<br>`view BugFix-Accounting.product_template_form_bugfix_accounting_field_content` |
| `x_studio_non_billable` | Non Billable | boolean | Marks the product as non-billable; read by the 'IMP - Service Item Charge/Duty' action and shown on the product form. | stored |  | `product.product.x_studio_non_billable`<br>`server action BugFix-Accounting.server_action_1387_imp_service_item_charge_duty_tax`<br>`server action BugFix-Sales.server_action_1387_imp_service_item_charge_duty_tax` (BugFix-Sales)<br>`view BugFix-Accounting.product_template_form_bugfix_accounting_field_content` |

**Server actions (2):**

- **IMP - Service Item - Charge-Duty-Tax** (`server_action_1387_imp_service_item_charge_duty_tax`, type `code`)
  - Function: For service products, prevents more than one billable service item per company being set up as Charge, Duty or Tax (and one non-billable Charge/Duty) by raising an error.
  - Depends on: `model product.template` (product), `model res.company` (base), `product.template.type` (product), `product.template.x_studio_charge_type`, `product.template.x_studio_non_billable`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (48 lines)</summary>

```python

if record.type == 'service':
  
  company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
  company = env['res.company'].browse(company_id)
  
  if record.x_studio_charge_type == 'Charge' and record.x_studio_non_billable == False:
    product = env['product.template'].search([('x_studio_charge_type', '=', 'Charge'), ('x_studio_non_billable', '=', False),('company_id', '=', company.id)], limit=1)
    if product:
      for p in product:
        if p.id != record.id:
          raise UserError("Only One Service Item can be Setup as Charge/ Not Non Billable Item!")

  if record.x_studio_charge_type == 'Duty' and record.x_studio_non_billable == False:
    product = env['product.template'].search([('x_studio_charge_type', '=', 'Duty'), ('x_studio_non_billable', '=', False),('company_id', '=', company.id)], limit=1)
    if product:
      for p in product:
        if p.id != record.id:
          raise UserError("Ony One Service Item can be Setup as Duty/ Not Non Billable Item!")

  if record.x_studio_charge_type == 'Tax' and record.x_studio_non_billable == False:
    product = env['product.template'].search([('x_studio_charge_type', '=', 'Tax'), ('x_studio_non_billable', '=', False),('company_id', '=', company.id)], limit=1)
    if product:
      for p in product:
        if p.id != record.id:
          raise UserError("Ony One Service Item can be Setup as Tax/ Not Non Billable Item!")
          
          
  if record.x_studio_charge_type == 'Charge' and record.x_studio_non_billable == True:
    product = env['product.template'].search([('x_studio_charge_type', '=', 'Charge'), ('x_studio_non_billable', '=', True),('company_id', '=', company.id)], limit=1)
    if product:
      for p in product:
        if p.id != record.id:
          raise UserError("Ony One Service Item can be Setup as Charge/ Non Billable Item!")

  if record.x_studio_charge_type == 'Duty' and record.x_studio_non_billable == True:
    product = env['product.template'].search([('x_studio_charge_type', '=', 'Duty'), ('x_studio_non_billable', '=', True),('company_id', '=', company.id)], limit=1)
    if product:
      for p in product:
        if p.id != record.id:
          raise UserError("Ony One Service Item can be Setup as Duty/ Non Billable Item!")

  """if record.x_studio_charge_type == 'Tax' and record.x_studio_non_billable == True:
    product = env['product.template'].search([('x_studio_charge_type', '=', 'Tax'), ('x_studio_non_billable', '=', True),('company_id', '=', company.id)], limit=1)
    if product:
      for p in product:
        if p.id != record.id:
          raise UserError("Ony One Service Item can be Setup as Tax/ Non Billable Item!")"""
```
  </details>
- **JIN - Company Id in Product** (`server_action_2587_jin_company_id_in_product`, type `code`)
  - Function: Sets the product's Company to the user's currently active company.
  - Depends on: `model product.template` (product), `model res.company` (base)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (5 lines)</summary>

```python

company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
company = env['res.company'].browse(company_id)

record['company_id'] = company.id
```
  </details>
**Automations (1):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| Avoid Product Duplicate | `base_automation_1_avoid_product_duplicate` | archived | When a record is created or updated on Product, runs nothing (no action linked). **Archived — does not run.** | `model product.template` (product) |  |

**Window actions (4):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Product.Template | `aw_f4_product_template_product_template` | Opens **Product** records (kanban,tree,form,activity). | `model product.template` (product) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_product_template` (BugFix-Studio-Misc) |
| Product.Template | `act_window_2288_product_template` | Opens **Product** records (kanban,tree,form,activity). | `model product.template` (product) |  |
| product.template | `aw_f4_product_template_product_template_1` | Opens **Product** records (kanban,tree,form,activity). | `model product.template` (product) | `menu BugFix-Studio-Misc.menu_f6f_product_template` (BugFix-Studio-Misc) |
| product.template | `act_window_2622_product_template` | Opens **Product** records (kanban,tree,form,activity). | `model product.template` (product) |  |

**Views (2):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| product.template.form.bugfix.accounting.field.content | `product_template_form_bugfix_accounting_field_content` | form | inside `//group[@name='studio_group_zujMt_right']`: add field x_studio_charge_type, field x_studio_non_billable | Adds Charge Type (radio) and Non Billable to the right-hand Studio group of the product form; both are editable only for service products. | `product.template.type` (product)<br>`product.template.x_studio_charge_type`<br>`product.template.x_studio_non_billable`<br>`view BugFix-Sales.ported_product_template_studio_2551` (BugFix-Sales) |  |
| product.template.product.form_button | `view_5061_product_template_product_form_button_e` | form | before `//button[@name='action_open_label_layout']`: add | Inactive (archived) product form extension whose only content (an action button) was stripped as unresolvable; has no effect. | `view product.product_template_only_form_view` (product) |  |

**Record rules (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Product multi-company | `rule_39_product_multi_company` | For everyone (global rule): read/write/create/delete on Product only where `['|', ('company_id', 'parent_of', company_ids), ('company_id', '=', False)]`. | `model product.template` (product)<br>`product.template.company_id` (product) |  |
| Public product template | `rule_445_public_product_template` | For User types / Portal, User types / Public: read on Product only where `[('website_published', '=', True), ("sale_ok", "=", True)]`. | `group base.group_portal` (base)<br>`group base.group_public` (base)<br>`model product.template` (product)<br>`product.template.sale_ok` (product)<br>`product.template.website_published` (website_sale) |  |
| test_access_rights | `rule_270_test_access_rights` | For everyone (global rule): read/delete on Product with no record filter (empty domain = all records). | `model product.template` (product) |  |
