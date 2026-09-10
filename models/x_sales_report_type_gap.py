# -*- coding: utf-8 -*-
from odoo import models, fields

class XSalesReportTypeGap(models.Model):
    _inherit = 'x_sales_report_type'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Report Name')
