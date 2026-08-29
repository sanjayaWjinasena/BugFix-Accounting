# -*- coding: utf-8 -*-
"""x_rm_daily_sales_repor — Daily sales KPI reporting row.

Per-sales-centre row storing monthly targets, daily / month /
cumulative net invoice values, achievement percentages. All
plain floats — no computes; values are stamped at row-generation
time by the report seeding logic (external to this model).
"""
from odoo import fields, models


class XRmDailySalesRepor(models.Model):
    _name = 'x_rm_daily_sales_repor'
    _description = 'Daily Sales Report Row'
    _order = 'x_studio_sequence, id'
    _rec_name = 'x_name'

    x_active = fields.Boolean(string='Active', default=True)
    x_name = fields.Char(string='Name')
    x_studio_achieve_cumulative_ = fields.Float(string='Achieve Cumulative (%)')
    x_studio_achievement_ = fields.Float(string='Achievement (%)')
    x_studio_m_sales_target = fields.Float(string='M. Sales Target')
    x_studio_net_invoice_value_cumulative = fields.Float(
        string='Net Invoice Value - Cumulative',
    )
    x_studio_net_invoice_value_day = fields.Float(
        string='Net Invoice Value - Day',
    )
    x_studio_net_invoice_value_month = fields.Float(
        string='Net Invoice Value - Month',
    )
    x_studio_s_target_cumulative = fields.Float(string='S. Target - Cumulative ')
    x_studio_sales_centre = fields.Char(string='Sales Centre')
    x_studio_sales_report_model_id = fields.Many2one(
        'x_sales_report_model', string='Sales Report Model Id',
    )
    x_studio_sequence = fields.Integer(string='Sequence', default=10)
