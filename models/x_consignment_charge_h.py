# -*- coding: utf-8 -*-
"""Sentinel declaration for x_consignment_charge_h so cross-references resolve."""
from odoo import fields, models


# NOTE (v0.0.143): the Many2one(s) x_studio_structure_details_line_ids / x_studio_structure_master_id were MOVED to BugFix-Purchase v0.1.0.178.
# Their comodel is owned by a DOWNSTREAM module; declared here they were
# `_unknown` for the whole upgrade-mode registry build (see BugFix-Purchase
# models/upstream_link_fields.py). Do NOT re-add them here.

class XConsignmentChargeH(models.Model):
    _name = 'x_consignment_charge_h'
    _description = 'Consignment Charge Header'

    _inherit = ['mail.thread', 'mail.activity.mixin']
    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_allocate_header_charges = fields.Boolean(string='Allocate Header Charges')
    x_studio_amount = fields.Float(string='Amount')
    x_studio_basis = fields.Selection([('Percentage', 'Percentage'), ('Fixed Per Document', 'Fixed Per Document')], string='Basis')
    x_studio_charge_group = fields.Selection([('None', 'None'), ('Charges', 'Charges'), ('Duty', 'Duty'), ('Taxes', 'Taxes')], string='Charge Group')
    x_studio_charge_name = fields.Char(string='Charge Name')
    x_studio_company_id = fields.Many2one('res.company', string='Company')
    x_studio_consignment_id = fields.Many2one('x_consignment_header', string='Consignment Id')
    x_studio_formula = fields.Char(string='Formula')
    x_studio_ledger_post = fields.Boolean(string='Ledger Post')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_structure_no = fields.Integer(string='Structure No')
    x_studio_tax_appicable = fields.Boolean(string='Tax Applicable')
    x_studio_tax_appicable2 = fields.Boolean(string='Tax Applicable2')
    x_studio_tp_processed = fields.Boolean(string='TP Processed')
