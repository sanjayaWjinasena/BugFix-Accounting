from odoo import fields, models


class XCustomCurrencyRate(models.Model):
    """Studio-ported custom model custom_currency_rate."""

    _name = "custom_currency_rate"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.activity.mixin"]
    _description = "Custom Currency Rate"

    active = fields.Boolean()
    name = fields.Char()
    accounting_company_id = fields.Many2one("res.company", string="Company")
    custom_currency_id = fields.Many2one(
        "custom_currency", string="Custom Currency Id", ondelete="restrict"
    )
    end_date = fields.Date()
    rate = fields.Float()
    sequence = fields.Integer()
    start_date = fields.Date()


class XCustomCurrencyRateGap(models.Model):
    _inherit = "custom_currency_rate"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char()
