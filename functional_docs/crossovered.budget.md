# BugFix-Accounting — `crossovered.budget`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `crossovered.budget` — Budget

*Extends a model created by `account_budget`.* Python: `models/crossovered_budget.py`, `models/crossovered_budget_gap.py`.

Other repos that use this model: `report BugFix-Studio-Misc.action_report_2792_budget_report` (BugFix-Studio-Misc)<br>`sale.order.x_studio_project_budget` (BugFix-Sales)<br>`server action BugFix-Sales.server_action_2178_proj_create_budget_entries` (BugFix-Sales)

**Summary:**

<!-- SUMMARY:model:crossovered.budget -->
This repo adds 20 fields and their computes to budgets for project budgeting. The fields cover the analytic account, project number, source sales order, project value, planned and actual expenses, actual invoiced amount, completion %, estimated revenue, gross margin and its %, and Confirm/SPR status flags based on the sales order's purchase requests. Automations block confirming a budget without valid non-zero lines and block deleting budgets created from a sales order. The customized budget form disables create, adds these figures and locks line analytic accounts. The repo also adds Budget window actions filtered by sales order.
<!-- /SUMMARY -->

**Fields (20):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `x_currency_id` | Currency | many2one → `res.currency` | Currency of the budget's monetary fields, defaulted by an ir.default record. | stored | `model res.currency` (base) | `default BugFix-Accounting.default_574_crossovered_budget_x_currency_id`<br>`view BugFix-Accounting.ported_view_4942_odoo_studio_crossove_a555672e_6698_4232_9115_1daaed24a1bb` |
| `x_studio_actual_expenses_incurred` | Actual Expenses Incurred | monetary | Actual expenses: sum of practical amounts on 'Expenses' budget lines, sign-flipped to a positive figure. | computed by `_compute_x_studio_actual_expenses_incurred`; not stored | `crossovered.budget._compute_x_studio_actual_expenses_incurred()` | `crossovered.budget._compute_x_studio_actual_expenses_incurred()`<br>`crossovered.budget._compute_x_studio_gross_margin()`<br>`crossovered.budget._compute_x_studio_project_completed_percentage_1()`<br>`view BugFix-Accounting.ported_view_4942_odoo_studio_crossove_a555672e_6698_4232_9115_1daaed24a1bb` |
| `x_studio_actual_invoiced_amount` | Actual Invoiced Amount | monetary | Actual revenue: sum of practical (actual) amounts on 'Revenue' budget lines. | computed by `_compute_x_studio_actual_invoiced_amount`; not stored | `crossovered.budget._compute_x_studio_actual_invoiced_amount()` | `crossovered.budget._compute_x_studio_actual_invoiced_amount()`<br>`view BugFix-Accounting.ported_view_4942_odoo_studio_crossove_a555672e_6698_4232_9115_1daaed24a1bb` |
| `x_studio_analytic_account` | Analytic Account | many2one → `account.analytic.account` | Analytic account the budget is for, entered on the budget form. | stored | `model account.analytic.account` (analytic) | `view BugFix-Accounting.ported_view_4942_odoo_studio_crossove_a555672e_6698_4232_9115_1daaed24a1bb` |
| `x_studio_confirm_status` | Confirm Status | boolean | True when the source sales order is a Project-type, inventory-short order whose purchase requests still have outstanding quantities, or that has no purchase request (or the PR model is absent). | computed by `_compute_x_studio_confirm_status`; not stored | `crossovered.budget._compute_x_studio_confirm_status()` | `crossovered.budget._compute_x_studio_confirm_status()`<br>`server action BugFix-Accounting.sa_f5_crossovered_budget_proj_validate_confirm`<br>`server action BugFix-Accounting.server_action_2570_proj_validate_confirm`<br>`view BugFix-Accounting.ported_view_4942_odoo_studio_crossove_a555672e_6698_4232_9115_1daaed24a1bb` |
| `x_studio_confirm_validation` | Confirm Validation | text | Text field on the budget form (default from ir.default); no logic in this repo reads it. | stored |  | `default BugFix-Accounting.default_412_crossovered_budget_x_studio_confirm_validation`<br>`view BugFix-Accounting.ported_view_4942_odoo_studio_crossove_a555672e_6698_4232_9115_1daaed24a1bb` |
| `x_studio_created_from_sales_order_1` | Created From Sales Order | many2one → `sale.order` | Sales order the project budget was created from. Drives Confirm Status and SPR Status, and the 'Proj - Validate Confirm/Delete' checks. | stored | `model sale.order` (sale) | `crossovered.budget._compute_x_studio_confirm_status()`<br>`crossovered.budget._compute_x_studio_spr_status()`<br>`server action BugFix-Accounting.sa_f5_crossovered_budget_proj_validate_confirm`<br>`server action BugFix-Accounting.sa_f5_crossovered_budget_proj_validate_delete`<br>`server action BugFix-Accounting.server_action_2183_proj_validate_delete`<details><summary>+5 more</summary>`server action BugFix-Accounting.server_action_2570_proj_validate_confirm`<br>`view BugFix-Accounting.ported_view_4942_odoo_studio_crossove_a555672e_6698_4232_9115_1daaed24a1bb`<br>`window action BugFix-Accounting.act_window_2180_budget`<br>`window action BugFix-Accounting.action_2180_budget`<br>`window action BugFix-Accounting.aw_f4_crossovered_budget_budget`</details> |
| `x_studio_estimated_revenue_1` | Estimated Revenue | monetary | Revenue earned to date estimated as Project Value x Project Completed Percentage. | computed by `_compute_x_studio_estimated_revenue_1`; not stored | `crossovered.budget._compute_x_studio_estimated_revenue_1()` | `crossovered.budget._compute_x_studio_estimated_revenue_1()`<br>`crossovered.budget._compute_x_studio_gross_margin()`<br>`crossovered.budget._compute_x_studio_gross_margin_percentage()`<br>`crossovered.budget._compute_x_studio_gross_margin_percentage_1()`<br>`crossovered.budget._compute_x_studio_percentage()`<details><summary>+1 more</summary>`view BugFix-Accounting.ported_view_4942_odoo_studio_crossove_a555672e_6698_4232_9115_1daaed24a1bb`</details> |
| `x_studio_gross_margin` | Gross Margin | monetary | Estimated Revenue minus Actual Expenses Incurred. | computed by `_compute_x_studio_gross_margin`; not stored | `crossovered.budget._compute_x_studio_gross_margin()` | `crossovered.budget._compute_x_studio_gross_margin()`<br>`crossovered.budget._compute_x_studio_gross_margin_percentage()`<br>`crossovered.budget._compute_x_studio_gross_margin_percentage_1()`<br>`crossovered.budget._compute_x_studio_percentage()`<br>`view BugFix-Accounting.ported_view_4942_odoo_studio_crossove_a555672e_6698_4232_9115_1daaed24a1bb` |
| `x_studio_gross_margin_percentage` | Gross Margin Percentage | monetary | Gross Margin as a percentage of Estimated Revenue (0 when revenue is 0), stored on a monetary field; duplicate of the float version. | computed by `_compute_x_studio_gross_margin_percentage`; not stored | `crossovered.budget._compute_x_studio_gross_margin_percentage()` | `crossovered.budget._compute_x_studio_gross_margin_percentage()`<br>`view BugFix-Accounting.ported_view_4942_odoo_studio_crossove_a555672e_6698_4232_9115_1daaed24a1bb` |
| `x_studio_gross_margin_percentage_1` | Gross Margin Percentage | float | Gross Margin as a percentage of Estimated Revenue (0 when revenue is 0). | computed by `_compute_x_studio_gross_margin_percentage_1`; not stored | `crossovered.budget._compute_x_studio_gross_margin_percentage_1()` | `crossovered.budget._compute_x_studio_gross_margin_percentage_1()`<br>`view BugFix-Accounting.ported_view_4942_odoo_studio_crossove_a555672e_6698_4232_9115_1daaed24a1bb` |
| `x_studio_percentage` | Percentage | char | Computed text field that is always empty (compute sets ''); kept for compatibility, no business effect. | computed by `_compute_x_studio_percentage`; not stored | `crossovered.budget._compute_x_studio_percentage()` | `crossovered.budget._compute_x_studio_percentage()` |
| `x_studio_project_completed_percentage` | Project Completed Percentage | monetary | Monetary field whose compute always returns 0; superseded by the float 'Project Completed Percentage' field. | computed by `_compute_x_studio_project_completed_percentage`; not stored | `crossovered.budget._compute_x_studio_project_completed_percentage()` | `crossovered.budget._compute_x_studio_project_completed_percentage()`<br>`view BugFix-Accounting.ported_view_4942_odoo_studio_crossove_a555672e_6698_4232_9115_1daaed24a1bb` |
| `x_studio_project_completed_percentage_1` | Project Completed Percentage | float | Project completion %: Actual Expenses Incurred divided by Total Project Expenses x 100 (0 when no planned expenses). | computed by `_compute_x_studio_project_completed_percentage_1`; not stored | `crossovered.budget._compute_x_studio_project_completed_percentage_1()` | `crossovered.budget._compute_x_studio_estimated_revenue_1()`<br>`crossovered.budget._compute_x_studio_project_completed_percentage_1()`<br>`view BugFix-Accounting.ported_view_4942_odoo_studio_crossove_a555672e_6698_4232_9115_1daaed24a1bb` |
| `x_studio_project_no` | Project No | many2one → `project.project` | Project the budget belongs to, entered on the budget form. | stored | `model project.project` (project) | `view BugFix-Accounting.ported_view_4942_odoo_studio_crossove_a555672e_6698_4232_9115_1daaed24a1bb` |
| `x_studio_project_value` | Project Value | monetary | Total planned amount of budget lines whose budgetary position is named 'Revenue'. | computed by `_compute_x_studio_project_value`; not stored | `crossovered.budget._compute_x_studio_project_value()` | `crossovered.budget._compute_x_studio_estimated_revenue_1()`<br>`crossovered.budget._compute_x_studio_project_value()`<br>`view BugFix-Accounting.ported_view_4942_odoo_studio_crossove_a555672e_6698_4232_9115_1daaed24a1bb` |
| `x_studio_spr_status` | SPR Status | boolean | True when the source sales order is a Project-type sub-contract order with no purchase request in 'Done' status (or the PR model is absent). | computed by `_compute_x_studio_spr_status`; not stored | `crossovered.budget._compute_x_studio_spr_status()` | `crossovered.budget._compute_x_studio_spr_status()`<br>`view BugFix-Accounting.ported_view_4942_odoo_studio_crossove_a555672e_6698_4232_9115_1daaed24a1bb` |
| `x_studio_total` | Total | integer | Integer total shown on the budget form (default from ir.default); not computed. | stored |  | `default BugFix-Accounting.default_573_crossovered_budget_x_studio_total`<br>`view BugFix-Accounting.ported_view_4942_odoo_studio_crossove_a555672e_6698_4232_9115_1daaed24a1bb` |
| `x_studio_total_project_expenses` | Total Project Expenses | monetary | Planned expenses: sum of planned amounts on 'Expenses' budget lines, sign-flipped to a positive figure. | computed by `_compute_x_studio_total_project_expenses`; not stored | `crossovered.budget._compute_x_studio_total_project_expenses()` | `crossovered.budget._compute_x_studio_project_completed_percentage_1()`<br>`crossovered.budget._compute_x_studio_total_project_expenses()`<br>`view BugFix-Accounting.ported_view_4942_odoo_studio_crossove_a555672e_6698_4232_9115_1daaed24a1bb` |
| `x_studio_valid_budget_lines` | Valid Budget Lines | boolean | True when the budget has at least one line and no line has a zero planned amount; checked by the 'Proj - Validate Confirm' action before confirming. | computed by `_compute_x_studio_valid_budget_lines`; not stored | `crossovered.budget._compute_x_studio_valid_budget_lines()` | `crossovered.budget._compute_x_studio_valid_budget_lines()`<br>`server action BugFix-Accounting.sa_f5_crossovered_budget_proj_validate_confirm`<br>`server action BugFix-Accounting.server_action_2570_proj_validate_confirm`<br>`view BugFix-Accounting.ported_view_4942_odoo_studio_crossove_a555672e_6698_4232_9115_1daaed24a1bb` |

