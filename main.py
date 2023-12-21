from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from flask_jwt_extended import JWTManager
import secrets

from api.utils.celery_config import make_celery
from api.views.cupons_ocr_view import CuponsPendentesOCR, cupons_ocr_swagger, CuponsPendentesDetail

from api.views.cupons_sem_imagem_view import CuponsSemFotoList, cupons_sem_imagem_swagger, CuponsSemFotoDetail
from api.views.cupons_view import CuponsList, CuponsDetails, cupons_swagger
from api.views.login import LoginList


app = Flask(__name__)

SWAGGER_URL = '/swagger'

api = Api(app,  version='1.0', title='Documentação API Cupons', description='API para o aplicativo de Cupons', doc=SWAGGER_URL)


api.add_resource(CuponsList, "/cupons")
api.add_resource(CuponsDetails,"/cupons/<int:id>")
api.add_namespace(cupons_swagger)

api.add_resource(CuponsPendentesOCR, "/cupons/ocr/pendentes")
api.add_resource(CuponsPendentesDetail,"/cupons/ocr/pendentes/<int:id>")
api.add_namespace(cupons_ocr_swagger)


api.add_resource(CuponsSemFotoList, "/cupons/sem_imagem")
api.add_resource(CuponsSemFotoDetail, "/cupons/sem_imagem/<int:id>")
api.add_namespace(cupons_sem_imagem_swagger)


api.add_resource(LoginList,"/login")


CORS(app, resources={r"/*": {"origins": "*"}})
app.config['JWT_SECRET_KEY'] = secrets.token_hex(32)
app.config.from_object('config')

jwt = JWTManager(app)



app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
celery = make_celery(app)







if __name__ == '__main__':
    app.run(host="0.0.0.0", port="3036", debug=True)


