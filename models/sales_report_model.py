"""Sentinel declaration for sales_report_model so cross-references resolve."""

from odoo import fields, models


class XSalesReportModel(models.Model):
    _name = "sales_report_model"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "Sales Report Model"

    _inherit = ["mail.thread", "mail.activity.mixin"]
    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
    actual_gp_ = fields.Float(string="Actual GP")
    actual_line_ids = fields.One2many(
        "rm_gross_margin_actu",
        "sales_report_model_id",
        string="Actual Line Ids",
    )
    actuals = fields.Boolean(string="Actuals")
    as_on_date = fields.Date(string="As on Date")
    as_on_date_1 = fields.Date(string="From Date")
    as_on_date_2 = fields.Date(string="To Date")
    auto_generated = fields.Boolean(string="Auto Generated")
    comparison_line_ids = fields.One2many(
        "rm_gross_margin_comp",
        "sales_report_model_id",
        string="Comparison Line Ids",
    )
    contingency_ = fields.Float(string="Contingency %")
    created_date = fields.Date(string="Created Date")
    created_from_project_update = fields.Many2one(
        "project.update", string="Created From Project Update"
    )
    customer = fields.Many2many(
        "res.partner",
        "x_sales_report_model_x_studio_customer_rel",
        "host_id",
        "target_id",
        string="Customer",
    )
    daily_sales_report_id = fields.One2many(
        "rm_daily_sales_repor",
        "sales_report_model_id",
        string="Daily Sales Report Id 1",
    )
    daily_sales_report_id_1 = fields.One2many(
        "rm_daily_s1",
        "sales_report_model_id",
        string="Daily Sales Report Id 2",
    )
    daily_sales_report_id_2 = fields.One2many(
        "rm_daily_s2",
        "sales_report_model_id",
        string="Daily Sales Report Id 3",
    )
    daily_sales_report_id_3 = fields.One2many(
        "rm_daily_s3",
        "sales_report_model_id",
        string="Daily Sales Report Id 4",
    )
    date_updated = fields.Boolean(string="Date Updated")
    distributor_addition = fields.Float(string="Distributor Addition %")
    estimated_gp_ = fields.Float(string="Estimated GP")
    estimated_line_ids = fields.One2many(
        "rm_gross_margin_esti",
        "sales_report_model_id",
        string="Estimated Line Ids",
    )
    factory_oh = fields.Float(string="Factory OH")
    factory_oh_labour = fields.Float(string="Factory OH (Labour)")
    financial_progress = fields.Float(string="Financial Progress")
    from_date = fields.Date(string="From Date")
    idling_rate = fields.Float(string="Idling Rate %")
    invoice_details_line_ids = fields.One2many(
        "rm_gross_margin_invo",
        "sales_report_model_id",
        string="Invoice Details Line Ids",
    )
    journal_item_ids = fields.One2many(
        "account.move.line",
        related="report_type.journal_items_id",
        string="Journal Item Ids",
        readonly=True,
    )
    management_purpose = fields.Boolean(string="Management Purpose")
    month_end_entry_updated = fields.Boolean(string="Month End Entry Updated")
    none_moving_item_ids = fields.One2many(
        "rm_none_moving",
        "sales_report_model_id",
        string="None Moving Item IDs",
    )
    oh_absorbed_2_factory = fields.Float(string="OH Absorbed 2 (Factory)")
    oh_absorbed_2_other = fields.Float(string="OH Absorbed 2 (Other)")
    oh_absorbed_2_sales = fields.Float(string="OH Absorbed 2 (Sales)")
    oh_absorbed_factory = fields.Float(string="OH Absorbed (Factory)")
    oh_absorbed_other = fields.Float(string="OH Absorbed (Other)")
    oh_absorbed_sales = fields.Float(string="OH Absorbed (Sales)")
    one2many_field_1Aq0X = fields.One2many(
        "rm_production_varian",
        "sales_report_model_id",
        string="New One2many",
    )
    one2many_field_1rlRW = fields.One2many(
        "rm_production_orders",
        "sales_report_model_id",
        string="New One2many",
    )
    one2many_field_6rdac = fields.One2many(
        "rm_sales_prod_purch", "sales_report_model_id", string="New One2many"
    )
    one2many_field_jTZq4 = fields.One2many(
        "rm_sales_order_line",
        "sales_report_model_id",
        string="Sales Order Lines",
    )
    one2many_field_yeTsx = fields.One2many(
        "rm_prod_summary_spli",
        "sales_report_model_id",
        string="New One2many",
    )
    other_oh = fields.Float(string="Other OH")
    profit_mark_up_ = fields.Float(string="Profit Mark Up %")
    project_no = fields.Many2one("project.project", string="Project No")
    pump_price_costing_ids = fields.One2many(
        "pump_price_costing",
        "sales_report_model_id",
        string="Pump Price Costing Ids",
    )
    related_field_DqBBB = fields.One2many(
        "sale.order.line",
        related="report_type.sales_lines_id",
        string="New Related Field",
        readonly=True,
    )
    # TODO: related_field_NsCKm = fields.One2many('stock.move.line', <inverse>,
    # string='New Related Field')
    # TODO: related_field_PaCjA = fields.One2many('stock.move', <inverse>,
    # string='New Related Field')
    # TODO: related_field_XCKXu = fields.One2many('stock.move.line', <inverse>,
    # string='New Related Field')
    # TODO: related_field_bCtVj = fields.One2many('stock.move.line', <inverse>,
    # string='New Related Field')
    related_field_n589a = fields.One2many(
        "account.move.line",
        related="report_type.journal_items_id",
        string="New Related Field",
        readonly=True,
    )
    related_field_nfrkz = fields.One2many(
        "account.move",
        related="report_type.journal_entry_id",
        string="New Related Field",
        readonly=True,
    )
    # TODO: related_field_oeTJK = fields.One2many('mrp.production', <inverse>,
    # string='New Related Field')
    report_code = fields.Selection(
        string="Report Code",
        related="report_type.report_code",
        store=True,
        readonly=True,
    )
    report_type = fields.Many2one("sales_report_type", string="Report Type")
    sales_centre = fields.Many2many(
        "crm.team",
        "x_sales_report_model_x_studio_sales_centre_rel",
        "host_id",
        "target_id",
        string="Sales Centre",
    )
    sales_oh = fields.Float(string="Sales OH")
    sales_report_model_id_4 = fields.One2many(
        "rm_customer_wise_inv",
        "sales_report_model_id",
        string="Sales Report Model Id",
    )
    sales_report_model_id_5 = fields.One2many(
        "rm_cust_invoice_s1",
        "sales_report_model_id",
        string="Sales Report Model Id",
    )
    selection_field_Fbw0x = fields.Selection(
        [("Draft", "Draft"), ("Done", "Done")], string="Status"
    )
    sequence = fields.Integer(string="Sequence")
    sscl = fields.Float(string="SSCL %")


class XSalesReportModelGap(models.Model):
    _inherit = "sales_report_model"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
