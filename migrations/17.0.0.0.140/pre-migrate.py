# -*- coding: utf-8 -*-
"""v17.0.0.0.140: delete stale ir.default rows for
x_misc_charge_codes.x_studio_credit_acc_type and x_studio_debit_acc_type.

These defaults were shipped in v135 via ir_defaults_unblocked.xml but
caused Jinasena_MasterData_Purchase's x_misc_charge_codes.csv to fail
with "Wrong value for ... 'G/L Account'" on each row. v139 removed the
XML records but noupdate=1 means the DB rows persist; this migration
deletes them explicitly so a fresh / in-place install path both work.

Uses ORM env['ir.default'].unlink — no cr.execute. Idempotent (no-op
when rows don't exist).
"""
import logging

from odoo import api, SUPERUSER_ID

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    if not version:
        return
    env = api.Environment(cr, SUPERUSER_ID, {})
    Fld = env['ir.model.fields'].sudo()
    Default = env['ir.default'].sudo()
    for fname in ('x_studio_credit_acc_type', 'x_studio_debit_acc_type'):
        fld = Fld.search(
            [('model', '=', 'x_misc_charge_codes'), ('name', '=', fname)],
            limit=1,
        )
        if not fld:
            continue
        stale = Default.search([('field_id', '=', fld.id)])
        if stale:
            stale.unlink()
            _logger.info(
                "BugFix-Accounting v140: removed %d stale ir.default on "
                "x_misc_charge_codes.%s", len(stale), fname,
            )
