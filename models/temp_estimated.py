"""temp_estimated — line-level detail behind both estimated + actual
gross-margin reporting.

This model is the row-side of TWO one2many parents:
  * rm_gross_margin_esti.sales_order_line_ids
      inverse: estimated_line_ids
  * rm_gross_margin_actu.sales_order_line_ids
      inverse: actual_line_ids

Studio declared both inverses as `many2one` (parent-pointer style),
which is Odoo's standard one2many idiom. Same shape used by
temp_actual_budget for budget lines.
"""

from odoo import fields, models


class XTempEstimated(models.Model):
    _name = "temp_estimated"
    _description = "Temp_Estimated"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "sequence, id"
    _rec_name = "name"

    active = fields.Boolean(string="Active", default=True)
    currency_id = fields.Many2one("res.currency", string="Currency")
    name = fields.Char(string="Name")

    # Parent-pointer m2os (inverse for the header's one2many).
    actual_line_ids = fields.Many2one(
        "rm_gross_margin_actu",
        string="Actual Line Ids",
        ondelete="cascade",
    )
    estimated_line_ids = fields.Many2one(
        "rm_gross_margin_esti",
        string="Estimated Line Ids",
        ondelete="cascade",
    )

    category = fields.Many2one(
        "project_category",
        string="Category",
    )
    customer = fields.Many2one("res.partner", string="Customer")
    delivered_qty = fields.Float(string="Delivered Qty")
    description = fields.Char(string="Description")
    product_id = fields.Many2one(
        "product.product",
        string="Product Id",
    )
    project_no = fields.Many2one(
        "project.project",
        string="Project No",
    )
    quantity = fields.Float(string="Quantity")
    sales_order = fields.Many2one("sale.order", string="Sales Order")
    sales_order_line_id = fields.Many2one(
        "sale.order.line",
        string="Sales Order Line Id",
    )
    sequence = fields.Integer(string="Sequence", default=10)
    sub_total = fields.Monetary(
        string="Sub Total",
        currency_field="currency_id",
    )
    trans_type = fields.Char(string="Trans Type")
    unit_price = fields.Float(string="Unit Price")
    uom = fields.Many2one("uom.uom", string="UOM")


class XTempEstimatedGap(models.Model):
    _inherit = "temp_estimated"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    currency_id = fields.Many2one(comodel_name="res.currency", string="Currency")
    name = fields.Char(string="Name")
