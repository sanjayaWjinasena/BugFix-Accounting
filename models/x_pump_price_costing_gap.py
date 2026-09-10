# -*- coding: utf-8 -*-
from odoo import models, fields

class XPumpPriceCostingGap(models.Model):
    _inherit = 'x_pump_price_costing'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
