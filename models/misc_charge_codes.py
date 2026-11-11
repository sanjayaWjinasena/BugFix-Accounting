"""Sentinel declaration for misc_charge_codes so cross-references resolve.

NOTE (v0.0.141): the three link Many2ones to trf_charges / trf_duty /
trf_taxes were MOVED to BugFix-Purchase (models/misc_charge_codes.py,
v0.1.0.176). Those comodels are owned by BugFix-Purchase, which is
downstream of this module; declaring them here made them `_unknown` for
the whole upgrade-mode registry build and crashed Jinasena_All cascades
on Jinasena_MasterData_Purchase/data/link/misc_charge_codes.csv
(relation "_unknown" does not exist). Do NOT re-add them here.
"""

from odoo import fields, models


class XMiscChargeCodes(models.Model):
    _name = "misc_charge_codes"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "Misc Charge Codes"

    _inherit = ["mail.thread", "mail.activity.mixin"]
    active = fields.Boolean()
    name = fields.Char(string="Misc. Charge Code")
    charge_group = fields.Selection(
        [
            ("None", "None"),
            ("Charges", "Charges"),
            ("Duty", "Duty"),
            ("Taxes", "Taxes"),
        ],
    )
    accounting_company_id = fields.Many2one("res.company", string="Company")
    credit_acc_type = fields.Selection(
        [("Item", "Item"), ("G/L Account", "G/L Account")], string="Credit Acc. Type"
    )
    credit_account = fields.Many2one("account.account")
    debit_acc_type = fields.Selection(
        [("Item", "Item"), ("G/L Account", "G/L Account")], string="Cost Load Type"
    )
    debit_account = fields.Many2one("account.account")
    description = fields.Char()
    sequence = fields.Integer()
    system_entry = fields.Boolean()


class XMiscChargeCodesGap(models.Model):
    _inherit = "misc_charge_codes"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char(string="Misc. Charge Code")
