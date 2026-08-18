# -*- coding: utf-8 -*-
from odoo import fields, models


class XTestRmGrossMargin(models.Model):
    """Studio-ported custom model x_test_rm_gross_margin."""
    _name = 'x_test_rm_gross_margin'
    _description = 'Test Rm Gross Margin'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Description', required=True)
    x_studio_sequence = fields.Integer(string='Sequence')
