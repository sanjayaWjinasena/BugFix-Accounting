# -*- coding: utf-8 -*-
{
    'name': 'Jinasena : Module : Accounting',
    'version': '17.0.0.0.50',
    'summary': 'Studio-to-Python port for BugFix-Accounting',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Accounting',
    'license': 'LGPL-3',
    # Do NOT depend on studio_customization -- Odoo SH does not ship
    # a manifest for it, listing it causes install skip.
    #
    # v0.0.50: break the 2-way cycle Purchase <-> Accounting that was
    # silently blocking cross-module upgrades. Removed BugFix-Purchase
    # from depends. Fix: account_move.x_studio_cre (the only STORED
    # Many2one to x_purchase_request_cas in this module) is now
    # store=False. The account_payment / account_bank_statement_line
    # versions were already store=False. crossovered.budget compute
    # traversals into x_purchase_request use env.get() which is
    # runtime-guarded (returns None if model absent). No schema-time
    # need for the dep anymore.
    # Enables clean DAG: Sales -> Accounting -> Purchase (Purchase at
    # top of stack), where Purchase can freely depend on Accounting
    # for its own artifacts without creating a cycle.
    # v0.0.14 additions:
    #   * mrp — x_rm_production_orders / x_rm_production_varian
    #     m2o into mrp.production; without this dep the setup_nonrelated
    #     fails with KeyError on fresh install.
    #   * sale — x_rm_sales_order_line m2o into sale.order.
    #   * crm — x_rm_daily_s1/s2/s3 m2o into crm.team (sales centre).
    #   * stock — x_rm_production_orders.x_studio_warehouse into
    #     stock.location.
    #   * studio_usermodel_migration — x_rm_sales_order_line m2o into
    #     x_customer_group. That module owns the customer/vendor group
    #     catalog. Adds a new local dep edge into BugFix-Accounting,
    #     which was previously a root. No cycle: studio_usermodel_migration
    #     is itself a root.
    #
    # v0.0.15 additions:
    #   * project — x_temp_estimated.x_studio_project_no m2o into
    #     project.project. Standard Odoo module.
    #   * BugFix-Project — x_temp_estimated.x_studio_category m2o into
    #     x_project_category (owned by BugFix-Project). New local dep
    #     edge BugFix-Accounting -> BugFix-Project verified acyclic
    #     (BugFix-Project depends only on standard Odoo modules).
    #
    # v0.0.17 additions:
    #   * account_budget — standard Odoo Enterprise module owning
    #     crossovered.budget + crossovered.budget.lines (extended by
    #     models/crossovered_budget.py).
    #   * BugFix-Sales — crossovered.budget compute traversals into
    #     sale.order.x_studio_quotation_type / _inventory_short /
    #     _sub_contract fields, which BugFix-Sales owns.
    #   * BugFix-Purchase — crossovered.budget compute uses
    #     env['x_purchase_request'] (soft-guarded so absence doesn't
    #     crash, but declaring the dep is cleaner for fresh install).
    # v0.0.19 addition:
    #   * account_reports — v0.0.19 resolves the account.archived.tax.tag.tree
    #     inherit against account_reports.view_archived_tag_move_tree.
    # v0.0.23 addition:
    #   * bank-data — supplies the 19 bare x_ fields on account.move.line
    #     (x_dest_bank_micr, x_cbc_amount, x_return_code, ...) that the
    #     ported Studio tree-BankData + tree-EPF views reference. Also
    #     supplies the 17 hr.payslip fields and paymaster.config model.
    #     Verified acyclic (bank-data depends on account/hr/hr_payroll/base
    #     only). Root cause of the v0.0.22 install failure — rule captured
    #     as feedback-pin-source-verification in project memory.
    # v0.0.44 addition:
    #   * seed_master_data_and_settings - needed for the
    #     srv_sls_credit_note_notify_tharaka child action which uses
    #     activity_user_id=seed_master_data_and_settings.user_146 (Tharaka
    #     Herath). No cycle: seed only depends on base/stock/hr/mail.
    # v0.0.49: Restore "Pump Price Costing" form tab on x_sales_report_model.
    #   * views/x_sales_report_model_studio_ported_v2.xml: the
    #     `<page name="studio_page_l5MQG" invisible="1"/>` stub added
    #     in v0.0.31 (stripped because x_pump_price_costing wasn't
    #     on-disk) is replaced with the byte-verbatim 6994-byte page
    #     block from Clear-DB view 3786. 65 field columns on the
    #     nested x_pump_price_costing tree + parent.x_studio_actuals
    #     column-invisible expressions + page-level invisible bound
    #     to x_studio_report_code == 'Costing Work Sheet'.
    #   * All 66 field refs (65 on x_pump_price_costing + the O2M on
    #     x_sales_report_model) verified present on repair-test-101
    #     before landing.
    #   * INSTALL_JOURNEY.md item #4 "Pump Price Costing" restore
    #     path complete.
    # v0.0.48: x_pump_price_costing custom model port.
    #   * models/x_pump_price_costing.py declares the 69 Studio x_*
    #     fields from Clear-DB verbatim (0 rows on Clear-DB - schema-
    #     only asset). Order: x_studio_sequence asc, id asc. Mixed with
    #     mail.thread + mail.activity.mixin per the ir.model.data state.
    #   * models/x_sales_report_model.py: TODO comment for
    #     x_studio_pump_price_costing_ids O2M replaced with the real
    #     declaration pointing at the new model via
    #     x_studio_sales_report_model_id (the inverse M2O this file
    #     declares).
    #   * security/ir_model_pins.xml: added model_x_pump_price_costing
    #     pin so cross-refs resolve on module load.
    #   * security/ir.model.access.csv: base.group_user rw access.
    #   * Views (form, tree, search) not ported this pass - the Studio
    #     defaults on Clear-DB are auto-generated stubs, no
    #     act_window references any of them.
    #   * Unblocks INSTALL_JOURNEY.md item #4 "Pump Price Costing" tab
    #     restoration on x_sales_report_model form (follow-up commit).
    # v0.0.47: wired 18 base.automation stubs to their server actions.
    #   * data/server_actions.xml grew from 13 -> 22 records with
    #     byte-verbatim ports of the 9 previously-missing actions
    #     (1144, 1368, 1408, 1409, 1720, 1733, 1766, 1847, 2417).
    #     All state=code, usage=base_automation. Sizes: 239-1289 B.
    #   * data/automations.xml: every TODO comment replaced by
    #     <field name="action_server_ids" eval="[(6, 0, [ref('...')])]"/>
    #     18/18 wires. base.automation records now actually invoke
    #     their server actions on trigger.
    #   * New models/account_analytic_distribution_model.py declares
    #     x_studio_partner_mandatory (Bool) - required by action 2417
    #     (Update Analytic Tag Parameters). Clear-DB has no on-disk
    #     definition for this field either; we're the first Python
    #     owner. account.analytic.distribution.model is standard Odoo,
    #     transitively pulled by 'account'.
    # v0.0.46: reports/reports.xml ported from stub to full 6-report load:
    #   * report_payment_receipt (Clear-DB action 3455, "Jinasena Payment
    #     Receipt" on account.payment). Substantive A4-statement template
    #     using the account.paperformat_euro_bank_statement paperformat.
    #     Company header, receipt-no, customer info, amount + amount-in-words,
    #     cheque details, stamp-duty footer with cashier signature block.
    #   * report_journal_entry_1 (Clear-DB action 3469, "Journal Entry
    #     Report" on account.move). Empty Studio stub, kept for
    #     print-menu-binding parity.
    #   * report_journal_entry_2 (Clear-DB action 3470, "Journal Entry
    #     Report" on account.move). Full Pro-Forma-Invoice template
    #     (~10 KB). Named "Journal Entry Report" in the print menu but
    #     the body renders a pro forma invoice — Clear-DB mislabel
    #     preserved for byte-parity.
    #   * report_pro_forma_invoice (Clear-DB action 3468, "Pro forma
    #     Invoice" on account.move). Empty Studio stub, real content
    #     lives in report_journal_entry_2 (see above).
    #   * report_account_payment_1 / _2 (Clear-DB actions 3454 / 3456,
    #     both "account.payment Report"). Both empty stubs.
    # v0.0.45: last of the 9 server-action stubs ported byte-verbatim.
    #   * srv_imp_update_consignment_pi (Clear-DB action 1370, ~30 KB
    #     of Python). Reconciles vendor bill against consignment,
    #     aggregates charge/duty/tax across 4 billable buckets,
    #     rewrites invoice lines against x_imports_ledger_setup, and
    #     creates vendor-despatch + custom-clearance reversal journal
    #     entries when the consignment header enables them. See the
    #     comment block above the record in data/server_actions_v2.xml.
    #   * New models/product_template.py adds x_studio_charge_type
    #     (Selection Charge/Duty/Tax) + x_studio_non_billable (Bool)
    #     to product.template. Clear-DB pins them as state='manual'
    #     with pin.module='product'; on-disk we own them here because
    #     BugFix-Accounting is the only consumer (three
    #     product.product.search calls in the ported action, resolved
    #     via _inherits). No new manifest dep needed - 'product' is
    #     transitively pulled by 'account'/'sale'/'stock'.
    'depends': [
        'base_setup', 'account', 'account_budget', 'account_reports',
        'mrp', 'sale', 'crm', 'stock', 'project',
        'studio_usermodel_migration', 'BugFix-Project',
        'BugFix-Sales', 'bank-data',
        'seed_master_data_and_settings',
    ],
    # v0.0.2: data XMLs populated from Clear-DB snapshot via
    # scripts/populate_data_xmls.py (13 server actions, 22
    # automations, 66 window actions -- real content, no longer
    # just TODO stubs).
    #
    # NOT yet loaded (still TODO stubs):
    #   * reports/reports.xml -- 6 Studio QWeb reports need hand-porting
    #     as full QWeb templates + report actions.
    #   * views/ -- 84 view records need hand-porting (see VIEWS_TODO.md).
    'data': [
        'security/ir_model_pins.xml',
        'security/ir.model.access.csv',
        'data/server_actions.xml',
        # v0.0.20: 9 server-action stubs + 2 window actions needed by
        # views/account_move_studio_ported_v2.xml (which was hitting
        # "Action 2176 (id: 2176) does not exist" install failure
        # because it referenced Clear-DB's auto-numbered ids by
        # `name="NNNN"`). All 11 now have stable xmlids that the view
        # arch references via %(BugFix-Accounting.xxx)d interpolation.
        # Server-action stubs raise UserError with "port pending"
        # until each is filled with the Clear-DB Python code in
        # follow-up commits.
        'data/server_actions_v2.xml',
        'data/automations.xml',
        'data/act_windows.xml',
        'views/x_advance_payment_acco_studio_ported.xml',
        'views/x_custom_currency_studio_ported.xml',
        'views/x_custom_currency_rate_studio_ported.xml',
        'views/x_customer_posting_pro_studio_ported.xml',
        'views/x_lc_header_studio_ported.xml',
        'views/x_rm_cust_invoice_s1_studio_ported.xml',
        'views/x_rm_customer_wise_inv_studio_ported.xml',
        'views/x_rm_gross_margin_actu_studio_ported.xml',
        'views/x_rm_gross_margin_comp_studio_ported.xml',
        'views/x_temp_actual_budget_studio_ported.xml',
        'views/x_temp_tp_invoice_line_studio_ported.xml',
        'views/x_test_rm_gross_margin_studio_ported.xml',
        'views/x_tp_invoice_header_studio_ported.xml',
        'views/x_temp_tp_invoice_head_studio_ported.xml',
        'views/account_report_expression_studio_ported.xml',
        'views/account_tax_group_studio_ported.xml',
        'views/account_account_studio_ported.xml',
        'views/account_payment_studio_ported.xml',
        'views/account_payment_term_studio_ported.xml',
        'views/account_journal_studio_ported.xml',
        'views/account_analytic_plan_studio_ported.xml',
        'views/account_move_studio_ported.xml',
        'views/account_report_external_value_studio_ported.xml',
        'views/account_tax_repartition_line_studio_ported.xml',
        'views/account_analytic_account_studio_ported.xml',
        'views/account_asset_studio_ported.xml',
        'views/account_group_studio_ported.xml',
        'views/account_tax_studio_ported.xml',
        'views/account_analytic_line_studio_ported.xml',
        # v0.0.18: auto-generated view records ported from Clear-DB
        # by scripts/port_bugfix_accounting_views.py (2026-08-29).
        # 40 files, 140 view records covering all 40 target models —
        # default primary form/tree/search PLUS priority-99 Studio
        # inherits with byte-verbatim arch_db. Loaded AFTER the older
        # hand-ported views so any id collisions get caught by
        # ir.model.data uniqueness (the earlier records win).
        'views/account_analytic_line_studio_ported_v2.xml',
        # v0.0.19: TODO markers resolved. account.out.invoice.tree
        # inherits resolved to account.view_out_invoice_tree +
        # account.view_in_invoice_tree (both children of the same
        # Studio pin name but different Odoo canonical xmlids).
        # account.move.line.tree-ETF and -BankData now inherit from
        # our own ported_view_8294 / ported_view_8295 primary parents
        # (Clear-DB's ad-hoc primaries with no ir.model.data pin —
        # rehosted verbatim). account.archived.tax.tag.tree resolved
        # to account_reports.view_archived_tag_move_tree.
        'views/account_move_studio_ported_v2.xml',
        'views/account_move_line_studio_ported_v2.xml',
        'views/account_payment_studio_ported_v2.xml',
        'views/crossovered_budget_studio_ported_v2.xml',
        'views/x_advance_payment_acco_studio_ported_v2.xml',
        'views/x_consignment_charge_h_studio_ported_v2.xml',
        'views/x_custom_currency_studio_ported_v2.xml',
        'views/x_custom_currency_rate_studio_ported_v2.xml',
        'views/x_customer_posting_pro_studio_ported_v2.xml',
        'views/x_journal_types_studio_ported_v2.xml',
        'views/x_lc_header_studio_ported_v2.xml',
        'views/x_misc_charge_codes_studio_ported_v2.xml',
        'views/x_rm_cust_invoice_s1_studio_ported_v2.xml',
        'views/x_rm_customer_wise_inv_studio_ported_v2.xml',
        'views/x_rm_daily_s1_studio_ported_v2.xml',
        'views/x_rm_daily_s2_studio_ported_v2.xml',
        'views/x_rm_daily_s3_studio_ported_v2.xml',
        'views/x_rm_daily_sales_repor_studio_ported_v2.xml',
        'views/x_rm_date_test_studio_ported_v2.xml',
        'views/x_rm_gross_margin_actu_studio_ported_v2.xml',
        'views/x_rm_gross_margin_comp_studio_ported_v2.xml',
        'views/x_rm_gross_margin_esti_studio_ported_v2.xml',
        'views/x_rm_gross_margin_esti_line_7e86d_studio_ported_v2.xml',
        'views/x_rm_gross_margin_invo_studio_ported_v2.xml',
        'views/x_rm_none_moving_studio_ported_v2.xml',
        'views/x_rm_prod_summary_spli_studio_ported_v2.xml',
        'views/x_rm_production_orders_studio_ported_v2.xml',
        'views/x_rm_production_varian_studio_ported_v2.xml',
        'views/x_rm_sales_order_line_studio_ported_v2.xml',
        'views/x_rm_sales_prod_purch_studio_ported_v2.xml',
        'views/x_sales_report_model_studio_ported_v2.xml',
        'views/x_sales_report_type_studio_ported_v2.xml',
        'views/x_temp_actual_budget_studio_ported_v2.xml',
        'views/x_temp_estimated_studio_ported_v2.xml',
        'views/x_temp_tp_invoice_head_studio_ported_v2.xml',
        'views/x_temp_tp_invoice_line_studio_ported_v2.xml',
        'views/x_test_rm_gross_margin_studio_ported_v2.xml',
        'views/x_tp_invoice_header_studio_ported_v2.xml',
        'views/x_tp_invoice_line_studio_ported_v2.xml',
        # v0.0.46: 6 Studio QWeb reports (2 substantive + 4 empty stubs).
        # See the v0.0.46 comment block above for per-report notes and
        # Clear-DB id -> local xmlid correspondence.
        'reports/reports.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
