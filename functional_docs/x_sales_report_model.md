# BugFix-Accounting — `x_sales_report_model`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_sales_report_model` — Sales Report Model

*Extends a model created by `Jinasena_Masterdata_Reporting`.* Python: `models/x_sales_report_model.py`, `models/x_sales_report_model_gap.py`. Record name field: `x_name`.

Other repos that use this model: `access right BugFix-Project.access_x_sales_report_model_user` (BugFix-Project)<br>`access right Jinasena_Masterdata_Reporting.access_x_sales_report_model_user` (Jinasena_Masterdata_Reporting)<br>`project.update.x_studio_gross_margin_report` (BugFix-Project)<br>`report BugFix-Studio-Misc.action_report_1674_daily_sales_report` (BugFix-Studio-Misc)<br>`report BugFix-Studio-Misc.action_report_1684_customer_invoice_details` (BugFix-Studio-Misc)<br>`report BugFix-Studio-Misc.action_report_1713_sales_report_model_report` (BugFix-Studio-Misc)<br>`report BugFix-Studio-Misc.action_report_1728_daily_sales_report` (BugFix-Studio-Misc)<br>`report BugFix-Studio-Misc.action_report_1736_sales_details_for_incentive_calculation` (BugFix-Studio-Misc)<details><summary>+6 more</summary>`report BugFix-Studio-Misc.action_report_1739_production_order_wip` (BugFix-Studio-Misc)<br>`report BugFix-Studio-Misc.action_report_2111_project_gross_margin` (BugFix-Studio-Misc)<br>`server action BugFix-Project.server_action_2119_project_update_month_end_entries_2` (BugFix-Project)<br>`server action BugFix-Project.server_action_2130_project_update_project_gross_margin_report_auto_generate` (BugFix-Project)<br>`server action BugFix-Project.server_action_2131_project_update_project_gross_margin_report_auto_generate` (BugFix-Project)<br>`server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up` (BugFix-Studio-Misc)</details>

**Summary:**

<!-- SUMMARY:model:x_sales_report_model -->
The report run header (created by Jinasena_Masterdata_Reporting) that this repo also declares in Python; each record is one run of a report type with parameters such as As On Date, sales centre, project and date range. This repo adds the report logic: on save, automations keyed on the report code rebuild the result lines for Daily Sales Summary, Sales Details for Incentive Calc., Production Overview - WIP, Slow Moving Items, Sales - Production - Purchase, Production Summary - Split, Production Job Variance, Project Gross Margin and Costing Work Sheet, plus Generate and Clear actions for the Customer wise Invoices and Daily Sales Report. Other automations assign the reference from 'report.model.seq', stamp the created date, delete generated lines when a report is deleted and block deleting reports in Done status. It also adds the extended form with status bar, parameter and log groups and result tabs, a newest-first list, and actions that create or purge auto-generated Project Gross Margin reports for a hard-coded project id.
<!-- /SUMMARY -->

