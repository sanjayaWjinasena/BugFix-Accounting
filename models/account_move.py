# -*- coding: utf-8 -*-
from odoo import fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    x_studio_account_mandatory = fields.Boolean(string='Account Mandatory')
    x_studio_advance_acc_updated = fields.Boolean(string='Advance ACC Updated')
    x_studio_bank_guarantee_approved = fields.Boolean(string='Bank Guarantee Approved', readonly=True)
    x_studio_bank_guarantee_notification = fields.Boolean(string='Bank Guarantee Notification', readonly=True, store=False)
    x_studio_bank_guarantee_validation = fields.Boolean(string='Bank Guarantee Validation', readonly=True, store=False)
    x_studio_bg_sent = fields.Boolean(string='BG Sent')
    x_studio_consignment_no = fields.Many2one('x_consignment_header', string='Consignment No')
    x_studio_cre = fields.Many2one('x_purchase_request_cas', string='Created From CP No')
    x_studio_create_from_transfer_1 = fields.Many2one('stock.picking', string='Create From Transfer')
    x_studio_created_from_consignment = fields.Many2one('x_consignment_header', string='Created From Consignment')
    x_studio_created_from_consignment_1 = fields.Many2one('x_consignment_header', string='Created From Consignment')
    x_studio_created_from_npo_no = fields.Many2one('x_po_non_inventory', string='Created From NPO No')
    x_studio_created_from_project = fields.Boolean(string='Created From Project')
    x_studio_created_from_project_no = fields.Many2one('project.project', string='Created From Project No')
    x_studio_created_from_transfer = fields.Many2one('stock.picking', string='Created From Transfer')
    x_studio_created_from_vendor_bill = fields.Many2one('account.move', string='Created From Vendor Bill')
    x_studio_created_from_vendor_bill_1 = fields.Many2one('account.move', string='Created From Vendor Bill')
    x_studio_credit_limit_approved = fields.Boolean(string='Credit Limit Approved', readonly=True)
    x_studio_credit_limit_validation = fields.Boolean(string='Credit Limit Validation', readonly=True, store=False)
    x_studio_credit_note_approved = fields.Boolean(string='Credit Note Approved')
    x_studio_credit_note_request_sent = fields.Boolean(string='Credit Note Request Sent')
    x_studio_currency_rate = fields.Float(string='Currency Rate')
    x_studio_currency_rate_updated = fields.Boolean(string='Currency Rate Updated')
    x_studio_custom_clearance_no = fields.Char(string='Custom Clearance No', readonly=True)
    x_studio_journal_type = fields.Selection([], string='Journal Type')
    x_studio_lc_no = fields.Many2one('x_lc_header', string='LC No')
    x_studio_lc_test1 = fields.Boolean(string='LC - test1', readonly=True)
    x_studio_order_payment_method = fields.Selection([], string='Order Payment Method', readonly=True)
    x_studio_over_bank_guarantee = fields.Boolean(string='Over Bank Guarantee', readonly=True)
    x_studio_project_no = fields.Many2one('project.project', string='Project No')
    x_studio_project_no_bill = fields.Many2one('project.project', string='Project No Bill')
    x_studio_project_no_issue = fields.Many2one('project.project', string='Project No Issue')
    x_studio_project_no_settle = fields.Many2one('project.project', string='Project No Settle')
    x_studio_purchase_id = fields.Many2one('purchase.order', string='Purchase Order')
    x_studio_purchase_type = fields.Selection([], string='PR Type', readonly=True)
    # x_studio_report_type_s_cust_aging moved to
    # Jinasena_Masterdata_Reporting/models/account_move.py so it lives
    # in the same module as its O2M partner
    # x_sales_report_type.x_studio_journal_entry_id.
    x_studio_rug_acc_updated = fields.Boolean(string='RUG Account Updated')
    x_studio_rug_confirmed = fields.Boolean(string='RUG Confirmed', readonly=True)
    x_studio_rug_rejected = fields.Boolean(string='RUG Rejected', readonly=True)
    x_studio_sale_id = fields.Many2one('sale.order', string='Sale_Id')
    x_studio_supplier_invoice_number = fields.Char(string="XXX Supplier's Invoice Number (Bill Reference)")
    x_studio_test_type = fields.Selection([], string='Test Type')
    x_studio_tp_id = fields.Many2one('x_tp_invoice_header', string='Created From TP Invoice')
    x_studio_type = fields.Selection([], string='Type')
    x_studio_update_consignment = fields.Boolean(string='Update Consignment')
    x_studio_valid_lines = fields.Boolean(string='Valid Lines', readonly=True, store=False)
    x_x_studio_created_from_vendor_bill_1__account_move_count = fields.Integer(string='Created From Vendor Bill count', store=False)
    x_x_studio_created_from_vendor_bill__account_move_count = fields.Integer(string='Created From Vendor Bill count', store=False)
