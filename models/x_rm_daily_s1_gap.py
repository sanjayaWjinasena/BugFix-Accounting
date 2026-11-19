# -*- coding: utf-8 -*-
from odoo import models, fields

class XRmDailyS1Gap(models.Model):
    _inherit = 'x_rm_daily_s1'
    _rec_name = 'x_name'  # Clear-DB Studio model: records are named by x_name

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
