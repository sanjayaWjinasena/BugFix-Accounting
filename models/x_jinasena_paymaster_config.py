# -*- coding: utf-8 -*-
from odoo import fields, models


class XJinasenaPaymasterConfig(models.Model):
    """Studio-ported custom model x_jinasena_paymaster_config."""
    _name = 'x_jinasena_paymaster_config'
    _description = 'Jinasena Paymaster Config'

    x_cr_dr_code = fields.Char(string='Cr/Dr Code (H)')
    x_currency_code = fields.Char(string='Currency Code (K)')
    x_filler = fields.Char(string='Filler (T)')
    x_name = fields.Char(string='Name')
    x_orig_account = fields.Char(string='Orig Account (N)')
    x_orig_bank_micr = fields.Char(string='Orig Bank MICR (L)')
    x_orig_branch = fields.Char(string='Orig Branch (M)')
    x_orig_name = fields.Char(string='Orig Name (O)')
    x_return_code = fields.Char(string='Return Code (G)')
    x_return_date = fields.Char(string='Return Date (I)')
    x_security_field = fields.Char(string='Security Field (S)')
    x_trn_code = fields.Char(string='TRN Code (F)')
