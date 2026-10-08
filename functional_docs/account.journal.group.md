# BugFix-Accounting — `account.journal.group`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.journal.group` — Account Journal Group

*Extends a model created by `account`.*

**Summary:**

<!-- SUMMARY:model:account.journal.group -->
This repo adds no fields or logic to journal groups. It only ships the standard multi-company record rule.
<!-- /SUMMARY -->

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Journal Group multi-company | `rule_79_journal_group_multi_company` | For everyone (global rule): read/write/create/delete on Account Journal Group only where `[('company_id', 'parent_of', company_ids)]`. | `account.journal.group.company_id` (account)<br>`model account.journal.group` (account) |  |
