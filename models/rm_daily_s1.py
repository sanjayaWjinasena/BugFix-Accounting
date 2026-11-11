"""rm_daily_s1 — Daily-sales reporting row, variant 1.

One of three near-identical daily-sales row models (s1/s2/s3) that
Studio uses to feed different pivots of the same daily-sales report
header (sales_report_model). Each row records a single invoice
line's contribution to a day's sales at a sales-centre for a
partner+product combo.

s1 and s2 have identical field shape; s3 diverges only in the
partner reference field name (`many2one_field_CiZHF`
instead of `partner`), likely a Studio-designer artefact
that we preserve verbatim.
"""

from odoo import fields, models


class XRmDailyS1(models.Model):
    _name = "rm_daily_s1"
    _description = "RM Daily S1"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "sequence, id"
    _rec_name = "name"

    active = fields.Boolean(default=True)
    name = fields.Char()
    accounting_invoice_date = fields.Date(string="Invoice Date")
    number = fields.Char()
    partner = fields.Many2one("res.partner")
    product_id = fields.Many2one("product.product")
    quantity = fields.Float()
    sales_centre = fields.Many2one("crm.team")
    sales_report_model_id = fields.Many2one(
        "sales_report_model",
    )
    sequence = fields.Integer(default=10)
    value = fields.Float()


class XRmDailyS1Gap(models.Model):
    _inherit = "rm_daily_s1"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char()
