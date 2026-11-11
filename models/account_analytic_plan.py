from odoo import fields, models


class AccountAnalyticPlan(models.Model):
    _inherit = "account.analytic.plan"

    group_id_account_analytic_account_count = fields.Integer(
        string="Group count", store=False
    )
    group_id_account_analytic_line_count = fields.Integer(
        string="Group count", store=False
    )


class AccountAnalyticPlanGap(models.Model):
    _inherit = "account.analytic.plan"

    group_id_account_analytic_account_count = fields.Integer(string="Group count")
    group_id_account_analytic_line_count = fields.Integer(string="Group count")
