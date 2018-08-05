# -*- coding: utf-8 -*-
{
    'name': "Employee Mod for Doyarushka",

    'summary': """
        This is an "hr.employee" model mod for Doyarushka""",

    'description': """

    """,

    'author': "Ivan Sova",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
	'license':'LGPL-3',
    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_recruitment'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/hr_views.xml',
        'views/hr_settings_views.xml',
        'views/templates.xml',
        'data/cron.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}