# -*- coding: utf-8 -*-
from odoo import models, fields

class XJournalTypesGap(models.Model):
    _inherit = 'x_journal_types'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Journal Type')
