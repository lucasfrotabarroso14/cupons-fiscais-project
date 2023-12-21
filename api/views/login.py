from datetime import timedelta

from flask_restx import Resource
from flask import request, jsonify, make_response
import requests
from flask_jwt_extended import create_access_token
class LoginList(Resource):
    def post(self):
        login = request.json["login"]
        validation_url ='url do servico de login'
        response = requests.post(validation_url,json={"login": login})
        if response.status_code == 200:
            data = response.json()
            access_token = create_access_token(identity=data, expires_delta = timedelta(days=1))
            return make_response(jsonify({
                'message': 'Login realizado com sucesso',
                'access_token': access_token,
                'status': '200'

            }),200)
        elif response.status_code == 401:
            return make_response(
                jsonify(
                {
                    'message': 'Credenciais inválidas. Tente novamente',
                    'status': '401'

                 }
                       ),401)
        else:
            return make_response(
                jsonify(
                {
                    'message': 'Erro interno',
                    'status': '401'
                }
            ),500 )

