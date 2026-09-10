# -*- coding: utf-8 -*-
from odoo import models, fields

class XRmDailySalesReporGap(models.Model):
    _inherit = 'x_rm_daily_sales_repor'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
