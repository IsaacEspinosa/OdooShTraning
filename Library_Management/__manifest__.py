# -*- coding: utf-8 -*-
{
    'name': 'Library Management',
    
    'summary': """Module that will manage many aspects of the Library""",
    
    'description': """
    Odoo
        Book1
        Book2
    """,
    
    'autor': 'Isaac',
    
    'website': 'https:www.WEB.com',
    
    'category':'Training',
    'version':'0.1',
    
    'depends': ['base'],
    
    'data':[
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/books_views.xml',
        'views/rentals_views.xml',
        'views/library_menu.xml',
    ],
    'demo':[
        #'demo/demo_data.xml'
    ],
}