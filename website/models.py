from flask_login import UserMixin
from sqlalchemy.sql import func
from . import db


class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(1000))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    stock_1 = db.Column(db.String(50))
    percentage_difference_limit = db.Column(db.Float, default=2.0)
    stock_2 = db.Column(db.String(50))
    stock_3 = db.Column(db.String(50))
    stock_4 = db.Column(db.String(50))
    stock_5 = db.Column(db.String(50))


    def get_id(self):
        return str(self.user_id)
