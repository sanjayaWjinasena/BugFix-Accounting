# -*- coding: utf-8 -*-
from odoo import fields, models


class XCustomCurrency(models.Model):
    """Studio-ported custom model x_custom_currency."""
    _name = 'x_custom_currency'
    _description = 'Custom Currency'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_active = fields.Boolean(string='Active')
    x_studio_company_id = fields.Many2one('res.company', string='Company')
    x_studio_currency_id = fields.Many2one('res.currency', string='Currency')
    x_studio_currency_unit = fields.Char(string='Currency Unit', readonly=True)
    x_studio_current_rate = fields.Float(string='Current Rate', readonly=True)
    x_studio_date = fields.Date(string='Date', readonly=True)
    x_studio_iso_currency_code = fields.Char(string='ISO Currency Code', required=True)
    x_studio_name = fields.Char(string='Name')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_symbol = fields.Char(string='Symbol', readonly=True)
    x_x_studio_custom_currency_id__x_custom_currency_rate_count = fields.Integer(string='Custom Currency Id count', store=False)