**Fields (89):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Calendar meeting linked to the next activity on the Sales Report Model record; standard mixin field. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Due date of the next scheduled activity on the Sales Report Model record; standard mixin field. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; warning=Alert; danger=Error; danger=Error | Warning or error decoration shown when an exception-type activity exists on the Sales Report Model record; standard mixin field. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Icon shown for an exception activity on the Sales Report Model record; standard mixin field. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Activities (to-dos, calls, meetings) scheduled on this Sales Report Model record; standard mail activity mixin field. | stored | `model mail.activity` (mail) | `view BugFix-Accounting.ported_view_3784_default_form_view_fo_d583be6a_921f_4205_94a7_603a2375ce6e`<br>`x_sales_report_model.activity_summary` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.activity_type_icon` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.activity_type_id` (Jinasena_Masterdata_Reporting) |
| `activity_state` | Activity State | selection: overdue=Overdue; overdue=Overdue; today=Today; today=Today; planned=Planned; planned=Planned | Standard activity status of the Sales Report Model record (Overdue, Today, Planned), computed from its next activity deadline. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Summary text of the next scheduled activity on the Sales Report Model record; standard mixin field. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_sales_report_model.activity_ids` (Jinasena_Masterdata_Reporting) |  |
| `activity_type_icon` | Activity Type Icon | char | Font Awesome icon of the next activity type, used in kanban/list activity widgets; standard mixin field. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_sales_report_model.activity_ids` (Jinasena_Masterdata_Reporting) |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Type of the next scheduled activity on the Sales Report Model record, read from its activities; standard mixin field. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_sales_report_model.activity_ids` (Jinasena_Masterdata_Reporting) |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | User responsible for the next scheduled activity on the Sales Report Model record; standard activity mixin field. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the Sales Report Model record was created; set automatically. Used as the trigger of the on-creation automation(s): jin report model seq no, report model created date, srm rpt project gross margin notify users. | stored |  | `automation BugFix-Accounting.base_automation_126_jin_report_model_seq_no`<br>`automation BugFix-Accounting.base_automation_188_report_model_created_date`<br>`automation BugFix-Accounting.base_automation_189_srm_rpt_project_gross_margin_notify_users` |
| `create_uid` | Created by | many2one → `res.users` | User who created the Sales Report Model record; set automatically. | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name Odoo shows for the Sales Report Model record in dropdowns, lists and breadcrumbs; computed from its name field. | not stored |  |  |
| `has_message` | Has Message | boolean | Whether the Sales Report Model record has any chatter messages; standard chatter field. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the Sales Report Model record, assigned automatically. | stored |  |  |
| `message_attachment_count` | Attachment Count | integer | Number of attachments on the Sales Report Model record; standard chatter field. | not stored |  |  |
| `message_follower_ids` | Followers | one2many → `mail.followers` | Followers who receive notifications for the Sales Report Model record, shown in the chatter. | stored | `model mail.followers` (mail) | `view BugFix-Accounting.ported_view_3784_default_form_view_fo_d583be6a_921f_4205_94a7_603a2375ce6e` |
| `message_has_error` | Message Delivery error | boolean | Whether a message on the Sales Report Model record failed to be delivered; standard chatter field. | not stored |  |  |
| `message_has_error_counter` | Number of errors | integer | Number of messages on the Sales Report Model record with delivery errors; standard chatter field. | not stored |  |  |
| `message_has_sms_error` | SMS Delivery error | boolean | Whether an SMS sent from the Sales Report Model record failed; standard chatter field. | not stored |  |  |
| `message_ids` | Messages | one2many → `mail.message` | Chatter messages and log notes posted on the Sales Report Model record. | stored | `model mail.message` (mail) | `view BugFix-Accounting.ported_view_3784_default_form_view_fo_d583be6a_921f_4205_94a7_603a2375ce6e` |
| `message_is_follower` | Is Follower | boolean | Whether the current user follows the Sales Report Model record; standard chatter field. | not stored |  |  |
| `message_needaction` | Action Needed | boolean | Whether the Sales Report Model record has unread messages that need the current user's attention; standard chatter field. | not stored |  |  |
| `message_needaction_counter` | Number of Actions | integer | Number of messages on the Sales Report Model record needing the current user's attention; standard chatter field. | not stored |  |  |
| `message_partner_ids` | Followers (Partners) | many2many → `res.partner` | Partners following the Sales Report Model record; standard chatter field used for searching. | not stored | `model res.partner` (base) |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Due date of the current user's next activity on the Sales Report Model record; standard mixin field. | not stored |  |  |
| `rating_ids` | Ratings | one2many → `rating.rating` | Customer ratings linked to the Sales Report Model record; standard field from the mail thread mixin, not used here. | stored | `model rating.rating` (rating) |  |
| `website_message_ids` | Website Messages | one2many → `mail.message` | Messages on the Sales Report Model record that are visible on the website/portal; standard chatter field. | stored | `model mail.message` (mail) |  |
| `write_date` | Last Updated on | datetime | Date and time the Sales Report Model record was last modified; set automatically. | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last modified the Sales Report Model record; set automatically. | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Active flag of the Sales Report Model record: unchecking it archives the record and hides it from default searches; defaults to checked via ir.default. | stored |  | `default BugFix-Accounting.default_250_x_sales_report_model_x_active`<br>`view BugFix-Accounting.ported_view_3784_default_form_view_fo_d583be6a_921f_4205_94a7_603a2375ce6e`<br>`view BugFix-Accounting.ported_view_3785_default_search_view_36b50122_6852_4842_9718_7d6fbf0c90e3`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b`<br>`view BugFix-Project.ported_default_form_view_fo_d583be6a_921f_4205_94a7_603a2375ce6e` (BugFix-Project)<details><summary>+1 more</summary>`view BugFix-Project.ported_default_search_view__36b50122_6852_4842_9718_7d6fbf0c90e3` (BugFix-Project)</details> |
| `x_name` | Name | char | Reference number of the report run; assigned by the 'Report Model Seq No' automation on creation and used as the name in report generation actions. | stored |  | `server action BugFix-Accounting.sa_f5_x_sales_report_model_report_model_seq_no`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_production_job_variance`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_production_overview_wip`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_production_summary_split`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_project_gross_margin`<details><summary>+16 more</summary>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_sales_production_purchase_report`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_slow_moving_items`<br>`server action BugFix-Accounting.server_action_1726_srm_auto_populate_data`<br>`server action BugFix-Accounting.server_action_1747_report_model_seq_no`<br>`server action BugFix-Accounting.server_action_1761_srm_rpt_production_overview_wip`<br>`server action BugFix-Accounting.server_action_1762_srm_rpt_slow_moving_items`<br>`server action BugFix-Accounting.server_action_1763_srm_rpt_sales_production_purchase_report`<br>`server action BugFix-Accounting.server_action_1764_srm_rpt_production_summary_split`<br>`server action BugFix-Accounting.server_action_1765_srm_rpt_production_job_variance`<br>`server action BugFix-Accounting.server_action_2102_srm_rpt_project_gross_margin`<br>`view BugFix-Accounting.ported_view_3783_default_list_view_fo_8853c5be_dc14_48d4_82c4_f209d820d16a`<br>`view BugFix-Accounting.ported_view_3784_default_form_view_fo_d583be6a_921f_4205_94a7_603a2375ce6e`<br>`view BugFix-Accounting.ported_view_3785_default_search_view_36b50122_6852_4842_9718_7d6fbf0c90e3`<br>`view BugFix-Project.ported_default_form_view_fo_d583be6a_921f_4205_94a7_603a2375ce6e` (BugFix-Project)<br>`view BugFix-Project.ported_default_list_view_fo_8853c5be_dc14_48d4_82c4_f209d820d16a` (BugFix-Project)<br>`view BugFix-Project.ported_default_search_view__36b50122_6852_4842_9718_7d6fbf0c90e3` (BugFix-Project)</details> |
| `x_studio_actual_gp_` | Actual GP | float | Actual gross profit figure shown on the Project Gross Margin report. | stored |  | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b`<br>`view BugFix-Accounting.ported_view_3791_odoo_studio_default_25244692_8d9f_4fba_9286_7f16ca6d45f1` |
| `x_studio_actual_line_ids` | Actual Line Ids | one2many → `x_rm_gross_margin_actu` | Actuals lines of a Project Gross Margin report, shown read-only on the "Actual Amounts" tab when the report code is Project Gross Margin; generated by SRM - RPT - Project Gross Margin. | stored | `model x_rm_gross_margin_actu` | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_actuals` | Actuals | boolean | Checkbox on the report form (default from ir.default) to include actuals; no logic in this repo reads it. | stored |  | `default BugFix-Accounting.default_406_x_sales_report_model_x_studio_actuals`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_as_on_date` | As on Date | date | Report 'as on' date; changing it triggers the report-generation automations (daily sales, incentive, WIP, slow moving, production summary/variance, etc.). | stored |  | `automation BugFix-Accounting.base_automation_116_srm_auto_populate_data`<br>`automation BugFix-Accounting.base_automation_120_srm_auto_populate_report_type_in_account_move_lines`<br>`automation BugFix-Accounting.base_automation_125_srm_auto_delete_sub_models`<br>`automation BugFix-Accounting.base_automation_131_srm_rpt_daily_sales_summary`<br>`automation BugFix-Accounting.base_automation_132_srm_rpt_sales_details_for_incentive_calc`<details><summary>+30 more</summary>`automation BugFix-Accounting.base_automation_133_srm_rpt_production_overview_wip`<br>`automation BugFix-Accounting.base_automation_134_srm_rpt_slow_moving_items`<br>`automation BugFix-Accounting.base_automation_135_srm_rpt_sales_production_purchase_report`<br>`automation BugFix-Accounting.base_automation_136_srm_rpt_production_summary_split`<br>`automation BugFix-Accounting.base_automation_137_srm_rpt_production_job_variance`<br>`automation BugFix-Accounting.base_automation_182_srm_rpt_project_gross_margin`<br>`automation BugFix-Accounting.base_automation_248_srm_rpt_costing_work_sheet`<br>`automation BugFix-Stock.base_automation_124_srm_auto_populate_report_type_in_product_moves` (BugFix-Stock)<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_daily_sales_summary`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_production_job_variance`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_production_summary_split`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_project_gross_margin`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_sales_details_for_incentive_calc`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_sales_production_purchase_report`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_slow_moving_items`<br>`server action BugFix-Accounting.server_action_1670_rpt_daily_sales_report_generate`<br>`server action BugFix-Accounting.server_action_1680_rpt_customer_wise_invoices_generate`<br>`server action BugFix-Accounting.server_action_1709_srm_auto_populate_data`<br>`server action BugFix-Accounting.server_action_1726_srm_auto_populate_data`<br>`server action BugFix-Accounting.server_action_1727_srm_auto_populate_data_tau`<br>`server action BugFix-Accounting.server_action_1730_srm_auto_populate_data_original`<br>`server action BugFix-Accounting.server_action_1759_srm_rpt_daily_sales_summary`<br>`server action BugFix-Accounting.server_action_1760_srm_rpt_sales_details_for_incentive_calc`<br>`server action BugFix-Accounting.server_action_1762_srm_rpt_slow_moving_items`<br>`server action BugFix-Accounting.server_action_1763_srm_rpt_sales_production_purchase_report`<br>`server action BugFix-Accounting.server_action_1764_srm_rpt_production_summary_split`<br>`server action BugFix-Accounting.server_action_1765_srm_rpt_production_job_variance`<br>`server action BugFix-Accounting.server_action_2102_srm_rpt_project_gross_margin`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b`<br>`view BugFix-Accounting.ported_view_3791_odoo_studio_default_25244692_8d9f_4fba_9286_7f16ca6d45f1`</details> |
| `x_studio_as_on_date_1` | From Date | date | Start date of the period for the Costing Work Sheet report; triggers its regeneration. | stored |  | `automation BugFix-Accounting.base_automation_248_srm_rpt_costing_work_sheet`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_costing_work_sheet`<br>`server action BugFix-Accounting.server_action_2490_srm_rpt_costing_work_sheet`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_as_on_date_2` | To Date | date | End date of the period for the Costing Work Sheet report. | stored |  | `server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_costing_work_sheet`<br>`server action BugFix-Accounting.server_action_2490_srm_rpt_costing_work_sheet`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_auto_generated` | Auto Generated | boolean | Marks report records created automatically by the scheduled Project Gross Margin report action. | stored |  | `server action BugFix-Accounting.server_action_2116_project_gross_margin_report`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b`<br>`view BugFix-Accounting.ported_view_3791_odoo_studio_default_25244692_8d9f_4fba_9286_7f16ca6d45f1` |
| `x_studio_comparison_line_ids` | Comparison Line Ids | one2many → `x_rm_gross_margin_comp` | Comparison lines (estimated vs delivered vs invoiced per product/order) of a Project Gross Margin report, shown read-only on the "Comparison Details" tab. | stored | `model x_rm_gross_margin_comp` | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_contingency_` | Contingency % | float | Contingency percentage parameter of the Costing Work Sheet report (default from ir.default); changing it re-runs the report. | stored |  | `automation BugFix-Accounting.base_automation_248_srm_rpt_costing_work_sheet`<br>`default BugFix-Accounting.default_398_x_sales_report_model_x_studio_contingency_`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_costing_work_sheet`<br>`server action BugFix-Accounting.server_action_2490_srm_rpt_costing_work_sheet`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_created_date` | Created Date | date | Date the report record was created, set by the 'Report Model Created Date' automation; used by the 'Project Gross Margin - Delete Reports' action to clean up old reports. | stored |  | `server action BugFix-Accounting.sa_f5_x_sales_report_model_report_model_created_date`<br>`server action BugFix-Accounting.server_action_2126_report_model_created_date`<br>`server action BugFix-Accounting.server_action_2127_project_gross_margin_delete_reports`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_created_from_project_update` | Created From Project Update | many2one → `project.update` | Project update this report was created from, shown on the report form. | stored | `model project.update` (project) | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_customer` | Customer | many2many → `res.partner` | Customers to filter the report by; used by the Project Gross Margin and Customer-wise Invoices report actions. | stored | `model res.partner` (base) | `server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_project_gross_margin`<br>`server action BugFix-Accounting.server_action_1680_rpt_customer_wise_invoices_generate`<br>`server action BugFix-Accounting.server_action_2102_srm_rpt_project_gross_margin`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_daily_sales_report_id` | Daily Sales Report Id 1 | one2many → `x_rm_daily_sales_repor` | Daily Sales Report lines (sales centre targets vs net invoice values) of the report; shown on the "Daily Sales Report" tab, which is always hidden. | stored | `model x_rm_daily_sales_repor` | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_daily_sales_report_id_1` | Daily Sales Report Id 2 | one2many → `x_rm_daily_s1` | Invoice lines of a Daily Sales Summary report, shown on the "Invoices - For the Date (Filtered)" tab filtered to the report's As on Date; generated by SRM - RPT - Daily Sales Summary. | stored | `model x_rm_daily_s1` | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_daily_sales_report_id_2` | Daily Sales Report Id 3 | one2many → `x_rm_daily_s2` | RM Daily S2 invoice lines shown on the "Invoices - For the Month" tab, which is always hidden; no logic in this repo fills these lines. | stored | `model x_rm_daily_s2` | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_daily_sales_report_id_3` | Daily Sales Report Id 4 | one2many → `x_rm_daily_s3` | RM Daily S3 invoice lines shown on the "Invoices - For the Year" tab, which is always hidden; no logic in this repo fills these lines. | stored | `model x_rm_daily_s3` | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_date_updated` | Date Updated | boolean | Checkbox shown on the report form; no logic in this repo sets or reads it. | stored |  | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_distributor_addition` | Distributor Addition % | float | Distributor addition percentage parameter for the Costing Work Sheet report (default from ir.default); changing it re-runs the report. | stored |  | `automation BugFix-Accounting.base_automation_248_srm_rpt_costing_work_sheet`<br>`default BugFix-Accounting.default_396_x_sales_report_model_x_studio_distributor_additi`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_costing_work_sheet`<br>`server action BugFix-Accounting.server_action_2490_srm_rpt_costing_work_sheet`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_estimated_gp_` | Estimated GP | float | Estimated gross profit figure shown on the Project Gross Margin report. | stored |  | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b`<br>`view BugFix-Accounting.ported_view_3791_odoo_studio_default_25244692_8d9f_4fba_9286_7f16ca6d45f1` |
| `x_studio_estimated_line_ids` | Estimated Line Ids | one2many → `x_rm_gross_margin_esti` | Estimated (quotation) lines of a Project Gross Margin report, shown read-only on the "Quotation/ Estimated" tab; generated by SRM - RPT - Project Gross Margin. | stored | `model x_rm_gross_margin_esti` | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_factory_oh` | Factory OH | float | Factory overhead parameter for the Costing Work Sheet report (default from ir.default); changing it re-runs the report. | stored |  | `automation BugFix-Accounting.base_automation_248_srm_rpt_costing_work_sheet`<br>`default BugFix-Accounting.default_400_x_sales_report_model_x_studio_factory_oh`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_costing_work_sheet`<br>`server action BugFix-Accounting.server_action_2490_srm_rpt_costing_work_sheet`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_factory_oh_labour` | Factory OH (Labour) | float | Factory overhead (labour) parameter for the Costing Work Sheet report (default from ir.default); changing it re-runs the report. | stored |  | `automation BugFix-Accounting.base_automation_248_srm_rpt_costing_work_sheet`<br>`default BugFix-Accounting.default_399_x_sales_report_model_x_studio_factory_oh_labour`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_costing_work_sheet`<br>`server action BugFix-Accounting.server_action_2490_srm_rpt_costing_work_sheet`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_financial_progress` | Financial Progress | float | Financial progress figure shown on the Project Gross Margin report. | stored |  | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b`<br>`view BugFix-Accounting.ported_view_3791_odoo_studio_default_25244692_8d9f_4fba_9286_7f16ca6d45f1` |
| `x_studio_from_date` | From Date | date | Start date of the reporting period, used by the auto-populate, Production Job Variance and Project Gross Margin report actions. | stored |  | `automation BugFix-Accounting.base_automation_116_srm_auto_populate_data`<br>`automation BugFix-Accounting.base_automation_137_srm_rpt_production_job_variance`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_production_job_variance`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_project_gross_margin`<br>`server action BugFix-Accounting.server_action_1726_srm_auto_populate_data`<details><summary>+3 more</summary>`server action BugFix-Accounting.server_action_1765_srm_rpt_production_job_variance`<br>`server action BugFix-Accounting.server_action_2102_srm_rpt_project_gross_margin`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b`</details> |
| `x_studio_idling_rate` | Idling Rate % | float | Idling rate percentage parameter for the Costing Work Sheet report (default from ir.default); changing it re-runs the report. | stored |  | `automation BugFix-Accounting.base_automation_248_srm_rpt_costing_work_sheet`<br>`default BugFix-Accounting.default_395_x_sales_report_model_x_studio_idling_rate`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_costing_work_sheet`<br>`server action BugFix-Accounting.server_action_2490_srm_rpt_costing_work_sheet`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_invoice_details_line_ids` | Invoice Details Line Ids | one2many → `x_rm_gross_margin_invo` | Invoice detail lines of a Project Gross Margin report, shown read-only on the "Invoice Details" tab. | stored | `model x_rm_gross_margin_invo` | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_journal_item_ids` | Journal Item Ids | one2many → `account.move.line` | Journal items linked to the selected report type, read through `x_studio_report_type.x_studio_journal_items_id`; shown on the report and used by the auto-populate action. | related `x_studio_report_type.x_studio_journal_items_id`; not stored | `model account.move.line` (account)<br>`x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_type.x_studio_journal_items_id` (Jinasena_Masterdata_Reporting) | `server action BugFix-Accounting.server_action_1709_srm_auto_populate_data`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_management_purpose` | Management Purpose | boolean | Marks Project Gross Margin reports created by the scheduled 'Management Purpose' variant of the report action. | stored |  | `server action BugFix-Accounting.server_action_2128_project_gross_margin_report_management_purpose`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_month_end_entry_updated` | Month End Entry Updated | boolean | Flag shown on the Project Gross Margin report indicating month-end entries were updated; no logic in this repo sets it. | stored |  | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b`<br>`view BugFix-Accounting.ported_view_3791_odoo_studio_default_25244692_8d9f_4fba_9286_7f16ca6d45f1` |
| `x_studio_none_moving_item_ids` | None Moving Item IDs | one2many → `x_rm_none_moving` | Slow-moving item lines of the report, shown on the "Slow Moving Items (Filtered)" tab when the report code is Slow Moving Items. | stored | `model x_rm_none_moving` | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_oh_absorbed_2_factory` | OH Absorbed 2 (Factory) | float | Second-level factory overhead absorbed, used/filled by the Costing Work Sheet report action (default from ir.default). | stored |  | `default BugFix-Accounting.default_405_x_sales_report_model_x_studio_oh_absorbed_2_fact`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_costing_work_sheet`<br>`server action BugFix-Accounting.server_action_2490_srm_rpt_costing_work_sheet`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_oh_absorbed_2_other` | OH Absorbed 2 (Other) | float | Second-level other overhead absorbed, used by the Costing Work Sheet report action. | stored |  | `server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_costing_work_sheet`<br>`server action BugFix-Accounting.server_action_2490_srm_rpt_costing_work_sheet`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_oh_absorbed_2_sales` | OH Absorbed 2 (Sales) | float | Second-level sales overhead absorbed, used by the Costing Work Sheet report action. | stored |  | `server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_costing_work_sheet`<br>`server action BugFix-Accounting.server_action_2490_srm_rpt_costing_work_sheet`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_oh_absorbed_factory` | OH Absorbed (Factory) | float | Factory overhead absorbed, used by the Costing Work Sheet report action (default from ir.default). | stored |  | `default BugFix-Accounting.default_403_x_sales_report_model_x_studio_oh_absorbed_factor`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_costing_work_sheet`<br>`server action BugFix-Accounting.server_action_2490_srm_rpt_costing_work_sheet`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_oh_absorbed_other` | OH Absorbed (Other) | float | Other overhead absorbed, used by the Costing Work Sheet report action. | stored |  | `server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_costing_work_sheet`<br>`server action BugFix-Accounting.server_action_2490_srm_rpt_costing_work_sheet`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_oh_absorbed_sales` | OH Absorbed (Sales) | float | Sales overhead absorbed, used by the Costing Work Sheet report action. | stored |  | `server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_costing_work_sheet`<br>`server action BugFix-Accounting.server_action_2490_srm_rpt_costing_work_sheet`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_one2many_field_1Aq0X` | New One2many | one2many → `x_rm_production_varian` | Production Job Variance lines (BOM vs consumed quantities and costs), shown on the "Production Variance (Filtered)" tab for that report code. Still has Studio's default label "New One2many". | stored | `model x_rm_production_varian` | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_one2many_field_1rlRW` | New One2many | one2many → `x_rm_production_orders` | Production order lines of a Production Overview - WIP report, shown on the "MO - WIP (Filtered)" tab. Still has Studio's default label "New One2many". | stored | `model x_rm_production_orders` | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_one2many_field_6rdac` | New One2many | one2many → `x_rm_sales_prod_purch` | Sales/production/purchase lines of the Sales - Production - Purchase Report, shown on its "(Filtered)" tab. Still has Studio's default label "New One2many". | stored | `model x_rm_sales_prod_purch` | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_one2many_field_jTZq4` | Sales Order Lines | one2many → `x_rm_sales_order_line` | Sales order lines of a Sales Details for Incentive Calc. report, shown on the "Order Lines - For the Date (Filtered)" tab. | stored | `model x_rm_sales_order_line` | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_one2many_field_yeTsx` | New One2many | one2many → `x_rm_prod_summary_spli` | Production Summary - Split lines, shown on the "Prod. Summary Split (Filtered)" tab for that report code. Still has Studio's default label "New One2many". | stored | `model x_rm_prod_summary_spli` | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_other_oh` | Other OH | float | Other overhead parameter for the Costing Work Sheet report (default from ir.default); changing it re-runs the report. | stored |  | `automation BugFix-Accounting.base_automation_248_srm_rpt_costing_work_sheet`<br>`default BugFix-Accounting.default_402_x_sales_report_model_x_studio_other_oh`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_costing_work_sheet`<br>`server action BugFix-Accounting.server_action_2490_srm_rpt_costing_work_sheet`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_profit_mark_up_` | Profit Mark Up % | float | Profit mark-up percentage parameter for the Costing Work Sheet report (default from ir.default). | stored |  | `default BugFix-Accounting.default_404_x_sales_report_model_x_studio_profit_mark_up_`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_costing_work_sheet`<br>`server action BugFix-Accounting.server_action_2490_srm_rpt_costing_work_sheet`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_project_no` | Project No | many2one → `project.project` | Project the report is for; used by the Project Gross Margin report actions and its window action. | stored | `model project.project` (project) | `server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_project_gross_margin`<br>`server action BugFix-Accounting.server_action_2102_srm_rpt_project_gross_margin`<br>`server action BugFix-Accounting.server_action_2116_project_gross_margin_report`<br>`server action BugFix-Accounting.server_action_2128_project_gross_margin_report_management_purpose`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b`<details><summary>+2 more</summary>`view BugFix-Accounting.ported_view_3791_odoo_studio_default_25244692_8d9f_4fba_9286_7f16ca6d45f1`<br>`window action BugFix-Accounting.action_2115_gross_margin_reports`</details> |
| `x_studio_pump_price_costing_ids` | Pump Price Costing Ids | one2many → `x_pump_price_costing` | Pump price costing lines of a Costing Work Sheet report, shown read-only on the "Pump Price Costing" tab; generated by SRM - RPT - Costing Work Sheet. | stored | `model x_pump_price_costing` | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_related_field_DqBBB` | New Related Field | one2many → `sale.order.line` | Sales order lines linked to the selected report type (related through the report type's Sales Lines), shown on the report form. | related `x_studio_report_type.x_studio_sales_lines_id`; not stored | `model sale.order.line` (sale)<br>`x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_type.x_studio_sales_lines_id` (Jinasena_Masterdata_Reporting) | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_related_field_n589a` | New Related Field | one2many → `account.move.line` | Journal items linked to the selected report type (same source as Journal Item Ids); not shown in any view in this repo. | related `x_studio_report_type.x_studio_journal_items_id`; not stored | `model account.move.line` (account)<br>`x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_type.x_studio_journal_items_id` (Jinasena_Masterdata_Reporting) |  |
| `x_studio_related_field_nfrkz` | New Related Field | one2many → `account.move` | Journal entries linked to the selected report type (related through its Journal Entry list), shown on the report form. | related `x_studio_report_type.x_studio_journal_entry_id`; not stored | `model account.move` (account)<br>`x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_type.x_studio_journal_entry_id` (Jinasena_Masterdata_Reporting) | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_report_code` | Report Code | selection: s-dailysales=Daily Sales Summary; s-dailysales=Daily Sales Summary; s-salesincentive=Sales Details for Incentive Calc.; s-salesincentive=Sales Details for Incentive Calc.; m-wip=Production Overview - WIP; m-wip=Production Overview - WIP | Code identifying which report this run produces; checked by the report-generation actions (daily sales, production, gross margin, costing work sheet...) to decide which one runs. Python declares only 3 options (Daily Sales, Incentive, WIP). | stored |  | `automation BugFix-Accounting.base_automation_182_srm_rpt_project_gross_margin`<br>`automation BugFix-Accounting.base_automation_248_srm_rpt_costing_work_sheet`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_costing_work_sheet`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_daily_sales_summary`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_production_job_variance`<details><summary>+21 more</summary>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_production_overview_wip`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_production_summary_split`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_project_gross_margin`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_sales_details_for_incentive_calc`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_sales_production_purchase_report`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_slow_moving_items`<br>`server action BugFix-Accounting.server_action_1726_srm_auto_populate_data`<br>`server action BugFix-Accounting.server_action_1759_srm_rpt_daily_sales_summary`<br>`server action BugFix-Accounting.server_action_1760_srm_rpt_sales_details_for_incentive_calc`<br>`server action BugFix-Accounting.server_action_1761_srm_rpt_production_overview_wip`<br>`server action BugFix-Accounting.server_action_1762_srm_rpt_slow_moving_items`<br>`server action BugFix-Accounting.server_action_1763_srm_rpt_sales_production_purchase_report`<br>`server action BugFix-Accounting.server_action_1764_srm_rpt_production_summary_split`<br>`server action BugFix-Accounting.server_action_1765_srm_rpt_production_job_variance`<br>`server action BugFix-Accounting.server_action_2102_srm_rpt_project_gross_margin`<br>`server action BugFix-Accounting.server_action_2116_project_gross_margin_report`<br>`server action BugFix-Accounting.server_action_2127_project_gross_margin_delete_reports`<br>`server action BugFix-Accounting.server_action_2128_project_gross_margin_report_management_purpose`<br>`server action BugFix-Accounting.server_action_2490_srm_rpt_costing_work_sheet`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b`<br>`view BugFix-Accounting.ported_view_3791_odoo_studio_default_25244692_8d9f_4fba_9286_7f16ca6d45f1`</details> |
| `x_studio_report_type` | Report Type | many2one → `x_sales_report_type` | Sales Report Type (report definition) this run belongs to; setting it triggers the matching report-generation automation. | stored | `model x_sales_report_type` (Jinasena_Masterdata_Reporting) | `automation BugFix-Accounting.base_automation_116_srm_auto_populate_data`<br>`automation BugFix-Accounting.base_automation_131_srm_rpt_daily_sales_summary`<br>`automation BugFix-Accounting.base_automation_132_srm_rpt_sales_details_for_incentive_calc`<br>`automation BugFix-Accounting.base_automation_133_srm_rpt_production_overview_wip`<br>`automation BugFix-Accounting.base_automation_134_srm_rpt_slow_moving_items`<details><summary>+42 more</summary>`automation BugFix-Accounting.base_automation_135_srm_rpt_sales_production_purchase_report`<br>`automation BugFix-Accounting.base_automation_136_srm_rpt_production_summary_split`<br>`automation BugFix-Accounting.base_automation_137_srm_rpt_production_job_variance`<br>`automation BugFix-Accounting.base_automation_182_srm_rpt_project_gross_margin`<br>`automation BugFix-Accounting.base_automation_248_srm_rpt_costing_work_sheet`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_costing_work_sheet`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_daily_sales_summary`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_production_job_variance`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_production_overview_wip`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_production_summary_split`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_project_gross_margin`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_sales_details_for_incentive_calc`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_sales_production_purchase_report`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_slow_moving_items`<br>`server action BugFix-Accounting.server_action_1709_srm_auto_populate_data`<br>`server action BugFix-Accounting.server_action_1711_srm_auto_populate_data_2`<br>`server action BugFix-Accounting.server_action_1726_srm_auto_populate_data`<br>`server action BugFix-Accounting.server_action_1727_srm_auto_populate_data_tau`<br>`server action BugFix-Accounting.server_action_1730_srm_auto_populate_data_original`<br>`server action BugFix-Accounting.server_action_1759_srm_rpt_daily_sales_summary`<br>`server action BugFix-Accounting.server_action_1760_srm_rpt_sales_details_for_incentive_calc`<br>`server action BugFix-Accounting.server_action_1761_srm_rpt_production_overview_wip`<br>`server action BugFix-Accounting.server_action_1762_srm_rpt_slow_moving_items`<br>`server action BugFix-Accounting.server_action_1763_srm_rpt_sales_production_purchase_report`<br>`server action BugFix-Accounting.server_action_1764_srm_rpt_production_summary_split`<br>`server action BugFix-Accounting.server_action_1765_srm_rpt_production_job_variance`<br>`server action BugFix-Accounting.server_action_2102_srm_rpt_project_gross_margin`<br>`server action BugFix-Accounting.server_action_2116_project_gross_margin_report`<br>`server action BugFix-Accounting.server_action_2127_project_gross_margin_delete_reports`<br>`server action BugFix-Accounting.server_action_2128_project_gross_margin_report_management_purpose`<br>`server action BugFix-Accounting.server_action_2490_srm_rpt_costing_work_sheet`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b`<br>`view BugFix-Accounting.ported_view_3791_odoo_studio_default_25244692_8d9f_4fba_9286_7f16ca6d45f1`<br>`x_sales_report_model.x_studio_journal_item_ids` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_related_field_DqBBB` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_related_field_NsCKm` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_related_field_PaCjA` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_related_field_XCKXu` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_related_field_bCtVj` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_related_field_n589a` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_related_field_nfrkz` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_related_field_oeTJK` (Jinasena_Masterdata_Reporting)</details> |
| `x_studio_sales_centre` | Sales Centre | many2many → `crm.team` | Sales teams (sales centres) to filter the report by; used by the daily sales, auto-populate and customer-wise invoice report actions. | stored | `model crm.team` (sales_team) | `automation BugFix-Accounting.base_automation_116_srm_auto_populate_data`<br>`automation BugFix-Accounting.base_automation_131_srm_rpt_daily_sales_summary`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_daily_sales_summary`<br>`server action BugFix-Accounting.server_action_1670_rpt_daily_sales_report_generate`<br>`server action BugFix-Accounting.server_action_1680_rpt_customer_wise_invoices_generate`<details><summary>+6 more</summary>`server action BugFix-Accounting.server_action_1709_srm_auto_populate_data`<br>`server action BugFix-Accounting.server_action_1726_srm_auto_populate_data`<br>`server action BugFix-Accounting.server_action_1727_srm_auto_populate_data_tau`<br>`server action BugFix-Accounting.server_action_1730_srm_auto_populate_data_original`<br>`server action BugFix-Accounting.server_action_1759_srm_rpt_daily_sales_summary`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b`</details> |
| `x_studio_sales_oh` | Sales OH | float | Sales overhead parameter for the Costing Work Sheet report (default from ir.default); changing it re-runs the report. | stored |  | `automation BugFix-Accounting.base_automation_248_srm_rpt_costing_work_sheet`<br>`default BugFix-Accounting.default_401_x_sales_report_model_x_studio_sales_oh`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_costing_work_sheet`<br>`server action BugFix-Accounting.server_action_2490_srm_rpt_costing_work_sheet`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_sales_report_model_id_4` | Sales Report Model Id | one2many → `x_rm_customer_wise_inv` | Customer wise Invoices lines (total invoiced per customer), shown read-only on the "Customer wise Invoices" tab, visible only when Report Type has database id 3. | stored | `model x_rm_customer_wise_inv` | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_sales_report_model_id_5` | Sales Report Model Id | one2many → `x_rm_cust_invoice_s1` | Invoice breakup lines (per invoice/product), shown read-only on the "Invoice Breakup" tab, visible only when Report Type has database id 3. | stored | `model x_rm_cust_invoice_s1` | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| `x_studio_selection_field_Fbw0x` | Status | selection: Draft=Draft; Draft=Draft; Done=Done; Done=Done | Report run status, Draft or Done (default from ir.default); report 'Clear' actions reset it to Draft. | stored |  | `default BugFix-Accounting.default_256_x_sales_report_model_x_studio_selection_field_Fbw0x`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b`<br>`view BugFix-Accounting.ported_view_3791_odoo_studio_default_25244692_8d9f_4fba_9286_7f16ca6d45f1` |
| `x_studio_sequence` | Sequence | integer | Sort order of Sales Report Model records in the list view (drag-and-drop handle); default value set by ir.default. | stored |  | `default BugFix-Accounting.default_251_x_sales_report_model_x_studio_sequence`<br>`view BugFix-Accounting.ported_view_3783_default_list_view_fo_8853c5be_dc14_48d4_82c4_f209d820d16a`<br>`view BugFix-Project.ported_default_list_view_fo_8853c5be_dc14_48d4_82c4_f209d820d16a` (BugFix-Project) |
| `x_studio_sscl` | SSCL % | float | SSCL (Social Security Contribution Levy) percentage parameter for the Costing Work Sheet report (default from ir.default). | stored |  | `default BugFix-Accounting.default_397_x_sales_report_model_x_studio_sscl`<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_costing_work_sheet`<br>`server action BugFix-Accounting.server_action_2490_srm_rpt_costing_work_sheet`<br>`view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |

**Server actions (43):**

- **Create activity: Gross Margin Report Generated** (`server_action_2129_srm_rpt_project_gross_margin_notify_users`, type `next_activity`)
  - Function: Schedule-activity action run by the Gross Margin report automation; no activity type, user or summary is configured in the port, so it schedules nothing meaningful.
  - Depends on: `model x_sales_report_model` (Jinasena_Masterdata_Reporting)
  - Used by: `automation BugFix-Accounting.base_automation_189_srm_rpt_project_gross_margin_notify_users`
  <details><summary>code (12 lines)</summary>

```python

# Available variables:
#  - env: Odoo Environment on which the action is triggered
#  - model: Odoo Model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: Odoo function to compare floats based on specific precisions
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - UserError: Warning Exception to use with raise
#  - Command: x2Many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **Execute Code** (`server_action_1675_restrict_delete_in_sales_report_model`, type `code`)
  - Function: Run on deletion of a Sales Report Model: blocks deleting records whose status is 'Done' (error message wording says the reverse).
  - Depends on: `model x_sales_report_model` (Jinasena_Masterdata_Reporting)
  - Used by: `automation BugFix-Accounting.base_automation_99_restrict_delete_in_sales_report_model`
  <details><summary>code (3 lines)</summary>

```python

if record.x_studio_selection_field_Fbw0x == 'Done':
  raise UserError("You can only delete a report model if the report model is in done state.")
```
  </details>
- **Execute Code** (`server_action_1746_srm_auto_delete_sub_models`, type `code`)
  - Function: Run by the auto-delete automation: removes all generated sub-report rows (production orders, non-moving, sales-prod-purch, summary split, variance) of the Sales Report Model.
  - Depends on: `model x_rm_none_moving`, `model x_rm_prod_summary_spli`, `model x_rm_production_orders`, `model x_rm_production_varian`, `model x_rm_sales_prod_purch`<details><summary>+1 more</summary>`model x_sales_report_model` (Jinasena_Masterdata_Reporting)</details>
  - Used by: `automation BugFix-Accounting.base_automation_125_srm_auto_delete_sub_models`
  <details><summary>code (21 lines)</summary>

```python

if record.id:
  temp_rec = env['x_rm_production_orders'].search([('x_studio_sales_report_model_id', '=', record.id)])
  for del_record in temp_rec:
    del_record.unlink()
    
  temp_rec2 = env['x_rm_none_moving'].search([('x_studio_sales_report_model_id', '=', record.id)])
  for del_record2 in temp_rec2:
    del_record2.unlink()
    
  temp_rec3 = env['x_rm_sales_prod_purch'].search([('x_studio_sales_report_model_id', '=', record.id)])
  for del_record3 in temp_rec3:
    del_record3.unlink()
    
  temp_rec4 = env['x_rm_prod_summary_spli'].search([('x_studio_sales_report_model_id', '=', record.id)])
  for del_record4 in temp_rec4:
    del_record4.unlink()
    
  temp_rec5 = env['x_rm_production_varian'].search([('x_studio_sales_report_model_id', '=', record.id)])
  for del_record5 in temp_rec5:
    del_record5.unlink()
```
  </details>
- **Execute Code** (`server_action_1747_report_model_seq_no`, type `code`)
  - Function: Run by the Report Model Seq No automation: when Name is 'New', assigns the next number from 'report.model.seq'.
  - Depends on: `model ir.sequence` (base), `model x_sales_report_model` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_name` (Jinasena_Masterdata_Reporting)
  - Used by: `automation BugFix-Accounting.base_automation_126_jin_report_model_seq_no`
  <details><summary>code (6 lines)</summary>

```python

#record['x_name'] = env['ir.sequence'].next_by_code('purchase.request.seq')

if record.x_name == 'New':
    seq = env['ir.sequence'].next_by_code('report.model.seq')
    record.write({'x_name': seq})
```
  </details>
- **Execute Code** (`server_action_1759_srm_rpt_daily_sales_summary`, type `code`)
  - Function: Run by automation for report code 'Daily Sales Summary': filters journal items by As On Date and Sales Centre, deletes old rows and creates daily sales summary rows.
  - Depends on: `model x_rm_daily_s1`, `model x_sales_report_model` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_code` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting)<details><summary>+1 more</summary>`x_sales_report_model.x_studio_sales_centre` (Jinasena_Masterdata_Reporting)</details>
  - Used by: `automation BugFix-Accounting.base_automation_131_srm_rpt_daily_sales_summary`
  <details><summary>code (56 lines)</summary>

