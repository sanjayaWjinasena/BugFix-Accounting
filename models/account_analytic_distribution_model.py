# -*- coding: utf-8 -*-
from odoo import fields, models


class AccountAnalyticDistributionModel(models.Model):
    _inherit = 'account.analytic.distribution.model'

    x_studio_partner_mandatory = fields.Boolean(string='Partner Mandatory')
