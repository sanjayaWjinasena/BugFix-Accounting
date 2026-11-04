"""x_temp_estimated — line-level detail behind both estimated + actual
gross-margin reporting.

This model is the row-side of TWO one2many parents:
  * x_rm_gross_margin_esti.x_studio_sales_order_line_ids
      inverse: x_studio_estimated_line_ids
  * x_rm_gross_margin_actu.x_studio_sales_order_line_ids
      inverse: x_studio_actual_line_ids

Studio declared both inverses as `many2one` (parent-pointer style),
which is Odoo's standard one2many idiom. Same shape used by
x_temp_actual_budget for budget lines.
"""

from odoo import fields, models


class XTempEstimated(models.Model):
    _name = "x_temp_estimated"
    _description = "Temp_Estimated"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "sequence, id"
    _rec_name = "name"

    active = fields.Boolean(string="Active", default=True)
    x_currency_id = fields.Many2one("res.currency", string="Currency")
    name = fields.Char(string="Name")

    # Parent-pointer m2os (inverse for the header's one2many).
    x_studio_actual_line_ids = fields.Many2one(
        "x_rm_gross_margin_actu",
        string="Actual Line Ids",
        ondelete="cascade",
    )
    x_studio_estimated_line_ids = fields.Many2one(
        "x_rm_gross_margin_esti",
        string="Estimated Line Ids",
        ondelete="cascade",
    )

    x_studio_category = fields.Many2one(
        "x_project_category",
        string="Category",
    )
    x_studio_customer = fields.Many2one("res.partner", string="Customer")
    x_studio_delivered_qty = fields.Float(string="Delivered Qty")
    description = fields.Char(string="Description")
    x_studio_product_id = fields.Many2one(
        "product.product",
        string="Product Id",
    )
    x_studio_project_no = fields.Many2one(
        "project.project",
        string="Project No",
    )
    quantity = fields.Float(string="Quantity")
    sales_order = fields.Many2one("sale.order", string="Sales Order")
    x_studio_sales_order_line_id = fields.Many2one(
        "sale.order.line",
        string="Sales Order Line Id",
    )
    sequence = fields.Integer(string="Sequence", default=10)
    x_studio_sub_total = fields.Monetary(
        string="Sub Total",
        currency_field="x_currency_id",
    )
    x_studio_trans_type = fields.Char(string="Trans Type")
    unit_price = fields.Float(string="Unit Price")
    x_studio_uom = fields.Many2one("uom.uom", string="UOM")


class XTempEstimatedGap(models.Model):
    _inherit = "x_temp_estimated"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    x_currency_id = fields.Many2one(comodel_name="res.currency", string="Currency")
    name = fields.Char(string="Name")
