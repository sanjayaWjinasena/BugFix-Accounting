# -*- coding: utf-8 -*-
"""Ported declaration for x_journal_types (Studio custom model).

Clear-DB has this model with 6 user fields plus mail.thread +
mail.activity.mixin. Ported byte-verbatim so the pinned form view
in x_journal_types_studio_ported_v2.xml validates on fresh install.
"""
from odoo import fields, models


class XJournalTypes(models.Model):
    _name = 'x_journal_types'
    _description = 'Journal Types'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    x_active = fields.Boolean(string='Active', default=True)
    x_name = fields.Char(string='Journal Type', required=True)
    x_studio_company_id = fields.Many2one('res.company', string='Company')
    x_studio_description = fields.Char(string='Description')
    x_studio_offset_account = fields.Many2one('account.account', string='Offset Account')
    x_studio_sequence = fields.Integer(string='Sequence')
