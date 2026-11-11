"""rm_daily_s3 — Daily-sales reporting row, variant 3.

Same shape as s1 / s2 EXCEPT the partner reference is named
`many2one_field_CiZHF` (Studio-auto-generated identifier)
instead of the semantic name `partner` that s1/s2 use.
Preserving the field name verbatim per feedback-clear-db-verbatim.
"""

from odoo import fields, models


class XRmDailyS3(models.Model):
    _name = "rm_daily_s3"
    _description = "RM Daily S3"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "sequence, id"
    _rec_name = "name"

    active = fields.Boolean(default=True)
    name = fields.Char()
    accounting_invoice_date = fields.Date(string="Invoice Date")
    number = fields.Char()
    many2one_field_CiZHF = fields.Many2one(
        "res.partner",
        string="Partner",
    )
    product_id = fields.Many2one("product.product")
    quantity = fields.Float()
    sales_centre = fields.Many2one("crm.team")
    sales_report_model_id = fields.Many2one(
        "sales_report_model",
    )
    sequence = fields.Integer(default=10)
    value = fields.Float()


class XRmDailyS3Gap(models.Model):
    _inherit = "rm_daily_s3"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char()
