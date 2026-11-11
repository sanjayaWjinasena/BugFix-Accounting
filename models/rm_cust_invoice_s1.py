from odoo import fields, models


class XRmCustInvoiceS1(models.Model):
    """Studio-ported custom model rm_cust_invoice_s1."""

    _name = "rm_cust_invoice_s1"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.activity.mixin"]
    _description = "RM Cust Invoice S1"

    active = fields.Boolean()
    name = fields.Char()
    accounting_invoice_date = fields.Date(string="Invoice Date")
    number = fields.Char()
    partner = fields.Many2one("res.partner")
    product_id = fields.Many2one("product.product")
    quantity = fields.Float()
    sales_centre = fields.Many2one("crm.team")
    sales_report_model_id = fields.Many2one(
        "sales_report_model", string="Customer Invoice Details"
    )
    sequence = fields.Integer()
    value = fields.Float()


class XRmCustInvoiceS1Gap(models.Model):
    _inherit = "rm_cust_invoice_s1"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char()