```python

if record.x_studio_report_type:

  if record.x_studio_report_code == 'Daily Sales Summary':

    report_type_lines = record.x_studio_report_type.x_studio_journal_items_id

    

    # filter area ------------------------------------------------------------------------------------------------------------------------------------------------

    # filter by as on date

    if record.x_studio_as_on_date:

      report_type_lines = report_type_lines.filtered(lambda x: x.date == record.x_studio_as_on_date)

      

    # filter by sales centre

      if record.x_studio_sales_centre:

        report_type_lines = report_type_lines.filtered(lambda x: x.x_studio_sales_team == record.x_studio_sales_centre)

          

    # delete record area ----------------------------------------------------------------------------------------------------------------------------------------------  

    # delete old record

    

    # Daily Sales Summary

    temp_rec_1 = env['x_rm_daily_s1'].search([('x_studio_sales_report_model_id', '=', record._origin.id)])

    if temp_rec_1:

      for del_temp_rec_1 in temp_rec_1:

        del_temp_rec_1.unlink()

    

    # Business Logic --------------------------------------------------------------------------------------------------------------------------------------------   

    # create new record 

    

    # Daily Sales Summary

    for line in report_type_lines:

      create_sub_model = env['x_rm_daily_s1'].create({'x_studio_sales_report_model_id':record.id,'x_studio_invoice_date':line.date,'x_studio_number':line.move_name,'x_studio_partner':line.partner_id.id,'x_studio_sales_centre':line.x_studio_sales_team.id,'x_studio_product_id':line.product_id.id,'x_studio_quantity':line.quantity,'x_studio_value':line.price_subtotal})
```
  </details>
- **Execute Code** (`server_action_1760_srm_rpt_sales_details_for_incentive_calc`, type `code`)
  - Function: Run by automation for 'Sales Details for Incentive Calc.': takes income product journal items on As On Date, deletes old rows and creates sales detail rows for incentive calculation.
  - Depends on: `model x_rm_sales_order_line`, `model x_sales_report_model` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_code` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting)
  - Used by: `automation BugFix-Accounting.base_automation_132_srm_rpt_sales_details_for_incentive_calc`
  <details><summary>code (56 lines)</summary>

```python

if record.x_studio_report_type:

  if record.x_studio_report_code == 'Sales Details for Incentive Calc.':

    report_type_lines = record.x_studio_report_type.x_studio_journal_items_id

    

    # filter area ------------------------------------------------------------------------------------------------------------------------------------------------

    # filter by as on date

    if record.x_studio_as_on_date:

      report_type_lines = report_type_lines.filtered(lambda x: x.date == record.x_studio_as_on_date)

    # filter by product

      report_type_lines = report_type_lines.filtered(lambda x: x.product_id.id > 0)

    # filter by internal group

      report_type_lines = report_type_lines.filtered(lambda x: x.account_internal_group == 'income')

      

    # delete record area ----------------------------------------------------------------------------------------------------------------------------------------------  

    # delete old record

    

    # Sales Details for Incentive Calculation     

    temp_rec_2 = env['x_rm_sales_order_line'].search([('x_studio_sales_report_model_id', '=', record._origin.id)])

    if temp_rec_2:

      for del_temp_rec_2 in temp_rec_2:

        del_temp_rec_2.unlink()

    

    # Business Logic --------------------------------------------------------------------------------------------------------------------------------------------   

    # create new record 

    

    # Sales Details for Incentive Calculation    

    for line in report_type_lines:

      create_sub_model = env['x_rm_sales_order_line'].create({'x_studio_sales_report_model_id':record.id,'x_studio_date':line.date,'x_studio_customer_acc':line.partner_id.id,'x_studio_customer_group':line.partner_id.x_studio_customer_group.id,'x_studio_name':line.partner_id.name,'x_studio_sales_order':line.move_id.x_studio_sale_id.id,'x_studio_invoice':line.move_id.id,'x_studio_product_1':line.product_id.id,'x_studio_product_category':line.product_id.categ_id.id,'x_studio_quantity':line.quantity,'x_studio_unit_price':line.price_unit,'x_studio_net_value':line.price_total})
```
  </details>
- **Execute Code** (`server_action_1761_srm_rpt_production_overview_wip`, type `code`)
  - Function: Run by automation for 'Production Overview - WIP': deletes old rows and lists in-progress manufacturing orders with product, quantities and dates.
  - Depends on: `model x_rm_production_orders`, `model x_sales_report_model` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_name` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_code` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting)
  - Used by: `automation BugFix-Accounting.base_automation_133_srm_rpt_production_overview_wip`
  <details><summary>code (44 lines)</summary>

```python

if record.x_studio_report_type:

  if record.x_studio_report_code == 'Production Overview - WIP':

    report_type_lines = record.x_studio_report_type.x_studio_production_order_id

 

    # filter area ------------------------------------------------------------------------------------------------------------------------------------------------

    report_type_lines = report_type_lines.filtered(lambda x: x.state == 'progress')

    

    # delete record area ----------------------------------------------------------------------------------------------------------------------------------------------  

    # delete old record

    

    # MO - WIP     

    temp_rec_3 = env['x_rm_production_orders'].search([('x_studio_sales_report_model_id', '=', record._origin.id)])

    if temp_rec_3:

      for del_temp_rec_3 in temp_rec_3:

        del_temp_rec_3.unlink()

    

    # Business Logic --------------------------------------------------------------------------------------------------------------------------------------------   

    # create new record 

    

    # Production Overview - WIP

    for line in report_type_lines:

      create_sub_model = env['x_rm_production_orders'].create({'x_studio_sales_report_model_id':record.id,'x_studio_production_id':line.id,'x_studio_product_code':line.product_id.id,'x_studio_description':line.product_id.name,'x_studio_warehouse':line.location_dest_id.id,'x_studio_status':line.state,'x_studio_estimated':line.product_qty,'x_studio_started':line.qty_producing,'x_studio_start':line.date_start,'x_studio_header_reference': record.x_name,'x_studio_end':line.date_finished})
```
  </details>
- **Execute Code** (`server_action_1762_srm_rpt_slow_moving_items`, type `code`)
  - Function: Run by automation for 'Slow Moving Items': totals received and issued quantities per product for the last four months up to As On Date and creates non-moving item rows.
  - Depends on: `model product.product` (product), `model x_rm_none_moving`, `model x_sales_report_model` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_name` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting)<details><summary>+2 more</summary>`x_sales_report_model.x_studio_report_code` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting)</details>
  - Used by: `automation BugFix-Accounting.base_automation_134_srm_rpt_slow_moving_items`
  <details><summary>code (224 lines)</summary>

```python

if record.x_studio_report_type:

  if record.x_studio_report_code == 'Slow Moving Items':

    report_type_lines = record.x_studio_report_type.x_studio_slow_moving_item_id

    

    currentdate = record.x_studio_as_on_date

    

    firstdayOfmonth = datetime.date(currentdate.year, currentdate.month, 1)

    next_month = currentdate.replace(day=28) + datetime.timedelta(days=4)

    lastdayOfmonth = next_month - datetime.timedelta(days=next_month.day)

    

    if firstdayOfmonth.month != 1:

      firstdayOfmonth2 = datetime.date(firstdayOfmonth.year, firstdayOfmonth.month-1, 1)

    else:

      firstdayOfmonth2 = datetime.date(firstdayOfmonth.year-1, 12, 1)

      

    next_month2 = firstdayOfmonth2.replace(day=28) + datetime.timedelta(days=4)

    lastdayOfmonth2 = next_month2 - datetime.timedelta(days=next_month2.day)

    

    if firstdayOfmonth.month > 2:

      firstdayOfmonth3 = datetime.date(firstdayOfmonth.year, firstdayOfmonth.month-2, 1)

    else:

      if firstdayOfmonth.month == 2:

        firstdayOfmonth3 = datetime.date(firstdayOfmonth.year-1, 12, 1)

      else:

        firstdayOfmonth3 = datetime.date(firstdayOfmonth.year-1, 11, 1)

        

    next_month3 = firstdayOfmonth3.replace(day=28) + datetime.timedelta(days=4)

    lastdayOfmonth3 = next_month3 - datetime.timedelta(days=next_month3.day)

    

    if firstdayOfmonth.month > 3:

      firstdayOfmonth4 = datetime.date(firstdayOfmonth.year, firstdayOfmonth.month-3, 1)

    else:

      if firstdayOfmonth.month == 3:

        firstdayOfmonth4 = datetime.date(firstdayOfmonth.year-1, 12, 1)

      elif firstdayOfmonth.month == 2:

        firstdayOfmonth4 = datetime.date(firstdayOfmonth.year-1, 11, 1)

      else:

        firstdayOfmonth4 = datetime.date(firstdayOfmonth.year-1, 10, 1)

        

    next_month4 = firstdayOfmonth4.replace(day=28) + datetime.timedelta(days=4)

    lastdayOfmonth4 = next_month4 - datetime.timedelta(days=next_month4.day)

    

    # filter area ------------------------------------------------------------------------------------------------------------------------------------------------

    report_type_lines_receipt = report_type_lines.filtered(lambda x: (x.date.date() >= firstdayOfmonth and x.date.date() <= lastdayOfmonth and x.picking_code == 'incoming'))

    report_type_lines_delivery = report_type_lines.filtered(lambda x: (x.date.date() >= firstdayOfmonth and x.date.date() <= lastdayOfmonth and x.picking_code == 'outgoing'))

      

    report_type_lines_receipt2 = report_type_lines.filtered(lambda x: (x.date.date() >= firstdayOfmonth2 and x.date.date() <= lastdayOfmonth2 and x.picking_code == 'incoming'))

    report_type_lines_delivery2 = report_type_lines.filtered(lambda x: (x.date.date() >= firstdayOfmonth2 and x.date.date() <= lastdayOfmonth2 and x.picking_code == 'outgoing'))

    

    report_type_lines_receipt3 = report_type_lines.filtered(lambda x: (x.date.date() >= firstdayOfmonth3 and x.date.date() <= lastdayOfmonth3 and x.picking_code == 'incoming'))

    report_type_lines_delivery3 = report_type_lines.filtered(lambda x: (x.date.date() >= firstdayOfmonth3 and x.date.date() <= lastdayOfmonth3 and x.picking_code == 'outgoing'))

      

    report_type_lines_receipt4 = report_type_lines.filtered(lambda x: (x.date.date() >= firstdayOfmonth4 and x.date.date() <= lastdayOfmonth4 and x.picking_code == 'incoming'))

    report_type_lines_delivery4 = report_type_lines.filtered(lambda x: (x.date.date() >= firstdayOfmonth4 and x.date.date() <= lastdayOfmonth4 and x.picking_code == 'outgoing'))

    

    # delete record area ----------------------------------------------------------------------------------------------------------------------------------------------  

    # delete old record

    

    # Slow Moving Items     

    temp_rec_4 = env['x_rm_none_moving'].search([('x_studio_sales_report_model_id', '=', record._origin.id)])
# … 104 more lines
```
  </details>
- **Execute Code** (`server_action_1763_srm_rpt_sales_production_purchase_report`, type `code`)
  - Function: Run by automation for 'Sales - Production - Purchase Report': rebuilds per-product sales, production and purchase quantity rows up to As On Date. Calls `datetime.strptime` on a date, which likely fails.
  - Depends on: `model mrp.production` (mrp), `model product.product` (product), `model purchase.order.line` (purchase), `model sale.order.line` (sale), `model stock.valuation.layer` (stock_account)<details><summary>+6 more</summary>`model x_rm_sales_prod_purch`, `model x_sales_report_model` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_name` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_code` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting)</details>
  - Used by: `automation BugFix-Accounting.base_automation_135_srm_rpt_sales_production_purchase_report`
  <details><summary>code (102 lines)</summary>

```python

if record.x_studio_report_type:

  if record.x_studio_report_code == 'Sales - Production - Purchase Report':

    report_type_lines = record.x_studio_report_type.x_studio_sales_prod_purch_id

  

    # filter area ------------------------------------------------------------------------------------------------------------------------------------------------

    report_type_lines = report_type_lines.filtered(lambda x: (x.date.date() <= record.x_studio_as_on_date))

    

    # delete record area ----------------------------------------------------------------------------------------------------------------------------------------------  

    # delete old record

    

    # Sales - Production - Purchase Report     

    temp_rec_6 = env['x_rm_sales_prod_purch'].search([('x_studio_sales_report_model_id', '=', record._origin.id)])

    if temp_rec_6:

      for del_temp_rec_6 in temp_rec_6:

        del_temp_rec_6.unlink()

    

    # Business Logic --------------------------------------------------------------------------------------------------------------------------------------------   

    # create new record 

    

    # Sales - Production - Purchase Report   

    d = record.x_studio_as_on_date

    #d1 = datetime.strftime(d, "%Y-%m-%d %H:%M:%S")

    #d2 = datetime.strftime(d, "%Y-%m-%d 23:59:59")

    d1 = datetime.strptime(d, "%Y-%m-%d %H:%M:%S")

    d2 = datetime.strptime(d, "%Y-%m-%d 23:59:59")

    product = env['product.product'].search([('type', '!=', 'service')])

    if product:

     for products in product:

       project_qty = 0

       so_qty = 0

       prod_qty = 0

       purch_qty = 0

         

       last_prod_purch = env['stock.valuation.layer'].search([('product_id', '=', products.id),('quantity', '>', 0),('create_date', '>=', d1),('create_date', '<=', d2)],order='create_date desc',limit=1)

         

       sales_qtys = env['sale.order.line'].search([('product_id', '=', products.id)])

       sales_qtys = sales_qtys.filtered(lambda x: x.create_date.date() <= record.x_studio_as_on_date)

       for qtys in sales_qtys:

         so_qty += qtys.product_uom_qty 

           

       prod_qtys = env['mrp.production'].search([('product_id', '=', products.id)])

       prod_qtys = prod_qtys.filtered(lambda x: x.date_planned_start.date() <= record.x_studio_as_on_date)

       for prodqtys in prod_qtys: 

         prod_qty += prodqtys.product_qty

           

       purch_qtys = env['purchase.order.line'].search([('product_id', '=', products.id)])

       purch_qtys = purch_qtys.filtered(lambda x: x.create_date.date() <= record.x_studio_as_on_date)

       for purchqtys in purch_qtys:

         purch_qty += purchqtys.product_qty

           

       create_sub_model = env['x_rm_sales_prod_purch'].create({'x_studio_sales_report_model_id':record.id,'x_studio_description':products.id,'x_studio_base_price':products.list_price,'x_studio_product_type':products.type,'x_studio_date_1':last_prod_purch.create_date.date(),'x_studio_unit_cost':last_prod_purch.unit_cost,'x_studio_project_category':project_qty,'x_studio_sales_order':so_qty,'x_studio_production_qty':prod_qty,'x_studio_purchase_qty':purch_qty,'x_studio_header_reference': record.x_name})
```
  </details>
- **Execute Code** (`server_action_1764_srm_rpt_production_summary_split`, type `code`)
  - Function: Run by automation for 'Production Summary - Split': deletes old rows and creates summary lines for raw-material moves up to As On Date with quantities, variance and cost.
  - Depends on: `model x_rm_prod_summary_spli`, `model x_sales_report_model` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_name` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_code` (Jinasena_Masterdata_Reporting)<details><summary>+1 more</summary>`x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting)</details>
  - Used by: `automation BugFix-Accounting.base_automation_136_srm_rpt_production_summary_split`
  <details><summary>code (44 lines)</summary>

```python

