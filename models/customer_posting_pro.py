from odoo import fields, models


class XCustomerPostingPro(models.Model):
    """Studio-ported custom model customer_posting_pro."""

    _name = "customer_posting_pro"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.activity.mixin"]
    _description = "Customer Posting Profile"

    active = fields.Boolean()
    name = fields.Char(string="Customer Posting Profile")
    item_relation_type = fields.Selection(
        [("All", "All"), ("Group", "Group"), ("Table", "Table")],
    )
    many2one_field_eYVbe = fields.Many2one("product.product", string="Product")
    notes = fields.Text()
    sequence = fields.Integer()


class XCustomerPostingProGap(models.Model):
    _inherit = "customer_posting_pro"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char(string="Customer Posting Profile")
