"""BugFix-Accounting v17.0.0.0.138: seed ir.model.fields.selection rows via
Odoo's own _update_selection helper (framework API, not cr.execute).

Companion to _seed_field_selections in ../../hooks.py; this covers
version-upgrade path (post_init_hook covers fresh install).
"""

import logging

from odoo import SUPERUSER_ID, api

_logger = logging.getLogger(__name__)

_FIELD_SELECTIONS = [
    ("customer_posting_pro", "item_relation_type", "All", "All", 10),
    ("misc_charge_codes", "charge_group", "None", "None", 10),
    ("consignment_charge_h", "charge_group", "None", "None", 10),
    ("consignment_charge_h", "basis", "Percentage", "Percentage", 10),
    ("temp_tp_invoice_line", "basis", "Percentage", "Percentage", 10),
    ("temp_tp_invoice_line", "charge_group", "None", "None", 10),
    ("account.move.line", "status", "draft", "Draft", 10),
    ("lc_header", "lc_credit_type", "Irrevocable", "Irrevocable", 10),
    (
        "lc_header",
        "lc_credit_sub_type",
        "Non Transferable",
        "Non Transferable",
        10,
    ),
    ("lc_header", "status", "Draft", "Draft", 10),
    ("lc_header", "tolerance_type", "Plus", "Plus", 10),
    ("lc_header", "partial_shipment", "Allowed", "Allowed", 10),
    ("lc_header", "transshipment", "Allowed", "Allowed", 10),
    ("lc_header", "draft", "At Sight", "At Sight", 10),
    ("lc_header", "confirmation_instructions", "None", "None", 10),
    ("lc_header", "selection_field_yo4qM", "Draft", "Draft", 10),
    ("sales_report_model", "selection_field_Fbw0x", "Draft", "Draft", 10),
    ("misc_charge_codes", "debit_acc_type", "Item", "Item", 10),
    ("misc_charge_codes", "credit_acc_type", "Item", "Item", 10),
    (
        "sales_report_type",
        "report_code",
        "Daily Sales Summary",
        "Daily Sales Summary",
        10,
    ),
    (
        "sales_report_model",
        "report_code",
        "s-dailysales",
        "Daily Sales Summary",
        10,
    ),
    ("rm_sales_prod_purch", "product_type", "consu", "Consumable", 10),
    ("account.move", "order_payment_method", "Cash", "Cash", 10),
    ("account.move.line", "payment_status", "not_paid", "Not Paid", 10),
    ("account.move.line", "customer_group_type", "General", "General", 10),
    ("account.move.line", "status_1", "draft", "Draft", 10),
    ("product.template", "product_type", "None", "None", 10),
    ("account.move.line", "pr_type", "Local", "Local", 10),
    ("account.move", "purchase_type", "Local", "Local", 10),
    ("account.move", "test_type", "One", "One", 10),
    ("account.move", "journal_type", "Bill", "Bill", 10),
    ("account.move.line", "journal_type", "Bill", "Bill", 10),
    ("account.payment", "type", "General", "General", 10),
    ("account.move", "type", "General", "General", 10),
    ("customer_posting_pro", "item_relation_type", "Group", "Group", 1),
    ("misc_charge_codes", "charge_group", "Charges", "Charges", 1),
    ("consignment_charge_h", "charge_group", "Charges", "Charges", 1),
    (
        "consignment_charge_h",
        "basis",
        "Fixed Per Document",
        "Fixed Per Document",
        1,
    ),
    (
        "temp_tp_invoice_line",
        "basis",
        "Fixed Per Document",
        "Fixed Per Document",
        1,
    ),
    ("temp_tp_invoice_line", "charge_group", "Charges", "Charges", 1),
    ("account.move.line", "status", "posted", "Posted", 1),
    ("lc_header", "lc_credit_type", "Revocable", "Revocable", 1),
    ("lc_header", "lc_credit_sub_type", "Transferable", "Transferable", 1),
    ("lc_header", "tolerance_type", "Minus", "Minus", 1),
    ("lc_header", "partial_shipment", "Not Allowed", "Not Allowed", 1),
    ("lc_header", "transshipment", "Not Allowed", "Not Allowed", 1),
    ("lc_header", "draft", "Deferred Payment", "Deferred Payment", 1),
    ("lc_header", "confirmation_instructions", "A", "A", 1),
    ("lc_header", "selection_field_yo4qM", "Posted", "Posted", 1),
    ("lc_header", "status", "Posted", "Posted", 1),
    ("sales_report_model", "selection_field_Fbw0x", "Done", "Done", 1),
    ("misc_charge_codes", "debit_acc_type", "G/L Account", "G/L Account", 1),
    (
        "misc_charge_codes",
        "credit_acc_type",
        "G/L Account",
        "G/L Account",
        1,
    ),
    (
        "sales_report_type",
        "report_code",
        "Sales Details for Incentive Calc.",
        "Sales Details for Incentive Calc.",
        1,
    ),
    (
        "sales_report_model",
        "report_code",
        "s-salesincentive",
        "Sales Details for Incentive Calc.",
        1,
    ),
    ("rm_sales_prod_purch", "product_type", "service", "Service", 1),
    ("account.move", "order_payment_method", "Credit", "Credit", 1),
    ("account.move.line", "payment_status", "in_payment", "In Payment", 1),
    (
        "account.move.line",
        "customer_group_type",
        "Distributor",
        "Distributor",
        1,
    ),
    ("account.move.line", "status_1", "posted", "Posted", 1),
    ("account.move.line", "pr_type", "Import", "Import", 1),
    ("account.move", "purchase_type", "Import", "Import", 1),
    ("account.move", "test_type", "Two", "Two", 1),
    ("account.move", "journal_type", "Payment", "Payment", 1),
    ("account.move.line", "journal_type", "Payment", "Payment", 1),
    ("account.payment", "type", "Advance Payment", "Advance Payment", 1),
    ("account.move", "type", "Advance Payment", "Advance Payment", 1),
    ("customer_posting_pro", "item_relation_type", "Table", "Table", 2),
    ("misc_charge_codes", "charge_group", "Duty", "Duty", 2),
    ("consignment_charge_h", "charge_group", "Duty", "Duty", 2),
    ("temp_tp_invoice_line", "charge_group", "Duty", "Duty", 2),
    ("account.move.line", "status", "cancel", "Cancelled", 2),
    ("lc_header", "lc_credit_sub_type", "Revolving", "Revolving", 2),
    ("lc_header", "confirmation_instructions", "B", "B", 2),
    ("lc_header", "status", "Paid", "Paid", 2),
    ("lc_header", "selection_field_yo4qM", "Amended", "Amended", 2),
    (
        "sales_report_type",
        "report_code",
        "Production Overview - WIP",
        "Production Overview - WIP",
        2,
    ),
    (
        "sales_report_model",
        "report_code",
        "m-wip",
        "Production Overview - WIP",
        2,
    ),
    (
        "rm_sales_prod_purch",
        "product_type",
        "product",
        "Storable Product",
        2,
    ),
    ("account.move.line", "payment_status", "paid", "Paid", 2),
    ("account.move.line", "customer_group_type", "Dealer", "Dealer", 2),
    ("account.move.line", "status_1", "cancel", "Cancelled", 2),
    ("account.move", "journal_type", "Settlement", "Settlement", 2),
    ("account.move.line", "journal_type", "Settlement", "Settlement", 2),
    ("misc_charge_codes", "charge_group", "Taxes", "Taxes", 3),
    ("consignment_charge_h", "charge_group", "Taxes", "Taxes", 3),
    ("temp_tp_invoice_line", "charge_group", "Taxes", "Taxes", 3),
    ("lc_header", "confirmation_instructions", "C", "C", 3),
    ("lc_header", "status", "Amended", "Amended", 3),
    (
        "sales_report_type",
        "report_code",
        "Customer Aging Report",
        "Customer Aging Report",
        3,
    ),
    ("lc_header", "selection_field_yo4qM", "Paid", "Paid", 3),
    ("account.move.line", "payment_status", "partial", "Partially Paid", 3),
    ("lc_header", "status", "Cancelled", "Cancelled", 4),
    (
        "sales_report_type",
        "report_code",
        "Slow Moving Items",
        "Slow Moving Items",
        4,
    ),
    ("lc_header", "selection_field_yo4qM", "Cancelled", "Cancelled", 4),
    ("account.move.line", "payment_status", "reversed", "Reversed", 4),
    (
        "sales_report_type",
        "report_code",
        "Sales - Production - Purchase Report",
        "Sales - Production - Purchase Report",
        5,
    ),
    (
        "account.move.line",
        "payment_status",
        "invoicing_legacy",
        "Invoicing App Legacy",
        5,
    ),
    (
        "sales_report_type",
        "report_code",
        "Production Summary - Split",
        "Production Summary - Split",
        6,
    ),
    (
        "sales_report_type",
        "report_code",
        "Production Job Variance",
        "Production Job Variance",
        7,
    ),
    ("sales_report_type", "report_code", "Casting Melt", "Casting Melt", 8),
    (
        "sales_report_type",
        "report_code",
        "Import Transaction",
        "Import Transaction",
        9,
    ),
    (
        "sales_report_type",
        "report_code",
        "Project Gross Margin",
        "Project Gross Margin",
        10,
    ),
    (
        "sales_report_type",
        "report_code",
        "Costing Work Sheet",
        "Costing Work Sheet",
        11,
    ),
]


