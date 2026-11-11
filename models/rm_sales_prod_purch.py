"""rm_sales_prod_purch — Sales vs production vs purchase reporting row.

Per-product summary of production quantity, purchase quantity,
sales-order quantity, base/unit costs and the derived project
category. Reads product type (consu / service / product) from
the linked product.product for filtering.
"""

from odoo import fields, models


class XRmSalesProdPurch(models.Model):
    _name = "rm_sales_prod_purch"
    _description = "RM Sales Prod. Purch."
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "sequence, id"
    _rec_name = "name"

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(string="Name")
    base_price = fields.Float(string="Base Price")
    date = fields.Date(string="Date")
    date_1 = fields.Date(string="Date")
    description = fields.Many2one(
        "product.product",
        string="Description",
    )
    header_reference = fields.Char(string="Header Reference")
    product_category = fields.Many2one(
        "product.category",
        string="Product Category",
        related="description.categ_id",
        store=False,
        readonly=True,
    )
    product_code = fields.Char(
        string="Product Code",
        related="description.default_code",
        readonly=True,
    )
    product_type = fields.Selection(
        string="Product Type",
        related="description.type",
        store=False,
        readonly=True,
    )
    production_qty = fields.Float(string="Production Qty")
    project_category = fields.Float(string="Project")
    purchase_qty = fields.Float(string="Purchase Qty")
    sales_order = fields.Float(string="Sales Order")
    sales_report_model_id = fields.Many2one(
        "sales_report_model",
        string="Sales Report Model Id",
    )
    sequence = fields.Integer(string="Sequence", default=10)
    unit_cost = fields.Float(string="Unit Cost")


class XRmSalesProdPurchGap(models.Model):
    _inherit = "rm_sales_prod_purch"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
