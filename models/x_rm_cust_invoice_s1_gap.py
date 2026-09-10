# -*- coding: utf-8 -*-
from odoo import models, fields

class XRmCustInvoiceS1Gap(models.Model):
    _inherit = 'x_rm_cust_invoice_s1'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
