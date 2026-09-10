# -*- coding: utf-8 -*-
from odoo import models, fields

class XMiscChargeCodesGap(models.Model):
    _inherit = 'x_misc_charge_codes'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Misc. Charge Code')