def migrate(cr, version):
    if not version:
        return
    env = api.Environment(cr, SUPERUSER_ID, {})
    Sel = env["ir.model.fields.selection"].sudo()
    Fld = env["ir.model.fields"].sudo()
    grouped = {}
    for model, fname, value, label, seq in _FIELD_SELECTIONS:
        grouped.setdefault((model, fname), []).append((value, label, seq))
    for (model, fname), values in grouped.items():
        fld = Fld.search(
            [("model", "=", model), ("name", "=", fname)],
            limit=1,
        )
        if not fld:
            continue
        existing_recs = Sel.search(
            [("field_id", "=", fld.id)],
            order="sequence",
        )
        existing_pairs = [(r.value, r.name) for r in existing_recs]
        existing_values = {v for v, _ in existing_pairs}
        added = []
        for v, line, _seq in sorted(values, key=lambda t: t[2]):
            if v in existing_values:
                continue
            existing_pairs.append((v, line))
            existing_values.add(v)
            added.append(v)
        if not added:
            continue
        try:
            with cr.savepoint():
                Sel._update_selection(model, fname, existing_pairs)
                _logger.info(
                    "BugFix-Accounting v17.0.0.0.138: seeded %s.%s += %s.",
                    model,
                    fname,
                    added,
                )
        except Exception as e:
            _logger.warning(
                "BugFix-Accounting v17.0.0.0.138: seed failed %s.%s (%s).",
                model,
                fname,
                e,
                exc_info=True,
            )
