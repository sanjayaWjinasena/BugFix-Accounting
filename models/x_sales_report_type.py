# -*- coding: utf-8 -*-
"""Sentinel declaration for x_sales_report_type so cross-references resolve."""
from odoo import fields, models


class XSalesReportType(models.Model):
    _name = 'x_sales_report_type'
    _description = 'X Sales Report Type'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Report Name')
    # TODO: x_studio_journal_entry_id = fields.One2many('account.move', <inverse>, string='Journal Entry Id')
    # TODO: x_studio_journal_items_id = fields.One2many('account.move.line', <inverse>, string='Journal Items Id')
    # TODO: x_studio_prod_summary_split_id = fields.One2many('stock.move.line', <inverse>, string='Prod. Summary Split Id')
    # TODO: x_studio_production_order_id = fields.One2many('mrp.production', <inverse>, string='Production Order Id')
    # TODO: x_studio_production_variance_id = fields.One2many('stock.move', <inverse>, string='Production Variance Id')
    x_studio_report_code = fields.Selection([], string='Report Code')
    # TODO: x_studio_sales_lines_id = fields.One2many('sale.order.line', <inverse>, string='Sales Lines Id')
    # TODO: x_studio_sales_prod_purch_id = fields.One2many('stock.move.line', <inverse>, string='Sales Prod. Purch. Id')
    x_studio_sequence = fields.Integer(string='Sequence')
    # TODO: x_studio_slow_moving_item_id = fields.One2many('stock.move.line', <inverse>, string='Slow Moving Item Id')
    # TODO: x_studio_test = fields.One2many('account.move.line', <inverse>, string='test')
