# -*- coding: utf-8 -*-
from odoo import models, fields

class XLcHeaderGap(models.Model):
    _inherit = 'x_lc_header'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='LC Registration No')
