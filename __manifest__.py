{
    'name': 'Migration helper',
    'author':  'NTSW',
    'category': 'Sales',
    'sequence': 14,
    'summary': '',
    'license': 'AGPL-3',
    'images': [
    ],
    'depends': [
        'base',
        'account'
    ],
    'data': ['views/migrations_views.xml',
             'views/migrations_partner_views.xml'
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
