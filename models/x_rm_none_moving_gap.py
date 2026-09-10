# -*- coding: utf-8 -*-
from odoo import models, fields

class XRmNoneMovingGap(models.Model):
    _inherit = 'x_rm_none_moving'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
