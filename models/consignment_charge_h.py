"""Sentinel declaration for consignment_charge_h so cross-references resolve."""

from odoo import fields, models

# NOTE (v0.0.143): the Many2one(s) structure_details_line_ids /
# structure_master_id were MOVED to BugFix-Purchase v0.1.0.178.
# Their comodel is owned by a DOWNSTREAM module; declared here they were
# `_unknown` for the whole upgrade-mode registry build (see BugFix-Purchase
# models/upstream_link_fields.py). Do NOT re-add them here.


class XConsignmentChargeH(models.Model):
    _name = "consignment_charge_h"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "Consignment Charge Header"

    _inherit = ["mail.thread", "mail.activity.mixin"]
    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
    allocate_header_charges = fields.Boolean(string="Allocate Header Charges")
    amount = fields.Float(string="Amount")
    basis = fields.Selection(
        [("Percentage", "Percentage"), ("Fixed Per Document", "Fixed Per Document")],
        string="Basis",
    )
    charge_group = fields.Selection(
        [
            ("None", "None"),
            ("Charges", "Charges"),
            ("Duty", "Duty"),
            ("Taxes", "Taxes"),
        ],
        string="Charge Group",
    )
    charge_name = fields.Char(string="Charge Name")
    accounting_company_id = fields.Many2one("res.company", string="Company")
    consignment_id = fields.Many2one(
        "consignment_header", string="Consignment Id"
    )
    formula = fields.Char(string="Formula")
    ledger_post = fields.Boolean(string="Ledger Post")
    sequence = fields.Integer(string="Sequence")
    structure_no = fields.Integer(string="Structure No")
    tax_appicable = fields.Boolean(string="Tax Applicable")
    tax_appicable2 = fields.Boolean(string="Tax Applicable2")
    tp_processed = fields.Boolean(string="TP Processed")


class XConsignmentChargeHGap(models.Model):
    _inherit = "consignment_charge_h"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
