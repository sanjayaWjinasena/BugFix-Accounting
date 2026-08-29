# -*- coding: utf-8 -*-
"""x_rm_production_varian — Production-variance reporting row.

Compares BOM planned vs actual for a single production step:
BOM item, item number, estimated qty, actual production qty,
consumption qty, unit cost, total cost, variance.

Two product references (`x_studio_description` = the finished-good
product, `x_studio_description_1` = the BOM component product) —
Studio's original naming preserved verbatim.
"""
from odoo import fields, models


class XRmProductionVarian(models.Model):
    _name = 'x_rm_production_varian'
    _description = 'Production Variance Reporting Row'
    _order = 'x_studio_sequence, id'
    _rec_name = 'x_name'

    x_active = fields.Boolean(string='Active', default=True)
    x_name = fields.Char(string='Name')
    x_studio_avg_cost = fields.Float(string='Avg. Cost')
    x_studio_bom_item = fields.Char(
        string='BOM Item',
        related='x_studio_description_1.default_code',
        readonly=True,
    )
    x_studio_bom_qty = fields.Float(string='BOM Qty')
    x_studio_cons_qty = fields.Float(string='Cons. Qty')
    x_studio_description = fields.Many2one(
        'product.product', string='Description',
    )
    x_studio_description_1 = fields.Many2one(
        'product.product', string='Description',
    )
    x_studio_esti_qty = fields.Float(string='Esti. Qty')
    x_studio_header_reference = fields.Char(string='Header Reference')
    x_studio_item_number = fields.Char(
        string='Item Number',
        related='x_studio_description.default_code',
        readonly=True,
    )
    x_studio_prod_qty = fields.Float(string='Prod. Qty')
    x_studio_production_id = fields.Many2one(
        'mrp.production', string='Production Id',
    )
    x_studio_sales_report_model_id = fields.Many2one(
        'x_sales_report_model', string='Sales Report Model Id',
    )
    x_studio_sequence = fields.Integer(string='Sequence', default=10)
    x_studio_total_cost = fields.Float(string='Total Cost')
    x_studio_unit = fields.Many2one(
        'uom.uom',
        string='Unit',
        related='x_studio_description.uom_id',
        store=False,
        readonly=True,
    )
    x_studio_variance = fields.Float(string='Variance')
