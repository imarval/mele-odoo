from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    document_number = fields.Char(string='Document Number')

    @api.model
    def create_customer(self, vals):
        # Crear un nuevo cliente
        customer = self.create(vals)
        return customer.id

    @api.model
    def list_customers(self):
        # Listar todos los clientes
        customers = self.search([])
        return customers.read(['id', 'name', 'email', 'phone', 'street', 'document_number'])
