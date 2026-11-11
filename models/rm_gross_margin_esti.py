"""rm_gross_margin_esti — Gross-margin ESTIMATE header row.

Per-category estimate row under a sales_report_model. Bundles a
transaction type (Item / Expense / Fee / Hour), estimated amount,
actual cost / balance cost, and a one2many into temp_estimated
for line-level breakdown.
"""

from odoo import fields, models


class XRmGrossMarginEsti(models.Model):
    _name = "rm_gross_margin_esti"
    _description = "RM Gross Margin - Estimated"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "sequence, id"
    _rec_name = "name"

    active = fields.Boolean(default=True)
    name = fields.Char()
    actual_cost = fields.Float(string="Delivered Amount")
    balance_cost = fields.Float(string="Balance Amount")
    category = fields.Char()
    estimated_amt = fields.Float(string="Estimated Amt.")
    group_title = fields.Char(string="          ")
    header_reference = fields.Char()
    sales_order_line_ids = fields.One2many(
        "temp_estimated",
        "estimated_line_ids",
        string="Sales Order Line Ids",
    )
    sales_report_model_id = fields.Many2one(
        "sales_report_model",
        string="Sales Report Model Id",
        ondelete="cascade",
    )
    sequence = fields.Integer(default=10)
    total = fields.Boolean()
    transaction_type = fields.Selection(
        [
            ("Item", "Item"),
            ("Expense", "Expense"),
            ("Fee", "Fee"),
            ("Hour", "Hour"),
        ],
    )


class XRmGrossMarginEstiGap(models.Model):
    _inherit = "rm_gross_margin_esti"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char()
