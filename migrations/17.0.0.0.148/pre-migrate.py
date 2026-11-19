# -*- coding: utf-8 -*-
"""v0.0.148: detach this module's ir.model.data pointers for account.bank.statement.line fields
that are no longer declared here.

account.bank.statement.line _inherits account.move, so these fields now come from account.move as
related='move_id.<name>' (as on Clear-DB). Without this step, ir.model.data._process_end would
treat the ir.model.fields rows as stale (their xmlid was not re-loaded) and unlink them at the end
of the upgrade although the fields still exist. Only the pointer rows are removed, never the fields.
ORM only; no-op on fresh installs and when the rows are already gone.
"""
import logging

from odoo import api, SUPERUSER_ID

_logger = logging.getLogger(__name__)

MODULE = 'BugFix-Accounting'
FIELDS = (
    'x_studio_account_mandatory',
    'x_studio_advance_acc_updated',
    'x_studio_bank_guarantee_approved',
    'x_studio_bank_guarantee_notification',
    'x_studio_bank_guarantee_validation',
    'x_studio_bg_sent',
    'x_studio_consignment_no',
    'x_studio_create_from_transfer_1',
    'x_studio_created_from_consignment',
    'x_studio_created_from_consignment_1',
    'x_studio_created_from_project',
    'x_studio_created_from_project_no',
    'x_studio_created_from_transfer',
    'x_studio_created_from_vendor_bill',
    'x_studio_created_from_vendor_bill_1',
    'x_studio_credit_limit_approved',
    'x_studio_credit_limit_validation',
    'x_studio_credit_note_approved',
    'x_studio_credit_note_request_sent',
    'x_studio_currency_rate',
    'x_studio_currency_rate_updated',
    'x_studio_custom_clearance_no',
    'x_studio_journal_type',
    'x_studio_lc_no',
    'x_studio_lc_test1',
    'x_studio_order_payment_method',
    'x_studio_over_bank_guarantee',
    'x_studio_project_no',
    'x_studio_project_no_bill',
    'x_studio_project_no_issue',
    'x_studio_project_no_settle',
    'x_studio_purchase_id',
    'x_studio_purchase_type',
    'x_studio_report_type_s_cust_aging',
    'x_studio_rug_acc_updated',
    'x_studio_rug_confirmed',
    'x_studio_rug_rejected',
    'x_studio_sale_id',
    'x_studio_supplier_invoice_number',
    'x_studio_test_type',
    'x_studio_tp_id',
    'x_studio_type',
    'x_studio_update_consignment',
    'x_studio_valid_lines',
    'x_x_studio_created_from_vendor_bill_1__account_move_count',
    'x_x_studio_created_from_vendor_bill__account_move_count',
)


def migrate(cr, version):
    if not version:
        return
    env = api.Environment(cr, SUPERUSER_ID, {})
    xmlids = ['field_account_bank_statement_line__%s' % name for name in FIELDS]
    imd = env['ir.model.data'].sudo().search([
        ('module', '=', MODULE),
        ('model', '=', 'ir.model.fields'),
        ('name', 'in', xmlids),
    ])
    if imd:
        count = len(imd)
        imd.unlink()
        _logger.info("%s v0.0.148: detached %d statement-line field pointer(s)", MODULE, count)
