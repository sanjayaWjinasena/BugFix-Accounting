# -*- coding: utf-8 -*-
from odoo import models, fields

class XTestRmGrossMarginGap(models.Model):
    _inherit = 'x_test_rm_gross_margin'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Description', required=True)
