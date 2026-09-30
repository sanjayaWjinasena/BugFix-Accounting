# -*- coding: utf-8 -*-
"""BugFix-Accounting: post-install hooks.

Seeds ir.model.fields.selection rows that Studio populated in CDB but
Odoo 17 doesn't recreate on install. Uses the ORM (no direct SQL) per the
project's no-direct-SQL rule; the sibling migrations/<v>/post-migrate.py
runs the same seeding on version upgrades.
"""
import logging

_logger = logging.getLogger(__name__)

# --- Field selection seed data (ORM-only, no direct SQL) ---
# All rows Studio populated in CDB but Odoo 17 doesn't recreate on install.
# `state='base'` rows: options for Python-declared Selection fields that
# Odoo would normally set at install but Studio-side sequence differs.
# `related=` rows: audit-parity stubs — Odoo resolves at runtime from the
# source field, so shipping these creates DB rows for audit match with zero
# functional effect. (See feedback-python-only-fixes: prefer ORM over SQL.)
# (model, field_name, value, display_name, sequence)
_FIELD_SELECTIONS = [
    ('x_customer_posting_pro', 'x_studio_item_relation_type', 'All', 'All', 10),
    ('x_misc_charge_codes', 'x_studio_charge_group', 'None', 'None', 10),
    ('x_consignment_charge_h', 'x_studio_charge_group', 'None', 'None', 10),
    ('x_consignment_charge_h', 'x_studio_basis', 'Percentage', 'Percentage', 10),
    ('x_temp_tp_invoice_line', 'x_studio_basis', 'Percentage', 'Percentage', 10),
    ('x_temp_tp_invoice_line', 'x_studio_charge_group', 'None', 'None', 10),
    ('account.move.line', 'x_studio_status', 'draft', 'Draft', 10),
    ('x_lc_header', 'x_studio_lc_credit_type', 'Irrevocable', 'Irrevocable', 10),
    ('x_lc_header', 'x_studio_lc_credit_sub_type', 'Non Transferable', 'Non Transferable', 10),
    ('x_lc_header', 'x_studio_status', 'Draft', 'Draft', 10),
    ('x_lc_header', 'x_studio_tolerance_type', 'Plus', 'Plus', 10),
    ('x_lc_header', 'x_studio_partial_shipment', 'Allowed', 'Allowed', 10),
    ('x_lc_header', 'x_studio_transshipment', 'Allowed', 'Allowed', 10),
    ('x_lc_header', 'x_studio_draft', 'At Sight', 'At Sight', 10),
    ('x_lc_header', 'x_studio_confirmation_instructions', 'None', 'None', 10),
    ('x_lc_header', 'x_studio_selection_field_yo4qM', 'Draft', 'Draft', 10),
    ('x_sales_report_model', 'x_studio_selection_field_Fbw0x', 'Draft', 'Draft', 10),
    ('x_misc_charge_codes', 'x_studio_debit_acc_type', 'Item', 'Item', 10),
    ('x_misc_charge_codes', 'x_studio_credit_acc_type', 'Item', 'Item', 10),
    ('x_sales_report_type', 'x_studio_report_code', 'Daily Sales Summary', 'Daily Sales Summary', 10),
    ('x_sales_report_model', 'x_studio_report_code', 's-dailysales', 'Daily Sales Summary', 10),
    ('x_rm_sales_prod_purch', 'x_studio_product_type', 'consu', 'Consumable', 10),
    ('account.move', 'x_studio_order_payment_method', 'Cash', 'Cash', 10),
    ('account.move.line', 'x_studio_payment_status', 'not_paid', 'Not Paid', 10),
    ('account.move.line', 'x_studio_customer_group_type', 'General', 'General', 10),
    ('account.move.line', 'x_studio_status_1', 'draft', 'Draft', 10),
    ('product.template', 'x_studio_product_type', 'None', 'None', 10),
    ('account.move.line', 'x_studio_pr_type', 'Local', 'Local', 10),
    ('account.move', 'x_studio_purchase_type', 'Local', 'Local', 10),
    ('account.move', 'x_studio_test_type', 'One', 'One', 10),
    ('account.move', 'x_studio_journal_type', 'Bill', 'Bill', 10),
    ('account.move.line', 'x_studio_journal_type', 'Bill', 'Bill', 10),
    ('account.payment', 'x_studio_type', 'General', 'General', 10),
    ('account.move', 'x_studio_type', 'General', 'General', 10),
    ('x_customer_posting_pro', 'x_studio_item_relation_type', 'Group', 'Group', 1),
    ('x_misc_charge_codes', 'x_studio_charge_group', 'Charges', 'Charges', 1),
    ('x_consignment_charge_h', 'x_studio_charge_group', 'Charges', 'Charges', 1),
    ('x_consignment_charge_h', 'x_studio_basis', 'Fixed Per Document', 'Fixed Per Document', 1),
    ('x_temp_tp_invoice_line', 'x_studio_basis', 'Fixed Per Document', 'Fixed Per Document', 1),
    ('x_temp_tp_invoice_line', 'x_studio_charge_group', 'Charges', 'Charges', 1),
    ('account.move.line', 'x_studio_status', 'posted', 'Posted', 1),
    ('x_lc_header', 'x_studio_lc_credit_type', 'Revocable', 'Revocable', 1),
    ('x_lc_header', 'x_studio_lc_credit_sub_type', 'Transferable', 'Transferable', 1),
    ('x_lc_header', 'x_studio_tolerance_type', 'Minus', 'Minus', 1),
    ('x_lc_header', 'x_studio_partial_shipment', 'Not Allowed', 'Not Allowed', 1),
    ('x_lc_header', 'x_studio_transshipment', 'Not Allowed', 'Not Allowed', 1),
    ('x_lc_header', 'x_studio_draft', 'Deferred Payment', 'Deferred Payment', 1),
    ('x_lc_header', 'x_studio_confirmation_instructions', 'A', 'A', 1),
    ('x_lc_header', 'x_studio_selection_field_yo4qM', 'Posted', 'Posted', 1),
    ('x_lc_header', 'x_studio_status', 'Posted', 'Posted', 1),
    ('x_sales_report_model', 'x_studio_selection_field_Fbw0x', 'Done', 'Done', 1),
    ('x_misc_charge_codes', 'x_studio_debit_acc_type', 'G/L Account', 'G/L Account', 1),
    ('x_misc_charge_codes', 'x_studio_credit_acc_type', 'G/L Account', 'G/L Account', 1),
    ('x_sales_report_type', 'x_studio_report_code', 'Sales Details for Incentive Calc.', 'Sales Details for Incentive Calc.', 1),
    ('x_sales_report_model', 'x_studio_report_code', 's-salesincentive', 'Sales Details for Incentive Calc.', 1),
    ('x_rm_sales_prod_purch', 'x_studio_product_type', 'service', 'Service', 1),
    ('account.move', 'x_studio_order_payment_method', 'Credit', 'Credit', 1),
    ('account.move.line', 'x_studio_payment_status', 'in_payment', 'In Payment', 1),
    ('account.move.line', 'x_studio_customer_group_type', 'Distributor', 'Distributor', 1),
    ('account.move.line', 'x_studio_status_1', 'posted', 'Posted', 1),
    ('account.move.line', 'x_studio_pr_type', 'Import', 'Import', 1),
    ('account.move', 'x_studio_purchase_type', 'Import', 'Import', 1),
    ('account.move', 'x_studio_test_type', 'Two', 'Two', 1),
    ('account.move', 'x_studio_journal_type', 'Payment', 'Payment', 1),
    ('account.move.line', 'x_studio_journal_type', 'Payment', 'Payment', 1),
    ('account.payment', 'x_studio_type', 'Advance Payment', 'Advance Payment', 1),
    ('account.move', 'x_studio_type', 'Advance Payment', 'Advance Payment', 1),
    ('x_customer_posting_pro', 'x_studio_item_relation_type', 'Table', 'Table', 2),
    ('x_misc_charge_codes', 'x_studio_charge_group', 'Duty', 'Duty', 2),
    ('x_consignment_charge_h', 'x_studio_charge_group', 'Duty', 'Duty', 2),
    ('x_temp_tp_invoice_line', 'x_studio_charge_group', 'Duty', 'Duty', 2),
    ('account.move.line', 'x_studio_status', 'cancel', 'Cancelled', 2),
    ('x_lc_header', 'x_studio_lc_credit_sub_type', 'Revolving', 'Revolving', 2),
    ('x_lc_header', 'x_studio_confirmation_instructions', 'B', 'B', 2),
    ('x_lc_header', 'x_studio_status', 'Paid', 'Paid', 2),
    ('x_lc_header', 'x_studio_selection_field_yo4qM', 'Amended', 'Amended', 2),
    ('x_sales_report_type', 'x_studio_report_code', 'Production Overview - WIP', 'Production Overview - WIP', 2),
    ('x_sales_report_model', 'x_studio_report_code', 'm-wip', 'Production Overview - WIP', 2),
    ('x_rm_sales_prod_purch', 'x_studio_product_type', 'product', 'Storable Product', 2),
    ('account.move.line', 'x_studio_payment_status', 'paid', 'Paid', 2),
    ('account.move.line', 'x_studio_customer_group_type', 'Dealer', 'Dealer', 2),
    ('account.move.line', 'x_studio_status_1', 'cancel', 'Cancelled', 2),
    ('account.move', 'x_studio_journal_type', 'Settlement', 'Settlement', 2),
    ('account.move.line', 'x_studio_journal_type', 'Settlement', 'Settlement', 2),
    ('x_misc_charge_codes', 'x_studio_charge_group', 'Taxes', 'Taxes', 3),
    ('x_consignment_charge_h', 'x_studio_charge_group', 'Taxes', 'Taxes', 3),
    ('x_temp_tp_invoice_line', 'x_studio_charge_group', 'Taxes', 'Taxes', 3),
    ('x_lc_header', 'x_studio_confirmation_instructions', 'C', 'C', 3),
    ('x_lc_header', 'x_studio_status', 'Amended', 'Amended', 3),
    ('x_sales_report_type', 'x_studio_report_code', 'Customer Aging Report', 'Customer Aging Report', 3),
    ('x_lc_header', 'x_studio_selection_field_yo4qM', 'Paid', 'Paid', 3),
    ('account.move.line', 'x_studio_payment_status', 'partial', 'Partially Paid', 3),
    ('x_lc_header', 'x_studio_status', 'Cancelled', 'Cancelled', 4),
    ('x_sales_report_type', 'x_studio_report_code', 'Slow Moving Items', 'Slow Moving Items', 4),
    ('x_lc_header', 'x_studio_selection_field_yo4qM', 'Cancelled', 'Cancelled', 4),
    ('account.move.line', 'x_studio_payment_status', 'reversed', 'Reversed', 4),
    ('x_sales_report_type', 'x_studio_report_code', 'Sales - Production - Purchase Report', 'Sales - Production - Purchase Report', 5),
    ('account.move.line', 'x_studio_payment_status', 'invoicing_legacy', 'Invoicing App Legacy', 5),
    ('x_sales_report_type', 'x_studio_report_code', 'Production Summary - Split', 'Production Summary - Split', 6),
    ('x_sales_report_type', 'x_studio_report_code', 'Production Job Variance', 'Production Job Variance', 7),
    ('x_sales_report_type', 'x_studio_report_code', 'Casting Melt', 'Casting Melt', 8),
    ('x_sales_report_type', 'x_studio_report_code', 'Import Transaction', 'Import Transaction', 9),
    ('x_sales_report_type', 'x_studio_report_code', 'Project Gross Margin', 'Project Gross Margin', 10),
    ('x_sales_report_type', 'x_studio_report_code', 'Costing Work Sheet', 'Costing Work Sheet', 11),
]


def _seed_field_selections(env, entries):
    """Idempotent ORM create of ir.model.fields.selection rows.
    Skip if the field is absent or the (field, value) row already exists.
    Per-row savepoint so a single failure doesn't abort the batch."""
    Fld = env['ir.model.fields'].sudo()
    Sel = env['ir.model.fields.selection'].sudo()
    for model, fname, value, label, seq in entries:
        fld = Fld.search(
            [('model', '=', model), ('name', '=', fname)], limit=1,
        )
        if not fld:
            _logger.info(
                "BugFix-Accounting: seed skip %s.%s (field absent).", model, fname,
            )
            continue
        exists = Sel.search(
            [('field_id', '=', fld.id), ('value', '=', value)], limit=1,
        )
        if exists:
            continue
        try:
            with env.cr.savepoint():
                Sel.create({
                    'field_id': fld.id, 'value': value,
                    'name': label, 'sequence': seq,
                })
        except Exception as e:
            _logger.warning(
                "BugFix-Accounting: seed failed %s.%s=%r (%s).",
                model, fname, value, e,
            )


def post_init_hook(env):
    _seed_field_selections(env, _FIELD_SELECTIONS)
