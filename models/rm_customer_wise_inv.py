from odoo import fields, models


class XRmCustomerWiseInv(models.Model):
    """Studio-ported custom model rm_customer_wise_inv."""

    _name = "rm_customer_wise_inv"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.activity.mixin"]
    _description = "RM Customer wise Invoices"

    active = fields.Boolean()
    name = fields.Char()
    customer = fields.Many2one("res.partner")
    sales_report_model_id = fields.Many2one(
        "sales_report_model", string="Sales Report Model Id"
    )
    sequence = fields.Integer()
    total_invoice_amount = fields.Float()


class XRmCustomerWiseInvGap(models.Model):
    _inherit = "rm_customer_wise_inv"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char()
