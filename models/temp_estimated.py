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

    active = fields.Boolean(default=True)
    currency_id = fields.Many2one("res.currency")
    name = fields.Char()

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
    )
    customer = fields.Many2one("res.partner")
    delivered_qty = fields.Float()
    description = fields.Char()
    product_id = fields.Many2one(
        "product.product",
        string="Product Id",
    )
    project_no = fields.Many2one(
        "project.project",
    )
    quantity = fields.Float()
    sales_order = fields.Many2one("sale.order")
    sales_order_line_id = fields.Many2one(
        "sale.order.line",
        string="Sales Order Line Id",
    )
    sequence = fields.Integer(default=10)
    sub_total = fields.Monetary(
        currency_field="currency_id",
    )
    trans_type = fields.Char()
    unit_price = fields.Float()
    uom = fields.Many2one("uom.uom", string="UOM")


class XTempEstimatedGap(models.Model):
    _inherit = "temp_estimated"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    currency_id = fields.Many2one(comodel_name="res.currency")
    name = fields.Char()
