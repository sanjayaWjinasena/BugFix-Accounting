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

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(string="Name")
    description = fields.Char(string="Description")
    accounting_end = fields.Datetime(string="End")
    estimated = fields.Float(string="Estimated")
    good_qty = fields.Float(string="Good Qty")
    header_reference = fields.Char(string="Header Reference")
    product_code = fields.Many2one(
        "product.product",
        string="Product Code",
    )
    production_id = fields.Many2one(
        "mrp.production",
        string="Production Id",
    )
    sales_report_model_id = fields.Many2one(
        "sales_report_model",
        string="Sales Report Model Id",
    )
    sequence = fields.Integer(string="Sequence", default=10)
    start = fields.Datetime(string="Start")
    started = fields.Float(string="Started")
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
        string="Status",
    )
    warehouse = fields.Many2one("stock.location", string="Warehouse")


class XRmProductionOrdersGap(models.Model):
    _inherit = "rm_production_orders"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
