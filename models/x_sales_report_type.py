# -*- coding: utf-8 -*-
"""BugFix-Accounting _inherit of x_sales_report_type.

The model itself moved to Jinasena_Masterdata_Reporting v17.0.1.0.0.
This file is kept as an empty _inherit placeholder because
models/__init__.py still imports it. Any BugFix-Accounting-specific
extensions of x_sales_report_type would go here.
"""
from odoo import models


class XSalesReportType(models.Model):
    _inherit = 'x_sales_report_type'
