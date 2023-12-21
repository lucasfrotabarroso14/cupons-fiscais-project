import psycopg2

DATABASE = {
    'database': 'exampledb',
    'host': 'localhost',
    'user': 'docker',
    'password': 'docker',
    'port': '5440'
}


import psycopg2

def execute_query(query, params=None):
    conn = None
    try:
        conn = psycopg2.connect(**DATABASE)
        cursor = conn.cursor()
        formatted_query = query.strip().replace("\n", "")

        if formatted_query.split(' ')[0] == "SELECT":
            cursor.execute(formatted_query, params)
            results = cursor.fetchall()

            column_names = [desc[0] for desc in cursor.description]

            data = []
            for row in results:
                data.append(dict(zip(column_names, row)))
            return data, True
        else:
            if "RETURNING" in formatted_query:
                cursor.execute(formatted_query, params)
                result = cursor.fetchone()[0]  # Obtém o valor retornado (ID)
            else:
                cursor.execute(formatted_query, params)
                result = cursor.rowcount

            conn.commit()
            return result, True

    except psycopg2.Error as e:
        return str(e), False
    finally:
        if conn:
            cursor.close()
            conn.close()



