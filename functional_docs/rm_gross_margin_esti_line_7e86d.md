# BugFix-Accounting — `rm_gross_margin_esti_line_7e86d`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `rm_gross_margin_esti_line_7e86d` — Rm Gross Margin Esti  Lines

*Created by this repo.* Python: `models/rm_gross_margin_esti_line_7e86d.py`, `models/x_rm_gross_margin_esti_line_7e86d_gap.py`. Record name field: `name`.

Other repos that use this model: `server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:rm_gross_margin_esti_line_7e86d -->
Purpose not evident from code. It is a sub-line with only a Description and a link to a Project Gross Margin estimated line; no inverse list or logic in this repo uses it.
<!-- /SUMMARY -->

**Fields (9):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `create_date` | Created on | datetime | Date and time this Rm Gross Margin Esti  Lines record was created; set automatically. | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created this Rm Gross Margin Esti  Lines record; set automatically. | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Standard computed name of the Rm Gross Margin Esti  Lines record as shown in links and dropdowns. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the Rm Gross Margin Esti  Lines record, assigned automatically. | stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time this Rm Gross Margin Esti  Lines record was last modified; set automatically. | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last modified this Rm Gross Margin Esti  Lines record; set automatically. | stored | `model res.users` (base) |  |
| `name` | Description | char | Description of the sub-line; shown in its list, form and search views. | stored; required |  | `view BugFix-Accounting.view_rm_gross_margin_esti_line_7e86d_list`<br>`view BugFix-Accounting.view_rm_gross_margin_esti_line_7e86d_form`<br>`view BugFix-Accounting.view_rm_gross_margin_esti_line_7e86d_search`<br>`view BugFix-Accounting.view_rm_gross_margin_esti_line_7e86d_list_2`<br>`view BugFix-Accounting.view_rm_gross_margin_esti_line_7e86d_form_2`<details><summary>+1 more</summary>`view BugFix-Accounting.view_rm_gross_margin_esti_line_7e86d_search_2`</details> |
| `rm_gross_margin_esti_id` | X Rm Gross Margin Esti | many2one → `rm_gross_margin_esti` | Parent Project Gross Margin estimated line this sub-line belongs to; no inverse list or logic uses it in this repo. | stored | `model rm_gross_margin_esti` |  |
| `sequence` | Sequence | integer | Sort order of the Gross Margin Estimated sub-line (default 10); used as the drag handle in its list view. | default `10`; stored |  | `view BugFix-Accounting.view_rm_gross_margin_esti_line_7e86d_list`<br>`view BugFix-Accounting.view_rm_gross_margin_esti_line_7e86d_list_2` |

**Views (6):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for rm_gross_margin_esti_line_7e86d | `view_rm_gross_margin_esti_line_7e86d_form` | form | full form layout with 1 fields | Default form for RM Gross Margin Estimated Lines: required Name title and two empty groups (no chatter). One of two duplicate default form views ported for this model. | `rm_gross_margin_esti_line_7e86d.name` |  |
| Default form view for rm_gross_margin_esti_line_7e86d | `view_rm_gross_margin_esti_line_7e86d_form_2` | form | full form layout with 1 fields | Default form for RM Gross Margin Estimated Lines: required Name title and two empty groups (no chatter). Duplicate of `ported_view_4907`; only one is used as the default. | `rm_gross_margin_esti_line_7e86d.name` |  |
| Default list view for rm_gross_margin_esti_line_7e86d | `view_rm_gross_margin_esti_line_7e86d_list` | tree | full tree layout with 2 fields | Inline-editable default list for RM Gross Margin Estimated Lines with sequence handle and Name. | `rm_gross_margin_esti_line_7e86d.name`<br>`rm_gross_margin_esti_line_7e86d.sequence` |  |
| Default list view for rm_gross_margin_esti_line_7e86d | `view_rm_gross_margin_esti_line_7e86d_list_2` | tree | full tree layout with 2 fields | Default list for RM Gross Margin Estimated Lines with sequence handle and Name (not editable); duplicate of `ported_view_4906`. | `rm_gross_margin_esti_line_7e86d.name`<br>`rm_gross_margin_esti_line_7e86d.sequence` |  |
| Default search view for rm_gross_margin_esti_line_7e86d | `view_rm_gross_margin_esti_line_7e86d_search` | search | full search layout with 1 fields | Default search view for RM Gross Margin Estimated Lines: search by name only. One of two duplicate search views for this model. | `rm_gross_margin_esti_line_7e86d.name` |  |
| Default search view for rm_gross_margin_esti_line_7e86d | `view_rm_gross_margin_esti_line_7e86d_search_2` | search | full search layout with 1 fields | Default search view for RM Gross Margin Estimated Lines: search by name only. Duplicate of `ported_view_4908`. | `rm_gross_margin_esti_line_7e86d.name` |  |

**Access rights (8):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Rm Gross Margin Esti  Lines group_system | `access_rm_gross_margin_esti_lines_group_system_3` | Gives **Administration / Settings** read/write/create/delete access to Rm Gross Margin Esti  Lines records. | `group base.group_system` (base)<br>`model rm_gross_margin_esti_line_7e86d` |  |
| Rm Gross Margin Esti  Lines group_system | `access_rm_gross_margin_esti_lines_group_system_4` | Gives **Administration / Settings** read/write/create/delete access to Rm Gross Margin Esti  Lines records. | `group base.group_system` (base)<br>`model rm_gross_margin_esti_line_7e86d` |  |
| Rm Gross Margin Esti  Lines group_system | `access_rm_gross_margin_esti_lines_group_system` | Gives **Administration / Settings** read/write/create/delete access to Rm Gross Margin Esti  Lines records. | `group base.group_system` (base)<br>`model rm_gross_margin_esti_line_7e86d` |  |
| Rm Gross Margin Esti  Lines group_system | `access_rm_gross_margin_esti_lines_group_system_2` | Gives **Administration / Settings** read/write/create/delete access to Rm Gross Margin Esti  Lines records. | `group base.group_system` (base)<br>`model rm_gross_margin_esti_line_7e86d` |  |
| Rm Gross Margin Esti  Lines group_user | `access_rm_gross_margin_esti_lines_group_user_3` | Gives **User types / Internal User** read access to Rm Gross Margin Esti  Lines records. | `group base.group_user` (base)<br>`model rm_gross_margin_esti_line_7e86d` |  |
| Rm Gross Margin Esti  Lines group_user | `access_rm_gross_margin_esti_lines_group_user_4` | Gives **User types / Internal User** read access to Rm Gross Margin Esti  Lines records. | `group base.group_user` (base)<br>`model rm_gross_margin_esti_line_7e86d` |  |
| Rm Gross Margin Esti  Lines group_user | `access_rm_gross_margin_esti_lines_group_user` | Gives **User types / Internal User** read access to Rm Gross Margin Esti  Lines records. | `group base.group_user` (base)<br>`model rm_gross_margin_esti_line_7e86d` |  |
| Rm Gross Margin Esti  Lines group_user | `access_rm_gross_margin_esti_lines_group_user_2` | Gives **User types / Internal User** read access to Rm Gross Margin Esti  Lines records. | `group base.group_user` (base)<br>`model rm_gross_margin_esti_line_7e86d` |  |
