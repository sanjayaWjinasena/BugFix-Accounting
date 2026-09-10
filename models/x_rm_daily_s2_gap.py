# -*- coding: utf-8 -*-
from odoo import models, fields

class XRmDailyS2Gap(models.Model):
    _inherit = 'x_rm_daily_s2'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
