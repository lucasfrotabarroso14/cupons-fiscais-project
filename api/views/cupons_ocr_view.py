import json

from flask import make_response, jsonify, request
from flask_restx import Resource,Namespace
from datetime import datetime

from ..services import cupons_service, cupons_ocr_service
from ..services.cupons_ocr_service import get_cupons_pendentes_ocr
from ..utils.Serialize import Serialize

cupons_ocr_swagger = Namespace('cupons/ocr/pendentes', description='Endpoints para o serviço de OCR')

@cupons_ocr_swagger.route('/')
class CuponsPendentesOCR(Resource):
    def get(self):
        data, status = get_cupons_pendentes_ocr()

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
                "message": "Erro",
                "result": data
            }
            response = make_response(json.dumps(response_data), 404)
            response.headers['Content-Type'] = 'application/json'
            return response

@cupons_ocr_swagger.route('/<int:id>')
class CuponsPendentesDetail(Resource):
    def get(self,id):
        data, status = cupons_ocr_service.get_cupons_pendentes_ocr_by_id(id)
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


    def put(self,id):
        data = request.get_json()
        imagem = data.get('imagem')
        resultado_ocr = data.get('resultado_ocr')
        data_hora_upload = data.get('data_hora_upload')


        if not resultado_ocr:
            response_data = {
                "status_code": 404,
                "status": False,
                "message": "Campo obrigatório está faltando na solicitação.",
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
            'data_hora_upload': data_hora_upload,
            'data_hora_aceite': datetime.today(),
            'status_ocr':'concluido',
            'resultado_ocr': resultado_ocr

        }

        data, status =cupons_ocr_service.update(id,cupom_obj)
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

