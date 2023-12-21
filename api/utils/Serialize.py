import json
import base64
from flask import make_response, jsonify
from flask_restx import Resource
from api.services import cupons_service
from datetime import datetime

class Serialize():

    def serialize_datetime(obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        raise TypeError("Object of type {} is not JSON serializable".format(type(obj).__name__))

    def serialize_memoryview(obj): #retorna base64
        if isinstance(obj, memoryview):

            return base64.b64encode(obj).decode('utf-8')
        raise TypeError("Object of type {} is not JSON serializable".format(type(obj).__name__))

    # def serialize_memoryview(obj): #igual a tabela
    #     if isinstance(obj, memoryview):
    #         # Converte o memoryview em uma representação hexadecimal
    #         return obj.tobytes().hex()
    #     raise TypeError("Object of type {} is not JSON serializable".format(type(obj).__name__))

    # @staticmethod
    # def serialize_memoryview(obj): # com a \\ no comeco:
    #     if isinstance(obj, memoryview):
    #         # Converte o memoryview em uma representação hexadecimal com o prefixo \x
    #         hex_data = obj.tobytes().hex()
    #         return "\\x" + hex_data
    #     raise TypeError("Object of type {} is not JSON serializable".format(type(obj).__name__))

    def serialize(obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, memoryview):
            return Serialize.serialize_memoryview(obj)
        else:
            return obj