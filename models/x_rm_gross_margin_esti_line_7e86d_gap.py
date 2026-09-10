# -*- coding: utf-8 -*-
from odoo import models, fields

class XRmGrossMarginEstiLine7e86dGap(models.Model):
    _inherit = 'x_rm_gross_margin_esti_line_7e86d'

    x_name = fields.Char(string='Description', required=True)
    x_rm_gross_margin_esti_id = fields.Many2one(comodel_name='x_rm_gross_margin_esti', string='X Rm Gross Margin Esti')
