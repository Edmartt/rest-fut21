from os import environ
import mysql.connector


class Database():

    def create_connection(self):
        connection = mysql.connector.connect(
            host=environ.get('MYSQL_HOST'),
            user=environ.get('MYSQL_USER'),
            password=environ.get('MYSQL_PASSWORD'),
            database=environ.get('MYSQL_DB')
            )
        cursor = connection.cursor(prepared=True)

        return connection, cursor

    def create_table(self):
        querys = [
                'DROP TABLE IF EXISTS playersdata;',
                """CREATE TABLE IF NOT EXISTS playersdata (id INT UNSIGNED NOT NULL
                PRIMARY KEY
                AUTO_INCREMENT, name VARCHAR(60) NOT NULL, position VARCHAR(60)
                NOT NULL, nation VARCHAR(60) NOT NULL, club VARCHAR(60) NOT NULL)
                DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;"""
                ]

        connection, cursor = self.create_connection()

        try:
            for query in querys:
                cursor.execute(query)
            connection.commit()
            print('Tables created')
        except mysql.connector.Error as ex:
            print(ex)
        finally:
            connection.close()
