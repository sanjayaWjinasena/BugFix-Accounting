# -*- coding: utf-8 -*-
"""Sentinel declaration for x_sales_report_model so cross-references resolve."""
from odoo import fields, models


class XSalesReportModel(models.Model):
    _name = 'x_sales_report_model'
    _description = 'X Sales Report Model'

    _inherit = ['mail.thread', 'mail.activity.mixin']
    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_actual_gp_ = fields.Float(string='Actual GP')
    x_studio_actual_line_ids = fields.One2many('x_rm_gross_margin_actu', 'x_studio_sales_report_model_id', string='Actual Line Ids')
    x_studio_actuals = fields.Boolean(string='Actuals')
    x_studio_as_on_date = fields.Date(string='As on Date')
    x_studio_as_on_date_1 = fields.Date(string='From Date')
    x_studio_as_on_date_2 = fields.Date(string='To Date')
    x_studio_auto_generated = fields.Boolean(string='Auto Generated')
    x_studio_comparison_line_ids = fields.One2many('x_rm_gross_margin_comp', 'x_studio_sales_report_model_id', string='Comparison Line Ids')
    x_studio_contingency_ = fields.Float(string='Contingency %')
    x_studio_created_date = fields.Date(string='Created Date')
    x_studio_created_from_project_update = fields.Many2one('project.update', string='Created From Project Update')
    x_studio_customer = fields.Many2many('res.partner', 'x_sales_report_model_x_studio_customer_rel', 'host_id', 'target_id', string='Customer')
    x_studio_daily_sales_report_id = fields.One2many('x_rm_daily_sales_repor', 'x_studio_sales_report_model_id', string='Daily Sales Report Id 1')
    x_studio_daily_sales_report_id_1 = fields.One2many('x_rm_daily_s1', 'x_studio_sales_report_model_id', string='Daily Sales Report Id 2')
    x_studio_daily_sales_report_id_2 = fields.One2many('x_rm_daily_s2', 'x_studio_sales_report_model_id', string='Daily Sales Report Id 3')
    x_studio_daily_sales_report_id_3 = fields.One2many('x_rm_daily_s3', 'x_studio_sales_report_model_id', string='Daily Sales Report Id 4')
    x_studio_date_updated = fields.Boolean(string='Date Updated')
    x_studio_distributor_addition = fields.Float(string='Distributor Addition %')
    x_studio_estimated_gp_ = fields.Float(string='Estimated GP')
    x_studio_estimated_line_ids = fields.One2many('x_rm_gross_margin_esti', 'x_studio_sales_report_model_id', string='Estimated Line Ids')
    x_studio_factory_oh = fields.Float(string='Factory OH')
    x_studio_factory_oh_labour = fields.Float(string='Factory OH (Labour)')
    x_studio_financial_progress = fields.Float(string='Financial Progress')
    x_studio_from_date = fields.Date(string='From Date')
    x_studio_idling_rate = fields.Float(string='Idling Rate %')
    x_studio_invoice_details_line_ids = fields.One2many('x_rm_gross_margin_invo', 'x_studio_sales_report_model_id', string='Invoice Details Line Ids')
    x_studio_journal_item_ids = fields.One2many(
        'account.move.line',
        related='x_studio_report_type.x_studio_journal_items_id',
        string='Journal Item Ids',
        readonly=True,
    )
    x_studio_management_purpose = fields.Boolean(string='Management Purpose')
    x_studio_month_end_entry_updated = fields.Boolean(string='Month End Entry Updated')
    x_studio_none_moving_item_ids = fields.One2many('x_rm_none_moving', 'x_studio_sales_report_model_id', string='None Moving Item IDs')
    x_studio_oh_absorbed_2_factory = fields.Float(string='OH Absorbed 2 (Factory)')
    x_studio_oh_absorbed_2_other = fields.Float(string='OH Absorbed 2 (Other)')
    x_studio_oh_absorbed_2_sales = fields.Float(string='OH Absorbed 2 (Sales)')
    x_studio_oh_absorbed_factory = fields.Float(string='OH Absorbed (Factory)')
    x_studio_oh_absorbed_other = fields.Float(string='OH Absorbed (Other)')
    x_studio_oh_absorbed_sales = fields.Float(string='OH Absorbed (Sales)')
    x_studio_one2many_field_1Aq0X = fields.One2many('x_rm_production_varian', 'x_studio_sales_report_model_id', string='New One2many')
    x_studio_one2many_field_1rlRW = fields.One2many('x_rm_production_orders', 'x_studio_sales_report_model_id', string='New One2many')
    x_studio_one2many_field_6rdac = fields.One2many('x_rm_sales_prod_purch', 'x_studio_sales_report_model_id', string='New One2many')
    x_studio_one2many_field_jTZq4 = fields.One2many('x_rm_sales_order_line', 'x_studio_sales_report_model_id', string='Sales Order Lines')
    x_studio_one2many_field_yeTsx = fields.One2many('x_rm_prod_summary_spli', 'x_studio_sales_report_model_id', string='New One2many')
    x_studio_other_oh = fields.Float(string='Other OH')
    x_studio_profit_mark_up_ = fields.Float(string='Profit Mark Up %')
    x_studio_project_no = fields.Many2one('project.project', string='Project No')
    # TODO: x_studio_pump_price_costing_ids = fields.One2many('x_pump_price_costing', <inverse>, string='Pump Price Costing Ids')
    x_studio_related_field_DqBBB = fields.One2many(
        'sale.order.line',
        related='x_studio_report_type.x_studio_sales_lines_id',
        string='New Related Field',
        readonly=True,
    )
    # TODO: x_studio_related_field_NsCKm = fields.One2many('stock.move.line', <inverse>, string='New Related Field')
    # TODO: x_studio_related_field_PaCjA = fields.One2many('stock.move', <inverse>, string='New Related Field')
    # TODO: x_studio_related_field_XCKXu = fields.One2many('stock.move.line', <inverse>, string='New Related Field')
    # TODO: x_studio_related_field_bCtVj = fields.One2many('stock.move.line', <inverse>, string='New Related Field')
    x_studio_related_field_n589a = fields.One2many(
        'account.move.line',
        related='x_studio_report_type.x_studio_journal_items_id',
        string='New Related Field',
        readonly=True,
    )
    x_studio_related_field_nfrkz = fields.One2many(
        'account.move',
        related='x_studio_report_type.x_studio_journal_entry_id',
        string='New Related Field',
        readonly=True,
    )
    # TODO: x_studio_related_field_oeTJK = fields.One2many('mrp.production', <inverse>, string='New Related Field')
    x_studio_report_code = fields.Selection([], string='Report Code')
    x_studio_report_type = fields.Many2one('x_sales_report_type', string='Report Type')
    x_studio_sales_centre = fields.Many2many('crm.team', 'x_sales_report_model_x_studio_sales_centre_rel', 'host_id', 'target_id', string='Sales Centre')
    x_studio_sales_oh = fields.Float(string='Sales OH')
    x_studio_sales_report_model_id_4 = fields.One2many('x_rm_customer_wise_inv', 'x_studio_sales_report_model_id', string='Sales Report Model Id')
    x_studio_sales_report_model_id_5 = fields.One2many('x_rm_cust_invoice_s1', 'x_studio_sales_report_model_id', string='Sales Report Model Id')
    x_studio_selection_field_Fbw0x = fields.Selection([], string='Status')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_sscl = fields.Float(string='SSCL %')
