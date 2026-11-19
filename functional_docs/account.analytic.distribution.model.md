# BugFix-Accounting — `account.analytic.distribution.model`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.analytic.distribution.model` — Analytic Distribution Model

*Extends a model created by `analytic`.* Python: `models/account_analytic_distribution_model.py`.

Other repos that use this model: `server action BugFix-Purchase.server_action_2411_update_analytic_tag_parameters_purchase_line_produ` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_2412_update_analytic_tag_parameters_purchase_order_vend` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_2413_update_analytic_tag_parameters_purchase_order_user` (BugFix-Purchase)<br>`server action BugFix-Sales.server_action_2414_update_analytic_tag_parameters_sales_order_customer` (BugFix-Sales)<br>`server action BugFix-Sales.server_action_2415_update_analytic_tag_parameters_sales_order_user` (BugFix-Sales)<br>`server action BugFix-Sales.server_action_2416_update_analytic_tag_parameters_sales_line_product` (BugFix-Sales)

**Summary:**

<!-- SUMMARY:model:account.analytic.distribution.model -->
This repo adds one field: a 'Partner Mandatory' checkbox on analytic distribution models. No logic in this repo reads it. The docs show that BugFix-Purchase and BugFix-Sales server actions use this model.
<!-- /SUMMARY -->

**Fields (1):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `x_studio_partner_mandatory` | Partner Mandatory | boolean | Checkbox on analytic distribution models flagging that a partner is mandatory; no logic in this repo reads it. | stored |  |  |
