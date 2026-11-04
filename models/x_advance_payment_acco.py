from odoo import fields, models


class XAdvancePaymentAcco(models.Model):
    """Studio-ported custom model x_advance_payment_acco."""

    _name = "x_advance_payment_acco"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.activity.mixin"]
    _description = "Advance Payment Account"

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
    x_studio_advance_account_project = fields.Many2one(
        "account.account", string="Advance Account (Project)"
    )
    x_studio_advance_payment_account_purchases = fields.Many2one(
        "account.account", string="Account"
    )
    x_studio_advance_payment_account_purchases_1 = fields.Many2one(
        "account.account", string="Advance Payment Account (Purchases)"
    )
    x_studio_advance_payment_account_sales = fields.Many2one(
        "account.account", string="Advance Payment Account (Sales)"
    )
    sequence = fields.Integer(string="Sequence")


class XAdvancePaymentAccoGap(models.Model):
    _inherit = "x_advance_payment_acco"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
