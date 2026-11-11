"""rm_none_moving — None-moving stock reporting row.

Per-product line under a sales_report_model header, capturing
in-hand and issue quantities across up to 4 time buckets plus the
current qty / base price / value. Related fields expose the product's
category and default_code without denormalising the storage.
"""

from odoo import fields, models


class XRmNoneMoving(models.Model):
    _name = "rm_none_moving"
    _description = "RM None Moving"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "sequence, id"
    _rec_name = "name"

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(string="Name")
    base_price = fields.Float(string="Base Price")
    description = fields.Many2one(
        "product.product",
        string="Description",
    )
    header_reference = fields.Char(string="Header Reference")
    in_hand_1 = fields.Float(string="In Hand")
    in_hand_2 = fields.Float(string="In Hand")
    in_hand_3 = fields.Float(string="In Hand")
    in_hand_4 = fields.Float(string="In Hand")
    issue_1 = fields.Float(string="Issue")
    issue_2 = fields.Float(string="Issue")
    issue_3 = fields.Float(string="Issue")
    issue_4 = fields.Float(string="Issue")
    product_category = fields.Many2one(
        "product.category",
        string="Product Category",
        related="description.categ_id",
        store=False,
        readonly=True,
    )
    product_code_1 = fields.Char(
        string="Product Code",
        related="description.default_code",
        readonly=True,
    )
    qty = fields.Float(string="Qty")
    sales_report_model_id = fields.Many2one(
        "sales_report_model",
        string="Sales Report Model Id",
    )
    sequence = fields.Integer(string="Sequence", default=10)
    value = fields.Float(string="Value")


class XRmNoneMovingGap(models.Model):
    _inherit = "rm_none_moving"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
