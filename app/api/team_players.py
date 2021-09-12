from .dao import QueryGenerator


class Team:

    def get_players(self, team_name: str, querygen: QueryGenerator) -> list:
        query = 'SELECT * FROM playersdata WHERE club=%s'
        return querygen.select(query, (team_name,))

    def get_player_string(self, string: dict,
                          querygen: QueryGenerator) -> list:
        query = '''SELECT * FROM playersdata WHERE name
        LIKE %s ORDER BY name {}'''.format(string.get('order', 'asc'))

        querystring = string.get('search', None)
        return querygen.select(query, (querystring+'%',))
