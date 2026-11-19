# BugFix-Accounting — `account.move.send`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.move.send` — Account Move Send

*Extends a model created by `account`.*

**Summary:**

<!-- SUMMARY:model:account.move.send -->
This repo adds no fields or logic to the invoice send-and-print wizard. It ships three record rules: Sales users see only customer invoices and refunds (all of them, or only their own), and Accounting Billing users have unrestricted access.
<!-- /SUMMARY -->

**Record rules (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| All Invoice Send and Print | `rule_778_all_invoice_send_and_print` | For Sales / User: All Documents: read/write/create/delete on Account Move Send only where `[('move_ids.move_type', 'in', ('out_invoice', 'out_refund'))]`. | `account.move.move_type` (account)<br>`account.move.send.move_ids` (account)<br>`group sales_team.group_sale_salesman_all_leads` (sales_team)<br>`model account.move.send` (account) |  |
| Personal Invoice Send and Print | `rule_777_personal_invoice_send_and_print` | For Sales / User: Own Documents Only: read/write/create/delete on Account Move Send only where `[('move_ids.move_type', 'in', ('out_invoice', 'out_refund')), '|', ('move_ids.invoice_user_id', '=', user.id), ('move_ids.invoice_user_id', '=', False)]`. | `account.move.invoice_user_id` (account)<br>`account.move.move_type` (account)<br>`account.move.send.move_ids` (account)<br>`group sales_team.group_sale_salesman` (sales_team)<br>`model account.move.send` (account) |  |
| Readonly Invoice Send and Print | `rule_769_readonly_invoice_send_and_print` | For Accounting / Billing: read/write/create/delete on Account Move Send with no record filter (empty domain = all records). | `group account.group_account_invoice` (account)<br>`model account.move.send` (account) |  |
