# -*- coding: utf-8 -*-
from odoo import fields, models


# NOTE (v0.0.143): the Many2one(s) x_studio_cre / x_studio_created_from_npo_no / x_studio_created_from_pr_no /
#   x_studio_many2one_field_4CPvU / x_studio_many2one_field_rpsBC were MOVED to BugFix-Purchase v0.1.0.178.
# Their comodel is owned by a DOWNSTREAM module; declared here they were
# `_unknown` for the whole upgrade-mode registry build (see BugFix-Purchase
# models/upstream_link_fields.py). Do NOT re-add them here.

# v0.0.148: fields that exist on account.move are NOT declared here. account.bank.statement.line
#   _inherits account.move, so Odoo adds them automatically as related='move_id.<name>' (as on
#   Clear-DB). Declaring them here replaced that link with an always-empty plain field.

class AccountBankStatementLine(models.Model):
    _inherit = 'account.bank.statement.line'

    x_studio_boolean_field_A32jc = fields.Boolean(string='New Checkbox', store=False)
    x_studio_boolean_field_E4oM7 = fields.Boolean(string='New Checkbox', store=False)
    x_studio_boolean_field_EoMg9 = fields.Boolean(string='New Checkbox', store=False)
    x_studio_boolean_field_MVlhn = fields.Boolean(string='New Checkbox', store=False)
    x_studio_boolean_field_RIlaO = fields.Boolean(string='New Checkbox', store=False)
    x_studio_boolean_field_XzV6D = fields.Boolean(string='New Checkbox', store=False)
    x_studio_boolean_field_bnVim = fields.Boolean(string='New Checkbox', store=False)
    x_studio_boolean_field_djczB = fields.Boolean(string='New Checkbox', store=False)
    x_studio_boolean_field_qcQya = fields.Boolean(string='New Checkbox', store=False)
    x_studio_boolean_field_xNbhc = fields.Boolean(string='New Checkbox', store=False)
    x_studio_boolean_field_xud0H = fields.Boolean(string='New Checkbox', store=False)
    x_studio_boolean_field_ydmJ5 = fields.Boolean(string='New Checkbox', store=False)
    x_studio_boolean_field_ygnit = fields.Boolean(string='New Checkbox', store=False)
    x_studio_char_field_FnRNH = fields.Char(string='New Text', store=False)
    x_studio_co = fields.Many2one('x_consignment_header', string='Co', store=False)
    x_studio_create_from_transfer = fields.Many2one('stock.picking', string='Create From Transfer', store=False)
    x_studio_created_from_consignment_2 = fields.Many2one('x_consignment_header', string='Created From Consignment 2', store=False)
    x_studio_created_from_tp_invoice = fields.Many2one('x_tp_invoice_header', string='Created From TP Invoice', store=False)
    x_studio_created_transfer = fields.Many2one('stock.picking', string='Created Transfer', store=False)
    x_studio_float_field_5tma1 = fields.Float(string='New Decimal', store=False)
    x_studio_many2one_field_6HjHy = fields.Many2one('account.move', string='Journal Entry', store=False)
    x_studio_many2one_field_6Sjmv = fields.Many2one('stock.picking', string='Transfer', store=False)
    x_studio_many2one_field_A197A = fields.Many2one('x_consignment_header', string='Consignment Header', store=False)
    x_studio_many2one_field_B4ibh = fields.Many2one('project.project', string='Project', store=False)
    x_studio_many2one_field_KKFaY = fields.Many2one('x_tp_invoice_header', string='TP Invoice Header', store=False)
    x_studio_many2one_field_L9MIu = fields.Many2one('x_sales_report_type', string='Sales Report Type', store=False)
    x_studio_many2one_field_P4o2n = fields.Many2one('project.project', string='Project', store=False)
    x_studio_many2one_field_PJkjM = fields.Many2one('x_lc_header', string='LC Header', store=False)
    x_studio_many2one_field_R46Ke = fields.Many2one('project.project', string='Project', store=False)
    x_studio_many2one_field_TEK9K = fields.Many2one('stock.picking', string='Transfer', store=False)
    x_studio_many2one_field_XhwuI = fields.Many2one('purchase.order', string='Purchase Order', store=False)
    x_studio_many2one_field_aIXMs = fields.Many2one('x_tp_invoice_header', string='TP Invoice Header', store=False)
    x_studio_many2one_field_ffAE3 = fields.Many2one('account.move', string='Journal Entry', store=False)
    x_studio_many2one_field_jslCp = fields.Many2one('x_consignment_header', string='Consignment Header', store=False)
    x_studio_many2one_field_mULOh = fields.Many2one('account.move', string='Journal Entry', store=False)
    x_studio_many2one_field_mucWu = fields.Many2one('x_consignment_header', string='Consignment Header', store=False)
    x_studio_many2one_field_re1H2 = fields.Many2one('sale.order', string='Sales Order', store=False)
    x_studio_many2one_field_tpCkS = fields.Many2one('project.project', string='Project', store=False)
    x_studio_many2one_field_vAeTQ = fields.Many2one('project.project', string='Project', store=False)
    x_studio_many2one_field_xkSx5 = fields.Many2one('account.move', string='Journal Entry', store=False)
    x_studio_project_no_1 = fields.Many2one('project.project', string='Project No', store=False)
    x_studio_project_no_settle_1 = fields.Many2one('project.project', string='Project No Settle', store=False)
    x_studio_related_field_1JsOz = fields.Boolean(string='New Related Field', readonly=True, store=False)
    x_studio_related_field_7SPn1 = fields.Boolean(string='New Related Field', readonly=True, store=False)
    x_studio_related_field_DBwI2 = fields.Selection([], string='New Related Field', readonly=True, store=False)
    x_studio_related_field_QgLxV = fields.Boolean(string='New Related Field', readonly=True, store=False)
    x_studio_related_field_T4rIR = fields.Selection([], string='New Related Field', readonly=True, store=False)
    x_studio_related_field_VMbnh = fields.Boolean(string='New Related Field', readonly=True, store=False)
    x_studio_related_field_bRYM3 = fields.Selection([], string='New Related Field', readonly=True, store=False)
    x_studio_related_field_m4xKC = fields.Selection([], string='New Related Field', readonly=True, store=False)
    x_studio_related_field_nIq3I = fields.Selection([], string='New Related Field', readonly=True, store=False)
    x_studio_related_field_nQx1u = fields.Boolean(string='New Related Field', readonly=True, store=False)
    x_studio_related_field_pSJXo = fields.Char(string='New Related Field', readonly=True, store=False)
    x_studio_related_field_v5UEx = fields.Boolean(string='New Related Field', readonly=True, store=False)
    x_studio_related_field_w1zkr = fields.Selection([], string='New Related Field', readonly=True, store=False)
    x_studio_related_field_yj3hQ = fields.Selection([], string='New Related Field', readonly=True, store=False)
    x_studio_selection_field_5Gimk = fields.Selection([], string='New Selection', store=False)
    x_studio_selection_field_KlNrV = fields.Selection([], string='New Selection', store=False)
    x_studio_selection_field_N6ihz = fields.Selection([], string='New Selection', store=False)
