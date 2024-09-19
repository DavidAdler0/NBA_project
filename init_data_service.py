import requests
from db import db
from player_model import PlayerData


def get_season_data_from_API(season):
    url = "http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?"
    params = {'season': season, 'pageSize': 1000}
    response = requests.get(url, params=params)
    data = response.json()
    return data


def update_data_to_db(data):
    for player in data:
        new_data = PlayerData(player_id = player['playerId'],
                            player_name = player['playerName'],
                            position = player['position'],
                            team = player['team'],
                            season = player['season'],
                            num_of_games = player['games'],
                            field_goals = player['fieldGoals'],
                            field_attempts = player['fieldAttempts'],
                            field_percent = player['fieldPercent'],
                            three_fg = player['threeFg'],
                            three_attempts = player['threeAttempts'],
                            three_percent = player['threePercent'],
                            two_fg = player['twoFg'],
                            two_attempts = player['twoAttempts'],
                            two_percent = player['twoPercent'],
                            turnovers = player['turnovers'],
                            assists = player['assists'],
                            points = player['points'])
        db.session.add(new_data)
    db.session.commit()





