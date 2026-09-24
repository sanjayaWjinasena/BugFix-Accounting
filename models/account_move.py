# -*- coding: utf-8 -*-
import datetime

from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    x_studio_account_mandatory = fields.Boolean(string='Account Mandatory')
    x_studio_advance_acc_updated = fields.Boolean(string='Advance ACC Updated')
    x_studio_bank_guarantee_approved = fields.Boolean(
        string='Bank Guarantee Approved', readonly=True,
        related='x_studio_sale_id.x_studio_bank_guarantee_approved', store=True)
    x_studio_bank_guarantee_notification = fields.Boolean(
        string='Bank Guarantee Notification', readonly=True,
        compute='_compute_x_studio_bank_guarantee_notification', store=True)
    x_studio_bank_guarantee_validation = fields.Boolean(
        string='Bank Guarantee Validation', readonly=True,
        compute='_compute_x_studio_bank_guarantee_validation', store=True)
    x_studio_bg_sent = fields.Boolean(string='BG Sent')
    x_studio_consignment_no = fields.Many2one('x_consignment_header', string='Consignment No')
    # store=False: x_purchase_request_cas lives in BugFix-Purchase.
    # A stored M2O here would force BugFix-Accounting to dep on
    # BugFix-Purchase, creating the mutual cycle
    # Purchase -> Accounting -> Purchase. account_payment and
    # account_bank_statement_line versions are already store=False.
    x_studio_cre = fields.Many2one('x_purchase_request_cas', string='Created From CP No', store=False)
    x_studio_create_from_transfer_1 = fields.Many2one('stock.picking', string='Create From Transfer')
    x_studio_created_from_consignment = fields.Many2one('x_consignment_header', string='Created From Consignment')
    x_studio_created_from_consignment_1 = fields.Many2one('x_consignment_header', string='Created From Consignment')
    x_studio_created_from_npo_no = fields.Many2one('x_po_non_inventory', string='Created From NPO No')
    x_studio_created_from_project = fields.Boolean(string='Created From Project')
    x_studio_created_from_project_no = fields.Many2one('project.project', string='Created From Project No')
    x_studio_created_from_transfer = fields.Many2one('stock.picking', string='Created From Transfer')
    x_studio_created_from_vendor_bill = fields.Many2one('account.move', string='Created From Vendor Bill')
    x_studio_created_from_vendor_bill_1 = fields.Many2one('account.move', string='Created From Vendor Bill')
    x_studio_credit_limit_approved = fields.Boolean(
        string='Credit Limit Approved', readonly=True,
        related='x_studio_sale_id.x_studio_credit_limit_approved', store=True)
    x_studio_credit_limit_validation = fields.Boolean(
        string='Credit Limit Validation', readonly=True,
        compute='_compute_x_studio_credit_limit_validation', store=True)
    x_studio_credit_note_approved = fields.Boolean(string='Credit Note Approved')
    x_studio_credit_note_request_sent = fields.Boolean(string='Credit Note Request Sent')
    x_studio_currency_rate = fields.Float(string='Currency Rate')
    x_studio_currency_rate_updated = fields.Boolean(string='Currency Rate Updated')
    x_studio_custom_clearance_no = fields.Char(
        string='Custom Clearance No', readonly=True,
        related='x_studio_consignment_no.x_studio_custom_clearance_no', store=True)
    x_studio_journal_type = fields.Selection([('Bill', 'Bill'), ('Payment', 'Payment'), ('Settlement', 'Settlement')], string='Journal Type')
    x_studio_lc_no = fields.Many2one('x_lc_header', string='LC No')
    # store=False: purchase.order.x_studio_lc is a BugFix-Purchase-added
    # field, and BugFix-Purchase loads AFTER BugFix-Accounting. Setting
    # store=True would trigger _auto_init resolution of the downstream
    # field at Accounting-load time and crash the registry.
    x_studio_lc_test1 = fields.Boolean(
        string='LC - test1', readonly=True,
        related='purchase_id.x_studio_lc', store=False)
    x_studio_order_payment_method = fields.Selection(
        [('Cash', 'Cash'), ('Credit', 'Credit')],
        string='Order Payment Method', readonly=True,
        related='x_studio_sale_id.x_studio_order_payment_method', store=True)
    x_studio_over_bank_guarantee = fields.Boolean(
        string='Over Bank Guarantee', readonly=True,
        related='x_studio_sale_id.x_studio_over_bank_guarantee', store=True)
    x_studio_project_no = fields.Many2one('project.project', string='Project No')
    x_studio_project_no_bill = fields.Many2one('project.project', string='Project No Bill')
    x_studio_project_no_issue = fields.Many2one('project.project', string='Project No Issue')
    x_studio_project_no_settle = fields.Many2one('project.project', string='Project No Settle')
    x_studio_purchase_id = fields.Many2one('purchase.order', string='Purchase Order')
    # store=False: same reason as x_studio_lc_test1 above -
    # x_studio_pr_type on purchase.order is BugFix-Purchase-owned.
    x_studio_purchase_type = fields.Selection(
        [('Local', 'Local'), ('Import', 'Import')],
        string='PR Type', readonly=True,
        related='x_studio_purchase_id.x_studio_pr_type', store=False)
    x_studio_report_type_s_cust_aging = fields.Many2one('x_sales_report_type', string='Report Type (S - Cust Aging)')
    x_studio_rug_acc_updated = fields.Boolean(string='RUG Account Updated')
    x_studio_rug_confirmed = fields.Boolean(
        string='RUG Confirmed', readonly=True,
        related='x_studio_sale_id.x_studio_rug_confirmed', store=True)
    x_studio_rug_rejected = fields.Boolean(
        string='RUG Rejected', readonly=True,
        related='x_studio_sale_id.x_studio_rug_rejected', store=True)
    x_studio_sale_id = fields.Many2one('sale.order', string='Sale_Id')
    x_studio_supplier_invoice_number = fields.Char(string="XXX Supplier's Invoice Number (Bill Reference)")
    x_studio_test_type = fields.Selection([('One', 'One'), ('Two', 'Two')], string='Test Type')
    x_studio_tp_id = fields.Many2one('x_tp_invoice_header', string='Created From TP Invoice')
    x_studio_type = fields.Selection([('General', 'General'), ('Advance Payment', 'Advance Payment')], string='Type')
    x_studio_update_consignment = fields.Boolean(string='Update Consignment')
    x_studio_valid_lines = fields.Boolean(
        string='Valid Lines', readonly=True, store=False,
        compute='_compute_x_studio_valid_lines')
    x_x_studio_created_from_vendor_bill_1__account_move_count = fields.Integer(
        string='Created From Vendor Bill count', store=False,
        compute='_compute_vendor_bill_1_count')
    x_x_studio_created_from_vendor_bill__account_move_count = fields.Integer(
        string='Created From Vendor Bill count', store=False,
        compute='_compute_vendor_bill_count')

    # ------------------------------------------------------------------
    # Computed fields (ported from CDB Studio compute code)
    # ------------------------------------------------------------------
    # Note: CDB's depends clauses reference only 'partner_id, amount_total'
    # for the guarantee/notification computes even though the code reads
    # customer_group / mandatory_bank_guarantee / expiry_date /
    # bank_guarantee_amount. Preserved verbatim - the compute won't
    # invalidate on those deeper changes but that's CDB behavior.

    @api.depends('partner_id', 'amount_total', 'x_studio_bank_guarantee_approved',
                 'move_type')
    def _compute_x_studio_bank_guarantee_notification(self):
        today = datetime.date.today()
        for record in self:
            notification = False
            if not record.x_studio_bank_guarantee_approved:
                p = record.partner_id
                if p and (p.customer_rank or 0) > 0 and record.move_type == 'out_invoice':
                    cg = getattr(p, 'x_studio_customer_group', False)
                    group_type = getattr(cg, 'x_studio_group_type', None) if cg else None
                    if group_type and group_type != 'General':
                        mandatory = getattr(p, 'x_studio_mandatory_bank_guarantee', False)
                        expiry = getattr(p, 'x_studio_expiry_date', None)
                        bg_amount = getattr(p, 'x_studio_bank_guarantee_amount', 0) or 0
                        exposure = (p.credit or 0) + (record.amount_total or 0)
                        expired = expiry and expiry < today
                        if not mandatory:
                            if expired:
                                notification = True
                            elif bg_amount < exposure:
                                notification = True
                        # else (mandatory=True): notification stays False
            record.x_studio_bank_guarantee_notification = notification

    @api.depends('partner_id', 'amount_total', 'x_studio_bank_guarantee_approved',
                 'move_type')
    def _compute_x_studio_bank_guarantee_validation(self):
        today = datetime.date.today()
        for record in self:
            validation = False
            if not record.x_studio_bank_guarantee_approved:
                p = record.partner_id
                if p and (p.customer_rank or 0) > 0 and record.move_type == 'out_invoice':
                    cg = getattr(p, 'x_studio_customer_group', False)
                    group_type = getattr(cg, 'x_studio_group_type', None) if cg else None
                    if group_type and group_type != 'General':
                        mandatory = getattr(p, 'x_studio_mandatory_bank_guarantee', False)
                        expiry = getattr(p, 'x_studio_expiry_date', None)
                        bg_amount = getattr(p, 'x_studio_bank_guarantee_amount', 0) or 0
                        exposure = (p.credit or 0) + (record.amount_total or 0)
                        expired = expiry and expiry < today
                        if mandatory:
                            if expired:
                                validation = True
                            elif bg_amount < exposure:
                                validation = True
                        # else (mandatory=False): validation stays False
            record.x_studio_bank_guarantee_validation = validation

    @api.depends('partner_id', 'partner_id.credit', 'partner_id.credit_limit',
                 'amount_total', 'x_studio_order_payment_method',
                 'x_studio_credit_limit_approved')
    def _compute_x_studio_credit_limit_validation(self):
        for record in self:
            valid = False
            if not record.x_studio_credit_limit_approved:
                p = record.partner_id
                if p and record.x_studio_order_payment_method == 'Credit':
                    valid = ((p.credit or 0) + (record.amount_total or 0)) > (p.credit_limit or 0)
            record.x_studio_credit_limit_validation = valid

    @api.depends('invoice_line_ids', 'invoice_line_ids.price_unit',
                 'invoice_line_ids.display_type')
    def _compute_x_studio_valid_lines(self):
        for rec in self:
            has_zero_price = False
            count = 0
            for line in rec.invoice_line_ids:
                count += 1
                if not line.display_type and line.price_unit == 0:
                    has_zero_price = True
            # If no lines, mark valid (matches CDB code path).
            rec.x_studio_valid_lines = has_zero_price if count > 0 else True

    def _compute_vendor_bill_count(self):
        # CDB compute uses read_group. Port as batched search_count.
        # store=False so runs per-read.
        for rec in self:
            rec.x_x_studio_created_from_vendor_bill__account_move_count = self.env[
                'account.move'].search_count([('x_studio_created_from_vendor_bill', '=', rec.id)])

    def _compute_vendor_bill_1_count(self):
        for rec in self:
            rec.x_x_studio_created_from_vendor_bill_1__account_move_count = self.env[
                'account.move'].search_count([('x_studio_created_from_vendor_bill_1', '=', rec.id)])
