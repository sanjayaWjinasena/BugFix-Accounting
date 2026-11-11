"""tp_invoice_header — Transfer-Price (TP) invoice header.

Vendor bill created from an import consignment. Each header carries
one or more tp_invoice_line rows (Percentage / Fixed charge groups
across Charges / Duty / Taxes) whose amounts roll up into monetary
totals + tax subtotal.

v0.0.16 (chunk 3) filled the TODO one2many + populated selections +
ported the four SUM computes and the account_move smart-button
counter compute — all verbatim from Clear-DB.
"""

from odoo import api, fields, models


class XTpInvoiceHeader(models.Model):
    _name = "tp_invoice_header"
    _inherit = ["mail.activity.mixin"]
    _description = "TP Invoice Header"
    _order = "sequence, id"
    _rec_name = "name"

    active = fields.Boolean(default=True)
    currency_id = fields.Many2one("res.currency")
    name = fields.Char(string="Invoice Reference")
    con_no = fields.Many2one(
        "consignment_header",
        string="Created From Consignment No",
    )
    accounting_currency_id = fields.Many2one("res.currency", string="Currency")
    accounting_invoice_date = fields.Date(
        string="Supplier's Invoice Date (Bill Date)",
    )
    invoice_no = fields.Char(
        string="Supplier's Invoice No (Bill Reference)",
    )
    accounting_name = fields.Char(
        string="Name",
        related="vendor.name",
        readonly=True,
    )
    pipeline_status_bar = fields.Selection(
        [("Draft", "Draft"), ("Posted", "Posted")],
        string="Pipeline status bar",
    )
    sequence = fields.Integer(default=10)
    status = fields.Selection(
        [("Draft", "Draft"), ("Posted", "Posted")],
    )
    vendor = fields.Many2one("res.partner")
    tp_lines = fields.One2many(
        "tp_invoice_line",
        "tp_invoice_header_id",
        string="TP Lines",
    )

    # ---- Non-stored monetary totals (ported verbatim from Studio) ----

    total_invoice_amount = fields.Monetary(
        string="Untaxed Amount",
        currency_field="currency_id",
        compute="_compute_total_invoice_amount",
        store=False,
        readonly=True,
    )
    taxes_1 = fields.Monetary(
        string="Taxes",
        currency_field="currency_id",
        compute="_compute_taxes_1",
        store=False,
        readonly=True,
    )
    total_1 = fields.Monetary(
        string="Total",
        currency_field="currency_id",
        compute="_compute_total_1",
        store=False,
        readonly=True,
    )
    total_original_invoice_amount = fields.Float(
        compute="_compute_total_original_invoice_amount",
        store=False,
        readonly=True,
    )
    tp_id__account_move_count = fields.Integer(
        string="Created From TP Invoice count",
        compute="_compute_tp_id__account_move_count",
        store=False,
    )

    @api.depends(
        "tp_lines",
        "tp_lines.invoice_amount",
    )
    def _compute_total_invoice_amount(self):
        for rec in self:
            rec.total_invoice_amount = sum(line.invoice_amount for line in rec.tp_lines)

    @api.depends(
        "tp_lines",
        "tp_lines.taxes",
        "tp_lines.invoice_amount",
    )
    def _compute_taxes_1(self):
        for rec in self:
            rec.taxes_1 = sum(line.tax_amount for line in rec.tp_lines)

    @api.depends(
        "total_invoice_amount",
        "taxes_1",
    )
    def _compute_total_1(self):
        for rec in self:
            rec.total_1 = rec.total_invoice_amount + rec.taxes_1

    @api.depends(
        "tp_lines",
        "tp_lines.original_amount",
    )
    def _compute_total_original_invoice_amount(self):
        for rec in self:
            rec.total_original_invoice_amount = sum(
                line.original_amount for line in rec.tp_lines
            )

    def _compute_tp_id__account_move_count(self):
        """Count of account.move rows whose tp_id points at
        this header. Ported from Studio's read_group snippet. Guarded
        so absence of `tp_id` on account.move (fresh install
        without BugFix-Accounting's account.move Studio extensions
        yet) doesn't crash the compute — falls back to 0.
        """
        AccountMove = self.env["account.move"]
        if "tp_id" not in AccountMove._fields:
            for rec in self:
                rec.tp_id__account_move_count = 0
            return
        results = AccountMove.read_group(
            [("tp_id", "in", self.ids)],
            ["tp_id"],
            ["tp_id"],
        )
        counts = {
            r["tp_id"][0]: r["x_studio_tp_id_count"] for r in results if r.get("tp_id")
        }
        for rec in self:
            rec.tp_id__account_move_count = counts.get(rec.id, 0)


class XTpInvoiceHeaderGap(models.Model):
    _inherit = "tp_invoice_header"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    currency_id = fields.Many2one(comodel_name="res.currency")
    name = fields.Char(string="Invoice Reference")
