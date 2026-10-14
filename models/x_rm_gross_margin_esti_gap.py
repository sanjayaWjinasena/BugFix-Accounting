from odoo import fields, models


class XRmGrossMarginEstiGap(models.Model):
    _inherit = 'x_rm_gross_margin_esti'
    _rec_name = 'x_name'  # Clear-DB Studio model: records are named by x_name

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
