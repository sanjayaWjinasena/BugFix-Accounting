from odoo import fields, models


class XJinasenaPaymasterConfig(models.Model):
    """Studio-ported custom model misc_jinasena_paymaster_config.

    NOTE: de-``x_``-ing this model to ``jinasena_paymaster_config`` would
    collide with bank-data's ``jinasena.paymaster.config`` -- Odoo derives
    the table name by swapping dots for underscores, so both models map to
    the table ``jinasena_paymaster_config``. bank-data owns the functional
    model (wizard, tests, hr.payslip / account.move.line integration); this
    is only the Clear-DB Studio pin. Hence the ``misc_`` prefix, same as
    x_product_product -> misc_product_product and
    x_res_config_settings -> misc_res_config_settings.
    """

    _name = "misc_jinasena_paymaster_config"
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
    _inherit = "misc_jinasena_paymaster_config"
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
