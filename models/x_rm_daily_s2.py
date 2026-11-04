"""x_rm_daily_s2 — Daily-sales reporting row, variant 2.

Identical field shape to x_rm_daily_s1. Studio created these as
separate models to allow independent pivots of the same underlying
sales data under different filters/breakdowns.
"""

from odoo import fields, models


class XRmDailyS2(models.Model):
    _name = "x_rm_daily_s2"
    _description = "RM Daily S2"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "sequence, id"
    _rec_name = "name"

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(string="Name")
    x_studio_invoice_date = fields.Date(string="Invoice Date")
    x_studio_number = fields.Char(string="Number")
    x_studio_partner = fields.Many2one("res.partner", string="Partner")
    x_studio_product_id = fields.Many2one("product.product", string="Product")
    quantity = fields.Float(string="Quantity")
    x_studio_sales_centre = fields.Many2one("crm.team", string="Sales Centre")
    x_studio_sales_report_model_id = fields.Many2one(
        "x_sales_report_model",
        string="Sales Report Model",
    )
    sequence = fields.Integer(string="Sequence", default=10)
    x_studio_value = fields.Float(string="Value")


class XRmDailyS2Gap(models.Model):
    _inherit = "x_rm_daily_s2"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
