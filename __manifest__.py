{
    'name': 'Mele Connector',
    'version': '1.0.0',
    'summary': 'Integrador de Odoo con Mele POS',
    'description': """
        Este módulo permite a Odoo integrarse con Mele, permitiendo a usuarios Odoo
        usar toda la potencia de los servicios Mele.

        Este módulo tambien permite ver las facturas que se suben desde una aplicación externa en una vista específica.
    """,
    'author': 'mele-dev',
    'category': 'Connector',
    'depends': ['base', 'product','account','stock','sale','contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/invoice_views.xml',
        'views/product_views.xml',
    ],
    'installable': True,
    'application': True,
}
