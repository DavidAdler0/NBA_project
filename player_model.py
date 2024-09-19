
from flask_sqlalchemy import SQLAlchemy
from db import db
import requests


class PlayerData(db.Model):
    __tablename__ = 'all_players_data'
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.String(80), nullable=False)
    player_name = db.Column(db.String(80), nullable=False)
    position = db.Column(db.String(80), nullable=False)
    team = db.Column(db.String(80), nullable=True)
    season = db.Column(db.String(80), nullable=True)
    num_of_games = db.Column(db.Integer, nullable=True)

    field_goals = db.Column(db.Integer, nullable=True)
    field_attempts = db.Column(db.Integer, nullable=True)
    field_percent = db.Column(db.Integer, nullable=True)
    three_fg = db.Column(db.Integer, nullable=True)
    three_attempts = db.Column(db.Integer, nullable=True)
    three_percent = db.Column(db.Integer, nullable=True)
    two_fg = db.Column(db.Integer, nullable=True)
    two_attempts = db.Column(db.Integer, nullable=True)
    two_percent = db.Column(db.Integer, nullable=True)

    turnovers = db.Column(db.Integer, nullable=True)
    assists = db.Column(db.Integer, nullable=True)
    points = db.Column(db.Integer, nullable=True)

    atr = db.Column(db.Integer, nullable=True)
    ppg = db.Column(db.Integer, nullable=True)
    ppg_ratio = db.Column(db.Integer, nullable=True)


    def to_dict(self):
        return   {
                    "id": self.id,
                    "playerName": self.player_name,
                    "position": self.position,
                    "games": self.num_of_games,
                    "fieldGoals": self.field_goals,
                    "fieldAttempts": self.field_attempts,
                    "fieldPercent": self.field_percent,
                    "threeFg": self.three_fg,
                    "threeAttempts": self.three_attempts,
                    "threePercent": self.three_percent,
                    "twoFg": self.two_fg,
                    "twoAttempts": self.two_attempts,
                    "twoPercent": self.two_percent,
                    "assists": self.assists,
                    "turnovers": self.turnovers,
                    "points": self.points,
                    "team": self.team,
                    "season": self.season,
                    "playerId": self.player_id,
                  }



