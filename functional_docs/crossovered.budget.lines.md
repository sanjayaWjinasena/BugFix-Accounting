# BugFix-Accounting — `crossovered.budget.lines`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `crossovered.budget.lines` — Budget Line

*Extends a model created by `account_budget`.* Python: `models/crossovered_budget.py`.

**Summary:**

<!-- SUMMARY:model:crossovered.budget.lines -->
This repo adds an 'Estimate' monetary field to budget lines. Its compute always returns 0. An automation copies the budget's Analytic Account onto each line when lines are created or updated. The repo also ships the standard multi-company record rule.
<!-- /SUMMARY -->

**Fields (1):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `x_studio_estimate` | Estimate | monetary | Monetary 'Estimate' on budget lines whose compute always returns 0 (the original Studio field had an empty compute); no business effect. | computed by `_compute_x_studio_estimate`; not stored | `crossovered.budget.lines._compute_x_studio_estimate()` | `crossovered.budget.lines._compute_x_studio_estimate()` |

**Python methods (1):**

| Method | Function | Decorators | Extends standard | Depends on | Used by | Where |
|---|---|---|---|---|---|---|
| `_compute_x_studio_estimate` | Compute for Estimate on budget lines; a no-op placeholder that always sets 0. |  |  | `crossovered.budget.lines.x_studio_estimate` | `crossovered.budget.lines.x_studio_estimate` | `models/crossovered_budget.py:352` |

**Server actions (1):**

- **Execute Code** (`server_action_2184_proj_pass_analytic_account_to_lines`, type `code`)
  - Function: Run by automation on budget lines: copies the budget's Analytic Account onto the line's analytic account.
  - Depends on: `crossovered.budget.lines.crossovered_budget_id` (account_budget), `model crossovered.budget.lines` (account_budget)
  - Used by: `automation BugFix-Accounting.base_automation_198_proj_pass_analytic_account_to_lines`
  <details><summary>code (3 lines)</summary>

```python
if record.crossovered_budget_id.x_studio_analytic_account.id != False:

  record.write({'analytic_account_id': record.crossovered_budget_id.x_studio_analytic_account.id})
```
  </details>
**Automations (1):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| PROJ - Pass Analytic Account to Lines | `base_automation_198_proj_pass_analytic_account_to_lines` |  | When a record is created or updated on Budget Line, runs _Execute Code_. | `crossovered.budget.lines.create_date` (account_budget)<br>`model crossovered.budget.lines` (account_budget)<br>`server action BugFix-Accounting.server_action_2184_proj_pass_analytic_account_to_lines` |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Budget lines multi-company | `rule_332_budget_lines_multi_company` | For everyone (global rule): read/write/create/delete on Budget Line only where `[('company_id', 'in', company_ids)]`. | `crossovered.budget.lines.company_id` (account_budget)<br>`model crossovered.budget.lines` (account_budget) |  |
