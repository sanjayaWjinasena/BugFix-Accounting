# -*- coding: utf-8 -*-
from odoo import models, fields

class XTempEstimatedGap(models.Model):
    _inherit = 'x_temp_estimated'
    _rec_name = 'x_name'  # Clear-DB Studio model: records are named by x_name

    x_active = fields.Boolean(string='Active')
    x_currency_id = fields.Many2one(comodel_name='res.currency', string='Currency')
    x_name = fields.Char(string='Name')
