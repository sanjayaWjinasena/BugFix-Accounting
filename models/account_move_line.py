from odoo import api, fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    aaa = fields.Char(string="AAA", readonly=True, store=False)
    account_mandatory = fields.Boolean()
    analytic_group = fields.Many2one("account.analytic.plan")
    beneficiary_id = fields.Char(
        string="Beneficiary ID",
        related="contract_id.employee_id.identification_id",
        store=True,
        readonly=True,
    )
    beneficiary_name = fields.Char(
        string="Beneficiary Name",
        related="contract_id.employee_id.name",
        store=True,
        readonly=True,
    )
    category = fields.Many2one("project_category")
    contract_id = fields.Many2one("hr.contract", string="Contract Id")
    accounting_credit_limit = fields.Float(
        string="Credit Limit",
        related="partner_id.credit_limit",
        store=True,
        readonly=True,
    )
    credit_limit_2 = fields.Float(
        compute="_compute_credit_limit_2",
        store=False,
        readonly=True,
    )
    customer_group_type = fields.Selection(
        string="Customer Group Type",
        related="partner_id.customer_group.group_type",
        store=True,
        readonly=True,
    )
    employers_contribution = fields.Float(
        string="Employer's Contribution",
        compute="_compute_employers_contribution",
        store=True,
        readonly=True,
    )
    epf_number = fields.Char(
        string="EPF Number",
        related="contract_id.employee_id.epf_no",
        store=True,
        readonly=True,
    )
    etf_number = fields.Char(
        string="ETF Number",
        related="contract_id.employee_id.etf_no",
        store=True,
        readonly=True,
    )
    initials = fields.Char(
        string="Initials",
        related="contract_id.initial",
        store=True,
        readonly=True,
    )
    accounting_invoice_date = fields.Date(
        string="Invoice Date", related="move_id.invoice_date", store=True, readonly=True
    )
    journal = fields.Many2one(
        "account.move", string="Journal", readonly=True, related="move_id", store=True
    )
    journal_type = fields.Selection(
        string="Journal Type",
        related="move_id.journal_type",
        store=True,
        readonly=True,
    )
    many2one_field_kiSUJ = fields.Many2one(
        "sales_report_type", string="Sales Report Type"
    )
    members_contribution = fields.Float(
        string="Member's Contribution",
        compute="_compute_members_contribution",
        store=True,
        readonly=True,
    )
    nic_number = fields.Char(
        string="NIC Number",
        related="contract_id.employee_id.identification_id",
        store=True,
        readonly=True,
    )
    occupation_code = fields.Char(
        string="New Related Field",
        related="contract_id.employee_id.occupation_code",
        store=True,
        readonly=True,
    )
    partner = fields.Many2one(
        "res.partner",
        string="Partner",
        related="move_id.partner_id",
        store=True,
        readonly=True,
    )
    payment_status = fields.Selection(
        string="Payment Status",
        related="move_id.payment_state",
        store=True,
        readonly=True,
    )
    pr_type = fields.Selection(
        string="PR Type",
        related="move_id.purchase_type",
        store=True,
        readonly=True,
    )
    product_category = fields.Many2one(
        "product.category",
        string="Product Category",
        related="product_id.categ_id",
        store=False,
        readonly=True,
    )
    project_no = fields.Many2one(
        "project.project",
        string="Project No",
        related="move_id.project_no",
        store=True,
        readonly=True,
    )
    purchase_order = fields.Char(
        string="Purchase Order",
        related="purchase_order_id.name",
        store=True,
        readonly=True,
    )
    purpose_code = fields.Char(
        string="Purpose Code",
        related="contract_id.employee_id.purpose_code",
        store=True,
        readonly=True,
    )
    related_field_5LBku = fields.Char(
        string="New Related Field", readonly=True, store=False
    )
    related_field_5j5_1isv2aad6 = fields.Char(
        string="New Related Field",
        related="contract_id.employee_id.occupation_code",
        store=True,
        readonly=True,
    )
    related_field_CQ41C = fields.Many2one(
        "product.product",
        string="New Related Field",
        related="product_id.product_variant_id.product_variant_id",
        store=False,
        readonly=True,
    )
    related_field_CvPMn = fields.Char(
        string="New Related Field",
        related="product_id.many2one_field_8eWzY.item_ids.price",
        store=False,
        readonly=True,
    )
    related_field_FWW4G = fields.Float(string="New Related Field", readonly=True)
    related_field_HFHrh = fields.Char(
        string="New Related Field", readonly=True, store=False
    )
    related_field_HO3gE = fields.Char(
        string="New Related Field", readonly=True, store=False
    )
    related_field_MnJZJ = fields.Char(
        string="New Related Field", readonly=True, store=False
    )
    related_field_Nf3SX = fields.Float(string="New Related Field", readonly=True)
    related_field_SORzX = fields.Integer(
        string="New Related Field",
        related="move_id.journal_id.id",
        store=True,
        readonly=True,
    )
    related_field_VzwUx = fields.Integer(
        string="New Related Field",
        related="move_id.journal_id.id",
        store=True,
        readonly=True,
    )
    related_field_WVIs6 = fields.Char(
        string="New Related Field",
        compute="_compute_related_field_WVIs6",
        store=False,
        readonly=True,
    )
    related_field_X2pdt = fields.Float(
        string="New Related Field",
        related="product_id.many2one_field_8eWzY.item_ids.fixed_price",
        store=True,
        readonly=True,
    )
    related_field_aD9tj = fields.Float(
        string="New Related Field",
        related="product_id.many2one_field_8eWzY.item_ids.fixed_price",
        store=True,
        readonly=True,
    )
    related_field_e9NHB = fields.Char(string="New Related Field", readonly=True)
    related_field_kbp8y = fields.Char(
        string="New Related Field",
        related="product_id.product_variant_id.display_name",
        store=False,
        readonly=True,
    )
    related_field_lBjdh = fields.Float(
        string="New Related Field",
        related="product_id.list_price",
        store=False,
        readonly=True,
    )
    # TODO: related_field_zy8mz = fields.One2many(...) -- Studio inverse name
    # unknown; port from Clear-DB manually.
    sales_report_type = fields.Many2one(
        "sales_report_type", string="Report Type (S- Incentive Calculation)"
    )
    sales_team = fields.Many2one(
        "crm.team",
        string="Sales Team",
        related="move_id.team_id",
        store=True,
        readonly=True,
    )
    status = fields.Selection(
        string="Status", related="move_id.state", store=True, readonly=True
    )
    status_1 = fields.Selection(
        string="Status", related="move_id.state", store=True, readonly=True
    )
    surname = fields.Char(
        string="Surname",
        related="contract_id.surname",
        store=True,
        readonly=True,
    )
    swift_code = fields.Char(
        string="Swift Code",
        related="contract_id.employee_id.bank_account_id.swift_code",
        store=True,
        readonly=True,
    )
    tags = fields.Many2many(
        "misc_charge_codes",
        "account_move_line_x_studio_tags_rel",
        "account_id",
        "x_misc_charge_codes_id",
    )
    tax = fields.Monetary(
        string="Tax",
        readonly=True,
        currency_field="currency_id",
        related="move_id.amount_tax",
        store=True,
    )
    to_account = fields.Char(
        string="To Account",
        related="contract_id.employee_id.bank_account_id.acc_number",
        store=True,
        readonly=True,
    )
    total_contribution = fields.Float(
        compute="_compute_total_contribution",
        store=True,
        readonly=True,
    )
    total_earnings = fields.Monetary(
        string="Total Earnings",
        readonly=True,
        currency_field="currency_id",
        related="contract_id.wage",
        store=True,
    )

    @api.depends("distribution_analytic_account_ids", "journal_id", "name", "date")
    def _compute_employers_contribution(self):
        AML = self.env["account.move.line"]
        for rec in self:
            value = 0
            if rec.name == "EPF 12%":
                value = abs(rec.amount_currency or 0)
            elif rec.name == "EPF 8%" and rec.distribution_analytic_account_ids:
                etf = AML.search(
                    [
                        (
                            "distribution_analytic_account_ids",
                            "in",
                            rec.distribution_analytic_account_ids.ids,
                        ),
                        ("name", "=", "EPF 12%"),
                        ("date", "=", rec.date),
                    ],
                    limit=1,
                )
                if etf:
                    value = abs(etf.amount_currency or 0)
            rec.employers_contribution = value

    @api.depends("distribution_analytic_account_ids", "journal_id", "name", "date")
    def _compute_members_contribution(self):
        AML = self.env["account.move.line"]
        for rec in self:
            value = 0
            if rec.name == "EPF 8%":
                value = abs(rec.amount_currency or 0)
            elif rec.name == "EPF 12%" and rec.distribution_analytic_account_ids:
                epf = AML.search(
                    [
                        (
                            "distribution_analytic_account_ids",
                            "in",
                            rec.distribution_analytic_account_ids.ids,
                        ),
                        ("name", "=", "EPF 8%"),
                        ("date", "=", rec.date),
                    ],
                    limit=1,
                )
                if epf:
                    value = abs(epf.amount_currency or 0)
            rec.members_contribution = value

    @api.depends("members_contribution", "employers_contribution")
    def _compute_total_contribution(self):
        for rec in self:
            rec.total_contribution = (
                rec.members_contribution + rec.employers_contribution
            )

    @api.depends("purchase_order_id")
    def _compute_related_field_WVIs6(self):
        # CDB related target: purchase_order_id.order_line.indent_no
        # indent_no on purchase.order.line is BugFix-Purchase-owned,
        # loads AFTER Accounting - can't use related at setup time. Runtime
        # hasattr guard reads first order line's indent_no if available.
        for rec in self:
            value = False
            po = rec.purchase_order_id
            if po and po.order_line and "indent_no" in po.order_line._fields:
                first_line = po.order_line[:1]
                if first_line:
                    value = first_line.indent_no or False
            rec.related_field_WVIs6 = value

    def _compute_credit_limit_2(self):
        # CDB compute calls self._fix_repair_compute_credit_limit_2() which
        # is a Fix-repair-added method. Fix-repair loads AFTER Accounting,
        # so at Accounting-load time the method doesn't exist. Guard at
        # runtime with hasattr. If Fix-repair not installed, field stays 0.
        for rec in self:
            if hasattr(rec, "_fix_repair_compute_credit_limit_2"):
                rec._fix_repair_compute_credit_limit_2()
            else:
                rec.credit_limit_2 = 0

    related_field_zy8mz = fields.One2many(
        string="New Related Field",
        related="purchase_order_id.order_line",
        readonly=True,
    )
