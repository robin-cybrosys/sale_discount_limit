{
    'name': "Discount Limit",

    'application': "True",

    'sequence': "3",

    'author': "Cybrosys Technologies",

    'website': "http://www.cybrosys.com",

    'category': 'sales',

    'version': '15.0.1.0.0',

    'licence': "LGPL-3",

    'depends': ['base', 'sale', 'sale_management', 'mail'],

    'data': [
        # 'security/ir.model.access.csv',
        'data/scheduler.xml',
        'views/sale_discount_views.xml',
        'views/res_config_settings_views.xml',
    ],

}
