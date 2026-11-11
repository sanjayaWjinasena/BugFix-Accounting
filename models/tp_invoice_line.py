"""tp_invoice_line — Transfer-Price (TP) invoice line.

Child of tp_invoice_header via inverse `tp_invoice_header_id`.
Each line captures a single charge / duty / tax entry against a
consignment, with either a Percentage or Fixed basis and an m2m into
account.tax for the applied tax rates.
"""

from odoo import fields, models


class XTpInvoiceLine(models.Model):
    _name = "tp_invoice_line"
    _description = "TP Invoice Line"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "sequence, id"
    _rec_name = "name"

    active = fields.Boolean(default=True)
    name = fields.Char()
    basis = fields.Selection(
        [
            ("Percentage", "Percentage"),
            ("Fixed Per Document", "Fixed Per Document"),
        ],
    )
    charge_group = fields.Selection(
        [
            ("None", "None"),
            ("Charges", "Charges"),
            ("Duty", "Duty"),
            ("Taxes", "Taxes"),
        ],
    )
    charge_name = fields.Char()
    consignment_charge_header_id = fields.Many2one(
        "consignment_charge_h",
        string="Consignment Charge Header Id",
    )
    consignment_id = fields.Many2one(
        "consignment_header",
        string="Consignment Id",
    )
    invoice_amount = fields.Float()
    original_amount = fields.Float()
    sequence = fields.Integer(default=10)
    tax_amount = fields.Float()
    taxes = fields.Many2many(
        "account.tax",
        relation="account_tax_x_tp_invoice_line_rel",
        column1="x_tp_invoice_line_id",
        column2="account_tax_id",
    )
    tp_invoice_header_id = fields.Many2one(
        "tp_invoice_header",
        string="TP Invoice Header Id",
        ondelete="cascade",
    )


class XTpInvoiceLineGap(models.Model):
    _inherit = "tp_invoice_line"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char()
