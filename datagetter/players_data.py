from datagetter.database import Database


def insert_data(names, positions, nations, clubs):
    db_object = Database()
    connection, cursor = db_object.create_connection()
    query = '''INSERT INTO playersdata (name, position, nation, club)
        VALUES(%s, %s, %s, %s)'''

    try:
        cursor.executemany(query, zip(names, positions, nations, clubs))
        connection.commit()
        print('Datos agregados a la base de datos')

    except Exception as ex:
        print('No se han podido ingresar los datos por: ', ex)

    finally:
        connection.close()
