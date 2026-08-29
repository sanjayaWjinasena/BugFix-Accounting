# -*- coding: utf-8 -*-
"""Placeholder file - kept so models/__init__.py imports don't break
during the v0.0.33 upstream migration.

x_sales_report_type moved to studio_usermodel_migration
('Jinasena : Masterdata : User') as of v0.0.12. All fields
(x_studio_journal_entry_id, x_studio_journal_items_id,
x_studio_sales_lines_id, x_studio_test, x_studio_report_code,
x_studio_sequence, x_active, x_name) live there now.

The inverse M2Os previously in this repo's account_move.py,
account_move_line.py, and BugFix-Sales/sale_order_line.py also moved
upstream to make the O2M/M2O pairs live in the same module.
"""
from odoo import models


class XSalesReportType(models.Model):
    _inherit = 'x_sales_report_type'
    # Kept as empty _inherit to preserve the import in __init__.py.
    # Any Accounting-specific extension goes here in the future.
