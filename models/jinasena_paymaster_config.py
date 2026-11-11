from odoo import fields, models


class XJinasenaPaymasterConfig(models.Model):
    """Studio-ported custom model jinasena_paymaster_config."""

    _name = "jinasena_paymaster_config"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "CBC Paymaster Config"

    cr_dr_code = fields.Char(string="Cr/Dr Code (H)")
    currency_code = fields.Char(string="Currency Code (K)")
    filler = fields.Char(string="Filler (T)")
    name = fields.Char()
    orig_account = fields.Char(string="Orig Account (N)")
    orig_bank_micr = fields.Char(string="Orig Bank MICR (L)")
    orig_branch = fields.Char(string="Orig Branch (M)")
    orig_name = fields.Char(string="Orig Name (O)")
    return_code = fields.Char(string="Return Code (G)")
    return_date = fields.Char(string="Return Date (I)")
    security_field = fields.Char(string="Security Field (S)")
    trn_code = fields.Char(string="TRN Code (F)")


class XJinasenaPaymasterConfigGap(models.Model):
    _inherit = "jinasena_paymaster_config"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    cr_dr_code = fields.Char(string="Cr/Dr Code (H)")
    currency_code = fields.Char(string="Currency Code (K)")
    filler = fields.Char(string="Filler (T)")
    name = fields.Char()
    orig_account = fields.Char(string="Orig Account (N)")
    orig_bank_micr = fields.Char(string="Orig Bank MICR (L)")
    orig_branch = fields.Char(string="Orig Branch (M)")
    orig_name = fields.Char(string="Orig Name (O)")
    return_code = fields.Char(string="Return Code (G)")
    return_date = fields.Char(string="Return Date (I)")
    security_field = fields.Char(string="Security Field (S)")
    trn_code = fields.Char(string="TRN Code (F)")
