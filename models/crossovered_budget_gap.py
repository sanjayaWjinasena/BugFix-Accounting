from odoo import fields, models


class CrossoveredBudgetGap(models.Model):
    _inherit = "crossovered.budget"

    x_currency_id = fields.Many2one(comodel_name="res.currency", string="Currency")
