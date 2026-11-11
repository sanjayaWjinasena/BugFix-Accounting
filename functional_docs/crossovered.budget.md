# BugFix-Accounting — `crossovered.budget`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `crossovered.budget` — Budget

*Extends a model created by `account_budget`.* Python: `models/crossovered_budget.py`, `models/crossovered_budget_gap.py`.

Other repos that use this model: `report BugFix-Studio-Misc.report_budget_report` (BugFix-Studio-Misc)<br>`sale.order.project_budget` (BugFix-Sales)<br>`server action BugFix-Sales.action_proj_create_budget_entries` (BugFix-Sales)

**Summary:**

<!-- SUMMARY:model:crossovered.budget -->
This repo adds 20 fields and their computes to budgets for project budgeting. The fields cover the analytic account, project number, source sales order, project value, planned and actual expenses, actual invoiced amount, completion %, estimated revenue, gross margin and its %, and Confirm/SPR status flags based on the sales order's purchase requests. Automations block confirming a budget without valid non-zero lines and block deleting budgets created from a sales order. The customized budget form disables create, adds these figures and locks line analytic accounts. The repo also adds Budget window actions filtered by sales order.
<!-- /SUMMARY -->

**Fields (20):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `currency_id` | Currency | many2one → `res.currency` | Currency of the budget's monetary fields, defaulted by an ir.default record. | stored | `model res.currency` (base) | `default BugFix-Accounting.default_574_crossovered_budget_currency_id`<br>`view BugFix-Accounting.view_crossovered_budget_view_form_inherit` |
| `actual_expenses_incurred` | Actual Expenses Incurred | monetary | Actual expenses: sum of practical amounts on 'Expenses' budget lines, sign-flipped to a positive figure. | computed by `_compute_actual_expenses_incurred`; not stored | `crossovered.budget._compute_actual_expenses_incurred()` | `crossovered.budget._compute_actual_expenses_incurred()`<br>`crossovered.budget._compute_gross_margin()`<br>`crossovered.budget._compute_project_completed_percentage_1()`<br>`view BugFix-Accounting.view_crossovered_budget_view_form_inherit` |
| `actual_invoiced_amount` | Actual Invoiced Amount | monetary | Actual revenue: sum of practical (actual) amounts on 'Revenue' budget lines. | computed by `_compute_actual_invoiced_amount`; not stored | `crossovered.budget._compute_actual_invoiced_amount()` | `crossovered.budget._compute_actual_invoiced_amount()`<br>`view BugFix-Accounting.view_crossovered_budget_view_form_inherit` |
| `analytic_account` | Analytic Account | many2one → `account.analytic.account` | Analytic account the budget is for, entered on the budget form. | stored | `model account.analytic.account` (analytic) | `view BugFix-Accounting.view_crossovered_budget_view_form_inherit` |
| `confirm_status` | Confirm Status | boolean | True when the source sales order is a Project-type, inventory-short order whose purchase requests still have outstanding quantities, or that has no purchase request (or the PR model is absent). | computed by `_compute_confirm_status`; not stored | `crossovered.budget._compute_confirm_status()` | `crossovered.budget._compute_confirm_status()`<br>`server action BugFix-Accounting.action_crossovered_budget_proj_validate_confirm`<br>`server action BugFix-Accounting.action_proj_validate_confirm`<br>`view BugFix-Accounting.view_crossovered_budget_view_form_inherit` |
| `confirm_validation` | Confirm Validation | text | Text field on the budget form (default from ir.default); no logic in this repo reads it. | stored |  | `default BugFix-Accounting.default_crossovered_budget_confirm_validation`<br>`view BugFix-Accounting.view_crossovered_budget_view_form_inherit` |
| `created_from_sales_order_1` | Created From Sales Order | many2one → `sale.order` | Sales order the project budget was created from. Drives Confirm Status and SPR Status, and the 'Proj - Validate Confirm/Delete' checks. | stored | `model sale.order` (sale) | `crossovered.budget._compute_confirm_status()`<br>`crossovered.budget._compute_spr_status()`<br>`server action BugFix-Accounting.action_crossovered_budget_proj_validate_confirm`<br>`server action BugFix-Accounting.action_crossovered_budget_proj_validate_delete`<br>`server action BugFix-Accounting.action_proj_validate_delete`<details><summary>+5 more</summary>`server action BugFix-Accounting.action_proj_validate_confirm`<br>`view BugFix-Accounting.view_crossovered_budget_view_form_inherit`<br>`window action BugFix-Accounting.action_budget_2`<br>`window action BugFix-Accounting.action_budget`<br>`window action BugFix-Accounting.aw_f4_crossovered_budget_budget`</details> |
| `estimated_revenue_1` | Estimated Revenue | monetary | Revenue earned to date estimated as Project Value x Project Completed Percentage. | computed by `_compute_estimated_revenue_1`; not stored | `crossovered.budget._compute_estimated_revenue_1()` | `crossovered.budget._compute_estimated_revenue_1()`<br>`crossovered.budget._compute_gross_margin()`<br>`crossovered.budget._compute_gross_margin_percentage()`<br>`crossovered.budget._compute_gross_margin_percentage_1()`<br>`crossovered.budget._compute_percentage()`<details><summary>+1 more</summary>`view BugFix-Accounting.view_crossovered_budget_view_form_inherit`</details> |
| `gross_margin` | Gross Margin | monetary | Estimated Revenue minus Actual Expenses Incurred. | computed by `_compute_gross_margin`; not stored | `crossovered.budget._compute_gross_margin()` | `crossovered.budget._compute_gross_margin()`<br>`crossovered.budget._compute_gross_margin_percentage()`<br>`crossovered.budget._compute_gross_margin_percentage_1()`<br>`crossovered.budget._compute_percentage()`<br>`view BugFix-Accounting.view_crossovered_budget_view_form_inherit` |
| `gross_margin_percentage` | Gross Margin Percentage | monetary | Gross Margin as a percentage of Estimated Revenue (0 when revenue is 0), stored on a monetary field; duplicate of the float version. | computed by `_compute_gross_margin_percentage`; not stored | `crossovered.budget._compute_gross_margin_percentage()` | `crossovered.budget._compute_gross_margin_percentage()`<br>`view BugFix-Accounting.view_crossovered_budget_view_form_inherit` |
| `gross_margin_percentage_1` | Gross Margin Percentage | float | Gross Margin as a percentage of Estimated Revenue (0 when revenue is 0). | computed by `_compute_gross_margin_percentage_1`; not stored | `crossovered.budget._compute_gross_margin_percentage_1()` | `crossovered.budget._compute_gross_margin_percentage_1()`<br>`view BugFix-Accounting.view_crossovered_budget_view_form_inherit` |
| `percentage` | Percentage | char | Computed text field that is always empty (compute sets ''); kept for compatibility, no business effect. | computed by `_compute_percentage`; not stored | `crossovered.budget._compute_percentage()` | `crossovered.budget._compute_percentage()` |
| `project_completed_percentage` | Project Completed Percentage | monetary | Monetary field whose compute always returns 0; superseded by the float 'Project Completed Percentage' field. | computed by `_compute_project_completed_percentage`; not stored | `crossovered.budget._compute_project_completed_percentage()` | `crossovered.budget._compute_project_completed_percentage()`<br>`view BugFix-Accounting.view_crossovered_budget_view_form_inherit` |
| `project_completed_percentage_1` | Project Completed Percentage | float | Project completion %: Actual Expenses Incurred divided by Total Project Expenses x 100 (0 when no planned expenses). | computed by `_compute_project_completed_percentage_1`; not stored | `crossovered.budget._compute_project_completed_percentage_1()` | `crossovered.budget._compute_estimated_revenue_1()`<br>`crossovered.budget._compute_project_completed_percentage_1()`<br>`view BugFix-Accounting.view_crossovered_budget_view_form_inherit` |
| `project_no` | Project No | many2one → `project.project` | Project the budget belongs to, entered on the budget form. | stored | `model project.project` (project) | `view BugFix-Accounting.view_crossovered_budget_view_form_inherit` |
| `project_value` | Project Value | monetary | Total planned amount of budget lines whose budgetary position is named 'Revenue'. | computed by `_compute_project_value`; not stored | `crossovered.budget._compute_project_value()` | `crossovered.budget._compute_estimated_revenue_1()`<br>`crossovered.budget._compute_project_value()`<br>`view BugFix-Accounting.view_crossovered_budget_view_form_inherit` |
| `spr_status` | SPR Status | boolean | True when the source sales order is a Project-type sub-contract order with no purchase request in 'Done' status (or the PR model is absent). | computed by `_compute_spr_status`; not stored | `crossovered.budget._compute_spr_status()` | `crossovered.budget._compute_spr_status()`<br>`view BugFix-Accounting.view_crossovered_budget_view_form_inherit` |
| `total` | Total | integer | Integer total shown on the budget form (default from ir.default); not computed. | stored |  | `default BugFix-Accounting.default_573_crossovered_budget_total`<br>`view BugFix-Accounting.view_crossovered_budget_view_form_inherit` |
| `total_project_expenses` | Total Project Expenses | monetary | Planned expenses: sum of planned amounts on 'Expenses' budget lines, sign-flipped to a positive figure. | computed by `_compute_total_project_expenses`; not stored | `crossovered.budget._compute_total_project_expenses()` | `crossovered.budget._compute_project_completed_percentage_1()`<br>`crossovered.budget._compute_total_project_expenses()`<br>`view BugFix-Accounting.view_crossovered_budget_view_form_inherit` |
| `valid_budget_lines` | Valid Budget Lines | boolean | True when the budget has at least one line and no line has a zero planned amount; checked by the 'Proj - Validate Confirm' action before confirming. | computed by `_compute_valid_budget_lines`; not stored | `crossovered.budget._compute_valid_budget_lines()` | `crossovered.budget._compute_valid_budget_lines()`<br>`server action BugFix-Accounting.action_crossovered_budget_proj_validate_confirm`<br>`server action BugFix-Accounting.action_proj_validate_confirm`<br>`view BugFix-Accounting.view_crossovered_budget_view_form_inherit` |

