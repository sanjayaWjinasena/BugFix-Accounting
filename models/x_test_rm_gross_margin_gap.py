from odoo import fields, models


class XTestRmGrossMarginGap(models.Model):
    _inherit = "x_test_rm_gross_margin"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Description", required=True)
