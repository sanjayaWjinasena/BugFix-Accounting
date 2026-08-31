# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    x_studio_charge_type = fields.Selection([
        ('Charge', 'Charge'),
        ('Duty', 'Duty'),
        ('Tax', 'Tax'),
    ], string='Charge Type')
    x_studio_non_billable = fields.Boolean(string='Non Billable')
