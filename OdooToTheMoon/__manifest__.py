# -*- coding: utf-8 -*-
{
    'name': 'Odoo To The Moon',
    
    'summary': """Module to travel to the moon""",
    
    'description': """
    Odoo
        Moon1
        Moon2
    """,
    
    'autor': 'Isaac',
    
    'website': 'https:www.WEB.com',
    
    'category':'Training',
    'version':'0.1',
    
    'depends': ['base'],
    
    'data':[
        'security/ship_security.xml',
        'security/ir.model.access.csv',
        'views/spaceship_views.xml',
        'views/spaceship_menu.xml',
        'demo/demo_data.xml',
    ],
    'demo':[
        #'demo/demo_data.xml'
    ],
}