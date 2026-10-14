from odoo import fields, models


class XRmGrossMarginEstiLine7e86dGap(models.Model):
    _inherit = 'x_rm_gross_margin_esti_line_7e86d'
    _rec_name = 'x_name'  # Clear-DB Studio model: records are named by x_name

    x_name = fields.Char(string='Description', required=True)
    x_rm_gross_margin_esti_id = fields.Many2one(comodel_name='x_rm_gross_margin_esti')
