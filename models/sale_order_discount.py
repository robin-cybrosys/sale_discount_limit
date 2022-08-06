from odoo import models, api, fields
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = ['sale.order']

    max_disc_limit = fields.Float(default=lambda self: self.env[
        'ir.config_parameter'].sudo().get_param(
        'sale.order.max_disc_limit'))
    cumulative_discount = fields.Float(default=lambda self: self.env[
        'ir.config_parameter'].sudo().get_param('my.global.variable'))
    discount_total = fields.Float(compute='_compute_discount')

    @api.depends('order_line.discount')
    def _compute_discount(self):
        unit_price = sum(self.order_line.mapped('price_unit'))
        subtotal = sum(self.order_line.mapped('price_subtotal'))
        self.discount_total = unit_price - subtotal
        print(self.discount_total, "compute")

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        if self.state == 'sale':
            self.cumulative_discount += self.discount_total
            if self.cumulative_discount <= self.max_disc_limit:
                self.env['ir.config_parameter'].sudo().set_param(
                    'my.global.variable', self.cumulative_discount
                )
                # print(self.cumulative_discount, "after confirmed")
            else:
                raise ValidationError(
                    "The total discount of the month have exceeded the limit!")

            return res
