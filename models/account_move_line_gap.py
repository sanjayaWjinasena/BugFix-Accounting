from odoo import fields, models


class AccountMoveLineGap(models.Model):
    _inherit = "account.move.line"

    x_studio_related_field_zy8mz = fields.One2many(
        string="New Related Field",
        related="purchase_order_id.order_line",
        readonly=True,
    )