if record.x_studio_report_type:

  if record.x_studio_report_code == 'Production Summary - Split':

    report_type_lines = record.x_studio_report_type.x_studio_prod_summary_split_id

  

    # filter area ------------------------------------------------------------------------------------------------------------------------------------------------

    report_type_lines = report_type_lines.filtered(lambda x: (x.date.date() <= record.x_studio_as_on_date))

    

    # delete record area ----------------------------------------------------------------------------------------------------------------------------------------------  

    # delete old record

    

    # Production Summary - Split     

    temp_rec_7 = env['x_rm_prod_summary_spli'].search([('x_studio_sales_report_model_id', '=', record._origin.id)])

    if temp_rec_7:

      for del_temp_rec_7 in temp_rec_7:

        del_temp_rec_7.unlink()

        

    # Business Logic --------------------------------------------------------------------------------------------------------------------------------------------   

    # create new record 

    

    # Production Summary - Split 

    for line in report_type_lines:

      create_sub_model = env['x_rm_prod_summary_spli'].create({'x_studio_sales_report_model_id':record.id,'x_studio_description':line.raw_material_production_id.product_id.id,'x_studio_production_id':line.raw_material_production_id.id,'x_studio_prod_qty':line.raw_material_production_id.product_qty,'x_studio_description_1':line.product_id.id,'x_studio_bom_qty':line.x_studio_original_qty,'x_studio_esti_qty':line.x_studio_original_qty,'x_studio_cons_qty':line.product_uom_qty,'x_studio_variance':line.x_studio_variance,'x_studio_avg_cost':line.price_unit,'x_studio_total_cost':(line.product_uom_qty*line.price_unit),'x_studio_header_reference': record.x_name})
```
  </details>
- **Execute Code** (`server_action_1765_srm_rpt_production_job_variance`, type `code`)
  - Function: Run by automation for 'Production Job Variance': rebuilds variance rows for raw-material moves with non-zero variance between From Date and As On Date.
  - Depends on: `model x_rm_production_varian`, `model x_sales_report_model` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_name` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_from_date` (Jinasena_Masterdata_Reporting)<details><summary>+2 more</summary>`x_sales_report_model.x_studio_report_code` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting)</details>
  - Used by: `automation BugFix-Accounting.base_automation_137_srm_rpt_production_job_variance`
  <details><summary>code (44 lines)</summary>

```python

if record.x_studio_report_type:

  if record.x_studio_report_code == 'Production Job Variance':

    report_type_lines = record.x_studio_report_type.x_studio_production_variance_id

  

    # filter area ------------------------------------------------------------------------------------------------------------------------------------------------

    report_type_lines = report_type_lines.filtered(lambda x: (x.date.date() >= record.x_studio_from_date and x.date.date() <= record.x_studio_as_on_date and x.x_studio_variance != 0))

    

    # delete record area ----------------------------------------------------------------------------------------------------------------------------------------------  

    # delete old record

    

    # Production Variance     

    temp_rec_5 = env['x_rm_production_varian'].search([('x_studio_sales_report_model_id', '=', record._origin.id)])

    if temp_rec_5:

      for del_temp_rec_5 in temp_rec_5:

        del_temp_rec_5.unlink()

        

    # Business Logic --------------------------------------------------------------------------------------------------------------------------------------------   

    # create new record 

    

    # Production Variance

    for line in report_type_lines:

      create_sub_model = env['x_rm_production_varian'].create({'x_studio_sales_report_model_id':record.id,'x_studio_description':line.raw_material_production_id.product_id.id,'x_studio_production_id':line.raw_material_production_id.id,'x_studio_prod_qty':line.raw_material_production_id.product_qty,'x_studio_description_1':line.product_id.id,'x_studio_bom_qty':line.x_studio_original_qty,'x_studio_esti_qty':line.x_studio_original_qty,'x_studio_cons_qty':line.product_uom_qty,'x_studio_variance':line.x_studio_variance,'x_studio_avg_cost':line.price_unit,'x_studio_total_cost':(line.product_uom_qty*line.price_unit),'x_studio_header_reference': record.x_name})
```
  </details>
- **Execute Code** (`server_action_2102_srm_rpt_project_gross_margin`, type `code`)
  - Function: Run by automation for 'Project Gross Margin': rebuilds estimated, actual, invoiced and comparison gross margin rows per project category from budgets, sales, journal items and payments.
  - Depends on: `model account.move.line` (account), `model account.payment` (account), `model crossovered.budget.lines` (account_budget), `model sale.order.line` (sale), `model sale.order` (sale)<details><summary>+13 more</summary>`model x_project_category` (BugFix-Project), `model x_rm_gross_margin_actu`, `model x_rm_gross_margin_comp`, `model x_rm_gross_margin_esti`, `model x_rm_gross_margin_invo`, `model x_sales_report_model` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_name` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_customer` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_from_date` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_project_no` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_code` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting)</details>
  - Used by: `automation BugFix-Accounting.base_automation_182_srm_rpt_project_gross_margin`
  <details><summary>code (968 lines)</summary>

```python

if record.x_studio_report_type:

  if record.x_studio_report_code == 'Project Gross Margin':

    tot_estimated_val = 0

    tot_actual_val = 0

    tot_balance_val = 0

    tot_estimated_val_1 = 0

    tot_actual_val_1 = 0

    tot_balance_val_1 = 0

    tot_estimated_val_2 = 0

    tot_actual_val_2 = 0

    tot_balance_val_2 = 0

    tot_estimated_val_3 = 0

    tot_actual_val_3 = 0

    tot_balance_val_3 = 0

    tot_estimated_val_4 = 0

    tot_actual_val_4 = 0

    tot_balance_val_4 = 0

    tot_estimated_val_5 = 0

    tot_actual_val_5 = 0

    tot_balance_val_5 = 0

    tot_estimated_val_6 = 0

    tot_actual_val_6 = 0

    tot_balance_val_6 = 0

    tot_estimated_val_7 = 0

    tot_actual_val_7 = 0

    tot_balance_val_7 = 0

    cat_count = 0

    cat_count_2 = 0

    cat_count_3 = 0

    cat_count_4 = 0

    cat_count_5 = 0

    cat_count_6 = 0

    cat_count_7 = 0

    cat_grand_count = 0

    invoice_count = 0

    invoice_total = 0

    on_account_val = 0

    estimated_gp = 0

    actual_gp = 0

    outstanding_cash = 0

    settlement_cash = 0

    outstanding_cash_tot = 0

    temp_actual_lines_2=[]

    temp_actual_lines_3=[]

    temp_actual_lines_4=[]

    temp_actual_lines_5=[]

    temp_actual_lines_6=[]

    temp_actual_budget=[]

    #report_type_lines = record.x_studio_report_type.x_studio_production_variance_id

  

    # filter area ------------------------------------------------------------------------------------------------------------------------------------------------

    #report_type_lines = report_type_lines.filtered(lambda x: (x.date.date() >= record.x_studio_from_date and x.date.date() <= record.x_studio_as_on_date and x.x_studio_variance != 0))

    

    # delete record area ----------------------------------------------------------------------------------------------------------------------------------------------  

    # delete old record

    

    # Project Gross Margin - Estimated    

    temp_rec_1 = env['x_rm_gross_margin_esti'].search([('x_studio_sales_report_model_id', '=', record._origin.id)])

    if temp_rec_1:

      for del_temp_rec_1 in temp_rec_1:
# … 848 more lines
```
  </details>
- **Execute Code** (`server_action_2126_report_model_created_date`, type `code`)
  - Function: Run by automation: stamps the Sales Report Model's Created Date with the current date and time.
  - Depends on: `model x_sales_report_model` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_created_date` (Jinasena_Masterdata_Reporting)
  - Used by: `automation BugFix-Accounting.base_automation_188_report_model_created_date`
  <details><summary>code (2 lines)</summary>

```python

record['x_studio_created_date'] = datetime.datetime.today()
```
  </details>
- **Execute Code** (`server_action_2490_srm_rpt_costing_work_sheet`, type `code`)
  - Function: Run by automation for 'Costing Work Sheet': deletes old rows and rebuilds Pump Price Costing lines for all Pump products of the active company using BoMs, pricelists, MOs and journal items.
  - Depends on: `model account.move.line` (account), `model mrp.bom` (mrp), `model mrp.production` (mrp), `model product.pricelist.item` (product), `model product.pricelist` (product)<details><summary>+23 more</summary>`model product.template` (product), `model res.company` (base), `model x_pump_price_costing`, `model x_sales_report_model` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_as_on_date_1` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_as_on_date_2` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_contingency_` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_distributor_addition` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_factory_oh_labour` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_factory_oh` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_idling_rate` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_oh_absorbed_2_factory` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_oh_absorbed_2_other` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_oh_absorbed_2_sales` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_oh_absorbed_factory` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_oh_absorbed_other` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_oh_absorbed_sales` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_other_oh` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_profit_mark_up_` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_code` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_sales_oh` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_sscl` (Jinasena_Masterdata_Reporting)</details>
  - Used by: `automation BugFix-Accounting.base_automation_248_srm_rpt_costing_work_sheet`
  <details><summary>code (526 lines)</summary>

```python

if record.x_studio_report_type:

  if record.x_studio_report_code == 'Costing Work Sheet':

    

    company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]

    company = env['res.company'].browse(company_id)

    

    # Project Gross Margin - Estimated    

    temp_rec_1 = env['x_pump_price_costing'].search([('x_studio_sales_report_model_id', '=', record._origin.id)])

    if temp_rec_1:

      for del_temp_rec_1 in temp_rec_1:

        del_temp_rec_1.unlink()

    

    # Business Logic --------------------------------------------------------------------------------------------------------------------------------------------   

    # create new record 

    

    # Pump Price Costing

    # Tab - 01 //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    

    pump = env['product.template'].search([('x_studio_product_type', '=', 'Pump'),('company_id', '=', company.id)])

    for pumps in pump:

      standard_count = 0

      standard_final = 0

      standard_count2 = 0

      standard_final2 = 0

      current_base_price = 0

      current_base_price_date = False

      discount = 0

      sscl = 0

      cost_import = 0

      cost_other = 0

      contingency_rs = 0

      total_cost = 0

      labour = 0

      factory_oh = 0

      total_factory_cost = 0

      total_factory_cost_a = 0

      net_selling_price = 0

      actual = 0

      actual_1 = 0

      #######

      contribution_rs = 0

      contribution_2 = 0

      sales_oh = 0

      sales_oh_rs = 0

      other_oh = 0

      other_oh_rs = 0

      profitloss_as_of_net_sale = 0

      current_retail_price_vat_18 = 0

      total_material_cost = 0

      oh_absorbed_factory = 0

      oh_absorbed_sales = 0

      oh_absorbed_other = 0

      profit_mark_up_ = 0

      profit_mark_up_rs = 0

      net_selling_price_1 = 0

      sscl_1 = 0

      max_discount_1 = 0

      proposed_base_price = 0

      current_base_price = 0

      difference = 0
# … 406 more lines
```
  </details>
- **Project Gross Margin - Delete Reports** (`server_action_2127_project_gross_margin_delete_reports`, type `code`)
  - Function: Deletes 'Project Gross Margin' Sales Report Models created on or before the end of the month two months before the current month.
  - Depends on: `model x_sales_report_model` (Jinasena_Masterdata_Reporting), `model x_sales_report_type` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_created_date` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_code` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (32 lines)</summary>

```python

report_type = env['x_sales_report_type'].search([('x_studio_report_code', '=', 'Project Gross Margin')])
if report_type:
  currentdate = datetime.datetime.today()
      
  firstdayOfmonth = datetime.date(currentdate.year, currentdate.month, 1)
  next_month = currentdate.replace(day=28) + datetime.timedelta(days=4)
  lastdayOfmonth = next_month - datetime.timedelta(days=next_month.day)
      
  if firstdayOfmonth.month != 1:
    firstdayOfmonth2 = datetime.date(firstdayOfmonth.year, firstdayOfmonth.month-1, 1)
  else:
    firstdayOfmonth2 = datetime.date(firstdayOfmonth.year-1, 12, 1)
    
  next_month2 = firstdayOfmonth2.replace(day=28) + datetime.timedelta(days=4)
  lastdayOfmonth2 = next_month2 - datetime.timedelta(days=next_month2.day)
  
  if firstdayOfmonth.month > 2:
    firstdayOfmonth3 = datetime.date(firstdayOfmonth.year, firstdayOfmonth.month-2, 1)
  else:
    if firstdayOfmonth.month == 2:
      firstdayOfmonth3 = datetime.date(firstdayOfmonth.year-1, 12, 1)
    else:
      firstdayOfmonth3 = datetime.date(firstdayOfmonth.year-1, 11, 1)
          
  next_month3 = firstdayOfmonth3.replace(day=28) + datetime.timedelta(days=4)
  lastdayOfmonth3 = next_month3 - datetime.timedelta(days=next_month3.day)
  
  delete_report_model = env['x_sales_report_model'].search([('x_studio_report_type', '=', report_type.id),('x_studio_created_date', '<=', lastdayOfmonth3)])
  if delete_report_model:
      for delete_report in delete_report_model:
        delete_report.unlink()
```
  </details>
- **Project Gross Margin Report** (`server_action_2116_project_gross_margin_report`, type `code`)
  - Function: Creates a new auto-generated 'Project Gross Margin' Sales Report Model for a hard-coded project id 2466.
  - Depends on: `model x_sales_report_model` (Jinasena_Masterdata_Reporting), `model x_sales_report_type` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_auto_generated` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_project_no` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_code` (Jinasena_Masterdata_Reporting)<details><summary>+1 more</summary>`x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting)</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (4 lines)</summary>

```python

report_type = env['x_sales_report_type'].search([('x_studio_report_code', '=', 'Project Gross Margin')])
if report_type:
  create_report_model = env['x_sales_report_model'].create({'x_studio_report_type':report_type.id,'x_studio_project_no':2466,'x_studio_auto_generated':True})
```
  </details>
- **Project Gross Margin Report - Management Purpose** (`server_action_2128_project_gross_margin_report_management_purpose`, type `code`)
  - Function: Creates a 'Project Gross Margin' Sales Report Model flagged for management purpose for a hard-coded project id 2466.
  - Depends on: `model x_sales_report_model` (Jinasena_Masterdata_Reporting), `model x_sales_report_type` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_management_purpose` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_project_no` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_code` (Jinasena_Masterdata_Reporting)<details><summary>+1 more</summary>`x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting)</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (4 lines)</summary>

```python

report_type = env['x_sales_report_type'].search([('x_studio_report_code', '=', 'Project Gross Margin')])
if report_type:
  create_report_model = env['x_sales_report_model'].create({'x_studio_report_type':report_type.id,'x_studio_project_no':2466,'x_studio_management_purpose':True})
```
  </details>
- **RPT - Customer wise Invoices - Clear** (`server_action_1681_rpt_customer_wise_invoices_clear`, type `code`)
  - Function: Deletes the Customer-wise Invoices report rows (summary and detail) of the Sales Report Model and resets its status to Draft.
  - Depends on: `model x_rm_cust_invoice_s1`, `model x_rm_customer_wise_inv`, `model x_sales_report_model` (Jinasena_Masterdata_Reporting)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (12 lines)</summary>

```python
if record.id:
  temp_rec = env['x_rm_customer_wise_inv'].search([('x_studio_sales_report_model_id', '=', record.id)])
  if temp_rec:
    for del_temp_rec in temp_rec:
      del_temp_rec.unlink()  
      
    temp_rec_1 = env['x_rm_cust_invoice_s1'].search([('x_studio_sales_report_model_id', '=', record.id)])
    if temp_rec_1:
      for del_temp_rec_1 in temp_rec_1:
        del_temp_rec_1.unlink()

    record['x_studio_selection_field_Fbw0x'] = 'Draft'
```
  </details>
- **RPT - Customer wise Invoices - Generate** (`server_action_1680_rpt_customer_wise_invoices_generate`, type `code`)
  - Function: Builds the Customer-wise Invoices report for As On Date: per selected (or all) customer creates detail rows for posted invoice lines and a total row; errors if nothing found, then sets status Done. Filters on Odoo 14 field `exclude_from_invoice_tab`.
  - Depends on: `model account.move.line` (account), `model res.partner` (base), `model x_rm_cust_invoice_s1`, `model x_rm_customer_wise_inv`, `model x_sales_report_model` (Jinasena_Masterdata_Reporting)<details><summary>+3 more</summary>`x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_customer` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_sales_centre` (Jinasena_Masterdata_Reporting)</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (30 lines)</summary>

```python
if record.id:
  today = datetime.date.today()
  count = 0
  c = 0
  if not record.x_studio_customer:
    customer = env['res.partner'].search([])
  else:
    vals = []
    for filter in record.x_studio_customer:
      c += 1
      vals.insert(c,filter.id)

    customer = env['res.partner'].search([('id', '=', vals)])
    
  if customer:
    for customers in customer:
      net_inv_val_day = 0
      invoice_line =  env['account.move.line'].search([('partner_id', '=', customers.id), ('x_studio_invoice_date', '=', record.x_studio_as_on_date), ('x_studio_status', '=', 'posted'), ('exclude_from_invoice_tab', '=', False)])
      if invoice_line:
        for invoice_lines in invoice_line:
          count += 1
          net_inv_val_day += invoice_lines.price_subtotal
          create_sub_model = env['x_rm_cust_invoice_s1'].create({'x_studio_sales_report_model_id':record.id,'x_studio_invoice_date':invoice_lines.date,'x_studio_number':invoice_lines.move_name,'x_studio_partner':invoice_lines.partner_id.id,'x_studio_sales_centre':invoice_lines.x_studio_sales_team.id,'x_studio_product_id':invoice_lines.product_id.id,'x_studio_quantity':invoice_lines.quantity,'x_studio_value':invoice_lines.price_subtotal})
  
        create_model = env['x_rm_customer_wise_inv'].create({'x_studio_sales_report_model_id':record.id,'x_studio_customer':customers.id,'x_studio_total_invoice_amount':net_inv_val_day})

  if count == 0:
    raise UserError('No Data to Populate.')
  
  record['x_studio_selection_field_Fbw0x'] = 'Done'
```
  </details>
- **RPT - Daily Sales Report - Clear** (`server_action_1671_rpt_daily_sales_report_clear`, type `code`)
  - Function: Deletes the Daily Sales Report rows (summary and detail) of the Sales Report Model and resets its status to Draft.
  - Depends on: `model x_rm_daily_s1`, `model x_rm_daily_sales_repor`, `model x_sales_report_model` (Jinasena_Masterdata_Reporting)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (12 lines)</summary>

```python
if record.id:
  temp_rec = env['x_rm_daily_sales_repor'].search([('x_studio_sales_report_model_id', '=', record.id)])
  if temp_rec:
    for del_temp_rec in temp_rec:
      del_temp_rec.unlink()   
      
    temp_rec_1 = env['x_rm_daily_s1'].search([('x_studio_sales_report_model_id', '=', record.id)])
    if temp_rec_1:
      for del_temp_rec_1 in temp_rec_1:
        del_temp_rec_1.unlink() 
  
    record['x_studio_selection_field_Fbw0x'] = 'Draft'
```
  </details>
- **RPT - Daily Sales Report - Clear - TEST** (`server_action_1710_rpt_daily_sales_report_clear_test`, type `code`)
  - Function: Test variant of the Daily Sales Report clear: deletes the detail rows (x_rm_daily_s1) and resets status to Draft.
  - Depends on: `model x_rm_daily_s1`, `model x_sales_report_model` (Jinasena_Masterdata_Reporting)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (9 lines)</summary>

```python
if record.id:
  c = 0
  temp_rec_1 = env['x_rm_daily_s1'].search([('x_studio_sales_report_model_id', '=', record.id)])
  if temp_rec_1:
    for del_temp_rec_1 in temp_rec_1:
      c += 1
      del_temp_rec_1.unlink() 
  #raise UserError(c)
  record['x_studio_selection_field_Fbw0x'] = 'Draft'
```
  </details>
