from symbol import parameters
from sys import prefix

from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError

from get_pleyers_service import display_generated_players
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
def get_players_by_position():
    positions = ['PG', 'SG', 'SF', 'PF', 'C']
    if request.args.get('position') not in positions:
        return "no such position", 405
    if request.args.get('position') is None:
        return "no position received", 405
    position = request.args.get('position')
    season = request.args.get('season')
    res = display_generated_players(position, season)
    return jsonify(res)

