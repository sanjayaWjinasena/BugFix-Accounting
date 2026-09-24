# -*- coding: utf-8 -*-
from odoo import api, fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    x_studio_aaa = fields.Char(string='AAA', readonly=True, store=False)
    x_studio_account_mandatory = fields.Boolean(string='Account Mandatory')
    x_studio_analytic_group = fields.Many2one('account.analytic.plan', string='Analytic Group')
    x_studio_beneficiary_id = fields.Char(string='Beneficiary ID', related='x_studio_contract_id.employee_id.identification_id', store=True, readonly=True)
    x_studio_beneficiary_name = fields.Char(string='Beneficiary Name', related='x_studio_contract_id.employee_id.name', store=True, readonly=True)
    x_studio_category = fields.Many2one('x_project_category', string='Category')
    x_studio_contract_id = fields.Many2one('hr.contract', string='Contract Id')
    x_studio_credit_limit = fields.Float(string='Credit Limit', related='partner_id.credit_limit', store=True, readonly=True)
    x_studio_credit_limit_2 = fields.Float(string='Credit Limit 2', readonly=True)
    x_studio_customer_group_type = fields.Selection([('General', 'General'), ('Distributor', 'Distributor'), ('Dealer', 'Dealer')], string='Customer Group Type', related='partner_id.x_studio_customer_group.x_studio_group_type', store=True, readonly=True)
    x_studio_employers_contribution = fields.Float(string="Employer's Contribution", compute='_compute_x_studio_employers_contribution', store=True, readonly=True)
    x_studio_epf_number = fields.Char(string='EPF Number', related='x_studio_contract_id.employee_id.x_studio_epf_no', store=True, readonly=True)
    x_studio_etf_number = fields.Char(string='ETF Number', related='x_studio_contract_id.employee_id.x_studio_etf_no', store=True, readonly=True)
    x_studio_initials = fields.Char(string='Initials', related='x_studio_contract_id.x_studio_initial', store=True, readonly=True)
    x_studio_invoice_date = fields.Date(string='Invoice Date', related='move_id.invoice_date', store=True, readonly=True)
    x_studio_journal = fields.Many2one('account.move', string='Journal', related='move_id', store=True, readonly=True)
    x_studio_journal_type = fields.Selection([('Bill', 'Bill'), ('Payment', 'Payment'), ('Settlement', 'Settlement')], string='Journal Type', related='move_id.x_studio_journal_type', store=True, readonly=True)
    x_studio_many2one_field_kiSUJ = fields.Many2one('x_sales_report_type', string='Sales Report Type')
    x_studio_members_contribution = fields.Float(string="Member's Contribution", compute='_compute_x_studio_members_contribution', store=True, readonly=True)
    x_studio_nic_number = fields.Char(string='NIC Number', related='x_studio_contract_id.employee_id.identification_id', store=True, readonly=True)
    x_studio_occupation_code = fields.Char(string='New Related Field', related='x_studio_contract_id.employee_id.x_studio_occupation_code', store=True, readonly=True)
    x_studio_partner = fields.Many2one('res.partner', string='Partner', related='move_id.partner_id', store=True, readonly=True)
    x_studio_payment_status = fields.Selection([('not_paid', 'Not Paid'), ('in_payment', 'In Payment'), ('paid', 'Paid'), ('partial', 'Partially Paid'), ('reversed', 'Reversed'), ('invoicing_legacy', 'Invoicing App Legacy')], string='Payment Status', related='move_id.payment_state', store=True, readonly=True)
    x_studio_pr_type = fields.Selection([('Local', 'Local'), ('Import', 'Import')], string='PR Type', related='move_id.x_studio_purchase_type', store=True, readonly=True)
    x_studio_product_category = fields.Many2one('product.category', string='Product Category', related='product_id.categ_id', store=False, readonly=True)
    x_studio_project_no = fields.Many2one('project.project', string='Project No', related='move_id.x_studio_project_no', store=True, readonly=True)
    x_studio_purchase_order = fields.Char(string='Purchase Order', related='purchase_order_id.name', store=True, readonly=True)
    x_studio_purpose_code = fields.Char(string='Purpose Code', related='x_studio_contract_id.employee_id.x_studio_purpose_code', store=True, readonly=True)
    x_studio_related_field_5LBku = fields.Char(string='New Related Field', readonly=True, store=False)
    x_studio_related_field_5j5_1isv2aad6 = fields.Char(string='New Related Field', related='x_studio_contract_id.employee_id.x_studio_occupation_code', store=True, readonly=True)
    x_studio_related_field_CQ41C = fields.Many2one('product.product', string='New Related Field', related='product_id.product_variant_id.product_variant_id', store=False, readonly=True)
    x_studio_related_field_CvPMn = fields.Char(string='New Related Field', related='product_id.x_studio_many2one_field_8eWzY.item_ids.price', store=False, readonly=True)
    x_studio_related_field_FWW4G = fields.Float(string='New Related Field', readonly=True)
    x_studio_related_field_HFHrh = fields.Char(string='New Related Field', readonly=True, store=False)
    x_studio_related_field_HO3gE = fields.Char(string='New Related Field', readonly=True, store=False)
    x_studio_related_field_MnJZJ = fields.Char(string='New Related Field', readonly=True, store=False)
    x_studio_related_field_Nf3SX = fields.Float(string='New Related Field', readonly=True)
    x_studio_related_field_SORzX = fields.Integer(string='New Related Field', related='move_id.journal_id.id', store=True, readonly=True)
    x_studio_related_field_VzwUx = fields.Integer(string='New Related Field', related='move_id.journal_id.id', store=True, readonly=True)
    x_studio_related_field_WVIs6 = fields.Char(string='New Related Field', related='purchase_order_id.order_line.x_studio_indent_no', store=True, readonly=True)
    x_studio_related_field_X2pdt = fields.Float(string='New Related Field', related='product_id.x_studio_many2one_field_8eWzY.item_ids.fixed_price', store=True, readonly=True)
    x_studio_related_field_aD9tj = fields.Float(string='New Related Field', related='product_id.x_studio_many2one_field_8eWzY.item_ids.fixed_price', store=True, readonly=True)
    x_studio_related_field_e9NHB = fields.Char(string='New Related Field', related='purchase_line_id.order_id.x_studio_indent', store=True, readonly=True)
    x_studio_related_field_kbp8y = fields.Char(string='New Related Field', related='product_id.product_variant_id.display_name', store=False, readonly=True)
    x_studio_related_field_lBjdh = fields.Float(string='New Related Field', related='product_id.list_price', store=False, readonly=True)
    # TODO: x_studio_related_field_zy8mz = fields.One2many(...) -- Studio inverse name unknown; port from Clear-DB manually.
    x_studio_sales_report_type = fields.Many2one('x_sales_report_type', string='Report Type (S- Incentive Calculation)')
    x_studio_sales_team = fields.Many2one('crm.team', string='Sales Team', related='move_id.team_id', store=True, readonly=True)
    x_studio_status = fields.Selection([('draft', 'Draft'), ('posted', 'Posted'), ('cancel', 'Cancelled')], string='Status', related='move_id.state', store=True, readonly=True)
    x_studio_status_1 = fields.Selection([('draft', 'Draft'), ('posted', 'Posted'), ('cancel', 'Cancelled')], string='Status', related='move_id.state', store=True, readonly=True)
    x_studio_surname = fields.Char(string='Surname', related='x_studio_contract_id.x_studio_surname', store=True, readonly=True)
    x_studio_swift_code = fields.Char(string='Swift Code', related='x_studio_contract_id.employee_id.bank_account_id.x_studio_swift_code', store=True, readonly=True)
    x_studio_tags = fields.Many2many('x_misc_charge_codes', 'account_move_line_x_studio_tags_rel', 'account_id', 'x_misc_charge_codes_id', string='Tags')
    x_studio_tax = fields.Float(string='Tax', readonly=True)  # was Monetary (no currency_field)
    x_studio_to_account = fields.Char(string='To Account', related='x_studio_contract_id.employee_id.bank_account_id.acc_number', store=True, readonly=True)
    x_studio_total_contribution = fields.Float(string='Total Contribution', compute='_compute_x_studio_total_contribution', store=True, readonly=True)
    x_studio_total_earnings = fields.Float(string='Total Earnings', readonly=True)  # was Monetary (no currency_field)

    @api.depends('distribution_analytic_account_ids', 'journal_id', 'name', 'date')
    def _compute_x_studio_employers_contribution(self):
        AML = self.env['account.move.line']
        for rec in self:
            value = 0
            if rec.name == 'EPF 12%':
                value = abs(rec.amount_currency or 0)
            elif rec.name == 'EPF 8%' and rec.distribution_analytic_account_ids:
                etf = AML.search([
                    ('distribution_analytic_account_ids', 'in', rec.distribution_analytic_account_ids.ids),
                    ('name', '=', 'EPF 12%'),
                    ('date', '=', rec.date),
                ], limit=1)
                if etf:
                    value = abs(etf.amount_currency or 0)
            rec.x_studio_employers_contribution = value

    @api.depends('distribution_analytic_account_ids', 'journal_id', 'name', 'date')
    def _compute_x_studio_members_contribution(self):
        AML = self.env['account.move.line']
        for rec in self:
            value = 0
            if rec.name == 'EPF 8%':
                value = abs(rec.amount_currency or 0)
            elif rec.name == 'EPF 12%' and rec.distribution_analytic_account_ids:
                epf = AML.search([
                    ('distribution_analytic_account_ids', 'in', rec.distribution_analytic_account_ids.ids),
                    ('name', '=', 'EPF 8%'),
                    ('date', '=', rec.date),
                ], limit=1)
                if epf:
                    value = abs(epf.amount_currency or 0)
            rec.x_studio_members_contribution = value

    @api.depends('x_studio_members_contribution', 'x_studio_employers_contribution')
    def _compute_x_studio_total_contribution(self):
        for rec in self:
            rec.x_studio_total_contribution = (
                rec.x_studio_members_contribution + rec.x_studio_employers_contribution)

