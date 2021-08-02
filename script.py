import requests
from datagetter.database import Database
from datagetter.players_data import insert_data


def get_data(url="https://www.easports.com/fifa/ultimate-team/api/fut/item",
             page=1):

    db_object = Database()
    db_object.create_table()

    args = {'page': page} if page else {}

# listas con las propiedades de los jugadores
    player_names = []
    players_positions = []
    players_nations = []
    players_clubs = []

    response = requests.get(url, params=args).json()

    for i in response['items']:

        player_names.append(i['firstName'] + ' ' + i['lastName'])
        players_positions.append(i['position'])
        players_nations.append(i['nation']['name'])
        players_clubs.append(i['club']['name'])
    insert_data(player_names, players_positions, players_nations,
                players_clubs)

    choice = input('Do you want to read the next page (Y/N): '.lower())
    page += 1
    if choice == 'y' and page <= 908:
        get_data(url, page)


get_data()
