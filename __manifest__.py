# -*- coding: utf-8 -*-
#############################################################################
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2022-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#############################################################################
{
    'name': 'Sale Order Multi Lot Selection',
    'summary': """Multi Lot Selection on Sale Orders""",
    'description': """Multi Lot Selection on Sale Orders""",
    'application': 'True',
    'sequence': '3',
    'version': '16.0.1.0.0',
    'author': 'Cybrosys Techno solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "http://www.cybrosys.com",
    'category': 'sales',
    'licence': 'LGPL-3',
    'depends': ['base', 'sale', 'sale_management', 'stock'],
    'data': [
        'views/sale_order_views.xml'
    ],
    'images': ['static/description/banner.png']

}
