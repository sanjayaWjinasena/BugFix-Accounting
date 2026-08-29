# -*- coding: utf-8 -*-
"""x_rm_gross_margin_actu — Gross-margin ACTUAL header row.

Actual counterpart to x_rm_gross_margin_esti. Same shape plus
budget-line linkage via x_temp_actual_budget.

v0.0.15 (chunk 2) filled in the two TODO one2many inverses that the
initial sentinel port left blank + populated the transaction_type_1
selection tuple.
"""
from odoo import fields, models


class XRmGrossMarginActu(models.Model):
    _name = 'x_rm_gross_margin_actu'
    _description = 'Gross Margin Actual Row'
    _order = 'x_studio_sequence, id'
    _rec_name = 'x_name'

    x_active = fields.Boolean(string='Active', default=True)
    x_name = fields.Char(string='Name')
    x_studio_budget_line = fields.Boolean(string='Budget Line')
    x_studio_budget_line_ids = fields.One2many(
        'x_temp_actual_budget',
        'x_studio_actual_line_ids',
        string='Budget Line Ids',
    )
    x_studio_cost_price = fields.Float(string='Delivered Amount')
    x_studio_estimated_total = fields.Float(string='Estimated Amount')
    x_studio_header_reference = fields.Char(string='Header Reference')
    x_studio_normal_line = fields.Boolean(string='Normal Line')
    x_studio_other_expenses = fields.Char(string='Other Expenses')
    x_studio_sales_order_line_ids = fields.One2many(
        'x_temp_estimated',
        'x_studio_actual_line_ids',
        string='Sales Order Line Ids',
    )
    x_studio_sales_report_model_id = fields.Many2one(
        'x_sales_report_model', string='Sales Report Model Id',
    )
    x_studio_sequence = fields.Integer(string='Sequence', default=10)
    x_studio_transaction_type_1 = fields.Selection(
        [
            ('Item', 'Item'),
            ('Expense', 'Expense'),
            ('Fee', 'Fee'),
            ('Hour', 'Hour'),
        ],
        string='Transaction Type',
    )
    x_studio_variance_est_act = fields.Float(string='Variance (Est - Act)')
