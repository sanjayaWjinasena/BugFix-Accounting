import datetime

from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    account_mandatory = fields.Boolean(string="Account Mandatory")
    advance_acc_updated = fields.Boolean(string="Advance ACC Updated")
    bank_guarantee_approved = fields.Boolean(
        string="Bank Guarantee Approved",
        readonly=True,
        related="sale_id.bank_guarantee_approved",
        store=True,
    )
    bank_guarantee_notification = fields.Boolean(
        string="Bank Guarantee Notification",
        readonly=True,
        compute="_compute_bank_guarantee_notification",
        store=True,
    )
    bank_guarantee_validation = fields.Boolean(
        string="Bank Guarantee Validation",
        readonly=True,
        compute="_compute_bank_guarantee_validation",
        store=True,
    )
    bg_sent = fields.Boolean(string="BG Sent")
    consignment_no = fields.Many2one(
        "consignment_header", string="Consignment No"
    )
    # v0.0.129 recovery — declared here as plain M2O so account.payment
    # can relate to them via move_id.X. On CDB these existed only as
    # state='manual' on account.move; the v0.0.113 orphan filter skipped
    # them but audit v129 showed they have 100+ view refs so users need
    # them functional. store=True except created_from_pr_no
    # which targets a BugFix-Purchase-owned comodel (downstream, needs
    # store=False to avoid _auto_init cycle at Accounting load time).
    co = fields.Many2one("consignment_header", string="Co")
    create_from_transfer = fields.Many2one(
        "stock.picking", string="Create From Transfer"
    )
    # v0.0.143: created_from_pr_no, cre and
    # created_from_npo_no MOVED to BugFix-Purchase (models/account_move.py).
    # Their comodels (po_non_inventory, purchase_request_cas) are owned by
    # BugFix-Purchase, downstream of this module -> sticky `_unknown` here.
    create_from_transfer_1 = fields.Many2one(
        "stock.picking", string="Create From Transfer"
    )
    created_from_consignment = fields.Many2one(
        "consignment_header", string="Created From Consignment"
    )
    created_from_consignment_1 = fields.Many2one(
        "consignment_header", string="Created From Consignment"
    )
    created_from_project = fields.Boolean(string="Created From Project")
    created_from_project_no = fields.Many2one(
        "project.project", string="Created From Project No"
    )
    created_from_transfer = fields.Many2one(
        "stock.picking", string="Created From Transfer"
    )
    created_from_vendor_bill = fields.Many2one(
        "account.move", string="Created From Vendor Bill"
    )
    created_from_vendor_bill_1 = fields.Many2one(
        "account.move", string="Created From Vendor Bill"
    )
    credit_limit_approved = fields.Boolean(
        string="Credit Limit Approved",
        readonly=True,
        related="sale_id.credit_limit_approved",
        store=True,
    )
    credit_limit_validation = fields.Boolean(
        string="Credit Limit Validation",
        readonly=True,
        compute="_compute_credit_limit_validation",
        store=True,
    )
    credit_note_approved = fields.Boolean(string="Credit Note Approved")
    credit_note_request_sent = fields.Boolean(
        string="Credit Note Request Sent"
    )
    currency_rate = fields.Float(string="Currency Rate")
    currency_rate_updated = fields.Boolean(string="Currency Rate Updated")
    custom_clearance_no = fields.Char(
        string="Custom Clearance No",
        readonly=True,
        related="consignment_no.custom_clearance_no",
        store=True,
    )
    journal_type = fields.Selection(
        [("Bill", "Bill"), ("Payment", "Payment"), ("Settlement", "Settlement")],
        string="Journal Type",
    )
    lc_no = fields.Many2one("lc_header", string="LC No")
    # Would be related='purchase_id.lc' per CDB, but lc
    # is declared in BugFix-Purchase which loads AFTER BugFix-Accounting.
    # Related setup crashes at class construction (setup_related runs BEFORE
    # _auto_init and store=False does NOT rescue this). Convert to computed
    # with runtime hasattr() guard. Fires on purchase_id change.
    lc_test1 = fields.Boolean(
        string="LC - test1",
        readonly=True,
        compute="_compute_lc_test1",
        store=True,
    )
    order_payment_method = fields.Selection(
        string="Order Payment Method",
        readonly=True,
        related="sale_id.order_payment_method",
        store=True,
    )
    over_bank_guarantee = fields.Boolean(
        string="Over Bank Guarantee",
        readonly=True,
        related="sale_id.over_bank_guarantee",
        store=True,
    )
    project_no = fields.Many2one("project.project", string="Project No")
    project_no_bill = fields.Many2one(
        "project.project", string="Project No Bill"
    )
    project_no_issue = fields.Many2one(
        "project.project", string="Project No Issue"
    )
    project_no_settle = fields.Many2one(
        "project.project", string="Project No Settle"
    )
    accounting_purchase_id = fields.Many2one("purchase.order", string="Purchase Order")
    # Same load-order trap as lc_test1 above - pr_type
    # on purchase.order is a BugFix-Purchase-added field. Use compute
    # with runtime guard instead of related.
    purchase_type = fields.Selection(
        [("Local", "Local"), ("Import", "Import")],
        string="PR Type",
        readonly=True,
        compute="_compute_purchase_type",
        store=True,
    )
    report_type_s_cust_aging = fields.Many2one(
        "sales_report_type", string="Report Type (S - Cust Aging)"
    )
    rug_acc_updated = fields.Boolean(string="RUG Account Updated")
    rug_confirmed = fields.Boolean(
        string="RUG Confirmed",
        readonly=True,
        related="sale_id.rug_confirmed",
        store=True,
    )
    rug_rejected = fields.Boolean(
        string="RUG Rejected",
        readonly=True,
        related="sale_id.rug_rejected",
        store=True,
    )
    sale_id = fields.Many2one("sale.order", string="Sale_Id")
    supplier_invoice_number = fields.Char(
        string="XXX Supplier's Invoice Number (Bill Reference)"
    )
    test_type = fields.Selection(
        [("One", "One"), ("Two", "Two")], string="Test Type"
    )
    tp_id = fields.Many2one(
        "tp_invoice_header", string="Created From TP Invoice"
    )
    type = fields.Selection(
        [("General", "General"), ("Advance Payment", "Advance Payment")], string="Type"
    )
    update_consignment = fields.Boolean(string="Update Consignment")
    valid_lines = fields.Boolean(
        string="Valid Lines",
        readonly=True,
        store=False,
        compute="_compute_valid_lines",
    )
    created_from_vendor_bill_1__account_move_count = fields.Integer(
        string="Created From Vendor Bill count",
        store=False,
        compute="_compute_vendor_bill_1_count",
    )
    created_from_vendor_bill__account_move_count = fields.Integer(
        string="Created From Vendor Bill count",
        store=False,
        compute="_compute_vendor_bill_count",
    )

    # ------------------------------------------------------------------
    # Computed fields (ported from CDB Studio compute code)
    # ------------------------------------------------------------------

    @api.depends(
        "partner_id", "amount_total", "bank_guarantee_approved", "move_type"
    )
    def _compute_bank_guarantee_notification(self):
        today = datetime.date.today()
        for record in self:
            notification = False
            if not record.bank_guarantee_approved:
                p = record.partner_id
                if (
                    p
                    and (p.customer_rank or 0) > 0
                    and record.move_type == "out_invoice"
                ):
                    cg = getattr(p, "customer_group", False)
                    group_type = (
                        getattr(cg, "group_type", None) if cg else None
                    )
                    if group_type and group_type != "General":
                        mandatory = getattr(p, "mandatory_bank_guarantee", False)
                        expiry = getattr(p, "expiry_date", None)
                        bg_amount = getattr(p, "bank_guarantee_amount", 0) or 0
                        exposure = (p.credit or 0) + (record.amount_total or 0)
                        expired = expiry and expiry < today
                        if not mandatory:
                            if expired:
                                notification = True
                            elif bg_amount < exposure:
                                notification = True
            record.bank_guarantee_notification = notification

    @api.depends(
        "partner_id", "amount_total", "bank_guarantee_approved", "move_type"
    )
    def _compute_bank_guarantee_validation(self):
        today = datetime.date.today()
        for record in self:
            validation = False
            if not record.bank_guarantee_approved:
                p = record.partner_id
                if (
                    p
                    and (p.customer_rank or 0) > 0
                    and record.move_type == "out_invoice"
                ):
                    cg = getattr(p, "customer_group", False)
                    group_type = (
                        getattr(cg, "group_type", None) if cg else None
                    )
                    if group_type and group_type != "General":
                        mandatory = getattr(p, "mandatory_bank_guarantee", False)
                        expiry = getattr(p, "expiry_date", None)
                        bg_amount = getattr(p, "bank_guarantee_amount", 0) or 0
                        exposure = (p.credit or 0) + (record.amount_total or 0)
                        expired = expiry and expiry < today
                        if mandatory:
                            if expired:
                                validation = True
                            elif bg_amount < exposure:
                                validation = True
            record.bank_guarantee_validation = validation

    @api.depends(
        "partner_id",
        "partner_id.credit",
        "partner_id.credit_limit",
        "amount_total",
        "order_payment_method",
        "credit_limit_approved",
    )
    def _compute_credit_limit_validation(self):
        for record in self:
            valid = False
            if not record.credit_limit_approved:
                p = record.partner_id
                if p and record.order_payment_method == "Credit":
                    valid = ((p.credit or 0) + (record.amount_total or 0)) > (
                        p.credit_limit or 0
                    )
            record.credit_limit_validation = valid

    @api.depends(
        "invoice_line_ids",
        "invoice_line_ids.price_unit",
        "invoice_line_ids.display_type",
    )
    def _compute_valid_lines(self):
        for rec in self:
            has_zero_price = False
            count = 0
            for line in rec.invoice_line_ids:
                count += 1
                if not line.display_type and line.price_unit == 0:
                    has_zero_price = True
            rec.valid_lines = has_zero_price if count > 0 else True

    @api.depends("purchase_id")
    def _compute_lc_test1(self):
        # Runtime guard: lc is on purchase.order but declared by
        # BugFix-Purchase which loads AFTER BugFix-Accounting. Can't use
        # related= at model class setup - use hasattr at compute-time
        # instead. Reactivity: fires on purchase_id assignment/change; does
        # NOT fire when the downstream lc value changes on the
        # same PO (would need @api.depends('purchase_id.lc') which
        # crashes at setup for same reason).
        for rec in self:
            po = rec.purchase_id
            if po and "lc" in po._fields:
                rec.lc_test1 = bool(po.lc)
            else:
                rec.lc_test1 = False

    @api.depends("accounting_purchase_id")
    def _compute_purchase_type(self):
        # Same load-order guard as _compute_lc_test1.
        for rec in self:
            po = rec.accounting_purchase_id
            if po and "pr_type" in po._fields:
                rec.purchase_type = po.pr_type or False
            else:
                rec.purchase_type = False

    def _compute_vendor_bill_count(self):
        for rec in self:
            rec.created_from_vendor_bill__account_move_count = self.env[
                "account.move"
            ].search_count([("created_from_vendor_bill", "=", rec.id)])

    def _compute_vendor_bill_1_count(self):
        for rec in self:
            rec.created_from_vendor_bill_1__account_move_count = self.env[
                "account.move"
            ].search_count([("created_from_vendor_bill_1", "=", rec.id)])