**Python methods (14):**

| Method | Function | Decorators | Extends standard | Depends on | Used by | Where |
|---|---|---|---|---|---|---|
| `_compute_percentage` | Compute for Percentage on budgets; always sets an empty string, so the field carries no value (placeholder). | api.depends('gross_margin', 'estimated_revenue_1') |  | `crossovered.budget.estimated_revenue_1`<br>`crossovered.budget.gross_margin`<br>`crossovered.budget.percentage` | `crossovered.budget.percentage` | `models/crossovered_budget.py:169` |
| `_compute_project_completed_percentage` | Compute for Project Completed Percentage; always sets 0 (placeholder with no logic). |  |  | `crossovered.budget.project_completed_percentage` | `crossovered.budget.project_completed_percentage` | `models/crossovered_budget.py:173` |
| `_compute_project_value` | Compute for Project Value: sums Planned Amount of budget lines whose budgetary position is named 'Revenue'. | api.depends('crossovered_budget_line') |  | `crossovered.budget.crossovered_budget_line` (account_budget)<br>`crossovered.budget.project_value` | `crossovered.budget.project_value` | `models/crossovered_budget.py:178` |
| `_compute_total_project_expenses` | Compute for Total Project Expenses: negated sum of Planned Amount on budget lines whose budgetary position is 'Expenses' (gives a positive cost). | api.depends('crossovered_budget_line') |  | `crossovered.budget.crossovered_budget_line` (account_budget)<br>`crossovered.budget.total_project_expenses` | `crossovered.budget.total_project_expenses` | `models/crossovered_budget.py:187` |
| `_compute_actual_invoiced_amount` | Compute for Actual Invoiced Amount: sums Practical (actual) Amount of 'Revenue' budget lines. | api.depends('crossovered_budget_line') |  | `crossovered.budget.crossovered_budget_line` (account_budget)<br>`crossovered.budget.actual_invoiced_amount` | `crossovered.budget.actual_invoiced_amount` | `models/crossovered_budget.py:196` |
| `_compute_actual_expenses_incurred` | Compute for Actual Expenses Incurred: negated sum of Practical Amount on 'Expenses' budget lines. | api.depends('crossovered_budget_line') |  | `crossovered.budget.crossovered_budget_line` (account_budget)<br>`crossovered.budget.actual_expenses_incurred` | `crossovered.budget.actual_expenses_incurred` | `models/crossovered_budget.py:205` |
| `_compute_estimated_revenue_1` | Compute for Estimated Revenue: Project Value multiplied by Project Completed Percentage (1) divided by 100. | api.depends('project_completed_percentage_1', 'project_value') |  | `crossovered.budget.estimated_revenue_1`<br>`crossovered.budget.project_completed_percentage_1`<br>`crossovered.budget.project_value` | `crossovered.budget.estimated_revenue_1` | `models/crossovered_budget.py:217` |
| `_compute_gross_margin` | Compute for Gross Margin: Estimated Revenue minus Actual Expenses Incurred. | api.depends('estimated_revenue_1', 'actual_expenses_incurred') |  | `crossovered.budget.actual_expenses_incurred`<br>`crossovered.budget.estimated_revenue_1`<br>`crossovered.budget.gross_margin` | `crossovered.budget.gross_margin` | `models/crossovered_budget.py:228` |
| `_compute_gross_margin_percentage` | Compute for Gross Margin Percentage: Gross Margin divided by Estimated Revenue times 100, or 0 when Estimated Revenue is not positive. | api.depends('gross_margin', 'estimated_revenue_1') |  | `crossovered.budget.estimated_revenue_1`<br>`crossovered.budget.gross_margin_percentage`<br>`crossovered.budget.gross_margin` | `crossovered.budget.gross_margin_percentage` | `models/crossovered_budget.py:236` |
| `_compute_gross_margin_percentage_1` | Compute for Gross Margin Percentage (1): same formula as Gross Margin Percentage (Gross Margin / Estimated Revenue x 100, 0 if revenue not positive). | api.depends('gross_margin', 'estimated_revenue_1') |  | `crossovered.budget.estimated_revenue_1`<br>`crossovered.budget.gross_margin_percentage_1`<br>`crossovered.budget.gross_margin` | `crossovered.budget.gross_margin_percentage_1` | `models/crossovered_budget.py:245` |
| `_compute_project_completed_percentage_1` | Compute for Project Completed Percentage (1): Actual Expenses Incurred divided by Total Project Expenses times 100, or 0 when total expenses are not positive. | api.depends('actual_expenses_incurred', 'x_studio_total_project_expense… |  | `crossovered.budget.actual_expenses_incurred`<br>`crossovered.budget.project_completed_percentage_1`<br>`crossovered.budget.total_project_expenses` | `crossovered.budget.project_completed_percentage_1` | `models/crossovered_budget.py:257` |
| `_compute_confirm_status` | Compute for Confirm Status: True when the source sales order is a Project, inventory-short SO whose purchase requests still have outstanding quantities (or none exist / PR model absent). | api.depends('created_from_sales_order_1.quotation_type', 'x_st… |  | `crossovered.budget.confirm_status`<br>`crossovered.budget.created_from_sales_order_1`<br>`sale.order.inventory_short` (BugFix-Sales)<br>`sale.order.quotation_type` (BugFix-Sales) | `crossovered.budget.confirm_status` | `models/crossovered_budget.py:269` |
| `_compute_spr_status` | Compute for SPR Status: True when the source sales order is a Project sub-contract SO with no purchase request in 'Done' state (or PR model absent). | api.depends('created_from_sales_order_1') |  | `crossovered.budget.created_from_sales_order_1`<br>`crossovered.budget.spr_status` | `crossovered.budget.spr_status` | `models/crossovered_budget.py:303` |
| `_compute_valid_budget_lines` | Compute for Valid Budget Lines: True only if the budget has at least one line and no line has a Planned Amount of 0. | api.depends('crossovered_budget_line') |  | `crossovered.budget.crossovered_budget_line` (account_budget)<br>`crossovered.budget.valid_budget_lines` | `crossovered.budget.valid_budget_lines` | `models/crossovered_budget.py:326` |

**Server actions (4):**

- **Execute Code** (`action_proj_validate_delete`, type `code`)
  - Function: Run on budget deletion: blocks deleting budgets that were created from a sales order.
  - Depends on: `crossovered.budget.created_from_sales_order_1`, `model crossovered.budget` (account_budget)
  - Used by: `automation BugFix-Accounting.automation_proj_validate_delete`
  <details><summary>code (3 lines)</summary>

```python
if record.created_from_sales_order_1.id != False:
    raise UserError("Budgets created from SOs can not be deleted.")
```
  </details>
- **Execute Code** (`action_proj_validate_confirm`, type `code`)
  - Function: Run on budget confirmation: blocks if Valid Budget Lines is false. The follow-up 'finalize related RFQs' check sits after the raise and never runs (dead code).
  - Depends on: `crossovered.budget.state` (account_budget), `crossovered.budget.confirm_status`, `crossovered.budget.created_from_sales_order_1`, `crossovered.budget.valid_budget_lines`, `model crossovered.budget` (account_budget)
  - Used by: `automation BugFix-Accounting.automation_proj_validate_confirm`
  <details><summary>code (10 lines)</summary>

```python
if record.state == "confirm":
    """if record.created_from_sales_order_1.id != False:
    if record.valid_budget_lines == False:
      raise UserError('At least one budget line should be available with value greater than zero when confirming.')"""
    if record.valid_budget_lines == False:
        raise UserError(
            "At least one budget line should be available with value greater than zero when confirming."
        )

        if record.confirm_status == True:
            raise UserError("Please finalize all the related RFQs.")
```
  </details>
- **PROJ - Validate Confirm** (`action_crossovered_budget_proj_validate_confirm`, type `code`)
  - Function: When a budget is confirmed, blocks if Valid Budget Lines is false (needs at least one non-zero line). The 'finalize related RFQs' check is unreachable dead code placed after the raise.
  - Depends on: `crossovered.budget.state` (account_budget), `crossovered.budget.confirm_status`, `crossovered.budget.created_from_sales_order_1`, `crossovered.budget.valid_budget_lines`, `model crossovered.budget` (account_budget)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (9 lines)</summary>

```python
if record.state == "confirm":
    """if record.created_from_sales_order_1.id != False:
    if record.valid_budget_lines == False:
      raise UserError('At least one budget line should be available with value greater than zero when confirming.')"""
    if record.valid_budget_lines == False:
        raise UserError(
            "At least one budget line should be available with value greater than zero when confirming."
        )

        if record.confirm_status == True:
            raise UserError("Please finalize all the related RFQs.")
```
  </details>
- **PROJ - Validate Delete** (`action_crossovered_budget_proj_validate_delete`, type `code`)
  - Function: Blocks deletion of budgets created from a sales order ('Budgets created from SOs can not be deleted').
  - Depends on: `crossovered.budget.created_from_sales_order_1`, `model crossovered.budget` (account_budget)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (2 lines)</summary>

```python
if record.created_from_sales_order_1.id != False:
    raise UserError("Budgets created from SOs can not be deleted.")
```
  </details>
**Automations (2):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| PROJ - Validate Confirm | `automation_proj_validate_confirm` |  | When a record is created or updated on Budget, runs _Execute Code_. | `model crossovered.budget` (account_budget)<br>`server action BugFix-Accounting.action_proj_validate_confirm` |  |
| PROJ - Validate Delete | `automation_proj_validate_delete` |  | When a record is deleted on Budget, runs _Execute Code_. | `model crossovered.budget` (account_budget)<br>`server action BugFix-Accounting.action_proj_validate_delete` |  |

**Window actions (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Budget | `aw_f4_crossovered_budget_budget` | Opens **Budget** records (tree,form), filtered to `[('created_from_sales_order_1', '=', active_id)]`. | `crossovered.budget.created_from_sales_order_1`<br>`model crossovered.budget` (account_budget) |  |
| Budget | `action_budget` | Opens **Budget** records (tree,form), filtered to `[('created_from_sales_order_1', '=', active_id)]`. | `crossovered.budget.created_from_sales_order_1`<br>`model crossovered.budget` (account_budget) |  |
| Budget | `action_budget_2` | Opens **Budget** records (tree,form), filtered to `[('created_from_sales_order_1', '=', active_id)]`. | `crossovered.budget.created_from_sales_order_1`<br>`model crossovered.budget` (account_budget) | `view BugFix-Accounting.view_ported_sale_ord_acct` |

**Views (2):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: crossovered.budget.view.form customization | `view_crossovered_budget_view_form_inherit` | form | set create=false, delete=true on `//form[1]`; set invisible=((state != 'confirm') or ((state != 'confirm') or (spr_status == True))) or (state not in ['False']) on `//button[@name='action_budget_validate']`; set readonly=(state != 'draft') or ((created_from_sales_order_1 != False) or (state != 'draft')) on `//form[1]/sheet[1]/div[1]/h1[1]/field[@name='name']`; after `//field[@name='user_id']`: add field analytic_account, field project_no, field created_from_sales_order_1, field confirm_validation, field spr_status; before `//form[1]/sheet[1]/group[1]/group[2]/label[1]`: add field total, field confirm_status, field valid_budget_lines; before `//form[1]/sheet[1]/notebook[1]/page[@name='budget_lines']/field[@name='crossovered_budget_line']/tree[1]/field[@name='general_budget_id']`: add field crossovered_budget_id; set readonly=parent.analytic_account != False on `//form[1]/sheet[1]/notebook[1]/page[@name='budget_lines']/field[@name='crossovered_budget_line']/tree[1]/field[@name='analytic_account_id']`; after `//field[@name='theoritical_amount']`: add field estimate … | Budget form customization: disables create, makes name read-only for budgets created from a sales order, adds Analytic Account, Project No, totals and validation flags, locks line analytic accounts when the header has one, adds Estimate per line and a hidden 'Estimate Run' tab. Its Approve-button condition effectively always hides that button. | `crossovered.budget.currency_id`<br>`crossovered.budget.actual_expenses_incurred`<br>`crossovered.budget.actual_invoiced_amount`<br>`crossovered.budget.analytic_account`<br>`crossovered.budget.confirm_status`<details><summary>+15 more</summary>`crossovered.budget.confirm_validation`<br>`crossovered.budget.created_from_sales_order_1`<br>`crossovered.budget.estimated_revenue_1`<br>`crossovered.budget.gross_margin_percentage_1`<br>`crossovered.budget.gross_margin_percentage`<br>`crossovered.budget.gross_margin`<br>`crossovered.budget.project_completed_percentage_1`<br>`crossovered.budget.project_completed_percentage`<br>`crossovered.budget.project_no`<br>`crossovered.budget.project_value`<br>`crossovered.budget.spr_status`<br>`crossovered.budget.total_project_expenses`<br>`crossovered.budget.total`<br>`crossovered.budget.valid_budget_lines`<br>`view account_budget.crossovered_budget_view_form` (account_budget)</details> |  |
| Odoo Studio: crossovered.budget.view.tree customization | `view_crossovered_budget_view_tree_inherit` | tree | set create=true on `//tree[1]` | Enables the Create button on the Budgets list. | `view account_budget.crossovered_budget_view_tree` (account_budget) |  |

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| crossovered.budget | `access_crossovered_budget` | Gives **Sales / Jin - Sales - POS Users** read access to Budget records. | `group BugFix-Approvals.group_jin_sales_pos_users` (BugFix-Approvals)<br>`model crossovered.budget` (account_budget) |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Budget multi-company | `rule_budget_multi_company` | For everyone (global rule): read/write/create/delete on Budget only where `[('company_id', 'in', company_ids)]`. | `crossovered.budget.company_id` (account_budget)<br>`model crossovered.budget` (account_budget) |  |
