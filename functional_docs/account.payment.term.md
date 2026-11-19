# BugFix-Accounting — `account.payment.term`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.payment.term` — Payment Terms

*Extends a model created by `account`.*

Other repos that use this model: `res.users.x_studio_payment_term` (studio_usermodel_migration)<br>`res.users.x_studio_related_field_j3X4Q` (studio_usermodel_migration)<br>`res.users.x_studio_related_field_ngmve` (studio_usermodel_migration)<br>`res.users.x_studio_related_field_tLbBY` (studio_usermodel_migration)<br>`res.users.x_studio_terms_of_payment` (studio_usermodel_migration)<br>`server action BugFix-Studio-Misc.server_action_2827_jin_company_id_in_payment_terms_d7` (BugFix-Studio-Misc)<br>`x_customer_group.x_studio_payment_term` (studio_usermodel_migration)<br>`x_vendor_group.x_studio_payment_term` (studio_usermodel_migration)

**Summary:**

<!-- SUMMARY:model:account.payment.term -->
This repo adds an automation that sets a payment term's Company to the user's currently active company when the term is created or updated. On the Payment Terms form, Company is made read-only and the term lines list is redefined. The list gains a record ID column. The repo also ships a company record rule.
<!-- /SUMMARY -->

**Server actions (1):**

- **JIN - Company Id in Payment Terms** (`server_action_2827_jin_company_id_in_payment_terms`, type `code`)
  - Function: Run by the JIN automation: sets the payment term's Company to the user's currently active company.
  - Depends on: `model account.payment.term` (account), `model res.company` (base)
  - Used by: `automation BugFix-Accounting.base_automation_335_jin_company_id_in_payment_terms`
  <details><summary>code (4 lines)</summary>

```python
company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
company = env['res.company'].browse(company_id)

record['company_id'] = company.id
```
  </details>
**Automations (1):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| JIN - Company Id in Payment Terms | `base_automation_335_jin_company_id_in_payment_terms` |  | When a record is created or updated on Payment Terms, runs _JIN - Company Id in Payment Terms_. | `account.payment.term.create_date` (account)<br>`model account.payment.term` (account)<br>`server action BugFix-Accounting.server_action_2827_jin_company_id_in_payment_terms` |  |

**Views (2):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: account.payment.term.form customization | `ported_view_6052_customization_account_payment_term_form` | form | set force_save=True, readonly=1 on `//field[@name='company_id']`; inside `//field[@name='line_ids']`: add tree | Payment Terms form: makes Company read-only (force-saved) and defines the term lines list as Due Type, Value (read-only for balance lines) and Days. | `view account.view_payment_term_form` (account) |  |
| Odoo Studio: account.payment.term.tree customization | `ported_view_3118_customization_account_payment_term_tree` | tree | after `//tree[1]/field[@name='name']`: add field id | Adds the record ID column after Name in the Payment Terms list. | `view account.view_payment_term_tree` (account) |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Account payment term company rule | `rule_92_account_payment_term_company_rule` | For everyone (global rule): read/write/create/delete on Payment Terms only where `['|', ('company_id', '=', False), ('company_id', 'parent_of', company_ids)]`. | `account.payment.term.company_id` (account)<br>`model account.payment.term` (account) |  |
