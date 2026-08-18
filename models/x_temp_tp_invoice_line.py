# -*- coding: utf-8 -*-
from odoo import fields, models


class XTempTpInvoiceLine(models.Model):
    """Studio-ported custom model x_temp_tp_invoice_line."""
    _name = 'x_temp_tp_invoice_line'
    _description = 'Temp Tp Invoice Line'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_amount = fields.Float(string='Amount')
    x_studio_basis = fields.Selection([], string='Basis')
    x_studio_charge_group = fields.Selection([], string='Charge Group')
    x_studio_charge_name = fields.Char(string='Charge Name')
    x_studio_consignment_charge_header_id = fields.Many2one('x_consignment_charge_h', string='Consignment Charge Header Id')
    x_studio_consignment_id = fields.Many2one('x_consignment_header', string='Consignment Id')
    x_studio_select = fields.Boolean(string='Select')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_temp_tp_invoice_header_id = fields.Many2one('x_temp_tp_invoice_head', string='Temp TP Invoice Header Id')
