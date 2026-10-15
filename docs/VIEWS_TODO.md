> **⚠ SUPERSEDED — cross-repo tracker moved.**
>
> This document is a historical snapshot. The canonical Studio → Python
> migration state lives at:
>
>     D:\Odoo Playwright Tests\PlayWrite Testings\MIGRATION_TRACKER.md
>
> Refresh with `python scripts/refresh_migration_tracker.py --live`.
> Do NOT update this file for new work — append to the tracker's
> Iteration Log instead. Content below preserved for provenance.

---

# BugFix-Accounting — views to hand-port

84 views need hand-porting from Clear-DB. Do NOT 
auto-copy the arch — each has Studio xpath quirks that need 
human review before commit.

| # | Clear-DB view ID | Type | Target model | Name | Inherits |
|---|---|---|---|---|---|
| 1 | 5901 | form | `x_advance_payment_acco` | Default form view for x_advance_payment_acco | — |
| 2 | 2922 | form | `x_custom_currency` | Default form view for x_custom_currency | — |
| 3 | 2925 | form | `x_custom_currency_rate` | Default form view for x_custom_currency_rate | — |
| 4 | 2311 | form | `x_customer_posting_pro` | Default form view for x_customer_posting_pro | — |
| 5 | 3820 | form | `x_rm_cust_invoice_s1` | Default form view for x_rm_cust_invoice_s1 | — |
| 6 | 3816 | form | `x_rm_customer_wise_inv` | Default form view for x_rm_customer_wise_inv | — |
| 7 | 4944 | form | `x_rm_gross_margin_comp` | Default form view for x_rm_gross_margin_comp | — |
| 8 | 4913 | form | `x_temp_actual_budget` | Default form view for x_temp_actual_budget | — |
| 9 | 3035 | form | `x_temp_tp_invoice_line` | Default form view for x_temp_tp_invoice_line | — |
| 10 | 9490 | form | `x_test_rm_gross_margin` | Default form view for x_test_rm_gross_margin | — |
| 11 | 5900 | tree | `x_advance_payment_acco` | Default list view for x_advance_payment_acco | — |
| 12 | 2921 | tree | `x_custom_currency` | Default list view for x_custom_currency | — |
| 13 | 2924 | tree | `x_custom_currency_rate` | Default list view for x_custom_currency_rate | — |
| 14 | 2310 | tree | `x_customer_posting_pro` | Default list view for x_customer_posting_pro | — |
| 15 | 3819 | tree | `x_rm_cust_invoice_s1` | Default list view for x_rm_cust_invoice_s1 | — |
| 16 | 3815 | tree | `x_rm_customer_wise_inv` | Default list view for x_rm_customer_wise_inv | — |
| 17 | 4943 | tree | `x_rm_gross_margin_comp` | Default list view for x_rm_gross_margin_comp | — |
| 18 | 4912 | tree | `x_temp_actual_budget` | Default list view for x_temp_actual_budget | — |
| 19 | 3034 | tree | `x_temp_tp_invoice_line` | Default list view for x_temp_tp_invoice_line | — |
| 20 | 9489 | tree | `x_test_rm_gross_margin` | Default list view for x_test_rm_gross_margin | — |
| 21 | 7979 | pivot | `account.journal` | Default pivot view for ir.model(435,) | — |
| 22 | 3261 | pivot | `account.move` | Default pivot view for ir.model(446,) | — |
| 23 | 5902 | search | `x_advance_payment_acco` | Default search view for x_advance_payment_acco | — |
| 24 | 2923 | search | `x_custom_currency` | Default search view for x_custom_currency | — |
| 25 | 2926 | search | `x_custom_currency_rate` | Default search view for x_custom_currency_rate | — |
| 26 | 2312 | search | `x_customer_posting_pro` | Default search view for x_customer_posting_pro | — |
| 27 | 3821 | search | `x_rm_cust_invoice_s1` | Default search view for x_rm_cust_invoice_s1 | — |
| 28 | 3817 | search | `x_rm_customer_wise_inv` | Default search view for x_rm_customer_wise_inv | — |
| 29 | 4945 | search | `x_rm_gross_margin_comp` | Default search view for x_rm_gross_margin_comp | — |
| 30 | 4914 | search | `x_temp_actual_budget` | Default search view for x_temp_actual_budget | — |
| 31 | 3036 | search | `x_temp_tp_invoice_line` | Default search view for x_temp_tp_invoice_line | — |
| 32 | 9491 | search | `x_test_rm_gross_margin` | Default search view for x_test_rm_gross_margin | — |
| 33 | 5905 | tree | `account.payment.method.line` | Default tree view for ir.model(1327,) | — |
| 34 | 5904 | form | `x_advance_payment_acco` | Odoo Studio: Default form view for x_advance_payment_acco customization | Default form view for x_advance_payment_acco |
| 35 | 2927 | form | `x_custom_currency` | Odoo Studio: Default form view for x_custom_currency customization | Default form view for x_custom_currency |
| 36 | 2929 | form | `x_custom_currency_rate` | Odoo Studio: Default form view for x_custom_currency_rate customization | Default form view for x_custom_currency_rate |
| 37 | 2313 | form | `x_customer_posting_pro` | Odoo Studio: Default form view for x_customer_posting_pro customization | Default form view for x_customer_posting_pro |
| 38 | 3823 | form | `x_rm_cust_invoice_s1` | Odoo Studio: Default form view for x_rm_cust_invoice_s1 customization | Default form view for x_rm_cust_invoice_s1 |
| 39 | 3818 | form | `x_rm_customer_wise_inv` | Odoo Studio: Default form view for x_rm_customer_wise_inv customization | Default form view for x_rm_customer_wise_inv |
| 40 | 3038 | form | `x_temp_tp_invoice_line` | Odoo Studio: Default form view for x_temp_tp_invoice_line customization | Default form view for x_temp_tp_invoice_line |
| 41 | 5903 | tree | `x_advance_payment_acco` | Odoo Studio: Default list view for x_advance_payment_acco customization | Default list view for x_advance_payment_acco |
| 42 | 2931 | tree | `x_custom_currency` | Odoo Studio: Default list view for x_custom_currency customization | Default list view for x_custom_currency |
| 43 | 2930 | tree | `x_custom_currency_rate` | Odoo Studio: Default list view for x_custom_currency_rate customization | Default list view for x_custom_currency_rate |
| 44 | 2314 | tree | `x_customer_posting_pro` | Odoo Studio: Default list view for x_customer_posting_pro customization | Default list view for x_customer_posting_pro |
| 45 | 4946 | tree | `x_rm_gross_margin_comp` | Odoo Studio: Default list view for x_rm_gross_margin_comp customization | Default list view for x_rm_gross_margin_comp |
| 46 | 4915 | tree | `x_temp_actual_budget` | Odoo Studio: Default list view for x_temp_actual_budget customization | Default list view for x_temp_actual_budget |
| 47 | 5906 | tree | `account.payment.method.line` | Odoo Studio: Default tree view for ir.model(1327,) customization | Default tree view for ir.model(1327,) |
| 48 | 2195 | form | `account.account` | Odoo Studio: account.account.form customization | account.account.form |
| 49 | 2943 | tree | `account.account` | Odoo Studio: account.account.list customization | account.account.list |
| 50 | 5075 | tree | `account.analytic.account` | Odoo Studio: account.analytic.account.list customization | account.analytic.account.list |
| 51 | 5073 | form | `account.analytic.plan` | Odoo Studio: account.analytic.group.form customization | account.analytic.plan.form |
| 52 | 5911 | tree | `account.analytic.line` | Odoo Studio: account.analytic.line.view.tree.with.user customization | account.analytic.line.view.tree.with.user |
| 53 | 8351 | tree | `account.move.line` | Odoo Studio: account.archived.tax.tag.tree customization | account.archived.tax.tag.tree |
| 54 | 8350 | tree | `account.asset` | Odoo Studio: account.asset.tree customization | account.asset.tree |
| 55 | 6033 | tree | `account.group` | Odoo Studio: account.group.tree customization | account.group.tree |
| 56 | 5957 | tree | `account.tax` | Odoo Studio: account.invoice.line.tax.search customization | account.invoice.line.tax.search |
| 57 | 2442 | tree | `account.move` | Odoo Studio: account.invoice.tree customization | account.invoice.tree |
| 58 | 8579 | form | `account.journal` | Odoo Studio: account.journal.form customization | account.journal.form |
| 59 | 2549 | tree | `account.journal` | Odoo Studio: account.journal.tree customization | account.journal.tree |
| 60 | 2440 | form | `account.move` | Odoo Studio: account.move.form customization | account.move.form |
| 61 | 4017 | form | `account.move` | Odoo Studio: account.move.form customization_button | account.move.form |
| 62 | 3844 | form | `account.move.line` | Odoo Studio: account.move.line.form customization | account.move.line.form |
| 63 | 5060 | tree | `account.move.line` | Odoo Studio: account.move.line.tree customization | account.move.line.tree |
| 64 | 8298 | tree | `account.move.line` | Odoo Studio: account.move.line.tree-BankData customization | account.move.line.tree-BankData |
| 65 | 8297 | tree | `account.move.line` | Odoo Studio: account.move.line.tree-EPF customization | account.move.line.tree-EPF |
| 66 | 8296 | tree | `account.move.line` | Odoo Studio: account.move.line.tree-ETF customization | account.move.line.tree-ETF |
| 67 | 5291 | tree | `account.move.line` | Odoo Studio: account.move.line.tree.grouped_Test-01 customization | account.move.line.tree.grouped_Test-01 |
| 68 | 2591 | tree | `account.move` | Odoo Studio: account.move.tree customization | account.move.tree |
| 69 | 3906 | tree | `account.move` | Odoo Studio: account.out.invoice.tree customization | account.out.invoice.tree |
| 70 | 3907 | tree | `account.move` | Odoo Studio: account.out.invoice.tree customization | account.out.invoice.tree |
| 71 | 3066 | form | `account.payment` | Odoo Studio: account.payment.form customization | account.payment.form |
| 72 | 6052 | form | `account.payment.term` | Odoo Studio: account.payment.term.form customization | account.payment.term.form |
| 73 | 3118 | tree | `account.payment.term` | Odoo Studio: account.payment.term.tree customization | account.payment.term.tree |
| 74 | 3112 | tree | `account.payment` | Odoo Studio: account.payment.tree customization | account.payment.tree |
| 75 | 8293 | tree | `account.move.line` | account.move.line.tree-EPF | — |
| 76 | 5044 | tree | `account.move.line` | account.move.line.tree.grouped_1 | — |
| 77 | 6494 | form | `account.report.expression` | account.report.expression.form | — |
| 78 | 6497 | tree | `account.report.external.value` | account.report.external.value.tree | — |
| 79 | 6234 | form | `account.tax.group` | account.tax.group.form | — |
| 80 | 4122 | search | `account.tax.group` | account.tax.group.search.filters | — |
| 81 | 930 | tree | `account.tax.group` | account.tax.group.tree | — |
| 82 | 924 | tree | `account.tax.repartition.line` | account.tax.repartition.line.tree | — |
| 83 | 4372 | form | `account.tax.unit` | account.tax.unit.form | — |
| 84 | 4373 | tree | `account.tax.unit` | account.tax.unit.tree | — |
