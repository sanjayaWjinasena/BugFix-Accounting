# -*- coding: utf-8 -*-
from odoo import models, fields

class XRmSalesOrderLineGap(models.Model):
    _inherit = 'x_rm_sales_order_line'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
