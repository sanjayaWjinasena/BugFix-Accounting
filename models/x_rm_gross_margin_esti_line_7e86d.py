# -*- coding: utf-8 -*-
"""x_rm_gross_margin_esti_line_7e86d — sub-line under a gross-margin
estimate row.

Studio auto-generated child model (the `_line_7e86d` suffix is
Studio's inline-list-nested-child-model naming convention). Kept
verbatim for parity — Clear-DB's parent form arch references this
model directly in the notebook page as an inline editable list.
"""
from odoo import fields, models


class XRmGrossMarginEstiLine(models.Model):
    _name = 'x_rm_gross_margin_esti_line_7e86d'
    _description = 'Gross Margin Estimate Sub-Line'
    _order = 'x_studio_sequence, id'
    _rec_name = 'x_name'

    x_name = fields.Char(string='Description', required=True)
    x_rm_gross_margin_esti_id = fields.Many2one(
        'x_rm_gross_margin_esti', string='X Rm Gross Margin Esti',
    )
    x_studio_sequence = fields.Integer(string='Sequence', default=10)
