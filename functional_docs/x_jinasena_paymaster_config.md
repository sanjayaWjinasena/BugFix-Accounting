# BugFix-Accounting — `x_jinasena_paymaster_config`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_jinasena_paymaster_config` — CBC Paymaster Config

*Created by this repo.* Python: `models/x_jinasena_paymaster_config.py`, `models/x_jinasena_paymaster_config_gap.py`. Record name field: `x_name`.

**Summary:**

<!-- SUMMARY:model:x_jinasena_paymaster_config -->
Purpose not evident from code. It holds fixed values for a Paymaster bank transfer file (originating account, bank MICR, branch and name, transaction, return and credit/debit codes, currency code, filler and security field), but no view, action or logic in this repo reads them and only an Internal User access right is defined.
<!-- /SUMMARY -->

**Fields (18):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `create_date` | Created on | datetime | Date and time the CBC Paymaster Config record was created; set automatically. | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the CBC Paymaster Config record; set automatically. | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name Odoo shows for the CBC Paymaster Config record in dropdowns, lists and breadcrumbs; computed from its name field. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the CBC Paymaster Config record, assigned automatically. | stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time the CBC Paymaster Config record was last modified; set automatically. | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last modified the CBC Paymaster Config record; set automatically. | stored | `model res.users` (base) |  |
| `x_cr_dr_code` | Cr/Dr Code (H) | char | Fixed Credit/Debit code value for the Paymaster bank transfer file configuration (letter in the label is the file column); entered as configuration data, not referenced by views or logic in this repo. | stored |  |  |
| `x_currency_code` | Currency Code (K) | char | Fixed currency code value for the Paymaster bank transfer file configuration (letter in the label is the file column); entered as configuration data, not referenced by views or logic in this repo. | stored |  |  |
| `x_filler` | Filler (T) | char | Fixed filler value for the Paymaster bank transfer file configuration (letter in the label is the file column); entered as configuration data, not referenced by views or logic in this repo. | stored |  |  |
| `x_name` | Name | char | Name of the Paymaster bank file configuration record. | stored |  |  |
| `x_orig_account` | Orig Account (N) | char | Fixed originating account number value for the Paymaster bank transfer file configuration (letter in the label is the file column); entered as configuration data, not referenced by views or logic in this repo. | stored |  |  |
| `x_orig_bank_micr` | Orig Bank MICR (L) | char | Fixed originating bank MICR code value for the Paymaster bank transfer file configuration (letter in the label is the file column); entered as configuration data, not referenced by views or logic in this repo. | stored |  |  |
| `x_orig_branch` | Orig Branch (M) | char | Fixed originating branch code value for the Paymaster bank transfer file configuration (letter in the label is the file column); entered as configuration data, not referenced by views or logic in this repo. | stored |  |  |
| `x_orig_name` | Orig Name (O) | char | Fixed originating account name value for the Paymaster bank transfer file configuration (letter in the label is the file column); entered as configuration data, not referenced by views or logic in this repo. | stored |  |  |
| `x_return_code` | Return Code (G) | char | Fixed return code value for the Paymaster bank transfer file configuration (letter in the label is the file column); entered as configuration data, not referenced by views or logic in this repo. | stored |  |  |
| `x_return_date` | Return Date (I) | char | Fixed return date value for the Paymaster bank transfer file configuration (letter in the label is the file column); entered as configuration data, not referenced by views or logic in this repo. | stored |  |  |
| `x_security_field` | Security Field (S) | char | Fixed security field value for the Paymaster bank transfer file configuration (letter in the label is the file column); entered as configuration data, not referenced by views or logic in this repo. | stored |  |  |
| `x_trn_code` | TRN Code (F) | char | Fixed transaction (TRN) code value for the Paymaster bank transfer file configuration (letter in the label is the file column); entered as configuration data, not referenced by views or logic in this repo. | stored |  |  |

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| x_jinasena_paymaster_config user access | `access_x_jinasena_paymaster_config_user` | Gives **User types / Internal User** read/write/create/delete access to CBC Paymaster Config records. | `group base.group_user` (base)<br>`model x_jinasena_paymaster_config` |  |
