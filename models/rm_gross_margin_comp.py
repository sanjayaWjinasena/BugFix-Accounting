from odoo import fields, models


class XRmGrossMarginComp(models.Model):
    """Studio-ported custom model rm_gross_margin_comp."""

    _name = "rm_gross_margin_comp"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.activity.mixin"]
    _description = "RM Gross Margin - Comparison"

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
    delivered_amount = fields.Float(string="Delivered Amount")
    delivered_not_invoiced = fields.Float(string="Delivered not Invoiced")
    estimated_amount = fields.Float(string="Estimated Amount")
    header_reference = fields.Char(string="Header Reference")
    invoiced_amount = fields.Float(string="Invoiced Amount")
    many2one_field_7fcuw = fields.Many2one("product.product", string="Product")
    sales_order = fields.Many2one("sale.order", string="Sales Order")
    sales_report_model_id = fields.Many2one(
        "sales_report_model", string="Sales Report Model Id", ondelete="cascade"
    )
    sequence = fields.Integer(string="Sequence")


class XRmGrossMarginCompGap(models.Model):
    _inherit = "rm_gross_margin_comp"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
