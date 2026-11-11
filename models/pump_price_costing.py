"""pump_price_costing - pump price costing worksheet.

Studio-created custom model. Each row records a pump product's
price/cost worksheet with dozens of float fields grouped as:
  * Current / proposed base + retail prices
  * Total cost breakdown (material, factory, labour with/without OT)
  * OH absorbed (factory / other / sales)
  * Contribution / profit-markup / max-discount at three tiers
  * Actual vs standard idling rates + labour hours

Linked to sales_report_model via sales_report_model_id
so a report header can gather multiple pump-costing rows. The
inverse O2M pump_price_costing_ids is declared in
models/sales_report_model.py.

Clear-DB has 0 rows in this table -- schema-only asset. Ported for
fresh-install completeness so the "Pump Price Costing" tab
(currently stripped from sales_report_model form) can be restored
in a follow-up commit per docs/INSTALL_JOURNEY.md item #4.
"""

from odoo import fields, models


class XPumpPriceCosting(models.Model):
    _name = "pump_price_costing"
    _description = "Pump Price Costing"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "sequence asc, id asc"
    _rec_name = "name"

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
    actual = fields.Float(string="Actual (Exc. Casting Hours)")
    actual_1 = fields.Float(string="Actual (Tot. Labour Hours)")
    contingency_1 = fields.Float(string="Contingency %")
    contingency_rs = fields.Float(string="Contingency (Rs.)")
    contribution_2 = fields.Float(string="Contribution %")
    contribution_rs = fields.Float(string="Contribution Rs.")
    current_base_price = fields.Float(string="Current Base Price")
    current_retail_price_vat_18 = fields.Float(
        string="Current Retail Price (VAT 15%)"
    )
    date = fields.Date(string="Date")
    difference = fields.Float(string="Difference")
    accounting_discount = fields.Float(string="Discount")
    distributor_addition = fields.Float(string="Distributor Addition")
    factory_oh = fields.Float(string="Factory OH")
    float_field_YMvHy = fields.Float(string="New Decimal")
    idling_rate = fields.Float(string="Idling Rate (Exc. Casting Hours)")
    idling_rate_1 = fields.Float(string="Idling Rate (Tot. Labour Hours)")
    labour = fields.Float(string="New Decimal")
    labour_1 = fields.Float(string="Labour")
    material_cost_imports = fields.Float(string="Material Cost (Imports)")
    material_cost_other = fields.Float(string="Material Cost (Other)")
    max_discount = fields.Float(string="Max. Discount")
    max_discount_1 = fields.Float(string="Max Discount ")
    max_discount_2 = fields.Float(string="Max Discount ")
    net_selling_price = fields.Float(string="Net Selling Price")
    net_selling_price_1 = fields.Float(string="Net Selling Price")
    net_selling_price_2 = fields.Float(string="Net Selling Price")
    oh_absorbed_factory = fields.Float(string="OH Absorbed Factory")
    oh_absorbed_factory_1 = fields.Float(string="OH Absorbed Factory")
    oh_absorbed_other = fields.Float(string="OH Absorbed Other")
    oh_absorbed_other_1 = fields.Float(string="OH Absorbed Other")
    oh_absorbed_sales = fields.Float(string="OH Absorbed Sales")
    oh_absorbed_sales_1 = fields.Float(string="OH Absorbed Sales")
    other_oh = fields.Float(string="Other OH")
    other_oh_rs = fields.Float(string="Other OH Rs.")
    product_id = fields.Many2one("product.product", string="Product Id")
    product_id_1 = fields.Many2one(
        "product.template", string="Product Id (Actual)"
    )
    profit_mark_up_ = fields.Float(string="Profit Mark Up %")
    profit_mark_up_3 = fields.Float(string="Profit Mark Up")
    profit_mark_up_rs = fields.Float(string="Profit Mark Up Rs.")
    profit_mark_up_rs_1 = fields.Float(string="Profit Mark Up Rs.")
    profitloss_as_of_net_sale = fields.Float(
        string="Profit/(Loss) As % of Net Sale"
    )
    proposed_base_price = fields.Float(string="Proposed Base Price")
    proposed_base_price_1 = fields.Float(string="Proposed Base Price")
    report_reference_1 = fields.Char(string="Report Reference")
    route_time = fields.Float(string="Route Time")
    rs = fields.Float(string="Rs.")
    rs_1 = fields.Char(string="Rs.")
    sales_oh = fields.Float(string="Sales OH")
    sales_oh_rs = fields.Float(string="Sales OH Rs.")
    sales_report_model_id = fields.Many2one(
        "sales_report_model", string="Report Reference"
    )
    satd_discount = fields.Float(string="Satd. Discount")
    sequence = fields.Integer(string="Sequence")
    sscl = fields.Float(string="SSCL")
    sscl_1 = fields.Float(string="SSCL")
    sscl_2 = fields.Float(string="SSCL")
    standard = fields.Float(string="Standard (Exc. Casting Hours)")
    standard_1 = fields.Float(string="Standard (Tot. Labour Hours)")
    system_cost = fields.Float(string="System Cost", store=False)
    total_actual_labour_cost = fields.Float(string="Total Actual Labour Cost")
    total_actual_labour_cost_ot = fields.Float(
        string="Total Actual Labour Cost (OT)"
    )
    total_actual_labour_cost_without_ot = fields.Float(
        string="Total Actual Labour Cost (Without OT)"
    )
    total_cost = fields.Float(string="Total Cost")
    total_factory_cost = fields.Float(string="Total Factory Cost")
    total_factory_cost_1 = fields.Float(string="Total Factory Cost (Actual)")
    total_material_cost = fields.Float(string="Total Material Cost")
    total_material_cost_1 = fields.Float(string="Total Material Cost")
    total_material_cost_2 = fields.Float(string="Total Material Cost")


class XPumpPriceCostingGap(models.Model):
    _inherit = "pump_price_costing"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
