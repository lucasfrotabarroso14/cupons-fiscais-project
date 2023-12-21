import json
import base64
from flask import make_response, jsonify, request
from flask_restx import Resource,Namespace
from api.services import cupons_service
from datetime import datetime


from ..services.cupons_service import post_cupons
from ..utils.Serialize import Serialize



cupons_swagger = Namespace('cupons', description='Endpoints para cupons')
@cupons_swagger.route('/')
class CuponsList(Resource):
    def get(self):
        data, status = cupons_service.get_all()

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

    def post(self):
        data = request.get_json()
        bandeira_cartao = data.get('bandeira_do_cartao')
        imagem = data.get('imagem')
        forma_de_pagamento = data.get('forma_de_pagamento')
        # status_ocr = data.get("status_ocr")
        # resultado_ocr = data.get("resultado_ocr")

        if not bandeira_cartao or not forma_de_pagamento :
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
            'bandeira_do_cartao': bandeira_cartao,
            'imagem': imagem,
            'forma_de_pagamento': forma_de_pagamento,
            'codigo_pedido_interno': 'CIA178243HJ',
            'status': 'B',
            'nsu': '32105952',
            'autorizacao': '00000000041010',
            'codigo_filial': '02',
            'codigo_gerente': '888912',
            'codigo_vendedor': '02321',
            'data_hora_upload': datetime.today(),
            'data_hora_aceite': datetime.today(),
            "status_ocr": "Pendente",  # esses dados vao ser pegue do job
            "resultado_ocr": None  # vai ser pegue do job

        }
        # cupom_obj = {
        #     'bandeira_do_cartao':bandeira_cartao,
        #     'imagem':imagem,
        #     'forma_de_pagamento': forma_de_pagamento,
        #     'codigo_pedido_interno': 'CXA178243HJ',
        #     'status':'A',
        #     'nsu':'20105952',
        #     'autorizacao':'00000000041010',
        #     'codigo_filial': '02',
        #     'codigo_gerente':'999055',
        #     'codigo_vendedor':'023456',
        #     'data_hora_upload': datetime.today(),
        #     'data_hora_aceite': datetime.today(),
        #     "status_ocr": "Pendente", #esses dados vao ser pegue do job
        #     "resultado_ocr": "valor inicial" #vai ser pegue do job
        #
        # }
        res, status = post_cupons(cupom_obj)
        if status:
            response_data = {
                "status_code": 200,
                "status": True,
                "message": "Sucesso",
                "result": res
            }
            response = make_response(json.dumps(response_data, default=Serialize.serialize), 200)
            response.headers["Content-Type"] = "application/json"
            return response



@cupons_swagger.route('/<int:id>')
class CuponsDetails(Resource):
    def delete(self, id):
        data, status = cupons_service.deletar_cupom(id)
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

    def get(self,id):
        data, status = cupons_service.get_by_id(id)
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
            'data_hora_upload':  datetime.today(),
            'data_hora_aceite': data_hora_aceite,
            'status_ocr':'pendente',
            'resultado_ocr': None

        }

        data, status =cupons_service.update(id,cupom_obj)
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






