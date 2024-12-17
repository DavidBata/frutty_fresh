
{
    'name': 'Frutty Fresh',
    'version': '1.2',
    'category': 'Sales/Sales',
    'summary': 'reporte doble para ventas',
    'description': """
    Custom report doble, for sale order
    """,
    'depends': [
        'base',
        'sale', 
        'web' 
    ],
    'data': [
        'views/peformance.xml',
        'views/template_sale_order.xml',
        'views/template_sale_order_doble.xml'
        
    ],

    'installable': True,
    'license': 'LGPL-3',
}
