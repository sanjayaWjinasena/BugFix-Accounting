"""rm_sales_order_line — Sales-order-line reporting row.

Snapshot of a sale.order.line (product, quantity, unit price,
discount, net value) plus derived customer group / invoice /
address for the daily sales report family.

customer_group targets a model owned by studio_usermodel_migration;
that module is already in BugFix-Sales's dep chain but NOT in
BugFix-Accounting's — the m2o will fail to resolve on fresh install
if the target model isn't registered. See the manifest change in
this commit for the added dep.
"""

from odoo import fields, models


class XRmSalesOrderLine(models.Model):
    _name = "rm_sales_order_line"
    _description = "RM Sales Order Line"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "sequence, id"
    _rec_name = "name"

    active = fields.Boolean(default=True)
    name = fields.Char()
    customer_acc = fields.Many2one("res.partner")
    customer_group = fields.Many2one(
        "customer_group",
    )
    date = fields.Date()
    disc_ = fields.Float(string="Disc (%)")
    disc_amount = fields.Float(string="Disc. Amount")
    inv_address = fields.Char(string="Inv. Address")
    invoice = fields.Many2one("account.move")
    accounting_name = fields.Char(string="Name")
    net_value = fields.Float()
    product_1 = fields.Many2one("product.product", string="Product")
    product_category = fields.Many2one(
        "product.category",
    )
    quantity = fields.Float()
    sales_order = fields.Many2one("sale.order")
    sales_report_model_id = fields.Many2one(
        "sales_report_model",
        string="Sales Report Model Id",
    )
    sequence = fields.Integer(default=10)
    total_base_price = fields.Float()
    unit_price = fields.Float()


class XRmSalesOrderLineGap(models.Model):
    _inherit = "rm_sales_order_line"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char()
