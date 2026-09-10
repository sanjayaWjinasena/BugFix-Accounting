# -*- coding: utf-8 -*-
from odoo import models, fields

class XCustomCurrencyRateGap(models.Model):
    _inherit = 'x_custom_currency_rate'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
