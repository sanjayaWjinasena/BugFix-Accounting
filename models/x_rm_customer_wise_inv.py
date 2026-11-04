from odoo import fields, models


class XRmCustomerWiseInv(models.Model):
    """Studio-ported custom model x_rm_customer_wise_inv."""

    _name = "x_rm_customer_wise_inv"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.activity.mixin"]
    _description = "RM Customer wise Invoices"

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
    x_studio_customer = fields.Many2one("res.partner", string="Customer")
    x_studio_sales_report_model_id = fields.Many2one(
        "x_sales_report_model", string="Sales Report Model Id"
    )
    sequence = fields.Integer(string="Sequence")
    x_studio_total_invoice_amount = fields.Float(string="Total Invoice Amount")


class XRmCustomerWiseInvGap(models.Model):
    _inherit = "x_rm_customer_wise_inv"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
