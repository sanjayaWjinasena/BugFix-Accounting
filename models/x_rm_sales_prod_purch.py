# -*- coding: utf-8 -*-
"""x_rm_sales_prod_purch — Sales vs production vs purchase reporting row.

Per-product summary of production quantity, purchase quantity,
sales-order quantity, base/unit costs and the derived project
category. Reads product type (consu / service / product) from
the linked product.product for filtering.
"""
from odoo import fields, models


class XRmSalesProdPurch(models.Model):
    _name = 'x_rm_sales_prod_purch'
    _description = 'Sales / Production / Purchase Reporting Row'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'x_studio_sequence, id'
    _rec_name = 'x_name'

    x_active = fields.Boolean(string='Active', default=True)
    x_name = fields.Char(string='Name')
    x_studio_base_price = fields.Float(string='Base Price')
    x_studio_date = fields.Date(string='Date')
    x_studio_date_1 = fields.Date(string='Date')
    x_studio_description = fields.Many2one(
        'product.product', string='Description',
    )
    x_studio_header_reference = fields.Char(string='Header Reference')
    x_studio_product_category = fields.Many2one(
        'product.category',
        string='Product Category',
        related='x_studio_description.categ_id',
        store=False,
        readonly=True,
    )
    x_studio_product_code = fields.Char(
        string='Product Code',
        related='x_studio_description.default_code',
        readonly=True,
    )
    x_studio_product_type = fields.Selection(
        [
            ('consu', 'Consumable'),
            ('service', 'Service'),
            ('product', 'Storable Product'),
        ],
        string='Product Type',
        related='x_studio_description.type',
        store=False,
        readonly=True,
    )
    x_studio_production_qty = fields.Float(string='Production Qty')
    x_studio_project_category = fields.Float(string='Project')
    x_studio_purchase_qty = fields.Float(string='Purchase Qty')
    x_studio_sales_order = fields.Float(string='Sales Order')
    x_studio_sales_report_model_id = fields.Many2one(
        'x_sales_report_model', string='Sales Report Model Id',
    )
    x_studio_sequence = fields.Integer(string='Sequence', default=10)
    x_studio_unit_cost = fields.Float(string='Unit Cost')
