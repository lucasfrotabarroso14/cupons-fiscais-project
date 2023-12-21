import base64
from api.jobs.ocr_tasks import processar_ocr
from config import execute_query


def get_cupom_sem_foto():
    query = """
    SELECT 
    id,bandeira_do_cartao,imagem,forma_de_pagamento,codigo_pedido_interno,status,nsu,autorizacao,codigo_filial,codigo_gerente,
    codigo_vendedor,data_hora_upload,data_hora_aceite
    FROM 
    cupons
    WHERE
    imagem IS NULL

    """
    result, status = execute_query(query, {})
    if status:
        return result, 200
    else:
        return [], 404

def get_cupom_sem_imagem_by_id(id):
    query = """
    SELECT
    *
    FROM
    cupons
    WHERE
    id = %(id)s
    """
    params={"id": id}
    result, status = execute_query(query, params)

    if status:
        return result, 200
    else:
        return [], 404
