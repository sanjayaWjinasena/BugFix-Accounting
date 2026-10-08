# BugFix-Accounting — `x_rm_gross_margin_esti_line_7e86d`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_rm_gross_margin_esti_line_7e86d` — Rm Gross Margin Esti  Lines

*Created by this repo.* Python: `models/x_rm_gross_margin_esti_line_7e86d.py`, `models/x_rm_gross_margin_esti_line_7e86d_gap.py`. Record name field: `x_name`.

Other repos that use this model: `server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:x_rm_gross_margin_esti_line_7e86d -->
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
| `x_name` | Description | char | Description of the sub-line; shown in its list, form and search views. | stored; required |  | `view BugFix-Accounting.ported_view_4906_default_list_view_fo_b9016b82_f925_4499_95cb_16cf6742f25d`<br>`view BugFix-Accounting.ported_view_4907_default_form_view_fo_39a7a263_33fd_4e79_847c_0718bde4f6b5`<br>`view BugFix-Accounting.ported_view_4908_default_search_view_7d163442_ff51_45ed_9906_ed8405211391`<br>`view BugFix-Accounting.ported_view_4909_default_list_view_fo_e690196a_6de2_4b2a_82fd_cf9e11b09610`<br>`view BugFix-Accounting.ported_view_4910_default_form_view_fo_4c81dc72_e412_414e_bf17_a5524b2251be`<details><summary>+1 more</summary>`view BugFix-Accounting.ported_view_4911_default_search_view_fafce8d5_8b53_4663_a8ed_bf587c9a23cf`</details> |
| `x_rm_gross_margin_esti_id` | X Rm Gross Margin Esti | many2one → `x_rm_gross_margin_esti` | Parent Project Gross Margin estimated line this sub-line belongs to; no inverse list or logic uses it in this repo. | stored | `model x_rm_gross_margin_esti` |  |
| `x_studio_sequence` | Sequence | integer | Sort order of the Gross Margin Estimated sub-line (default 10); used as the drag handle in its list view. | default `10`; stored |  | `view BugFix-Accounting.ported_view_4906_default_list_view_fo_b9016b82_f925_4499_95cb_16cf6742f25d`<br>`view BugFix-Accounting.ported_view_4909_default_list_view_fo_e690196a_6de2_4b2a_82fd_cf9e11b09610` |

**Views (6):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_rm_gross_margin_esti_line_7e86d | `ported_view_4907_default_form_view_fo_39a7a263_33fd_4e79_847c_0718bde4f6b5` | form | full form layout with 1 fields | Default form for RM Gross Margin Estimated Lines: required Name title and two empty groups (no chatter). One of two duplicate default form views ported for this model. | `x_rm_gross_margin_esti_line_7e86d.x_name` |  |
| Default form view for x_rm_gross_margin_esti_line_7e86d | `ported_view_4910_default_form_view_fo_4c81dc72_e412_414e_bf17_a5524b2251be` | form | full form layout with 1 fields | Default form for RM Gross Margin Estimated Lines: required Name title and two empty groups (no chatter). Duplicate of `ported_view_4907`; only one is used as the default. | `x_rm_gross_margin_esti_line_7e86d.x_name` |  |
| Default list view for x_rm_gross_margin_esti_line_7e86d | `ported_view_4906_default_list_view_fo_b9016b82_f925_4499_95cb_16cf6742f25d` | tree | full tree layout with 2 fields | Inline-editable default list for RM Gross Margin Estimated Lines with sequence handle and Name. | `x_rm_gross_margin_esti_line_7e86d.x_name`<br>`x_rm_gross_margin_esti_line_7e86d.x_studio_sequence` |  |
| Default list view for x_rm_gross_margin_esti_line_7e86d | `ported_view_4909_default_list_view_fo_e690196a_6de2_4b2a_82fd_cf9e11b09610` | tree | full tree layout with 2 fields | Default list for RM Gross Margin Estimated Lines with sequence handle and Name (not editable); duplicate of `ported_view_4906`. | `x_rm_gross_margin_esti_line_7e86d.x_name`<br>`x_rm_gross_margin_esti_line_7e86d.x_studio_sequence` |  |
| Default search view for x_rm_gross_margin_esti_line_7e86d | `ported_view_4908_default_search_view_7d163442_ff51_45ed_9906_ed8405211391` | search | full search layout with 1 fields | Default search view for RM Gross Margin Estimated Lines: search by name only. One of two duplicate search views for this model. | `x_rm_gross_margin_esti_line_7e86d.x_name` |  |
| Default search view for x_rm_gross_margin_esti_line_7e86d | `ported_view_4911_default_search_view_fafce8d5_8b53_4663_a8ed_bf587c9a23cf` | search | full search layout with 1 fields | Default search view for RM Gross Margin Estimated Lines: search by name only. Duplicate of `ported_view_4908`. | `x_rm_gross_margin_esti_line_7e86d.x_name` |  |

**Access rights (8):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Rm Gross Margin Esti  Lines group_system | `access_1749_rm_gross_margin_esti__lines_group_system` | Gives **Administration / Settings** read/write/create/delete access to Rm Gross Margin Esti  Lines records. | `group base.group_system` (base)<br>`model x_rm_gross_margin_esti_line_7e86d` |  |
| Rm Gross Margin Esti  Lines group_system | `access_1751_rm_gross_margin_esti__lines_group_system` | Gives **Administration / Settings** read/write/create/delete access to Rm Gross Margin Esti  Lines records. | `group base.group_system` (base)<br>`model x_rm_gross_margin_esti_line_7e86d` |  |
| Rm Gross Margin Esti  Lines group_system | `access_1749_rm_gross_margin_esti_lines_group_system` | Gives **Administration / Settings** read/write/create/delete access to Rm Gross Margin Esti  Lines records. | `group base.group_system` (base)<br>`model x_rm_gross_margin_esti_line_7e86d` |  |
| Rm Gross Margin Esti  Lines group_system | `access_1751_rm_gross_margin_esti_lines_group_system` | Gives **Administration / Settings** read/write/create/delete access to Rm Gross Margin Esti  Lines records. | `group base.group_system` (base)<br>`model x_rm_gross_margin_esti_line_7e86d` |  |
| Rm Gross Margin Esti  Lines group_user | `access_1750_rm_gross_margin_esti__lines_group_user` | Gives **User types / Internal User** read access to Rm Gross Margin Esti  Lines records. | `group base.group_user` (base)<br>`model x_rm_gross_margin_esti_line_7e86d` |  |
| Rm Gross Margin Esti  Lines group_user | `access_1752_rm_gross_margin_esti__lines_group_user` | Gives **User types / Internal User** read access to Rm Gross Margin Esti  Lines records. | `group base.group_user` (base)<br>`model x_rm_gross_margin_esti_line_7e86d` |  |
| Rm Gross Margin Esti  Lines group_user | `access_1750_rm_gross_margin_esti_lines_group_user` | Gives **User types / Internal User** read access to Rm Gross Margin Esti  Lines records. | `group base.group_user` (base)<br>`model x_rm_gross_margin_esti_line_7e86d` |  |
| Rm Gross Margin Esti  Lines group_user | `access_1752_rm_gross_margin_esti_lines_group_user` | Gives **User types / Internal User** read access to Rm Gross Margin Esti  Lines records. | `group base.group_user` (base)<br>`model x_rm_gross_margin_esti_line_7e86d` |  |
