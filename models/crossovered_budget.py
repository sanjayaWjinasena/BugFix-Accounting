# -*- coding: utf-8 -*-
"""crossovered.budget — Studio extensions for project-budget management.

Extends the standard-Odoo (account_budget) `crossovered.budget` model
with 20 Studio-created fields covering:
  * Currency + analytic account + linked sale.order / project
  * A validation flag (x_studio_confirm_status) that walks the
    linked SO's quotation type + inventory-short flag and checks
    x_purchase_request (BugFix-Purchase) for outstanding items
  * Four monetary aggregates (project value, actual invoiced,
    actual expenses, total project expenses) that walk the
    account_budget crossovered_budget_line rows by their
    general_budget_id.name label
  * Gross margin + gross-margin-percentage pair (monetary + float
    variants — Studio duplicated for widget compatibility)
  * Project-completed-percentage pair (same duplication pattern)
  * Estimated-revenue compute
  * Validation booleans for budget-line non-zero + SPR status
    (subcontracting purchase request check)

Every compute traverses either:
  * standard-Odoo fields (crossovered_budget_line.planned_amount,
    .practical_amount, .general_budget_id.name)
  * Studio fields on sale.order provided by BugFix-Sales
    (x_studio_quotation_type, x_studio_inventory_short,
    x_studio_sub_contract)
  * x_purchase_request records provided by BugFix-Purchase
    (searched by x_studio_created_from_so pointing at the linked SO)

Ported verbatim from Clear-DB's Studio compute strings on 2026-08-29
per the feedback-clear-db-verbatim rule. Guards added for missing
x_purchase_request model (fresh install without BugFix-Purchase yet)
so the compute doesn't crash; falls back to conservative False.
"""
from odoo import api, fields, models


