# -*- coding: utf-8 -*-
from odoo import fields, models


class XRmCustomerWiseInv(models.Model):
    """Studio-ported custom model x_rm_customer_wise_inv."""
    _name = 'x_rm_customer_wise_inv'
    _description = 'Rm Customer Wise Inv'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_customer = fields.Many2one('res.partner', string='Customer')
    x_studio_sales_report_model_id = fields.Many2one('x_sales_report_model', string='Sales Report Model Id')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_total_invoice_amount = fields.Float(string='Total Invoice Amount')
