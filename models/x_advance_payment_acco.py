# -*- coding: utf-8 -*-
from odoo import fields, models


class XAdvancePaymentAcco(models.Model):
    """Studio-ported custom model x_advance_payment_acco."""
    _name = 'x_advance_payment_acco'
    _description = 'Advance Payment Acco'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_advance_account_project = fields.Many2one('account.account', string='Advance Account (Project)')
    x_studio_advance_payment_account_purchases = fields.Many2one('account.account', string='Account')
    x_studio_advance_payment_account_purchases_1 = fields.Many2one('account.account', string='Advance Payment Account (Purchases)')
    x_studio_advance_payment_account_sales = fields.Many2one('account.account', string='Advance Payment Account (Sales)')
    x_studio_sequence = fields.Integer(string='Sequence')
