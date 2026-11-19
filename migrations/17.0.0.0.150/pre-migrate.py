# -*- coding: utf-8 -*-
"""v0.0.150 (pre): Purchasing Cost and Sales Summary move into code (data/account_reports_jinasena.xml).

They were made by hand on upgrade-testing (no xmlid). Adopt each existing report, found by name,
and its report action (found by the report it opens) under the file's xmlids, so the upgrade
updates them instead of creating duplicates. The report's existing columns and lines (with their
expressions) are removed first: the file re-creates them exactly. Nothing else is touched.
ORM only; no-op on fresh installs and once adopted.
"""
import ast
import logging

from odoo import api, SUPERUSER_ID

_logger = logging.getLogger(__name__)

MODULE = 'BugFix-Accounting'
# report name: (report xmlid, client action xmlid)
REPORTS = {
    'Purchasing Cost': ('account_report_purchasing_cost', 'action_report_purchasing_cost'),
    'Sales Summary': ('account_report_sales_summary', 'action_report_sales_summary'),
}


def _report_id_of(action):
    try:
        return (ast.literal_eval(action.context or '{}') or {}).get('report_id')
    except Exception:
        return None


def migrate(cr, version):
    if not version:
        return
    env = api.Environment(cr, SUPERUSER_ID, {'active_test': False})
    imd = env['ir.model.data'].sudo()
    for name, (report_xmlid, action_xmlid) in REPORTS.items():
        if imd.search_count([('module', '=', MODULE), ('name', '=', report_xmlid)]):
            continue
        report = env['account.report'].search([('name', '=', name)], limit=1)
        if not report:
            continue
        report.line_ids.unlink()
        report.column_ids.unlink()
        imd.create({'module': MODULE, 'name': report_xmlid, 'model': 'account.report', 'res_id': report.id, 'noupdate': False})
        action = env['ir.actions.client'].search([('tag', '=', 'account_report')]).filtered(lambda a: _report_id_of(a) == report.id)[:1]
        if action and not imd.search_count([('module', '=', MODULE), ('name', '=', action_xmlid)]):
            imd.create({'module': MODULE, 'name': action_xmlid, 'model': 'ir.actions.client', 'res_id': action.id, 'noupdate': False})
        _logger.info('%s: adopted report %s (%s) and action %s', MODULE, report.id, name, action.id if action else None)
