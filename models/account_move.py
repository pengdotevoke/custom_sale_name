from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    sale_order_name = fields.Char(
        string="Sales Order",
        compute="_compute_sale_order_name",
        store=True,
    )

    @api.depends('invoice_origin')
    def _compute_sale_order_name(self):
        for invoice in self:
            if invoice.invoice_origin:
                # Find the related sale order by name
                sale_order = self.env['sale.order'].search([('name', '=', invoice.invoice_origin)], limit=1)
                invoice.sale_order_name = sale_order.name if sale_order else ''
            else:
                invoice.sale_order_name = ''
