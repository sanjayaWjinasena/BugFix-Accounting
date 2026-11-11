from odoo import fields, models


class XRmCustInvoiceS1(models.Model):
    """Studio-ported custom model rm_cust_invoice_s1."""

    _name = "rm_cust_invoice_s1"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.activity.mixin"]
    _description = "RM Cust Invoice S1"

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
    accounting_invoice_date = fields.Date(string="Invoice Date")
    number = fields.Char(string="Number")
    partner = fields.Many2one("res.partner", string="Partner")
    product_id = fields.Many2one("product.product", string="Product")
    quantity = fields.Float(string="Quantity")
    sales_centre = fields.Many2one("crm.team", string="Sales Centre")
    sales_report_model_id = fields.Many2one(
        "sales_report_model", string="Customer Invoice Details"
    )
    sequence = fields.Integer(string="Sequence")
    value = fields.Float(string="Value")


class XRmCustInvoiceS1Gap(models.Model):
    _inherit = "rm_cust_invoice_s1"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
