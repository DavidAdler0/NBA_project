from itertools import groupby

from player_model import PlayerData

def find_all_seasons(player_id):
    all_data_of_player = list(filter(lambda x: x.player_id == player_id, PlayerData.query.all()))
    sorted_data_of_player = sorted(all_data_of_player, key=lambda x: x.season)
    players_seasons = []
    for season, season_group in groupby(sorted_data_of_player, key=lambda data: data.season):
        players_seasons.append(season)
        return players_seasons

def calculate_atr(obj):
    if obj.turnovers == 0:
        return obj.assists
    return obj.assists/obj.turnovers

def calculate_ppg(players_list):
    num_of_games = len(players_list)
    all_points = sum(map(lambda x: x.points, players_list))
    return all_points/num_of_games

def calculate_average_ppg(players_list):
    sorted_data = sorted(players_list, key=lambda player: player.player_id)
    all_ppg = []
    for player_id, player_group in groupby(sorted_data, key=lambda player: player.player_id):
        ppg = calculate_ppg(list(player_group))
        all_ppg.append(ppg)
    return sum(all_ppg)/len(all_ppg)

def calculate_ppg_ratio(players_list, all_players_list):
    players_avg_ppg = calculate_ppg(players_list)
    avg_ppg = calculate_average_ppg(all_players_list)
    return players_avg_ppg/avg_ppg


def display_generated_players(position, season = None):
    if season is None:
        filtered_players = list(filter(lambda player: player.position == position, PlayerData.query.all()))
    else:
        filtered_players = list(filter(lambda player: player.position == position and player.season == season, PlayerData.query.all()))
    sorted_data = sorted(filtered_players, key=lambda player: player.player_id)
    generated_players = []
    for player_id, player_group in groupby(sorted_data, key=lambda player: player.player_id):
        players_list = list(player_group)
        players_info = players_list[0]
        player_to_display = {'playerName': player_id,
            'team': players_info.team,
            'position': players_info.position,
            'listOfSeason': find_all_seasons(players_info.player_id),
            'points': players_info.points,
            'games': players_info.num_of_games,
            'twoPercent': players_info.two_percent,
            'threePercent': players_info.three_percent,
            'ATR': calculate_atr(players_info),
            'PPG Ratio': calculate_ppg_ratio(players_list, sorted_data),}
        generated_players.append(player_to_display)
    return generated_players