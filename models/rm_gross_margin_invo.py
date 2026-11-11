"""rm_gross_margin_invo — Gross-margin invoice reporting row.

Per-invoice line under a gross-margin report showing invoice date,
amount, invoice status char, and both payment/state selections.

status shadows account.move.state's selection; payment_status
shadows account.move.payment_state. Selection tuples ported verbatim
from Clear-DB so any Studio filter / kanban decoration referring to
the string codes keeps working.
"""

from odoo import fields, models


class XRmGrossMarginInvo(models.Model):
    _name = "rm_gross_margin_invo"
    _description = "RM Gross Margin - Invoice Details"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "sequence, id"
    _rec_name = "name"

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(string="Name")
    amount = fields.Float(string="Amount")
    group_title = fields.Char(string="          ")
    header_reference = fields.Char(string="Header Reference")
    accounting_invoice_date = fields.Date(string="Invoice Date")
    invoice_no = fields.Many2one("account.move", string="Invoice No")
    invoice_status = fields.Char(string="Invoice Status")
    payment_status = fields.Selection(
        [
            ("not_paid", "Not Paid"),
            ("in_payment", "In Payment"),
            ("paid", "Paid"),
            ("partial", "Partially Paid"),
            ("reversed", "Reversed"),
            ("invoicing_legacy", "Invoicing App Legacy"),
        ],
        string="Payment Status",
    )
    sales_report_model_id = fields.Many2one(
        "sales_report_model",
        string="Sales Report Model Id",
        ondelete="cascade",
    )
    sequence = fields.Integer(string="Sequence", default=10)
    status = fields.Selection(
        [
            ("draft", "Draft"),
            ("posted", "Posted"),
            ("cancel", "Cancel"),
        ],
        string="Invoice Status",
    )


class XRmGrossMarginInvoGap(models.Model):
    _inherit = "rm_gross_margin_invo"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
