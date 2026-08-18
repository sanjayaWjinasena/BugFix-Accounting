# -*- coding: utf-8 -*-
from odoo import fields, models


class XCustomCurrencyRate(models.Model):
    """Studio-ported custom model x_custom_currency_rate."""
    _name = 'x_custom_currency_rate'
    _description = 'Custom Currency Rate'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_company_id = fields.Many2one('res.company', string='Company')
    x_studio_custom_currency_id = fields.Many2one('x_custom_currency', string='Custom Currency Id')
    x_studio_end_date = fields.Date(string='End Date')
    x_studio_rate = fields.Float(string='Rate')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_start_date = fields.Date(string='Start Date')
