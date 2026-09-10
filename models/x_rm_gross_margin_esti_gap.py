# -*- coding: utf-8 -*-
from odoo import models, fields

class XRmGrossMarginEstiGap(models.Model):
    _inherit = 'x_rm_gross_margin_esti'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
