# BugFix-Accounting — `account.group`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.group` — Account Group

*Extends a model created by `account`.*

**Summary:**

<!-- SUMMARY:model:account.group -->
This repo only adds an optional record ID column before the code prefix in the Account Groups list. It adds no fields or logic.
<!-- /SUMMARY -->

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: account.group.tree customization | `ported_view_6033_customization_account_group_tree` | tree | before `//field[@name='code_prefix_start']`: add field id | Adds an optional record ID column before the code prefix in the Account Groups list. | `view account.view_account_group_tree` (account) |  |
