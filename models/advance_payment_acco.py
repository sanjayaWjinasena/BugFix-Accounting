from odoo import fields, models


class XAdvancePaymentAcco(models.Model):
    """Studio-ported custom model advance_payment_acco."""

    _name = "advance_payment_acco"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.activity.mixin"]
    _description = "Advance Payment Account"

    active = fields.Boolean()
    name = fields.Char()
    advance_account_project = fields.Many2one(
        "account.account", string="Advance Account (Project)"
    )
    advance_payment_account_purchases = fields.Many2one(
        "account.account", string="Account"
    )
    advance_payment_account_purchases_1 = fields.Many2one(
        "account.account", string="Advance Payment Account (Purchases)"
    )
    advance_payment_account_sales = fields.Many2one(
        "account.account", string="Advance Payment Account (Sales)"
    )
    sequence = fields.Integer()


class XAdvancePaymentAccoGap(models.Model):
    _inherit = "advance_payment_acco"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char()
