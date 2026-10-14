from odoo import fields, models


class AccountAnalyticPlanGap(models.Model):
    _inherit = "account.analytic.plan"

    x_group_id_account_analytic_account_count = fields.Integer(string="Group count")
    x_group_id_account_analytic_line_count = fields.Integer(string="Group count")
