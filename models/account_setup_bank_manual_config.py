# -*- coding: utf-8 -*-
from odoo import fields, models


class AccountSetupBankManualConfig(models.Model):
    _inherit = 'account.setup.bank.manual.config'

    x_studio_bank_code = fields.Char(string='bank code', store=False)
    x_studio_bank_code_1 = fields.Char(string='Bank code', store=False)
    x_studio_branch_code = fields.Char(string='branch code', store=False)
    x_studio_branch_code_1 = fields.Char(string='Branch code', store=False)
    x_studio_char_field_445_1jk2c8gep = fields.Char(string='New Text', store=False)
    x_studio_char_field_8qe_1jk2c6sho = fields.Char(string='New Text', store=False)
    x_studio_char_field_yfp1a = fields.Char(string='New Text', store=False)
    x_studio_swift_code = fields.Char(string='SWIFT Code', store=False)
