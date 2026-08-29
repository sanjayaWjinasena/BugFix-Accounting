# -*- coding: utf-8 -*-
"""x_rm_date_test — Studio-created test reporting model.

Small catchall reporting row keyed off x_sales_report_model_id (the
shared header). Kept in the port because Clear-DB has it as
state='manual' with 4 fields and Studio pins it; a fresh install
without this model would break any menu / view that references it.

No computes, no cross-repo refs.
"""
from odoo import fields, models


class XRmDateTest(models.Model):
    _name = 'x_rm_date_test'
    _description = 'Date Test Reporting Row'
    _order = 'x_studio_sequence, id'
    _rec_name = 'x_name'

    x_active = fields.Boolean(string='Active', default=True)
    x_name = fields.Char(string='Name')
    x_studio_date_test = fields.Date(string='Date Test')
    x_studio_sequence = fields.Integer(string='Sequence', default=10)
