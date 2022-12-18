from marshmallow import Schema, fields
from project.setup_db import db


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    wins_count = db.Column(db.Integer(), default=0)
    loses_count = db.Column(db.Integer(), default=0)


class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    email = fields.Email()
    password = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
    wins_count = fields.Int()
    loses_count = fields.Int()
