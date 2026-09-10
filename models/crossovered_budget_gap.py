# -*- coding: utf-8 -*-
from odoo import models, fields

class CrossoveredBudgetGap(models.Model):
    _inherit = 'crossovered.budget'

    x_currency_id = fields.Many2one(comodel_name='res.currency', string='Currency')
