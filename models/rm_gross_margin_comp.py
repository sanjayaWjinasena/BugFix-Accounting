from odoo import fields, models


class XRmGrossMarginComp(models.Model):
    """Studio-ported custom model rm_gross_margin_comp."""

    _name = "rm_gross_margin_comp"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.activity.mixin"]
    _description = "RM Gross Margin - Comparison"

    active = fields.Boolean()
    name = fields.Char()
    delivered_amount = fields.Float()
    delivered_not_invoiced = fields.Float(string="Delivered not Invoiced")
    estimated_amount = fields.Float()
    header_reference = fields.Char()
    invoiced_amount = fields.Float()
    many2one_field_7fcuw = fields.Many2one("product.product", string="Product")
    sales_order = fields.Many2one("sale.order")
    sales_report_model_id = fields.Many2one(
        "sales_report_model", string="Sales Report Model Id", ondelete="cascade"
    )
    sequence = fields.Integer()


class XRmGrossMarginCompGap(models.Model):
    _inherit = "rm_gross_margin_comp"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char()