**Python methods (14):**

| Method | Function | Decorators | Extends standard | Depends on | Used by | Where |
|---|---|---|---|---|---|---|
| `_compute_x_studio_percentage` | Compute for Percentage on budgets; always sets an empty string, so the field carries no value (placeholder). | api.depends('x_studio_gross_margin', 'x_studio_estimated_revenue_1') |  | `crossovered.budget.x_studio_estimated_revenue_1`<br>`crossovered.budget.x_studio_gross_margin`<br>`crossovered.budget.x_studio_percentage` | `crossovered.budget.x_studio_percentage` | `models/crossovered_budget.py:169` |
| `_compute_x_studio_project_completed_percentage` | Compute for Project Completed Percentage; always sets 0 (placeholder with no logic). |  |  | `crossovered.budget.x_studio_project_completed_percentage` | `crossovered.budget.x_studio_project_completed_percentage` | `models/crossovered_budget.py:173` |
| `_compute_x_studio_project_value` | Compute for Project Value: sums Planned Amount of budget lines whose budgetary position is named 'Revenue'. | api.depends('crossovered_budget_line') |  | `crossovered.budget.crossovered_budget_line` (account_budget)<br>`crossovered.budget.x_studio_project_value` | `crossovered.budget.x_studio_project_value` | `models/crossovered_budget.py:178` |
| `_compute_x_studio_total_project_expenses` | Compute for Total Project Expenses: negated sum of Planned Amount on budget lines whose budgetary position is 'Expenses' (gives a positive cost). | api.depends('crossovered_budget_line') |  | `crossovered.budget.crossovered_budget_line` (account_budget)<br>`crossovered.budget.x_studio_total_project_expenses` | `crossovered.budget.x_studio_total_project_expenses` | `models/crossovered_budget.py:187` |
| `_compute_x_studio_actual_invoiced_amount` | Compute for Actual Invoiced Amount: sums Practical (actual) Amount of 'Revenue' budget lines. | api.depends('crossovered_budget_line') |  | `crossovered.budget.crossovered_budget_line` (account_budget)<br>`crossovered.budget.x_studio_actual_invoiced_amount` | `crossovered.budget.x_studio_actual_invoiced_amount` | `models/crossovered_budget.py:196` |
| `_compute_x_studio_actual_expenses_incurred` | Compute for Actual Expenses Incurred: negated sum of Practical Amount on 'Expenses' budget lines. | api.depends('crossovered_budget_line') |  | `crossovered.budget.crossovered_budget_line` (account_budget)<br>`crossovered.budget.x_studio_actual_expenses_incurred` | `crossovered.budget.x_studio_actual_expenses_incurred` | `models/crossovered_budget.py:205` |
| `_compute_x_studio_estimated_revenue_1` | Compute for Estimated Revenue: Project Value multiplied by Project Completed Percentage (1) divided by 100. | api.depends('x_studio_project_completed_percentage_1', 'x_studio_project_value') |  | `crossovered.budget.x_studio_estimated_revenue_1`<br>`crossovered.budget.x_studio_project_completed_percentage_1`<br>`crossovered.budget.x_studio_project_value` | `crossovered.budget.x_studio_estimated_revenue_1` | `models/crossovered_budget.py:217` |
| `_compute_x_studio_gross_margin` | Compute for Gross Margin: Estimated Revenue minus Actual Expenses Incurred. | api.depends('x_studio_estimated_revenue_1', 'x_studio_actual_expenses_incurred') |  | `crossovered.budget.x_studio_actual_expenses_incurred`<br>`crossovered.budget.x_studio_estimated_revenue_1`<br>`crossovered.budget.x_studio_gross_margin` | `crossovered.budget.x_studio_gross_margin` | `models/crossovered_budget.py:228` |
| `_compute_x_studio_gross_margin_percentage` | Compute for Gross Margin Percentage: Gross Margin divided by Estimated Revenue times 100, or 0 when Estimated Revenue is not positive. | api.depends('x_studio_gross_margin', 'x_studio_estimated_revenue_1') |  | `crossovered.budget.x_studio_estimated_revenue_1`<br>`crossovered.budget.x_studio_gross_margin_percentage`<br>`crossovered.budget.x_studio_gross_margin` | `crossovered.budget.x_studio_gross_margin_percentage` | `models/crossovered_budget.py:236` |
| `_compute_x_studio_gross_margin_percentage_1` | Compute for Gross Margin Percentage (1): same formula as Gross Margin Percentage (Gross Margin / Estimated Revenue x 100, 0 if revenue not positive). | api.depends('x_studio_gross_margin', 'x_studio_estimated_revenue_1') |  | `crossovered.budget.x_studio_estimated_revenue_1`<br>`crossovered.budget.x_studio_gross_margin_percentage_1`<br>`crossovered.budget.x_studio_gross_margin` | `crossovered.budget.x_studio_gross_margin_percentage_1` | `models/crossovered_budget.py:245` |
| `_compute_x_studio_project_completed_percentage_1` | Compute for Project Completed Percentage (1): Actual Expenses Incurred divided by Total Project Expenses times 100, or 0 when total expenses are not positive. | api.depends('x_studio_actual_expenses_incurred', 'x_studio_total_project_expense… |  | `crossovered.budget.x_studio_actual_expenses_incurred`<br>`crossovered.budget.x_studio_project_completed_percentage_1`<br>`crossovered.budget.x_studio_total_project_expenses` | `crossovered.budget.x_studio_project_completed_percentage_1` | `models/crossovered_budget.py:257` |
| `_compute_x_studio_confirm_status` | Compute for Confirm Status: True when the source sales order is a Project, inventory-short SO whose purchase requests still have outstanding quantities (or none exist / PR model absent). | api.depends('x_studio_created_from_sales_order_1.x_studio_quotation_type', 'x_st… |  | `crossovered.budget.x_studio_confirm_status`<br>`crossovered.budget.x_studio_created_from_sales_order_1`<br>`sale.order.x_studio_inventory_short` (BugFix-Sales)<br>`sale.order.x_studio_quotation_type` (BugFix-Sales) | `crossovered.budget.x_studio_confirm_status` | `models/crossovered_budget.py:269` |
| `_compute_x_studio_spr_status` | Compute for SPR Status: True when the source sales order is a Project sub-contract SO with no purchase request in 'Done' state (or PR model absent). | api.depends('x_studio_created_from_sales_order_1') |  | `crossovered.budget.x_studio_created_from_sales_order_1`<br>`crossovered.budget.x_studio_spr_status` | `crossovered.budget.x_studio_spr_status` | `models/crossovered_budget.py:303` |
| `_compute_x_studio_valid_budget_lines` | Compute for Valid Budget Lines: True only if the budget has at least one line and no line has a Planned Amount of 0. | api.depends('crossovered_budget_line') |  | `crossovered.budget.crossovered_budget_line` (account_budget)<br>`crossovered.budget.x_studio_valid_budget_lines` | `crossovered.budget.x_studio_valid_budget_lines` | `models/crossovered_budget.py:326` |

**Server actions (4):**

- **Execute Code** (`server_action_2183_proj_validate_delete`, type `code`)
  - Function: Run on budget deletion: blocks deleting budgets that were created from a sales order.
  - Depends on: `crossovered.budget.x_studio_created_from_sales_order_1`, `model crossovered.budget` (account_budget)
  - Used by: `automation BugFix-Accounting.base_automation_197_proj_validate_delete`
  <details><summary>code (3 lines)</summary>

```python

if record.x_studio_created_from_sales_order_1.id != False:
  raise UserError('Budgets created from SOs can not be deleted.')
```
  </details>
- **Execute Code** (`server_action_2570_proj_validate_confirm`, type `code`)
  - Function: Run on budget confirmation: blocks if Valid Budget Lines is false. The follow-up 'finalize related RFQs' check sits after the raise and never runs (dead code).
  - Depends on: `crossovered.budget.state` (account_budget), `crossovered.budget.x_studio_confirm_status`, `crossovered.budget.x_studio_created_from_sales_order_1`, `crossovered.budget.x_studio_valid_budget_lines`, `model crossovered.budget` (account_budget)
  - Used by: `automation BugFix-Accounting.base_automation_256_proj_validate_confirm`
  <details><summary>code (10 lines)</summary>

```python

if record.state == 'confirm':
  """if record.x_studio_created_from_sales_order_1.id != False:
    if record.x_studio_valid_budget_lines == False:
      raise UserError('At least one budget line should be available with value greater than zero when confirming.')"""
  if record.x_studio_valid_budget_lines == False:
    raise UserError('At least one budget line should be available with value greater than zero when confirming.')
      
    if record.x_studio_confirm_status == True:
      raise UserError('Please finalize all the related RFQs.')
```
  </details>
- **PROJ - Validate Confirm** (`sa_f5_crossovered_budget_proj_validate_confirm`, type `code`)
  - Function: When a budget is confirmed, blocks if Valid Budget Lines is false (needs at least one non-zero line). The 'finalize related RFQs' check is unreachable dead code placed after the raise.
  - Depends on: `crossovered.budget.state` (account_budget), `crossovered.budget.x_studio_confirm_status`, `crossovered.budget.x_studio_created_from_sales_order_1`, `crossovered.budget.x_studio_valid_budget_lines`, `model crossovered.budget` (account_budget)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (9 lines)</summary>

```python
if record.state == 'confirm':
  """if record.x_studio_created_from_sales_order_1.id != False:
    if record.x_studio_valid_budget_lines == False:
      raise UserError('At least one budget line should be available with value greater than zero when confirming.')"""
  if record.x_studio_valid_budget_lines == False:
    raise UserError('At least one budget line should be available with value greater than zero when confirming.')
      
    if record.x_studio_confirm_status == True:
      raise UserError('Please finalize all the related RFQs.')
```
  </details>
- **PROJ - Validate Delete** (`sa_f5_crossovered_budget_proj_validate_delete`, type `code`)
  - Function: Blocks deletion of budgets created from a sales order ('Budgets created from SOs can not be deleted').
  - Depends on: `crossovered.budget.x_studio_created_from_sales_order_1`, `model crossovered.budget` (account_budget)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (2 lines)</summary>

```python
if record.x_studio_created_from_sales_order_1.id != False:
  raise UserError('Budgets created from SOs can not be deleted.')
```
  </details>
**Automations (2):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| PROJ - Validate Confirm | `base_automation_256_proj_validate_confirm` |  | When a record is created or updated on Budget, runs _Execute Code_. | `model crossovered.budget` (account_budget)<br>`server action BugFix-Accounting.server_action_2570_proj_validate_confirm` |  |
| PROJ - Validate Delete | `base_automation_197_proj_validate_delete` |  | When a record is deleted on Budget, runs _Execute Code_. | `model crossovered.budget` (account_budget)<br>`server action BugFix-Accounting.server_action_2183_proj_validate_delete` |  |

**Window actions (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Budget | `aw_f4_crossovered_budget_budget` | Opens **Budget** records (tree,form), filtered to `[('x_studio_created_from_sales_order_1', '=', active_id)]`. | `crossovered.budget.x_studio_created_from_sales_order_1`<br>`model crossovered.budget` (account_budget) |  |
| Budget | `action_2180_budget` | Opens **Budget** records (tree,form), filtered to `[('x_studio_created_from_sales_order_1', '=', active_id)]`. | `crossovered.budget.x_studio_created_from_sales_order_1`<br>`model crossovered.budget` (account_budget) |  |
| Budget | `act_window_2180_budget` | Opens **Budget** records (tree,form), filtered to `[('x_studio_created_from_sales_order_1', '=', active_id)]`. | `crossovered.budget.x_studio_created_from_sales_order_1`<br>`model crossovered.budget` (account_budget) | `view BugFix-Accounting.ported_odoo_studio_sale_ord_acct` |

**Views (2):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: crossovered.budget.view.form customization | `ported_view_4942_odoo_studio_crossove_a555672e_6698_4232_9115_1daaed24a1bb` | form | set create=false, delete=true on `//form[1]`; set invisible=((state != 'confirm') or ((state != 'confirm') or (x_studio_spr_status == True))) or (state not in ['False']) on `//button[@name='action_budget_validate']`; set readonly=(state != 'draft') or ((x_studio_created_from_sales_order_1 != False) or (state != 'draft')) on `//form[1]/sheet[1]/div[1]/h1[1]/field[@name='name']`; after `//field[@name='user_id']`: add field x_studio_analytic_account, field x_studio_project_no, field x_studio_created_from_sales_order_1, field x_studio_confirm_validation, field x_studio_spr_status; before `//form[1]/sheet[1]/group[1]/group[2]/label[1]`: add field x_studio_total, field x_studio_confirm_status, field x_studio_valid_budget_lines; before `//form[1]/sheet[1]/notebook[1]/page[@name='budget_lines']/field[@name='crossovered_budget_line']/tree[1]/field[@name='general_budget_id']`: add field crossovered_budget_id; set readonly=parent.x_studio_analytic_account != False on `//form[1]/sheet[1]/notebook[1]/page[@name='budget_lines']/field[@name='crossovered_budget_line']/tree[1]/field[@name='analytic_account_id']`; after `//field[@name='theoritical_amount']`: add field x_studio_estimate … | Budget form customization: disables create, makes name read-only for budgets created from a sales order, adds Analytic Account, Project No, totals and validation flags, locks line analytic accounts when the header has one, adds Estimate per line and a hidden 'Estimate Run' tab. Its Approve-button condition effectively always hides that button. | `crossovered.budget.x_currency_id`<br>`crossovered.budget.x_studio_actual_expenses_incurred`<br>`crossovered.budget.x_studio_actual_invoiced_amount`<br>`crossovered.budget.x_studio_analytic_account`<br>`crossovered.budget.x_studio_confirm_status`<details><summary>+15 more</summary>`crossovered.budget.x_studio_confirm_validation`<br>`crossovered.budget.x_studio_created_from_sales_order_1`<br>`crossovered.budget.x_studio_estimated_revenue_1`<br>`crossovered.budget.x_studio_gross_margin_percentage_1`<br>`crossovered.budget.x_studio_gross_margin_percentage`<br>`crossovered.budget.x_studio_gross_margin`<br>`crossovered.budget.x_studio_project_completed_percentage_1`<br>`crossovered.budget.x_studio_project_completed_percentage`<br>`crossovered.budget.x_studio_project_no`<br>`crossovered.budget.x_studio_project_value`<br>`crossovered.budget.x_studio_spr_status`<br>`crossovered.budget.x_studio_total_project_expenses`<br>`crossovered.budget.x_studio_total`<br>`crossovered.budget.x_studio_valid_budget_lines`<br>`view account_budget.crossovered_budget_view_form` (account_budget)</details> |  |
| Odoo Studio: crossovered.budget.view.tree customization | `ported_view_5912_odoo_studio_crossove_b4e03115_c663_4324_8258_dcddf1e8a51d` | tree | set create=true on `//tree[1]` | Enables the Create button on the Budgets list. | `view account_budget.crossovered_budget_view_tree` (account_budget) |  |

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| crossovered.budget | `access_6854_crossovered_budget` | Gives **Sales / Jin - Sales - POS Users** read access to Budget records. | `group BugFix-Approvals.group_132_jin_sales_pos_users` (BugFix-Approvals)<br>`model crossovered.budget` (account_budget) |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Budget multi-company | `rule_331_budget_multi_company` | For everyone (global rule): read/write/create/delete on Budget only where `[('company_id', 'in', company_ids)]`. | `crossovered.budget.company_id` (account_budget)<br>`model crossovered.budget` (account_budget) |  |
