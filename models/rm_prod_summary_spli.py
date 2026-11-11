"""rm_prod_summary_spli — Production-summary split-quantity row.

Per-job-per-product row splitting a production quantity across two
splits (usage / configuration decided by report seed). Related field
`product_code` exposes the linked product's default_code
for column display without duplicating storage.
"""

from odoo import fields, models


class XRmProdSummarySpli(models.Model):
    _name = "rm_prod_summary_spli"
    _description = "RM Prod. Summary Split"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "sequence, id"
    _rec_name = "name"

    active = fields.Boolean(default=True)
    name = fields.Char()
    description = fields.Many2one(
        "product.product",
    )
    header_reference = fields.Char()
    job_no = fields.Char()
    product_code = fields.Char(
        string="Product Code",
        related="description.default_code",
        readonly=True,
    )
    quantity = fields.Float()
    sales_report_model_id = fields.Many2one(
        "sales_report_model",
        string="Sales Report Model Id",
    )
    sequence = fields.Integer(default=10)
    split = fields.Float()
    split_1 = fields.Float(string="Split")
    total = fields.Float()


class XRmProdSummarySpliGap(models.Model):
    _inherit = "rm_prod_summary_spli"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char()
