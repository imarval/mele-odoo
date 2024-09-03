import logging

from odoo import models, api
from ..services.api_service import ApiService

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _model = 'product'

    @api.model
    def create(self, vals):
        res = super(ProductTemplate, self).create(vals)
        ApiService.send_to_external_api('create', self._model, res)
        return res

    def write(self, vals):
        result = super(ProductTemplate, self).write(vals)
        ApiService.send_to_external_api('update', self._model, self)
        return result

    def unlink(self):
        for record in self:
            ApiService.send_to_external_api('delete', self._model, record)
        result = super(ProductTemplate, self).unlink()
        return result
