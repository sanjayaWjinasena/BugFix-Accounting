from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    charge_type = fields.Selection(
        [
            ("Charge", "Charge"),
            ("Duty", "Duty"),
            ("Tax", "Tax"),
        ],
        string="Charge Type",
    )
    non_billable = fields.Boolean(string="Non Billable")
