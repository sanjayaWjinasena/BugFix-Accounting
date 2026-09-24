# -*- coding: utf-8 -*-
"""Sentinel declaration for x_lc_header so cross-references resolve."""
from odoo import api, fields, models


class XLcHeader(models.Model):
    _name = 'x_lc_header'
    _inherit = ['mail.activity.mixin']
    _description = 'LC Header'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='LC Registration No')
    x_studio_additional_conditions = fields.Text(string='Additional Conditions (47A/B)')
    x_studio_available_with_by = fields.Char(string='Available with / By (41A)')
    x_studio_bank_charges = fields.Text(string='Bank Charges (71B)')
    x_studio_beneficiary = fields.Char(string='Beneficiary (59)')
    x_studio_company_id = fields.Many2one('res.company', string='Company')
    x_studio_confirmation_instructions = fields.Selection([('None', 'None'), ('A', 'A'), ('B', 'B'), ('C', 'C')], string='Confirmation Instructions (49)')
    x_studio_created_from_purchase_order = fields.Many2one('purchase.order', string='PO Number')
    x_studio_currency_id = fields.Many2one('res.currency', string='Currency')
    x_studio_date_of_expiry = fields.Date(string='Date of Expiry (31D)')
    x_studio_date_of_issue = fields.Date(string='Date of Issue (31C)')
    x_studio_date_of_receipt = fields.Date(string='Date of Receipt')
    x_studio_deferred_days = fields.Float(string='Deferred Days')
    x_studio_description_of_goods = fields.Char(string='Description of Goods and / or Services (45A)')
    x_studio_document_required = fields.Text(string='Document Required (46A/B)')
    x_studio_draft = fields.Selection([('At Sight', 'At Sight'), ('Deferred Payment', 'Deferred Payment')], string='Draft (42C)')
    x_studio_indent_no = fields.Char(string='Indent No')
    x_studio_instruction_remarks = fields.Text(string='Instruction / Remarks (78)')
    x_studio_issuing_bank = fields.Many2one('res.bank', string='Issuing Bank')
    x_studio_issuing_bank_reference_no_1 = fields.Char(string='Issuing Bank Reference No')
    x_studio_latest_shipment_date = fields.Date(string='Latest Shipment Date (44C)')
    x_studio_lc_amount = fields.Float(string='LC Amount (32B)')
    x_studio_lc_amount_lcy = fields.Float(
        string='LC Amount (LCY)',
        compute='_compute_x_studio_lc_amount_lcy', store=True, readonly=True)
    x_studio_lc_credit_sub_type = fields.Selection([('Non Transferable', 'Non Transferable'), ('Transferable', 'Transferable'), ('Revolving', 'Revolving')], string='Documentary Credit Sub Type (40A)')
    x_studio_lc_credit_type = fields.Selection([('Irrevocable', 'Irrevocable'), ('Revocable', 'Revocable')], string='Documentary Credit Type (40A)')
    x_studio_lc_no = fields.Char(string='Documentatry Credit Number (20)')
    x_studio_loading_on_board = fields.Char(string='Loading on Board (44A)')
    x_studio_paid_amount_lcy = fields.Float(string='Paid Amount (LCY)')
    x_studio_partial_shipment = fields.Selection([('Allowed', 'Allowed'), ('Not Allowed', 'Not Allowed')], string='Partial Shipment (43P)')
    x_studio_period_for_presentation = fields.Float(string='Period for Presentation (48)')
    x_studio_place_of_expiry = fields.Char(string='Place of Expiry (31D)')
    x_studio_revised_lc_amount = fields.Float(
        string='Revised Amount',
        compute='_compute_x_studio_revised_lc_amount', store=True, readonly=True)

    @api.depends('x_studio_currency_id', 'x_studio_currency_id.rate', 'x_studio_lc_amount')
    def _compute_x_studio_lc_amount_lcy(self):
        # Ported from CDB Studio compute. Original did a res.currency search
        # with a non-existent 'date' filter (schema-invalid); rewritten to
        # use the standard currency.rate field which is auto-updated per
        # company's currency conversion date.
        for rec in self:
            cur = rec.x_studio_currency_id
            if cur and cur.rate:
                rec.x_studio_lc_amount_lcy = round((rec.x_studio_lc_amount or 0) / cur.rate, 2)
            else:
                rec.x_studio_lc_amount_lcy = 0

    @api.depends('x_studio_lc_amount', 'x_studio_tolerance_type', 'x_studio_tolerance')
    def _compute_x_studio_revised_lc_amount(self):
        for record in self:
            amount = record.x_studio_lc_amount or 0
            tolerance = record.x_studio_tolerance or 0
            adjustment = amount * tolerance / 100
            if record.x_studio_tolerance_type == 'Plus':
                record.x_studio_revised_lc_amount = amount + adjustment
            elif record.x_studio_tolerance_type == 'Minus':
                record.x_studio_revised_lc_amount = amount - adjustment
            else:
                record.x_studio_revised_lc_amount = amount
    x_studio_selection_field_yo4qM = fields.Selection([('Draft', 'Draft'), ('Posted', 'Posted'), ('Amended', 'Amended'), ('Paid', 'Paid'), ('Cancelled', 'Cancelled')], string='Pipeline status bar')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_status = fields.Selection([('Draft', 'Draft'), ('Posted', 'Posted'), ('Paid', 'Paid'), ('Amended', 'Amended'), ('Cancelled', 'Cancelled')], string='Status')
    x_studio_tolerance = fields.Float(string='Tolerance (39A)')
    x_studio_tolerance_type = fields.Selection([('Plus', 'Plus'), ('Minus', 'Minus')], string='Tolerance Type')
    x_studio_transportation = fields.Char(string='Transportation (44B)')
    x_studio_transshipment = fields.Selection([('Allowed', 'Allowed'), ('Not Allowed', 'Not Allowed')], string='Transshipment (43T)')
    x_studio_vendor = fields.Many2one('res.partner', string='Vendor')
    x_studio_version_no = fields.Integer(string='Version No')
