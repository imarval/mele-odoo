{
    'name': 'Conector Mele para Odoo',
    'version': '1.0',
    'category': 'Retail',
    'summary': 'Transforma la gestión de tu retail con la integración en tiempo real del potente POS de Mele y Odoo.',
    'description': """
        <p><strong>Optimiza tu gestión de retail con la integración perfecta entre Mele y Odoo.</strong></p>

        <p><strong>¿Qué es el Conector Mele para Odoo?</strong></p>
        <p>El Conector Mele para Odoo lleva tu experiencia de gestión retail al siguiente nivel al integrar el sofisticado sistema de punto de venta (POS) de Mele con el versátil ERP de Odoo. Diseñado para grandes retailers y pequeños negocios por igual, Mele destaca por su facilidad de uso y sus funcionalidades avanzadas, haciendo de este conector una herramienta esencial para una gestión de retail eficiente y moderna.</p>

        <p><strong>Ventajas clave del Conector:</strong></p>
        <ul>
            <li><strong>Integración Fluida:</strong> Une la potencia del POS de Mele con la flexibilidad del ERP de Odoo, garantizando una sincronización precisa y efectiva.</li>
            <li><strong>Sincronización en Tiempo Real:</strong> Conecta tus ventas en el POS de Mele directamente con Odoo, asegurando que tus datos estén siempre actualizados.</li>
            <li><strong>Actualización Automática de Productos:</strong> Cambios en Odoo como nombre, precio o stock se reflejan instantáneamente en el POS de Mele, manteniendo la coherencia en tu inventario.</li>
            <li><strong>Eficiencia Mejorada:</strong> Optimiza la gestión de inventario y ventas con una integración que facilita la administración y reduce los errores manuales.</li>
        </ul>

        <p><strong>¿Por qué elegir este conector?</strong></p>
        <p>Al elegir el Conector Mele para Odoo, maximizarás el potencial de ambas plataformas, mejorando la eficiencia operativa y elevando la experiencia de tus clientes. No más procesos manuales y desactualización; simplemente una sincronización perfecta que te permite enfocarte en lo que realmente importa: hacer crecer tu negocio.</p>

        <p><strong>Aprovecha el poder combinado de Mele y Odoo para transformar tu gestión de retail hoy mismo.</strong></p>
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
        'static/description/screenshot2.png',
    ],
    'installable': True,
    'application': True,
}
