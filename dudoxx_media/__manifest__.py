{
    'name': 'Dudoxx Media Manager',
    'version': '1.0',
    'category': 'Healthcare',
    'summary': 'Modern Media Manager for Medical Audio and Images',
    'description': """
        Dudoxx Media Manager
        ====================
        This module provides a modern, user-friendly UI for storing, managing, 
        and processing medical audio and image files in a healthcare setting.
    """,
    'author': 'Walid Boudabbous, Dudoxx UG',
    'website': 'https://www.dudoxx.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'security/access_rules.xml',
        'views/dudoxx_media_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'dudoxx_media/static/src/css/dudoxx_media.css',
            'dudoxx_media/static/src/js/dudoxx_media_widgets.js',
        ],
    },
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}