# -*- coding: utf-8 -*-
from odoo import models, fields

class XTempTpInvoiceLineGap(models.Model):
    _inherit = 'x_temp_tp_invoice_line'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
