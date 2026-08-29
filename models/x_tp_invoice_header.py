# -*- coding: utf-8 -*-
"""x_tp_invoice_header — Transfer-Price (TP) invoice header.

Vendor bill created from an import consignment. Each header carries
one or more x_tp_invoice_line rows (Percentage / Fixed charge groups
across Charges / Duty / Taxes) whose amounts roll up into monetary
totals + tax subtotal.

v0.0.16 (chunk 3) filled the TODO one2many + populated selections +
ported the four SUM computes and the account_move smart-button
counter compute — all verbatim from Clear-DB.
"""
from odoo import api, fields, models


class XTpInvoiceHeader(models.Model):
    _name = 'x_tp_invoice_header'
    _description = 'TP Invoice Header'
    _order = 'x_studio_sequence, id'
    _rec_name = 'x_name'

    x_active = fields.Boolean(string='Active', default=True)
    x_currency_id = fields.Many2one('res.currency', string='Currency')
    x_name = fields.Char(string='Invoice Reference')
    x_studio_con_no = fields.Many2one(
        'x_consignment_header', string='Created From Consignment No',
    )
    x_studio_currency_id = fields.Many2one('res.currency', string='Currency')
    x_studio_invoice_date = fields.Date(
        string="Supplier's Invoice Date (Bill Date)",
    )
    x_studio_invoice_no = fields.Char(
        string="Supplier's Invoice No (Bill Reference)",
    )
    x_studio_name = fields.Char(
        string='Name',
        related='x_studio_vendor.name',
        readonly=True,
    )
    x_studio_pipeline_status_bar = fields.Selection(
        [('Draft', 'Draft'), ('Posted', 'Posted')],
        string='Pipeline status bar',
    )
    x_studio_sequence = fields.Integer(string='Sequence', default=10)
    x_studio_status = fields.Selection(
        [('Draft', 'Draft'), ('Posted', 'Posted')],
        string='Status',
    )
    x_studio_vendor = fields.Many2one('res.partner', string='Vendor')
    x_studio_tp_lines = fields.One2many(
        'x_tp_invoice_line',
        'x_studio_tp_invoice_header_id',
        string='TP Lines',
    )

    # ---- Non-stored monetary totals (ported verbatim from Studio) ----

    x_studio_total_invoice_amount = fields.Monetary(
        string='Untaxed Amount',
        currency_field='x_currency_id',
        compute='_compute_x_studio_total_invoice_amount',
        store=False,
        readonly=True,
    )
    x_studio_taxes_1 = fields.Monetary(
        string='Taxes',
        currency_field='x_currency_id',
        compute='_compute_x_studio_taxes_1',
        store=False,
        readonly=True,
    )
    x_studio_total_1 = fields.Monetary(
        string='Total',
        currency_field='x_currency_id',
        compute='_compute_x_studio_total_1',
        store=False,
        readonly=True,
    )
    x_studio_total_original_invoice_amount = fields.Float(
        string='Total Original Invoice Amount',
        compute='_compute_x_studio_total_original_invoice_amount',
        store=False,
        readonly=True,
    )
    x_x_studio_tp_id__account_move_count = fields.Integer(
        string='Created From TP Invoice count',
        compute='_compute_x_x_studio_tp_id__account_move_count',
        store=False,
    )

    @api.depends(
        'x_studio_tp_lines',
        'x_studio_tp_lines.x_studio_invoice_amount',
    )
    def _compute_x_studio_total_invoice_amount(self):
        for rec in self:
            rec.x_studio_total_invoice_amount = sum(
                line.x_studio_invoice_amount
                for line in rec.x_studio_tp_lines
            )

    @api.depends(
        'x_studio_tp_lines',
        'x_studio_tp_lines.x_studio_taxes',
        'x_studio_tp_lines.x_studio_invoice_amount',
    )
    def _compute_x_studio_taxes_1(self):
        for rec in self:
            rec.x_studio_taxes_1 = sum(
                line.x_studio_tax_amount
                for line in rec.x_studio_tp_lines
            )

    @api.depends(
        'x_studio_total_invoice_amount',
        'x_studio_taxes_1',
    )
    def _compute_x_studio_total_1(self):
        for rec in self:
            rec.x_studio_total_1 = (
                rec.x_studio_total_invoice_amount + rec.x_studio_taxes_1
            )

    @api.depends(
        'x_studio_tp_lines',
        'x_studio_tp_lines.x_studio_original_amount',
    )
    def _compute_x_studio_total_original_invoice_amount(self):
        for rec in self:
            rec.x_studio_total_original_invoice_amount = sum(
                line.x_studio_original_amount
                for line in rec.x_studio_tp_lines
            )

    def _compute_x_x_studio_tp_id__account_move_count(self):
        """Count of account.move rows whose x_studio_tp_id points at
        this header. Ported from Studio's read_group snippet. Guarded
        so absence of `x_studio_tp_id` on account.move (fresh install
        without BugFix-Accounting's account.move Studio extensions
        yet) doesn't crash the compute — falls back to 0.
        """
        AccountMove = self.env['account.move']
        if 'x_studio_tp_id' not in AccountMove._fields:
            for rec in self:
                rec.x_x_studio_tp_id__account_move_count = 0
            return
        results = AccountMove.read_group(
            [('x_studio_tp_id', 'in', self.ids)],
            ['x_studio_tp_id'],
            ['x_studio_tp_id'],
        )
        counts = {
            r['x_studio_tp_id'][0]: r['x_studio_tp_id_count']
            for r in results if r.get('x_studio_tp_id')
        }
        for rec in self:
            rec.x_x_studio_tp_id__account_move_count = counts.get(rec.id, 0)
