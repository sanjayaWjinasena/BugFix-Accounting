"""rm_daily_sales_repor — Daily sales KPI reporting row.

Per-sales-centre row storing monthly targets, daily / month /
cumulative net invoice values, achievement percentages. All
plain floats — no computes; values are stamped at row-generation
time by the report seeding logic (external to this model).
"""

from odoo import fields, models


class XRmDailySalesRepor(models.Model):
    _name = "rm_daily_sales_repor"
    _description = "RM Daily Sales Report"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "sequence, id"
    _rec_name = "name"

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(string="Name")
    achieve_cumulative_ = fields.Float(string="Achieve Cumulative (%)")
    achievement_ = fields.Float(string="Achievement (%)")
    m_sales_target = fields.Float(string="M. Sales Target")
    net_invoice_value_cumulative = fields.Float(
        string="Net Invoice Value - Cumulative",
    )
    net_invoice_value_day = fields.Float(
        string="Net Invoice Value - Day",
    )
    net_invoice_value_month = fields.Float(
        string="Net Invoice Value - Month",
    )
    s_target_cumulative = fields.Float(string="S. Target - Cumulative ")
    sales_centre = fields.Char(string="Sales Centre")
    sales_report_model_id = fields.Many2one(
        "sales_report_model",
        string="Sales Report Model Id",
    )
    sequence = fields.Integer(string="Sequence", default=10)


class XRmDailySalesReporGap(models.Model):
    _inherit = "rm_daily_sales_repor"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
