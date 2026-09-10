# -*- coding: utf-8 -*-
from odoo import models, fields

class XRmProductionOrdersGap(models.Model):
    _inherit = 'x_rm_production_orders'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
