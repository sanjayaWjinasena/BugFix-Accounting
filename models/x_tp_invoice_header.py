# -*- coding: utf-8 -*-
"""Sentinel declaration for x_tp_invoice_header so cross-references resolve."""
from odoo import fields, models


class XTpInvoiceHeader(models.Model):
    _name = 'x_tp_invoice_header'
    _description = 'X Tp Invoice Header'

    x_active = fields.Boolean(string='Active')
    x_currency_id = fields.Many2one('res.currency', string='Currency')
    x_name = fields.Char(string='Invoice Reference')
    x_studio_con_no = fields.Many2one('x_consignment_header', string='Created From Consignment No')
    x_studio_currency_id = fields.Many2one('res.currency', string='Currency')
    x_studio_invoice_date = fields.Date(string="Supplier's Invoice Date (Bill Date)")
    x_studio_invoice_no = fields.Char(string="Supplier's Invoice No (Bill Reference)")
    x_studio_name = fields.Char(string='Name')
    x_studio_pipeline_status_bar = fields.Selection([], string='Pipeline status bar')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_status = fields.Selection([], string='Status')
    x_studio_taxes_1 = fields.Float(string='Taxes')  # was Monetary
    x_studio_total_1 = fields.Float(string='Total')  # was Monetary
    x_studio_total_invoice_amount = fields.Float(string='Untaxed Amount')  # was Monetary
    x_studio_total_original_invoice_amount = fields.Float(string='Total Original Invoice Amount')
    # TODO: x_studio_tp_lines = fields.One2many('x_tp_invoice_line', <inverse>, string='TP Lines')
    x_studio_vendor = fields.Many2one('res.partner', string='Vendor')
    x_x_studio_tp_id__account_move_count = fields.Integer(string='Created From TP Invoice count')
