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

    active = fields.Boolean(default=True)
    name = fields.Char()
    base_price = fields.Float()
    date = fields.Date()
    date_1 = fields.Date(string="Date")
    description = fields.Many2one(
        "product.product",
    )
    header_reference = fields.Char()
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
    production_qty = fields.Float()
    project_category = fields.Float(string="Project")
    purchase_qty = fields.Float()
    sales_order = fields.Float()
    sales_report_model_id = fields.Many2one(
        "sales_report_model",
        string="Sales Report Model Id",
    )
    sequence = fields.Integer(default=10)
    unit_cost = fields.Float()


class XRmSalesProdPurchGap(models.Model):
    _inherit = "rm_sales_prod_purch"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char()
