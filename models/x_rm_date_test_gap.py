from odoo import fields, models


class XRmDateTestGap(models.Model):
    _inherit = "x_rm_date_test"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char()
