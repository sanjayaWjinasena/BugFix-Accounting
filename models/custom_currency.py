from odoo import fields, models


class XCustomCurrency(models.Model):
    """Studio-ported custom model custom_currency."""

    _name = "custom_currency"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.activity.mixin"]
    _description = "Custom Currency"

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
    accounting_active = fields.Boolean(string="Active")
    accounting_company_id = fields.Many2one("res.company", string="Company")
    accounting_currency_id = fields.Many2one("res.currency", string="Currency")
    currency_unit = fields.Char(string="Currency Unit", readonly=True)
    current_rate = fields.Float(string="Current Rate", readonly=True)
    date = fields.Date(string="Date", readonly=True)
    iso_currency_code = fields.Char(string="ISO Currency Code", required=True)
    accounting_name = fields.Char(string="Name")
    sequence = fields.Integer(string="Sequence")
    symbol = fields.Char(string="Symbol", readonly=True)
    custom_currency_id__x_custom_currency_rate_count = fields.Integer(
        string="Custom Currency Id count", store=False
    )


class XCustomCurrencyGap(models.Model):
    _inherit = "custom_currency"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
