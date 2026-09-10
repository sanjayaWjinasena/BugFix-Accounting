# -*- coding: utf-8 -*-
from odoo import models, fields

class XConsignmentChargeHGap(models.Model):
    _inherit = 'x_consignment_charge_h'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
