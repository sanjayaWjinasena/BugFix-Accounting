# -*- coding: utf-8 -*-
from odoo import fields, models


class XCustomerPostingPro(models.Model):
    """Studio-ported custom model x_customer_posting_pro."""
    _name = 'x_customer_posting_pro'
    _description = 'Customer Posting Pro'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Customer Posting Profile')
    x_studio_item_relation_type = fields.Selection([], string='Item Relation Type')
    x_studio_many2one_field_eYVbe = fields.Many2one('product.product', string='Product')
    x_studio_notes = fields.Text(string='Notes')
    x_studio_sequence = fields.Integer(string='Sequence')
