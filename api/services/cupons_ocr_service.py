import base64


from api.jobs.ocr_tasks import processar_ocr
from config import execute_query


def get_cupons_pendentes_ocr():
    query = """
    SELECT id,imagem, status_ocr, resultado_ocr,data_hora_upload
    FROM CUPONS
    WHERE
    status_ocr = 'pendente' 
    AND
    imagem IS NOT NULL
    
    
    """
    result, status = execute_query(query, {})
    if status:
        return result, 200
    else:
        return [], 404

def get_cupons_pendentes_ocr_by_id(id):
    query = """
    SELECT
    id,imagem, status_ocr, resultado_ocr,data_hora_upload
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


def update(id, obj):
    query = """
    UPDATE 
    cupons
    SET
            bandeira_do_cartao = %s,
            imagem = %s,
            forma_de_pagamento = %s,
            codigo_pedido_interno = %s,
            status = %s,
            nsu = %s,
            autorizacao = %s,
            codigo_filial = %s,
            codigo_gerente = %s,
            codigo_vendedor = %s,
            data_hora_upload = %s ,
            data_hora_aceite = %s ,
            status_ocr = %s,
            resultado_ocr = %s

        WHERE
        id = %s
    """
    params = (
        obj["bandeira_do_cartao"],
        obj["imagem"],
        obj["forma_de_pagamento"],
        obj['codigo_pedido_interno'],
        obj['status'],
        obj['nsu'],
        obj['autorizacao'],
        obj['codigo_filial'],
        obj['codigo_gerente'],
        obj['codigo_vendedor'],
        obj['data_hora_upload'],
        obj['data_hora_aceite'],
        obj['status_ocr'],
        obj['resultado_ocr'],
        id
    )

    result, status = execute_query(query, params)

    if status:

        query = """
        SELECT
         id,status_ocr,resultado_ocr,data_hora_aceite
         FROM
        cupons 
        WHERE 
        id = %s
        """

        params = (id,)
        result, status = execute_query(query, params)
        return result[0], 200
    else:
        return 'Erro ao ao atualizar o registro.', 404














