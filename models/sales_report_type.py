"""Sentinel declaration for sales_report_type so cross-references resolve."""

from odoo import fields, models


class XSalesReportType(models.Model):
    _name = "sales_report_type"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "Sales Report Type"

    _inherit = ["mail.thread", "mail.activity.mixin"]
    active = fields.Boolean()
    name = fields.Char(string="Report Name")
    journal_entry_id = fields.One2many(
        "account.move",
        "report_type_s_cust_aging",
        string="Journal Entry Id",
    )
    journal_items_id = fields.One2many(
        "account.move.line",
        "sales_report_type",
        string="Journal Items Id",
    )
    # TODO: prod_summary_split_id = fields.One2many('stock.move.line',
    # <inverse>, string='Prod. Summary Split Id')
    # TODO: production_order_id = fields.One2many('mrp.production', <inverse>,
    # string='Production Order Id')
    # TODO: production_variance_id = fields.One2many('stock.move', <inverse>,
    # string='Production Variance Id')
    report_code = fields.Selection(
        [
            ("Daily Sales Summary", "Daily Sales Summary"),
            ("Sales Details for Incentive Calc.", "Sales Details for Incentive Calc."),
            ("Production Overview - WIP", "Production Overview - WIP"),
            ("Customer Aging Report", "Customer Aging Report"),
            ("Slow Moving Items", "Slow Moving Items"),
            (
                "Sales - Production - Purchase Report",
                "Sales - Production - Purchase Report",
            ),
            ("Production Summary - Split", "Production Summary - Split"),
            ("Production Job Variance", "Production Job Variance"),
            ("Casting Melt", "Casting Melt"),
            ("Import Transaction", "Import Transaction"),
            ("Project Gross Margin", "Project Gross Margin"),
            ("Costing Work Sheet", "Costing Work Sheet"),
        ],
    )
    sales_lines_id = fields.One2many(
        "sale.order.line",
        "sales_report_type",
        string="Sales Lines Id",
    )
    # TODO: sales_prod_purch_id = fields.One2many('stock.move.line', <inverse>,
    # string='Sales Prod. Purch. Id')
    sequence = fields.Integer()
    # TODO: slow_moving_item_id = fields.One2many('stock.move.line', <inverse>,
    # string='Slow Moving Item Id')
    test = fields.One2many(
        "account.move.line",
        "many2one_field_kiSUJ",
        string="test",
    )


class XSalesReportTypeGap(models.Model):
    _inherit = "sales_report_type"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char(string="Report Name")
