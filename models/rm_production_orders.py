"""rm_production_orders — Production-order reporting row.

Per-MO row capturing product code, start/end, estimated and started
quantities, good quantity, warehouse location, and the MO status
(draft/confirmed/progress/to_close/done/cancelled — note Studio's
verbatim typo 'canccel' preserved).
"""

from odoo import fields, models


class XRmProductionOrders(models.Model):
    _name = "rm_production_orders"
    _description = "RM Production Orders"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "sequence, id"
    _rec_name = "name"

    active = fields.Boolean(default=True)
    name = fields.Char()
    description = fields.Char()
    accounting_end = fields.Datetime(string="End")
    estimated = fields.Float()
    good_qty = fields.Float()
    header_reference = fields.Char()
    product_code = fields.Many2one(
        "product.product",
    )
    production_id = fields.Many2one(
        "mrp.production",
        string="Production Id",
    )
    sales_report_model_id = fields.Many2one(
        "sales_report_model",
        string="Sales Report Model Id",
    )
    sequence = fields.Integer(default=10)
    start = fields.Datetime()
    started = fields.Float()
    status = fields.Selection(
        [
            ("draft", "Draft"),
            ("confirmed", "Confirmed"),
            ("progress", "In Progress"),
            ("to_close", "To Close"),
            ("done", "Done"),
            # Studio-verbatim typo 'canccel' preserved.
            ("canccel", "Cancelled"),
        ],
    )
    warehouse = fields.Many2one("stock.location")


class XRmProductionOrdersGap(models.Model):
    _inherit = "rm_production_orders"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char()
