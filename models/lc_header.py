"""Sentinel declaration for lc_header so cross-references resolve."""

from odoo import api, fields, models


class XLcHeader(models.Model):
    _name = "lc_header"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.activity.mixin"]
    _description = "LC Header"

    active = fields.Boolean(string="Active")
    name = fields.Char(string="LC Registration No")
    additional_conditions = fields.Text(string="Additional Conditions (47A/B)")
    available_with_by = fields.Char(string="Available with / By (41A)")
    bank_charges = fields.Text(string="Bank Charges (71B)")
    beneficiary = fields.Char(string="Beneficiary (59)")
    accounting_company_id = fields.Many2one("res.company", string="Company")
    confirmation_instructions = fields.Selection(
        [("None", "None"), ("A", "A"), ("B", "B"), ("C", "C")],
        string="Confirmation Instructions (49)",
    )
    created_from_purchase_order = fields.Many2one(
        "purchase.order", string="PO Number"
    )
    accounting_currency_id = fields.Many2one("res.currency", string="Currency")
    date_of_expiry = fields.Date(string="Date of Expiry (31D)")
    date_of_issue = fields.Date(string="Date of Issue (31C)")
    date_of_receipt = fields.Date(string="Date of Receipt")
    deferred_days = fields.Float(string="Deferred Days")
    description_of_goods = fields.Char(
        string="Description of Goods and / or Services (45A)"
    )
    document_required = fields.Text(string="Document Required (46A/B)")
    draft = fields.Selection(
        [("At Sight", "At Sight"), ("Deferred Payment", "Deferred Payment")],
        string="Draft (42C)",
    )
    indent_no = fields.Char(string="Indent No")
    instruction_remarks = fields.Text(string="Instruction / Remarks (78)")
    issuing_bank = fields.Many2one("res.bank", string="Issuing Bank")
    issuing_bank_reference_no_1 = fields.Char(
        string="Issuing Bank Reference No"
    )
    latest_shipment_date = fields.Date(string="Latest Shipment Date (44C)")
    lc_amount = fields.Float(string="LC Amount (32B)")
    lc_amount_lcy = fields.Float(
        string="LC Amount (LCY)",
        compute="_compute_lc_amount_lcy",
        store=True,
        readonly=True,
    )
    lc_credit_sub_type = fields.Selection(
        [
            ("Non Transferable", "Non Transferable"),
            ("Transferable", "Transferable"),
            ("Revolving", "Revolving"),
        ],
        string="Documentary Credit Sub Type (40A)",
    )
    lc_credit_type = fields.Selection(
        [("Irrevocable", "Irrevocable"), ("Revocable", "Revocable")],
        string="Documentary Credit Type (40A)",
    )
    lc_no = fields.Char(string="Documentatry Credit Number (20)")
    loading_on_board = fields.Char(string="Loading on Board (44A)")
    paid_amount_lcy = fields.Float(string="Paid Amount (LCY)")
    partial_shipment = fields.Selection(
        [("Allowed", "Allowed"), ("Not Allowed", "Not Allowed")],
        string="Partial Shipment (43P)",
    )
    period_for_presentation = fields.Float(
        string="Period for Presentation (48)"
    )
    place_of_expiry = fields.Char(string="Place of Expiry (31D)")
    revised_lc_amount = fields.Float(
        string="Revised Amount",
        compute="_compute_revised_lc_amount",
        store=True,
        readonly=True,
    )

    @api.depends(
        "accounting_currency_id", "accounting_currency_id.rate", "lc_amount"
    )
    def _compute_lc_amount_lcy(self):
        # Ported from CDB Studio compute. Original did a res.currency search
        # with a non-existent 'date' filter (schema-invalid); rewritten to
        # use the standard currency.rate field which is auto-updated per
        # company's currency conversion date.
        for rec in self:
            cur = rec.accounting_currency_id
            if cur and cur.rate:
                rec.lc_amount_lcy = round(
                    (rec.lc_amount or 0) / cur.rate, 2
                )
            else:
                rec.lc_amount_lcy = 0

    @api.depends("lc_amount", "tolerance_type", "tolerance")
    def _compute_revised_lc_amount(self):
        for record in self:
            amount = record.lc_amount or 0
            tolerance = record.tolerance or 0
            adjustment = amount * tolerance / 100
            if record.tolerance_type == "Plus":
                record.revised_lc_amount = amount + adjustment
            elif record.tolerance_type == "Minus":
                record.revised_lc_amount = amount - adjustment
            else:
                record.revised_lc_amount = amount

    selection_field_yo4qM = fields.Selection(
        [
            ("Draft", "Draft"),
            ("Posted", "Posted"),
            ("Amended", "Amended"),
            ("Paid", "Paid"),
            ("Cancelled", "Cancelled"),
        ],
        string="Pipeline status bar",
    )
    sequence = fields.Integer(string="Sequence")
    status = fields.Selection(
        [
            ("Draft", "Draft"),
            ("Posted", "Posted"),
            ("Paid", "Paid"),
            ("Amended", "Amended"),
            ("Cancelled", "Cancelled"),
        ],
        string="Status",
    )
    tolerance = fields.Float(string="Tolerance (39A)")
    tolerance_type = fields.Selection(
        [("Plus", "Plus"), ("Minus", "Minus")], string="Tolerance Type"
    )
    transportation = fields.Char(string="Transportation (44B)")
    transshipment = fields.Selection(
        [("Allowed", "Allowed"), ("Not Allowed", "Not Allowed")],
        string="Transshipment (43T)",
    )
    vendor = fields.Many2one("res.partner", string="Vendor")
    version_no = fields.Integer(string="Version No")


class XLcHeaderGap(models.Model):
    _inherit = "lc_header"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="LC Registration No")
