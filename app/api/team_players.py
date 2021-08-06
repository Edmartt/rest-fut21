from .db import get_db

class Team:

    def get_players(self, team_name: str) -> list:
        connection, cursor = get_db()
        query = 'SELECT * FROM playersdata WHERE club=%s'

        try:
            cursor.execute(query, (team_name,))
            result = cursor.fetchall()
            if result:
                return result

        except Exception as ex:
            print(ex)
        finally:
            connection.close()


    def get_player_string(self, string: str) -> list:
        connection, cursor = get_db()
        query = 'SELECT * FROM playersdata WHERE name LIKE %s ORDER BY name {}'.format(string.get('order', 'asc'))

        qstring1 = string.get('search', None)

        try:
            cursor.execute(query, (qstring1+"%",))
            result = cursor.fetchall()
            if result:
                return result

        except Exception as ex:
            print(ex)

        finally:
            connection.close()
