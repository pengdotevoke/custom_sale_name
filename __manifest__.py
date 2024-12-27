{
    'name': 'Custom Sale Slip',
    'version': '1.0',
    'summary': 'Add LPO and Invoice Number to Delivery Slip',
    'author': 'James Otieno',
    'depends': ['stock', 'account', 'sale', 'sale_stock'],
    'data': [
        'views/account_move_views.xml',
    ],
    'installable': True,
    'application': False,
}