- **RPT - Daily Sales Report - Generate** (`server_action_1670_rpt_daily_sales_report_generate`, type `code`)
  - Function: Builds the Daily Sales Report for As On Date per sales centre from posted invoice lines; summary rows use hard-coded month, target and achievement figures (e.g. 45000, 100000). Errors if no data, then sets status Done.
  - Depends on: `model account.move.line` (account), `model crm.team` (sales_team), `model x_rm_daily_s1`, `model x_rm_daily_sales_repor`, `model x_sales_report_model` (Jinasena_Masterdata_Reporting)<details><summary>+2 more</summary>`x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_sales_centre` (Jinasena_Masterdata_Reporting)</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (30 lines)</summary>

```python
if record.id:
  today = datetime.date.today()
  count = 0
  c = 0
  if not record.x_studio_sales_centre:
    sales_centre = env['crm.team'].search([],order="name asc")
  else:
    vals = []
    for filter in record.x_studio_sales_centre:
      c += 1
      vals.insert(c,filter.id)

    sales_centre = env['crm.team'].search([('id', '=', vals)],order="name asc")
    
  if sales_centre:
    for sales_centres in sales_centre:
      net_inv_val_day = 0
      invoice_line =  env['account.move.line'].search([('x_studio_sales_team', '=', sales_centres.id), ('x_studio_invoice_date', '=', record.x_studio_as_on_date), ('x_studio_status', '=', 'posted'), ('exclude_from_invoice_tab', '=', False)])
      if invoice_line:
        for invoice_lines in invoice_line:
          count += 1
          net_inv_val_day += invoice_lines.price_subtotal
          create_sub_model = env['x_rm_daily_s1'].create({'x_studio_sales_report_model_id':record.id,'x_studio_invoice_date':invoice_lines.date,'x_studio_number':invoice_lines.move_name,'x_studio_partner':invoice_lines.partner_id.id,'x_studio_sales_centre':invoice_lines.x_studio_sales_team.id,'x_studio_product_id':invoice_lines.product_id.id,'x_studio_quantity':invoice_lines.quantity,'x_studio_value':invoice_lines.price_subtotal})
  
        create_model = env['x_rm_daily_sales_repor'].create({'x_studio_sales_report_model_id':record.id,'x_studio_sales_centre':sales_centres.name,'x_studio_net_invoice_value_day':net_inv_val_day,'x_studio_net_invoice_value_month':45000,'x_studio_net_invoice_value_cumulative':175000,'x_studio_m_sales_target':100000,'x_studio_s_target_cumulative':500000,'x_studio_achievement_':12,'x_studio_achieve_cumulative_':23})

  if count == 0:
    raise UserError('No Data to Populate.')
  
  record['x_studio_selection_field_Fbw0x'] = 'Done'
```
  </details>
- **RPT - Sample Button** (`srv_sales_report_sample_button`, type `code`)
  - Function: No-op placeholder action behind the RPT Sample Button on the Sales Report Model form; does nothing.
  - Depends on: `model x_sales_report_model` (Jinasena_Masterdata_Reporting)
  - Used by: `view BugFix-Accounting.ported_view_3784_default_form_view_fo_d583be6a_921f_4205_94a7_603a2375ce6e`
  <details><summary>code (1 lines)</summary>

```python
action = None  # No-op template action from Clear-DB (Studio scaffold).
```
  </details>
- **RPT - Sample Button** (`server_action_1676_rpt_sample_button`, type `object_write`)
  - Function: Legacy 'update record' action for the RPT Sample Button with no field or value configured; does nothing and is not referenced.
  - Depends on: `model x_sales_report_model` (Jinasena_Masterdata_Reporting)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **Report Model Created Date** (`sa_f5_x_sales_report_model_report_model_created_date`, type `code`)
  - Function: Stamps the Sales Report Model's Created Date with the current date and time.
  - Depends on: `model x_sales_report_model` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_created_date` (Jinasena_Masterdata_Reporting)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (1 lines)</summary>

```python
record['x_studio_created_date'] = datetime.datetime.today()
```
  </details>
- **Report Model Seq.No** (`sa_f5_x_sales_report_model_report_model_seq_no`, type `code`)
  - Function: When the Sales Report Model's Name is still 'New', assigns the next number from the 'report.model.seq' sequence.
  - Depends on: `model ir.sequence` (base), `model x_sales_report_model` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_name` (Jinasena_Masterdata_Reporting)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (5 lines)</summary>

```python
#record['x_name'] = env['ir.sequence'].next_by_code('purchase.request.seq')

if record.x_name == 'New':
    seq = env['ir.sequence'].next_by_code('report.model.seq')
    record.write({'x_name': seq})
```
  </details>
- **Restrict Delete in Sales Report Model** (`sa_f5_x_sales_report_model_restrict_delete_in_sales_report_model`, type `code`)
  - Function: Blocks deletion of a Sales Report Model whose status field is 'Done' (the error text says the opposite: 'only delete ... in done state').
  - Depends on: `model x_sales_report_model` (Jinasena_Masterdata_Reporting)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (2 lines)</summary>

```python
if record.x_studio_selection_field_Fbw0x == 'Done':
  raise UserError("You can only delete a report model if the report model is in done state.")
```
  </details>
- **SRM - Auto Delete Sub Models** (`sa_f5_x_sales_report_model_srm_auto_delete_sub_models`, type `code`)
  - Function: Deletes the report's generated sub-records (production orders, non-moving items, sales-production-purchase, production summary split and production variance lines) linked to this Sales Report Model.
  - Depends on: `model x_rm_none_moving`, `model x_rm_prod_summary_spli`, `model x_rm_production_orders`, `model x_rm_production_varian`, `model x_rm_sales_prod_purch`<details><summary>+1 more</summary>`model x_sales_report_model` (Jinasena_Masterdata_Reporting)</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (20 lines)</summary>

```python
if record.id:
  temp_rec = env['x_rm_production_orders'].search([('x_studio_sales_report_model_id', '=', record.id)])
  for del_record in temp_rec:
    del_record.unlink()
    
  temp_rec2 = env['x_rm_none_moving'].search([('x_studio_sales_report_model_id', '=', record.id)])
  for del_record2 in temp_rec2:
    del_record2.unlink()
    
  temp_rec3 = env['x_rm_sales_prod_purch'].search([('x_studio_sales_report_model_id', '=', record.id)])
  for del_record3 in temp_rec3:
    del_record3.unlink()
    
  temp_rec4 = env['x_rm_prod_summary_spli'].search([('x_studio_sales_report_model_id', '=', record.id)])
  for del_record4 in temp_rec4:
    del_record4.unlink()
    
  temp_rec5 = env['x_rm_production_varian'].search([('x_studio_sales_report_model_id', '=', record.id)])
  for del_record5 in temp_rec5:
    del_record5.unlink()
```
  </details>
- **SRM - Auto Populate Data** (`server_action_1726_srm_auto_populate_data`, type `code`)
  - Function: Run by the SRM Auto Populate automation: depending on report code (WIP, Job Variance, Sales-Production-Purchase, Summary Split, Slow Moving), deletes old report rows and regenerates them from the report type's source lines.
  - Depends on: `model mrp.production` (mrp), `model product.product` (product), `model purchase.order.line` (purchase), `model sale.order.line` (sale), `model stock.valuation.layer` (stock_account)<details><summary>+14 more</summary>`model x_rm_daily_s1`, `model x_rm_none_moving`, `model x_rm_prod_summary_spli`, `model x_rm_production_orders`, `model x_rm_production_varian`, `model x_rm_sales_order_line`, `model x_rm_sales_prod_purch`, `model x_sales_report_model` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_name` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_from_date` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_code` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_sales_centre` (Jinasena_Masterdata_Reporting)</details>
  - Used by: `automation BugFix-Accounting.base_automation_116_srm_auto_populate_data`
  <details><summary>code (483 lines)</summary>

```python
if record.x_studio_report_type:

  if record.x_studio_report_code == 'Production Overview - WIP':

    report_type_lines = record.x_studio_report_type.x_studio_production_order_id

  elif record.x_studio_report_code == 'Production Job Variance':

    report_type_lines = record.x_studio_report_type.x_studio_production_variance_id

  elif record.x_studio_report_code == 'Sales - Production - Purchase Report':

    report_type_lines = record.x_studio_report_type.x_studio_sales_prod_purch_id

  elif record.x_studio_report_code == 'Production Summary - Split':

    report_type_lines = record.x_studio_report_type.x_studio_prod_summary_split_id

  elif record.x_studio_report_code == 'Slow Moving Items':

    report_type_lines = record.x_studio_report_type.x_studio_slow_moving_item_id

    

    currentdate = record.x_studio_as_on_date

    

    firstdayOfmonth = datetime.date(currentdate.year, currentdate.month, 1)

    next_month = currentdate.replace(day=28) + datetime.timedelta(days=4)

    lastdayOfmonth = next_month - datetime.timedelta(days=next_month.day)

    

    if firstdayOfmonth.month != 1:

      firstdayOfmonth2 = datetime.date(firstdayOfmonth.year, firstdayOfmonth.month-1, 1)

    else:

      firstdayOfmonth2 = datetime.date(firstdayOfmonth.year-1, 12, 1)

      

    next_month2 = firstdayOfmonth2.replace(day=28) + datetime.timedelta(days=4)

    lastdayOfmonth2 = next_month2 - datetime.timedelta(days=next_month2.day)

    

    if firstdayOfmonth.month > 2:

      firstdayOfmonth3 = datetime.date(firstdayOfmonth.year, firstdayOfmonth.month-2, 1)

    else:

      if firstdayOfmonth.month == 2:

        firstdayOfmonth3 = datetime.date(firstdayOfmonth.year-1, 12, 1)

      else:

        firstdayOfmonth3 = datetime.date(firstdayOfmonth.year-1, 11, 1)

        

    next_month3 = firstdayOfmonth3.replace(day=28) + datetime.timedelta(days=4)

    lastdayOfmonth3 = next_month3 - datetime.timedelta(days=next_month3.day)

    

    if firstdayOfmonth.month > 3:

      firstdayOfmonth4 = datetime.date(firstdayOfmonth.year, firstdayOfmonth.month-3, 1)

    else:

      if firstdayOfmonth.month == 3:

        firstdayOfmonth4 = datetime.date(firstdayOfmonth.year-1, 12, 1)

      elif firstdayOfmonth.month == 2:

        firstdayOfmonth4 = datetime.date(firstdayOfmonth.year-1, 11, 1)

      else:

        firstdayOfmonth4 = datetime.date(firstdayOfmonth.year-1, 10, 1)

        

    next_month4 = firstdayOfmonth4.replace(day=28) + datetime.timedelta(days=4)

    lastdayOfmonth4 = next_month4 - datetime.timedelta(days=next_month4.day)

    

  else:

    report_type_lines = record.x_studio_report_type.x_studio_journal_items_id

    

  # filter area ------------------------------------------------------------------------------------------------------------------------------------------------

  if record.x_studio_report_code == 'Production Overview - WIP':

    report_type_lines = report_type_lines.filtered(lambda x: x.state == 'progress')

  elif record.x_studio_report_code == 'Production Job Variance':

    report_type_lines = report_type_lines.filtered(lambda x: (x.date.date() >= record.x_studio_from_date and x.date.date() <= record.x_studio_as_on_date and x.x_studio_variance != 0))

  elif record.x_studio_report_code == 'Sales - Production - Purchase Report':

    report_type_lines = report_type_lines.filtered(lambda x: (x.date.date() <= record.x_studio_as_on_date))

# … 363 more lines
```
  </details>
- **SRM - Auto Populate Data** (`server_action_1709_srm_auto_populate_data`, type `code`)
  - Function: Early version of SRM Auto Populate: deletes old daily summary rows and recreates one per journal item linked on the report model.
  - Depends on: `model x_rm_daily_s1`, `model x_sales_report_model` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_journal_item_ids` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting)<details><summary>+1 more</summary>`x_sales_report_model.x_studio_sales_centre` (Jinasena_Masterdata_Reporting)</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (20 lines)</summary>

```python
if record.x_studio_report_type:
  count = 0
  c=0
  temp_rec_1 = env['x_rm_daily_s1'].search([('x_studio_sales_report_model_id', '=', record._origin.id)])
  if temp_rec_1:
    for del_temp_rec_1 in temp_rec_1:
      c += 1
      del_temp_rec_1.unlink() 
  
  for invoice_lines in record.x_studio_journal_item_ids:
  #  if invoice_lines.date == record.x_studio_as_on_date:
  #    count += 1
    create_sub_model = env['x_rm_daily_s1'].create({'x_studio_sales_report_model_id':record.id,'x_studio_invoice_date':invoice_lines.date,'x_studio_number':invoice_lines.move_name,'x_studio_partner':invoice_lines.partner_id.id,'x_studio_sales_centre':invoice_lines.x_studio_sales_team.id,'x_studio_product_id':invoice_lines.product_id.id,'x_studio_quantity':invoice_lines.quantity,'x_studio_value':invoice_lines.price_subtotal})
      
  
 
  #if count == 0:
    #raise UserError('No Data to Populate.')
  
  #record['x_studio_selection_field_Fbw0x'] = 'Done'
```
  </details>
- **SRM - Auto Populate Data - 2** (`server_action_1711_srm_auto_populate_data_2`, type `code`)
  - Function: Variant that only deletes the report's existing daily summary rows (x_rm_daily_s1) without regenerating them.
  - Depends on: `model x_rm_daily_s1`, `model x_sales_report_model` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (7 lines)</summary>

```python
if record.x_studio_report_type:
  temp_rec_1 = env['x_rm_daily_s1'].search([('x_studio_sales_report_model_id', '=', record._origin.id)])
  if temp_rec_1:
    for del_temp_rec_1 in temp_rec_1:
      del_temp_rec_1.unlink() 
  
  #record['x_studio_selection_field_Fbw0x'] = 'Done'
```
  </details>
- **SRM - Auto Populate Data - TAU** (`server_action_1727_srm_auto_populate_data_tau`, type `code`)
  - Function: Variant of SRM Auto Populate: filters the report type's journal items by As On Date and Sales Centre, deletes old rows and creates daily summary rows.
  - Depends on: `model x_rm_daily_s1`, `model x_sales_report_model` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_sales_centre` (Jinasena_Masterdata_Reporting)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (16 lines)</summary>

```python
if record.x_studio_report_type:
  report_type_lines = record.x_studio_report_type.x_studio_journal_items_id
  # filter by As on date
  if record.x_studio_as_on_date:
    report_type_lines = report_type_lines.filtered(lambda x: x.date == record.x_studio_as_on_date)
  # filter by sales centre
  if record.x_studio_sales_centre:
    report_type_lines = report_type_lines.filtered(lambda x: x.x_studio_sales_team == record.x_studio_sales_centre)
  # delete old record
  temp_rec_1 = env['x_rm_daily_s1'].search([('x_studio_sales_report_model_id', '=', record._origin.id)])
  if temp_rec_1:
    for del_temp_rec_1 in temp_rec_1:
      del_temp_rec_1.unlink()
  # create new record
  for line in report_type_lines:
    create_sub_model = env['x_rm_daily_s1'].create({'x_studio_sales_report_model_id':record.id,'x_studio_invoice_date':line.date,'x_studio_number':line.move_name,'x_studio_partner':line.partner_id.id,'x_studio_sales_centre':line.x_studio_sales_team.id,'x_studio_product_id':line.product_id.id,'x_studio_quantity':line.quantity,'x_studio_value':line.price_subtotal})
```
  </details>
- **SRM - Auto Populate Data-Original** (`server_action_1730_srm_auto_populate_data_original`, type `code`)
  - Function: Original SRM Auto Populate: filters the report type's journal items by As On Date and Sales Centre, deletes old rows and creates daily summary rows.
  - Depends on: `model x_rm_daily_s1`, `model x_sales_report_model` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_sales_centre` (Jinasena_Masterdata_Reporting)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (16 lines)</summary>

```python
if record.x_studio_report_type:
  report_type_lines = record.x_studio_report_type.x_studio_journal_items_id
  # filter by as on date
  if record.x_studio_as_on_date:
    report_type_lines = report_type_lines.filtered(lambda x: x.date == record.x_studio_as_on_date)
  # filter by sales centre
  if record.x_studio_sales_centre:
    report_type_lines = report_type_lines.filtered(lambda x: x.x_studio_sales_team == record.x_studio_sales_centre)
  # delete old record
  temp_rec_1 = env['x_rm_daily_s1'].search([('x_studio_sales_report_model_id', '=', record._origin.id)])
  if temp_rec_1:
    for del_temp_rec_1 in temp_rec_1:
      del_temp_rec_1.unlink()
  # create new record (Business Logic)
  for line in report_type_lines:
    create_sub_model = env['x_rm_daily_s1'].create({'x_studio_sales_report_model_id':record.id,'x_studio_invoice_date':line.date,'x_studio_number':line.move_name,'x_studio_partner':line.partner_id.id,'x_studio_sales_centre':line.x_studio_sales_team.id,'x_studio_product_id':line.product_id.id,'x_studio_quantity':line.quantity,'x_studio_value':line.price_subtotal})
```
  </details>
- **SRM - RPT - Costing Work Sheet** (`sa_f5_x_sales_report_model_srm_rpt_costing_work_sheet`, type `code`)
  - Function: For report code 'Costing Work Sheet': deletes old rows and rebuilds Pump Price Costing lines for every Pump product of the active company, using BoMs, pricelists, manufacturing orders and journal items to compute costs and selling prices.
  - Depends on: `model account.move.line` (account), `model mrp.bom` (mrp), `model mrp.production` (mrp), `model product.pricelist.item` (product), `model product.pricelist` (product)<details><summary>+23 more</summary>`model product.template` (product), `model res.company` (base), `model x_pump_price_costing`, `model x_sales_report_model` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_as_on_date_1` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_as_on_date_2` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_contingency_` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_distributor_addition` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_factory_oh_labour` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_factory_oh` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_idling_rate` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_oh_absorbed_2_factory` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_oh_absorbed_2_other` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_oh_absorbed_2_sales` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_oh_absorbed_factory` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_oh_absorbed_other` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_oh_absorbed_sales` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_other_oh` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_profit_mark_up_` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_code` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_sales_oh` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_sscl` (Jinasena_Masterdata_Reporting)</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (525 lines)</summary>

```python
if record.x_studio_report_type:

  if record.x_studio_report_code == 'Costing Work Sheet':

    

    company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]

    company = env['res.company'].browse(company_id)

    

    # Project Gross Margin - Estimated    

    temp_rec_1 = env['x_pump_price_costing'].search([('x_studio_sales_report_model_id', '=', record._origin.id)])

    if temp_rec_1:

      for del_temp_rec_1 in temp_rec_1:

        del_temp_rec_1.unlink()

    

    # Business Logic --------------------------------------------------------------------------------------------------------------------------------------------   

    # create new record 

    

    # Pump Price Costing

    # Tab - 01 //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    

    pump = env['product.template'].search([('x_studio_product_type', '=', 'Pump'),('company_id', '=', company.id)])

    for pumps in pump:

      standard_count = 0

      standard_final = 0

      standard_count2 = 0

      standard_final2 = 0

      current_base_price = 0

      current_base_price_date = False

      discount = 0

      sscl = 0

      cost_import = 0

      cost_other = 0

      contingency_rs = 0

      total_cost = 0

      labour = 0

      factory_oh = 0

      total_factory_cost = 0

      total_factory_cost_a = 0

      net_selling_price = 0

      actual = 0

      actual_1 = 0

      #######

      contribution_rs = 0

      contribution_2 = 0

      sales_oh = 0

      sales_oh_rs = 0

      other_oh = 0

      other_oh_rs = 0

      profitloss_as_of_net_sale = 0

      current_retail_price_vat_18 = 0

      total_material_cost = 0

      oh_absorbed_factory = 0

      oh_absorbed_sales = 0

      oh_absorbed_other = 0

      profit_mark_up_ = 0

      profit_mark_up_rs = 0

      net_selling_price_1 = 0

      sscl_1 = 0

      max_discount_1 = 0

      proposed_base_price = 0

      current_base_price = 0

      difference = 0

