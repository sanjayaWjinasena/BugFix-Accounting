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

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(string="Name")
    customer_acc = fields.Many2one("res.partner", string="Customer Acc")
    customer_group = fields.Many2one(
        "customer_group",
        string="Customer Group",
    )
    date = fields.Date(string="Date")
    disc_ = fields.Float(string="Disc (%)")
    disc_amount = fields.Float(string="Disc. Amount")
    inv_address = fields.Char(string="Inv. Address")
    invoice = fields.Many2one("account.move", string="Invoice")
    accounting_name = fields.Char(string="Name")
    net_value = fields.Float(string="Net Value")
    product_1 = fields.Many2one("product.product", string="Product")
    product_category = fields.Many2one(
        "product.category",
        string="Product Category",
    )
    quantity = fields.Float(string="Quantity")
    sales_order = fields.Many2one("sale.order", string="Sales Order")
    sales_report_model_id = fields.Many2one(
        "sales_report_model",
        string="Sales Report Model Id",
    )
    sequence = fields.Integer(string="Sequence", default=10)
    total_base_price = fields.Float(string="Total Base Price")
    unit_price = fields.Float(string="Unit Price")


class XRmSalesOrderLineGap(models.Model):
    _inherit = "rm_sales_order_line"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
