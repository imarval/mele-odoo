from odoo import models, fields, api # type: ignore

class MeleStockQuant(models.Model):
    _name = 'mele.stock.quant'
    _description = 'Stock Quant for Mele'


    def get_all_records(self):
        return "hola mundo"
    
    def test_method(self):
        return "test success"

    @api.model
    def update_product_stock(self, product_id, location_id, new_quantity):
        if product_id is None or new_quantity is None:
            raise ValueError("Product ID and New Quantity must not be None")
        
        product = self.env['product.product'].browse(product_id)
        if product.type != 'product':
            raise ValueError(f"El producto con ID {product_id} no es un producto almacenable.")

        quant = self.env['stock.quant'].search([
            ('product_id', '=', product_id)
        ], limit=1)

        if quant:
            quant.sudo().write({'quantity': new_quantity})
            return f"Stock actualizado para el producto {product.name} en la ubicación {location_id}."
        else:
            self.env['stock.quant'].sudo().create({
                'product_id': product_id,
                'location_id': location_id,
                'quantity': new_quantity,
            })

            return f"Nuevo stock creado para el producto {product.name} en la ubicación {location_id}."
