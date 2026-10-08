# BugFix-Accounting — `account.report.external.value`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.report.external.value` — Accounting Report External Value

*Extends a model created by `account`.*

**Summary:**

<!-- SUMMARY:model:account.report.external.value -->
This repo adds no fields or logic to report external values. It ships one list view of manually entered external values (name, date, numeric and text value) with target and company details as optional columns.
<!-- /SUMMARY -->

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| account.report.external.value.tree | `ported_account_report_external_value_tree` | tree | full tree layout with 10 fields | List of manually entered report External Values (no create): name, date, numeric and text value, with target expression/line/label, foreign VAT fiscal position and company as optional hidden columns. | `account.report.external.value.company_id` (account)<br>`account.report.external.value.date` (account)<br>`account.report.external.value.foreign_vat_fiscal_position_id` (account)<br>`account.report.external.value.name` (account)<br>`account.report.external.value.report_country_id` (account)<details><summary>+6 more</summary>`account.report.external.value.target_report_expression_id` (account)<br>`account.report.external.value.target_report_expression_label` (account)<br>`account.report.external.value.target_report_line_id` (account)<br>`account.report.external.value.text_value` (account)<br>`account.report.external.value.value` (account)<br>`group base.group_multi_company` (base)</details> |  |
