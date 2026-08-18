# -*- coding: utf-8 -*-
from odoo import fields, models


class XRmGrossMarginComp(models.Model):
    """Studio-ported custom model x_rm_gross_margin_comp."""
    _name = 'x_rm_gross_margin_comp'
    _description = 'Rm Gross Margin Comp'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_delivered_amount = fields.Float(string='Delivered Amount')
    x_studio_delivered_not_invoiced = fields.Float(string='Delivered not Invoiced')
    x_studio_estimated_amount = fields.Float(string='Estimated Amount')
    x_studio_header_reference = fields.Char(string='Header Reference')
    x_studio_invoiced_amount = fields.Float(string='Invoiced Amount')
    x_studio_many2one_field_7fcuw = fields.Many2one('product.product', string='Product')
    x_studio_sales_order = fields.Many2one('sale.order', string='Sales Order')
    x_studio_sales_report_model_id = fields.Many2one('x_sales_report_model', string='Sales Report Model Id')
    x_studio_sequence = fields.Integer(string='Sequence')
