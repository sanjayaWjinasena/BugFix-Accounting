# -*- coding: utf-8 -*-
"""Extension point for x_sales_report_model on BugFix-Accounting.

Model owner: studio_usermodel_migration (models/x_sales_report_model.py).
All 25 scalar fields, the 4 relational fields (customer, project_no,
report_type, sales_centre) and the 4 related One2many navigations are
declared upstream.

Kept as the insertion point for the 16 direct One2many navigations
into x_rm_* target models (x_rm_gross_margin_actu, x_rm_gross_margin_comp,
x_rm_daily_s1/s2/s3, x_rm_sales_order_line, etc.) — those target models
live in BugFix-Accounting, so this is the natural home for
`_inherit = 'x_sales_report_model'` with the 16 O2Ms. See
INSTALL_JOURNEY.md follow-up item #1 and the "Direct O2Ms to x_rm_*
models (16 total) NOT declared here" note in the upstream file.
"""
from odoo import models


class XSalesReportModel(models.Model):
    _inherit = 'x_sales_report_model'
