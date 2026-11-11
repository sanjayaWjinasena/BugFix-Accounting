"""rm_production_varian — Production-variance reporting row.

Compares BOM planned vs actual for a single production step:
BOM item, item number, estimated qty, actual production qty,
consumption qty, unit cost, total cost, variance.

Two product references (`description` = the finished-good
product, `description_1` = the BOM component product) —
Studio's original naming preserved verbatim.
"""

from odoo import fields, models


class XRmProductionVarian(models.Model):
    _name = "rm_production_varian"
    _description = "RM Production Variance"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "sequence, id"
    _rec_name = "name"

    active = fields.Boolean(default=True)
    name = fields.Char()
    avg_cost = fields.Float(string="Avg. Cost")
    bom_item = fields.Char(
        string="BOM Item",
        related="description_1.default_code",
        readonly=True,
    )
    bom_qty = fields.Float(string="BOM Qty")
    cons_qty = fields.Float(string="Cons. Qty")
    description = fields.Many2one(
        "product.product",
    )
    description_1 = fields.Many2one(
        "product.product",
        string="Description",
    )
    esti_qty = fields.Float(string="Esti. Qty")
    header_reference = fields.Char()
    item_number = fields.Char(
        string="Item Number",
        related="description.default_code",
        readonly=True,
    )
    prod_qty = fields.Float(string="Prod. Qty")
    production_id = fields.Many2one(
        "mrp.production",
        string="Production Id",
    )
    sales_report_model_id = fields.Many2one(
        "sales_report_model",
        string="Sales Report Model Id",
    )
    sequence = fields.Integer(default=10)
    total_cost = fields.Float()
    unit = fields.Many2one(
        "uom.uom",
        string="Unit",
        related="description.uom_id",
        store=False,
        readonly=True,
    )
    variance = fields.Float()


class XRmProductionVarianGap(models.Model):
    _inherit = "rm_production_varian"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char()
