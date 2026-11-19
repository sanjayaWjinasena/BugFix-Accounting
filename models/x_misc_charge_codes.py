# -*- coding: utf-8 -*-
"""Sentinel declaration for x_misc_charge_codes so cross-references resolve.

NOTE (v0.0.141): the three link Many2ones to x_trf_charges / x_trf_duty /
x_trf_taxes were MOVED to BugFix-Purchase (models/x_misc_charge_codes.py,
v0.1.0.176). Those comodels are owned by BugFix-Purchase, which is
downstream of this module; declaring them here made them `_unknown` for
the whole upgrade-mode registry build and crashed Jinasena_All cascades
on Jinasena_MasterData_Purchase/data/link/x_misc_charge_codes.csv
(relation "_unknown" does not exist). Do NOT re-add them here.
"""
from odoo import fields, models


class XMiscChargeCodes(models.Model):
    _name = 'x_misc_charge_codes'
    _rec_name = 'x_name'  # Clear-DB Studio model: records are named by x_name
    _description = 'Misc Charge Codes'

    _inherit = ['mail.thread', 'mail.activity.mixin']
    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Misc. Charge Code')
    x_studio_charge_group = fields.Selection([('None', 'None'), ('Charges', 'Charges'), ('Duty', 'Duty'), ('Taxes', 'Taxes')], string='Charge Group')
    x_studio_company_id = fields.Many2one('res.company', string='Company')
    x_studio_credit_acc_type = fields.Selection([('Item', 'Item'), ('G/L Account', 'G/L Account')], string='Credit Acc. Type')
    x_studio_credit_account = fields.Many2one('account.account', string='Credit Account')
    x_studio_debit_acc_type = fields.Selection([('Item', 'Item'), ('G/L Account', 'G/L Account')], string='Cost Load Type')
    x_studio_debit_account = fields.Many2one('account.account', string='Debit Account')
    x_studio_description = fields.Char(string='Description')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_system_entry = fields.Boolean(string='System Entry')
