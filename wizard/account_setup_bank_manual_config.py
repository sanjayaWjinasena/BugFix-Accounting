from odoo import fields, models


class AccountSetupBankManualConfig(models.TransientModel):
    _inherit = "account.setup.bank.manual.config"

    bank_code = fields.Char(string="bank code", store=False)
    bank_code_1 = fields.Char(string="Bank code", store=False)
    branch_code = fields.Char(string="branch code", store=False)
    branch_code_1 = fields.Char(string="Branch code", store=False)
    char_field_445_1jk2c8gep = fields.Char(string="New Text", store=False)
    char_field_8qe_1jk2c6sho = fields.Char(string="New Text", store=False)
    char_field_yfp1a = fields.Char(string="New Text", store=False)
    swift_code = fields.Char(string="SWIFT Code", store=False)
