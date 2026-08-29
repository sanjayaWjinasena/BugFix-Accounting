# -*- coding: utf-8 -*-
"""x_rm_prod_summary_spli — Production-summary split-quantity row.

Per-job-per-product row splitting a production quantity across two
splits (usage / configuration decided by report seed). Related field
`x_studio_product_code` exposes the linked product's default_code
for column display without duplicating storage.
"""
from odoo import fields, models


class XRmProdSummarySpli(models.Model):
    _name = 'x_rm_prod_summary_spli'
    _description = 'Production Summary Split Reporting Row'
    _order = 'x_studio_sequence, id'
    _rec_name = 'x_name'

    x_active = fields.Boolean(string='Active', default=True)
    x_name = fields.Char(string='Name')
    x_studio_description = fields.Many2one(
        'product.product', string='Description',
    )
    x_studio_header_reference = fields.Char(string='Header Reference')
    x_studio_job_no = fields.Char(string='Job No')
    x_studio_product_code = fields.Char(
        string='Product Code',
        related='x_studio_description.default_code',
        readonly=True,
    )
    x_studio_quantity = fields.Float(string='Quantity')
    x_studio_sales_report_model_id = fields.Many2one(
        'x_sales_report_model', string='Sales Report Model Id',
    )
    x_studio_sequence = fields.Integer(string='Sequence', default=10)
    x_studio_split = fields.Float(string='Split')
    x_studio_split_1 = fields.Float(string='Split')
    x_studio_total = fields.Float(string='Total')
