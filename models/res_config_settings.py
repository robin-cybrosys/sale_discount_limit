from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    max_disc_limit = fields.Float(config_parameter='sale.order.max_disc_limit',
                                  digits=(5, 2))

    def vacuum_discount(self):
        # self.ensure_one()

        self.env['ir.config_parameter'].set_param(
            'sale.order.max_disc_limit', 0)
        self.env['ir.config_parameter'].sudo().set_param('my.global.variable',
                                                         0)
