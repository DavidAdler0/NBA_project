from flask import Flask

from init_blueprint import init_blueprint

from db import db
from init_data_service import update_data_to_db, get_season_data_from_API
from player_model import PlayerData

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///NBA.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db.init_app(app)
with app.app_context():
    db.create_all()

app.register_blueprint(blueprint=init_blueprint)

app.run(debug=True)

