from odoo import api, fields, models, _
class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    
