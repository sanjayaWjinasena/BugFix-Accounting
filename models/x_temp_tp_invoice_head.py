# -*- coding: utf-8 -*-
"""x_temp_tp_invoice_head — transient/staging header for TP invoices.

Used by the Studio-designed wizard flow to accumulate charge lines
before promoting them to a real x_tp_invoice_header. Field shape is
minimal — just the parent link to a consignment header, the vendor,
and a one2many of x_temp_tp_invoice_line rows.

v0.0.16 (chunk 3) filled the previously-TODO x_studio_charge_line
one2many with its inverse.
"""
from odoo import fields, models


class XTempTpInvoiceHead(models.Model):
    _name = 'x_temp_tp_invoice_head'
    _description = 'Temp TP Invoice Header'
    _order = 'x_studio_sequence, id'
    _rec_name = 'x_name'

    x_active = fields.Boolean(string='Active', default=True)
    x_name = fields.Char(string='Name')
    x_studio_charge_line = fields.One2many(
        'x_temp_tp_invoice_line',
        'x_studio_temp_tp_invoice_header_id',
        string='Charge Line',
    )
    x_studio_consignment_header_id = fields.Many2one(
        'x_consignment_header', string='Consignment Header Id',
    )
    x_studio_sequence = fields.Integer(string='Sequence', default=10)
    x_studio_supplier_id = fields.Many2one('res.partner', string='Vendor')
