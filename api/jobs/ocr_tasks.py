from celery import Celery
import time
# Importações e configuração do Celery
from config import execute_query

celery = Celery(
    'myapp',  # Nome do aplicativo Celery
    broker='redis://localhost:6379/0',  # URL do broker (pode ser Redis, RabbitMQ, etc)
    backend='redis://localhost:6379/1'  # URL do backend para resultados
)

@celery.task
def realizar_ocr(cupom_id):
    try:
        time.sleep(10)  # Simulação do tempo de processamento
        atualizar_status_ocr(cupom_id, "Concluido", "estado 02 (OCR REALIZADO)")
    except Exception as e:
        atualizar_status_ocr(cupom_id, "Falhou", str(e))

def processar_ocr(cupom_id):
    atualizar_status_ocr(cupom_id, "Em processamento", "estado 01")
    realizar_ocr.delay(cupom_id)

def atualizar_status_ocr(cupom_id, status_ocr, resultado_ocr):
    query = """
    UPDATE cupons
    SET 
    status_ocr = %s,
    resultado_ocr = %s
    WHERE id = %s
    """
    params = (status_ocr, resultado_ocr, cupom_id)
    execute_query(query, params)



# @celery.task
# def check_task_status(task_id):
#     result = AsyncResult(task_id)
#     if result.ready():
#         return {
#             'status': 'completed',
#             'result': result.result
#         }
#     elif result.failed():
#         return {
#             'status': 'failed',
#             'error_message': result.traceback
#         }
#     else:
#         return {
#             'status': 'pending'
#         }