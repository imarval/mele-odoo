from odoo import models, fields, api

class AccountInvoiceQuery(models.Model):
    _inherit = 'account.move'

    # Puedes agregar campos adicionales si es necesario
    custom_field = fields.Char(string="Custom Field")

    @api.model
    def query_invoices(self, date_from, date_to):
        domain = [('invoice_date', '>=', date_from), ('invoice_date', '<=', date_to), ('move_type', '=', 'out_invoice')]
        invoices = self.search(domain)
        return invoices
