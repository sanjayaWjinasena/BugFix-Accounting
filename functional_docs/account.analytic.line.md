# BugFix-Accounting — `account.analytic.line`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.analytic.line` — Analytic Line

*Extends a model created by `analytic`.* Python: `models/account_analytic_line.py`, `models/account_analytic_line_gap.py`.

Other repos that use this model: `window action BugFix-Analytics.act_window_242_gross_margin` (BugFix-Analytics)

**Summary:**

<!-- SUMMARY:model:account.analytic.line -->
This repo declares five per-plan analytic account columns on analytic lines (Department, Cost Center, Sales Center, Product Group, Employee). The fields exist so these columns are present on a fresh install. It also adds account and other columns to the analytic line list, six window actions and nine record rules that cover multi-company, billing, helpdesk, read-only and timesheet access.
<!-- /SUMMARY -->

**Fields (5):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `x_plan15_id` | Department | many2one → `account.analytic.account` | Analytic account of the 'Department' analytic plan on the analytic line (Odoo's per-plan column for plan id 15), declared here so the column exists on a fresh install. | stored | `model account.analytic.account` (analytic) |  |
| `x_plan18_id` | Cost Center | many2one → `account.analytic.account` | Analytic account of the 'Cost Center' analytic plan on the analytic line (Odoo's per-plan column for plan id 18), declared here so the column exists on a fresh install. | stored | `model account.analytic.account` (analytic) |  |
| `x_plan19_id` | Sales Center | many2one → `account.analytic.account` | Analytic account of the 'Sales Center' analytic plan on the analytic line (Odoo's per-plan column for plan id 19), declared here so the column exists on a fresh install. | stored | `model account.analytic.account` (analytic) |  |
| `x_plan20_id` | Product Group | many2one → `account.analytic.account` | Analytic account of the 'Product Group' analytic plan on the analytic line (Odoo's per-plan column for plan id 20), declared here so the column exists on a fresh install. | stored | `model account.analytic.account` (analytic) |  |
| `x_plan21_id` | Employee | many2one → `account.analytic.account` | Analytic account of the 'Employee' analytic plan on the analytic line (Odoo's per-plan column for plan id 21), declared here so the column exists on a fresh install. | stored | `model account.analytic.account` (analytic) |  |

**Window actions (6):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Analytic Line | `aw_f4_account_analytic_line_analytic_line` | Opens **Analytic Line** records (tree,form), filtered to `[(1, '=', 1)]`. | `model account.analytic.line` (analytic) |  |
| Analytic Line | `action_2334_analytic_line` | Opens **Analytic Line** records (tree,form), filtered to `[(1, '=', 1)]`. | `model account.analytic.line` (analytic) |  |
| Analytic Line | `act_window_2334_analytic_line` | Opens **Analytic Line** records (tree,form), filtered to `[(1, '=', 1)]`. | `model account.analytic.line` (analytic) | `view BugFix-Accounting.view_5073_odoo_studio_account_analytic_group_form_customization_e` |
| account.analytic.line | `aw_f4_account_analytic_line_account_analytic_line` | Opens **Analytic Line** records (kanban,tree,form,pivot,graph,grid). | `model account.analytic.line` (analytic) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_account_analytic_line` (BugFix-Studio-Misc) |
| account.analytic.line | `action_2742_account_analytic_line` | Opens **Analytic Line** records (kanban,tree,form,pivot,graph,grid). | `model account.analytic.line` (analytic) |  |
| account.analytic.line | `act_window_2742_account_analytic_line` | Opens **Analytic Line** records (kanban,tree,form,pivot,graph,grid). | `model account.analytic.line` (analytic) |  |

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: account.analytic.line.view.tree.with.user customization | `ported_view_5911_odoo_studio_account_b0ebdb96_c367_4044_8e3c_c00f0a925a60` | tree | after `//field[@name='date']`: add field account_id; after `//tree[1]/field[@name='name']`: add field amount | Adds the Analytic Account column after Date and the Amount column after Description to the analytic items list (`view_account_analytic_line_tree`), both shown by default. | `account.analytic.line.account_id` (analytic)<br>`account.analytic.line.amount` (analytic)<br>`view analytic.view_account_analytic_line_tree` (analytic) |  |

**Record rules (9):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Analytic line multi company rule | `rule_64_analytic_line_multi_company_rule` | For everyone (global rule): read/write/create/delete on Analytic Line only where `[('company_id', 'in', company_ids)]`. | `account.analytic.line.company_id` (analytic)<br>`model account.analytic.line` (analytic) |  |
| account.analytic.line.billing.user | `rule_76_account_analytic_line_billing_user` | For Accounting / Billing: read/write/create/delete on Analytic Line only where `[('project_id', '=', False)]`. | `account.analytic.line.project_id` (hr_timesheet)<br>`group account.group_account_invoice` (account)<br>`model account.analytic.line` (analytic) |  |
| account.analytic.line.helpdesk.user | `rule_430_account_analytic_line_helpdesk_user` | For Helpdesk / User: write/create/delete on Analytic Line only where `[('user_id', '=', user.id), ('helpdesk_ticket_id', '!=', False)]`. | `account.analytic.line.helpdesk_ticket_id` (helpdesk_timesheet)<br>`account.analytic.line.user_id` (analytic)<br>`group helpdesk.group_helpdesk_user` (helpdesk)<br>`model account.analytic.line` (analytic) |  |
| account.analytic.line.readonly.user | `rule_675_account_analytic_line_readonly_user` | For Accounting / Read-only: read on Analytic Line with no record filter (empty domain = all records). | `group account.group_account_readonly` (account)<br>`model account.analytic.line` (analytic) |  |
| account.analytic.line.timesheet.approver | `rule_136_account_analytic_line_timesheet_approver` | For Timesheets / User: all timesheets: read/write/create/delete on Analytic Line only where `[
                ('project_id', '!=', False),
                '|',
                    ('project_id.privacy_visibility', '!=', 'followers'),
                    ('project_id.message_partner_ids', 'in', [user.partner_id.id])
            ]`. | `account.analytic.line.project_id` (hr_timesheet)<br>`group hr_timesheet.group_hr_timesheet_approver` (hr_timesheet)<br>`model account.analytic.line` (analytic)<br>`project.project.message_partner_ids` (project)<br>`project.project.privacy_visibility` (project) |  |
| account.analytic.line.timesheet.manager | `rule_137_account_analytic_line_timesheet_manager` | For Timesheets / Administrator: read/write/create/delete on Analytic Line only where `[('project_id', '!=', False)]`. | `account.analytic.line.project_id` (hr_timesheet)<br>`group hr_timesheet.group_timesheet_manager` (hr_timesheet)<br>`model account.analytic.line` (analytic) |  |
| account.analytic.line.timesheet.manager | `rule_431_account_analytic_line_timesheet_manager` | For Helpdesk / Administrator: write/create/delete on Analytic Line only where `[('helpdesk_ticket_id', '!=', False)]`. | `account.analytic.line.helpdesk_ticket_id` (helpdesk_timesheet)<br>`group helpdesk.group_helpdesk_manager` (helpdesk)<br>`model account.analytic.line` (analytic) |  |
| account.analytic.line.timesheet.user | `rule_135_account_analytic_line_timesheet_user` | For Timesheets / User: own timesheets only: read/create on Analytic Line only where `[
                ('user_id', '=', user.id),
                ('project_id', '!=', False),
                '|', '|',
                    ('project_id.privacy_visibility', '!=', 'followers'),
                    ('project_id.message_partner_ids', 'in', [user.partner_id.id]),
                    ('task_id.message_partner_ids', 'in', [user.partner_id.id])
            ]`. | `account.analytic.line.project_id` (hr_timesheet)<br>`account.analytic.line.task_id` (hr_timesheet)<br>`account.analytic.line.user_id` (analytic)<br>`group hr_timesheet.group_hr_timesheet_user` (hr_timesheet)<br>`model account.analytic.line` (analytic)<details><summary>+3 more</summary>`project.project.message_partner_ids` (project)<br>`project.project.privacy_visibility` (project)<br>`project.task.message_partner_ids` (project)</details> |  |
| account.analytic.line.timesheet.user.update-unlink | `rule_181_account_analytic_line_timesheet_user_update_unlink` | For Timesheets / User: own timesheets only: write/delete on Analytic Line only where `[
                ('user_id', '=', user.id),
                ('validated', '=', False),
                ('project_id', '!=', False),
                '|',
                    ('project_id.privacy_visibility', '!=', 'followers'),
                    '|',
                        ('project_id.message_partner_ids', 'in', [user.partner_id.id]),
                        ('task_id.message_partner_ids', 'in', [user.partner_id.id])
            ]`. | `account.analytic.line.project_id` (hr_timesheet)<br>`account.analytic.line.task_id` (hr_timesheet)<br>`account.analytic.line.user_id` (analytic)<br>`account.analytic.line.validated` (timesheet_grid)<br>`group hr_timesheet.group_hr_timesheet_user` (hr_timesheet)<details><summary>+4 more</summary>`model account.analytic.line` (analytic)<br>`project.project.message_partner_ids` (project)<br>`project.project.privacy_visibility` (project)<br>`project.task.message_partner_ids` (project)</details> |  |
