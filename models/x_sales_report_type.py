# -*- coding: utf-8 -*-
"""Extension point for x_sales_report_type on BugFix-Accounting.

Model owner: studio_usermodel_migration (models/x_sales_report_type.py).
All base fields (x_active, x_name, x_studio_report_code, x_studio_sequence)
and the 4 One2many navigations (x_studio_journal_entry_id,
x_studio_journal_items_id, x_studio_sales_lines_id, x_studio_test) are
declared upstream — inverse M2Os on account.move / account.move.line /
sale.order.line also live in studio_usermodel_migration.

This _inherit-only stub is kept as the insertion point for future
x_rm_* O2M navigations (the 5 stock/mrp-side One2manys and any
BugFix-Accounting-owned x_rm_* targets) per
INSTALL_JOURNEY.md follow-up item #1.
"""
from odoo import models


class XSalesReportType(models.Model):
    _inherit = 'x_sales_report_type'
