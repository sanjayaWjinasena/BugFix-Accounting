# -*- coding: utf-8 -*-
"""v17.0.0.0.147: fields that are related on Clear-DB had lost related= in the port and are linked again
(stored). Their columns already existed, and Odoo does not backfill an existing column for a field that
becomes related, so recompute them for existing records. ORM only.
"""
from odoo import api, SUPERUSER_ID

FIELDS = {'x_sales_report_model': ['x_studio_report_code']}


def migrate(cr, version):
    if not version:
        return
    env = api.Environment(cr, SUPERUSER_ID, {'active_test': False})
    for model, names in FIELDS.items():
        if model not in env:
            continue
        records = env[model].search([])
        for name in names:
            if name in records._fields:
                env.add_to_compute(records._fields[name], records)
        records.flush_model([n for n in names if n in records._fields])
