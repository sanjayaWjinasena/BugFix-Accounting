# -*- coding: utf-8 -*-
"""x_rm_sales_order_line — Sales-order-line reporting row.

Snapshot of a sale.order.line (product, quantity, unit price,
discount, net value) plus derived customer group / invoice /
address for the daily sales report family.

x_customer_group targets a model owned by studio_usermodel_migration;
that module is already in BugFix-Sales's dep chain but NOT in
BugFix-Accounting's — the m2o will fail to resolve on fresh install
if the target model isn't registered. See the manifest change in
this commit for the added dep.
"""
from odoo import fields, models


class XRmSalesOrderLine(models.Model):
    _name = 'x_rm_sales_order_line'
    _description = 'Sales Order Line Reporting Row'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'x_studio_sequence, id'
    _rec_name = 'x_name'

    x_active = fields.Boolean(string='Active', default=True)
    x_name = fields.Char(string='Name')
    x_studio_customer_acc = fields.Many2one('res.partner', string='Customer Acc')
    x_studio_customer_group = fields.Many2one(
        'x_customer_group', string='Customer Group',
    )
    x_studio_date = fields.Date(string='Date')
    x_studio_disc_ = fields.Float(string='Disc (%)')
    x_studio_disc_amount = fields.Float(string='Disc. Amount')
    x_studio_inv_address = fields.Char(string='Inv. Address')
    x_studio_invoice = fields.Many2one('account.move', string='Invoice')
    x_studio_name = fields.Char(string='Name')
    x_studio_net_value = fields.Float(string='Net Value')
    x_studio_product_1 = fields.Many2one('product.product', string='Product')
    x_studio_product_category = fields.Many2one(
        'product.category', string='Product Category',
    )
    x_studio_quantity = fields.Float(string='Quantity')
    x_studio_sales_order = fields.Many2one('sale.order', string='Sales Order')
    x_studio_sales_report_model_id = fields.Many2one(
        'x_sales_report_model', string='Sales Report Model Id',
    )
    x_studio_sequence = fields.Integer(string='Sequence', default=10)
    x_studio_total_base_price = fields.Float(string='Total Base Price')
    x_studio_unit_price = fields.Float(string='Unit Price')
