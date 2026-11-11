"""Ported declaration for journal_types (Studio custom model).

Clear-DB has this model with 6 user fields plus mail.thread +
mail.activity.mixin. Ported byte-verbatim so the pinned form view
in x_journal_types_studio_ported_v2.xml validates on fresh install.
"""

from odoo import fields, models


class XJournalTypes(models.Model):
    _name = "journal_types"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "Journal Types"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    active = fields.Boolean(default=True)
    name = fields.Char(string="Journal Type", required=True)
    accounting_company_id = fields.Many2one("res.company", string="Company")
    description = fields.Char()
    offset_account = fields.Many2one("account.account")
    sequence = fields.Integer()


class XJournalTypesGap(models.Model):
    _inherit = "journal_types"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char(string="Journal Type")
