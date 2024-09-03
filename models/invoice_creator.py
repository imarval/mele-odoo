from odoo import models, fields, api

class InvoiceCreator(models.Model):
    _name = 'invoice.creator'
    _description = 'Invoice Creator'

    partner_id = fields.Many2one('res.partner', string='Customer', required=True)
    invoice_date = fields.Date(string='Invoice Date', required=True, default=fields.Date.context_today)
    invoice_line_ids = fields.One2many('invoice.creator.line', 'invoice_creator_id', string='Invoice Lines')

    def create_invoice(self):
        # Obtener el impuesto del IVA
        tax = self.env['account.tax'].search([('name', '=', 'IVA 21%')], limit=1)
        if not tax:
            raise ValueError("No se encontró un impuesto llamado 'IVA'.")

        # Obtener el diario de ventas
        journal = self.env['account.journal'].search([('type', '=', 'sale')], limit=1)
        if not journal:
            raise ValueError("No se encontró un diario de ventas.")

        # Preparar valores para la factura
        invoice_vals = {
            'move_type': 'out_invoice',
            'partner_id': self.partner_id.id,
            'invoice_date': self.invoice_date,
            'journal_id': journal.id,  # Incluir el diario
            'invoice_line_ids': [(0, 0, {
                'product_id': line.product_id.id,
                'quantity': line.quantity,
                'price_unit': line.price_unit,
                'tax_ids': [(6, 0, [tax.id])],  # Incluir el impuesto del IVA
            }) for line in self.invoice_line_ids],
        }

        # Incluir el tipo de documento si está disponible y es relevante para tu localización
        if hasattr(journal, 'l10n_latam_document_type_id'):
            if journal.l10n_latam_document_type_id:
                invoice_vals['l10n_latam_document_type_id'] = journal.l10n_latam_document_type_id.id
            else:
                raise ValueError("El diario de ventas no tiene configurado un tipo de documento.")

        # Crear la factura
        invoice = self.env['account.move'].create(invoice_vals)
        
        # Publicar la factura
        invoice.action_post()

        # Crear un pedido de venta
        sale_order_vals = {
            'partner_id': self.partner_id.id,
            'order_line': [(0, 0, {
                'product_id': line.product_id.id,
                'product_uom_qty': line.quantity,
                'price_unit': line.price_unit,
                'tax_id': [(6, 0, [tax.id])],
            }) for line in self.invoice_line_ids],
        }
        sale_order = self.env['sale.order'].create(sale_order_vals)
        
        # Confirmar el pedido de venta
        sale_order.action_confirm()
        
        # validar pedido
        for picking in sale_order.picking_ids:
            picking.action_assign()
            for move in picking.move_lines:
                move.quantity_done = move.product_uom_qty  # Validar todas las cantidades
            picking.button_validate()


        # Registrar un pago para marcar la factura como pagada
        payment_register = self.env['account.payment.register'].with_context(active_model='account.move', active_ids=invoice.ids).create({
            'payment_date': fields.Date.context_today(self),
            'journal_id': self.env['account.journal'].search([('type', '=', 'bank')], limit=1).id,
            'amount': invoice.amount_total,
        })
        payment_register.action_create_payments()

        return {
            'id': invoice.id,
            'name': invoice.name,
            'partner_id': invoice.partner_id.id,
            'invoice_date': invoice.invoice_date,
            'amount_total': invoice.amount_total,
            'state': invoice.state,
        }

class InvoiceCreatorLine(models.Model):
    _name = 'invoice.creator.line'
    _description = 'Invoice Creator Line'

    product_id = fields.Many2one('product.product', string='Product', required=True)
    quantity = fields.Float(string='Quantity', required=True, default=1.0)
    price_unit = fields.Float(string='Unit Price', required=True)
    invoice_creator_id = fields.Many2one('invoice.creator', string='Invoice Creator Reference', required=True, ondelete='cascade')
