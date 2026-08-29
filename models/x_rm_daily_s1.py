# -*- coding: utf-8 -*-
"""x_rm_daily_s1 — Daily-sales reporting row, variant 1.

One of three near-identical daily-sales row models (s1/s2/s3) that
Studio uses to feed different pivots of the same daily-sales report
header (x_sales_report_model). Each row records a single invoice
line's contribution to a day's sales at a sales-centre for a
partner+product combo.

s1 and s2 have identical field shape; s3 diverges only in the
partner reference field name (`x_studio_many2one_field_CiZHF`
instead of `x_studio_partner`), likely a Studio-designer artefact
that we preserve verbatim.
"""
from odoo import fields, models


class XRmDailyS1(models.Model):
    _name = 'x_rm_daily_s1'
    _description = 'Daily Sales Report Row S1'
    _order = 'x_studio_sequence, id'
    _rec_name = 'x_name'

    x_active = fields.Boolean(string='Active', default=True)
    x_name = fields.Char(string='Name')
    x_studio_invoice_date = fields.Date(string='Invoice Date')
    x_studio_number = fields.Char(string='Number')
    x_studio_partner = fields.Many2one('res.partner', string='Partner')
    x_studio_product_id = fields.Many2one('product.product', string='Product')
    x_studio_quantity = fields.Float(string='Quantity')
    x_studio_sales_centre = fields.Many2one('crm.team', string='Sales Centre')
    x_studio_sales_report_model_id = fields.Many2one(
        'x_sales_report_model', string='Sales Report Model',
    )
    x_studio_sequence = fields.Integer(string='Sequence', default=10)
    x_studio_value = fields.Float(string='Value')
