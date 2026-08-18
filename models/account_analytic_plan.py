# -*- coding: utf-8 -*-
from odoo import fields, models


class AccountAnalyticPlan(models.Model):
    _inherit = 'account.analytic.plan'

    x_group_id_account_analytic_account_count = fields.Integer(string='Group count', store=False)
    x_group_id_account_analytic_line_count = fields.Integer(string='Group count', store=False)
