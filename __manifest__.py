# -*- coding: utf-8 -*-
{
    'name': 'BugFix - Accounting',
    'version': '17.0.0.0.9',
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
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
