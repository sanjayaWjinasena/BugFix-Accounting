# -*- coding: utf-8 -*-
"""x_rm_daily_s3 — Daily-sales reporting row, variant 3.

Same shape as s1 / s2 EXCEPT the partner reference is named
`x_studio_many2one_field_CiZHF` (Studio-auto-generated identifier)
instead of the semantic name `x_studio_partner` that s1/s2 use.
Preserving the field name verbatim per feedback-clear-db-verbatim.
"""
from odoo import fields, models


class XRmDailyS3(models.Model):
    _name = 'x_rm_daily_s3'
    _description = 'Daily Sales Report Row S3'
    _order = 'x_studio_sequence, id'
    _rec_name = 'x_name'

    x_active = fields.Boolean(string='Active', default=True)
    x_name = fields.Char(string='Name')
    x_studio_invoice_date = fields.Date(string='Invoice Date')
    x_studio_number = fields.Char(string='Number')
    x_studio_many2one_field_CiZHF = fields.Many2one(
        'res.partner', string='Partner',
    )
    x_studio_product_id = fields.Many2one('product.product', string='Product')
    x_studio_quantity = fields.Float(string='Quantity')
    x_studio_sales_centre = fields.Many2one('crm.team', string='Sales Centre')
    x_studio_sales_report_model_id = fields.Many2one(
        'x_sales_report_model', string='Sales Report Model',
    )
    x_studio_sequence = fields.Integer(string='Sequence', default=10)
    x_studio_value = fields.Float(string='Value')
