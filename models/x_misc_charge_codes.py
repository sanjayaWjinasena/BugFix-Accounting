# -*- coding: utf-8 -*-
"""Sentinel declaration for x_misc_charge_codes so cross-references resolve."""
from odoo import fields, models


class XMiscChargeCodes(models.Model):
    _name = 'x_misc_charge_codes'
    _description = 'X Misc Charge Codes'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Misc. Charge Code')
    x_studio_charge_group = fields.Selection([], string='Charge Group')
    x_studio_charges_line_id = fields.Many2one('x_trf_charges', string='Charges Line Id')
    x_studio_company_id = fields.Many2one('res.company', string='Company')
    x_studio_credit_acc_type = fields.Selection([], string='Credit Acc. Type')
    x_studio_credit_account = fields.Many2one('account.account', string='Credit Account')
    x_studio_debit_acc_type = fields.Selection([], string='Cost Load Type')
    x_studio_debit_account = fields.Many2one('account.account', string='Debit Account')
    x_studio_description = fields.Char(string='Description')
    x_studio_duties_line_id = fields.Many2one('x_trf_duty', string='Duties Line Id')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_system_entry = fields.Boolean(string='System Entry')
    x_studio_taxes_line_id = fields.Many2one('x_trf_taxes', string='Taxes Line Id')
