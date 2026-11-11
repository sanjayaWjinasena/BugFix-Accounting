from odoo import api, fields, models

# NOTE (v0.0.143): the Many2one(s) cre / created_from_npo_no /
# created_from_pr_no (related
# mirrors of account.move) / many2one_field_4CPvU /
# many2one_field_rpsBC were MOVED to BugFix-Purchase v0.1.0.178.
# Their comodel is owned by a DOWNSTREAM module; declared here they were
# `_unknown` for the whole upgrade-mode registry build (see BugFix-Purchase
# models/upstream_link_fields.py). Do NOT re-add them here.


class AccountPayment(models.Model):
    _inherit = "account.payment"

    account_mandatory = fields.Boolean(
        string="Account Mandatory",
        related="move_id.account_mandatory",
        store=True,
        readonly=True,
    )
    advance_acc_updated = fields.Boolean(
        string="Advance ACC Updated",
        related="move_id.advance_acc_updated",
        store=True,
        readonly=True,
    )
    advance_payment_acc_updated = fields.Boolean(string="Advance Payment ACC Updated")
    bank_guarantee_approved = fields.Boolean(
        string="Bank Guarantee Approved",
        related="move_id.bank_guarantee_approved",
        store=True,
        readonly=True,
    )
    bank_guarantee_notification = fields.Boolean(
        string="Bank Guarantee Notification",
        related="move_id.bank_guarantee_notification",
        store=True,
        readonly=True,
    )
    bank_guarantee_validation = fields.Boolean(
        string="Bank Guarantee Validation",
        related="move_id.bank_guarantee_validation",
        store=True,
        readonly=True,
    )
    bg_sent = fields.Boolean(
        string="BG Sent", related="move_id.bg_sent", store=True, readonly=True
    )
    boolean_field_A32jc = fields.Boolean(string="New Checkbox", store=False)
    boolean_field_E4oM7 = fields.Boolean(string="New Checkbox", store=False)
    boolean_field_EoMg9 = fields.Boolean(string="New Checkbox", store=False)
    boolean_field_MVlhn = fields.Boolean(string="New Checkbox", store=False)
    boolean_field_RIlaO = fields.Boolean(string="New Checkbox", store=False)
    boolean_field_XzV6D = fields.Boolean(string="New Checkbox", store=False)
    boolean_field_bnVim = fields.Boolean(string="New Checkbox", store=False)
    boolean_field_djczB = fields.Boolean(string="New Checkbox", store=False)
    boolean_field_qcQya = fields.Boolean(string="New Checkbox", store=False)
    boolean_field_xNbhc = fields.Boolean(string="New Checkbox", store=False)
    boolean_field_xud0H = fields.Boolean(string="New Checkbox", store=False)
    boolean_field_ydmJ5 = fields.Boolean(string="New Checkbox", store=False)
    boolean_field_ygnit = fields.Boolean(string="New Checkbox", store=False)
    char_field_FnRNH = fields.Char(string="New Text", store=False)
    co = fields.Many2one(
        "consignment_header",
        string="Co",
        store=False,
        related="move_id.co",
        readonly=True,
    )
    consignment_no = fields.Many2one(
        "consignment_header",
        string="Consignment No",
        related="move_id.consignment_no",
        store=True,
        readonly=True,
    )
    create_from_transfer = fields.Many2one(
        "stock.picking",
        string="Create From Transfer",
        store=False,
        related="move_id.create_from_transfer",
        readonly=True,
    )
    create_from_transfer_1 = fields.Many2one(
        "stock.picking",
        string="Create From Transfer",
        related="move_id.create_from_transfer_1",
        store=True,
        readonly=True,
    )
    created_from_consignment = fields.Many2one(
        "consignment_header",
        string="Created From Consignment",
        related="move_id.created_from_consignment",
        store=True,
        readonly=True,
    )
    created_from_consignment_1 = fields.Many2one(
        "consignment_header",
        string="Created From Consignment",
        related="move_id.created_from_consignment_1",
        store=True,
        readonly=True,
    )
    created_from_consignment_2 = fields.Many2one("consignment_header", store=False)
    created_from_project = fields.Boolean(
        string="Created From Project",
        related="move_id.created_from_project",
        store=True,
        readonly=True,
    )
    created_from_project_1 = fields.Boolean(string="Created From Project")
    created_from_project_no = fields.Many2one(
        "project.project",
        string="Created From Project No",
        related="move_id.created_from_project_no",
        store=True,
        readonly=True,
    )
    created_from_tp_invoice = fields.Many2one(
        "tp_invoice_header", string="Created From TP Invoice", store=False
    )
    created_from_transfer = fields.Many2one(
        "stock.picking",
        string="Created From Transfer",
        related="move_id.created_from_transfer",
        store=True,
        readonly=True,
    )
    created_from_vendor_bill = fields.Many2one(
        "account.move",
        string="Created From Vendor Bill",
        related="move_id.created_from_vendor_bill",
        store=False,
        readonly=True,
    )
    created_from_vendor_bill_1 = fields.Many2one(
        "account.move",
        string="Created From Vendor Bill",
        related="move_id.created_from_vendor_bill_1",
        store=False,
        readonly=True,
    )
    created_transfer = fields.Many2one("stock.picking", store=False)
    credit_limit_approved = fields.Boolean(
        string="Credit Limit Approved",
        related="move_id.credit_limit_approved",
        store=True,
        readonly=True,
    )
    credit_limit_validation = fields.Boolean(
        string="Credit Limit Validation",
        related="move_id.credit_limit_validation",
        store=True,
        readonly=True,
    )
    credit_note_approved = fields.Boolean(
        string="Credit Note Approved",
        related="move_id.credit_note_approved",
        store=True,
        readonly=True,
    )
    credit_note_request_sent = fields.Boolean(
        string="Credit Note Request Sent",
        related="move_id.credit_note_request_sent",
        store=True,
        readonly=True,
    )
    currency_rate = fields.Float(
        string="Currency Rate",
        related="move_id.currency_rate",
        store=True,
        readonly=True,
    )
    currency_rate_updated = fields.Boolean(
        string="Currency Rate Updated",
        related="move_id.currency_rate_updated",
        store=True,
        readonly=True,
    )
    custom_clearance_no = fields.Char(
        string="Custom Clearance No",
        related="move_id.custom_clearance_no",
        store=True,
        readonly=True,
    )
    float_field_5tma1 = fields.Float(string="New Decimal", store=False)
    journal_type = fields.Selection(
        string="Journal Type",
        related="move_id.journal_type",
        store=True,
        readonly=True,
    )
    lc_no = fields.Many2one(
        "lc_header",
        string="LC No",
        related="move_id.lc_no",
        store=True,
        readonly=True,
    )
    lc_no_1 = fields.Many2one("lc_header", string="LC No")
    lc_test1 = fields.Boolean(
        string="LC - test1",
        related="move_id.lc_test1",
        store=True,
        readonly=True,
    )
    many2one_field_6HjHy = fields.Many2one(
        "account.move", string="Journal Entry", store=False
    )
    many2one_field_6Sjmv = fields.Many2one(
        "stock.picking", string="Transfer", store=False
    )
    many2one_field_A197A = fields.Many2one(
        "consignment_header", string="Consignment Header", store=False
    )
    many2one_field_B4ibh = fields.Many2one(
        "project.project", string="Project", store=False
    )
    many2one_field_KKFaY = fields.Many2one(
        "tp_invoice_header", string="TP Invoice Header", store=False
    )
    many2one_field_L9MIu = fields.Many2one(
        "sales_report_type", string="Sales Report Type", store=False
    )
    many2one_field_P4o2n = fields.Many2one(
        "project.project", string="Project", store=False
    )
    many2one_field_PJkjM = fields.Many2one("lc_header", string="LC Header", store=False)
    many2one_field_R46Ke = fields.Many2one(
        "project.project", string="Project", store=False
    )
    many2one_field_TEK9K = fields.Many2one(
        "stock.picking", string="Transfer", store=False
    )
    many2one_field_XhwuI = fields.Many2one(
        "purchase.order", string="Purchase Order", store=False
    )
    many2one_field_aIXMs = fields.Many2one(
        "tp_invoice_header", string="TP Invoice Header", store=False
    )
    many2one_field_ffAE3 = fields.Many2one(
        "account.move", string="Journal Entry", store=False
    )
    many2one_field_jslCp = fields.Many2one(
        "consignment_header", string="Consignment Header", store=False
    )
    many2one_field_mULOh = fields.Many2one(
        "account.move", string="Journal Entry", store=False
    )
    many2one_field_mucWu = fields.Many2one(
        "consignment_header", string="Consignment Header", store=False
    )
    many2one_field_re1H2 = fields.Many2one(
        "sale.order", string="Sales Order", store=False
    )
    many2one_field_tpCkS = fields.Many2one(
        "project.project", string="Project", store=False
    )
    many2one_field_vAeTQ = fields.Many2one(
        "project.project", string="Project", store=False
    )
    many2one_field_xkSx5 = fields.Many2one(
        "account.move", string="Journal Entry", store=False
    )
    order_payment_method = fields.Selection(
        string="Order Payment Method",
        related="move_id.order_payment_method",
        store=True,
        readonly=True,
    )
    over_bank_guarantee = fields.Boolean(
        string="Over Bank Guarantee",
        related="move_id.over_bank_guarantee",
        store=True,
        readonly=True,
    )
    payment_validation = fields.Boolean(
        compute="_compute_payment_validation",
        store=True,
        readonly=True,
    )
    payment_validation_1 = fields.Char(string="Payment Validation")
    project_no = fields.Many2one(
        "project.project",
        string="Project No",
        related="move_id.project_no",
        store=True,
        readonly=True,
    )
    project_no_1 = fields.Many2one("project.project", string="Project No")
    project_no_bill = fields.Many2one(
        "project.project",
        string="Project No Bill",
        related="move_id.project_no_bill",
        store=True,
        readonly=True,
    )
    project_no_issue = fields.Many2one(
        "project.project",
        string="Project No Issue",
        related="move_id.project_no_issue",
        store=True,
        readonly=True,
    )
    project_no_settle = fields.Many2one(
        "project.project",
        string="Project No Settle",
        related="move_id.project_no_settle",
        store=True,
        readonly=True,
    )
    project_no_settle_1 = fields.Many2one(
        "project.project", string="Project No Settle", store=False
    )
    accounting_purchase_id = fields.Many2one(
        "purchase.order",
        string="Purchase Order",
        related="move_id.accounting_purchase_id",
        store=False,
        readonly=True,
    )
    purchase_order = fields.Many2one("purchase.order")
    purchase_type = fields.Selection(
        string="PR Type",
        related="move_id.purchase_type",
        store=True,
        readonly=True,
    )
    quotation_type = fields.Selection(
        [("Sales", "Sales"), ("Project", "Project"), ("Repair", "Repair")],
    )
    related_field_1JsOz = fields.Boolean(
        string="New Related Field", readonly=True, store=False
    )
    related_field_7SPn1 = fields.Boolean(
        string="New Related Field", readonly=True, store=False
    )
    related_field_DBwI2 = fields.Selection(
        [], string="New Related Field", readonly=True, store=False
    )
    related_field_QgLxV = fields.Boolean(
        string="New Related Field", readonly=True, store=False
    )
    related_field_T4rIR = fields.Selection(
        [], string="New Related Field", readonly=True, store=False
    )
    related_field_VMbnh = fields.Boolean(
        string="New Related Field", readonly=True, store=False
    )
    related_field_bRYM3 = fields.Selection(
        [], string="New Related Field", readonly=True, store=False
    )
    related_field_m4xKC = fields.Selection(
        [], string="New Related Field", readonly=True, store=False
    )
    related_field_nIq3I = fields.Selection(
        [], string="New Related Field", readonly=True, store=False
    )
    related_field_nQx1u = fields.Boolean(
        string="New Related Field", readonly=True, store=False
    )
    related_field_pSJXo = fields.Char(
        string="New Related Field", readonly=True, store=False
    )
    related_field_v5UEx = fields.Boolean(
        string="New Related Field", readonly=True, store=False
    )
    related_field_w1zkr = fields.Selection(
        [], string="New Related Field", readonly=True, store=False
    )
    related_field_yj3hQ = fields.Selection(
        [], string="New Related Field", readonly=True, store=False
    )
    report_type_s_cust_aging = fields.Many2one(
        "sales_report_type",
        string="Report Type (S - Cust Aging)",
        related="move_id.report_type_s_cust_aging",
        store=False,
        readonly=True,
    )
    rug_acc_updated = fields.Boolean(
        string="RUG Account Updated",
        related="move_id.rug_acc_updated",
        store=True,
        readonly=True,
    )
    rug_confirmed = fields.Boolean(
        string="RUG Confirmed",
        related="move_id.rug_confirmed",
        store=True,
        readonly=True,
    )
    rug_rejected = fields.Boolean(
        string="RUG Rejected",
        related="move_id.rug_rejected",
        store=True,
        readonly=True,
    )
    sale_id = fields.Many2one(
        "sale.order",
        string="Sale_Id",
        related="move_id.sale_id",
        store=False,
        readonly=True,
    )
    sales_order = fields.Many2one("sale.order")
    selection_field_5Gimk = fields.Selection([], string="New Selection", store=False)
    selection_field_KlNrV = fields.Selection([], string="New Selection", store=False)
    selection_field_N6ihz = fields.Selection([], string="New Selection", store=False)
    supplier_invoice_number = fields.Char(
        string="XXX Supplier's Invoice Number (Bill Reference)",
        related="move_id.supplier_invoice_number",
        store=True,
        readonly=True,
    )
    test_type = fields.Selection(
        string="Test Type",
        related="move_id.test_type",
        store=True,
        readonly=True,
    )
    tp_id = fields.Many2one(
        "tp_invoice_header",
        string="Created From TP Invoice",
        related="move_id.tp_id",
        store=True,
        readonly=True,
    )
    tp_invoice_no = fields.Many2one("tp_invoice_header", string="TP Invoice No")
    type = fields.Selection(
        [("General", "General"), ("Advance Payment", "Advance Payment")]
    )
    update_consignment = fields.Boolean(
        string="Update Consignment",
        related="move_id.update_consignment",
        store=True,
        readonly=True,
    )
    valid_lines = fields.Boolean(
        string="Valid Lines",
        related="move_id.valid_lines",
        store=True,
        readonly=True,
    )
    created_from_vendor_bill_1__account_move_count = fields.Integer(
        string="Created From Vendor Bill count",
        related="move_id.created_from_vendor_bill_1__account_move_count",
        store=True,
        readonly=True,
    )
    created_from_vendor_bill__account_move_count = fields.Integer(
        string="Created From Vendor Bill count",
        related="move_id.created_from_vendor_bill__account_move_count",
        store=True,
        readonly=True,
    )

    @api.depends("quotation_type", "sales_order", "amount")
    def _compute_payment_validation(self):
        # Ported from CDB Studio compute (bugfix_sales:config-cutover-v22).
        # Minimal semantics: True when a sales_order link exists AND amount > 0.
        for rec in self:
            has_so = bool(getattr(rec, "sales_order", False))
            rec.payment_validation = has_so and (rec.amount or 0) > 0
