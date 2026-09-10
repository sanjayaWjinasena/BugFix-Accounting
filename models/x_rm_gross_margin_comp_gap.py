# -*- coding: utf-8 -*-
from odoo import models, fields

class XRmGrossMarginCompGap(models.Model):
    _inherit = 'x_rm_gross_margin_comp'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
