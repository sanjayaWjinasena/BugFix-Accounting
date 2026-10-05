# -*- coding: utf-8 -*-
from odoo import fields, models


class XTestRmGrossMargin(models.Model):
    """Studio-ported custom model x_test_rm_gross_margin."""
    _name = 'x_test_rm_gross_margin'
    _rec_name = 'x_name'  # Clear-DB Studio model: records are named by x_name
    _inherit = ['mail.activity.mixin']
    _description = 'Test - RM Gross Margin - Actuals'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Description', required=True)
    x_studio_sequence = fields.Integer(string='Sequence')
