# -*- coding: utf-8 -*-
from odoo import models, fields

class XRmSalesProdPurchGap(models.Model):
    _inherit = 'x_rm_sales_prod_purch'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