# … 405 more lines
```
  </details>
- **SRM - RPT - Daily Sales Summary** (`sa_f5_x_sales_report_model_srm_rpt_daily_sales_summary`, type `code`)
  - Function: For report code 'Daily Sales Summary': filters the report type's journal items by As On Date (and Sales Centre), deletes old rows and creates one x_rm_daily_s1 row per item with date, number, partner, product, quantity and value.
  - Depends on: `model x_rm_daily_s1`, `model x_sales_report_model` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_code` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting)<details><summary>+1 more</summary>`x_sales_report_model.x_studio_sales_centre` (Jinasena_Masterdata_Reporting)</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (55 lines)</summary>

```python
if record.x_studio_report_type:

  if record.x_studio_report_code == 'Daily Sales Summary':

    report_type_lines = record.x_studio_report_type.x_studio_journal_items_id

    

    # filter area ------------------------------------------------------------------------------------------------------------------------------------------------

    # filter by as on date

    if record.x_studio_as_on_date:

      report_type_lines = report_type_lines.filtered(lambda x: x.date == record.x_studio_as_on_date)

      

    # filter by sales centre

      if record.x_studio_sales_centre:

        report_type_lines = report_type_lines.filtered(lambda x: x.x_studio_sales_team == record.x_studio_sales_centre)

          

    # delete record area ----------------------------------------------------------------------------------------------------------------------------------------------  

    # delete old record

    

    # Daily Sales Summary

    temp_rec_1 = env['x_rm_daily_s1'].search([('x_studio_sales_report_model_id', '=', record._origin.id)])

    if temp_rec_1:

      for del_temp_rec_1 in temp_rec_1:

        del_temp_rec_1.unlink()

    

    # Business Logic --------------------------------------------------------------------------------------------------------------------------------------------   

    # create new record 

    

    # Daily Sales Summary

    for line in report_type_lines:

      create_sub_model = env['x_rm_daily_s1'].create({'x_studio_sales_report_model_id':record.id,'x_studio_invoice_date':line.date,'x_studio_number':line.move_name,'x_studio_partner':line.partner_id.id,'x_studio_sales_centre':line.x_studio_sales_team.id,'x_studio_product_id':line.product_id.id,'x_studio_quantity':line.quantity,'x_studio_value':line.price_subtotal})
```
  </details>
- **SRM - RPT - Production Job Variance** (`sa_f5_x_sales_report_model_srm_rpt_production_job_variance`, type `code`)
  - Function: For report code 'Production Job Variance': takes raw-material moves with non-zero variance between From Date and As On Date, deletes old rows and creates variance lines with BoM, estimated and consumed quantity and cost.
  - Depends on: `model x_rm_production_varian`, `model x_sales_report_model` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_name` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_from_date` (Jinasena_Masterdata_Reporting)<details><summary>+2 more</summary>`x_sales_report_model.x_studio_report_code` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting)</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (43 lines)</summary>

```python
if record.x_studio_report_type:

  if record.x_studio_report_code == 'Production Job Variance':

    report_type_lines = record.x_studio_report_type.x_studio_production_variance_id

  

    # filter area ------------------------------------------------------------------------------------------------------------------------------------------------

    report_type_lines = report_type_lines.filtered(lambda x: (x.date.date() >= record.x_studio_from_date and x.date.date() <= record.x_studio_as_on_date and x.x_studio_variance != 0))

    

    # delete record area ----------------------------------------------------------------------------------------------------------------------------------------------  

    # delete old record

    

    # Production Variance     

    temp_rec_5 = env['x_rm_production_varian'].search([('x_studio_sales_report_model_id', '=', record._origin.id)])

    if temp_rec_5:

      for del_temp_rec_5 in temp_rec_5:

        del_temp_rec_5.unlink()

        

    # Business Logic --------------------------------------------------------------------------------------------------------------------------------------------   

    # create new record 

    

    # Production Variance

    for line in report_type_lines:

      create_sub_model = env['x_rm_production_varian'].create({'x_studio_sales_report_model_id':record.id,'x_studio_description':line.raw_material_production_id.product_id.id,'x_studio_production_id':line.raw_material_production_id.id,'x_studio_prod_qty':line.raw_material_production_id.product_qty,'x_studio_description_1':line.product_id.id,'x_studio_bom_qty':line.x_studio_original_qty,'x_studio_esti_qty':line.x_studio_original_qty,'x_studio_cons_qty':line.product_uom_qty,'x_studio_variance':line.x_studio_variance,'x_studio_avg_cost':line.price_unit,'x_studio_total_cost':(line.product_uom_qty*line.price_unit),'x_studio_header_reference': record.x_name})
```
  </details>
- **SRM - RPT - Production Overview - WIP** (`sa_f5_x_sales_report_model_srm_rpt_production_overview_wip`, type `code`)
  - Function: For report code 'Production Overview - WIP': deletes old rows and lists every in-progress manufacturing order of the report type with product, destination, quantities and start/end dates.
  - Depends on: `model x_rm_production_orders`, `model x_sales_report_model` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_name` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_code` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (43 lines)</summary>

```python
if record.x_studio_report_type:

  if record.x_studio_report_code == 'Production Overview - WIP':

    report_type_lines = record.x_studio_report_type.x_studio_production_order_id

 

    # filter area ------------------------------------------------------------------------------------------------------------------------------------------------

    report_type_lines = report_type_lines.filtered(lambda x: x.state == 'progress')

    

    # delete record area ----------------------------------------------------------------------------------------------------------------------------------------------  

    # delete old record

    

    # MO - WIP     

    temp_rec_3 = env['x_rm_production_orders'].search([('x_studio_sales_report_model_id', '=', record._origin.id)])

    if temp_rec_3:

      for del_temp_rec_3 in temp_rec_3:

        del_temp_rec_3.unlink()

    

    # Business Logic --------------------------------------------------------------------------------------------------------------------------------------------   

    # create new record 

    

    # Production Overview - WIP

    for line in report_type_lines:

      create_sub_model = env['x_rm_production_orders'].create({'x_studio_sales_report_model_id':record.id,'x_studio_production_id':line.id,'x_studio_product_code':line.product_id.id,'x_studio_description':line.product_id.name,'x_studio_warehouse':line.location_dest_id.id,'x_studio_status':line.state,'x_studio_estimated':line.product_qty,'x_studio_started':line.qty_producing,'x_studio_start':line.date_start,'x_studio_header_reference': record.x_name,'x_studio_end':line.date_finished})
```
  </details>
- **SRM - RPT - Production Summary - Split** (`sa_f5_x_sales_report_model_srm_rpt_production_summary_split`, type `code`)
  - Function: For report code 'Production Summary - Split': deletes old rows and creates split summary lines for raw-material moves up to As On Date with BoM, estimated and consumed quantity, variance and cost.
  - Depends on: `model x_rm_prod_summary_spli`, `model x_sales_report_model` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_name` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_code` (Jinasena_Masterdata_Reporting)<details><summary>+1 more</summary>`x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting)</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (43 lines)</summary>

```python
if record.x_studio_report_type:

  if record.x_studio_report_code == 'Production Summary - Split':

    report_type_lines = record.x_studio_report_type.x_studio_prod_summary_split_id

  

    # filter area ------------------------------------------------------------------------------------------------------------------------------------------------

    report_type_lines = report_type_lines.filtered(lambda x: (x.date.date() <= record.x_studio_as_on_date))

    

    # delete record area ----------------------------------------------------------------------------------------------------------------------------------------------  

    # delete old record

    

    # Production Summary - Split     

    temp_rec_7 = env['x_rm_prod_summary_spli'].search([('x_studio_sales_report_model_id', '=', record._origin.id)])

    if temp_rec_7:

      for del_temp_rec_7 in temp_rec_7:

        del_temp_rec_7.unlink()

        

    # Business Logic --------------------------------------------------------------------------------------------------------------------------------------------   

    # create new record 

    

    # Production Summary - Split 

    for line in report_type_lines:

      create_sub_model = env['x_rm_prod_summary_spli'].create({'x_studio_sales_report_model_id':record.id,'x_studio_description':line.raw_material_production_id.product_id.id,'x_studio_production_id':line.raw_material_production_id.id,'x_studio_prod_qty':line.raw_material_production_id.product_qty,'x_studio_description_1':line.product_id.id,'x_studio_bom_qty':line.x_studio_original_qty,'x_studio_esti_qty':line.x_studio_original_qty,'x_studio_cons_qty':line.product_uom_qty,'x_studio_variance':line.x_studio_variance,'x_studio_avg_cost':line.price_unit,'x_studio_total_cost':(line.product_uom_qty*line.price_unit),'x_studio_header_reference': record.x_name})
```
  </details>
- **SRM - RPT - Project Gross Margin** (`sa_f5_x_sales_report_model_srm_rpt_project_gross_margin`, type `code`)
  - Function: For report code 'Project Gross Margin': deletes and rebuilds estimated, actual, invoiced and comparison gross-margin rows per project category from budget lines, sales orders, journal items and payments.
  - Depends on: `model account.move.line` (account), `model account.payment` (account), `model crossovered.budget.lines` (account_budget), `model sale.order.line` (sale), `model sale.order` (sale)<details><summary>+13 more</summary>`model x_project_category` (BugFix-Project), `model x_rm_gross_margin_actu`, `model x_rm_gross_margin_comp`, `model x_rm_gross_margin_esti`, `model x_rm_gross_margin_invo`, `model x_sales_report_model` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_name` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_customer` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_from_date` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_project_no` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_code` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting)</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (967 lines)</summary>

```python
if record.x_studio_report_type:

  if record.x_studio_report_code == 'Project Gross Margin':

    tot_estimated_val = 0

    tot_actual_val = 0

    tot_balance_val = 0

    tot_estimated_val_1 = 0

    tot_actual_val_1 = 0

    tot_balance_val_1 = 0

    tot_estimated_val_2 = 0

    tot_actual_val_2 = 0

    tot_balance_val_2 = 0

    tot_estimated_val_3 = 0

    tot_actual_val_3 = 0

    tot_balance_val_3 = 0

    tot_estimated_val_4 = 0

    tot_actual_val_4 = 0

    tot_balance_val_4 = 0

    tot_estimated_val_5 = 0

    tot_actual_val_5 = 0

    tot_balance_val_5 = 0

    tot_estimated_val_6 = 0

    tot_actual_val_6 = 0

    tot_balance_val_6 = 0

    tot_estimated_val_7 = 0

    tot_actual_val_7 = 0

    tot_balance_val_7 = 0

    cat_count = 0

    cat_count_2 = 0

    cat_count_3 = 0

    cat_count_4 = 0

    cat_count_5 = 0

    cat_count_6 = 0

    cat_count_7 = 0

    cat_grand_count = 0

    invoice_count = 0

    invoice_total = 0

    on_account_val = 0

    estimated_gp = 0

    actual_gp = 0

    outstanding_cash = 0

    settlement_cash = 0

    outstanding_cash_tot = 0

    temp_actual_lines_2=[]

    temp_actual_lines_3=[]

    temp_actual_lines_4=[]

    temp_actual_lines_5=[]

    temp_actual_lines_6=[]

    temp_actual_budget=[]

    #report_type_lines = record.x_studio_report_type.x_studio_production_variance_id

  

    # filter area ------------------------------------------------------------------------------------------------------------------------------------------------

    #report_type_lines = report_type_lines.filtered(lambda x: (x.date.date() >= record.x_studio_from_date and x.date.date() <= record.x_studio_as_on_date and x.x_studio_variance != 0))

    

    # delete record area ----------------------------------------------------------------------------------------------------------------------------------------------  

    # delete old record

    

    # Project Gross Margin - Estimated    

    temp_rec_1 = env['x_rm_gross_margin_esti'].search([('x_studio_sales_report_model_id', '=', record._origin.id)])

    if temp_rec_1:

      for del_temp_rec_1 in temp_rec_1:

# … 847 more lines
```
  </details>
- **SRM - RPT - Project Gross Margin - Notify Users** (`sa_f5_x_sales_report_model_srm_rpt_project_gross_margin_notify_users`, type `next_activity`)
  - Function: Schedule-activity type action with no activity type, user or summary configured (only the default code template); effectively does nothing useful as ported.
  - Depends on: `model x_sales_report_model` (Jinasena_Masterdata_Reporting)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **SRM - RPT - Sales - Production - Purchase Report** (`sa_f5_x_sales_report_model_srm_rpt_sales_production_purchase_report`, type `code`)
  - Function: For report code 'Sales - Production - Purchase Report': deletes old rows and builds per-product rows of SO, production and purchase quantities up to As On Date. Uses `datetime.strptime` on a date, which likely errors at runtime.
  - Depends on: `model mrp.production` (mrp), `model product.product` (product), `model purchase.order.line` (purchase), `model sale.order.line` (sale), `model stock.valuation.layer` (stock_account)<details><summary>+6 more</summary>`model x_rm_sales_prod_purch`, `model x_sales_report_model` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_name` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_code` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting)</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (101 lines)</summary>

```python
if record.x_studio_report_type:

  if record.x_studio_report_code == 'Sales - Production - Purchase Report':

    report_type_lines = record.x_studio_report_type.x_studio_sales_prod_purch_id

  

    # filter area ------------------------------------------------------------------------------------------------------------------------------------------------

    report_type_lines = report_type_lines.filtered(lambda x: (x.date.date() <= record.x_studio_as_on_date))

    

    # delete record area ----------------------------------------------------------------------------------------------------------------------------------------------  

    # delete old record

    

    # Sales - Production - Purchase Report     

    temp_rec_6 = env['x_rm_sales_prod_purch'].search([('x_studio_sales_report_model_id', '=', record._origin.id)])

    if temp_rec_6:

      for del_temp_rec_6 in temp_rec_6:

        del_temp_rec_6.unlink()

    

    # Business Logic --------------------------------------------------------------------------------------------------------------------------------------------   

    # create new record 

    

    # Sales - Production - Purchase Report   

    d = record.x_studio_as_on_date

    #d1 = datetime.strftime(d, "%Y-%m-%d %H:%M:%S")

    #d2 = datetime.strftime(d, "%Y-%m-%d 23:59:59")

    d1 = datetime.strptime(d, "%Y-%m-%d %H:%M:%S")

    d2 = datetime.strptime(d, "%Y-%m-%d 23:59:59")

    product = env['product.product'].search([('type', '!=', 'service')])

    if product:

     for products in product:

       project_qty = 0

       so_qty = 0

       prod_qty = 0

       purch_qty = 0

         

       last_prod_purch = env['stock.valuation.layer'].search([('product_id', '=', products.id),('quantity', '>', 0),('create_date', '>=', d1),('create_date', '<=', d2)],order='create_date desc',limit=1)

         

       sales_qtys = env['sale.order.line'].search([('product_id', '=', products.id)])

       sales_qtys = sales_qtys.filtered(lambda x: x.create_date.date() <= record.x_studio_as_on_date)

       for qtys in sales_qtys:

         so_qty += qtys.product_uom_qty 

           

       prod_qtys = env['mrp.production'].search([('product_id', '=', products.id)])

       prod_qtys = prod_qtys.filtered(lambda x: x.date_planned_start.date() <= record.x_studio_as_on_date)

       for prodqtys in prod_qtys: 

         prod_qty += prodqtys.product_qty

           

       purch_qtys = env['purchase.order.line'].search([('product_id', '=', products.id)])

       purch_qtys = purch_qtys.filtered(lambda x: x.create_date.date() <= record.x_studio_as_on_date)

       for purchqtys in purch_qtys:

         purch_qty += purchqtys.product_qty

           

       create_sub_model = env['x_rm_sales_prod_purch'].create({'x_studio_sales_report_model_id':record.id,'x_studio_description':products.id,'x_studio_base_price':products.list_price,'x_studio_product_type':products.type,'x_studio_date_1':last_prod_purch.create_date.date(),'x_studio_unit_cost':last_prod_purch.unit_cost,'x_studio_project_category':project_qty,'x_studio_sales_order':so_qty,'x_studio_production_qty':prod_qty,'x_studio_purchase_qty':purch_qty,'x_studio_header_reference': record.x_name})
```
  </details>
- **SRM - RPT - Sales Details for Incentive Calc.** (`sa_f5_x_sales_report_model_srm_rpt_sales_details_for_incentive_calc`, type `code`)
  - Function: For report code 'Sales Details for Incentive Calc.': filters income journal items with products on As On Date, deletes old rows and creates sales detail lines (customer, group, SO, invoice, product, qty, price, net value).
  - Depends on: `model x_rm_sales_order_line`, `model x_sales_report_model` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_code` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (55 lines)</summary>

```python
if record.x_studio_report_type:

  if record.x_studio_report_code == 'Sales Details for Incentive Calc.':

    report_type_lines = record.x_studio_report_type.x_studio_journal_items_id

    

    # filter area ------------------------------------------------------------------------------------------------------------------------------------------------

    # filter by as on date

    if record.x_studio_as_on_date:

      report_type_lines = report_type_lines.filtered(lambda x: x.date == record.x_studio_as_on_date)

    # filter by product

      report_type_lines = report_type_lines.filtered(lambda x: x.product_id.id > 0)

    # filter by internal group

      report_type_lines = report_type_lines.filtered(lambda x: x.account_internal_group == 'income')

      

    # delete record area ----------------------------------------------------------------------------------------------------------------------------------------------  

    # delete old record

    

    # Sales Details for Incentive Calculation     

    temp_rec_2 = env['x_rm_sales_order_line'].search([('x_studio_sales_report_model_id', '=', record._origin.id)])

    if temp_rec_2:

      for del_temp_rec_2 in temp_rec_2:

        del_temp_rec_2.unlink()

    

    # Business Logic --------------------------------------------------------------------------------------------------------------------------------------------   

    # create new record 

    

    # Sales Details for Incentive Calculation    

    for line in report_type_lines:

      create_sub_model = env['x_rm_sales_order_line'].create({'x_studio_sales_report_model_id':record.id,'x_studio_date':line.date,'x_studio_customer_acc':line.partner_id.id,'x_studio_customer_group':line.partner_id.x_studio_customer_group.id,'x_studio_name':line.partner_id.name,'x_studio_sales_order':line.move_id.x_studio_sale_id.id,'x_studio_invoice':line.move_id.id,'x_studio_product_1':line.product_id.id,'x_studio_product_category':line.product_id.categ_id.id,'x_studio_quantity':line.quantity,'x_studio_unit_price':line.price_unit,'x_studio_net_value':line.price_total})
