# -*- coding: utf-8 -*-
"""x_rm_none_moving — None-moving stock reporting row.

Per-product line under a x_sales_report_model header, capturing
in-hand and issue quantities across up to 4 time buckets plus the
current qty / base price / value. Related fields expose the product's
category and default_code without denormalising the storage.
"""
from odoo import fields, models


class XRmNoneMoving(models.Model):
    _name = 'x_rm_none_moving'
    _description = 'None-Moving Stock Reporting Row'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'x_studio_sequence, id'
    _rec_name = 'x_name'

    x_active = fields.Boolean(string='Active', default=True)
    x_name = fields.Char(string='Name')
    x_studio_base_price = fields.Float(string='Base Price')
    x_studio_description = fields.Many2one(
        'product.product', string='Description',
    )
    x_studio_header_reference = fields.Char(string='Header Reference')
    x_studio_in_hand_1 = fields.Float(string='In Hand')
    x_studio_in_hand_2 = fields.Float(string='In Hand')
    x_studio_in_hand_3 = fields.Float(string='In Hand')
    x_studio_in_hand_4 = fields.Float(string='In Hand')
    x_studio_issue_1 = fields.Float(string='Issue')
    x_studio_issue_2 = fields.Float(string='Issue')
    x_studio_issue_3 = fields.Float(string='Issue')
    x_studio_issue_4 = fields.Float(string='Issue')
    x_studio_product_category = fields.Many2one(
        'product.category',
        string='Product Category',
        related='x_studio_description.categ_id',
        store=False,
        readonly=True,
    )
    x_studio_product_code_1 = fields.Char(
        string='Product Code',
        related='x_studio_description.default_code',
        readonly=True,
    )
    x_studio_qty = fields.Float(string='Qty')
    x_studio_sales_report_model_id = fields.Many2one(
        'x_sales_report_model', string='Sales Report Model Id',
    )
    x_studio_sequence = fields.Integer(string='Sequence', default=10)
    x_studio_value = fields.Float(string='Value')
