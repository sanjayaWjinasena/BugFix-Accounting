"""temp_tp_invoice_head — transient/staging header for TP invoices.

Used by the Studio-designed wizard flow to accumulate charge lines
before promoting them to a real tp_invoice_header. Field shape is
minimal — just the parent link to a consignment header, the vendor,
and a one2many of temp_tp_invoice_line rows.

v0.0.16 (chunk 3) filled the previously-TODO charge_line
one2many with its inverse.
"""

from odoo import fields, models


class XTempTpInvoiceHead(models.Model):
    _name = "temp_tp_invoice_head"
    _inherit = ["mail.activity.mixin"]
    _description = "Temp TP Invoice Header"
    _order = "sequence, id"
    _rec_name = "name"

    active = fields.Boolean(default=True)
    name = fields.Char()
    charge_line = fields.One2many(
        "temp_tp_invoice_line",
        "temp_tp_invoice_header_id",
    )
    consignment_header_id = fields.Many2one(
        "consignment_header",
        string="Consignment Header Id",
    )
    sequence = fields.Integer(default=10)
    supplier_id = fields.Many2one("res.partner", string="Vendor")


class XTempTpInvoiceHeadGap(models.Model):
    _inherit = "temp_tp_invoice_head"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char()
