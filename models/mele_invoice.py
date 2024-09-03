from odoo import models, fields # type: ignore

class MeleInvoice(models.Model):
    _name = 'mele.invoice'
    _description = 'Mele Invoice'

    name = fields.Char(string='Invoice Number')
    partner_id = fields.Many2one('res.partner', string='Partner')
    amount_total = fields.Float(string='Total Amount')
    external_reference = fields.Char(string='External Reference')
    company_id = fields.Many2one('res.company', string='Company')