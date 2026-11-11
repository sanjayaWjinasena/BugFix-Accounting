from odoo import fields, models


class XTempActualBudget(models.Model):
    """Studio-ported custom model temp_actual_budget."""

    _name = "temp_actual_budget"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.activity.mixin"]
    _description = "Temp_Actual_Budget"

    active = fields.Boolean()
    currency_id = fields.Many2one("res.currency")
    name = fields.Char()
    actual_line_ids = fields.Many2one(
        "rm_gross_margin_actu", string="Actual Line Ids", ondelete="cascade"
    )
    analytic_account_id = fields.Many2one("account.analytic.account")
    budget_line_ids = fields.Many2one(
        "crossovered.budget.lines", string="Budget Line Ids"
    )
    crossovered_budget_id = fields.Many2one("crossovered.budget", string="Budget")
    date_from = fields.Date(string="Start Date")
    date_to = fields.Date(string="End Date")
    planned_amount = fields.Float()  # was Monetary (no currency_field)
    sequence = fields.Integer()


class XTempActualBudgetGap(models.Model):
    _inherit = "temp_actual_budget"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    currency_id = fields.Many2one(comodel_name="res.currency")
    name = fields.Char()
