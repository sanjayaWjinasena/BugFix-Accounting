from odoo import fields, models


class XTempActualBudget(models.Model):
    """Studio-ported custom model temp_actual_budget."""

    _name = "temp_actual_budget"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.activity.mixin"]
    _description = "Temp_Actual_Budget"

    active = fields.Boolean(string="Active")
    currency_id = fields.Many2one("res.currency", string="Currency")
    name = fields.Char(string="Name")
    actual_line_ids = fields.Many2one(
        "rm_gross_margin_actu", string="Actual Line Ids", ondelete="cascade"
    )
    analytic_account_id = fields.Many2one(
        "account.analytic.account", string="Analytic Account"
    )
    budget_line_ids = fields.Many2one(
        "crossovered.budget.lines", string="Budget Line Ids"
    )
    crossovered_budget_id = fields.Many2one(
        "crossovered.budget", string="Budget"
    )
    date_from = fields.Date(string="Start Date")
    date_to = fields.Date(string="End Date")
    planned_amount = fields.Float(
        string="Planned Amount"
    )  # was Monetary (no currency_field)
    sequence = fields.Integer(string="Sequence")


class XTempActualBudgetGap(models.Model):
    _inherit = "temp_actual_budget"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    currency_id = fields.Many2one(comodel_name="res.currency", string="Currency")
    name = fields.Char(string="Name")
