# BugFix-Accounting — `account.invoice.report`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.invoice.report` — Invoices Statistics

*Extends a model created by `account`.*

**Summary:**

<!-- SUMMARY:model:account.invoice.report -->
This repo adds no fields or logic to invoice statistics. It ships three record rules: a multi-company rule, an all-documents rule for Sales All Documents users, and an own-documents rule for Sales Own Documents users.
<!-- /SUMMARY -->

**Record rules (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| All Invoices Analysis | `rule_171_all_invoices_analysis` | For Sales / User: All Documents: read/write/create/delete on Invoices Statistics with no record filter (empty domain = all records). | `group sales_team.group_sale_salesman_all_leads` (sales_team)<br>`model account.invoice.report` (account) |  |
| Invoice Analysis multi-company | `rule_85_invoice_analysis_multi_company` | For everyone (global rule): read/write/create/delete on Invoices Statistics only where `[('company_id', 'in', company_ids + [False])]`. | `account.invoice.report.company_id` (account)<br>`model account.invoice.report` (account) |  |
| Personal Invoices Analysis | `rule_170_personal_invoices_analysis` | For Sales / User: Own Documents Only: read/write/create/delete on Invoices Statistics only where `['|', ('invoice_user_id', '=', user.id), ('invoice_user_id', '=', False)]`. | `account.invoice.report.invoice_user_id` (account)<br>`group sales_team.group_sale_salesman` (sales_team)<br>`model account.invoice.report` (account) |  |
