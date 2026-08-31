# -*- coding: utf-8 -*-
"""x_pump_price_costing - pump price costing worksheet.

Studio-created custom model. Each row records a pump product's
price/cost worksheet with dozens of float fields grouped as:
  * Current / proposed base + retail prices
  * Total cost breakdown (material, factory, labour with/without OT)
  * OH absorbed (factory / other / sales)
  * Contribution / profit-markup / max-discount at three tiers
  * Actual vs standard idling rates + labour hours

Linked to x_sales_report_model via x_studio_sales_report_model_id
so a report header can gather multiple pump-costing rows. The
inverse O2M x_studio_pump_price_costing_ids is declared in
models/x_sales_report_model.py.

Clear-DB has 0 rows in this table -- schema-only asset. Ported for
fresh-install completeness so the "Pump Price Costing" tab
(currently stripped from x_sales_report_model form) can be restored
in a follow-up commit per INSTALL_JOURNEY.md item #4.
"""
from odoo import fields, models


class XPumpPriceCosting(models.Model):
    _name = 'x_pump_price_costing'
    _description = 'Pump Price Costing'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'x_studio_sequence asc, id asc'
    _rec_name = 'x_name'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_actual = fields.Float(string='Actual (Exc. Casting Hours)')
    x_studio_actual_1 = fields.Float(string='Actual (Tot. Labour Hours)')
    x_studio_contingency_1 = fields.Float(string='Contingency %')
    x_studio_contingency_rs = fields.Float(string='Contingency (Rs.)')
    x_studio_contribution_2 = fields.Float(string='Contribution %')
    x_studio_contribution_rs = fields.Float(string='Contribution Rs.')
    x_studio_current_base_price = fields.Float(string='Current Base Price')
    x_studio_current_retail_price_vat_18 = fields.Float(string='Current Retail Price (VAT 15%)')
    x_studio_date = fields.Date(string='Date')
    x_studio_difference = fields.Float(string='Difference')
    x_studio_discount = fields.Float(string='Discount')
    x_studio_distributor_addition = fields.Float(string='Distributor Addition')
    x_studio_factory_oh = fields.Float(string='Factory OH')
    x_studio_float_field_YMvHy = fields.Float(string='New Decimal')
    x_studio_idling_rate = fields.Float(string='Idling Rate (Exc. Casting Hours)')
    x_studio_idling_rate_1 = fields.Float(string='Idling Rate (Tot. Labour Hours)')
    x_studio_labour = fields.Float(string='New Decimal')
    x_studio_labour_1 = fields.Float(string='Labour')
    x_studio_material_cost_imports = fields.Float(string='Material Cost (Imports)')
    x_studio_material_cost_other = fields.Float(string='Material Cost (Other)')
    x_studio_max_discount = fields.Float(string='Max. Discount')
    x_studio_max_discount_1 = fields.Float(string='Max Discount ')
    x_studio_max_discount_2 = fields.Float(string='Max Discount ')
    x_studio_net_selling_price = fields.Float(string='Net Selling Price')
    x_studio_net_selling_price_1 = fields.Float(string='Net Selling Price')
    x_studio_net_selling_price_2 = fields.Float(string='Net Selling Price')
    x_studio_oh_absorbed_factory = fields.Float(string='OH Absorbed Factory')
    x_studio_oh_absorbed_factory_1 = fields.Float(string='OH Absorbed Factory')
    x_studio_oh_absorbed_other = fields.Float(string='OH Absorbed Other')
    x_studio_oh_absorbed_other_1 = fields.Float(string='OH Absorbed Other')
    x_studio_oh_absorbed_sales = fields.Float(string='OH Absorbed Sales')
    x_studio_oh_absorbed_sales_1 = fields.Float(string='OH Absorbed Sales')
    x_studio_other_oh = fields.Float(string='Other OH')
    x_studio_other_oh_rs = fields.Float(string='Other OH Rs.')
    x_studio_product_id = fields.Many2one('product.product', string='Product Id')
    x_studio_product_id_1 = fields.Many2one('product.template', string='Product Id (Actual)')
    x_studio_profit_mark_up_ = fields.Float(string='Profit Mark Up %')
    x_studio_profit_mark_up_3 = fields.Float(string='Profit Mark Up')
    x_studio_profit_mark_up_rs = fields.Float(string='Profit Mark Up Rs.')
    x_studio_profit_mark_up_rs_1 = fields.Float(string='Profit Mark Up Rs.')
    x_studio_profitloss_as_of_net_sale = fields.Float(string='Profit/(Loss) As % of Net Sale')
    x_studio_proposed_base_price = fields.Float(string='Proposed Base Price')
    x_studio_proposed_base_price_1 = fields.Float(string='Proposed Base Price')
    x_studio_report_reference_1 = fields.Char(string='Report Reference')
    x_studio_route_time = fields.Float(string='Route Time')
    x_studio_rs = fields.Float(string='Rs.')
    x_studio_rs_1 = fields.Char(string='Rs.')
    x_studio_sales_oh = fields.Float(string='Sales OH')
    x_studio_sales_oh_rs = fields.Float(string='Sales OH Rs.')
    x_studio_sales_report_model_id = fields.Many2one('x_sales_report_model', string='Report Reference')
    x_studio_satd_discount = fields.Float(string='Satd. Discount')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_sscl = fields.Float(string='SSCL')
    x_studio_sscl_1 = fields.Float(string='SSCL')
    x_studio_sscl_2 = fields.Float(string='SSCL')
    x_studio_standard = fields.Float(string='Standard (Exc. Casting Hours)')
    x_studio_standard_1 = fields.Float(string='Standard (Tot. Labour Hours)')
    x_studio_system_cost = fields.Float(string='System Cost', store=False)
    x_studio_total_actual_labour_cost = fields.Float(string='Total Actual Labour Cost')
    x_studio_total_actual_labour_cost_ot = fields.Float(string='Total Actual Labour Cost (OT)')
    x_studio_total_actual_labour_cost_without_ot = fields.Float(string='Total Actual Labour Cost (Without OT)')
    x_studio_total_cost = fields.Float(string='Total Cost')
    x_studio_total_factory_cost = fields.Float(string='Total Factory Cost')
    x_studio_total_factory_cost_1 = fields.Float(string='Total Factory Cost (Actual)')
    x_studio_total_material_cost = fields.Float(string='Total Material Cost')
    x_studio_total_material_cost_1 = fields.Float(string='Total Material Cost')
    x_studio_total_material_cost_2 = fields.Float(string='Total Material Cost')
