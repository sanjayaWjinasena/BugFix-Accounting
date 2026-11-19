# BugFix-Accounting — `account.setup.bank.manual.config`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.setup.bank.manual.config` — Bank setup manual config

*Extends a model created by `account`.* Python: `models/account_setup_bank_manual_config.py`.

**Summary:**

<!-- SUMMARY:model:account.setup.bank.manual.config -->
This repo adds eight char fields to the 'add bank account' setup wizard: bank code, branch code and SWIFT code (some duplicated) plus three unnamed Studio text fields. They are not stored and no logic in this repo uses them.
<!-- /SUMMARY -->

**Fields (8):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `x_studio_bank_code` | bank code | char | Bank code entered in the 'add bank account' setup wizard (duplicate of 'Bank code'); transient and not stored, and not used by any logic. | not stored |  |  |
| `x_studio_bank_code_1` | Bank code | char | Bank code entered in the 'add bank account' setup wizard; transient and not stored, and not used by any logic in this repo. | not stored |  |  |
| `x_studio_branch_code` | branch code | char | Branch code entered in the 'add bank account' setup wizard (duplicate of 'Branch code'); transient and not stored, and not used by any logic. | not stored |  |  |
| `x_studio_branch_code_1` | Branch code | char | Branch code entered in the 'add bank account' setup wizard; transient and not stored, and not used by any logic in this repo. | not stored |  |  |
| `x_studio_char_field_445_1jk2c8gep` | New Text | char | Unnamed Studio text field on the 'add bank account' setup wizard; transient, not stored and not used anywhere. | not stored |  |  |
| `x_studio_char_field_8qe_1jk2c6sho` | New Text | char | Unnamed Studio text field on the 'add bank account' setup wizard; transient, not stored and not used anywhere. | not stored |  |  |
| `x_studio_char_field_yfp1a` | New Text | char | Unnamed Studio text field on the 'add bank account' setup wizard; transient, not stored and not used anywhere. | not stored |  |  |
| `x_studio_swift_code` | SWIFT Code | char | SWIFT code entered in the 'add bank account' setup wizard; transient and not stored, and not used by any logic in this repo. | not stored |  |  |
