"""x_rm_prod_summary_spli — Production-summary split-quantity row.

Per-job-per-product row splitting a production quantity across two
splits (usage / configuration decided by report seed). Related field
`x_studio_product_code` exposes the linked product's default_code
for column display without duplicating storage.
"""

from odoo import fields, models


class XRmProdSummarySpli(models.Model):
    _name = "x_rm_prod_summary_spli"
    _description = "RM Prod. Summary Split"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "sequence, id"
    _rec_name = "name"

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(string="Name")
    description = fields.Many2one(
        "product.product",
        string="Description",
    )
    x_studio_header_reference = fields.Char(string="Header Reference")
    x_studio_job_no = fields.Char(string="Job No")
    x_studio_product_code = fields.Char(
        string="Product Code",
        related="description.default_code",
        readonly=True,
    )
    quantity = fields.Float(string="Quantity")
    x_studio_sales_report_model_id = fields.Many2one(
        "x_sales_report_model",
        string="Sales Report Model Id",
    )
    sequence = fields.Integer(string="Sequence", default=10)
    x_studio_split = fields.Float(string="Split")
    x_studio_split_1 = fields.Float(string="Split")
    x_studio_total = fields.Float(string="Total")


class XRmProdSummarySpliGap(models.Model):
    _inherit = "x_rm_prod_summary_spli"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
