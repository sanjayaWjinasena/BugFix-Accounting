from odoo import fields, models


class XTempTpInvoiceLine(models.Model):
    """Studio-ported custom model temp_tp_invoice_line."""

    _name = "temp_tp_invoice_line"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.activity.mixin"]
    _description = "Temp TP Invoice Line"

    active = fields.Boolean()
    name = fields.Char()
    amount = fields.Float()
    basis = fields.Selection(
        [("Percentage", "Percentage"), ("Fixed Per Document", "Fixed Per Document")],
    )
    charge_group = fields.Selection(
        [
            ("None", "None"),
            ("Charges", "Charges"),
            ("Duty", "Duty"),
            ("Taxes", "Taxes"),
        ],
    )
    charge_name = fields.Char()
    consignment_charge_header_id = fields.Many2one(
        "consignment_charge_h", string="Consignment Charge Header Id"
    )
    consignment_id = fields.Many2one("consignment_header", string="Consignment Id")
    accounting_select = fields.Boolean(string="Select")
    sequence = fields.Integer()
    temp_tp_invoice_header_id = fields.Many2one(
        "temp_tp_invoice_head", string="Temp TP Invoice Header Id", ondelete="cascade"
    )


class XTempTpInvoiceLineGap(models.Model):
    _inherit = "temp_tp_invoice_line"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char()
