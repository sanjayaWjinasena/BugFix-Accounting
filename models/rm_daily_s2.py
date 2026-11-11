"""rm_daily_s2 — Daily-sales reporting row, variant 2.

Identical field shape to rm_daily_s1. Studio created these as
separate models to allow independent pivots of the same underlying
sales data under different filters/breakdowns.
"""

from odoo import fields, models


class XRmDailyS2(models.Model):
    _name = "rm_daily_s2"
    _description = "RM Daily S2"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "sequence, id"
    _rec_name = "name"

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(string="Name")
    accounting_invoice_date = fields.Date(string="Invoice Date")
    number = fields.Char(string="Number")
    partner = fields.Many2one("res.partner", string="Partner")
    product_id = fields.Many2one("product.product", string="Product")
    quantity = fields.Float(string="Quantity")
    sales_centre = fields.Many2one("crm.team", string="Sales Centre")
    sales_report_model_id = fields.Many2one(
        "sales_report_model",
        string="Sales Report Model",
    )
    sequence = fields.Integer(string="Sequence", default=10)
    value = fields.Float(string="Value")


class XRmDailyS2Gap(models.Model):
    _inherit = "rm_daily_s2"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
