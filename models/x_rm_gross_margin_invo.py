# -*- coding: utf-8 -*-
"""x_rm_gross_margin_invo — Gross-margin invoice reporting row.

Per-invoice line under a gross-margin report showing invoice date,
amount, invoice status char, and both payment/state selections.

x_studio_status shadows account.move.state's selection; x_studio_payment_status
shadows account.move.payment_state. Selection tuples ported verbatim
from Clear-DB so any Studio filter / kanban decoration referring to
the string codes keeps working.
"""
from odoo import fields, models


class XRmGrossMarginInvo(models.Model):
    _name = 'x_rm_gross_margin_invo'
    _description = 'Gross Margin Invoice Reporting Row'
    _order = 'x_studio_sequence, id'
    _rec_name = 'x_name'

    x_active = fields.Boolean(string='Active', default=True)
    x_name = fields.Char(string='Name')
    x_studio_amount = fields.Float(string='Amount')
    x_studio_group_title = fields.Char(string='          ')
    x_studio_header_reference = fields.Char(string='Header Reference')
    x_studio_invoice_date = fields.Date(string='Invoice Date')
    x_studio_invoice_no = fields.Many2one('account.move', string='Invoice No')
    x_studio_invoice_status = fields.Char(string='Invoice Status')
    x_studio_payment_status = fields.Selection(
        [
            ('not_paid', 'Not Paid'),
            ('in_payment', 'In Payment'),
            ('paid', 'Paid'),
            ('partial', 'Partially Paid'),
            ('reversed', 'Reversed'),
            ('invoicing_legacy', 'Invoicing App Legacy'),
        ],
        string='Payment Status',
    )
    x_studio_sales_report_model_id = fields.Many2one(
        'x_sales_report_model', string='Sales Report Model Id',
    )
    x_studio_sequence = fields.Integer(string='Sequence', default=10)
    x_studio_status = fields.Selection(
        [
            ('draft', 'Draft'),
            ('posted', 'Posted'),
            ('cancel', 'Cancel'),
        ],
        string='Invoice Status',
    )
