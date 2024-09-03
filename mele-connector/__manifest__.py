{
    'name': 'Mele Conector',
    'version': '1.0',
    'category': 'Retail',
    'summary': 'Transforma la gestión de tu retail con la integración en tiempo real del potente POS de Mele y Odoo.',
    'author': 'mele',
    'website': 'https://www.melecloud.com/pos',
    'depends': ['base', 'product','account','stock','sale','contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/invoice_views.xml',
        'views/product_views.xml',
    ],
    'images': [
        'static/description/icon.png',
        'static/banner/banner.png',
        'static/images/screenshot1.png',
        'static/images/screenshot2.png',
    ],
    'installable': True,
    'application': True,
}
