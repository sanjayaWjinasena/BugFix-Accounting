# -*- coding: utf-8 -*-
"""v0.0.141: detach this module's ir.model.data pointers for the three
x_misc_charge_codes link fields that moved to BugFix-Purchase v0.1.0.176.

Why pre-migrate: at the end of an upgrade Odoo's ir.model.data._process_end
walks every xmlid of the upgraded modules that was NOT re-loaded. For
    BugFix-Accounting.field_x_misc_charge_codes__x_studio_{charges,duties,taxes}_line_id
that is now the case (the field is no longer declared here). If no OTHER
xmlid pointed at the same ir.model.fields row, _process_end would UNLINK the
field and DROP its column -- live data. Removing just the ir.model.data rows
up front means the field row is never a cleanup candidate; BugFix-Purchase's
own reflection then re-attaches its xmlids to the same field rows.

ORM only (env['ir.model.data'].unlink on the pointer rows -- NOT the fields);
no cr.execute. Idempotent: no-op on fresh installs (version is None) and
when the rows are already gone.
"""
import logging

from odoo import api, SUPERUSER_ID

_logger = logging.getLogger(__name__)

MODULE = 'BugFix-Accounting'
XMLIDS = (
    'field_x_misc_charge_codes__x_studio_charges_line_id',
    'field_x_misc_charge_codes__x_studio_duties_line_id',
    'field_x_misc_charge_codes__x_studio_taxes_line_id',
)


def migrate(cr, version):
    if not version:
        return
    env = api.Environment(cr, SUPERUSER_ID, {})
    imd = env['ir.model.data'].sudo().search([
        ('module', '=', MODULE),
        ('model', '=', 'ir.model.fields'),
        ('name', 'in', XMLIDS),
    ])
    if imd:
        names = imd.mapped('name')
        imd.unlink()
        _logger.info(
            "%s v0.0.141: detached %d ir.model.data pointer(s) for moved "
            "x_misc_charge_codes link fields: %s", MODULE, len(names), names,
        )
