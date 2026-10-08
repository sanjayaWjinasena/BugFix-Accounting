# BugFix-Accounting — `account.asset`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.asset` — Asset/Revenue Recognition

*Extends a model created by `account_asset`.*

**Summary:**

<!-- SUMMARY:model:account.asset -->
This repo only adds the Asset Model column after Name in the Assets list. It adds no fields or logic to assets.
<!-- /SUMMARY -->

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: account.asset.tree customization | `ported_view_8350_customization_account_asset_tree` | tree | after `//tree[1]/field[@name='name']`: add field model_id | Adds the Asset Model column after Name in the Assets list. | `account.asset.model_id` (account_asset)<br>`view account_asset.view_account_asset_tree` (account_asset) |  |
