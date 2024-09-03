{
    'name': 'Conector Mele para Odoo',
    'version': '1.0',
    'category': 'Retail',
    'summary': 'Transforma la gestión de tu retail con la integración en tiempo real del potente POS de Mele y Odoo.',
    'description': """
        **Optimiza tu gestión de retail con la integración entre Mele y Odoo.**

        **¿Qué es el Conector Mele para Odoo?**
        El Conector Mele para Odoo lleva tu experiencia de gestión retail al siguiente nivel al integrar el sofisticado sistema de punto de venta (POS) de Mele con el versátil ERP de Odoo. Diseñado para grandes retailers y pequeños negocios por igual, Mele destaca por su facilidad de uso y sus funcionalidades avanzadas, haciendo de este conector una herramienta esencial para una gestión de retail eficiente y moderna.

        **Ventajas clave del Conector:**
        - **Integración Fluida:** Une la potencia del POS de Mele con la flexibilidad del ERP de Odoo, garantizando una sincronización precisa y efectiva.
        - **Sincronización en Tiempo Real:** Conecta tus ventas en el POS de Mele directamente con Odoo, asegurando que tus datos estén siempre actualizados.
        - **Actualización Automática de Productos:** Cambios en Odoo como nombre, precio o stock se reflejan instantáneamente en el POS de Mele, manteniendo la coherencia en tu inventario.
        - **Eficiencia Mejorada:** Optimiza la gestión de inventario y ventas con una integración que facilita la administración y reduce los errores manuales.

        **¿Por qué elegir este conector?**
        Al elegir el Conector Mele para Odoo, maximizarás el potencial de ambas plataformas, mejorando la eficiencia operativa y elevando la experiencia de tus clientes. No más procesos manuales y desactualización; simplemente una sincronización perfecta que te permite enfocarte en lo que realmente importa: hacer crecer tu negocio.

        Aprovecha el poder combinado de Mele y Odoo para transformar tu gestión de retail hoy mismo.
    """,
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
        'static/description/screenshot1.png',
        'static/description/screenshot2.png'
    ],
    'installable': True,
    'application': True,
}
