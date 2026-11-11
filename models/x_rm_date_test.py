"""x_rm_date_test — Studio-created test reporting model.

Small catchall reporting row keyed off x_sales_report_model_id (the
shared header). Kept in the port because Clear-DB has it as
state='manual' with 4 fields and Studio pins it; a fresh install
without this model would break any menu / view that references it.

No computes, no cross-repo refs.
"""

from odoo import fields, models


class XRmDateTest(models.Model):
    _name = "x_rm_date_test"
    _description = "RM Date Test"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "sequence, id"
    _rec_name = "name"

    active = fields.Boolean(default=True)
    name = fields.Char()
    x_studio_date_test = fields.Date(string="Date Test")
    sequence = fields.Integer(default=10)