```
  </details>
- **SRM - RPT - Slow Moving Items** (`sa_f5_x_sales_report_model_srm_rpt_slow_moving_items`, type `code`)
  - Function: For report code 'Slow Moving Items': for each stockable product, totals received and issued quantities for each of the last four months up to As On Date and creates non-moving item rows.
  - Depends on: `model product.product` (product), `model x_rm_none_moving`, `model x_sales_report_model` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_name` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting)<details><summary>+2 more</summary>`x_sales_report_model.x_studio_report_code` (Jinasena_Masterdata_Reporting), `x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting)</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (223 lines)</summary>

```python
if record.x_studio_report_type:

  if record.x_studio_report_code == 'Slow Moving Items':

    report_type_lines = record.x_studio_report_type.x_studio_slow_moving_item_id

    

    currentdate = record.x_studio_as_on_date

    

    firstdayOfmonth = datetime.date(currentdate.year, currentdate.month, 1)

    next_month = currentdate.replace(day=28) + datetime.timedelta(days=4)

    lastdayOfmonth = next_month - datetime.timedelta(days=next_month.day)

    

    if firstdayOfmonth.month != 1:

      firstdayOfmonth2 = datetime.date(firstdayOfmonth.year, firstdayOfmonth.month-1, 1)

    else:

      firstdayOfmonth2 = datetime.date(firstdayOfmonth.year-1, 12, 1)

      

    next_month2 = firstdayOfmonth2.replace(day=28) + datetime.timedelta(days=4)

    lastdayOfmonth2 = next_month2 - datetime.timedelta(days=next_month2.day)

    

    if firstdayOfmonth.month > 2:

      firstdayOfmonth3 = datetime.date(firstdayOfmonth.year, firstdayOfmonth.month-2, 1)

    else:

      if firstdayOfmonth.month == 2:

        firstdayOfmonth3 = datetime.date(firstdayOfmonth.year-1, 12, 1)

      else:

        firstdayOfmonth3 = datetime.date(firstdayOfmonth.year-1, 11, 1)

        

    next_month3 = firstdayOfmonth3.replace(day=28) + datetime.timedelta(days=4)

    lastdayOfmonth3 = next_month3 - datetime.timedelta(days=next_month3.day)

    

    if firstdayOfmonth.month > 3:

      firstdayOfmonth4 = datetime.date(firstdayOfmonth.year, firstdayOfmonth.month-3, 1)

    else:

      if firstdayOfmonth.month == 3:

        firstdayOfmonth4 = datetime.date(firstdayOfmonth.year-1, 12, 1)

      elif firstdayOfmonth.month == 2:

        firstdayOfmonth4 = datetime.date(firstdayOfmonth.year-1, 11, 1)

      else:

        firstdayOfmonth4 = datetime.date(firstdayOfmonth.year-1, 10, 1)

        

    next_month4 = firstdayOfmonth4.replace(day=28) + datetime.timedelta(days=4)

    lastdayOfmonth4 = next_month4 - datetime.timedelta(days=next_month4.day)

    

    # filter area ------------------------------------------------------------------------------------------------------------------------------------------------

    report_type_lines_receipt = report_type_lines.filtered(lambda x: (x.date.date() >= firstdayOfmonth and x.date.date() <= lastdayOfmonth and x.picking_code == 'incoming'))

    report_type_lines_delivery = report_type_lines.filtered(lambda x: (x.date.date() >= firstdayOfmonth and x.date.date() <= lastdayOfmonth and x.picking_code == 'outgoing'))

      

    report_type_lines_receipt2 = report_type_lines.filtered(lambda x: (x.date.date() >= firstdayOfmonth2 and x.date.date() <= lastdayOfmonth2 and x.picking_code == 'incoming'))

    report_type_lines_delivery2 = report_type_lines.filtered(lambda x: (x.date.date() >= firstdayOfmonth2 and x.date.date() <= lastdayOfmonth2 and x.picking_code == 'outgoing'))

    

    report_type_lines_receipt3 = report_type_lines.filtered(lambda x: (x.date.date() >= firstdayOfmonth3 and x.date.date() <= lastdayOfmonth3 and x.picking_code == 'incoming'))

    report_type_lines_delivery3 = report_type_lines.filtered(lambda x: (x.date.date() >= firstdayOfmonth3 and x.date.date() <= lastdayOfmonth3 and x.picking_code == 'outgoing'))

      

    report_type_lines_receipt4 = report_type_lines.filtered(lambda x: (x.date.date() >= firstdayOfmonth4 and x.date.date() <= lastdayOfmonth4 and x.picking_code == 'incoming'))

    report_type_lines_delivery4 = report_type_lines.filtered(lambda x: (x.date.date() >= firstdayOfmonth4 and x.date.date() <= lastdayOfmonth4 and x.picking_code == 'outgoing'))

    

    # delete record area ----------------------------------------------------------------------------------------------------------------------------------------------  

    # delete old record

    

    # Slow Moving Items     

    temp_rec_4 = env['x_rm_none_moving'].search([('x_studio_sales_report_model_id', '=', record._origin.id)])

# … 103 more lines
```
  </details>
**Automations (17):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| JIN-Report Model Seq.No | `base_automation_126_jin_report_model_seq_no` |  | When a record is created or updated on Sales Report Model, runs _Execute Code_. | `model x_sales_report_model` (Jinasena_Masterdata_Reporting)<br>`server action BugFix-Accounting.server_action_1747_report_model_seq_no`<br>`x_sales_report_model.create_date` (Jinasena_Masterdata_Reporting) |  |
| Report Model Created Date | `base_automation_188_report_model_created_date` |  | When a record is created or updated on Sales Report Model, runs _Execute Code_. | `model x_sales_report_model` (Jinasena_Masterdata_Reporting)<br>`server action BugFix-Accounting.server_action_2126_report_model_created_date`<br>`x_sales_report_model.create_date` (Jinasena_Masterdata_Reporting) |  |
| Restrict Delete in Sales Report Model | `base_automation_99_restrict_delete_in_sales_report_model` |  | When a record is deleted on Sales Report Model, runs _Execute Code_. | `model x_sales_report_model` (Jinasena_Masterdata_Reporting)<br>`server action BugFix-Accounting.server_action_1675_restrict_delete_in_sales_report_model` |  |
| SRM - Auto Delete Sub Models | `base_automation_125_srm_auto_delete_sub_models` |  | When a record is deleted on Sales Report Model and `[]`, runs _Execute Code_. | `model x_sales_report_model` (Jinasena_Masterdata_Reporting)<br>`server action BugFix-Accounting.server_action_1746_srm_auto_delete_sub_models`<br>`x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting) |  |
| SRM - Auto Populate Data | `base_automation_116_srm_auto_populate_data` |  | When a record is created or updated on Sales Report Model and `[]`, runs _SRM - Auto Populate Data_. | `model x_sales_report_model` (Jinasena_Masterdata_Reporting)<br>`server action BugFix-Accounting.server_action_1726_srm_auto_populate_data`<br>`x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_from_date` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting)<details><summary>+1 more</summary>`x_sales_report_model.x_studio_sales_centre` (Jinasena_Masterdata_Reporting)</details> |  |
| SRM - Auto Populate Data - TAU | `base_automation_117_srm_auto_populate_data_tau` | archived | When a record is created or updated on Sales Report Model and `[]`, runs nothing (no action linked). **Archived — does not run.** | `model x_sales_report_model` (Jinasena_Masterdata_Reporting) |  |
| SRM - Auto Populate Data-Original | `base_automation_119_srm_auto_populate_data_original` | archived | When a record is created or updated on Sales Report Model and `[]`, runs nothing (no action linked). **Archived — does not run.** | `model x_sales_report_model` (Jinasena_Masterdata_Reporting) |  |
| SRM - RPT - Costing Work Sheet | `base_automation_248_srm_rpt_costing_work_sheet` |  | When a record is created or updated on Sales Report Model and `[["x_studio_report_code","=","Costing Work Sheet"]]`, runs _Execute Code_. | `model x_sales_report_model` (Jinasena_Masterdata_Reporting)<br>`server action BugFix-Accounting.server_action_2490_srm_rpt_costing_work_sheet`<br>`x_sales_report_model.x_studio_as_on_date_1` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_contingency_` (Jinasena_Masterdata_Reporting)<details><summary>+8 more</summary>`x_sales_report_model.x_studio_distributor_addition` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_factory_oh_labour` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_factory_oh` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_idling_rate` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_other_oh` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_report_code` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_sales_oh` (Jinasena_Masterdata_Reporting)</details> |  |
| SRM - RPT - Daily Sales Summary | `base_automation_131_srm_rpt_daily_sales_summary` |  | When a record is created or updated on Sales Report Model and `[]`, runs _Execute Code_. | `model x_sales_report_model` (Jinasena_Masterdata_Reporting)<br>`server action BugFix-Accounting.server_action_1759_srm_rpt_daily_sales_summary`<br>`x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_sales_centre` (Jinasena_Masterdata_Reporting) |  |
| SRM - RPT - Production Job Variance | `base_automation_137_srm_rpt_production_job_variance` |  | When a record is created or updated on Sales Report Model and `[]`, runs _Execute Code_. | `model x_sales_report_model` (Jinasena_Masterdata_Reporting)<br>`server action BugFix-Accounting.server_action_1765_srm_rpt_production_job_variance`<br>`x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_from_date` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting) |  |
| SRM - RPT - Production Overview - WIP | `base_automation_133_srm_rpt_production_overview_wip` |  | When a record is created or updated on Sales Report Model and `[]`, runs _Execute Code_. | `model x_sales_report_model` (Jinasena_Masterdata_Reporting)<br>`server action BugFix-Accounting.server_action_1761_srm_rpt_production_overview_wip`<br>`x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting) |  |
| SRM - RPT - Production Summary - Split | `base_automation_136_srm_rpt_production_summary_split` |  | When a record is created or updated on Sales Report Model and `[]`, runs _Execute Code_. | `model x_sales_report_model` (Jinasena_Masterdata_Reporting)<br>`server action BugFix-Accounting.server_action_1764_srm_rpt_production_summary_split`<br>`x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting) |  |
| SRM - RPT - Project Gross Margin | `base_automation_182_srm_rpt_project_gross_margin` |  | When a record is created or updated on Sales Report Model and `[["x_studio_report_code","=","Project Gross Margin"]]`, runs _Execute Code_. | `model x_sales_report_model` (Jinasena_Masterdata_Reporting)<br>`server action BugFix-Accounting.server_action_2102_srm_rpt_project_gross_margin`<br>`x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_report_code` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting) |  |
| SRM - RPT - Project Gross Margin - Notify Users | `base_automation_189_srm_rpt_project_gross_margin_notify_users` |  | When a record is created or updated on Sales Report Model, runs _Create activity: Gross Margin Report Generated_. | `model x_sales_report_model` (Jinasena_Masterdata_Reporting)<br>`server action BugFix-Accounting.server_action_2129_srm_rpt_project_gross_margin_notify_users`<br>`x_sales_report_model.create_date` (Jinasena_Masterdata_Reporting) |  |
| SRM - RPT - Sales - Production - Purchase Report | `base_automation_135_srm_rpt_sales_production_purchase_report` |  | When a record is created or updated on Sales Report Model and `[]`, runs _Execute Code_. | `model x_sales_report_model` (Jinasena_Masterdata_Reporting)<br>`server action BugFix-Accounting.server_action_1763_srm_rpt_sales_production_purchase_report`<br>`x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting) |  |
| SRM - RPT - Sales Details for Incentive Calc. | `base_automation_132_srm_rpt_sales_details_for_incentive_calc` |  | When a record is created or updated on Sales Report Model and `[]`, runs _Execute Code_. | `model x_sales_report_model` (Jinasena_Masterdata_Reporting)<br>`server action BugFix-Accounting.server_action_1760_srm_rpt_sales_details_for_incentive_calc`<br>`x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting) |  |
| SRM - RPT - Slow Moving Items | `base_automation_134_srm_rpt_slow_moving_items` |  | When a record is created or updated on Sales Report Model and `[]`, runs _Execute Code_. | `model x_sales_report_model` (Jinasena_Masterdata_Reporting)<br>`server action BugFix-Accounting.server_action_1762_srm_rpt_slow_moving_items`<br>`x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting) |  |

