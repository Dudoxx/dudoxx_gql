{
    'name': 'Dudoxx Attachment',
    'version': '1.0',
    'author': 'Walid Boudabbous, DUDOXX UG',
    'category': 'Document Management',
    'depends': ['base', 'web'],
    'data': [
       
        'security/security.xml',
        'security/access_rules.xml',
         'security/ir.model.access.csv',
        'views/dudoxx_attachment_views.xml',
        'views/main_menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'dudoxx_attachment/static/src/css/ddx_attachment_styles.css',
            'dudoxx_attachment/static/src/js/ddx_attachment_script.js'
        ],
    },
    'description': 'Module to handle attachments with CRUD operations.',
    'installable': True,
    'application': True,
    'auto_install': False
}
