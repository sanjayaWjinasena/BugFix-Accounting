# -*- coding: utf-8 -*-
from odoo import models, fields

class XSalesReportModelGap(models.Model):
    _inherit = 'x_sales_report_model'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