**Window actions (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Gross Margin Reports | `action_2115_gross_margin_reports` | Opens **Sales Report Model** records (tree,form), filtered to `[('x_studio_project_no', '=', active_id)]`. | `model x_sales_report_model` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_project_no` (Jinasena_Masterdata_Reporting) |  |
| Sales Report Model | `action_1667_sales_report_model` | Opens **Sales Report Model** records (tree,form). | `model x_sales_report_model` (Jinasena_Masterdata_Reporting) | `menu BugFix-Accounting.menu_880_report_models`<br>`menu BugFix-Accounting.menu_881_sales_report_model`<br>`menu BugFix-Accounting.menu_f6_report_models`<br>`menu BugFix-Accounting.menu_f6_sales_report_model_1`<br>`menu BugFix-Accounting.menu_f6_sales_report_model` |

**Views (5):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_sales_report_model | `ported_view_3784_default_form_view_fo_d583be6a_921f_4205_94a7_603a2375ce6e` | form | full form layout with 5 fields | Base form for Sales Report Model (report run header): a permanently hidden 'Clear Data' header button, archived ribbon, Reference title, two groups and chatter; extended by its Studio customization. | `server action BugFix-Accounting.srv_sales_report_sample_button`<br>`x_sales_report_model.activity_ids` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.message_follower_ids` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.message_ids` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_active` (Jinasena_Masterdata_Reporting)<details><summary>+1 more</summary>`x_sales_report_model.x_name` (Jinasena_Masterdata_Reporting)</details> | `view BugFix-Accounting.ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` |
| Default list view for x_sales_report_model | `ported_view_3783_default_list_view_fo_8853c5be_dc14_48d4_82c4_f209d820d16a` | tree | full tree layout with 2 fields | Default list for Sales Report Model (`x_sales_report_model`) with sequence handle and Name. | `x_sales_report_model.x_name` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_sequence` (Jinasena_Masterdata_Reporting) | `view BugFix-Accounting.ported_view_3791_odoo_studio_default_25244692_8d9f_4fba_9286_7f16ca6d45f1` |
| Default search view for x_sales_report_model | `ported_view_3785_default_search_view_36b50122_6852_4842_9718_7d6fbf0c90e3` | search | full search layout with 1 fields | Default search view for Sales Report Model records (`x_sales_report_model`): search by name plus an Archived filter. | `x_sales_report_model.x_active` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_name` (Jinasena_Masterdata_Reporting) |  |
| Odoo Studio: Default form view for x_sales_report_model customization | `ported_view_3786_odoo_studio_default_ff0f5f4b_41b6_49a0_9acc_cb410e663b5b` | form | after `//header[1]/button[1]`: add field x_studio_selection_field_Fbw0x; set force_save=True, readonly=1, required= on `//field[@name='x_name']`; set string=Parameters on `//group[@name='studio_group_1eb3ec_left']`; inside `//group[@name='studio_group_1eb3ec_left']`: add field x_studio_report_type, field x_studio_actuals, field x_studio_project_no, field x_studio_from_date, field x_studio_as_on_date, field x_studio_as_on_date_1, field x_studio_as_on_date_2, field x_studio_idling_rate, field x_studio_distributor_addition, field x_studio_sscl, field x_studio_contingency_, field x_studio_factory_oh_labour …; set string=Log on `//group[@name='studio_group_1eb3ec_right']`; inside `//group[@name='studio_group_1eb3ec_right']`: add field create_uid, field create_date, field x_studio_created_from_project_update, field x_studio_created_date, field x_studio_auto_generated, field x_studio_management_purpose, field x_studio_month_end_entry_updated, field x_studio_estimated_gp_, field x_studio_actual_gp_, field x_studio_financial_progress, field x_studio_report_code, field id; after `//group[@name='studio_group_1eb3ec']`: add notebook, notebook | Sales Report Model form: adds a status bar, makes the Reference read-only, fills a Parameters group (report type, project, date range, rates and cost factors) and a Log group (creator, flags, GP and progress figures, report code), and adds result notebooks. | `account.move.line.account_id` (account)<br>`account.move.line.amount_currency` (account)<br>`account.move.line.balance` (account)<br>`account.move.line.company_currency_id` (account)<br>`account.move.line.company_id` (account)<details><summary>+370 more</summary>`account.move.line.credit` (account)<br>`account.move.line.currency_id` (account)<br>`account.move.line.date_maturity` (account)<br>`account.move.line.date` (account)<br>`account.move.line.debit` (account)<br>`account.move.line.matching_number` (account)<br>`account.move.line.move_attachment_ids` (account_accountant)<br>`account.move.line.move_id` (account)<br>`account.move.line.name` (account)<br>`account.move.line.parent_state` (account)<br>`account.move.line.partner_id` (account)<br>`account.move.line.product_id` (account)<br>`account.move.line.quantity` (account)<br>`account.move.line.reconcile_model_id` (account)<br>`account.move.line.reconciled` (account)<br>`account.move.line.ref` (account)<br>`account.move.line.statement_id` (account)<br>`account.move.line.tax_ids` (account)<br>`account.move.line.tax_tag_ids` (account)<br>`account.move.line.x_studio_sales_team`<br>`account.move.line.x_studio_status`<br>`group account.group_account_invoice` (account)<br>`group account.group_account_readonly` (account)<br>`group account.group_account_user` (account)<br>`group account.group_warning_account` (account)<br>`group base.group_multi_company` (base)<br>`group base.group_multi_currency` (base)<br>`ir.attachment.mimetype` (base)<br>`view BugFix-Accounting.ported_view_3784_default_form_view_fo_d583be6a_921f_4205_94a7_603a2375ce6e`<br>`window action account.action_view_account_move_reversal` (account)<br>`x_pump_price_costing.x_name`<br>`x_pump_price_costing.x_studio_actual_1`<br>`x_pump_price_costing.x_studio_actual`<br>`x_pump_price_costing.x_studio_contingency_1`<br>`x_pump_price_costing.x_studio_contingency_rs`<br>`x_pump_price_costing.x_studio_contribution_2`<br>`x_pump_price_costing.x_studio_contribution_rs`<br>`x_pump_price_costing.x_studio_current_base_price`<br>`x_pump_price_costing.x_studio_current_retail_price_vat_18`<br>`x_pump_price_costing.x_studio_date`<br>`x_pump_price_costing.x_studio_difference`<br>`x_pump_price_costing.x_studio_discount`<br>`x_pump_price_costing.x_studio_distributor_addition`<br>`x_pump_price_costing.x_studio_factory_oh`<br>`x_pump_price_costing.x_studio_idling_rate_1`<br>`x_pump_price_costing.x_studio_idling_rate`<br>`x_pump_price_costing.x_studio_labour_1`<br>`x_pump_price_costing.x_studio_material_cost_imports`<br>`x_pump_price_costing.x_studio_material_cost_other`<br>`x_pump_price_costing.x_studio_max_discount_1`<br>`x_pump_price_costing.x_studio_max_discount_2`<br>`x_pump_price_costing.x_studio_max_discount`<br>`x_pump_price_costing.x_studio_net_selling_price_1`<br>`x_pump_price_costing.x_studio_net_selling_price_2`<br>`x_pump_price_costing.x_studio_net_selling_price`<br>`x_pump_price_costing.x_studio_oh_absorbed_factory_1`<br>`x_pump_price_costing.x_studio_oh_absorbed_factory`<br>`x_pump_price_costing.x_studio_oh_absorbed_other_1`<br>`x_pump_price_costing.x_studio_oh_absorbed_other`<br>`x_pump_price_costing.x_studio_oh_absorbed_sales_1`<br>`x_pump_price_costing.x_studio_oh_absorbed_sales`<br>`x_pump_price_costing.x_studio_other_oh_rs`<br>`x_pump_price_costing.x_studio_other_oh`<br>`x_pump_price_costing.x_studio_product_id_1`<br>`x_pump_price_costing.x_studio_product_id`<br>`x_pump_price_costing.x_studio_profit_mark_up_3`<br>`x_pump_price_costing.x_studio_profit_mark_up_`<br>`x_pump_price_costing.x_studio_profit_mark_up_rs_1`<br>`x_pump_price_costing.x_studio_profit_mark_up_rs`<br>`x_pump_price_costing.x_studio_profitloss_as_of_net_sale`<br>`x_pump_price_costing.x_studio_proposed_base_price_1`<br>`x_pump_price_costing.x_studio_proposed_base_price`<br>`x_pump_price_costing.x_studio_route_time`<br>`x_pump_price_costing.x_studio_rs_1`<br>`x_pump_price_costing.x_studio_rs`<br>`x_pump_price_costing.x_studio_sales_oh_rs`<br>`x_pump_price_costing.x_studio_sales_oh`<br>`x_pump_price_costing.x_studio_sales_report_model_id`<br>`x_pump_price_costing.x_studio_satd_discount`<br>`x_pump_price_costing.x_studio_sequence`<br>`x_pump_price_costing.x_studio_sscl_1`<br>`x_pump_price_costing.x_studio_sscl_2`<br>`x_pump_price_costing.x_studio_sscl`<br>`x_pump_price_costing.x_studio_standard_1`<br>`x_pump_price_costing.x_studio_standard`<br>`x_pump_price_costing.x_studio_system_cost`<br>`x_pump_price_costing.x_studio_total_actual_labour_cost_ot`<br>`x_pump_price_costing.x_studio_total_actual_labour_cost_without_ot`<br>`x_pump_price_costing.x_studio_total_actual_labour_cost`<br>`x_pump_price_costing.x_studio_total_cost`<br>`x_pump_price_costing.x_studio_total_factory_cost_1`<br>`x_pump_price_costing.x_studio_total_factory_cost`<br>`x_pump_price_costing.x_studio_total_material_cost_1`<br>`x_pump_price_costing.x_studio_total_material_cost_2`<br>`x_pump_price_costing.x_studio_total_material_cost`<br>`x_rm_cust_invoice_s1.x_name`<br>`x_rm_cust_invoice_s1.x_studio_invoice_date`<br>`x_rm_cust_invoice_s1.x_studio_number`<br>`x_rm_cust_invoice_s1.x_studio_partner`<br>`x_rm_cust_invoice_s1.x_studio_product_id`<br>`x_rm_cust_invoice_s1.x_studio_quantity`<br>`x_rm_cust_invoice_s1.x_studio_sales_centre`<br>`x_rm_cust_invoice_s1.x_studio_sequence`<br>`x_rm_cust_invoice_s1.x_studio_value`<br>`x_rm_customer_wise_inv.x_name`<br>`x_rm_customer_wise_inv.x_studio_customer`<br>`x_rm_customer_wise_inv.x_studio_sequence`<br>`x_rm_customer_wise_inv.x_studio_total_invoice_amount`<br>`x_rm_daily_s1.x_name`<br>`x_rm_daily_s1.x_studio_invoice_date`<br>`x_rm_daily_s1.x_studio_number`<br>`x_rm_daily_s1.x_studio_partner`<br>`x_rm_daily_s1.x_studio_product_id`<br>`x_rm_daily_s1.x_studio_quantity`<br>`x_rm_daily_s1.x_studio_sales_centre`<br>`x_rm_daily_s1.x_studio_sales_report_model_id`<br>`x_rm_daily_s1.x_studio_sequence`<br>`x_rm_daily_s1.x_studio_value`<br>`x_rm_daily_s2.x_name`<br>`x_rm_daily_s2.x_studio_invoice_date`<br>`x_rm_daily_s2.x_studio_number`<br>`x_rm_daily_s2.x_studio_partner`<br>`x_rm_daily_s2.x_studio_quantity`<br>`x_rm_daily_s2.x_studio_sales_centre`<br>`x_rm_daily_s2.x_studio_sequence`<br>`x_rm_daily_s2.x_studio_value`<br>`x_rm_daily_s3.x_name`<br>`x_rm_daily_s3.x_studio_invoice_date`<br>`x_rm_daily_s3.x_studio_many2one_field_CiZHF`<br>`x_rm_daily_s3.x_studio_number`<br>`x_rm_daily_s3.x_studio_product_id`<br>`x_rm_daily_s3.x_studio_quantity`<br>`x_rm_daily_s3.x_studio_sales_centre`<br>`x_rm_daily_s3.x_studio_sequence`<br>`x_rm_daily_s3.x_studio_value`<br>`x_rm_daily_sales_repor.x_active`<br>`x_rm_daily_sales_repor.x_name`<br>`x_rm_daily_sales_repor.x_studio_achieve_cumulative_`<br>`x_rm_daily_sales_repor.x_studio_achievement_`<br>`x_rm_daily_sales_repor.x_studio_m_sales_target`<br>`x_rm_daily_sales_repor.x_studio_net_invoice_value_cumulative`<br>`x_rm_daily_sales_repor.x_studio_net_invoice_value_day`<br>`x_rm_daily_sales_repor.x_studio_net_invoice_value_month`<br>`x_rm_daily_sales_repor.x_studio_s_target_cumulative`<br>`x_rm_daily_sales_repor.x_studio_sales_centre`<br>`x_rm_daily_sales_repor.x_studio_sales_report_model_id`<br>`x_rm_daily_sales_repor.x_studio_sequence`<br>`x_rm_gross_margin_actu.x_active`<br>`x_rm_gross_margin_actu.x_name`<br>`x_rm_gross_margin_actu.x_studio_budget_line_ids`<br>`x_rm_gross_margin_actu.x_studio_budget_line`<br>`x_rm_gross_margin_actu.x_studio_cost_price`<br>`x_rm_gross_margin_actu.x_studio_estimated_total`<br>`x_rm_gross_margin_actu.x_studio_header_reference`<br>`x_rm_gross_margin_actu.x_studio_normal_line`<br>`x_rm_gross_margin_actu.x_studio_other_expenses`<br>`x_rm_gross_margin_actu.x_studio_sales_order_line_ids`<br>`x_rm_gross_margin_actu.x_studio_sales_report_model_id`<br>`x_rm_gross_margin_actu.x_studio_sequence`<br>`x_rm_gross_margin_actu.x_studio_transaction_type_1`<br>`x_rm_gross_margin_actu.x_studio_variance_est_act`<br>`x_rm_gross_margin_comp.x_name`<br>`x_rm_gross_margin_comp.x_studio_delivered_amount`<br>`x_rm_gross_margin_comp.x_studio_delivered_not_invoiced`<br>`x_rm_gross_margin_comp.x_studio_estimated_amount`<br>`x_rm_gross_margin_comp.x_studio_header_reference`<br>`x_rm_gross_margin_comp.x_studio_invoiced_amount`<br>`x_rm_gross_margin_comp.x_studio_many2one_field_7fcuw`<br>`x_rm_gross_margin_comp.x_studio_sales_order`<br>`x_rm_gross_margin_comp.x_studio_sales_report_model_id`<br>`x_rm_gross_margin_comp.x_studio_sequence`<br>`x_rm_gross_margin_esti.x_active`<br>`x_rm_gross_margin_esti.x_name`<br>`x_rm_gross_margin_esti.x_studio_actual_cost`<br>`x_rm_gross_margin_esti.x_studio_balance_cost`<br>`x_rm_gross_margin_esti.x_studio_category`<br>`x_rm_gross_margin_esti.x_studio_estimated_amt`<br>`x_rm_gross_margin_esti.x_studio_group_title`<br>`x_rm_gross_margin_esti.x_studio_header_reference`<br>`x_rm_gross_margin_esti.x_studio_sales_order_line_ids`<br>`x_rm_gross_margin_esti.x_studio_sales_report_model_id`<br>`x_rm_gross_margin_esti.x_studio_sequence`<br>`x_rm_gross_margin_esti.x_studio_transaction_type`<br>`x_rm_gross_margin_invo.x_name`<br>`x_rm_gross_margin_invo.x_studio_amount`<br>`x_rm_gross_margin_invo.x_studio_group_title`<br>`x_rm_gross_margin_invo.x_studio_header_reference`<br>`x_rm_gross_margin_invo.x_studio_invoice_date`<br>`x_rm_gross_margin_invo.x_studio_invoice_no`<br>`x_rm_gross_margin_invo.x_studio_payment_status`<br>`x_rm_gross_margin_invo.x_studio_sales_report_model_id`<br>`x_rm_gross_margin_invo.x_studio_sequence`<br>`x_rm_gross_margin_invo.x_studio_status`<br>`x_rm_none_moving.x_name`<br>`x_rm_none_moving.x_studio_base_price`<br>`x_rm_none_moving.x_studio_description`<br>`x_rm_none_moving.x_studio_in_hand_1`<br>`x_rm_none_moving.x_studio_in_hand_2`<br>`x_rm_none_moving.x_studio_in_hand_3`<br>`x_rm_none_moving.x_studio_in_hand_4`<br>`x_rm_none_moving.x_studio_issue_1`<br>`x_rm_none_moving.x_studio_issue_2`<br>`x_rm_none_moving.x_studio_issue_3`<br>`x_rm_none_moving.x_studio_issue_4`<br>`x_rm_none_moving.x_studio_product_category`<br>`x_rm_none_moving.x_studio_product_code_1`<br>`x_rm_none_moving.x_studio_qty`<br>`x_rm_none_moving.x_studio_sales_report_model_id`<br>`x_rm_none_moving.x_studio_sequence`<br>`x_rm_none_moving.x_studio_value`<br>`x_rm_prod_summary_spli.x_name`<br>`x_rm_prod_summary_spli.x_studio_description`<br>`x_rm_prod_summary_spli.x_studio_header_reference`<br>`x_rm_prod_summary_spli.x_studio_job_no`<br>`x_rm_prod_summary_spli.x_studio_product_code`<br>`x_rm_prod_summary_spli.x_studio_quantity`<br>`x_rm_prod_summary_spli.x_studio_sales_report_model_id`<br>`x_rm_prod_summary_spli.x_studio_sequence`<br>`x_rm_prod_summary_spli.x_studio_split_1`<br>`x_rm_prod_summary_spli.x_studio_split`<br>`x_rm_prod_summary_spli.x_studio_total`<br>`x_rm_production_orders.x_studio_description`<br>`x_rm_production_orders.x_studio_end`<br>`x_rm_production_orders.x_studio_estimated`<br>`x_rm_production_orders.x_studio_good_qty`<br>`x_rm_production_orders.x_studio_product_code`<br>`x_rm_production_orders.x_studio_production_id`<br>`x_rm_production_orders.x_studio_sales_report_model_id`<br>`x_rm_production_orders.x_studio_sequence`<br>`x_rm_production_orders.x_studio_start`<br>`x_rm_production_orders.x_studio_started`<br>`x_rm_production_orders.x_studio_status`<br>`x_rm_production_orders.x_studio_warehouse`<br>`x_rm_production_varian.x_name`<br>`x_rm_production_varian.x_studio_avg_cost`<br>`x_rm_production_varian.x_studio_bom_item`<br>`x_rm_production_varian.x_studio_bom_qty`<br>`x_rm_production_varian.x_studio_cons_qty`<br>`x_rm_production_varian.x_studio_description_1`<br>`x_rm_production_varian.x_studio_description`<br>`x_rm_production_varian.x_studio_esti_qty`<br>`x_rm_production_varian.x_studio_header_reference`<br>`x_rm_production_varian.x_studio_item_number`<br>`x_rm_production_varian.x_studio_prod_qty`<br>`x_rm_production_varian.x_studio_production_id`<br>`x_rm_production_varian.x_studio_sales_report_model_id`<br>`x_rm_production_varian.x_studio_sequence`<br>`x_rm_production_varian.x_studio_total_cost`<br>`x_rm_production_varian.x_studio_unit`<br>`x_rm_production_varian.x_studio_variance`<br>`x_rm_sales_order_line.x_studio_customer_acc`<br>`x_rm_sales_order_line.x_studio_customer_group`<br>`x_rm_sales_order_line.x_studio_date`<br>`x_rm_sales_order_line.x_studio_disc_`<br>`x_rm_sales_order_line.x_studio_disc_amount`<br>`x_rm_sales_order_line.x_studio_inv_address`<br>`x_rm_sales_order_line.x_studio_invoice`<br>`x_rm_sales_order_line.x_studio_name`<br>`x_rm_sales_order_line.x_studio_net_value`<br>`x_rm_sales_order_line.x_studio_product_1`<br>`x_rm_sales_order_line.x_studio_product_category`<br>`x_rm_sales_order_line.x_studio_quantity`<br>`x_rm_sales_order_line.x_studio_sales_order`<br>`x_rm_sales_order_line.x_studio_sequence`<br>`x_rm_sales_order_line.x_studio_total_base_price`<br>`x_rm_sales_order_line.x_studio_unit_price`<br>`x_rm_sales_prod_purch.x_name`<br>`x_rm_sales_prod_purch.x_studio_base_price`<br>`x_rm_sales_prod_purch.x_studio_date_1`<br>`x_rm_sales_prod_purch.x_studio_date`<br>`x_rm_sales_prod_purch.x_studio_description`<br>`x_rm_sales_prod_purch.x_studio_header_reference`<br>`x_rm_sales_prod_purch.x_studio_product_category`<br>`x_rm_sales_prod_purch.x_studio_product_code`<br>`x_rm_sales_prod_purch.x_studio_product_type`<br>`x_rm_sales_prod_purch.x_studio_production_qty`<br>`x_rm_sales_prod_purch.x_studio_project_category`<br>`x_rm_sales_prod_purch.x_studio_purchase_qty`<br>`x_rm_sales_prod_purch.x_studio_sales_order`<br>`x_rm_sales_prod_purch.x_studio_sales_report_model_id`<br>`x_rm_sales_prod_purch.x_studio_sequence`<br>`x_rm_sales_prod_purch.x_studio_unit_cost`<br>`x_sales_report_model.action_duplicate()` (Odoo)<br>`x_sales_report_model.action_post()` (Odoo)<br>`x_sales_report_model.action_reconcile()` (Odoo)<br>`x_sales_report_model.turn_as_asset()` (Odoo)<br>`x_sales_report_model.x_active` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_actual_gp_` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_actual_line_ids`<br>`x_sales_report_model.x_studio_actuals` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_as_on_date_1` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_as_on_date_2` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_auto_generated` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_comparison_line_ids`<br>`x_sales_report_model.x_studio_contingency_` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_created_date` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_created_from_project_update` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_customer` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_daily_sales_report_id_1`<br>`x_sales_report_model.x_studio_daily_sales_report_id_2`<br>`x_sales_report_model.x_studio_daily_sales_report_id_3`<br>`x_sales_report_model.x_studio_daily_sales_report_id`<br>`x_sales_report_model.x_studio_date_updated` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_distributor_addition` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_estimated_gp_` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_estimated_line_ids`<br>`x_sales_report_model.x_studio_factory_oh_labour` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_factory_oh` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_financial_progress` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_from_date` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_idling_rate` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_invoice_details_line_ids`<br>`x_sales_report_model.x_studio_journal_item_ids` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_management_purpose` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_month_end_entry_updated` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_none_moving_item_ids`<br>`x_sales_report_model.x_studio_oh_absorbed_2_factory` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_oh_absorbed_2_other` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_oh_absorbed_2_sales` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_oh_absorbed_factory` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_oh_absorbed_other` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_oh_absorbed_sales` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_one2many_field_1Aq0X`<br>`x_sales_report_model.x_studio_one2many_field_1rlRW`<br>`x_sales_report_model.x_studio_one2many_field_6rdac`<br>`x_sales_report_model.x_studio_one2many_field_jTZq4`<br>`x_sales_report_model.x_studio_one2many_field_yeTsx`<br>`x_sales_report_model.x_studio_other_oh` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_profit_mark_up_` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_project_no` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_pump_price_costing_ids`<br>`x_sales_report_model.x_studio_related_field_DqBBB` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_related_field_nfrkz` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_report_code` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_sales_centre` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_sales_oh` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_sales_report_model_id_4`<br>`x_sales_report_model.x_studio_sales_report_model_id_5`<br>`x_sales_report_model.x_studio_selection_field_Fbw0x` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_sscl` (Jinasena_Masterdata_Reporting)<br>`x_temp_actual_budget.x_currency_id`<br>`x_temp_actual_budget.x_name`<br>`x_temp_actual_budget.x_studio_actual_line_ids`<br>`x_temp_actual_budget.x_studio_analytic_account_id`<br>`x_temp_actual_budget.x_studio_budget_line_ids`<br>`x_temp_actual_budget.x_studio_crossovered_budget_id`<br>`x_temp_actual_budget.x_studio_date_from`<br>`x_temp_actual_budget.x_studio_date_to`<br>`x_temp_actual_budget.x_studio_planned_amount`<br>`x_temp_actual_budget.x_studio_sequence`<br>`x_temp_estimated.x_currency_id`<br>`x_temp_estimated.x_name`<br>`x_temp_estimated.x_studio_actual_line_ids`<br>`x_temp_estimated.x_studio_category`<br>`x_temp_estimated.x_studio_customer`<br>`x_temp_estimated.x_studio_delivered_qty`<br>`x_temp_estimated.x_studio_description`<br>`x_temp_estimated.x_studio_estimated_line_ids`<br>`x_temp_estimated.x_studio_product_id`<br>`x_temp_estimated.x_studio_project_no`<br>`x_temp_estimated.x_studio_quantity`<br>`x_temp_estimated.x_studio_sales_order_line_id`<br>`x_temp_estimated.x_studio_sales_order`<br>`x_temp_estimated.x_studio_sequence`<br>`x_temp_estimated.x_studio_sub_total`<br>`x_temp_estimated.x_studio_trans_type`<br>`x_temp_estimated.x_studio_unit_price`<br>`x_temp_estimated.x_studio_uom`</details> |  |
| Odoo Studio: Default list view for x_sales_report_model customization | `ported_view_3791_odoo_studio_default_25244692_8d9f_4fba_9286_7f16ca6d45f1` | tree | set default_order=x_name desc on `//tree[1]`; set column_invisible=1 on `//field[@name='x_studio_sequence']`; after `//field[@name='x_studio_sequence']`: add field display_name, field x_studio_report_type, field x_studio_as_on_date, field create_uid, field create_date, field x_studio_selection_field_Fbw0x, field x_studio_project_no, field x_studio_actual_gp_, field x_studio_estimated_gp_, field x_studio_financial_progress, field x_studio_report_code, field x_studio_auto_generated …; set column_invisible=1 on `//field[@name='x_name']` | Sales Report Model list, newest first: Reference, Report Type, As On Date, Created By/On, Status, Project No, actual and estimated GP, financial progress, report code, auto-generated flag and more; sequence and name hidden. | `view BugFix-Accounting.ported_view_3783_default_list_view_fo_8853c5be_dc14_48d4_82c4_f209d820d16a`<br>`x_sales_report_model.x_studio_actual_gp_` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_as_on_date` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_auto_generated` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_estimated_gp_` (Jinasena_Masterdata_Reporting)<details><summary>+6 more</summary>`x_sales_report_model.x_studio_financial_progress` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_month_end_entry_updated` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_project_no` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_report_code` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_selection_field_Fbw0x` (Jinasena_Masterdata_Reporting)</details> |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Sales Report Model group_system | `access_1498_sales_report_model_group_system` | Gives **Administration / Settings** read/write/create/delete access to Sales Report Model records. | `group base.group_system` (base)<br>`model x_sales_report_model` (Jinasena_Masterdata_Reporting) |  |
| Sales Report Model group_user | `access_1499_sales_report_model_group_user` | Gives **User types / Internal User** no access to Sales Report Model records. | `group base.group_user` (base)<br>`model x_sales_report_model` (Jinasena_Masterdata_Reporting) |  |
| x_sales_report_model user access | `access_x_sales_report_model_user` | Gives **User types / Internal User** read/write/create/delete access to Sales Report Model records. | `group base.group_user` (base)<br>`model x_sales_report_model` (Jinasena_Masterdata_Reporting) |  |
