# -*- coding: utf-8 -*-
from odoo import models, fields

class XRmProductionVarianGap(models.Model):
    _inherit = 'x_rm_production_varian'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
