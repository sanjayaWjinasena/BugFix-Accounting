from odoo import fields, models


class AccountAnalyticDistributionModel(models.Model):
    _inherit = "account.analytic.distribution.model"

    partner_mandatory = fields.Boolean(string="Partner Mandatory")
