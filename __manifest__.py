# -*- coding: utf-8 -*-
{
    'name': 'BugFix - Accounting',
    'version': '17.0.0.0.1',
    'summary': 'Studio-to-Python port for BugFix-Accounting',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Accounting',
    'license': 'LGPL-3',
    # Do NOT depend on studio_customization -- Odoo SH does not ship
    # a manifest for it, listing it causes install skip.
    'depends': ['base_setup', 'account'],
    'data': [
        'security/ir_model_pins.xml',
        'security/ir.model.access.csv',
        'data/server_actions.xml',
        'data/automations.xml',
        'data/act_windows.xml',
        'reports/reports.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}