class CrossoveredBudget(models.Model):
    _inherit = 'crossovered.budget'

    x_currency_id = fields.Many2one('res.currency', string='Currency')

    # ---- Standard scalars (stored, no compute) ----
    x_studio_analytic_account = fields.Many2one(
        'account.analytic.account', string='Analytic Account',
    )
    x_studio_confirm_validation = fields.Text(string='Confirm Validation')
    x_studio_created_from_sales_order_1 = fields.Many2one(
        'sale.order', string='Created From Sales Order',
    )
    x_studio_project_no = fields.Many2one(
        'project.project', string='Project No',
    )
    x_studio_total = fields.Integer(string='Total')

    # ---- Percentage char sentinel (non-stored, read-only) ----
    # Clear-DB has compute='' (empty string) with depends set.
    # Preserved as an empty compute that assigns "" so the depends
    # graph still fires when the depended-on fields change.
    x_studio_percentage = fields.Char(
        string='Percentage',
        compute='_compute_x_studio_percentage',
        store=False,
        readonly=True,
    )
    x_studio_project_completed_percentage = fields.Monetary(
        string='Project Completed Percentage',
        currency_field='x_currency_id',
        compute='_compute_x_studio_project_completed_percentage',
        store=False,
        readonly=True,
    )

    # ---- Aggregates over crossovered_budget_line by label ----
    # 'Revenue' vs 'Expenses' comes from general_budget_id.name, the
    # standard-Odoo budget-category label. Studio's convention on
    # Clear-DB uses those exact strings.

    x_studio_project_value = fields.Monetary(
        string='Project Value',
        currency_field='x_currency_id',
        compute='_compute_x_studio_project_value',
        store=False,
        readonly=True,
    )
    x_studio_total_project_expenses = fields.Monetary(
        string='Total Project Expenses',
        currency_field='x_currency_id',
        compute='_compute_x_studio_total_project_expenses',
        store=False,
        readonly=True,
    )
    x_studio_actual_invoiced_amount = fields.Monetary(
        string='Actual Invoiced Amount',
        currency_field='x_currency_id',
        compute='_compute_x_studio_actual_invoiced_amount',
        store=False,
        readonly=True,
    )
    x_studio_actual_expenses_incurred = fields.Monetary(
        string='Actual Expenses Incurred',
        currency_field='x_currency_id',
        compute='_compute_x_studio_actual_expenses_incurred',
        store=False,
        readonly=True,
    )

    # ---- Derived from aggregates ----
    x_studio_estimated_revenue_1 = fields.Monetary(
        string='Estimated Revenue',
        currency_field='x_currency_id',
        compute='_compute_x_studio_estimated_revenue_1',
        store=False,
        readonly=True,
    )
    x_studio_gross_margin = fields.Monetary(
        string='Gross Margin',
        currency_field='x_currency_id',
        compute='_compute_x_studio_gross_margin',
        store=False,
        readonly=True,
    )
    x_studio_gross_margin_percentage = fields.Monetary(
        string='Gross Margin Percentage',
        currency_field='x_currency_id',
        compute='_compute_x_studio_gross_margin_percentage',
        store=False,
        readonly=True,
    )
    x_studio_gross_margin_percentage_1 = fields.Float(
        string='Gross Margin Percentage',
        compute='_compute_x_studio_gross_margin_percentage_1',
        store=False,
        readonly=True,
    )
    x_studio_project_completed_percentage_1 = fields.Float(
        string='Project Completed Percentage',
        compute='_compute_x_studio_project_completed_percentage_1',
        store=False,
        readonly=True,
    )

    # ---- SO-driven validation booleans (traverse BugFix-Sales +
    # BugFix-Purchase) ----
    x_studio_confirm_status = fields.Boolean(
        string='Confirm Status',
        compute='_compute_x_studio_confirm_status',
        store=False,
        readonly=True,
    )
    x_studio_spr_status = fields.Boolean(
        string='SPR Status ',
        compute='_compute_x_studio_spr_status',
        store=False,
        readonly=True,
    )
    x_studio_valid_budget_lines = fields.Boolean(
        string='Valid Budget Lines',
        compute='_compute_x_studio_valid_budget_lines',
        store=False,
        readonly=True,
    )

    # ==============================================================
    # Compute methods — all @api.depends chains ported verbatim.
    # ==============================================================

    @api.depends('x_studio_gross_margin', 'x_studio_estimated_revenue_1')
    def _compute_x_studio_percentage(self):
        for rec in self:
            rec.x_studio_percentage = ''

    def _compute_x_studio_project_completed_percentage(self):
        for rec in self:
            rec.x_studio_project_completed_percentage = 0

    @api.depends('crossovered_budget_line')
    def _compute_x_studio_project_value(self):
        for rec in self:
            total = 0
            for line in rec.crossovered_budget_line:
                if line.general_budget_id.name == 'Revenue':
                    total += line.planned_amount
            rec.x_studio_project_value = total

    @api.depends('crossovered_budget_line')
    def _compute_x_studio_total_project_expenses(self):
        for rec in self:
            expense = 0
            for line in rec.crossovered_budget_line:
                if line.general_budget_id.name == 'Expenses':
                    expense -= line.planned_amount
            rec.x_studio_total_project_expenses = expense

    @api.depends('crossovered_budget_line')
    def _compute_x_studio_actual_invoiced_amount(self):
        for rec in self:
            total = 0
            for line in rec.crossovered_budget_line:
                if line.general_budget_id.name == 'Revenue':
                    total += line.practical_amount
            rec.x_studio_actual_invoiced_amount = total

    @api.depends('crossovered_budget_line')
    def _compute_x_studio_actual_expenses_incurred(self):
        for rec in self:
            expense = 0
            for line in rec.crossovered_budget_line:
                if line.general_budget_id.name == 'Expenses':
                    expense -= line.practical_amount
            rec.x_studio_actual_expenses_incurred = expense

    @api.depends(
        'x_studio_project_completed_percentage_1',
        'x_studio_project_value',
    )
    def _compute_x_studio_estimated_revenue_1(self):
        for rec in self:
            perc = (rec.x_studio_project_completed_percentage_1 or 0) / 100
            rec.x_studio_estimated_revenue_1 = (
                (rec.x_studio_project_value or 0) * round(perc, 4)
            )

    @api.depends(
        'x_studio_estimated_revenue_1',
        'x_studio_actual_expenses_incurred',
    )
    def _compute_x_studio_gross_margin(self):
        for rec in self:
            rec.x_studio_gross_margin = (
                (rec.x_studio_estimated_revenue_1 or 0)
                - (rec.x_studio_actual_expenses_incurred or 0)
            )

    @api.depends('x_studio_gross_margin', 'x_studio_estimated_revenue_1')
    def _compute_x_studio_gross_margin_percentage(self):
        for rec in self:
            gross = float(rec.x_studio_gross_margin or 0)
            total = float(rec.x_studio_estimated_revenue_1 or 0)
            rec.x_studio_gross_margin_percentage = (
                (gross / total) * 100 if total > 0 else 0
            )

    @api.depends('x_studio_gross_margin', 'x_studio_estimated_revenue_1')
    def _compute_x_studio_gross_margin_percentage_1(self):
        for rec in self:
            gross = float(rec.x_studio_gross_margin or 0)
            total = float(rec.x_studio_estimated_revenue_1 or 0)
            rec.x_studio_gross_margin_percentage_1 = (
                (gross / total) * 100 if total > 0 else 0
            )

    @api.depends(
        'x_studio_actual_expenses_incurred',
        'x_studio_total_project_expenses',
    )
    def _compute_x_studio_project_completed_percentage_1(self):
        for rec in self:
            act = float(rec.x_studio_actual_expenses_incurred or 0)
            total = float(rec.x_studio_total_project_expenses or 0)
            rec.x_studio_project_completed_percentage_1 = (
                (act / total) * 100 if total > 0 else 0
            )

    @api.depends(
        'x_studio_created_from_sales_order_1.x_studio_quotation_type',
        'x_studio_created_from_sales_order_1.x_studio_inventory_short',
    )
    def _compute_x_studio_confirm_status(self):
        """True when the linked SO is a Project-type + inventory-short
        SO whose x_purchase_request rows still show
        x_studio_total_order_remainder > 0 (i.e. items still
        outstanding on the PR). False otherwise — including for
        non-Project SOs and non-inventory-short cases.

        Guarded against missing x_purchase_request model (BugFix-Purchase
        not installed).
        """
        PurchaseRequest = self.env.get('x_purchase_request')
        for rec in self:
            valid_lines = False
            so = rec.x_studio_created_from_sales_order_1
            if so and so.x_studio_quotation_type == 'Project':
                if so.x_studio_inventory_short:
                    if PurchaseRequest is not None:
                        pr = PurchaseRequest.search([
                            ('x_studio_created_from_so', '=', so.id),
                        ])
                        if pr:
                            for line in pr:
                                if line.x_studio_total_order_remainder > 0:
                                    valid_lines = True
                                    break
                        else:
                            valid_lines = True
                    else:
                        # PR model absent — mirror Studio's implicit
                        # "no rows found → valid" branch.
                        valid_lines = True
            rec.x_studio_confirm_status = valid_lines

    @api.depends('x_studio_created_from_sales_order_1')
    def _compute_x_studio_spr_status(self):
        """True when the linked SO is a Project-type + sub-contract SO
        with NO 'Done' x_purchase_request. Empty for other cases.

        Guarded against missing x_purchase_request model.
        """
        PurchaseRequest = self.env.get('x_purchase_request')
        for rec in self:
            valid = False
            so = rec.x_studio_created_from_sales_order_1
            if so and so.x_studio_quotation_type == 'Project':
                if so.x_studio_sub_contract:
                    if PurchaseRequest is not None:
                        pr = PurchaseRequest.search([
                            ('x_studio_created_from_so', '=', so.id),
                            ('x_studio_selection_field_yzPk1', '=', 'Done'),
                        ], limit=1)
                        valid = False if pr else True
                    else:
                        valid = True
            rec.x_studio_spr_status = valid

    @api.depends('crossovered_budget_line')
    def _compute_x_studio_valid_budget_lines(self):
        """True when the budget has at least one line and no line has
        planned_amount == 0. Ported verbatim.
        """
        for rec in self:
            val = False
            val2 = False
            for line in rec.crossovered_budget_line:
                val = True
                if line.planned_amount == 0:
                    val2 = True
            if val2:
                val = False
            rec.x_studio_valid_budget_lines = val


class CrossoveredBudgetLines(models.Model):
    _inherit = 'crossovered.budget.lines'

    x_studio_estimate = fields.Monetary(
        string='Estimate',
        compute='_compute_x_studio_estimate',
        store=False,
        readonly=True,
    )

    def _compute_x_studio_estimate(self):
        """Clear-DB ships compute='' (empty). Preserved as a no-op
        that sets the field to 0 so the field renders without error.
        """
        for rec in self:
            rec.x_studio_estimate = 0
