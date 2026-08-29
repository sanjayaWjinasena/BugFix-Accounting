# -*- coding: utf-8 -*-
"""Extension of x_sales_report_model (owned by studio_usermodel_migration
= 'Jinasena : Masterdata : User' as of v0.0.12). BugFix-Accounting
adds the 16 direct One2many fields whose inverse M2O targets live
here (x_rm_* models).

Cycle-safe: x_rm_* target models are declared in BugFix-Accounting.
This module depends on studio_usermodel_migration. Order at install:
1. studio_usermodel_migration loads with x_sales_report_model shell.
2. BugFix-Accounting loads with x_rm_* models FIRST (they have no
   O2Ms into report_model - only the reverse M2O).
3. This _inherit file adds the O2Ms; their inverses now exist.
"""
from odoo import fields, models


class XSalesReportModel(models.Model):
    _inherit = 'x_sales_report_model'

    x_studio_actual_line_ids = fields.One2many('x_rm_gross_margin_actu', 'x_studio_sales_report_model_id', string='Actual Line Ids')
    x_studio_comparison_line_ids = fields.One2many('x_rm_gross_margin_comp', 'x_studio_sales_report_model_id', string='Comparison Line Ids')
    x_studio_daily_sales_report_id = fields.One2many('x_rm_daily_sales_repor', 'x_studio_sales_report_model_id', string='Daily Sales Report Id 1')
    x_studio_daily_sales_report_id_1 = fields.One2many('x_rm_daily_s1', 'x_studio_sales_report_model_id', string='Daily Sales Report Id 2')
    x_studio_daily_sales_report_id_2 = fields.One2many('x_rm_daily_s2', 'x_studio_sales_report_model_id', string='Daily Sales Report Id 3')
    x_studio_daily_sales_report_id_3 = fields.One2many('x_rm_daily_s3', 'x_studio_sales_report_model_id', string='Daily Sales Report Id 4')
    x_studio_estimated_line_ids = fields.One2many('x_rm_gross_margin_esti', 'x_studio_sales_report_model_id', string='Estimated Line Ids')
    x_studio_invoice_details_line_ids = fields.One2many('x_rm_gross_margin_invo', 'x_studio_sales_report_model_id', string='Invoice Details Line Ids')
    x_studio_none_moving_item_ids = fields.One2many('x_rm_none_moving', 'x_studio_sales_report_model_id', string='None Moving Item IDs')
    x_studio_one2many_field_1Aq0X = fields.One2many('x_rm_production_varian', 'x_studio_sales_report_model_id', string='New One2many')
    x_studio_one2many_field_1rlRW = fields.One2many('x_rm_production_orders', 'x_studio_sales_report_model_id', string='New One2many')
    x_studio_one2many_field_6rdac = fields.One2many('x_rm_sales_prod_purch', 'x_studio_sales_report_model_id', string='New One2many')
    x_studio_one2many_field_jTZq4 = fields.One2many('x_rm_sales_order_line', 'x_studio_sales_report_model_id', string='Sales Order Lines')
    x_studio_one2many_field_yeTsx = fields.One2many('x_rm_prod_summary_spli', 'x_studio_sales_report_model_id', string='New One2many')
    x_studio_sales_report_model_id_4 = fields.One2many('x_rm_customer_wise_inv', 'x_studio_sales_report_model_id', string='Sales Report Model Id')
    x_studio_sales_report_model_id_5 = fields.One2many('x_rm_cust_invoice_s1', 'x_studio_sales_report_model_id', string='Sales Report Model Id')

    # x_studio_pump_price_costing_ids remains TODO - target model
    # x_pump_price_costing not ported anywhere yet.
