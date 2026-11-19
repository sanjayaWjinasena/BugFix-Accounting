# BugFix-Accounting — `account.analytic.plan`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.analytic.plan` — Analytic Plans

*Extends a model created by `analytic`.* Python: `models/account_analytic_plan.py`, `models/account_analytic_plan_gap.py`.

Other repos that use this model: `sale.order.line._bugfix_analytics_build_distribution()` (BugFix-Analytics)<br>`server action BugFix-Sales.server_action_2178_proj_create_budget_entries` (BugFix-Sales)

**Summary:**

<!-- SUMMARY:model:account.analytic.plan -->
This repo adds two integer 'Group count' fields to analytic plans. They have no compute, so they are never calculated. The analytic plan form customization that would show them as smart buttons is archived and has no effect. The repo also adds two window actions that open analytic plans.
<!-- /SUMMARY -->

**Fields (2):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `x_group_id_account_analytic_account_count` | Group count | integer | Count field shown on the analytic plan form customization; plain integer with no compute in this repo, so it is never calculated. | not stored |  | `view BugFix-Accounting.view_5073_odoo_studio_account_analytic_group_form_customization_e` |
| `x_group_id_account_analytic_line_count` | Group count | integer | Count field shown on the analytic plan form customization; plain integer with no compute in this repo, so it is never calculated. | not stored |  | `view BugFix-Accounting.view_5073_odoo_studio_account_analytic_group_form_customization_e` |

**Window actions (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| account.analytic.plan | `action_3277_account_analytic_plan` | Opens **Analytic Plans** records (tree,form). | `model account.analytic.plan` (analytic) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_account_analytic_plan` (BugFix-Studio-Misc) |
| account.analytic.plan | `act_window_3277_account_analytic_plan` | Opens **Analytic Plans** records (tree,form). | `model account.analytic.plan` (analytic) |  |

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: account.analytic.group.form customization | `view_5073_odoo_studio_account_analytic_group_form_customization_e` | form | before `//form[1]/sheet[1]/group[1]`: add div | Inactive (archived) view: would add Analytic Account and Analytic Line count smart buttons to the Analytic Plan form; has no effect. | `account.analytic.plan.x_group_id_account_analytic_account_count`<br>`account.analytic.plan.x_group_id_account_analytic_line_count`<br>`view analytic.account_analytic_plan_form_view` (analytic)<br>`window action BugFix-Accounting.act_window_2334_analytic_line`<br>`window action BugFix-Accounting.action_2333_analytic_account` |  |
