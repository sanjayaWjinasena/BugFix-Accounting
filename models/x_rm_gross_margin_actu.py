# -*- coding: utf-8 -*-
"""Sentinel declaration for x_rm_gross_margin_actu so cross-references resolve."""
from odoo import fields, models


class XRmGrossMarginActu(models.Model):
    _name = 'x_rm_gross_margin_actu'
    _description = 'X Rm Gross Margin Actu'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_budget_line = fields.Boolean(string='Budget Line')
    # TODO: x_studio_budget_line_ids = fields.One2many('x_temp_actual_budget', <inverse>, string='Budget Line Ids')
    x_studio_cost_price = fields.Float(string='Delivered Amount')
    x_studio_estimated_total = fields.Float(string='Estimated Amount')
    x_studio_header_reference = fields.Char(string='Header Reference')
    x_studio_normal_line = fields.Boolean(string='Normal Line')
    x_studio_other_expenses = fields.Char(string='Other Expenses')
    # TODO: x_studio_sales_order_line_ids = fields.One2many('x_temp_estimated', <inverse>, string='Sales Order Line Ids')
    x_studio_sales_report_model_id = fields.Many2one('x_sales_report_model', string='Sales Report Model Id')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_transaction_type_1 = fields.Selection([], string='Transaction Type')
    x_studio_variance_est_act = fields.Float(string='Variance (Est - Act)')
