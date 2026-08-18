# -*- coding: utf-8 -*-
from odoo import fields, models


class XRmCustInvoiceS1(models.Model):
    """Studio-ported custom model x_rm_cust_invoice_s1."""
    _name = 'x_rm_cust_invoice_s1'
    _description = 'Rm Cust Invoice S1'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_invoice_date = fields.Date(string='Invoice Date')
    x_studio_number = fields.Char(string='Number')
    x_studio_partner = fields.Many2one('res.partner', string='Partner')
    x_studio_product_id = fields.Many2one('product.product', string='Product')
    x_studio_quantity = fields.Float(string='Quantity')
    x_studio_sales_centre = fields.Many2one('crm.team', string='Sales Centre')
    x_studio_sales_report_model_id = fields.Many2one('x_sales_report_model', string='Customer Invoice Details')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_value = fields.Float(string='Value')
