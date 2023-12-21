import json

from datetime import datetime
from flask import make_response
from flask_restx import Resource,Namespace
from api.services import cupons_service, cupons_sem_imagem_service
from ..services.cupons_sem_imagem_service import get_cupom_sem_foto
from flask import make_response, jsonify, request
from ..utils.Serialize import Serialize



cupons_sem_imagem_swagger = Namespace('cupons/sem_imagem', description='Endpoints para o Front-End (cupons sem imagem) ')

@cupons_sem_imagem_swagger.route('/')
class CuponsSemFotoList(Resource):
    def get(self):
        data, status = get_cupom_sem_foto()
        if status:
            response_data = {
                "statusCode": 200,
                "status": True,
                "message": "Sucesso",
                "result": data
            }
            response = make_response(json.dumps(response_data, default=Serialize.serialize), 200)
            response.headers["Content-Type"] = "application/json"
            return response

        else:
            response_data = {
                "statusCode": 404,
                "status": False,
                "message": "Sucesso",
                "result": data
            }
            response = make_response(json.dumps(response_data), 404)
            response.headers['Content-Type'] = 'application/json'
            return response

@cupons_sem_imagem_swagger.route('/<int:id>')
class CuponsSemFotoDetail(Resource):
    def get(self, id):
        data, status = cupons_sem_imagem_service.get_cupom_sem_imagem_by_id(id)
        if status:
            response_data = {
                "status_code": 200,
                "status": True,
                "message": "Sucesso",
                "result": data
            }
            response = make_response(json.dumps(response_data, default=Serialize.serialize), 200)
            response.headers["Content-Type"] = "application/json"
            return response

        else:
            response_data = {
                "status_code": 404,
                "status": False,
                "message": "Sucesso",
                "result": data
            }
            response = make_response(json.dumps(response_data), 404)
            response.headers['Content-Type'] = 'application/json'
            return response

    def put(self, id):
        data = request.get_json()
        bandeira_cartao = data.get('bandeira_do_cartao')
        imagem = data.get('imagem', None)
        forma_de_pagamento = data.get('forma_de_pagamento')
        data_hora_aceite = data.get('data_hora_aceite')
        if not bandeira_cartao or not forma_de_pagamento:
            response_data = {
                "status_code": 404,
                "status": False,
                "message": "Campos obrigatórios estão faltando na solicitação.",
                "result": data
            }
            response = make_response(json.dumps(response_data), 404)
            response.headers['Content-Type'] = 'application/json'
            return response

        cupom_obj = {
            'bandeira_do_cartao': "teste",
            'imagem': imagem,
            'forma_de_pagamento': 'teste',
            'codigo_pedido_interno': 'CXA178243HJ',
            'status': 'A',
            'nsu': '20105952',
            'autorizacao': '00000000041010',
            'codigo_filial': '02',
            'codigo_gerente': '999055',
            'codigo_vendedor': '023456',
            'data_hora_upload': datetime.today(),
            'data_hora_aceite': data_hora_aceite,
            'status_ocr': 'pendente',
            'resultado_ocr': None

        }

        data, status = cupons_service.update(id, cupom_obj)
        if status:
            response_data = {
                "status_code": 200,
                "status": True,
                "message": "Sucesso",
                "result": data
            }
            response = make_response(json.dumps(response_data, default=Serialize.serialize), 200)
            response.headers["Content-Type"] = "application/json"
            return response

        else:
            response_data = {
                "status_code": 404,
                "status": False,
                "message": "Sucesso",
                "result": data
            }
            response = make_response(json.dumps(response_data), 404)
            response.headers['Content-Type'] = 'application/json'
            return response



