"""rm_gross_margin_actu — Gross-margin ACTUAL header row.

Actual counterpart to rm_gross_margin_esti. Same shape plus
budget-line linkage via temp_actual_budget.

v0.0.15 (chunk 2) filled in the two TODO one2many inverses that the
initial sentinel port left blank + populated the transaction_type_1
selection tuple.
"""

from odoo import fields, models


class XRmGrossMarginActu(models.Model):
    _name = "rm_gross_margin_actu"
    _inherit = ["mail.activity.mixin"]
    _description = "RM Gross Margin - Actuals"
    _order = "sequence, id"
    _rec_name = "name"

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(string="Name")
    budget_line = fields.Boolean(string="Budget Line")
    budget_line_ids = fields.One2many(
        "temp_actual_budget",
        "actual_line_ids",
        string="Budget Line Ids",
    )
    cost_price = fields.Float(string="Delivered Amount")
    estimated_total = fields.Float(string="Estimated Amount")
    header_reference = fields.Char(string="Header Reference")
    normal_line = fields.Boolean(string="Normal Line")
    other_expenses = fields.Char(string="Other Expenses")
    sales_order_line_ids = fields.One2many(
        "temp_estimated",
        "actual_line_ids",
        string="Sales Order Line Ids",
    )
    sales_report_model_id = fields.Many2one(
        "sales_report_model",
        string="Sales Report Model Id",
        ondelete="cascade",
    )
    sequence = fields.Integer(string="Sequence", default=10)
    transaction_type_1 = fields.Selection(
        [
            ("Item", "Item"),
            ("Expense", "Expense"),
            ("Fee", "Fee"),
            ("Hour", "Hour"),
        ],
        string="Transaction Type",
    )
    variance_est_act = fields.Float(string="Variance (Est - Act)")


class XRmGrossMarginActuGap(models.Model):
    _inherit = "rm_gross_margin_actu"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
