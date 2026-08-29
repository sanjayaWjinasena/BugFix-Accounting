# -*- coding: utf-8 -*-
"""x_tp_invoice_line — Transfer-Price (TP) invoice line.

Child of x_tp_invoice_header via inverse `x_studio_tp_invoice_header_id`.
Each line captures a single charge / duty / tax entry against a
consignment, with either a Percentage or Fixed basis and an m2m into
account.tax for the applied tax rates.
"""
from odoo import fields, models


class XTpInvoiceLine(models.Model):
    _name = 'x_tp_invoice_line'
    _description = 'TP Invoice Line'
    _order = 'x_studio_sequence, id'
    _rec_name = 'x_name'

    x_active = fields.Boolean(string='Active', default=True)
    x_name = fields.Char(string='Name')
    x_studio_basis = fields.Selection(
        [
            ('Percentage', 'Percentage'),
            ('Fixed Per Document', 'Fixed Per Document'),
        ],
        string='Basis',
    )
    x_studio_charge_group = fields.Selection(
        [
            ('None', 'None'),
            ('Charges', 'Charges'),
            ('Duty', 'Duty'),
            ('Taxes', 'Taxes'),
        ],
        string='Charge Group',
    )
    x_studio_charge_name = fields.Char(string='Charge Name')
    x_studio_consignment_charge_header_id = fields.Many2one(
        'x_consignment_charge_h', string='Consignment Charge Header Id',
    )
    x_studio_consignment_id = fields.Many2one(
        'x_consignment_header', string='Consignment Id',
    )
    x_studio_invoice_amount = fields.Float(string='Invoice Amount')
    x_studio_original_amount = fields.Float(string='Original Amount')
    x_studio_sequence = fields.Integer(string='Sequence', default=10)
    x_studio_tax_amount = fields.Float(string='Tax Amount')
    x_studio_taxes = fields.Many2many('account.tax', string='Taxes')
    x_studio_tp_invoice_header_id = fields.Many2one(
        'x_tp_invoice_header', string='TP Invoice Header Id',
    )
