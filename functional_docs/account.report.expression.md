# BugFix-Accounting — `account.report.expression`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.report.expression` — Accounting Report Expression

*Extends a model created by `account`.*

**Summary:**

<!-- SUMMARY:model:account.report.expression -->
This repo adds no fields or logic to accounting report expressions. It ships one full form view with a Definition tab (engine, formula, subformula) and an Options tab (date scope, figure type, carryover target and display flags).
<!-- /SUMMARY -->

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| account.report.expression.form | `ported_account_report_expression_form` | form | full form layout with 9 fields | Form for an accounting report expression: Label title, Definition tab (engine, formula, subformula required for domain engine) and Options tab (date scope, figure type, carryover target, blank if zero, green on positive). | `account.report.expression.blank_if_zero` (account)<br>`account.report.expression.carryover_target` (account)<br>`account.report.expression.date_scope` (account)<br>`account.report.expression.engine` (account)<br>`account.report.expression.figure_type` (account)<details><summary>+4 more</summary>`account.report.expression.formula` (account)<br>`account.report.expression.green_on_positive` (account)<br>`account.report.expression.label` (account)<br>`account.report.expression.subformula` (account)</details> |  |
