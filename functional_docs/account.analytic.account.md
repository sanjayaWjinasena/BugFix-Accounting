# BugFix-Accounting — `account.analytic.account`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.analytic.account` — Analytic Account

*Extends a model created by `analytic`.*

Other repos that use this model: `record rule BugFix-Analytics.rule_63_analytic_multi_company_rule` (BugFix-Analytics)<br>`sale.order.line._bugfix_analytics_resolve_account()` (BugFix-Analytics)<br>`server action BugFix-Sales.server_action_2178_proj_create_budget_entries` (BugFix-Sales)<br>`stock.picking.x_studio_analytic_account` (BugFix-Analytics)<br>`window action BugFix-Analytics.act_window_2333_analytic_account` (BugFix-Analytics)<br>`window action BugFix-Analytics.act_window_3276_account_analytic_account` (BugFix-Analytics)<br>`x_work_center_costing.x_studio_general_analytic_tag` (BugFix-Studio-Misc)<br>`x_work_center_costing.x_studio_labour_analytic_tag` (BugFix-Studio-Misc)<details><summary>+1 more</summary>`x_work_center_costing.x_studio_overhead_analytic_tag` (BugFix-Studio-Misc)</details>

**Summary:**

<!-- SUMMARY:model:account.analytic.account -->
This repo adds no fields to analytic accounts. It adds an optional record ID column to the Analytic Accounts list and two window actions, one of them filtered to a single analytic plan. It also ships two empty test server actions ('test-to delete' and 'test2') that do nothing.
<!-- /SUMMARY -->

**Server actions (2):**

- **test-to delete** (`server_action_1704_test_to_delete`, type `code`)
  - Function: Empty test action on analytic accounts named 'test-to delete'; contains no code and does nothing.
  - Depends on: `model account.analytic.account` (analytic)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (0 lines)</summary>

```python

```
  </details>
- **test2** (`server_action_1706_test2`, type `object_write`)
  - Function: Test 'update record' action on analytic accounts with no field or value configured; does nothing and is not used anywhere.
  - Depends on: `model account.analytic.account` (analytic)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
**Window actions (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Analytic Account | `action_2333_analytic_account` | Opens **Analytic Account** records (tree,form), filtered to `[('plan_id', '=', active_id)]`. | `account.analytic.account.plan_id` (analytic)<br>`model account.analytic.account` (analytic) | `view BugFix-Accounting.view_5073_odoo_studio_account_analytic_group_form_customization_e` |
| account.analytic.account | `action_3276_account_analytic_account` | Opens **Analytic Account** records (kanban,tree,form). | `model account.analytic.account` (analytic) |  |

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: account.analytic.account.list customization | `ported_view_5075_customization_account_analytic_account_tree` | tree | after `//field[@name='balance']`: add field id | Adds an optional record ID column after Balance in the Analytic Accounts list. | `view analytic.view_account_analytic_account_list` (analytic) |  |
