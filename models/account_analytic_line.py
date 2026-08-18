# -*- coding: utf-8 -*-
from odoo import fields, models


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    x_plan15_id = fields.Many2one('account.analytic.account', string='Department')
    x_plan18_id = fields.Many2one('account.analytic.account', string='Cost Center')
    x_plan19_id = fields.Many2one('account.analytic.account', string='Sales Center')
    x_plan20_id = fields.Many2one('account.analytic.account', string='Product Group')
    x_plan21_id = fields.Many2one('account.analytic.account', string='Employee')
