from odoo import fields, models


class XTestRmGrossMargin(models.Model):
    """Studio-ported custom model x_test_rm_gross_margin."""

    _name = "x_test_rm_gross_margin"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.activity.mixin"]
    _description = "Test - RM Gross Margin - Actuals"

    active = fields.Boolean()
    name = fields.Char(string="Description", required=True)
    sequence = fields.Integer()
