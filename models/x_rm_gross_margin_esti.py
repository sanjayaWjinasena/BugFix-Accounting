# -*- coding: utf-8 -*-
"""x_rm_gross_margin_esti — Gross-margin ESTIMATE header row.

Per-category estimate row under a x_sales_report_model. Bundles a
transaction type (Item / Expense / Fee / Hour), estimated amount,
actual cost / balance cost, and a one2many into x_temp_estimated
for line-level breakdown.
"""
from odoo import fields, models


class XRmGrossMarginEsti(models.Model):
    _name = 'x_rm_gross_margin_esti'
    _description = 'Gross Margin Estimate Row'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'x_studio_sequence, id'
    _rec_name = 'x_name'

    x_active = fields.Boolean(string='Active', default=True)
    x_name = fields.Char(string='Name')
    x_studio_actual_cost = fields.Float(string='Delivered Amount')
    x_studio_balance_cost = fields.Float(string='Balance Amount')
    x_studio_category = fields.Char(string='Category')
    x_studio_estimated_amt = fields.Float(string='Estimated Amt.')
    x_studio_group_title = fields.Char(string='          ')
    x_studio_header_reference = fields.Char(string='Header Reference')
    x_studio_sales_order_line_ids = fields.One2many(
        'x_temp_estimated',
        'x_studio_estimated_line_ids',
        string='Sales Order Line Ids',
    )
    x_studio_sales_report_model_id = fields.Many2one(
        'x_sales_report_model', string='Sales Report Model Id',
    )
    x_studio_sequence = fields.Integer(string='Sequence', default=10)
    x_studio_total = fields.Boolean(string='Total')
    x_studio_transaction_type = fields.Selection(
        [
            ('Item', 'Item'),
            ('Expense', 'Expense'),
            ('Fee', 'Fee'),
            ('Hour', 'Hour'),
        ],
        string='Transaction Type',
    )
