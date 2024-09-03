import logging
import requests
import time

from odoo import models

_logger = logging.getLogger(__name__)


class ApiService(models.AbstractModel):
    _name = 'api.service'

    @staticmethod
    def send_to_external_api(event_type, model_name, record):
        # TODO: Parametrizar url sync orchestator api
        api_url = 'http://localhost:5172/sync'
        headers = {'Content-Type': 'application/json'}

        data = {
            "event_type": event_type,
            "model": model_name,
            "data": {}
        }

        for field_name, field in record.fields_get().items():
            if field_name in record:  # and field_name != 'id':
                value = record[field_name]
                data['data'][field_name] = ApiService._serialize_field(value)

        try:
            _logger.info(
                f"Sending event to Mele: "
                f"Event type: {event_type} "
                f"Model: {model_name} "
                f"Record: {data['data']['id']} - {data['data']['display_name']}"
            )


            start_time = time.time()
            response = requests.post(api_url, json=data, headers=headers)
            response.raise_for_status()
            end_time = time.time()

            # TODO: Para mantener el formato de logging de odoo
            # se imprime version de http raw.version returns 10 for HTTP/1.0 and 11 for HTTP/1.1
            protocol_version = response.raw.version / 10
            elapsed_time = end_time - start_time

            request_line = f"{response.request.method} {response.request.url} HTTP/{protocol_version:.1f}"

            logger.info(f'"{request_line}" {response.status_code} - {elapsed_time:.3f}')

        except requests.exceptions.RequestException as e:
            _logger.error('ERROR AL ENVIAR EL REQUEST A API EXTERNA', e)
            record.env['ir.logging'].sudo().create({
                'name': 'Mele Sync',
                'type': 'server',
                'message': f'Error: {str(e)}',
                'path': 'api_service',
                'func': 'send_to_external_api',
                'line': '13',
            })

    @staticmethod
    def _serialize_field(value):
        """Convierte items a tipos de datos serializables"""
        if isinstance(value, models.BaseModel):
            return value.id
        elif isinstance(value, (list, tuple)):
            return [ApiService._serialize_field(v) for v in value]
        elif isinstance(value, dict):
            return {k: ApiService._serialize_field(v) for k, v in value.items()}
        elif isinstance(value, (int, float, bool, str)):
            return value
        elif value is None:
            return value
        else:
            return str(value)
