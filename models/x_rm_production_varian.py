"""x_rm_production_varian — Production-variance reporting row.

Compares BOM planned vs actual for a single production step:
BOM item, item number, estimated qty, actual production qty,
consumption qty, unit cost, total cost, variance.

Two product references (`description` = the finished-good
product, `x_studio_description_1` = the BOM component product) —
Studio's original naming preserved verbatim.
"""

from odoo import fields, models


class XRmProductionVarian(models.Model):
    _name = "x_rm_production_varian"
    _description = "RM Production Variance"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "sequence, id"
    _rec_name = "name"

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(string="Name")
    x_studio_avg_cost = fields.Float(string="Avg. Cost")
    x_studio_bom_item = fields.Char(
        string="BOM Item",
        related="x_studio_description_1.default_code",
        readonly=True,
    )
    x_studio_bom_qty = fields.Float(string="BOM Qty")
    x_studio_cons_qty = fields.Float(string="Cons. Qty")
    description = fields.Many2one(
        "product.product",
        string="Description",
    )
    x_studio_description_1 = fields.Many2one(
        "product.product",
        string="Description",
    )
    x_studio_esti_qty = fields.Float(string="Esti. Qty")
    x_studio_header_reference = fields.Char(string="Header Reference")
    x_studio_item_number = fields.Char(
        string="Item Number",
        related="description.default_code",
        readonly=True,
    )
    x_studio_prod_qty = fields.Float(string="Prod. Qty")
    x_studio_production_id = fields.Many2one(
        "mrp.production",
        string="Production Id",
    )
    x_studio_sales_report_model_id = fields.Many2one(
        "x_sales_report_model",
        string="Sales Report Model Id",
    )
    sequence = fields.Integer(string="Sequence", default=10)
    x_studio_total_cost = fields.Float(string="Total Cost")
    x_studio_unit = fields.Many2one(
        "uom.uom",
        string="Unit",
        related="description.uom_id",
        store=False,
        readonly=True,
    )
    x_studio_variance = fields.Float(string="Variance")


class XRmProductionVarianGap(models.Model):
    _inherit = "x_rm_production_varian"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
