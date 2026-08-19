# -*- coding: utf-8 -*-
{
    'name': 'BugFix - Accounting',
    'version': '17.0.0.0.11',
    'summary': 'Studio-to-Python port for BugFix-Accounting',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Accounting',
    'license': 'LGPL-3',
    # Do NOT depend on studio_customization -- Odoo SH does not ship
    # a manifest for it, listing it causes install skip.
    'depends': ['base_setup', 'account'],
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
        'views/account_move_line_studio_ported.xml',
        'views/account_payment_studio_ported.xml',
        'views/account_payment_term_studio_ported.xml',
        'views/account_journal_studio_ported.xml',
        'views/account_analytic_plan_studio_ported.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
