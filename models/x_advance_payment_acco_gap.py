# -*- coding: utf-8 -*-
from odoo import models, fields

class XAdvancePaymentAccoGap(models.Model):
    _inherit = 'x_advance_payment_acco'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
