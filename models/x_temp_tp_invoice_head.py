# -*- coding: utf-8 -*-
"""Sentinel declaration for x_temp_tp_invoice_head so cross-references resolve."""
from odoo import fields, models


class XTempTpInvoiceHead(models.Model):
    _name = 'x_temp_tp_invoice_head'
    _description = 'X Temp Tp Invoice Head'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    # TODO: x_studio_charge_line = fields.One2many('x_temp_tp_invoice_line', <inverse>, string='Charge Line')
    x_studio_consignment_header_id = fields.Many2one('x_consignment_header', string='Consignment Header Id')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_supplier_id = fields.Many2one('res.partner', string='Vendor')
