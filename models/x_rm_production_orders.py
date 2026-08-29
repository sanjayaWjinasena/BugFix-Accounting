# -*- coding: utf-8 -*-
"""x_rm_production_orders — Production-order reporting row.

Per-MO row capturing product code, start/end, estimated and started
quantities, good quantity, warehouse location, and the MO status
(draft/confirmed/progress/to_close/done/cancelled — note Studio's
verbatim typo 'canccel' preserved).
"""
from odoo import fields, models


class XRmProductionOrders(models.Model):
    _name = 'x_rm_production_orders'
    _description = 'Production Orders Reporting Row'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'x_studio_sequence, id'
    _rec_name = 'x_name'

    x_active = fields.Boolean(string='Active', default=True)
    x_name = fields.Char(string='Name')
    x_studio_description = fields.Char(string='Description')
    x_studio_end = fields.Datetime(string='End')
    x_studio_estimated = fields.Float(string='Estimated')
    x_studio_good_qty = fields.Float(string='Good Qty')
    x_studio_header_reference = fields.Char(string='Header Reference')
    x_studio_product_code = fields.Many2one(
        'product.product', string='Product Code',
    )
    x_studio_production_id = fields.Many2one(
        'mrp.production', string='Production Id',
    )
    x_studio_sales_report_model_id = fields.Many2one(
        'x_sales_report_model', string='Sales Report Model Id',
    )
    x_studio_sequence = fields.Integer(string='Sequence', default=10)
    x_studio_start = fields.Datetime(string='Start')
    x_studio_started = fields.Float(string='Started')
    x_studio_status = fields.Selection(
        [
            ('draft', 'Draft'),
            ('confirmed', 'Confirmed'),
            ('progress', 'In Progress'),
            ('to_close', 'To Close'),
            ('done', 'Done'),
            # Studio-verbatim typo 'canccel' preserved.
            ('canccel', 'Cancelled'),
        ],
        string='Status',
    )
    x_studio_warehouse = fields.Many2one('stock.location', string='Warehouse')
