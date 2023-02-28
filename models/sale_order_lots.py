# -*- coding: utf-8 -*-
"""Sale Order Multi Lot Selection"""
################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2017-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Robin K(<robin@cybrosys.info>)
#
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
################################################################################

from odoo import models, api, fields


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    multi_lot_ids = fields.Many2many('stock.lot',
                                     'multi_lot_ids_rel', string="Lots")
    product_type = fields.Boolean(compute='_compute_product_type')

    @api.depends('product_id')
    def _compute_product_type(self):
        for rec in self:
            if rec.product_id and rec.product_id.type == 'product':
                rec.product_type = True
            else:
                rec.product_type = False


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        self.env['stock.picking.type'].search(
            [('code', '=', 'outgoing')]).show_operations = False
        for rec in self.order_line:
            if rec.product_type:
                move_lines_vals = []
                for item in rec.multi_lot_ids.ids:
                    move_lines_vals.append({
                        'picking_id': self.picking_ids.id,
                        'product_id': rec.product_id.id,
                        'location_id': self.picking_ids.location_id.id,
                        'location_dest_id': self.picking_ids.location_dest_id.id,
                        'owner_id': rec.product_id.seller_ids.partner_id.id,
                        'qty_done': 0,
                        'lot_id': item
                    })

                print(move_lines_vals,'first')
                picking_id = self.env['stock.move.line'].search(
                    [('picking_id', '=', self.picking_ids.id),
                     ('product_id', '=', rec.product_id.id),
                     ('reserved_uom_qty', '=', 0)
                     ])
                if not picking_id:
                    self.env['stock.move.line'].create(move_lines_vals)

        return res


class StockMove(models.Model):
    _inherit = "stock.move"

    def action_show_details(self):
        self.ensure_one()
        action = super().action_show_details()
        action['views'] = [
            (self.env.ref('stock.view_stock_move_operations').id, 'form')]
        action['context'].update({
            'show_lots_m2o': True,
            'show_lots_text': False,
            'force_manual_consumption': True,
            'show_source_location': False,
            'show_destination_location': False,
            'show_reserved_quantity': True,
            'show_owner': True
        })
        return action
