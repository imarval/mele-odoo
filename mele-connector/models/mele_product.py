from odoo import models, fields # type: ignore

class MeleProduct(models.Model):
    _name = 'mele.product'
    _description = 'Mele Product'

    name = fields.Char(string='Product Name')
    qty_available = fields.Float(string='Quantity Available')
    list_price = fields.Float(string='Sale Price')

    def fetch_all_products(self):
        products = self.env['product.product'].search([])
        product_data = []
        for product in products:
            product_data.append({
                'name': product.name,
                'qty_available': product.qty_available,
                'list_price': product.list_price,
            })
        return product_data
