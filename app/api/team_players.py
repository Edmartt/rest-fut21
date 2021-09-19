from .dao import QueryGenerator


class Team:

    def get_players(self, team_name: str, querygen: QueryGenerator) -> list:
        '''Returns all the pleyers from a team.

        :param: team_name: str: the name of the team you want to know
        the players in the team.

        :param: querygen: object for accesing database methods.

        :return: list
        '''
        query = 'SELECT * FROM playersdata WHERE club=%s'
        return querygen.select(query, (team_name,))

    def get_player_string(self, string: dict,
                          querygen: QueryGenerator) -> list:
        '''
        Returns all the coincidences related to players sent in a querystring.

        :param: string: dict: key value sent in a querystring from a
        get request. The expected key is order and the possible values are
        asc or desc, by default the value is asc.

        '''
        query = '''SELECT * FROM playersdata WHERE name
        LIKE %s ORDER BY name {}'''.format(string.get('order', 'asc'))

        querystring = string.get('search', None)
        return querygen.select(query, (querystring+'%',))
