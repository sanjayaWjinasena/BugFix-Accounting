# -*- coding: utf-8 -*-
from odoo import models, fields

class XRmProdSummarySpliGap(models.Model):
    _inherit = 'x_rm_prod_summary_spli'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
