# -*- coding: utf-8 -*-
from odoo import models, fields

class XTempEstimatedGap(models.Model):
    _inherit = 'x_temp_estimated'

    x_active = fields.Boolean(string='Active')
    x_currency_id = fields.Many2one(comodel_name='res.currency', string='Currency')
    x_name = fields.Char(string='Name')
