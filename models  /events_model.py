from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

class Event(db.Model):
    id = db.Column(db.BigInteger().with_variant(db.Integer, "sqlite"), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(40), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
