from symbol import parameters
from sys import prefix

from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError

from init_data_service import update_data_to_db, get_season_data_from_API
from player_model import PlayerData

init_blueprint = Blueprint('init_blueprint', __name__, url_prefix='/api/players')

# @init_blueprint.route('/')
# def init_data():
#     update_data_to_db(get_season_data_from_API(2024))
#     update_data_to_db(get_season_data_from_API(2023))
#     update_data_to_db(get_season_data_from_API(2022))
#     res = list(map(lambda player: player.to_dict(), PlayerData.query.all()))
#     return jsonify(res)
# fix route, condition with none, validation an errors
@init_blueprint.route('/', methods=['GET'])
def gat_players_by_position():
    positions = ['PG', 'SG', 'SF', 'PF', 'C']
    if request.args.get('position') not in positions:
        return "no such position", 405
    if request.args.get('position') is None:
        return "no position received", 405
    position = request.args.get('position')
    season = request.args.get('season')
    if season is None:
        filtered_players = list(filter(lambda player: player.position == position, PlayerData.query.all()))
    else:
        filtered_players = list(filter(lambda player: player.position == position and player.season == season, PlayerData.query.all()))
    res = list(map(lambda player: player.to_dict(), filtered_players))
    return jsonify(res)

