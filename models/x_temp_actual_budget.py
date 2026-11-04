from odoo import fields, models


class XTempActualBudget(models.Model):
    """Studio-ported custom model x_temp_actual_budget."""

    _name = "x_temp_actual_budget"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.activity.mixin"]
    _description = "Temp_Actual_Budget"

    active = fields.Boolean(string="Active")
    x_currency_id = fields.Many2one("res.currency", string="Currency")
    name = fields.Char(string="Name")
    x_studio_actual_line_ids = fields.Many2one(
        "x_rm_gross_margin_actu", string="Actual Line Ids", ondelete="cascade"
    )
    x_studio_analytic_account_id = fields.Many2one(
        "account.analytic.account", string="Analytic Account"
    )
    x_studio_budget_line_ids = fields.Many2one(
        "crossovered.budget.lines", string="Budget Line Ids"
    )
    x_studio_crossovered_budget_id = fields.Many2one(
        "crossovered.budget", string="Budget"
    )
    x_studio_date_from = fields.Date(string="Start Date")
    x_studio_date_to = fields.Date(string="End Date")
    x_studio_planned_amount = fields.Float(
        string="Planned Amount"
    )  # was Monetary (no currency_field)
    sequence = fields.Integer(string="Sequence")


class XTempActualBudgetGap(models.Model):
    _inherit = "x_temp_actual_budget"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    x_currency_id = fields.Many2one(comodel_name="res.currency", string="Currency")
    name = fields.Char(string="Name")
